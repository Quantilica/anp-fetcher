"""Extração e leitura tipada de arquivos brutos da ANP.

Camada de conversão de dados coletados para Polars/Parquet, no padrão do
``pdet-fetcher`` (reader + wrangling). Lê CSV (latin-1/utf-8, separador ``;``,
decimal vírgula), XLS/XLSX (via ``pl.read_excel`` + fastexcel) e arquivos
ZIP/7z, normaliza dtypes e escreve Parquet com metadados de proveniência
extraídos do sidecar ``DownloadManifest``.
"""

from __future__ import annotations

import logging
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Any

try:
    import polars as pl
    from quantilica.analytics.reader import (
        normalize_brazilian_numbers,
        read_brazilian_csv,
    )
    from quantilica.analytics.writer import manifest_to_metadata, to_parquet
except ImportError as exc:
    raise ImportError(
        "anp_fetcher.reader requer o extra 'analysis': "
        "uv add 'anp-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc
from quantilica.core.exceptions import StorageError
from quantilica.core.files import decompress_archive
from quantilica.core.manifests import DownloadManifest, read_manifest_sidecar

logger = logging.getLogger(__name__)

# Layouts do storage do anp-fetcher (o stamp @YYYYMMDD é opcional — ausente
# quando o servidor não reporta Last-Modified):
#   {base_id}[@{YYYYMMDD}].{ext}                   (estático)
#   {base_id}_{year}[@{YYYYMMDD}].{ext}            (anual)
#   {base_id}_{year}-{part:02d}[@{YYYYMMDD}].{ext} (mensal/semestral)
_FILENAME_RE = re.compile(
    r"^(?P<base_id>.+?)"
    r"(?:_(?P<year>\d{4})(?:-(?P<part>\d{2}))?)?"
    r"(?:@(?P<mod>\d{8}))?"
    r"\.(?P<ext>[a-z0-9]+)$"
)

_DECOMPRESSIBLE = {".zip", ".7z"}


def parse_filename(path: Path) -> dict[str, Any]:
    """Extrai metadados de um arquivo no padrão de nome do storage ANP.

    Args:
        path (Path): O caminho do arquivo bruto.

    Returns:
        dict[str, Any]: Metadados com ``base_id``, ``year``, ``part``,
            ``partition`` (string de partição ou None), ``modification``
            (YYYYMMDD) e ``ext``.
    """
    m = _FILENAME_RE.match(path.name)
    if not m:
        return {
            "filepath": path,
            "filename": path.name,
            "base_id": path.stem,
            "year": None,
            "part": None,
            "partition": None,
            "modification": None,
            "ext": path.suffix.lstrip("."),
        }
    g = m.groupdict()
    year = int(g["year"]) if g["year"] else None
    part = int(g["part"]) if g["part"] else None
    mod = int(g["mod"]) if g["mod"] else None
    if part is not None:
        partition = f"{year}-{part:02d}"
    elif year is not None:
        partition = str(year)
    else:
        partition = None
    return {
        "filepath": path,
        "filename": path.name,
        "base_id": g["base_id"],
        "year": year,
        "part": part,
        "partition": partition,
        "modification": mod,
        "ext": g["ext"],
    }


def decompress(path: Path) -> Path:
    """Descompacta um arquivo ZIP/7z e retorna o primeiro arquivo de dados.

    A extração é delegada a ``quantilica.core.files.decompress_archive``
    (nativa para ZIP/TAR com proteção contra path traversal, fallback
    ``7z``). O contrato público do módulo é preservado: falhas de extração
    sobem como ``RuntimeError``.

    Args:
        path (Path): O caminho do arquivo compactado.

    Returns:
        Path: O caminho do arquivo extraído (primeiro csv/xls/xlsx encontrado).

    Raises:
        RuntimeError: Se a extração falhar ou não produzir arquivos de dados.
    """
    logger.info("Descompactando %s", path)
    try:
        return decompress_archive(path, target_extensions=(".csv", ".xls", ".xlsx"))
    except StorageError as exc:
        raise RuntimeError(f"falha ao descompactar {path}: {exc}") from exc


def read_csv(path: Path, spec: dict[str, Any]) -> pl.DataFrame:
    """Lê um CSV da ANP (utf-8 com fallback latin-1).

    Args:
        path (Path): Caminho do arquivo CSV.
        spec (dict[str, Any]): Especificação de processamento do grupo.

    Returns:
        pl.DataFrame: O DataFrame lido com tipos inferidos.
    """
    kwargs: dict[str, Any] = {
        "separator": spec.get("separator", ";"),
        "infer_schema_length": spec.get("infer_schema_length", 0),
    }
    if spec.get("skip_rows"):
        kwargs["skip_rows"] = spec["skip_rows"]
    encoding = spec.get("encoding")
    try:
        return read_brazilian_csv(
            path, encoding=encoding or "utf-8", decimal=",", **kwargs
        )
    except Exception as exc:  # fallback latin-1
        if encoding is not None:
            raise
        logger.debug("UTF-8 falhou (%s); tentando latin-1", exc)
        try:
            return read_brazilian_csv(path, encoding="latin-1", decimal=",", **kwargs)
        except Exception as exc2:
            # Linhas com um campo a mais (separador no fim) ou CSV que o leitor
            # paralelo do polars recusa ("CSV malformed: expected N rows"). Por
            # último, sem tratar aspas: em revendas-glp elas fazem parte do texto
            # (D"AGUA, "O EDGAR") e, lidas como delimitador, engolem linhas.
            logger.warning("%s: %s; relendo de forma tolerante", path, exc2)
            attempts = [(q, enc) for q in ('"', None) for enc in ("utf-8", "latin-1")]
            for quote, enc in attempts:
                try:
                    return read_brazilian_csv(
                        path,
                        encoding=enc,
                        decimal=",",
                        truncate_ragged_lines=True,
                        quote_char=quote,
                        **kwargs,
                    )
                except Exception:
                    if (quote, enc) == attempts[-1]:
                        raise
            raise


def read_json(path: Path) -> pl.DataFrame:
    """Lê um JSON tabular (array de objetos), em UTF-8 (com BOM) ou Latin-1.

    Colunas com tipos mistos ficam como texto, para não perder registros.
    """
    import json as _json

    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        text = path.read_text(encoding="latin-1")
    data = _json.loads(text)
    if isinstance(data, dict):  # {"dados": [...]} e afins
        data = next((v for v in data.values() if isinstance(v, list)), [data])
    try:
        return pl.from_dicts(data)
    except Exception:
        keys = {k for row in data for k in row}
        return pl.from_dicts(data, schema_overrides={k: pl.String for k in keys})


def _excel_path(path: Path, tmp_dir: Path) -> Path:
    """O caminho a ler como planilha, com a extensão que bate com o conteúdo.

    A ANP publica xlsx com extensão ``.xls``; o leitor escolhe o formato pela
    extensão e recusa o arquivo ("Invalid OLE").
    """
    with open(path, "rb") as fh:
        is_zip = fh.read(4) == b"PK\x03\x04"
    want = ".xlsx" if is_zip else ".xls"
    if path.suffix.lower() == want:
        return path
    fixed = tmp_dir / (path.stem + want)
    shutil.copyfile(path, fixed)
    return fixed


def read_excel(
    path: Path, spec: dict[str, Any]
) -> pl.DataFrame | dict[str, pl.DataFrame]:
    """Lê uma planilha XLS/XLSX.

    Args:
        path (Path): Caminho do arquivo de planilha.
        spec (dict[str, Any]): Especificação de processamento. ``sheet=None``
            lê a primeira aba; ``sheet=0`` lê todas as abas (dict); ``sheet=N``
            lê a N-ésima aba.

    Returns:
        pl.DataFrame | dict[str, pl.DataFrame]: DataFrame único ou dict de
            DataFrames por nome de aba.
    """
    sheet = spec.get("sheet")
    with tempfile.TemporaryDirectory() as tmp:
        source = _excel_path(path, Path(tmp))
        if sheet == "all":
            frames = pl.read_excel(source, sheet_id=0)
            assert isinstance(frames, dict), "sheet_id=0 deve retornar dict"
            return frames
        if sheet is None:
            return pl.read_excel(source, sheet_id=None)
        return pl.read_excel(source, sheet_id=sheet)


_OLE_MAGIC = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"


def read_file(
    path: Path, spec: dict[str, Any]
) -> pl.DataFrame | dict[str, pl.DataFrame]:
    """Lê um arquivo bruto conforme o formato e a especificação do grupo.

    Args:
        path (Path): Caminho do arquivo (csv, xls ou xlsx).
        spec (dict[str, Any]): Especificação de processamento do grupo.

    Returns:
        pl.DataFrame | dict[str, pl.DataFrame]: Dados lidos.

    Raises:
        ValueError: Se o formato não for suportado.
    """
    suffix = path.suffix.lower()
    with open(path, "rb") as fh:
        head = fh.read(4096)
    magic = head[:8]
    if suffix in (".csv", ".xls", ".xlsx") and magic.startswith(b"PK\x03\x04"):
        # A extensão nem sempre diz o conteúdo: movterm.csv é um xlsx, e
        # shpc-ca_2014-01.csv é um ZIP com o CSV dentro.
        with zipfile.ZipFile(path) as archive:
            is_xlsx = "[Content_Types].xml" in archive.namelist()
        if is_xlsx:
            return read_excel(path, spec)
        return read_file(decompress(path), spec)
    separator = spec.get("separator", ";").encode()
    if (
        suffix in (".xls", ".xlsx")
        and not magic.startswith(_OLE_MAGIC)
        and separator in head
    ):
        # multas-2021.xlsx é um CSV de texto.
        return read_csv(path, spec)
    if suffix == ".csv":
        return read_csv(path, spec)
    if suffix in (".xls", ".xlsx"):
        return read_excel(path, spec)
    if suffix == ".json":
        return read_json(path)
    raise ValueError(f"Formato não suportado: {suffix}")


def normalize_dtypes(df: pl.DataFrame, spec: dict[str, Any]) -> pl.DataFrame:
    """Normaliza dtypes: números com vírgula decimal e strings sem espaços.

    A conversão de números brasileiros (``,`` decimal, ``.`` de milhar) é
    delegada a ``quantilica.analytics.reader.normalize_brazilian_numbers``;
    colunas ausentes no DataFrame são ignoradas (best-effort).

    Args:
        df (pl.DataFrame): O DataFrame a normalizar.
        spec (dict[str, Any]): Especificação com ``numeric_columns``.

    Returns:
        pl.DataFrame: O DataFrame normalizado.
    """
    numeric = list(spec.get("numeric_columns", []))
    df = normalize_brazilian_numbers(
        df, [c for c in numeric if c in df.columns and df[c].dtype == pl.Utf8]
    )
    df = df.with_columns(
        [
            pl.col(col).str.strip_chars()
            for col in df.columns
            if col not in numeric and df[col].dtype == pl.Utf8
        ]
    )
    return df


def provenance_metadata(path: Path) -> dict[str, str]:
    """Lê o sidecar ``{path}.manifest.json`` e devolve metadados de proveniência.

    Args:
        path (Path): Caminho do arquivo de dados bruto.

    Returns:
        dict[str, str]: Metadados ``quantilica.*`` vazios se não houver manifest.
    """
    return manifest_to_metadata(read_manifest_sidecar(path))


def write_parquet(
    df: pl.DataFrame,
    target: Path,
    *,
    source_path: Path | None = None,
) -> Path:
    """Escreve um DataFrame como Parquet (zstd) com proveniência opcional.

    A escrita é atômica (write-temp-rename) e, quando o arquivo bruto de
    origem tem sidecar ``.manifest.json``, o manifest de download é
    reconstruído e delegado ao ``to_parquet`` canônico: os metadados
    ``quantilica.*`` são injetados no Parquet e um sidecar de proveniência é
    escrito ao lado do destino.

    Args:
        df (pl.DataFrame): O DataFrame a escrever.
        target (Path): Caminho de destino do Parquet.
        source_path (Path | None, optional): Arquivo bruto de origem, para
            injetar os metadados do manifest sidecar.

    Returns:
        Path: O caminho do Parquet escrito.
    """
    return to_parquet(df, target, source_path=source_path)


def _sidecar_manifest(path: Path) -> DownloadManifest | None:
    """Reconstroi o ``DownloadManifest`` do sidecar ``{path}.manifest.json``.

    Alias fino para ``quantilica.core.manifests.read_manifest_sidecar``.

    Args:
        path (Path): Caminho do arquivo bruto de origem.

    Returns:
        DownloadManifest | None: O manifest reconstruído, ou None quando o
            sidecar não existe ou é inválido.
    """
    return read_manifest_sidecar(path)
