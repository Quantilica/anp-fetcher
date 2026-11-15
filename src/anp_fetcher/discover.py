"""Descoberta dos links mensais do SHPC na página da ANP.

A ANP publica os arquivos mensais da série histórica de preços (``shpc/dsan``) sem
padrão fixo de nome: em 2026, abril veio sem extensão, junho, agosto e setembro
repetem ``AAAA-MM`` no meio, fevereiro tem um erro de digitação e outubro virou
``10-glp.csv``. Em vez de manter uma tabela de exceções no catálogo, este módulo lê a
página "Série histórica de preços de combustíveis", extrai os ``href`` sob
``shpc/dsan/{ano}/`` e classifica cada um por (ano, mês, produto) com uma regra
tolerante:

- mês no início do nome (``MM-``), produto (``glp``, ``diesel-gnv`` ou
  ``gasolina-etanol``) no fim, extensão opcional e qualquer coisa no meio (``AAAA-MM``
  repetido, ``dados-abertos-precos``, erros de digitação);
- ou o padrão antigo ``precos-{produto}-MM`` (2023 a 2025).

Link de ``shpc/dsan`` que nenhuma regra classifica (``2026-11-glp.csv``,
``11-glp-p13.csv``) ou cujo ``AAAA-MM`` não bate com a pasta e o mês não é descartado em
silêncio: vai para ``ShpcPage.unclassified``, o ``sync`` avisa no log e ``anp discover``
o lista como mudança.

2023 a 2025 ficam no catálogo estático. De 2026 em diante o ``sync`` usa os links
descobertos (:func:`entries_for_group`), e só cai para a URL presumida do catálogo
quando a página não responde ou não lista o arquivo, sempre com aviso no log.
"""

from __future__ import annotations

import contextvars
import datetime as dt
import logging
import re
import time
from collections.abc import Iterable, Iterator
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from html.parser import HTMLParser
from typing import Any
from urllib.parse import unquote, urljoin, urlsplit

from ._catalog_base import DatasetEntry
from .catalog_dados_abertos import SHPC_MONTHLY_PRODUCTS, shpc_monthly_entry

__all__ = [
    "DISCOVER_FROM_YEAR",
    "SHPC_PAGE_URL",
    "DiscoverReport",
    "ShpcLink",
    "ShpcPage",
    "apply_links",
    "classify_href",
    "discover",
    "discovery_disabled",
    "entries_for_group",
    "extract_links",
    "extract_page",
    "fetch_links",
    "fetch_page",
    "reset_cache",
]

logger = logging.getLogger(__name__)

SHPC_PAGE_URL = (
    "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/"
    "serie-historica-de-precos-de-combustiveis"
)

# Primeiro ano em que o sync usa os links da página (antes, o catálogo estático).
DISCOVER_FROM_YEAR = 2026

# Dia do mês depois do qual a falta do mês anterior na página vira aviso de atraso.
LATE_AFTER_DAY = 15

_PRODUCTS = "|".join(sorted(SHPC_MONTHLY_PRODUCTS, key=len, reverse=True))
_DSAN_PATH = re.compile(r"/shpc/dsan/(\d{4})/([^/?#]+)$")
# Mês no início, produto no fim, extensão opcional, o resto livre.
_NAME_NEW = re.compile(
    rf"^(?P<month>\d{{2}})(?:[-_.].*?)?[-_.](?P<product>{_PRODUCTS})"
    r"(?:\.(?P<ext>[A-Za-z0-9]+))?$",
    re.IGNORECASE,
)
# Padrão antigo (2023-2025): precos-{produto}-MM.csv
_NAME_OLD = re.compile(
    rf"^precos-(?P<product>{_PRODUCTS})-(?P<month>\d{{2}})(?:\.(?P<ext>[A-Za-z0-9]+))?$",
    re.IGNORECASE,
)
_YEAR_MONTH = re.compile(r"(?<!\d)(\d{4})[-_](\d{2})(?!\d)")
_DATA_EXTS = {"csv", "xlsx", "xls", "zip"}
# Em duplicata do mês, o csv é o arquivo de dados; os outros ficam de reserva.
_EXT_RANK = {"csv": 0, "xlsx": 1, "zip": 2, "xls": 3}

# Falha da página: nova tentativa só depois disto (segundos), para o ``sync`` e o
# ``check`` não esperarem o tempo limite uma vez por grupo sem rede.
FAILURE_RETRY_SECONDS = 300.0
_PAGE_TIMEOUT = 20.0
_PAGE_ATTEMPTS = 2


