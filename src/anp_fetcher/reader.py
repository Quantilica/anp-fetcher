"""Extração e leitura tipada de arquivos brutos da ANP.

Camada de conversão de dados coletados para Polars/Parquet, no padrão do
``pdet-fetcher`` (reader + wrangling). Lê CSV (latin-1/utf-8, separador ``;``,
decimal vírgula), XLS/XLSX (via ``pl.read_excel`` + fastexcel) e arquivos
ZIP/7z, normaliza dtypes e escreve Parquet com metadados de proveniência
extraídos do sidecar ``DownloadManifest``.
"""

from __future__ import annotations

import codecs
import csv
import io
import itertools
import logging
import os
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


def decompress(path: Path, output_dir: Path | None = None) -> Path:
    """Descompacta um arquivo ZIP/7z e retorna o primeiro arquivo de dados.

    A extração é delegada a ``quantilica.core.files.decompress_archive``
    (nativa para ZIP/TAR com proteção contra path traversal, fallback
    ``7z``). O contrato público do módulo é preservado: falhas de extração
    sobem como ``RuntimeError``.

    Args:
        path (Path): O caminho do arquivo compactado.
        output_dir (Path | None): Pasta de destino. Sem ela, a extração vai para
            uma pasta temporária que o chamador precisa remover.

    Returns:
        Path: O caminho do arquivo extraído (primeiro csv/xls/xlsx encontrado).

    Raises:
        RuntimeError: Se a extração falhar ou não produzir arquivos de dados.
    """
    logger.info("Descompactando %s", path)
    try:
        return decompress_archive(
            path, output_dir, target_extensions=(".csv", ".xls", ".xlsx")
        )
    except StorageError as exc:
        raise RuntimeError(f"falha ao descompactar {path}: {exc}") from exc


# Membros de ZIP que o leitor abre. O JSON que a ANP publica ao lado de cada CSV
# (PMQC) é o mesmo dado em outro formato: fica de fora, o CSV é o que vale.
_MEMBER_SUFFIXES = (".csv", ".xls", ".xlsx")


def scratch_dir() -> str | None:
    """Pasta para temporários: o scratch do ``lake build`` ou o temp do sistema.

    Usa ``QUANTILICA_LAKE_SCRATCH`` quando definido e existente; nunca fica ao
    lado do bruto (um worker morto deixaria a pasta dentro da visão vigente).
    """
    scratch = os.environ.get("QUANTILICA_LAKE_SCRATCH") or None
    return scratch if scratch and os.path.isdir(scratch) else None


def _is_junk_member(name: str) -> bool:
    """Ruído de arquivo compactado: ``__MACOSX/``, locks do Office, ``Thumbs.db``."""
    parts = name.replace("\\", "/").split("/")
    base = parts[-1].lower()
    return (
        "__macosx" in (p.lower() for p in parts[:-1])
        or base.startswith(("~$", "."))
        or base == "thumbs.db"
        or base.startswith("md5_")
    )


def zip_data_members(path: Path) -> list[str]:
    """Membros de dados (csv/xls/xlsx) de um ZIP, em ordem de nome.

    Pastas, ruído (``Thumbs.db``, ``__MACOSX/``), PDF e JSON ficam de fora. Um
    ZIP que na verdade é uma planilha (``[Content_Types].xml``) não tem membros:
    é o próprio arquivo de dados.

    Args:
        path (Path): O arquivo ZIP.

    Returns:
        list[str]: Os nomes dos membros, como no ZIP.

    Raises:
        zipfile.BadZipFile: Se o arquivo não for um ZIP.
    """
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
    if "[Content_Types].xml" in names:
        return []
    return sorted(
        n
        for n in names
        if not n.endswith("/")
        and n.lower().endswith(_MEMBER_SUFFIXES)
        and not _is_junk_member(n)
    )


def extract_zip_member(path: Path, member: str, dest_dir: Path) -> Path:
    """Extrai um membro do ZIP para ``dest_dir`` com nome neutro e a mesma extensão.

    O nome neutro evita path traversal e colisão entre membros de pastas
    diferentes; a extensão fica porque o leitor escolhe o formato por ela.

    Args:
        path (Path): O arquivo ZIP.
        member (str): O nome do membro, como no ZIP.
        dest_dir (Path): Pasta de destino (existente).

    Returns:
        Path: O arquivo extraído.
    """
    target = Path(dest_dir) / f"membro{Path(member).suffix.lower()}"
    with zipfile.ZipFile(path) as archive, archive.open(member) as src:
        with open(target, "wb") as dst:
            shutil.copyfileobj(src, dst)
    return target


