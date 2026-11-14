"""``movimentacao-gn``: tabela larga (uma coluna por dia) em tabela longa."""

from __future__ import annotations

import calendar
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")
import polars as pl  # noqa: E402
from quantilica.analytics.lake import check_dataset, scan_dataset  # noqa: E402

from anp_fetcher.lake import SOURCE_ID, converter  # noqa: E402
from anp_fetcher.reader import read_file  # noqa: E402
from anp_fetcher.storage import _GROUP_DIRS  # noqa: E402
from anp_fetcher.wrangling import spec_for  # noqa: E402

GROUP = "movimentacao-gn"
SPEC = spec_for(GROUP)

# safra antiga: nomes como a ANP escrevia em 2021-2025
ANTIGO = [
    "Código da Instalação de Transporte",
    "Nome da Instalação de Transporte",
    "Nome da Instalação de Gasoduto",
    "Código da Instalação de Gasoduto",
    "Tipo da Instalação do Gasoduto",
    "Nome do Município da Instalação de Gasoduto",
    "Nome da UF da Instalação de Gasoduto",
    "Nome do Operador da Instalação de Gasoduto",
    "Código do Operador da Instalação de Gasoduto",
    "Nome do Carregador que usa a Instalação de Gasoduto",
    "Código do Carregador que usa a Instalação de Gasoduto",
    "Nome do Contrato da Instalação do Gasoduto",
    "Nome da variável",
]
# safra recente (2026)
NOVO = [
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
    "Nome da Variável",
]


def _ids(variavel: str) -> list[str]:
    return [
        "700521", "Bolívia - Mato Grosso", "", "", "", "", "", "Gasocidente",
        "1717813", "AMBAR", "1645009", "", variavel,
    ]  # fmt: skip


def _datas(ano: int, mes: int) -> list[str]:
    dias = calendar.monthrange(ano, mes)[1]
    return [f"{d:02d}/{mes:02d}/{ano}" for d in range(1, dias + 1)]


def _csv(
    path: Path,
    ids: list[str],
    cabecalho_datas: list[str],
    linhas: list[tuple[str, list[str]]],
) -> Path:
    """CSV em latin-1, como a ANP publica: ``(variável, valores por coluna)``."""
    texto = ";".join([*ids, *cabecalho_datas]) + "\n"
    for variavel, valores in linhas:
        texto += ";".join([*_ids(variavel), *valores]) + "\n"
    path.write_bytes(texto.encode("latin-1"))
    return path


def _valores(n: int, valor: str = "1,5") -> list[str]:
    return [valor] * n


def test_melt_e_decimais(tmp_path: Path) -> None:
    datas = _datas(2026, 2)  # 28 dias
    valores = _valores(28)
    valores[0], valores[1], valores[2] = " 1113,52 ", "- 153,85", "13.927,30"
    valores[3], valores[4], valores[5] = "5,78439E-13", "209.97", "-"
    valores[6], valores[7] = "#N/D", ""
    csv = _csv(
        tmp_path / "a.csv",
        NOVO,
        datas,
        [
            ("Volume Realizado (mil m³)", valores),
            ("Pressão Média (kgf/cm²)", _valores(28, "0")),
        ],
    )
    df = read_file(csv, SPEC)
    assert df.height == 2 * 28
    assert df.schema["data"] == pl.Date and df.schema["valor"] == pl.Float64
    vol = df.filter(pl.col("variavel") == "volume-realizado").sort("data")
    assert vol["data"][0].isoformat() == "2026-02-01"
    assert vol["data"][-1].isoformat() == "2026-02-28"
    assert vol["data"].n_unique() == 28
    assert vol["valor"].to_list()[:5] == pytest.approx(
        [1113.52, -153.85, 13927.30, 5.78439e-13, 209.97]
    )
    # '-', '#N/D' e célula vazia: a linha fica, com valor nulo
    assert vol["valor"].to_list()[5:8] == [None, None, None]
    assert vol["valor"].null_count() == 3
    assert vol["valor"].drop_nulls().len() == 28 - 3


def test_nomes_iguais_entre_safras(tmp_path: Path) -> None:
    antigo = _csv(
        tmp_path / "antigo.csv",
        ANTIGO,
        _datas(2021, 1),
        [("Volume Realizado", _valores(31))],
    )
    novo = _csv(
        tmp_path / "novo.csv",
        NOVO,
        _datas(2026, 4),
        [("Volume Realizado (mil m³)", _valores(30))],
    )
    a, n = read_file(antigo, SPEC), read_file(novo, SPEC)
    assert a.columns == n.columns
    assert a.schema == n.schema
    assert a.columns[:12] == SPEC["wide_dates"]["ids"]
    assert a.columns[12:] == ["variavel", "unidade", "variavel_fonte", "data", "valor"]
    assert a.height == 31 and n.height == 30
    assert a["Tipo da instalação de Gasoduto"].null_count() == 31