@dataclass(frozen=True, order=True)
class ShpcLink:
    """Link mensal do SHPC classificado.

    ``fallbacks`` guarda os outros arquivos do mesmo mês (xlsx, zip...) quando a página
    lista mais de um; ``url`` é sempre o de maior preferência (csv, xlsx, zip, xls).
    """

    year: int
    month: int
    product: str
    url: str
    ext: str
    fallbacks: tuple[str, ...] = ()

    @property
    def group(self) -> str:
        """Grupo do catálogo ao qual o link pertence."""
        return SHPC_MONTHLY_PRODUCTS[self.product][0]


@dataclass(frozen=True)
class ShpcPage:
    """O que a página do SHPC trouxe.

    Attributes:
        links: Links mensais classificados, um por (ano, mês, produto).
        unclassified: URLs de ``shpc/dsan/{ano}/`` (de ``DISCOVER_FROM_YEAR`` em diante,
            com extensão de dados ou sem extensão) que nenhuma regra classificou, ou
            cujo ``AAAA-MM`` não bate com a pasta e o mês do nome.
    """

    links: list[ShpcLink] = field(default_factory=list)
    unclassified: list[str] = field(default_factory=list)


def _classify(href: str, base_url: str) -> tuple[str, ShpcLink | None, int]:
    """``(status, link, ano)``; status: other, ignored, unclassified ou ok."""
    url = urljoin(base_url, href.strip()).split("#", 1)[0]
    found = _DSAN_PATH.search(urlsplit(url).path)
    if found is None:
        return "other", None, 0
    year = int(found.group(1))
    name = unquote(found.group(2))
    ext = name.rsplit(".", 1)[1].lower() if "." in name else ""
    if ext and ext not in _DATA_EXTS:
        return "ignored", None, year  # pdf, ods, dicionário: não é arquivo de dados
    match = _NAME_NEW.match(name) or _NAME_OLD.match(name)
    if match is None:
        return "unclassified", None, year
    month = int(match.group("month"))
    if not 1 <= month <= 12:
        return "unclassified", None, year
    # Um AAAA-MM no nome tem de bater com a pasta e com o mês do início.
    if any((int(y), int(m)) != (year, month) for y, m in _YEAR_MONTH.findall(name)):
        return "unclassified", None, year
    link = ShpcLink(
        year=year,
        month=month,
        product=match.group("product").lower(),
        url=url,
        # Sem extensão (abril de 2026) o arquivo é servido como CSV.
        ext=ext or "csv",
    )
    return "ok", link, year


def classify_href(href: str, *, base_url: str = SHPC_PAGE_URL) -> ShpcLink | None:
    """Classifica um ``href`` do SHPC mensal em (ano, mês, produto).

    Args:
        href: Valor do atributo ``href`` (absoluto ou relativo à página).
        base_url: URL da página, para resolver ``href`` relativo.

    Returns:
        ShpcLink | None: O link classificado; ``None`` fora de ``shpc/dsan/{ano}/``,
        com extensão que não é de dados, mês inválido, ``AAAA-MM`` que não bate com a
        pasta e o mês, ou nome que não segue nenhuma das duas regras.
    """
    return _classify(href, base_url)[1]


class _AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value:
                self.hrefs.append(value)


def _best_per_month(links: Iterable[ShpcLink]) -> list[ShpcLink]:
    """Um link por (ano, mês, produto): csv > xlsx > zip > xls; o resto vira reserva."""
    grouped: dict[tuple[int, int, str], dict[str, ShpcLink]] = {}
    for link in links:
        grouped.setdefault((link.year, link.month, link.product), {})[link.url] = link
    chosen: list[ShpcLink] = []
    for candidates in grouped.values():
        ranked = sorted(
            candidates.values(), key=lambda lk: (_EXT_RANK.get(lk.ext, 9), lk.url)
        )
        first, rest = ranked[0], ranked[1:]
        chosen.append(
            ShpcLink(
                first.year,
                first.month,
                first.product,
                first.url,
                first.ext,
                tuple(lk.url for lk in rest),
            )
        )
    return sorted(chosen)