def _field_counts(text: str, separator: str, limit: int) -> list[int]:
    """Quantidade de campos das primeiras linhas (com aspas, como o CSV)."""
    rows = csv.reader(io.StringIO(text), delimiter=separator)
    counts = []
    try:
        for row in rows:
            counts.append(len(row))
            if len(counts) >= limit:
                break
    except csv.Error:
        pass
    return counts


def _sniff_separator(path: Path, default: str) -> str:
    """Escolhe o separador (``;`` padrão ou ``,``) pela consistência das colunas.

    A maioria dos CSV da ANP usa ``;``, mas alguns arquivos do mesmo grupo usam
    ``,`` (``producao-mar``, ``armazenagem-terminais``); lidos com ``;`` eles
    viram uma coluna só ("Ano,Mês/Ano,Estado,..."). Para cada candidato conta
    os campos do cabeçalho e das 20 linhas seguintes: vale o que dá mais de um
    campo no cabeçalho e o mesmo número nas linhas de dados. O padrão fica no
    empate, então vírgulas dentro de nomes (``Preço (R$/l, média)``) ou um ``;``
    solto num nome de CSV com vírgulas não decidem.

    Args:
        path (Path): Caminho do arquivo CSV (já em UTF-8 ou 8 bits).
        default (str): O separador da especificação do grupo.

    Returns:
        str: O separador a usar.
    """
    with path.open("rb") as fh:
        text = fh.read(1 << 16).decode("latin-1").lstrip("\xef\xbb\xbf")
    if default == ",":
        return default

    def score(sep: str) -> tuple[bool, float, int]:
        counts = _field_counts(text, sep, 21)
        if not counts:
            return (False, 0.0, 0)
        head, rest = counts[0], counts[1:]
        same = sum(1 for c in rest if c == head) / len(rest) if rest else 1.0
        return (head > 1, same, head)

    return "," if score(",") > score(default) else default


_PT_LETTERS = frozenset("áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ")
_EIGHT_BIT = ("cp1252", "cp850", "mac_roman")


_MIN_LETRAS = 3


def _eight_bit_codec(sample: bytes) -> str | None:
    """``cp850`` ou ``mac_roman`` quando decodificam melhor que o latin-1/cp1252.

    Só vale para o que não é UTF-8. Decodifica a amostra nos três codecs e fica
    com o que gera mais letras acentuadas do português; ``cp1252`` (igual ao
    latin-1 fora de 0x80-0x9f) ou empate devolvem ``None``, o caminho de sempre.
    ``multas-*`` vem em cp850 (``ê`` = 0x88, controle em latin-1) e
    ``prorrogacoes-708`` em mac_roman; já o 0x92 de ``ATEM\x92S`` é o apóstrofo
    do cp1252, não uma letra cp850.
    """
    decoder = codecs.getincrementaldecoder("utf-8")()
    try:
        decoder.decode(sample, final=False)
        return None
    except UnicodeDecodeError:
        pass
    scores = {
        enc: sum(ch in _PT_LETTERS for ch in sample.decode(enc, "replace"))
        for enc in _EIGHT_BIT
    }
    best = max(_EIGHT_BIT, key=lambda enc: scores[enc])
    if best == "cp1252":
        return None
    # Margem mínima: um arquivo curto sem acentos e com um apóstrofo cp1252
    # (0x92) daria 1 a 0 para o mac_roman. Só troca com evidência clara.
    if scores[best] < _MIN_LETRAS or scores[best] < 2 * scores["cp1252"]:
        return None
    return best


def _transcode_codec(path: Path, *, eight_bit: bool = True) -> str | None:
    """O codec que o polars não lê sozinho: UTF-16, cp850 ou mac_roman.

    ``comercializacao-gn`` vem em UTF-16 LE com BOM; lido como 8 bits, os NUL
    e o BOM (``ÿþ``) entram nos nomes das colunas.

    Args:
        path (Path): O arquivo.
        eight_bit (bool): Também procura cp850/mac_roman (desligado quando o
            grupo fixa o encoding).

    Returns:
        str | None: ``"utf-16"`` (BOM), ``"utf-16-le"``, ``"utf-16-be"``,
            ``"cp850"``, ``"mac_roman"`` ou ``None`` quando UTF-8/latin-1 servem.
    """
    with path.open("rb") as fh:
        head = fh.read(1 << 20)
    if head[:2] in (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE):
        return "utf-16"
    probe = head[:4096]
    pairs = len(probe) // 2
    if pairs >= 4:
        even = probe[0 : pairs * 2 : 2].count(0)
        odd = probe[1 : pairs * 2 : 2].count(0)
        # texto latino em UTF-16: o byte alto é NUL em (quase) todos os caracteres
        if odd > pairs * 0.4 and even == 0:
            return "utf-16-le"
        if even > pairs * 0.4 and odd == 0:
            return "utf-16-be"
    return _eight_bit_codec(head) if eight_bit else None