@pytest.mark.parametrize(
    ("fonte", "variavel", "unidade"),
    [
        ("Volume Realizado (mil m³)", "volume-realizado", "mil m³"),
        ("Volume Realizado", "volume-realizado", None),
        ("Pressão Média (kgf/cm²)", "pressao-media", "kgf/cm²"),
        ("Alocação (%)", "alocacao", "%"),
        ("Alocação Petrobras(%)", "alocacao-petrobras", "%"),
        ("Alocação PETROBRAS (%)", "alocacao-petrobras", "%"),
        ("Desequilibrio Diário (mil m³)", "desequilibrio-diario", "mil m³"),
        ("Desequilíbrio Diário (mil m³)", "desequilibrio-diario", "mil m³"),
        (
            "Desequilíbrio Diário Acumulado ( mil m³)",
            "desequilibrio-diario-acumulado",
            "mil m³",
        ),
        ("Gás Não Contado5 (mil m³)", "gas-nao-contado", "mil m³"),
        ("Gás não contado (mil m³)", "gas-nao-contado", "mil m³"),
    ],
)
def test_variavel_unidade_e_fonte(
    tmp_path: Path, fonte: str, variavel: str, unidade: str | None
) -> None:
    csv = _csv(tmp_path / "v.csv", NOVO, _datas(2026, 2), [(fonte, _valores(28))])
    df = read_file(csv, SPEC)
    assert df["variavel"].unique().to_list() == [variavel]
    assert df["unidade"].unique().to_list() == [unidade]
    assert df["variavel_fonte"].unique().to_list() == [fonte]


def test_variavel_ausente_fica_nula(tmp_path: Path) -> None:
    csv = _csv(tmp_path / "n.csv", NOVO, _datas(2026, 2), [("", _valores(28))])
    df = read_file(csv, SPEC)
    assert df.height == 28
    assert df["variavel"].null_count() == 28
    assert df["unidade"].null_count() == 28
    assert df["variavel_fonte"].null_count() == 28


def test_coluna_sem_nome_no_fim_do_mes_e_descartada(tmp_path: Path) -> None:
    """2026-04/06: 31ª coluna sem cabeçalho num mês de 30 dias, sem data possível."""
    cabecalho = [*_datas(2026, 4), ""]
    csv = _csv(
        tmp_path / "b.csv",
        NOVO,
        cabecalho,
        [("Volume Realizado (mil m³)", [*_valores(30), "63,9"])],
    )
    df = read_file(csv, SPEC)
    assert df.height == 30
    assert df["data"].max().isoformat() == "2026-04-30"
    assert not [c for c in df.columns if c.startswith("coluna_")]
    assert df["valor"].to_list() == [1.5] * 30  # o 63,9 do resíduo não entra


def test_coluna_sem_nome_no_meio_do_mes_leva_o_dia_que_falta(tmp_path: Path) -> None:
    """2025-03: o cabeçalho de 02/03 veio em branco; o dado é desse dia."""
    datas = _datas(2025, 3)
    cabecalho = [datas[0], "", *datas[2:]]
    valores = _valores(31)
    valores[1] = "99,0"
    csv = _csv(tmp_path / "m.csv", NOVO, cabecalho, [("Alocação (%)", valores)])
    df = read_file(csv, SPEC).sort("data")
    assert df.height == 31
    assert df["data"].n_unique() == 31
    assert df.filter(pl.col("data").dt.day() == 2)["valor"].to_list() == [99.0]


def test_valor_nao_numerico_e_erro(tmp_path: Path) -> None:
    valores = _valores(28)
    valores[3] = "abc"
    csv = _csv(tmp_path / "e.csv", NOVO, _datas(2026, 2), [("Alocação (%)", valores)])
    with pytest.raises(ValueError, match="não convertida"):
        read_file(csv, SPEC)


def test_valor_com_ponto_ambiguo_e_erro(tmp_path: Path) -> None:
    valores = _valores(28)
    valores[3] = "1.234"
    csv = _csv(tmp_path / "p.csv", NOVO, _datas(2026, 2), [("Alocação (%)", valores)])
    with pytest.raises(ValueError, match="ambíguo"):
        read_file(csv, SPEC)


def test_lake_um_esquema_para_todas_as_safras(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    group_dir = raw_dir / _GROUP_DIRS[GROUP]
    group_dir.mkdir(parents=True)
    _csv(
        group_dir / f"{GROUP}_2021-02.csv",
        ANTIGO,
        _datas(2021, 2),
        [("Volume Realizado", _valores(28)), ("Desequilibrio Diário", _valores(28))],
    )
    _csv(
        group_dir / f"{GROUP}_2026-04.csv",
        NOVO,
        [*_datas(2026, 4), ""],
        [("Volume Realizado (mil m³)", [*_valores(30), "7"])],
    )
    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir, datasets=[GROUP])
    assert not res.errors, res.errors
    assert res.converted == 2

    dataset = lake_dir / SOURCE_ID / GROUP
    assert check_dataset(dataset) == []
    files = sorted(dataset.rglob("*.parquet"))
    assert len(files) == 2
    schemas = {tuple(pl.read_parquet(f).schema.items()) for f in files}
    assert len(schemas) == 1
    df = scan_dataset(dataset).collect()
    assert df.height == 2 * 28 + 30
    assert df["data"].dt.month().unique().sort().to_list() == [2, 4]
    assert df.filter(pl.col("ano") == 2021)["unidade"].null_count() == 2 * 28


def test_coluna_desconhecida_segue_como_vem(tmp_path: Path) -> None:
    """Coluna nova da fonte não some em silêncio nem derruba a conversão."""
    csv = _csv(
        tmp_path / "x.csv",
        [*NOVO[:-1], "Observação", NOVO[-1]],
        _datas(2026, 2),
        [("Alocação (%)", _valores(28))],
    )
    texto = csv.read_bytes().decode("latin-1").splitlines()
    # a linha de dados tem a célula da coluna nova antes da variável
    texto[1] = texto[1].replace(";Alocação (%);", ";nota;Alocação (%);")
    csv.write_bytes(("\n".join(texto) + "\n").encode("latin-1"))
    df = read_file(csv, SPEC)
    assert df.height == 28
    assert "Observação" in df.columns
    assert df["Observação"].unique().to_list() == ["nota"]