def extract_page(html: str, *, base_url: str = SHPC_PAGE_URL) -> ShpcPage:
    """Extrai e classifica os links mensais do SHPC de uma página HTML.

    Args:
        html: Conteúdo da página.
        base_url: URL da página, para resolver ``href`` relativo.

    Returns:
        ShpcPage: Links ordenados por (ano, mês, produto) e os hrefs não classificados.
    """
    parser = _AnchorParser()
    parser.feed(html)
    links: list[ShpcLink] = []
    unclassified: set[str] = set()
    for href in dict.fromkeys(parser.hrefs):
        status, link, year = _classify(href, base_url)
        if link is not None:
            links.append(link)
        elif status == "unclassified" and year >= DISCOVER_FROM_YEAR:
            unclassified.add(urljoin(base_url, href.strip()).split("#", 1)[0])
    return ShpcPage(_best_per_month(links), sorted(unclassified))


def extract_links(html: str, *, base_url: str = SHPC_PAGE_URL) -> list[ShpcLink]:
    """Como :func:`extract_page`, só os links classificados."""
    return extract_page(html, base_url=base_url).links


def fetch_page(client: Any | None = None, *, url: str = SHPC_PAGE_URL) -> ShpcPage:
    """Baixa a página do SHPC e devolve o que ela traz.

    Args:
        client: ``HttpClient`` do core; se ``None``, cria um (cabeçalhos de navegador).
        url: URL da página.

    Returns:
        ShpcPage: Links classificados e hrefs não classificados.

    Raises:
        RuntimeError: Se a página não trouxer nenhum link mensal (página de erro,
            troca de layout), ou nenhum de ``DISCOVER_FROM_YEAR`` em diante estando o
            ano corrente nesse intervalo (layout mudou só no bloco recente): vazio não
            pode virar "nenhum mês publicado".
    """
    page = extract_page(_download_page(client, url), base_url=url)
    if not page.links:
        raise RuntimeError(
            f"a página do SHPC não trouxe nenhum link mensal de {url} "
            "(layout mudou ou resposta de erro)"
        )
    if _today().year >= DISCOVER_FROM_YEAR and not any(
        link.year >= DISCOVER_FROM_YEAR for link in page.links
    ):
        raise RuntimeError(
            f"a página do SHPC não lista nenhum arquivo de {DISCOVER_FROM_YEAR} em "
            f"diante em {url} (layout mudou no bloco recente?)"
        )
    return page


def fetch_links(
    client: Any | None = None, *, url: str = SHPC_PAGE_URL
) -> list[ShpcLink]:
    """Como :func:`fetch_page`, só os links classificados."""
    return fetch_page(client, url=url).links


def _download_page(client: Any | None, url: str) -> str:
    from quantilica.core.http import HttpClient

    own = client is None
    http = client or HttpClient(
        timeout=_PAGE_TIMEOUT, attempts=_PAGE_ATTEMPTS, emulate_browser=True
    )
    try:
        return http.get_text(url)
    finally:
        if own:
            http.close()


def apply_links(
    entries: Iterable[DatasetEntry],
    links: Iterable[ShpcLink],
    *,
    group: str,
    from_year: int = DISCOVER_FROM_YEAR,
) -> list[DatasetEntry]:
    """Aplica os links descobertos às entradas de um grupo mensal do SHPC.

    Entradas de ``from_year`` em diante que a página lista trocam ``url`` e ``ext``
    pelos da página; os ``fallback_urls`` passam a ser os outros arquivos do mesmo mês
    na página (e perdem os presumidos). Meses da página que o catálogo não tem entram
    como entradas novas. Entradas sem link na página ficam como estão, com a URL
    presumida. Anos anteriores nunca mudam.

    Args:
        entries: Entradas do grupo, do catálogo.
        links: Links descobertos (de qualquer produto; só os do grupo contam).
        group: Id do grupo (``shpc-diesel-gnv``, ``shpc-gasolina-etanol`` ou
            ``shpc-glp-mensal``).
        from_year: Primeiro ano em que a descoberta vale.

    Returns:
        list[DatasetEntry]: Entradas do grupo, em ordem de (ano, mês).
    """
    by_month = {
        (link.year, link.month): link
        for link in links
        if link.group == group and link.year >= from_year
    }

    def entry_for(link: ShpcLink, base: DatasetEntry | None) -> DatasetEntry:
        if base is None:
            made = shpc_monthly_entry(
                link.product, link.year, link.month, link.url, link.ext
            )
        else:
            made = DatasetEntry(**{**base, "url": link.url, "ext": link.ext})
            made.pop("fallback_urls", None)  # type: ignore[misc]
        if link.fallbacks:
            made["fallback_urls"] = list(link.fallbacks)
        return made

    result: list[DatasetEntry] = []
    seen: set[tuple[int | None, int | None]] = set()
    for entry in entries:
        key = (entry["year"], entry["month"])
        seen.add(key)
        link = by_month.get(key)  # type: ignore[arg-type]
        result.append(entry if link is None else entry_for(link, entry))
    for key, link in sorted(by_month.items()):
        if key not in seen:
            result.append(entry_for(link, None))
    result.sort(key=lambda e: (e["year"] or 0, e["month"] or 0))
    return result


