"""Convert raw ANP open data into the Hive-partitioned lake.

Each raw file lands in
``<lake>/anp/<group>/[ano=<ano>/][mes=<mes>/]<file_key>.parquet``.
Monthly datasets (e.g. Preços de Combustíveis) are partitioned by ``ano=/mes=``;
annual statistical reports by ``ano=``; and static datasets are stored unpartitioned.
Data contracts are validated and cast when available.

Um ZIP com vários membros de dados rende um Parquet por membro
(``<zip>__<membro>.parquet``); ver :func:`route_group`.
"""

from __future__ import annotations

import glob
import logging
import re
import tempfile
import threading
import unicodedata
import zipfile
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

try:
    import polars as pl
    import pyarrow.parquet as pq
    from quantilica.analytics import lake as analytics_lake
    from quantilica.analytics.lake import META_FILE_KEY, LakeWriter
    from quantilica.core.files import sha256_file
    from quantilica.core.lake import (
        DatasetDescriptor,
        composite_file_key,
        file_key,
        partition_types_for,
    )
except ImportError as exc:
    raise ImportError(
        "anp_fetcher.lake requer o extra 'analysis': "
        "uv add 'anp-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

from anp_fetcher import __version__
from anp_fetcher.catalog import ALL_GROUP_KEYS, resolve_group
from anp_fetcher.reader import (
    decompress,
    extract_zip_member,
    normalize_dtypes,
    parse_filename,
    read_file,
    scratch_dir,
    zip_data_members,
)
from anp_fetcher.storage import _GROUP_DIRS
from anp_fetcher.wrangling import _apply_contract, spec_for

if TYPE_CHECKING:  # só tipagem: o core publicado antes do contrato não tem Planned
    from quantilica.core.lake import Planned

SOURCE_ID = "anp"

logger = logging.getLogger(__name__)

_YM = re.compile(r"^(?P<ano>\d{4})-(?P<mes>\d{2})$")
_YS = re.compile(r"^(?P<ano>\d{4})-S(?P<semestre>[12])$")
_Y = re.compile(r"^(?P<ano>\d{4})$")


@dataclass
class ConvertResult:
    """Counts of a conversion run; ``errors`` holds one message per failure.

    ``warnings`` lists what was deliberately left out without failing the run
    (a ZIP member that no declared table covers).
    """

    converted: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


# A ANP publica o mesmo conteúdo em vários formatos ("pmqc-csv_2024-01@...",
# "pmqc-json_2024-01@..."); só um vira Parquet, nesta ordem de preferência.
_FORMAT_TAG = re.compile(r"-(csv|json|xlsx?)(?=_|$)", re.IGNORECASE)
_FORMAT_RANK = {".csv": 0, ".zip": 1, ".7z": 1, ".xlsx": 2, ".xls": 3, ".json": 4}
# Formatos que o conversor sabe ler: direto (csv/json/xls/xlsx) ou depois de
# descompactar (zip/7z com um deles dentro). O resto é documentação, mapa ou
# imagem — o leitor não abre.
_TABULAR_SUFFIXES = frozenset({".csv", ".json", ".xls", ".xlsx", ".zip", ".7z"})
# Sidecar de manifest e resto de escrita interrompida: nunca dados brutos.
_MANIFEST_SUFFIX = ".manifest.json"
_TEMP_SUFFIX = ".tmp"


def is_tabular(path: Path) -> bool:
    """Se o conversor consegue ler o arquivo (``read_file`` ou ``decompress``)."""
    return path.suffix.lower() in _TABULAR_SUFFIXES


def _is_sidecar(path: Path) -> bool:
    """Se o arquivo é sidecar de manifest ou resto ``.tmp``, não dado bruto."""
    return path.name.endswith(_MANIFEST_SUFFIX) or path.name.endswith(_TEMP_SUFFIX)


def raw_files(src_group_dir: Path) -> list[Path]:
    """Arquivos de um diretório de grupo, sem sidecars nem restos ``.tmp``.

    É a descoberta compartilhada por :meth:`LakeConverter.convert` e
    :meth:`LakeConverter.inventory`, para os dois enxergarem o mesmo conjunto.
    """
    return sorted(
        p for p in src_group_dir.iterdir() if p.is_file() and not _is_sidecar(p)
    )


def _format_rank(path: Path) -> tuple[str, int, str]:
    """``(base, rank, stamp)`` de um arquivo: o conteúdo, o formato e a versão.

    O formato vem da extensão, mas a marca ``-json`` no nome (``pmqc-json_...zip``)
    vale mais: a ANP já publicou JSON com extensão ``.zip``, e o CSV é o que fica.
    """
    stem = path.name.split("@", 1)[0].rsplit(".", 1)[0]
    base = _FORMAT_TAG.sub("", stem)
    stamp = path.name.split("@", 1)[1] if "@" in path.name else ""
    tag = _FORMAT_TAG.search(stem)
    if tag and tag.group(1).lower() == "json":
        return base, _FORMAT_RANK[".json"], stamp
    return base, _FORMAT_RANK.get(path.suffix.lower(), 5), stamp


def _best_by_base(files: list[Path]) -> dict[str, tuple[int, str, Path]]:
    """Arquivo escolhido de cada conteúdo: ``base -> (rank, stamp, path)``."""
    best: dict[str, tuple[int, str, Path]] = {}
    for path in files:
        base, rank, stamp = _format_rank(path)
        current = best.get(base)
        # Formato preferido primeiro; no mesmo formato, a versão mais recente.
        if current is None or (rank, current[1]) < (current[0], stamp):
            best[base] = (rank, stamp, path)
    return best


def pick_one_format(files: list[Path]) -> list[Path]:
    """Um arquivo por conteúdo: o formato preferido, na versão mais recente.

    Arquivos da mesma pasta que diferem só no formato (sufixo ``-csv``/``-json`` na
    base e extensão) são o mesmo dado; converter todos duplica linhas no lake.
    """
    return sorted(path for _, _, path in _best_by_base(files).values())


def resolve_partitions(meta: dict[str, Any]) -> tuple[list[str], dict[str, str]]:
    """Determine partition keys and values from filename metadata."""
    partition = meta.get("partition")
    if not partition:
        return [], {}

    m_ys = _YS.match(partition)
    if m_ys:
        return ["ano", "semestre"], {
            "ano": m_ys["ano"],
            "semestre": f"S{m_ys['semestre']}",
        }

    m_ym = _YM.match(partition)
    if m_ym:
        return ["ano", "mes"], {"ano": m_ym["ano"], "mes": m_ym["mes"]}

    m_y = _Y.match(partition)
    if m_y:
        return ["ano"], {"ano": m_y["ano"]}

    return ["particao"], {"particao": partition}


#: ``base_id`` do catálogo -> dataset do lake, para grupos cujos arquivos têm esquemas
#: diferentes e precisam de datasets próprios. Fonte única do roteamento.
DATASET_ROUTES: dict[str, dict[str, str]] = {
    "royalties": {
        "royalties-uniao": "royalties_uniao",
        "royalties-estado": "royalties_estado",
        "royalties-municipio": "royalties_municipio",
        "pe-uniao": "participacoes_especiais",
        "pe-estado": "participacoes_especiais",
        "pe-municipio": "participacoes_especiais",
        "pe-campo": "participacoes_especiais",
        "preco-ref-gn": "preco_referencia_gn",
        "preco-ref-petroleo": "preco_referencia_petroleo",
    },
}

_COARSER_SUFFIX = {("ano",): "-anual", (): "-historico"}


def dataset_for_granularity(
    group: str,
    part_keys: list[str],
    finest: int,
    path: Path | None = None,
) -> str:
    """Dataset de um arquivo num grupo que mistura granularidades.

    Uma tabela Hive precisa da mesma profundidade de partições em todos os arquivos.
    Em ``producao-terra`` convivem séries mensais (``_2000-01``), anuais (``_2016``) e
    históricas (``-1941-1966``): a mais fina fica com o nome do grupo e as demais vão
    para ``<grupo>-anual`` ou ``<grupo>-historico``.
    """
    routes = DATASET_ROUTES.get(group)
    if routes is not None and path is not None:
        # Explícito por ``base_id`` (o do catálogo), nunca por trecho do nome.
        # Base não listada fica no dataset do grupo, sem adivinhação.
        return routes.get(parse_filename(path)["base_id"], group)
    if len(part_keys) >= finest:
        return group
    suffix = _COARSER_SUFFIX.get(tuple(part_keys), "-" + "-".join(part_keys))
    return group + suffix


@dataclass(frozen=True)
class Routed:
    """Um arquivo bruto (ou um membro dele) e o dataset/partição que ``convert`` dá."""

    path: Path
    dataset_id: str
    partition_keys: list[str]
    partition_values: dict[str, str]
    #: membro do ZIP que este item converte; ``None`` = arquivo todo
    member: str | None = None
    #: nome do membro no ``file_key``, único dentro do ZIP (``None`` = ``member``)
    key_name: str | None = None
    #: colunas literais acrescentadas ao Parquet (nome, valor): o que só o nome do
    #: membro diz (``ambiente`` mar/terra/presal)
    literals: tuple[tuple[str, str], ...] = ()
    #: motivo de o item ficar fora do lake (membro sem tabela declarada): ``convert``
    #: avisa e segue, sem erro nem dataset novo
    ignored: str | None = None


@dataclass(frozen=True)
class _Plan:
    """Um arquivo bruto ou um membro dele, antes de escolher o dataset."""

    path: Path
    keys: list[str]
    vals: dict[str, str]
    member: str | None = None
    key_name: str | None = None
    literals: tuple[tuple[str, str], ...] = ()
    #: dataset próprio da tabela (ZIP com layouts diferentes); ``None`` = do grupo
    table: str | None = None
    ignored: str | None = None


_PMQC_MEMBER = re.compile(r"(?P<ano>\d{4})_(?P<mes>\d{2})\.csv$", re.IGNORECASE)


def _pmqc_zip_members(path: Path) -> list[tuple[str, dict[str, str]]]:
    """CSV mensais de um ZIP anual do PMQC: ``(membro, {"ano":…, "mes":…})``."""
    try:
        names = zip_data_members(path)
    except (OSError, zipfile.BadZipFile):
        return []
    members = []
    for name in names:
        m = _PMQC_MEMBER.search(name)
        if m:
            members.append((name, {"ano": m["ano"], "mes": m["mes"]}))
    return members


def _ascii(text: str) -> str:
    """Minúsculas sem acento (``Lâminas`` -> ``laminas``)."""
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
    return folded.decode("ascii").lower()


def _kebab(text: str) -> str:
    """Id em kebab-case ASCII (``Asfalto_Vendas UF`` -> ``asfalto-vendas-uf``)."""
    return re.sub(r"[^0-9a-z]+", "-", _ascii(text)).strip("-")


#: Grupos cujos ZIPs trazem várias tabelas de layouts diferentes (uma por membro):
#: cada tabela vira o dataset ``<grupo>-<tabela>``, para o dataset ter um layout só.
#: Vale para ZIP com mais de um membro de dados; ZIP de um membro fica no grupo.
TABLE_DATASET_GROUPS = ("amostras-rochas-fluidos", "movimentacao-derivados")

#: Tabelas do ``arf-consolidacao-AAAA.zip``: trecho do nome do membro -> sufixo do id.
_ARF_TABLES = (
    ("calha", "calha"),
    ("celula", "celulas"),
    ("fluido", "fluidos"),
    ("lamina", "laminas"),
    ("later", "laterais"),  # lateral / laterais
    ("plugue", "plugues"),
    ("testemunho", "testemunhos"),
)


def _norm(text: str) -> str:
    """Nome sem acento, caixa nem pontuação (``Vendas_UF`` -> ``vendas uf``)."""
    return re.sub(r"[^0-9a-z]+", " ", _ascii(text)).strip()


#: ``movimentacao-derivados``: ZIP (``base_id``) -> ``(padrão, tabela)``. O padrão
#: casa o nome do membro sem acento, caixa nem pontuação; a tabela vira o dataset
#: ``movimentacao-derivados-<tabela>``. Ids curtos e sem ano: os históricos de
#: períodos diferentes (``..._2007_a_2017``, ``..._2018_a_2023``) são a mesma tabela.
#: Fonte única do roteamento, como :data:`DATASET_ROUTES`.
_MDPG_TABLES: dict[str, tuple[tuple[str, str], ...]] = {
    "mdpg-asfalto": (
        (r"^asfalto vendas distribuidor atual$", "asfalto-vendas-distribuidor-atual"),
        (
            r"^asfalto vendas distribuidor uf atual$",
            "asfalto-vendas-distribuidor-uf-atual",
        ),
        (
            r"^asfalto vendas distribuidor historico$",
            "asfalto-vendas-distribuidor-historico",
        ),
    ),
    "mdpg-aviacao": tuple(
        (rf"^aviacao {pat}$", f"aviacao-{tab}")
        for pat, tab in (
            ("entregas distribuidor atual", "entregas-distribuidor-atual"),
            ("entregas fornecedor atual", "entregas-fornecedor-atual"),
            ("entregas historico", "entregas-historico"),
            ("vendas atual", "vendas-atual"),
            ("vendas historico", "vendas-historico"),
            ("vendas uf atual", "vendas-uf-atual"),
        )
    ),
    "mdpg-glp": tuple(
        (rf"^glp {pat}$", f"glp-{tab}")
        for pat, tab in (
            ("entregas distribuidor atual", "entregas-distribuidor-atual"),
            ("entregas fornecedor atual", "entregas-fornecedor-atual"),
            ("entregas historico", "entregas-historico"),
            ("vendas atual", "vendas-atual"),
            ("vendas historico", "vendas-historico"),
            ("vendas uf atual", "vendas-uf-atual"),
        )
    ),
    "mdpg-liquidos": (
        (
            r"^liquidos entregas distribuidor atual$",
            "liquidos-entregas-distribuidor-atual",
        ),
        (
            r"^liquidos entregas fornecedor atual$",
            "liquidos-entregas-fornecedor-atual",
        ),
        (r"^liquidos entregas historico$", "liquidos-entregas-historico"),
        (
            r"^liquidos importacao de distribuidores$",
            "liquidos-importacao-distribuidores",
        ),
        (r"^liquidos vendas atual$", "liquidos-vendas-atual"),
        (
            r"^liquidos vendas historico(?: \d{4} a \d{4})?$",
            "liquidos-vendas-historico",
        ),
    ),
    "mdpg-logistica": (
        # só a edição atual (01, 02, 03): a antiga que ficou no ZIP ("LOGISTICA DO
        # ABASTECIMENTO NACIONAL", "VENDAS CONGENERES...") repete 2022 a 2024
        (r"^dados abertos logistica 0?1\b", "logistica-abastecimento-nacional"),
        (r"^dados abertos logistica 0?2\b", "logistica-vendas-mercado"),
        (r"^dados abertos logistica 0?3\b", "logistica-vendas-congeneres"),
    ),
    "mdpg-lubrificante": ((r"^lubrificante anexo ([a-z])$", "lubrificante-anexo-\\1"),),
    "mdpg-solvente": (
        (r"^solvente vendas dist atual$", "solvente-vendas-distribuidor-atual"),
        (r"^solvente vendas dist historico$", "solvente-vendas-distribuidor-historico"),
        (
            r"^solvente vendas distribuidor uf atual$",
            "solvente-vendas-distribuidor-uf-atual",
        ),
        (r"^solvente vendas prod atual$", "solvente-vendas-produtor-atual"),
        (r"^solvente vendas prod historico$", "solvente-vendas-produtor-historico"),
        (r"^solvente vendas produtor uf atual$", "solvente-vendas-produtor-uf-atual"),
    ),
    "mdpg-trr": (
        (r"^trr vendas dist atual$", "trr-vendas-distribuidor-atual"),
        (r"^trr vendas dist historico$", "trr-vendas-distribuidor-historico"),
        (r"^trr vendas distribuidor uf atual$", "trr-vendas-distribuidor-uf-atual"),
        (r"^trr vendas trr atual$", "trr-vendas-trr-atual"),
        (r"^trr vendas trr historico$", "trr-vendas-trr-historico"),
        (r"^trr vendas trr uf atual$", "trr-vendas-trr-uf-atual"),
    ),
}
#: membros que são só índice/documentação do ZIP: ficam fora do lake
_MDPG_SKIPPED = re.compile(r"^indice\b")


def _mdpg_table(base_id: str, member: str) -> str | None:
    """Tabela (sufixo do dataset) de um membro de ZIP do ``movimentacao-derivados``."""
    name = _norm(Path(member).stem)
    for pattern, table in _MDPG_TABLES.get(base_id, ()):
        found = re.search(pattern, name)
        if found:
            return found.expand(table)
    return None


def table_dataset_for_member(group: str, base_id: str, member: str) -> str | None:
    """Dataset de uma tabela de ZIP de ``TABLE_DATASET_GROUPS``, ou ``None``.

    ``movimentacao-derivados``: o mapa :data:`_MDPG_TABLES` (ZIP + padrão do nome do
    membro) dá o id, p.ex. ``Asfalto_Vendas_Distribuidor_UF_Atual.csv`` ->
    ``movimentacao-derivados-asfalto-vendas-distribuidor-uf-atual``.
    ``amostras-rochas-fluidos``: só o ``arf-consolidacao-*`` tem tabelas
    diferentes (calha, fluidos, lâminas, laterais, plugues, testemunhos, células);
    as depositárias são o mesmo formulário de preços, um por empresa, e vão
    todas para ``amostras-rochas-fluidos-depositarias``.
    """
    stem = Path(member).stem
    if group == "movimentacao-derivados":
        table = _mdpg_table(base_id, member)
        return f"{group}-{table}" if table else None
    if group == "amostras-rochas-fluidos":
        if base_id.startswith("arf-depositarias"):
            return f"{group}-depositarias"
        if base_id.startswith("arf-consolidacao"):
            name = _ascii(stem)
            for needle, suffix in _ARF_TABLES:
                if needle in name:
                    return f"{group}-{suffix}"
    return None


#: Grupos com um arquivo por ambiente (mar, terra, pré-sal) dentro do ZIP.
_AMBIENTE_GROUPS = ("ppg", "producao-poco-abertos")
# o nome pode terminar em "(2)" ou "_1": cópia que a ANP deixou no ZIP
_AMBIENTE = re.compile(r"(?:^|[^a-z])(mar|terra|presal)(?:[ _()-]*\d+[ _()-]*)?$")
_MONTHLY_MEMBER = re.compile(r"^\d{4}_\d{2}_")


def _ambiente(member: str) -> str | None:
    """``mar``, ``terra`` ou ``presal``, o último trecho do nome do membro."""
    found = _AMBIENTE.search(_ascii(Path(member).stem))
    return found.group(1) if found else None


def _drop_monthly_overlap(members: list[str]) -> list[str]:
    """Tira os membros mensais de um ambiente que já tem o anual consolidado.

    Os ZIPs de 2010 a 2015 trazem o ano inteiro (``2013_producao_terra.csv``) e
    o mesmo ano partido em meses (``2013_05_producao_terra.csv``): é o mesmo dado
    duas vezes (os mensais ainda repetem linhas e, em 2010, têm colunas
    deslocadas). Vale o anual.
    """
    annual = {
        _ambiente(m)
        for m in members
        if not _MONTHLY_MEMBER.match(Path(m).name) and _ambiente(m)
    }
    return [
        m
        for m in members
        if not (_MONTHLY_MEMBER.match(Path(m).name) and _ambiente(m) in annual)
    ]


def _unique_key_names(path: Path, members: list[str]) -> dict[str, str]:
    """Nome de cada membro no ``file_key``, sem repetir dentro do ZIP.

    O ``file_key`` usa só o nome do arquivo do membro; dois membros cujos nomes dão
    o mesmo slug (``PETROSYNERGY_2017.csv`` e ``PETROSYNERGY_2017..csv``) ficam
    com o sufixo ``_2``, ``_3`` no nome (antes da extensão), na ordem do nome.
    """
    taken: set[str] = set()
    names: dict[str, str] = {}
    for member in sorted(members):
        name = Path(member).name
        candidate, n = name, 1
        while composite_file_key(path, candidate) in taken:
            n += 1
            candidate = f"{Path(name).stem}_{n}{Path(name).suffix}"
        taken.add(composite_file_key(path, candidate))
        names[member] = candidate
    return names


_NAME_YEAR = re.compile(r"-(\d{4})(?=@|\.)")


def _zip_year(path: Path) -> str | None:
    """O ano no nome do ZIP (``arf-consolidacao-2017@2026….zip`` -> ``2017``)."""
    found = _NAME_YEAR.search(path.name)
    return found.group(1) if found else None


def _zip_parts(group: str, plan: _Plan) -> list[_Plan]:
    """Um item por membro de dados de um ZIP; vazio quando o ZIP vai inteiro.

    O ZIP vai inteiro (como antes) quando tem um membro de dados só, ou nenhum
    (7z, planilha com extensão ``.zip``, ZIP inválido: o erro sai na conversão).
    Com vários membros cada um vira um item, com o ``file_key`` ``<zip>__<membro>``:

    * grupos de produção por poço: o membro leva a coluna ``ambiente`` e o
      ``presal`` vai para o dataset ``<dataset>-presal``;
    * ``movimentacao-derivados``: cada tabela vai para o dataset do mapa
      :data:`_MDPG_TABLES`; membro de índice fica fora e membro que o mapa não
      conhece vira erro do item;
    * ``amostras-rochas-fluidos``: cada tabela do ``arf-consolidacao-AAAA`` e as
      depositárias (que levam a coluna ``membro``: o arquivo é a empresa) vão para
      datasets próprios, partição ``ano=`` tirada do nome do ZIP.
    """
    path = plan.path
    if path.suffix.lower() != ".zip":
        return []
    try:
        members = zip_data_members(path)
    except (OSError, zipfile.BadZipFile):
        return []
    if group in _AMBIENTE_GROUPS:
        members = _drop_monthly_overlap(members)
    if group == "movimentacao-derivados":
        members = [m for m in members if not _MDPG_SKIPPED.match(_norm(Path(m).stem))]
    if len(members) < 2:
        return []
    base_id = parse_filename(path)["base_id"]
    key_names = _unique_key_names(path, members)
    year = _zip_year(path)
    yearly = group == "amostras-rochas-fluidos" and base_id.startswith(
        ("arf-consolidacao", "arf-depositarias")
    )
    keys, vals = (["ano"], {"ano": year}) if yearly and year else (plan.keys, plan.vals)
    parts = []
    for member in members:
        literals: list[tuple[str, str]] = []
        table, ignored = None, None
        if group in _AMBIENTE_GROUPS and (amb := _ambiente(member)):
            literals.append(("ambiente", amb))
        if group in TABLE_DATASET_GROUPS:
            table = table_dataset_for_member(group, base_id, member)
            declared = group == "movimentacao-derivados" or yearly
            if table is None and declared:
                ignored = f"membro sem tabela declarada em {group}: {member}"
        if yearly and base_id.startswith("arf-depositarias"):
            literals.append(("membro", Path(member).stem))
        parts.append(
            _Plan(
                path,
                keys,
                vals,
                member=member,
                key_name=key_names[member],
                literals=tuple(literals),
                table=table,
                ignored=ignored,
            )
        )
    return parts


#: O pré-sal é um recorte do mar (as mesmas linhas já estão no ``mar``): vai para o
#: dataset ``<dataset>-presal``, para somar mar+terra não duplicar nada.
_PRESAL = "presal"


def _dataset_of(group: str, plan: _Plan, finest: int) -> str:
    """O dataset de um item: o da tabela, o ``-presal`` ou o da granularidade."""
    if plan.table:
        return plan.table
    dataset = dataset_for_granularity(group, plan.keys, finest, path=plan.path)
    if ("ambiente", _PRESAL) in plan.literals:
        return f"{dataset}-{_PRESAL}"
    return dataset


def _is_json_in_zip_clothing(path: Path) -> bool:
    """Se um arquivo ``.zip`` é na verdade JSON (``pmqc-json_2024-02.zip``)."""
    if path.suffix.lower() != ".zip" or zipfile.is_zipfile(path):
        return False
    with open(path, "rb") as fh:
        head = fh.read(64).lstrip()
    return head[:1] in (b"{", b"[")


def route_group(
    group: str, src_group_dir: Path
) -> tuple[list[Routed], list[tuple[Path, str]]]:
    """Roteia os arquivos de um grupo: os convertidos e os ignorados, com motivo.

    Regra única de :meth:`LakeConverter.convert` e :meth:`LakeConverter.inventory`:
    um arquivo por conteúdo (:func:`pick_one_format`), partições pelo nome
    (:func:`resolve_partitions`) e dataset pela granularidade do grupo
    (:func:`dataset_for_granularity`). ZIP com vários membros de dados rende um
    item por membro (:func:`_zip_parts`). Os arquivos descartados voltam com o
    motivo do inventário: ``"gemeo"`` (mesmo conteúdo em outro formato),
    ``"nao_tabular"`` (formato que o leitor não abre) ou ``"superado"``
    (versão anterior do mesmo formato).
    """
    files = raw_files(src_group_dir)
    best = _best_by_base(files)

    chosen = sorted(path for _, _, path in best.values())
    # JSON com extensão .zip: o leitor não abre, e não pode tomar o lugar do mês
    # que o ZIP anual traz em CSV.
    json_as_zip = {p for p in chosen if _is_json_in_zip_clothing(p)}
    chosen = [p for p in chosen if p not in json_as_zip]
    resolved = [_Plan(f, *resolve_partitions(parse_filename(f))) for f in chosen]
    expanded_away: set[Path] = set()
    if group == "pmqc":
        # ZIP anual (um CSV por mês): vira os meses do mesmo dataset dos mensais.
        # Mês que já existe como arquivo mensal avulso fica com o avulso, para não
        # duplicar linhas na partição.
        monthly = {
            (plan.vals["ano"], plan.vals["mes"])
            for plan in resolved
            if plan.keys == ["ano", "mes"]
        }
        pmqc: list[_Plan] = []
        for plan in resolved:
            members = (
                _pmqc_zip_members(plan.path)
                if plan.keys == ["ano"] and plan.path.suffix.lower() == ".zip"
                else []
            )
            if not members:
                pmqc.append(plan)
                continue
            names = _unique_key_names(plan.path, [name for name, _ in members])
            kept = [
                _Plan(
                    plan.path,
                    ["ano", "mes"],
                    mvals,
                    member=name,
                    key_name=names[name],
                )
                for name, mvals in members
                if (mvals["ano"], mvals["mes"]) not in monthly
            ]
            if not kept:
                expanded_away.add(plan.path)
            pmqc.extend(kept)
        resolved = pmqc
    expanded: list[_Plan] = []
    for plan in resolved:
        parts = _zip_parts(group, plan) if plan.member is None else []
        expanded.extend(parts or [plan])
    resolved = expanded
    finest = max((len(plan.keys) for plan in resolved if not plan.table), default=0)
    routed = [
        Routed(
            path=plan.path,
            dataset_id=_dataset_of(group, plan, finest),
            partition_keys=plan.keys,
            partition_values=plan.vals,
            member=plan.member,
            key_name=plan.key_name,
            literals=plan.literals,
            ignored=plan.ignored,
        )
        for plan in resolved
    ]

    routed_paths = {item.path for item in routed}
    ignored: list[tuple[Path, str]] = []
    for path in files:
        if path in routed_paths:
            continue
        if path in expanded_away:
            ignored.append((path, "gemeo"))
            continue
        if path in json_as_zip:
            # o mesmo mês vem em CSV no ZIP anual; sem a marca -json, JSON é dado
            reason = "gemeo" if _FORMAT_TAG.search(path.name) else "nao_tabular"
            ignored.append((path, reason))
            continue
        if not is_tabular(path):
            ignored.append((path, "nao_tabular"))
            continue
        chosen_path = best[_format_rank(path)[0]][2]
        reason = (
            "gemeo" if chosen_path.suffix.lower() != path.suffix.lower() else "superado"
        )
        ignored.append((path, reason))
    return routed, ignored


LAKE_DATASET_ALIASES: dict[str, str] = {
    "royalties_municipio": "royalties",
    "royalties-municipio": "royalties",
    "royalties_uniao": "royalties",
    "royalties-uniao": "royalties",
    "royalties_estado": "royalties",
    "royalties-estado": "royalties",
    "participacoes_especiais": "royalties",
    "participacoes-especiais": "royalties",
    "participacao_especial": "royalties",
    "participacao-especial": "royalties",
    "preco_referencia_gn": "royalties",
    "preco-referencia-gn": "royalties",
    "preco_referencia_petroleo": "royalties",
    "preco-referencia-petroleo": "royalties",
}


_SHA_LOCK = threading.Lock()


@contextmanager
def _sha_cached(path: Path, digest: str) -> Iterator[None]:
    """O ``LakeWriter`` hasheia o bruto a cada escrita; um ZIP com 30 membros seria
    lido 30 vezes. Dentro do bloco o hash de ``path`` já vem pronto. A troca do
    global é um estado do processo: o lock a serializa entre threads.
    """
    with _SHA_LOCK:
        original = analytics_lake.sha256_file

        def cached(target: str | Path, *args: Any, **kwargs: Any) -> str:
            if Path(target) == path:
                return digest
            return original(target, *args, **kwargs)

        analytics_lake.sha256_file = cached
        try:
            yield
        finally:
            analytics_lake.sha256_file = original


def _prune_zip_parts(
    lake_dir: Path, datasets: set[str], raw_file: Path, produced: set[str]
) -> int:
    """Apaga os Parquets de um ZIP que esta conversão não produziu mais.

    O rodapé (``quantilica.file_key``) de cada Parquet diz de que ZIP e membro ele
    veio: ``<zip>`` (layout antigo, só o 1º membro) ou ``<zip>__<membro>``. Cai tudo
    o que é do ZIP e não está em ``produced``, nos ``datasets`` que o roteamento do
    grupo usa: o layout antigo, o membro que sumiu ou mudou de nome numa edição nova
    do ZIP, e os membros de um ZIP que passou a ter um só. Sem isso o ``--force``
    deixaria o antigo ao lado do novo e as linhas dobrariam. Um dataset que fica
    sem dados sai com os arquivos.

    Returns:
        int: Quantos arquivos foram apagados.
    """
    base = lake_dir / SOURCE_ID
    if not base.is_dir() or not produced:
        return 0
    key = file_key(raw_file)
    removed = 0
    for name in sorted(datasets):
        dataset = base / name
        if not dataset.is_dir():
            continue
        dropped = 0
        for path in dataset.rglob(f"{glob.escape(key)}*.parquet"):
            if any(part.startswith(".") for part in path.relative_to(dataset).parts):
                continue  # staging do writer
            try:
                owner = (pq.ParquetFile(path).metadata.metadata or {}).get(
                    META_FILE_KEY.encode()
                )
            except (OSError, pq.lib.ArrowException):
                continue
            if owner is None:
                continue
            owner_key = owner.decode()
            if owner_key in produced or not (
                owner_key == key or owner_key.startswith(f"{key}__")
            ):
                continue
            path.unlink()
            removed += 1
            dropped += 1
            folder = path.parent
            while folder != dataset:  # partições que ficaram vazias
                try:
                    folder.rmdir()
                except OSError:
                    break
                folder = folder.parent
        if dropped and not any(dataset.rglob("*.parquet")):
            # dataset sem dados: sai o descritor e a pasta, se nada mais sobrou
            for leftover in ("_dataset.json", ".lock"):
                (dataset / leftover).unlink(missing_ok=True)
            try:
                dataset.rmdir()
            except OSError:
                pass
    return removed


_DIGESTS: dict[Path, tuple[tuple[int, int], str]] = {}


def _digest(path: Path) -> str:
    """O sha256 do bruto, calculado uma vez por arquivo (e por versão dele)."""
    stat = path.stat()
    signature = (stat.st_size, stat.st_mtime_ns)
    cached = _DIGESTS.get(path)
    if cached is None or cached[0] != signature:
        _DIGESTS[path] = (signature, sha256_file(path))
    return _DIGESTS[path][1]


def _item_key(item: Routed) -> str | None:
    """O ``file_key`` de um item de ZIP aberto por membro; ``None`` = o do arquivo."""
    if item.member is None:
        return None
    return composite_file_key(item.path, item.key_name or Path(item.member).name)


def _table_group(dataset: str) -> str | None:
    """O grupo de um dataset derivado (``ppg-presal``, ``...-calha``)."""
    for group in (*TABLE_DATASET_GROUPS, *_AMBIENTE_GROUPS):
        if dataset.startswith(f"{group}-"):
            return group
    return None


def _materialize(item: Routed, tmp_dir: Path) -> Path:
    """O arquivo a ler de um item: o bruto, o membro extraído ou o ZIP aberto.

    A extração vai para ``tmp_dir``, que o chamador descarta: nada fica no temp.
    """
    raw_file = item.path
    if item.member is not None:
        return extract_zip_member(raw_file, item.member, tmp_dir)
    suffix = raw_file.suffix.lower()
    if suffix == ".zip":
        if not zipfile.is_zipfile(raw_file):
            raise RuntimeError("não é um arquivo ZIP válido")
        members = zip_data_members(raw_file)
        if len(members) == 1:
            return extract_zip_member(raw_file, members[0], tmp_dir)
    if suffix in (".zip", ".7z"):
        try:
            return decompress(raw_file, tmp_dir)
        except RuntimeError as exc:
            raise RuntimeError(f"erro na descompressão: {exc}") from exc
    return raw_file


class LakeConverter:
    """Converter registered under the ``quantilica.lake`` entry point."""

    source_id = SOURCE_ID

    def datasets(self) -> list[str]:
        """Dataset ids this converter writes to the lake."""
        return sorted(k for k in ALL_GROUP_KEYS if k in _GROUP_DIRS)

    def convert(
        self,
        input_dir: Path,
        lake_dir: Path,
        *,
        datasets: list[str] | None = None,
        force: bool = False,
    ) -> ConvertResult:
        """Convert raw ANP files into ``lake_dir``.

        Args:
            input_dir: Root directory containing raw ANP files.
            lake_dir: Root of the lake.
            datasets: Optional list of group names or aliases to convert.
            force: Reconvert even if sha256 already matches in the lake.

        Returns:
            ConvertResult: Files converted, skipped, and error messages.
        """
        input_dir = Path(input_dir)
        lake_dir = Path(lake_dir)
        result = ConvertResult()
        if not input_dir.is_dir():
            result.errors.append(f"diretório '{input_dir}' não existe")
            return result

        target_groups: list[str] = []
        target_datasets: set[str] | None = None
        if datasets:
            target_datasets = set(datasets)
            for d in datasets:
                aliased = LAKE_DATASET_ALIASES.get(d, d)
                resolved = resolve_group(aliased) or _table_group(aliased) or aliased
                if resolved in _GROUP_DIRS and resolved not in target_groups:
                    target_groups.append(resolved)
                elif resolved not in _GROUP_DIRS:
                    result.errors.append(f"dataset desconhecido: {d}")
            if result.errors:
                return result
        else:
            target_groups = self.datasets()

        # Roteia antes de converter: o id de uma tabela só existe se um arquivo o rende.
        routes: dict[str, list[Routed]] = {}
        for group in target_groups:
            src_group_dir = input_dir / _GROUP_DIRS[group]
            if src_group_dir.exists():
                routes[group] = route_group(group, src_group_dir)[0]
        if target_datasets:
            known = {item.dataset_id for items in routes.values() for item in items}
            for d in sorted(target_datasets):
                aliased = LAKE_DATASET_ALIASES.get(d, d)
                if (
                    not resolve_group(aliased)
                    and aliased not in _GROUP_DIRS
                    and d not in known
                ):
                    result.errors.append(f"dataset desconhecido: {d}")
            if result.errors:
                return result

        writers: dict[str, LakeWriter] = {}

        for group, routed in routes.items():
            spec = spec_for(group)
            # por ZIP: itens que não chegaram ao lake (decide a limpeza) e chaves
            # produzidas (o que a limpeza preserva)
            failed: dict[Path, int] = {}
            produced: dict[Path, set[str]] = {}

            for item in routed:
                part_keys = item.partition_keys
                dataset_id = item.dataset_id
                label = (
                    f"{item.path.name}[{item.member}]"
                    if item.member
                    else item.path.name
                )
                failed.setdefault(item.path, 0)
                produced.setdefault(item.path, set())

                if (
                    target_datasets
                    and dataset_id not in target_datasets
                    and group not in target_datasets
                    and LAKE_DATASET_ALIASES.get(dataset_id) not in target_datasets
                ):
                    failed[item.path] += 1  # fora da seleção: ZIP incompleto
                    continue
                if item.ignored:
                    result.warnings.append(f"{label}: {item.ignored}")
                    logger.warning("%s: %s", label, item.ignored)
                    continue

                produced[item.path].add(_item_key(item) or file_key(item.path))
                writer_key = f"{dataset_id}:" + ",".join(part_keys)
                if writer_key not in writers:
                    writers[writer_key] = LakeWriter(
                        lake_dir / SOURCE_ID / dataset_id,
                        DatasetDescriptor(
                            source_id=SOURCE_ID,
                            dataset_id=dataset_id,
                            alias=dataset_id,
                            partition_keys=part_keys,
                            partition_types=partition_types_for(part_keys),
                        ),
                        force=force,
                    )
                writer = writers[writer_key]

                try:
                    with _sha_cached(item.path, _digest(item.path)):
                        if writer.is_current(
                            item.path,
                            partitions=item.partition_values,
                            file_key_name=_item_key(item),
                        ):
                            result.skipped += 1  # sem extrair nem ler o membro
                            continue
                        with tempfile.TemporaryDirectory(
                            prefix=".anp-zip-",
                            dir=scratch_dir(),
                            ignore_cleanup_errors=True,
                        ) as tmp:
                            source_path = _materialize(item, Path(tmp))
                            self._write_item(
                                writer, group, spec, item, source_path, result
                            )
                except Exception as exc:
                    message = str(exc).strip()
                    first_line = message.splitlines()[0] if message else repr(exc)
                    result.errors.append(f"{label}: {first_line}")
                    failed[item.path] += 1

            scope = {item.dataset_id for item in routed} | {group}
            for path, count in failed.items():
                if (
                    count == 0
                    and path.suffix.lower() == ".zip"
                    and spec.get("sheet") != "all"
                ):
                    _prune_zip_parts(lake_dir, scope, path, produced[path])

        return result

    @staticmethod
    def _write_item(
        writer: LakeWriter,
        group: str,
        spec: dict[str, Any],
        item: Routed,
        source_path: Path,
        result: ConvertResult,
    ) -> None:
        """Lê ``source_path`` (o arquivo ou o membro já extraído) e grava no lake."""
        raw_file = item.path
        part_keys_lower = [k.lower() for k in item.partition_keys]
        data = read_file(source_path, spec)
        frames = list(data.items()) if isinstance(data, dict) else [(None, data)]
        for sheet, frame in frames:
            norm = normalize_dtypes(frame, spec)
            norm = _apply_contract(group, norm, raw_file.name)
            if item.dataset_id == "participacoes_especiais":
                # quatro recortes (uniao/estado/municipio/campo) com
                # colunas diferentes no mesmo dataset: a coluna os separa.
                recorte = parse_filename(raw_file)["base_id"].removeprefix("pe-")
                norm = norm.with_columns(pl.lit(recorte).alias("recorte"))
            drop_part_cols = [c for c in norm.columns if c.lower() in part_keys_lower]
            if drop_part_cols:
                norm = norm.drop(drop_part_cols)
            existing = {c.lower() for c in norm.columns}
            norm = norm.with_columns(
                [
                    pl.lit(value).alias(name)
                    for name, value in item.literals
                    if name.lower() not in existing
                ]
            )
            file_key_override = None
            if item.member is not None:
                label = item.key_name or Path(item.member).name
                if sheet is not None:
                    label = f"{label} {sheet}"
                file_key_override = composite_file_key(raw_file, label)
            elif sheet is not None:
                file_key_override = composite_file_key(raw_file, sheet)

            written = writer.write_polars(
                norm,
                raw_file,
                partitions=item.partition_values,
                file_key_name=file_key_override,
                converter=f"anp-fetcher {__version__}",
            )
            if written.status == "skipped":
                result.skipped += 1
            else:
                result.converted += 1

    def inventory(self, input_dir: Path) -> list[Planned]:
        """Um ``Planned`` por arquivo bruto: o dataset ou o motivo de ignorar.

        Espelha a descoberta de :meth:`convert` (mesmas funções de roteamento):
        um arquivo por conteúdo e um dataset por granularidade. Arquivos que o
        leitor não abre (PDF, imagens, documentos, mapas) vêm como
        ``"nao_tabular"``; os gêmeos de outro formato como ``"gemeo"``; as
        versões anteriores do mesmo formato como ``"superado"``. Sidecars
        ``*.manifest.json`` e restos ``*.tmp`` não entram no inventário.

        Args:
            input_dir: Raiz dos arquivos brutos da ANP (a mesma de ``convert``).

        Returns:
            list[Planned]: Um item por arquivo, na ordem dos grupos.
        """
        # Import local: o core publicado antes do contrato não tem ``Planned``.
        from quantilica.core.lake import Planned

        input_dir = Path(input_dir)
        if not input_dir.is_dir():
            return []

        planned: list[Planned] = []
        covered: set[Path] = set()
        for group in self.datasets():
            src_group_dir = input_dir / _GROUP_DIRS[group]
            if not src_group_dir.is_dir():
                continue
            routed, ignored = route_group(group, src_group_dir)
            for item in routed:
                if item.path in covered:  # ZIP anual: um item por mês
                    continue
                covered.add(item.path)
                if is_tabular(item.path):
                    planned.append(Planned(item.path, dataset=item.dataset_id))
                else:
                    planned.append(Planned(item.path, skip_reason="nao_tabular"))
            for path, reason in ignored:
                covered.add(path)
                planned.append(Planned(path, skip_reason=reason))

        # Fora dos diretórios de grupo o conversor não procura nada. O não
        # tabular é documentação; o tabular fica sem destino para a auditoria
        # apontar a lacuna em vez de supor um Parquet que nunca existirá.
        for path in sorted(input_dir.rglob("*")):
            if not path.is_file() or path in covered or _is_sidecar(path):
                continue
            planned.append(
                Planned(path, skip_reason=None if is_tabular(path) else "nao_tabular")
            )
        return planned


converter = LakeConverter()
