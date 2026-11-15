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

2023 a 2025 ficam no catálogo estático. De 2026 em diante o ``sync`` usa os links
descobertos (:func:`entries_for_group`), e só cai para a URL presumida do catálogo
quando a página não responde, com aviso no log.
"""

from __future__ import annotations

import datetime as dt
import logging
import re
from collections.abc import Iterable
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
    "apply_links",
    "classify_href",
    "discover",
    "entries_for_group",
    "extract_links",
    "fetch_links",
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
_DATA_EXTS = {"csv", "xlsx", "xls", "zip"}


@dataclass(frozen=True, order=True)
class ShpcLink:
    """Link mensal do SHPC classificado."""

    year: int
    month: int
    product: str
    url: str
    ext: str

    @property
    def group(self) -> str:
        """Grupo do catálogo ao qual o link pertence."""
        return SHPC_MONTHLY_PRODUCTS[self.product][0]


def classify_href(href: str, *, base_url: str = SHPC_PAGE_URL) -> ShpcLink | None:
    """Classifica um ``href`` do SHPC mensal em (ano, mês, produto).

    Args:
        href: Valor do atributo ``href`` (absoluto ou relativo à página).
        base_url: URL da página, para resolver ``href`` relativo.

    Returns:
        ShpcLink | None: O link classificado; ``None`` fora de ``shpc/dsan/{ano}/``,
        com mês inválido ou nome que não segue nenhuma das duas regras.
    """
    url = urljoin(base_url, href.strip())
    path = urlsplit(url).path
    found = _DSAN_PATH.search(path)
    if found is None:
        return None
    year = int(found.group(1))
    name = unquote(found.group(2))
    match = _NAME_NEW.match(name) or _NAME_OLD.match(name)
    if match is None:
        return None
    month = int(match.group("month"))
    if not 1 <= month <= 12:
        return None
    ext = (match.group("ext") or "").lower()
    if ext not in _DATA_EXTS:
        # Sem extensão (abril de 2026) o arquivo é servido como CSV.
        ext = "csv"
    return ShpcLink(
        year=year,
        month=month,
        product=match.group("product").lower(),
        url=url.split("#", 1)[0],
        ext=ext,
    )


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


def extract_links(html: str, *, base_url: str = SHPC_PAGE_URL) -> list[ShpcLink]:
    """Extrai e classifica os links mensais do SHPC de uma página HTML.

    Args:
        html: Conteúdo da página.
        base_url: URL da página, para resolver ``href`` relativo.

    Returns:
        list[ShpcLink]: Links únicos, ordenados por (ano, mês, produto).
    """
    parser = _AnchorParser()
    parser.feed(html)
    links = {
        link
        for href in parser.hrefs
        if (link := classify_href(href, base_url=base_url)) is not None
    }
    return sorted(links)


def fetch_links(
    client: Any | None = None, *, url: str = SHPC_PAGE_URL
) -> list[ShpcLink]:
    """Baixa a página do SHPC e devolve os links mensais.

    Args:
        client: ``HttpClient`` do core; se ``None``, cria um (cabeçalhos de navegador).
        url: URL da página.

    Returns:
        list[ShpcLink]: Links classificados.

    Raises:
        RuntimeError: Se a página não trouxer nenhum link mensal (página de erro,
            troca de layout): vazio não pode virar "nenhum mês publicado".
    """
    html = _download_page(client, url)
    links = extract_links(html, base_url=url)
    if not links:
        raise RuntimeError(
            f"a página do SHPC não trouxe nenhum link mensal de {url} "
            "(layout mudou ou resposta de erro)"
        )
    return links


def _download_page(client: Any | None, url: str) -> str:
    from quantilica.core.http import HttpClient

    own = client is None
    http = client or HttpClient(timeout=60.0, attempts=3, emulate_browser=True)
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
    pelos da página (e perdem ``fallback_urls``, que só valiam para a URL presumida);
    meses da página que o catálogo não tem entram como entradas novas. Entradas sem
    link na página ficam como estão, com a URL presumida. Anos anteriores nunca mudam.

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
    result: list[DatasetEntry] = []
    seen: set[tuple[int | None, int | None]] = set()
    for entry in entries:
        key = (entry["year"], entry["month"])
        seen.add(key)
        link = by_month.get(key)  # type: ignore[arg-type]
        if link is None:
            result.append(entry)
            continue
        found = DatasetEntry(**{**entry, "url": link.url, "ext": link.ext})
        found.pop("fallback_urls", None)  # type: ignore[misc]
        result.append(found)
    for key, link in sorted(by_month.items()):
        if key not in seen:
            result.append(
                shpc_monthly_entry(
                    link.product, link.year, link.month, link.url, link.ext
                )
            )
    result.sort(key=lambda e: (e["year"] or 0, e["month"] or 0))
    return result


# ---------------------------------------------------------------------------
# Uso pelo sync: uma consulta por processo, com reserva se a página falhar.
# ---------------------------------------------------------------------------

_cache: dict[str, Any] = {}


def reset_cache() -> None:
    """Esquece a página consultada (para testes)."""
    _cache.clear()


def _page_links() -> list[ShpcLink] | None:
    """Links da página, consultados uma vez por processo; ``None`` se falhou."""
    if "links" not in _cache:
        try:
            _cache["links"] = fetch_links()
        except Exception as exc:  # rede, HTTP, layout: cai para a URL presumida
            logger.warning(
                "SHPC: não consegui ler os links da página da ANP (%s); "
                "usando as URLs presumidas do catálogo para %d em diante, "
                "que podem dar 404 em meses com nome fora do padrão.",
                exc,
                DISCOVER_FROM_YEAR,
            )
            _cache["links"] = None
    return _cache["links"]


def entries_for_group(group: str, entries: list[DatasetEntry]) -> list[DatasetEntry]:
    """Entradas do ``group`` com os links descobertos, se ele é um grupo mensal do SHPC.

    Args:
        group: Id canônico do grupo.
        entries: Entradas do catálogo estático.

    Returns:
        list[DatasetEntry]: As mesmas entradas para qualquer outro grupo ou se a página
        falhar; nos três grupos mensais, as de :func:`apply_links`.
    """
    if group not in {g for g, _ in SHPC_MONTHLY_PRODUCTS.values()}:
        return entries
    links = _page_links()
    if links is None:
        return entries
    return apply_links(entries, links, group=group)


# ---------------------------------------------------------------------------
# Relatório do comando ``anp discover``.
# ---------------------------------------------------------------------------


@dataclass
class DiscoverReport:
    """Resultado de :func:`discover`."""

    new_months: list[dict[str, Any]] = field(default_factory=list)
    late: list[dict[str, Any]] = field(default_factory=list)
    url_differs: list[dict[str, Any]] = field(default_factory=list)
    known: int = 0

    @property
    def has_changes(self) -> bool:
        """Há mês publicado fora do catálogo ou mês anterior atrasado."""
        return bool(self.new_months or self.late)

    def to_dict(self) -> dict[str, Any]:
        """Converte o relatório em dict serializável."""
        data = asdict(self)
        data["has_changes"] = self.has_changes
        return data


def _today() -> dt.date:
    return dt.date.today()


def _previous_month(today: dt.date) -> tuple[int, int]:
    return (today.year - 1, 12) if today.month == 1 else (today.year, today.month - 1)


def discover(
    links: Iterable[ShpcLink] | None = None,
    *,
    catalog: Iterable[DatasetEntry] | None = None,
    today: dt.date | None = None,
    client: Any | None = None,
) -> DiscoverReport:
    """Compara os links da página com o catálogo estático do SHPC mensal.

    Args:
        links: Links já extraídos; se ``None``, baixa a página.
        catalog: Entradas do catálogo estático dos três grupos mensais; se ``None``,
            usa o catálogo do pacote.
        today: Data de referência (para o aviso de atraso); padrão, hoje.
        client: ``HttpClient`` (só se ``links`` for ``None``).

    Returns:
        DiscoverReport: ``new_months`` (na página, fora do catálogo), ``late`` (mês
        anterior ao corrente ausente da página depois do dia 15) e ``url_differs`` (a
        página usa um nome diferente do presumido pelo catálogo; o sync usa o da
        página).

    Raises:
        RuntimeError: Se a página não trouxer links (``links`` omitido).
    """
    if links is None:
        links = fetch_links(client)
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

    report = DiscoverReport(known=len(links))
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