def _today() -> dt.date:
    return dt.date.today()


def _unpublished_from(today: dt.date) -> tuple[int, int]:
    """Primeiro (ano, mês) que a ANP ainda pode não ter publicado em ``today``."""
    if today.day > LATE_AFTER_DAY:
        return today.year, today.month
    return _previous_month(today)


def presumed_months(
    entries: Iterable[DatasetEntry],
    links: Iterable[ShpcLink],
    *,
    group: str,
    today: dt.date | None = None,
    from_year: int = DISCOVER_FROM_YEAR,
) -> list[tuple[int, int]]:
    """Meses de ``from_year`` em diante que ficam com URL presumida (fora da página).

    O mês ainda não publicado (o anterior, até o dia 15; o corrente depois) não conta.
    """
    cutoff = _unpublished_from(today or _today())
    listed = {(lk.year, lk.month) for lk in links if lk.group == group}
    return sorted(
        (e["year"], e["month"])
        for e in entries
        if e["year"] is not None
        and e["month"] is not None
        and e["year"] >= from_year
        and (e["year"], e["month"]) not in listed
        and (e["year"], e["month"]) < cutoff
    )


# ---------------------------------------------------------------------------
# Uso pelo sync: uma consulta por processo, com reserva se a página falhar.
# ---------------------------------------------------------------------------

_cache: dict[str, Any] = {}
_disabled: contextvars.ContextVar[bool] = contextvars.ContextVar(
    "anp_discover_disabled", default=False
)


def reset_cache() -> None:
    """Esquece a página consultada (para testes)."""
    _cache.clear()


@contextmanager
def discovery_disabled() -> Iterator[None]:
    """Dentro do bloco, :func:`entries_for_group` não consulta a página."""
    token = _disabled.set(True)
    try:
        yield
    finally:
        _disabled.reset(token)


def _monotonic() -> float:
    return time.monotonic()


def _page() -> ShpcPage | None:
    """A página, consultada uma vez por processo; ``None`` se falhou.

    A falha não fica para sempre: depois de ``FAILURE_RETRY_SECONDS`` tenta de novo.
    """
    if "page" in _cache:
        return _cache["page"]
    failed_at = _cache.get("failed_at")
    if failed_at is not None and _monotonic() - failed_at < FAILURE_RETRY_SECONDS:
        return None
    try:
        page = fetch_page()
    except Exception as exc:  # rede, HTTP, layout: cai para a URL presumida
        logger.warning(
            "SHPC: não consegui ler os links da página da ANP (%s); "
            "usando as URLs presumidas do catálogo para %d em diante, "
            "que podem dar 404 em meses com nome fora do padrão.",
            exc,
            DISCOVER_FROM_YEAR,
        )
        _cache["failed_at"] = _monotonic()
        return None
    _cache.pop("failed_at", None)
    _cache["page"] = page
    if page.unclassified:
        logger.warning(
            "SHPC: %d link(s) de shpc/dsan que a regra de nomes não reconhece, "
            "ignorados no sync (veja `anp discover`): %s",
            len(page.unclassified),
            ", ".join(page.unclassified[:5])
            + (" ..." if len(page.unclassified) > 5 else ""),
        )
    return page


