"""Extração e leitura tipada de arquivos brutos da ANP.

Camada de conversão de dados coletados para Polars/Parquet, no padrão do
``pdet-fetcher`` (reader + wrangling). Lê CSV (latin-1/utf-8, separador ``;``,
decimal vírgula), XLS/XLSX (via ``pl.read_excel`` + fastexcel) e arquivos
ZIP/7z, normaliza dtypes e escreve Parquet com metadados de proveniência
extraídos do sidecar ``DownloadManifest``.
"""

from __future__ import annotations

import codecs
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
    r"(?:_(?P<year>\d{4})(?:-(?P<part>(?:S[12]|\d{2})))?)?"
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
    part_raw = g.get("part")
    mod = int(g["mod"]) if g["mod"] else None

    part: int | None = None
    partition: str | None = None
    if part_raw:
        if part_raw.startswith("S") or part_raw.startswith("s"):
            sem = int(part_raw[1:])
            part = sem
            partition = f"{year}-S{sem}"
        else:
            part = int(part_raw)
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


def _sniff_separator(path: Path, default: str) -> str:
    """Escolhe o separador pelo cabeçalho: ``;`` (padrão) ou ``,``.

    A maioria dos CSV da ANP usa ``;``, mas alguns arquivos do mesmo grupo
    usam ``,`` (ex.: ``vendas-biodiesel-b100-m3.csv``, ``producao-mar``);
    lidos com ``;`` eles viram uma coluna só ("Ano,Mês/Ano,Estado,..."). Vence
    o separador mais frequente na primeira linha, e o padrão no empate; um
    ``;`` solto num nome de coluna de um CSV com vírgulas não decide.

    Args:
        path (Path): Caminho do arquivo CSV (já em UTF-8 ou 8 bits).
        default (str): O separador da especificação do grupo.

    Returns:
        str: O separador a usar.
    """
    with path.open("rb") as fh:
        header = fh.readline()
    if default != "," and header.count(b",") > header.count(default.encode()):
        return ","
    return default


def _transcode_codec(path: Path) -> str | None:
    """O codec que o polars não lê sozinho: UTF-16 ou DOS (cp850).

    ``comercializacao-gn`` vem em UTF-16 LE com BOM; lido como 8 bits, os NUL
    e o BOM (``ÿþ``) entram nos nomes das colunas. Alguns ``multas-*`` saem em
    cp850: lidos como latin-1, ``ê`` (0x88) vira um caractere de controle no
    nome da coluna.

    Returns:
        str | None: ``"utf-16"`` (BOM), ``"utf-16-le"``, ``"utf-16-be"``,
            ``"cp850"`` ou ``None`` quando UTF-8/latin-1 servem.
    """
    with path.open("rb") as fh:
        head = fh.read(1 << 20)
    if head[:2] in (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE):
        return "utf-16"
    if _is_dos_text(head):
        return "cp850"
    head = head[:4096]
    pairs = len(head) // 2
    if pairs < 4:
        return None
    even = head[0 : pairs * 2 : 2].count(0)
    odd = head[1 : pairs * 2 : 2].count(0)
    # texto latino em UTF-16: o byte alto é NUL em (quase) todos os caracteres
    if odd > pairs * 0.4 and even == 0:
        return "utf-16-le"
    if even > pairs * 0.4 and odd == 0:
        return "utf-16-be"
    return None


_INNER_C1 = re.compile(rb"[A-Za-z][\x80-\x9f][A-Za-z]")


def _is_dos_text(sample: bytes) -> bool:
    """Texto em cp850: não é UTF-8 e tem byte 0x80-0x9f no meio de palavra.

    Em latin-1 esses bytes são controles; em cp850 são letras acentuadas
    (``Superintend\\x88ncia`` = Superintendência). Aspas e travessões do cp1252
    também caem nessa faixa, mas vêm junto de espaço, não no meio da palavra.
    """
    if not _INNER_C1.search(sample):
        return False
    decoder = codecs.getincrementaldecoder("utf-8")()
    try:
        decoder.decode(sample, final=False)
    except UnicodeDecodeError:
        return True
    return False


def _transcode_to_utf8(path: Path, codec: str, target: Path) -> Path:
    """Regrava ``path`` em UTF-8 (em blocos, sem carregar o arquivo)."""
    decoder = codecs.getincrementaldecoder(codec)()
    with path.open("rb") as src, target.open("wb") as dst:
        while chunk := src.read(1 << 24):
            dst.write(decoder.decode(chunk).encode("utf-8"))
        dst.write(decoder.decode(b"", final=True).encode("utf-8"))
    return target


_CONTROL_RUN = re.compile(r"[\x00-\x20\x7f-\xa0\u200b-\u200f\u2028\u2029\ufeff]+")
MAX_COLUMN_NAME = 128


_BLANK_NAME = re.compile(r"(_duplicated_\d+|__blank_\d+|__UNNAMED__\d+)?")


def _blank(value: Any) -> bool:
    """Célula sem conteúdo: nula ou só espaços."""
    return value is None or str(value).strip() == ""