def _transcode_to_utf8(path: Path, codec: str, target: Path) -> Path:
    """Regrava ``path`` em UTF-8 (em blocos, sem carregar o arquivo)."""
    decoder = codecs.getincrementaldecoder(codec)()
    with path.open("rb") as src, target.open("wb") as dst:
        while chunk := src.read(1 << 24):
            dst.write(decoder.decode(chunk).encode("utf-8"))
        dst.write(decoder.decode(b"", final=True).encode("utf-8"))
    return target


_CONTROL_RUN = re.compile(r"[\x00-\x1f\x7f-\x9f]+")
_NUMBER = re.compile(r"[-+]?\d+([.,]\d+)*(e[-+]?\d+)?%?", re.IGNORECASE)
_BLANK_NAME = re.compile(r"(_duplicated_\d+|__blank_\d+)?")
MAX_COLUMN_NAME = 128


def _blank(value: Any) -> bool:
    """Célula sem conteúdo: nula ou só espaços."""
    return value is None or str(value).strip() == ""


def _blank_name(name: str) -> bool:
    """Nome de coluna sem conteúdo: vazio ou o ``_duplicated_N`` do polars.

    O polars dá ``_duplicated_N`` à segunda coluna de nome vazio (célula
    mesclada, delimitador sobrando); o nome em si continua vazio.
    """
    return _BLANK_NAME.fullmatch(name.strip()) is not None


def _unique(names: list[str]) -> list[str]:
    """Nomes sem repetição (a segunda ocorrência ganha ``_2``, a terceira ``_3``)."""
    seen: dict[str, int] = {}
    out = []
    for name in names:
        seen[name] = seen.get(name, 0) + 1
        out.append(name if seen[name] == 1 else f"{name}_{seen[name]}")
    return out


def _promote_header(df: pl.DataFrame) -> pl.DataFrame:
    """Usa como cabeçalho a primeira linha de nomes quando o topo é preâmbulo.

    Alguns CSV começam por título e linhas em branco (``multas``: "ANP - Agência
    Nacional..." e "RELAÇÃO DE MULTAS ..." antes do cabeçalho) ou por uma linha
    de grupos mesclados (``acervo-dados-tecnicos``). O leitor tomava essa
    primeira linha como nomes de colunas. Só age quando:

    - menos da metade dos nomes lidos tem conteúdo (a linha é preâmbulo);
    - toda linha entre ela e a candidata também é esparsa (menos da metade
      preenchida), para nunca pular dado;
    - a candidata tem ao menos 80% das células preenchidas e nenhuma numérica
      (um cabeçalho de dados reais, como ``A;;;`` seguido de ``1;x;y;z``, fica).
    """
    width = df.width
    if width < 2 or not all(t == pl.String for t in df.schema.values()):
        return df
    if sum(1 for c in df.columns if not _blank_name(c)) >= width * 0.5:
        return df
    for i, row in enumerate(df.head(30).rows()):
        filled = sum(1 for v in row if not _blank(v))
        if filled < width * 0.5:
            continue  # mais preâmbulo
        if filled < width * 0.8 or any(
            not _blank(v) and _NUMBER.fullmatch(str(v).strip()) for v in row
        ):
            return df
        # vazio vira marcador único: o DataFrame não aceita nomes repetidos
        header = [f"__blank_{j}" if _blank(v) else str(v) for j, v in enumerate(row)]
        body = df.slice(i + 1)
        body.columns = _unique(header)
        return body
    return df


_DATE_LIKE = re.compile(r"\d{1,4}[/.-]\d{1,2}([/.-]\d{1,4})?([ T]\d.*)?")
_HEADER_SCAN = 15  # linhas do topo em que se procura o cabeçalho
_MAX_SUBHEADERS = 3
_MIN_FALLBACK_WIDTH = 8  # folhas estreitas (formulários de preço) só pelo âncora


def _cell(value: Any) -> str:
    """Texto da célula: espaços repetidos e quebras viram um espaço; vazio é ``""``."""
    return "" if value is None else re.sub(r"\s+", " ", str(value)).strip()


