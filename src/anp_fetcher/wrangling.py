"""Driver de conversão de dados brutos ANP para Parquet.

No padrão do ``pdet-fetcher.wrangling``: converte os arquivos coletados
por grupo em Parquet limpo, idempotente (pula o que já foi convertido) e com
proveniência (metadados do manifest sidecar). Também extrai o schema dos
arquivos brutos para subsidiar ``DataContract``.
"""

from __future__ import annotations

import csv
import logging
from contextlib import ExitStack
from pathlib import Path
from typing import Any

try:
    import polars as pl
except ImportError as exc:
    raise ImportError(
        "anp_fetcher.wrangling requer o extra 'analysis': "
        "uv add 'anp-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

from .contracts import CONTRACTS
from .reader import (
    DEFAULT_NULL_VALUES,
    QualityReport,
    extracted_data,
    normalize_dtypes,
    parse_filename,
    read_file,
    write_parquet,
)
from .storage import _GROUP_DIRS

logger = logging.getLogger(__name__)

DEFAULT_SPEC: dict[str, Any] = {
    "encoding": None,  # None = tenta utf-8, cai para latin-1
    "separator": ";",
    "sheet": None,  # None = primeira aba; "all" = todas (dict); N = N-ésima
    "numeric_columns": [],
    # Ausência declarada nas colunas numéricas e de data: vira nulo e é contada.
    "null_values": list(DEFAULT_NULL_VALUES),
    # Fração das linhas de uma coluna tipada que pode virar nulo por não converter
    # (e ser contada); acima disso o arquivo falha. 0 = nenhuma.
    "max_invalid_frac": 0.0,
    "skip_rows": 0,
    "infer_schema_length": 0,
}

# Overrides por grupo. O padrão sãos cobre a maioria (CSV `;` latin-1).
_SHPC_SPEC: dict[str, Any] = {
    "encoding": "utf-8",
    "numeric_columns": ["Valor de Venda", "Valor de Compra"],
    "date_columns": {"Data da Coleta": "%d/%m/%Y"},
}

# Colunas de valor dos CSV de dados abertos de vendas, comércio exterior e
# produção; cada arquivo tem só algumas delas.
_ABERTOS_NUMERIC = [
    "VENDAS",
    "Vendas de Biodiesel",
    "P13",
    "OUTROS",
    "PRODUÇÃO",
    "PROCESSADO",
    "IMPORTADO",
    "IMPORTADO / EXPORTADO",
    "DISPÊNDIO",
    "DISPÊNDIO / RECEITA",
]

# Planilhas e CSV que começam por título e data (``ANP - Agência...``,
# ``Data: 15/03/2019``) e têm o cabeçalho em até três níveis (célula mesclada).
_POCO_HEADER_SPEC: dict[str, Any] = {"header": {"levels": True}}
# Consolidação de amostras (CSV com título) e depositárias (formulário de preços:
# o cabeçalho é a linha que começa por "Serviço").
_ARF_SPEC: dict[str, Any] = {"header": {"anchor": r"^servi[cç]o"}}

# Painéis estatísticos (planilha com várias tabelas empilhadas, ``Mês`` e os anos no
# cabeçalho): cada tabela vira linhas, com a coluna ``tabela`` de origem.
_PAINEL_TABLES = r"^m[eê]s(es)?$"
_PAINEL_SPEC: dict[str, Any] = {"header": {"tables": _PAINEL_TABLES}}
# Vendas: o painel mensal e as planilhas municipais (título, unidade e ano acima do
# cabeçalho ``CÓDIGO IBGE``, com ``IBGE`` repetido na linha de baixo).
_VENDAS_SPEC: dict[str, Any] = {
    "header": {
        "tables": _PAINEL_TABLES,
        "anchor": r"^c[oó]digo ibge",
        "levels": 1,  # só o ``IBGE`` repetido; a linha de baixo já é o 1º estado
        "drop_blank": True,
    },
    # nomes canônicos: a fonte alterna Município/Municípios e Vendas/Total/TOTAL GERAL
    "rename": {
        "Município": r"munic[ií]pios?",
        "Vendas": r"vendas|total|total geral",
    },
    # produto (slug do nome do arquivo, estável), produto_fonte e unidade (o texto
    # do preâmbulo da planilha, como vem)
    "preamble": {
        "produto": r"^vendas de (.+?)(?: por .*)?$",
        "unidade": r"^unidade de medida:\s*(.+)$",
    },
    "preamble_from_name": {"produto": r"^vendas-municipais-(.+)$"},
}

# Movimentação de gás natural em gasodutos: uma coluna por dia do mês (28 a 31, e um
# esquema diferente por arquivo) vira ``data``/``valor``. Os nomes das colunas de
# identificação são os da safra mais recente; a fonte os escreveu de outras formas
# (``Tipo da Instalação do Gasoduto``, ``Nome do Operador da Instalação``), e o
# casamento ignora acento, caixa e ``do``/``de``.
_MOVIMENTACAO_GN_SPEC: dict[str, Any] = {
    "wide_dates": {
        "ids": [
            "Código da Instalação de Transporte",
            "Nome da Instalação de Transporte",
            "Nome da Instalação de Gasoduto",
            "Código da Instalação de Gasoduto",
            "Tipo da instalação de Gasoduto",
            "Nome do Município da Instalação de Gasoduto",
            "Nome da UF da Instalação de Gasoduto",
            "Nome do Operador da instalação de Gasoduto",
            "Código do Operador da Instalação de Gasoduto",
            "Nome do Carregador que usa a Instalação de Gasoduto",
            "Código do Carregador que usa a Instalação de Gasoduto",
            "Nome do Contrato da Instalação de Gasoduto",
        ],
        "variable": "Nome da Variável",
    }
}

PROCESSING_SPECS: dict[str, dict[str, Any]] = {
    "movimentacao-gn": _MOVIMENTACAO_GN_SPEC,
    "ie": _PAINEL_SPEC,
    "pp": _PAINEL_SPEC,
    "pb": _PAINEL_SPEC,
    "vdpb": _VENDAS_SPEC,
    "ppg": {"header": {**_POCO_HEADER_SPEC["header"], "tables": _PAINEL_TABLES}},
    "producao-poco-abertos": _POCO_HEADER_SPEC,
    "amostras-rochas-fluidos": _ARF_SPEC,
    "shpc-ca": _SHPC_SPEC,
    "shpc-glp": _SHPC_SPEC,
    "shpc-diesel-gnv": _SHPC_SPEC,
    "shpc-gasolina-etanol": _SHPC_SPEC,
    "shpc-glp-mensal": _SHPC_SPEC,
    "shpc-4s": _SHPC_SPEC,
    "vdpb-abertos": {"numeric_columns": _ABERTOS_NUMERIC},
    "ie-abertos": {"numeric_columns": _ABERTOS_NUMERIC},
    "pp-abertos": {"numeric_columns": _ABERTOS_NUMERIC},
    "pb-abertos": {"numeric_columns": _ABERTOS_NUMERIC},
}


def spec_for(group: str) -> dict[str, Any]:
    """Devolve a especificação de processamento de um grupo (default + overrides).

    Args:
        group (str): O id canônico do grupo.

    Returns:
        dict[str, Any]: A especificação efetiva do grupo.
    """
    return {**DEFAULT_SPEC, **PROCESSING_SPECS.get(group, {})}


def _log_quality(name: str, quality: QualityReport) -> None:
    """Avisa no log o que virou nulo na conversão (célula vazia não conta)."""
    if quality.has_loss:
        logger.warning("%s: %s", name, quality.summary())


def _target_path(
    meta: dict[str, Any], group_dir: str, out_dir: Path, sheet: str | None = None
) -> Path:
    """Monta o caminho do Parquet espelhando o nome do arquivo bruto.

    Args:
        meta (dict[str, Any]): Metadados de ``parse_filename``.
        group_dir (str): Diretório do grupo sob a raiz de saída.
        out_dir (Path): Raiz de saída.
        sheet (str | None, optional): Nome da aba (multi-sheet excel).

    Returns:
        Path: O caminho do Parquet de destino.
    """
    base = meta["base_id"]
    if sheet:
        base = f"{base}_{sheet}"
    partition = meta["partition"]
    mod = meta["modification"]
    name = base if not partition else f"{base}_{partition}"
    if mod:
        name = f"{name}@{mod}"
    return out_dir / group_dir / f"{name}.parquet"


def _iter_group_files(input_dir: Path, group_dir: str) -> list[Path]:
    src = input_dir / group_dir
    if not src.exists():
        logger.warning("Diretório do grupo não existe: %s", src)
        return []
    return sorted(
        p
        for p in src.iterdir()
        if p.is_file() and not p.name.endswith(".manifest.json")
    )


def _apply_contract(
    group: str,
    data: pl.DataFrame,
    filename: str,
) -> pl.DataFrame:
    """Aplica o DataContract do grupo (best-effort): valida e casta.

    Args:
        group (str): O id canônico do grupo.
        data (pl.DataFrame): O DataFrame normalizado.
        filename (str): Nome do arquivo de origem (para o log).

    Returns:
        pl.DataFrame: O DataFrame com o contrato aplicado (ou inalterado).
    """
    contract = CONTRACTS.get(group)
    if contract is None:
        return data
    try:
        contract.validate(data)
        return contract.cast(data)
    except Exception as exc:
        logger.warning("Contrato %s não aplicado em %s: %s", group, filename, exc)
        return data


def convert_one(
    group: str,
    raw_file: Path,
    output_dir: Path,
) -> Path | list[Path]:
    """Converte um único arquivo bruto do grupo em Parquet.

    Args:
        group (str): O id canônico do grupo.
        raw_file (Path): O arquivo bruto coletado.
        output_dir (Path): A raiz de saída.

    Returns:
        Path | list[Path]: O(s) Parquet(s) escrito(s), ou lista vazia se pulado.
    """
    group_dir = _GROUP_DIRS[group]
    spec = spec_for(group)
    meta = parse_filename(raw_file)
    source_path = raw_file

    if raw_file.name.endswith(".manifest.json"):
        return []

    # A pasta de extração (a raiz, subpastas incluídas) some ao sair do ``with``.
    with ExitStack() as stack:
        if raw_file.suffix.lower() in (".zip", ".7z"):
            try:
                inner = stack.enter_context(extracted_data(raw_file))
            except RuntimeError as exc:
                logger.error("Falha ao descompactar %s: %s", raw_file.name, exc)
                return []
            source_path = inner
            raw_file = inner

        try:
            data = read_file(raw_file, spec)
        except Exception as exc:
            logger.error("Falha ao ler %s: %s", raw_file.name, exc)
            return []

    written: list[Path] = []
    if isinstance(data, dict):
        for sheet_name, frame in data.items():
            if frame.is_empty():
                continue
            target = _target_path(meta, group_dir, output_dir, sheet=sheet_name)
            if target.exists():
                logger.debug("Pulando %s (já convertido)", target.name)
                continue
            quality = QualityReport()
            frame = normalize_dtypes(frame, spec, report=quality)
            _log_quality(raw_file.name, quality)
            frame = _apply_contract(group, frame, raw_file.name)
            written.append(write_parquet(frame, target, source_path=source_path))
    else:
        target = _target_path(meta, group_dir, output_dir)
        if target.exists():
            logger.debug("Pulando %s (já convertido)", target.name)
            return []
        quality = QualityReport()
        data = normalize_dtypes(data, spec, report=quality)
        _log_quality(raw_file.name, quality)
        data = _apply_contract(group, data, raw_file.name)
        written.append(write_parquet(data, target, source_path=source_path))

    return written


def convert_group(groups: list[str], input_dir: Path, output_dir: Path) -> int:
    """Converte os grupos informados em Parquet (idempotente).

    Args:
        groups (list[str]): Ids canônicos dos grupos a converter.
        input_dir (Path): Diretório com os dados brutos.
        output_dir (Path): Diretório de saída dos Parquet.

    Returns:
        int: Número de arquivos Parquet escritos.
    """
    total = 0
    for group in groups:
        if group not in _GROUP_DIRS:
            logger.warning("Grupo desconhecido (sem diretório): %s", group)
            continue
        for raw_file in _iter_group_files(input_dir, _GROUP_DIRS[group]):
            written = convert_one(group, raw_file, output_dir)
            total += len(written)
    return total


def extract_schema(
    groups: list[str],
    input_dir: Path,
    output_file: Path,
) -> None:
    """Extrai o schema (colunas/ordem/tipo) dos arquivos brutos para referência.

    Args:
        groups (list[str]): Ids canônicos dos grupos.
        input_dir (Path): Diretório com os dados brutos.
        output_file (Path): Caminho do CSV de referência a escrever.
    """
    fieldnames = ["group", "base_id", "partition", "column", "order", "dtype"]
    with open(output_file, "w", encoding="utf-8", newline="\n") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for group in groups:
            group_dir = _GROUP_DIRS.get(group)
            if not group_dir:
                continue
            spec = spec_for(group)
            for raw_file in _iter_group_files(input_dir, group_dir):
                meta = parse_filename(raw_file)
                try:
                    data = read_file(raw_file, spec)
                except Exception as exc:
                    logger.error("Falha ao ler %s: %s", raw_file.name, exc)
                    continue
                frames = (
                    list(data.items()) if isinstance(data, dict) else [(None, data)]
                )
                for _sheet, frame in frames:
                    for order, column in enumerate(frame.columns):
                        writer.writerow(
                            {
                                "group": group,
                                "base_id": meta["base_id"],
                                "partition": meta["partition"],
                                "column": column,
                                "order": order,
                                "dtype": str(frame[column].dtype),
                            }
                        )
