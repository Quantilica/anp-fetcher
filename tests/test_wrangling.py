"""Tests for anp_fetcher.wrangling."""

from pathlib import Path

import polars as pl

from anp_fetcher.wrangling import (
    convert_group,
    convert_one,
    extract_schema,
    spec_for,
)


def test_apply_contract_on_shpc(tmp_path):
    src = _make_group_input(
        tmp_path,
        "shpc-combustiveis-automotivos",
        {
            "shpc-ca_2025-05@20250601.csv": (
                "Regiao - Sigla;Estado - Sigla;Municipio;Revenda;CNPJ da Revenda;"
                "Nome da Rua;Numero Rua;Complemento;Bairro;Cep;Produto;"
                "Data da Coleta;Valor de Venda;Valor de Compra;"
                "Unidade de Medida;Bandeira\n"
                "SE;SP;SAO PAULO;POSTO X;123;RUA A;10;;CENTRO;01000;GASOLINA;"
                "2025-05-01;5,49;4,99;R$/l;BR\n"
            )
        },
    )
    raw = src / "shpc-combustiveis-automotivos" / "shpc-ca_2025-05@20250601.csv"
    written = convert_one("shpc-ca", raw, tmp_path / "output")
    assert len(written) == 1
    df = pl.read_parquet(written[0])
    assert df["Valor de Venda"].dtype == pl.Float64
    assert df["Valor de Venda"][0] == 5.49
    assert df["Regiao - Sigla"][0] == "SE"


def _make_group_input(tmp_path: Path, group_dir: str, files: dict[str, str]) -> Path:
    src = tmp_path / "input" / group_dir
    src.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (src / name).write_text(content, encoding="utf-8")
    return tmp_path / "input"


def test_spec_for_default():
    spec = spec_for("producao-mar")
    assert spec["separator"] == ";"
    assert spec["encoding"] is None
    assert spec["numeric_columns"] == []


def test_spec_for_shpc_override():
    spec = spec_for("shpc-ca")
    assert spec["encoding"] == "utf-8"
    assert spec["numeric_columns"] == ["Valor de Venda", "Valor de Compra"]
    # defaults preservados
    assert spec["separator"] == ";"


def test_convert_one_writes_partitioned_parquet(tmp_path):
    src = _make_group_input(
        tmp_path,
        "shpc-combustiveis-automotivos",
        {"shpc-ca_2025-05@20250601.csv": "Municipio;Valor de Venda\nSAO PAULO;5,49\n"},
    )
    raw = src / "shpc-combustiveis-automotivos" / "shpc-ca_2025-05@20250601.csv"
    written = convert_one("shpc-ca", raw, tmp_path / "output")
    assert len(written) == 1
    target = (
        tmp_path
        / "output"
        / "shpc-combustiveis-automotivos"
        / ("shpc-ca_2025-05@20250601.parquet")
    )
    assert written[0] == target
    df = pl.read_parquet(target)
    assert df["Valor de Venda"].dtype == pl.Float64
    assert df["Valor de Venda"][0] == 5.49


def test_convert_one_skips_existing(tmp_path):
    src = _make_group_input(
        tmp_path,
        "shpc-combustiveis-automotivos",
        {"shpc-ca_2025-05@20250601.csv": "Municipio;Valor\nSAO PAULO;5,49\n"},
    )
    raw = src / "shpc-combustiveis-automotivos" / "shpc-ca_2025-05@20250601.csv"
    first = convert_one("shpc-ca", raw, tmp_path / "output")
    second = convert_one("shpc-ca", raw, tmp_path / "output")
    assert len(first) == 1
    assert second == []


def test_convert_group_tolerates_unreadable_file(tmp_path):
    src = _make_group_input(
        tmp_path,
        "importacoes-exportacoes",
        {"ie-m3@20260529.xlsx": "x"},  # bytes inválidos de xlsx -> erro tolerado
    )
    converted = convert_group(["ie"], src, tmp_path / "output")
    assert converted == 0
    out_dir = tmp_path / "output" / "importacoes-exportacoes"
    assert not out_dir.exists() or not list(out_dir.iterdir())


def test_convert_group_unknown_group(tmp_path):
    src = tmp_path / "input"
    converted = convert_group(["grupo-inexistente"], src, tmp_path / "output")
    assert converted == 0


def test_extract_schema(tmp_path):
    src = _make_group_input(
        tmp_path,
        "shpc-combustiveis-automotivos",
        {"shpc-ca_2025-05@20250601.csv": "Municipio;Valor de Venda\nSAO PAULO;5,49\n"},
    )
    out_csv = tmp_path / "schema.csv"
    extract_schema(["shpc-ca"], src, out_csv)
    lines = out_csv.read_text().strip().splitlines()
    assert len(lines) == 3  # header + 2 colunas
    assert "shpc-ca" in lines[1]
    assert "Municipio" in lines[1]
    assert '"Valor de Venda"' in lines[2] or "Valor de Venda" in lines[2]