def _data_like(text: str) -> bool:
    """Número, data ou período (``2005/01``): valor de linha de dados, não de nome."""
    return bool(_NUMBER.fullmatch(text) or _DATE_LIKE.fullmatch(text))


def _locate_header(rows: list[list[str]], width: int, anchor: str | None) -> int | None:
    """Índice da linha de cabeçalho nas primeiras linhas, ou ``None``.

    Com ``anchor`` (regex), é a primeira linha cuja primeira célula preenchida casa.
    Sem âncora (ou sem achar uma, em folha larga), é a primeira com 40% ou mais
    das células preenchidas (célula mesclada deixa o resto vazio) e só texto: o
    título e a data acima têm uma ou duas.
    """
    top = rows[:_HEADER_SCAN]
    if anchor:
        pattern = re.compile(anchor, re.IGNORECASE)
        for i, row in enumerate(top):
            cells = [c for c in row if c]
            if cells and pattern.search(cells[0]):
                return i
    if width < _MIN_FALLBACK_WIDTH and anchor:
        return None
    for i, row in enumerate(top):
        cells = [c for c in row if c]
        if len(cells) >= max(4, 0.4 * width) and not any(_data_like(c) for c in cells):
            return i
    return None


def _levels_names(levels: list[list[str]]) -> list[str]:
    """Nome de cada coluna a partir dos níveis do cabeçalho (cima para baixo).

    Célula mesclada vira vazia à direita: o nível herda o texto da esquerda, mas só
    nas colunas que têm texto em algum nível abaixo (``Gás Natural (Mm³/dia)`` sobre
    ``Associado``, ``Não Associado`` e ``Gás Total``).
    """
    width = len(levels[0])
    filled: list[list[str]] = []
    for r, row in enumerate(levels):
        out, current = [], ""
        for j in range(width):
            deeper = any(levels[k][j] for k in range(r + 1, len(levels)))
            if row[j]:
                current = row[j]
                out.append(row[j])
            elif deeper:
                out.append(current)
            else:
                current = ""
                out.append("")
        filled.append(out)
    return [
        _join_levels([filled[r][j] for r in range(len(levels))]) for j in range(width)
    ]


def _join_levels(parts: list[str]) -> str:
    """Junta os níveis de um nome; o nível que repete o que já está no nome some.

    ``CÓDIGO IBGE`` com ``IBGE`` embaixo (célula mesclada em duas linhas) é só
    ``CÓDIGO IBGE``.
    """
    name = ""
    for part in parts:
        if part and not re.search(
            rf"(?<!\w){re.escape(part.casefold())}(?!\w)", name.casefold()
        ):
            name = f"{name} {part}".strip()
    return name


_FILLER_ROW = re.compile(r"x{3,}", re.IGNORECASE)
# linha de nota/rodapé/filtro: nunca é o título de uma tabela
_NOT_A_TITLE = re.compile(
    r"^(selecione|fonte|notas?:|dados atualizados|voltar|periodicidade|\W*\d?\W*varia)",
    re.IGNORECASE,
)
_TITLE_MIN_CHARS = 25


def _block_end(rows: list[list[str]], start: int) -> int:
    """Primeira linha, a partir de ``start``, que já não é dado da tabela.

    Dado é a linha com duas ou mais células preenchidas que não seja a faixa de
    ``xxxx`` com que a planilha separa as tabelas.
    """
    end = start
    while end < len(rows):
        cells = [c for c in rows[end] if c]
        if len(cells) < 2 or all(_FILLER_ROW.fullmatch(c) for c in cells):
            break
        end += 1
    return end


def _block_title(rows: list[list[str]], start: int, header: int) -> str | None:
    """Título da tabela cujo cabeçalho está em ``header``.

    Candidata a título é a linha de uma célula só, de texto longo, que não seja
    nota nem filtro. Depois do ``Voltar ao índice`` da tabela anterior o título é
    a primeira candidata (as notas ``ATENÇÃO`` vêm depois dele); na primeira tabela,
    antes da qual há o índice e as notas da planilha, é a última candidata.
    """
    candidates: list[str] = []
    after_back = False
    for i in range(start, header):
        cells = [c for c in rows[i] if c]
        if cells and cells[0].casefold().startswith("voltar"):
            candidates, after_back = [], True
        elif (
            len(cells) == 1
            and len(cells[0]) >= _TITLE_MIN_CHARS
            and not _NOT_A_TITLE.match(cells[0])
        ):
            candidates.append(cells[0])
    if not candidates:
        return None
    return candidates[0] if after_back else candidates[-1]


