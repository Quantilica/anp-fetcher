"""Arquivos da ANP que os leitores recusavam."""

from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("fastexcel")

from anp_fetcher.lake import pick_one_format  # noqa: E402
from anp_fetcher.reader import read_csv, read_file  # noqa: E402


def test_xls_que_e_xlsx(tmp_path: Path) -> None:
    src = tmp_path / "producao-etanol-m3.xls"
    pl.DataFrame({"ano": [2024], "volume": [10.5]}).write_excel(tmp_path / "x.xlsx")
    (tmp_path / "x.xlsx").rename(src)
    df = read_file(src, {})
    assert df["volume"].to_list() == [10.5]


def test_csv_com_campo_a_mais(tmp_path: Path) -> None:
    src = tmp_path / "movterm.csv"
    src.write_text("a;b\n1;2\n3;4;\n", encoding="latin-1")
    df = read_csv(src, {})
    assert df.columns == ["a", "b"]
    assert df.height == 2


def test_json_tabular(tmp_path: Path) -> None:
    src = tmp_path / "pmqc-json_2024-01.json"
    src.write_text('[{"Produto": "ETANOL", "Valor": "1,5"}, {"Produto": "GLP"}]')
    df = read_file(src, {})
    assert df["Produto"].to_list() == ["ETANOL", "GLP"]


def test_pick_one_format() -> None:
    names = ["pmqc-csv_2024-01@20240210.csv", "pmqc-json_2024-01@20240210.json"]
    assert [p.name for p in pick_one_format([Path(n) for n in names])] == [names[0]]


def test_csv_que_e_xlsx(tmp_path: Path) -> None:
    src = tmp_path / "movterm.csv"
    pl.DataFrame({"uf": ["SP"], "volume": [1.5]}).write_excel(tmp_path / "x.xlsx")
    (tmp_path / "x.xlsx").rename(src)
    assert read_file(src, {})["uf"].to_list() == ["SP"]


def test_csv_com_aspas_no_texto(tmp_path: Path) -> None:
    # revendas-glp: aspas soltas no nome ("O EDGAR, D"AGUA) engoliam linhas.
    rows = ["id;nome;uf"] + [f"{i};REVENDA {i};SP" for i in range(3000)]
    rows[10] = '9;"O EDGAR;GO'
    rows[2000] = '1999;MINA D"AGUA;SP'
    src = tmp_path / "revendas-glp.csv"
    src.write_text("\n".join(rows) + "\n", encoding="latin-1")
    df = read_csv(src, {})
    assert df.height == 3000
    assert df["nome"][9] == '"O EDGAR'
    assert df["nome"][1999] == 'MINA D"AGUA'


def test_xlsx_que_e_csv(tmp_path: Path) -> None:
    src = tmp_path / "multas-2021.xlsx"
    src.write_text("﻿uf;valor\nSP;10\n", encoding="utf-8")
    assert read_file(src, {})["uf"].to_list() == ["SP"]


def test_csv_que_e_zip(tmp_path: Path) -> None:
    import zipfile

    src = tmp_path / "shpc-ca_2014-01.csv"
    with zipfile.ZipFile(src, "w") as archive:
        archive.writestr(
            "Precos semestrais - AUTOMOTIVOS_2014.01.csv", "uf;preco\nSP;3,1\n"
        )
    assert read_file(src, {})["uf"].to_list() == ["SP"]