def _blank_name(name: str) -> bool:
    """Nome de coluna sem conteúdo: vazio ou o ``_duplicated_N`` do polars.

    O polars dá ``_duplicated_N`` à segunda coluna de nome vazio (célula
    mesclada, delimitador sobrando) e ``__UNNAMED__N`` ao cabeçalho vazio de
    uma planilha; o nome em si continua vazio.
    """
    return _BLANK_NAME.fullmatch(_CONTROL_RUN.sub(" ", name).strip()) is not None


def _unique(names: list[str]) -> list[str]:
    """Nomes sem repetição (a segunda ocorrência ganha ``_2``, a terceira ``_3``)."""
    seen: dict[str, int] = {}
    out = []
    for name in names:
        seen[name] = seen.get(name, 0) + 1
        out.append(name if seen[name] == 1 else f"{name}_{seen[name]}")
    return out


def _promote_header(df: pl.DataFrame) -> pl.DataFrame:
    """Usa como cabeçalho a primeira linha densa quando o topo é preâmbulo.

    Alguns CSV começam por título e linhas em branco (``multas``: "ANP - Agência
    Nacional..." e "RELAÇÃO DE MULTAS ..." antes do cabeçalho) ou por uma linha
    de grupos mesclados (``acervo-dados-tecnicos``). O leitor tomava essa
    primeira linha como nomes de colunas. Só age quando menos da metade dos
    nomes tem conteúdo e uma das 30 primeiras linhas tem ao menos 80% das
    células preenchidas; arquivos com cabeçalho normal passam intactos.
    """
    width = df.width
    if width < 2 or not all(t == pl.String for t in df.schema.values()):
        return df
    names_filled = sum(1 for c in df.columns if not _blank_name(c))
    if names_filled >= width * 0.5:
        return df
    for i, row in enumerate(df.head(30).rows()):
        filled = sum(1 for v in row if not _blank(v))
        if filled >= width * 0.8:
            # vazio vira marcador único: o DataFrame não aceita nomes repetidos
            header = [
                f"__blank_{j}" if _blank(v) else str(v) for j, v in enumerate(row)
            ]
            body = df.slice(i + 1)
            body.columns = _unique(header)
            return body
    return df


def _clean_columns(df: pl.DataFrame) -> pl.DataFrame:
    """Garante nomes de colunas válidos: sem controle, não vazios, únicos, <= 128.

    - Controles, quebras de linha e espaços repetidos viram um espaço só
      (``"PCS GP\\n(kJ/m³)"`` -> ``"PCS GP (kJ/m³)"``).
    - Nome vazio (delimitador sobrando no fim do cabeçalho, célula mesclada): a
      coluna é descartada quando não tem nenhum valor; com valores, ganha o
      nome estável ``coluna_<posição>`` (posição 1-based no arquivo).
    - Nome com mais de 128 caracteres é cortado; repetidos ganham ``_2``, ``_3``.
    """
    keep: list[str] = []
    final: list[str] = []
    seen: set[str] = set()
    for pos, col in enumerate(df.columns, start=1):
        name = _CONTROL_RUN.sub(" ", col).strip()
        if _blank_name(name):
            series = df[col]
            if series.dtype == pl.String:
                series = series.str.strip_chars().replace("", None)
            if series.null_count() == series.len():
                continue
            name = f"coluna_{pos}"
        name = name[:MAX_COLUMN_NAME].rstrip()
        candidate, n = name, 1
        while candidate in seen:
            n += 1
            suffix = f"_{n}"
            candidate = name[: MAX_COLUMN_NAME - len(suffix)].rstrip() + suffix
        seen.add(candidate)
        keep.append(col)
        final.append(candidate)
    out = df.select(keep)
    out.columns = final
    return out