_FOOTNOTE_MARK = re.compile(r"\s*[¹²³⁴⁵⁶⁷⁸⁹⁰]+$")
_YEAR_PAIR = re.compile(r"\s*\d{4}\s*/\s*\d{4}")
_YEAR_COLUMN = re.compile(r"ANO (\d{4})$")


def _table_names(rows: list[list[str]], header: int, width: int) -> list[str]:
    """Nomes das colunas de uma tabela de painel (``Mês``, ``ANO 2000``, ...).

    A linha de cima entra como primeiro nível quando tem texto de cabeçalho (``ANO``
    mesclado sobre os anos, ``VARIAÇÃO DO ACUMULADO``). A marca de nota (``¹``) e
    os anos da variação (``NO ANO 2026 / 2025 (%)``, que mudam por tabela e por
    ano) saem do nome; o primeiro nome (``MÊS``, ``Meses``) é sempre ``Mês``.
    """
    above = rows[header - 1] if header else [""] * width
    cells = [c for c in above if c]
    has_above = (
        0 < len(cells) <= 0.6 * width
        and not any(_data_like(c) for c in cells)
        and not all(_FILLER_ROW.fullmatch(c) for c in cells)
    )
    levels = [above, rows[header]] if has_above else [rows[header]]
    names = []
    for j, name in enumerate(_levels_names(levels)):
        name = _YEAR_PAIR.sub("", _FOOTNOTE_MARK.sub("", name)).strip()
        name = re.sub(r"\s+", " ", name)
        names.append("Mês" if j == 0 else name or f"__blank_{j}")
    return _unique(names)


def _stacked_tables(df: pl.DataFrame, anchor: str) -> pl.DataFrame | None:
    """Empilha as tabelas de uma planilha de painel da ANP; ``None`` se não há.

    Os painéis estatísticos (``ie``, ``pp``, ``pb``, ``ppg``, ``vdpb``) são uma
    planilha com várias tabelas uma sobre a outra: título, filtros, a faixa de
    ``xxxx``, o cabeçalho (``Mês`` e os anos, com ``ANO`` mesclado na linha de
    cima), os meses, ``Total do Ano`` e as notas. Cada tabela é achada pela linha
    cuja primeira célula casa ``anchor`` (às vezes na segunda coluna, como em
    ``vendas``) e entra com as suas linhas de dado e os seus próprios nomes: as
    tabelas começam em anos diferentes (``ANO 2012``) e as colunas se juntam pelo
    nome, em vez de pela posição. A coluna ``tabela`` diz de qual veio a linha.
    Colunas só com números viram ``Float64``.
    """
    rows = [[_cell(v) for v in row] for row in df.rows()]
    pattern = re.compile(anchor, re.IGNORECASE)
    headers: list[tuple[int, int]] = []  # (linha, coluna da célula ``Mês``)
    for i, row in enumerate(rows):
        left = next((j for j, c in enumerate(row) if c), None)
        if (
            left is not None
            and pattern.search(row[left])
            and sum(1 for c in row if c) >= 3  # ``Mês`` e ao menos dois anos
        ):
            headers.append((i, left))
    if not headers:
        return None
    order: list[str] = []
    records: list[dict[str, str | None]] = []
    previous_end = 0
    for header, left in headers:
        table = [row[left:] for row in rows]
        names = _table_names(table, header, len(table[0]))
        end = _block_end(table, header + 1)
        title = _block_title(rows, previous_end, header)
        order.extend(n for n in names if n not in order)
        records.extend(
            {"tabela": title, **{n: c or None for n, c in zip(names, row, strict=True)}}
            for row in table[header + 1 : end]
        )
        previous_end = end
    if not records:
        return None
    years = sorted((n for n in order if _YEAR_COLUMN.fullmatch(n)), key=lambda n: n[4:])
    columns = ["tabela", "Mês", *years, *(n for n in order[1:] if n not in years)]
    frame: dict[str, pl.Series] = {}
    for name in columns:
        series = pl.Series(name, [r.get(name) for r in records], pl.String)
        if name not in ("tabela", "Mês"):
            number = series.cast(pl.Float64, strict=False)
            if number.null_count() == series.null_count():
                series = number
        frame[name] = series
    return pl.DataFrame(frame)