def entries_for_group(group: str, entries: list[DatasetEntry]) -> list[DatasetEntry]:
    """Entradas do ``group`` com os links descobertos, se ele é um grupo mensal do SHPC.

    Args:
        group: Id canônico do grupo.
        entries: Entradas do catálogo estático.

    Returns:
        list[DatasetEntry]: As mesmas entradas para qualquer outro grupo, dentro de
        :func:`discovery_disabled` ou se a página falhar; nos três grupos mensais, as
        de :func:`apply_links`. Meses de 2026 em diante que a página não lista seguem
        com a URL presumida, com aviso no log.
    """
    if group not in {g for g, _ in SHPC_MONTHLY_PRODUCTS.values()} or _disabled.get():
        return entries
    page = _page()
    if page is None:
        return entries
    missing = presumed_months(entries, page.links, group=group)
    if missing:
        logger.warning(
            "SHPC: %s: a página não lista %d arquivo(s) de %d em diante; ficam com a "
            "URL presumida (podem dar 404): %s",
            group,
            len(missing),
            DISCOVER_FROM_YEAR,
            ", ".join(f"{y}-{m:02d}" for y, m in missing[:6])
            + (" ..." if len(missing) > 6 else ""),
        )
    return apply_links(entries, page.links, group=group)


# ---------------------------------------------------------------------------
# Relatório do comando ``anp discover``.
# ---------------------------------------------------------------------------


@dataclass
class DiscoverReport:
    """Resultado de :func:`discover`."""

    new_months: list[dict[str, Any]] = field(default_factory=list)
    late: list[dict[str, Any]] = field(default_factory=list)
    url_differs: list[dict[str, Any]] = field(default_factory=list)
    unclassified: list[str] = field(default_factory=list)
    known: int = 0

    @property
    def has_changes(self) -> bool:
        """Há mês fora do catálogo, mês anterior atrasado ou link não reconhecido."""
        return bool(self.new_months or self.late or self.unclassified)

    def to_dict(self) -> dict[str, Any]:
        """Converte o relatório em dict serializável."""
        data = asdict(self)
        data["has_changes"] = self.has_changes
        return data


def _previous_month(today: dt.date) -> tuple[int, int]:
    return (today.year - 1, 12) if today.month == 1 else (today.year, today.month - 1)


def discover(
    links: Iterable[ShpcLink] | None = None,
    *,
    unclassified: Iterable[str] = (),
    catalog: Iterable[DatasetEntry] | None = None,
    today: dt.date | None = None,
    client: Any | None = None,
) -> DiscoverReport:
    """Compara os links da página com o catálogo estático do SHPC mensal.

    Args:
        links: Links já extraídos; se ``None``, baixa a página.
        unclassified: Hrefs não classificados que acompanham ``links``.
        catalog: Entradas do catálogo estático dos três grupos mensais; se ``None``,
            usa o catálogo do pacote.
        today: Data de referência (para o aviso de atraso); padrão, hoje.
        client: ``HttpClient`` (só se ``links`` for ``None``).

    Returns:
        DiscoverReport: ``new_months`` (na página, fora do catálogo), ``late`` (mês
        anterior ao corrente ausente da página depois do dia 15), ``unclassified``
        (links de ``shpc/dsan`` que a regra não reconhece) e ``url_differs`` (a página
        usa um nome diferente do presumido pelo catálogo; o sync usa o da página).

    Raises:
        RuntimeError: Se a página não trouxer links (``links`` omitido).
    """
    if links is None:
        page = fetch_page(client)
        links, unclassified = page.links, page.unclassified
    links = list(links)
    if catalog is None:
        from .catalog import list_datasets

        catalog = [
            entry
            for group, _ in SHPC_MONTHLY_PRODUCTS.values()
            for entry in list_datasets(group)
        ]
    in_catalog = {(e["group"], e["year"], e["month"]): e for e in catalog}
    today = today or _today()

    report = DiscoverReport(known=len(links), unclassified=sorted(unclassified))
    for link in links:
        entry = in_catalog.get((link.group, link.year, link.month))
        if entry is None:
            report.new_months.append(
                {
                    "group": link.group,
                    "year": link.year,
                    "month": link.month,
                    "url": link.url,
                }
            )
        elif link.year >= DISCOVER_FROM_YEAR and entry["url"] != link.url:
            report.url_differs.append(
                {
                    "group": link.group,
                    "year": link.year,
                    "month": link.month,
                    "catalogo": entry["url"],
                    "pagina": link.url,
                }
            )

    if today.day > LATE_AFTER_DAY:
        year, month = _previous_month(today)
        if year >= DISCOVER_FROM_YEAR:
            on_page = {(link.product, link.year, link.month) for link in links}
            for product, (group, _) in SHPC_MONTHLY_PRODUCTS.items():
                if (product, year, month) not in on_page:
                    report.late.append({"group": group, "year": year, "month": month})
    return report