def _read_csv_8bit(path: Path, spec: dict[str, Any]) -> pl.DataFrame:
    """Lê um CSV da ANP de 8 bits (utf-8 com fallback latin-1).

    Args:
        path (Path): Caminho do arquivo CSV.
        spec (dict[str, Any]): Especificação de processamento do grupo.

    Returns:
        pl.DataFrame: O DataFrame lido com tipos inferidos.
    """
    kwargs: dict[str, Any] = {
        "separator": _sniff_separator(path, spec.get("separator", ";")),
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


def read_csv(path: Path, spec: dict[str, Any]) -> pl.DataFrame:
    """Lê um CSV da ANP e devolve colunas com nomes válidos.

    Aceita UTF-8 (com ou sem BOM), latin-1, cp850 e UTF-16 (os dois últimos
    regravados em UTF-8 antes da leitura); o separador (``;`` ou ``,``) sai do
    cabeçalho. Preâmbulo no topo é descartado (:func:`_promote_header`) e os
    nomes passam por :func:`_clean_columns`.

    Args:
        path (Path): Caminho do arquivo CSV.
        spec (dict[str, Any]): Especificação de processamento do grupo.

    Returns:
        pl.DataFrame: O DataFrame lido com tipos inferidos.
    """
    codec = _transcode_codec(path)
    if codec is None:
        df = _read_csv_8bit(path, spec)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            utf8 = _transcode_to_utf8(path, codec, Path(tmp) / "utf8.csv")
            df = _read_csv_8bit(utf8, {**spec, "encoding": "utf-8"})
    if not spec.get("skip_rows"):
        df = _promote_header(df)
    return _clean_columns(df)


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
        return _clean_columns(pl.from_dicts(data))
    except Exception:
        keys = {k for row in data for k in row}
        return _clean_columns(
            pl.from_dicts(data, schema_overrides={k: pl.String for k in keys})
        )


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
            return {name: _clean_columns(f) for name, f in frames.items()}
        if sheet is None:
            return _clean_columns(pl.read_excel(source, sheet_id=None))
        return _clean_columns(pl.read_excel(source, sheet_id=sheet))


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
    # Os semestres SHPC de 2022 em diante vêm em .zip com um CSV dentro.
    if suffix in (".zip", ".csv", ".xls", ".xlsx") and magic.startswith(b"PK\x03\x04"):
        # A extensão nem sempre diz o conteúdo: movterm.csv é um xlsx, e
        # shpc-ca_2014-01.csv é um ZIP com o CSV dentro.
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
        if "[Content_Types].xml" in names:
            return read_excel(path, spec)
        csv_members = sorted(n for n in names if n.lower().endswith(".csv"))
        if len(csv_members) > 1:
            return _read_zip_csvs(path, csv_members, spec)
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


def _read_zip_csvs(
    path: Path, members: list[str], spec: dict[str, Any]
) -> pl.DataFrame:
    """Lê e empilha os CSV de um ZIP (ex.: ZIP anual do PMQC, um CSV por mês).

    Os membros entram em ordem de nome; os JSON gêmeos do ZIP são ignorados.
    """
    frames = []
    with zipfile.ZipFile(path) as archive, tempfile.TemporaryDirectory() as tmp:
        for i, member in enumerate(members):
            # nome neutro: evita path traversal e colisão entre pastas do ZIP
            target = Path(tmp) / f"{i:04d}.csv"
            with archive.open(member) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
            frames.append(read_csv(target, spec))
    # colunas vazias descartadas em um membro e não em outro não podem quebrar a união
    return pl.concat(frames, how="diagonal_relaxed")


def normalize_dtypes(df: pl.DataFrame, spec: dict[str, Any]) -> pl.DataFrame:
    """Normaliza dtypes: strings sem espaços, números e datas tipados.

    A conversão de números brasileiros (``,`` decimal, ``.`` de milhar) é
    delegada a ``quantilica.analytics.reader.normalize_brazilian_numbers``;
    as datas usam o formato de ``date_columns``. Colunas ausentes no
    DataFrame são ignoradas. Valor vazio vira nulo; valor não vazio que não
    converte levanta erro.

    Args:
        df (pl.DataFrame): O DataFrame a normalizar.
        spec (dict[str, Any]): Especificação com ``numeric_columns`` e
            ``date_columns`` (coluna → formato ``strptime``).

    Returns:
        pl.DataFrame: O DataFrame normalizado.

    Raises:
        ValueError: Se um valor não vazio não converter.
    """
    numeric = list(spec.get("numeric_columns", []))
    dates = dict(spec.get("date_columns", {}))
    df = df.with_columns(
        [
            pl.col(col).str.strip_chars()
            for col in df.columns
            if df[col].dtype == pl.Utf8
        ]
    )
    # Vazio é ausência; qualquer outro valor que não converta é erro, não nulo.
    df = df.with_columns(
        [
            pl.when(pl.col(col) == "").then(None).otherwise(pl.col(col)).alias(col)
            for col in [*numeric, *dates]
            if col in df.columns and df[col].dtype == pl.Utf8
        ]
    )
    to_number = [c for c in numeric if c in df.columns and df[c].dtype == pl.Utf8]
    before = {c: df[c] for c in to_number}
    df = normalize_brazilian_numbers(df, to_number)
    for col, raw in before.items():
        _check_conversion(col, raw, df[col])
    for col, fmt in dates.items():
        if col in df.columns and df[col].dtype == pl.Utf8:
            raw = df[col]
            df = df.with_columns(pl.col(col).str.strptime(pl.Date, fmt, strict=False))
            _check_conversion(col, raw, df[col])
    code_cols = [
        c for c in df.columns if any(k in c.lower() for k in ("ibge", "cnpj", "poco"))
    ]
    if code_cols:
        df = df.with_columns(
            [pl.col(c).cast(pl.String) for c in code_cols if df.schema[c] != pl.String]
        )
    return df


def _check_conversion(col: str, raw: pl.Series, converted: pl.Series) -> None:
    """Falha se algum valor não vazio virou nulo na conversão.

    Raises:
        ValueError: Com a coluna, a quantidade e até cinco exemplos.
    """
    lost = raw.filter(raw.is_not_null() & converted.is_null())
    if lost.len():
        examples = lost.unique().head(5).to_list()
        raise ValueError(
            f"Coluna {col!r}: {lost.len()} valor(es) não convertido(s), ex.: {examples}"
        )


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