def _real_header(
    df: pl.DataFrame, *, headerless: bool, options: dict[str, Any]
) -> pl.DataFrame:
    """Põe o cabeçalho de verdade nos nomes e tira o resto do topo.

    Planilhas da ANP começam por título e data (``ANP - Agência...``,
    ``Data: 15/03/2019``), têm o cabeçalho em até três níveis (célula mesclada) e às
    vezes repetem o cabeçalho no meio dos dados. Aqui o cabeçalho é a primeira linha
    de texto com boa parte das células preenchidas (:func:`_locate_header`); as linhas
    de só texto logo abaixo, com menos de 60% preenchidas, são os níveis seguintes
    (``options["levels"]``); linhas em branco entre eles somem; e as linhas de dados
    que repetem um nível do cabeçalho são descartadas. Sem cabeçalho achado, o
    DataFrame passa como veio.

    Args:
        df (pl.DataFrame): O que o leitor devolveu, tudo texto.
        headerless (bool): ``True`` quando a primeira linha ainda é dado (planilha
            lida sem cabeçalho); ``False`` quando já virou nome de coluna (CSV).
        options (dict[str, Any]): ``anchor`` (regex da primeira célula do
            cabeçalho), ``levels`` (aceita níveis abaixo do cabeçalho: ``True`` até
            três, ou o número máximo), ``drop_blank`` (descarta linhas sem nenhuma
            célula preenchida) e ``tables``
            (regex do cabeçalho de planilha de painel, com várias tabelas
            empilhadas: :func:`_stacked_tables`).
    """
    width = df.width
    if width < 2 or not all(t == pl.String for t in df.schema.values()):
        return df
    if headerless and options.get("tables"):
        stacked = _stacked_tables(df, options["tables"])
        if stacked is not None:
            return stacked
    names = [] if headerless else [None if _blank_name(c) else c for c in df.columns]
    rows = ([] if headerless else [[_cell(v) for v in names]]) + [
        [_cell(v) for v in row] for row in df.head(_HEADER_SCAN).rows()
    ]
    header = _locate_header(rows, width, options.get("anchor"))
    if header is None:
        return df
    consumed = header + 1
    levels = [rows[header]]
    sublevels = options.get("levels")
    if sublevels:
        # ``True``: até ``_MAX_SUBHEADERS`` níveis; um número: no máximo esse tanto
        limit = _MAX_SUBHEADERS if sublevels is True else int(sublevels)
        while consumed < len(rows) and len(levels) <= limit:
            cells = [c for c in rows[consumed] if c]
            if not cells:
                consumed += 1  # linha em branco dentro do cabeçalho
                continue
            if len(cells) <= 0.6 * width and not any(_data_like(c) for c in cells):
                levels.append(rows[consumed])
                consumed += 1
                continue
            break
    final = [n if n else f"__blank_{j}" for j, n in enumerate(_levels_names(levels))]
    offset = consumed - (0 if headerless else 1)
    body = df.slice(offset)
    body.columns = _unique(final)
    # descarta as linhas que repetem um nível do cabeçalho
    repeats = [[c.casefold() for c in lv] for lv in levels]

    def is_repeat(row: tuple[Any, ...]) -> bool:
        cells = [_cell(v).casefold() for v in row]
        used = [c for c in cells if c]
        return bool(used) and any(
            all(not c or c == lv[j] for j, c in enumerate(cells)) for lv in repeats
        )

    drop_blank = bool(options.get("drop_blank"))
    keep = [
        not (drop_blank and all(_blank(v) for v in row)) and not is_repeat(row)
        for row in body.rows()
    ]
    return body.filter(pl.Series(keep)) if not all(keep) else body


def _valid_name(name: str) -> bool:
    """Nome que o lake aceita: não vazio, sem controle e com até 128 caracteres."""
    return (
        bool(name.strip())
        and len(name) <= MAX_COLUMN_NAME
        and _CONTROL_RUN.search(name) is None
    )


def _clean_columns(df: pl.DataFrame) -> pl.DataFrame:
    """Corrige só os nomes de coluna inválidos; os válidos passam como estão.

    - Controle e quebra de linha (``"PCS GP\\n(kJ/m³)"``) viram um espaço.
    - Nome vazio (delimitador sobrando no fim do cabeçalho, célula mesclada): a
      coluna é descartada quando não tem nenhum valor; com valores, ganha o
      nome estável ``coluna_<posição>`` (posição 1-based no arquivo).
    - Nome com mais de 128 caracteres é cortado; repetido ganha ``_2``, ``_3``.

    Espaços das pontas ou repetidos, e nomes como ``__UNNAMED__N``, não mudam.
    """
    keep: list[str] = []
    final: list[str] = []
    seen: set[str] = set()
    for pos, col in enumerate(df.columns, start=1):
        name = col
        if _blank_name(name):
            series = df[col]
            if series.dtype == pl.String:
                series = series.str.strip_chars().replace("", None)
            if series.null_count() == series.len():
                continue
            name = f"coluna_{pos}"
        elif not _valid_name(name):
            name = _CONTROL_RUN.sub(" ", name).strip()[:MAX_COLUMN_NAME].rstrip()
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


def _read_csv_8bit(path: Path, spec: dict[str, Any], **extra: Any) -> pl.DataFrame:
    """Lê um CSV da ANP de 8 bits (utf-8 com fallback latin-1).

    Args:
        path (Path): Caminho do arquivo CSV.
        spec (dict[str, Any]): Especificação de processamento do grupo.
        **extra: Opções do leitor do polars (``has_header``, ``n_rows``).

    Returns:
        pl.DataFrame: O DataFrame lido com tipos inferidos.
    """
    kwargs: dict[str, Any] = {
        "separator": _sniff_separator(path, spec.get("separator", ";")),
        "infer_schema_length": spec.get("infer_schema_length", 0),
    }
    if spec.get("skip_rows"):
        kwargs["skip_rows"] = spec["skip_rows"]
    kwargs.update(extra)
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

    Aceita UTF-8 (com ou sem BOM), latin-1 e, regravados em UTF-8 antes da
    leitura, UTF-16, cp850 e mac_roman; o separador (``;`` ou ``,``) sai da
    consistência das colunas. Preâmbulo no topo é descartado
    (:func:`_promote_header`) e os nomes inválidos passam por
    :func:`_clean_columns`.

    Args:
        path (Path): Caminho do arquivo CSV.
        spec (dict[str, Any]): Especificação de processamento do grupo.

    Returns:
        pl.DataFrame: O DataFrame lido com tipos inferidos.
    """
    columns = spec.get("columns")
    df = _read_csv_text(path, spec, **({"has_header": False} if columns else {}))
    if columns:
        if df.width != len(columns):
            raise ValueError(
                f"CSV sem cabeçalho com {df.width} colunas; os nomes dados são "
                f"{len(columns)}"
            )
        df.columns = _unique(list(columns))
    elif spec.get("header"):
        df = _real_header(df, headerless=False, options=spec["header"])
    elif not spec.get("skip_rows"):
        df = _promote_header(df)
    return _clean_columns(df)


def _read_csv_text(path: Path, spec: dict[str, Any], **extra: Any) -> pl.DataFrame:
    """Lê o CSV como texto, regravando antes em UTF-8 o que não é de 8 bits."""
    codec = _transcode_codec(path, eight_bit=spec.get("encoding") is None)
    if codec is None:
        return _read_csv_8bit(path, spec, **extra)
    # No scratch do `lake build` quando definido, senão no temp do sistema.
    with tempfile.TemporaryDirectory(
        prefix=".anp-utf8-", dir=scratch_dir(), ignore_cleanup_errors=True
    ) as tmp:
        utf8 = _transcode_to_utf8(path, codec, Path(tmp) / "utf8.csv")
        return _read_csv_8bit(utf8, {**spec, "encoding": "utf-8"}, **extra)


def _first_csv_row(path: Path, spec: dict[str, Any]) -> list[str]:
    """Células da primeira linha de um CSV de 8 bits (UTF-8 com BOM ou latin-1)."""
    separator = _sniff_separator(path, spec.get("separator", ";"))
    for encoding in ("utf-8-sig", "latin-1"):
        try:
            with open(path, encoding=encoding, newline="") as fh:
                return next(csv.reader(fh, delimiter=separator), [])
        except UnicodeDecodeError:
            continue
    return []


def _is_data_row(cells: list[str]) -> bool:
    """Linha de registro, não de cabeçalho: tem números ou datas em boa parte."""
    filled = [c.strip() for c in cells if c.strip()]
    numeric = [c for c in filled if _data_like(c)]
    return len(numeric) >= 2 and len(numeric) >= 0.25 * len(filled)


def csv_lacks_header(path: Path, spec: dict[str, Any]) -> bool:
    """``True`` quando a primeira linha do CSV já é um registro (sem cabeçalho)."""
    if _transcode_codec(path, eight_bit=spec.get("encoding") is None) is not None:
        return False
    return _is_data_row(_first_csv_row(path, spec))


def _numeric_column(values: list[str | None]) -> bool:
    """Coluna em que todo valor preenchido é número (e há algum)."""
    filled = [v.strip() for v in values if v is not None and v.strip()]
    return bool(filled) and all(_NUMBER.fullmatch(v) for v in filled)


_MAX_EXTRA_COLUMNS = 2


def headerless_columns(
    path: Path, reference: Path, spec: dict[str, Any], *, sample: int = 100_000
) -> list[str] | None:
    """Nomes das colunas de um CSV sem cabeçalho, tirados de um CSV irmão.

    Há membros de ZIP em que a ANP publica o arquivo sem a linha de cabeçalho
    (``Liquidos_Vendas_Historico_2007_a_2017``): a primeira linha de dados virava
    o nome das colunas (``2007``, ``1``, ``810101001``...). O irmão com cabeçalho
    (``..._2018_a_2023``, do mesmo dataset) dá os nomes. Quando o irmão tem colunas
    a mais (``Descrição do Produto``), vale o alinhamento que casa na posição o
    tipo (número ou texto) e os valores de cada coluna com os do irmão. Largura
    que não fecha, ou alinhamento sem vencedor claro, é erro.

    Args:
        path (Path): O CSV a conferir.
        reference (Path): O CSV irmão, com cabeçalho.
        spec (dict[str, Any]): Especificação de processamento do grupo.
        sample (int, optional): Linhas do irmão que servem de amostra.

    Returns:
        list[str] | None: Os nomes, ou ``None`` se ``path`` tem cabeçalho (ou se
            ``reference`` não tem).

    Raises:
        ValueError: Se a largura não bate ou o alinhamento é ambíguo.
    """
    first = _first_csv_row(path, spec)
    names = _first_csv_row(reference, spec)
    if not _is_data_row(first) or not names or _is_data_row(names):
        return None
    width, ref_width = len(first), len(names)
    if not 0 <= ref_width - width <= _MAX_EXTRA_COLUMNS:
        raise ValueError(
            f"CSV sem cabeçalho com {width} colunas; o irmão {reference.name} tem "
            f"{ref_width}: nomes não inferíveis"
        )
    if width == ref_width:
        return names
    head = _read_csv_text(path, spec, has_header=False, n_rows=2000)
    ref = _read_csv_text(reference, spec, n_rows=sample)
    scored = sorted(
        (
            (_alignment_score(head, ref, kept), kept)
            for kept in itertools.combinations(range(ref_width), width)
        ),
        reverse=True,
    )
    best, kept = scored[0]
    if best < 0 or (len(scored) > 1 and scored[1][0] >= best):
        raise ValueError(
            f"CSV sem cabeçalho com {width} colunas; o alinhamento com o irmão "
            f"{reference.name} ({ref_width} colunas) é ambíguo: nomes não inferíveis"
        )
    return [names[i] for i in kept]


def _alignment_score(
    head: pl.DataFrame, ref: pl.DataFrame, kept: tuple[int, ...]
) -> float:
    """Quanto as colunas de ``head`` casam com as colunas ``kept`` de ``ref``.

    ``-1`` quando o tipo (número ou texto) de alguma coluna não bate; senão, a soma,
    nas colunas de texto, da fração dos valores distintos de ``head`` que o irmão
    também tem na coluna.
    """
    score = 0.0
    for i, k in enumerate(kept):
        mine = head.to_series(i).to_list()
        theirs = ref.to_series(k).to_list()
        if _numeric_column(mine) != _numeric_column(theirs):
            return -1.0
        if _numeric_column(mine):
            continue
        values = {v for v in mine if v}
        known = {v for v in theirs if v}
        if values:
            score += len(values & known) / len(values)
    return score


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
    header = spec.get("header")
    # Com cabeçalho de verdade a achar, a planilha vem sem cabeçalho e tudo texto.
    extra: dict[str, Any] = {"has_header": False, "infer_schema_length": 0}
    kwargs = extra if header else {}

    def tidy(frame: pl.DataFrame) -> pl.DataFrame:
        if header:
            frame = _real_header(frame, headerless=True, options=header)
        return _clean_columns(frame)

    with tempfile.TemporaryDirectory(
        dir=scratch_dir(), ignore_cleanup_errors=True
    ) as tmp:
        source = _excel_path(path, Path(tmp))
        if sheet == "all":
            frames = pl.read_excel(source, sheet_id=0, **kwargs)
            assert isinstance(frames, dict), "sheet_id=0 deve retornar dict"
            return {name: tidy(f) for name, f in frames.items()}
        if sheet is None:
            return tidy(pl.read_excel(source, sheet_id=None, **kwargs))
        return tidy(pl.read_excel(source, sheet_id=sheet, **kwargs))


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
        with tempfile.TemporaryDirectory(
            prefix=".anp-zip-", dir=scratch_dir(), ignore_cleanup_errors=True
        ) as tmp:
            return read_file(decompress(path, Path(tmp)), spec)
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
    return pl.concat(frames, how="vertical_relaxed")


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
