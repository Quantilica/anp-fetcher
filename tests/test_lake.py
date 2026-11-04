"""Tests for Hive lake conversion of ANP open data."""

from __future__ import annotations

from importlib.metadata import entry_points
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")
import polars as pl  # noqa: E402
from quantilica.analytics.lake import check_dataset, scan_dataset  # noqa: E402
from typer.testing import CliRunner  # noqa: E402

from anp_fetcher.lake import (  # noqa: E402
    SOURCE_ID,
    converter,
    dataset_for_granularity,
    resolve_partitions,
)
from anp_fetcher.plugin import app  # noqa: E402
from anp_fetcher.storage import _GROUP_DIRS  # noqa: E402


def test_entry_point_registered() -> None:
    eps = entry_points(group="quantilica.lake")
    matches = [ep for ep in eps if ep.name == "anp"]
    assert len(matches) == 1
    loaded = matches[0].load()
    assert loaded is converter
    assert loaded.source_id == SOURCE_ID


def test_resolve_partitions() -> None:
    keys_ym, vals_ym = resolve_partitions({"partition": "2024-05"})
    assert keys_ym == ["ano", "mes"]
    assert vals_ym == {"ano": "2024", "mes": "05"}

    keys_y, vals_y = resolve_partitions({"partition": "2024"})
    assert keys_y == ["ano"]
    assert vals_y == {"ano": "2024"}

    keys_empty, vals_empty = resolve_partitions({})
    assert keys_empty == []
    assert vals_empty == {}


def test_converter_datasets() -> None:
    datasets = converter.datasets()
    assert "shpc-glp" in datasets
    assert "shpc-gasolina-etanol" in datasets
    assert "royalties" in datasets


def test_convert_end_to_end(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    group = "shpc-glp"
    group_dir = raw_dir / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    raw_csv = group_dir / f"{group}_2024-05@20240601.csv"
    raw_csv.write_text(
        "Regiao;Estado;Municipio;Produto;Valor de Venda;Valor de Compra\n"
        "SE;SP;SAO PAULO;GLP;105,50;80,00\n",
        encoding="utf-8",
    )

    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert not res.errors, res.errors
    assert res.converted == 1
    assert res.skipped == 0

    dataset_lake = lake_dir / SOURCE_ID / group
    assert check_dataset(dataset_lake) == []
    df = scan_dataset(dataset_lake).collect()
    assert df.height == 1
    assert "ano" in df.columns
    assert "mes" in df.columns
    assert df["ano"][0] == 2024
    assert df["mes"][0] == "05"
    assert "Regiao" in df.columns

    # Second pass skips
    res2 = converter.convert(raw_dir, lake_dir)
    assert not res2.errors
    assert res2.converted == 0
    assert res2.skipped == 1


def test_cli_convert(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    group = "shpc-glp"
    group_dir = raw_dir / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    (group_dir / f"{group}_2024-05@20240601.csv").write_text(
        "Regiao;Estado;Municipio;Produto;Valor de Venda\nSE;SP;SAO PAULO;GLP;105,50\n",
        encoding="utf-8",
    )

    lake_dir = tmp_path / "lake"
    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "convert",
            "-i",
            str(raw_dir),
            "--lake",
            str(lake_dir),
            "--dataset",
            group,
        ],
    )
    assert result.exit_code == 0, result.output
    assert (lake_dir / SOURCE_ID / group).exists()


def test_dataset_for_granularity() -> None:
    assert (
        dataset_for_granularity("producao-terra", ["ano", "mes"], 2) == "producao-terra"
    )
    assert (
        dataset_for_granularity("producao-terra", ["ano"], 2) == "producao-terra-anual"
    )
    assert (
        dataset_for_granularity("producao-terra", [], 2) == "producao-terra-historico"
    )
    assert dataset_for_granularity("royalties", ["ano"], 1) == "royalties"


def test_granularidades_misturadas_viram_datasets_separados(tmp_path: Path) -> None:
    group = "producao-terra"
    group_dir = tmp_path / "raw" / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    for name in (
        "producao-terra-s1_2000-01.csv",
        "producao-terra-01_2016.csv",
        "producao-terra-1941-1966.csv",
    ):
        (group_dir / name).write_text("Campo;Volume\nX;1,5\n", encoding="utf-8")
    lake_dir = tmp_path / "lake"
    res = converter.convert(tmp_path / "raw", lake_dir, datasets=[group])
    assert not res.errors, res.errors
    assert res.converted == 3
    for ds in (group, f"{group}-anual", f"{group}-historico"):
        assert check_dataset(lake_dir / SOURCE_ID / ds) == [], ds
    assert scan_dataset(lake_dir / SOURCE_ID / group).collect().columns[-2:] == [
        "ano",
        "mes",
    ]


def test_semestral_lake_conversion(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    group = "shpc-ca"
    group_dir = raw_dir / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    raw_csv = group_dir / f"{group}_2024-S1@20240801.csv"
    raw_csv.write_text(
        "Regiao;Estado;Municipio;Produto;Valor de Venda;Valor de Compra\n"
        "SE;SP;SAO PAULO;ETANOL;3,50;2,80\n",
        encoding="utf-8",
    )

    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir, datasets=[group])
    assert not res.errors, res.errors
    assert res.converted == 1

    dataset_lake = lake_dir / SOURCE_ID / group
    assert check_dataset(dataset_lake) == []
    df = scan_dataset(dataset_lake).collect()
    assert df.height == 1
    assert "ano" in df.columns
    assert "semestre" in df.columns
    assert df["ano"][0] == 2024
    assert df["semestre"][0] == "S1"


def test_royalties_municipio_lake_conversion(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    group = "royalties"
    group_dir = raw_dir / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    raw_csv = group_dir / "royalties-municipio_2023@20240101.csv"
    raw_csv.write_text(
        "ANO;MES;UF;CODIGO_IBGE;MUNICIPIO;VALOR\n2023;12;RJ;3302403;MACAE;1250000,50\n",
        encoding="utf-8",
    )

    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir, datasets=[group])
    assert not res.errors, res.errors
    assert res.converted == 1

    dataset_lake = lake_dir / SOURCE_ID / "royalties_municipio"
    assert check_dataset(dataset_lake) == []
    df = scan_dataset(dataset_lake).collect()
    assert df.height == 1
    assert "ano" in df.columns
    assert df["ano"][0] == 2023
    assert df["CODIGO_IBGE"].dtype == pl.String
    assert df["CODIGO_IBGE"][0] == "3302403"


def test_participacoes_especiais_lake_conversion(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    group = "royalties"
    group_dir = raw_dir / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    (group_dir / "pe-municipio@20240101.csv").write_text(
        "ANO;UF;CODIGO_IBGE;MUNICIPIO;VALOR_PE\n2023;RJ;3302403;MACAE;5000000.00\n",
        encoding="utf-8",
    )
    (group_dir / "pe-uniao@20240101.csv").write_text(
        "ANO;VALOR_PE\n2023;15000000.00\n",
        encoding="utf-8",
    )

    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir, datasets=["participacoes_especiais"])
    assert not res.errors, res.errors
    assert res.converted == 2

    pe_lake = lake_dir / SOURCE_ID / "participacoes_especiais"
    assert check_dataset(pe_lake) == []
    df = scan_dataset(pe_lake).collect()
    assert df.height == 2
    assert sorted(df["recorte"].to_list()) == ["municipio", "uniao"]
    assert not (lake_dir / SOURCE_ID / "royalties").exists()


def test_royalties_routing_is_explicit_by_base_id(tmp_path: Path) -> None:
    from anp_fetcher.lake import dataset_for_granularity

    def route(name: str) -> str:
        return dataset_for_granularity("royalties", ["ano"], 1, path=Path(name))

    assert route("royalties-uniao_2024@20240101.csv") == "royalties_uniao"
    assert route("royalties-estado_2024@20240101.csv") == "royalties_estado"
    assert route("royalties-municipio_2024@20240101.csv") == "royalties_municipio"
    assert route("preco-ref-gn_2024@20240101.csv") == "preco_referencia_gn"
    assert route("preco-ref-petroleo_2024@20240101.csv") == "preco_referencia_petroleo"
    # base fora da tabela: dataset do grupo, sem adivinhar por trecho do nome
    assert route("royalties-pe-municipio_2024@20240101.csv") == "royalties"
    assert route("outro_municipio_2024@20240101.csv") == "royalties"


def test_convert_by_canonical_alias_anp(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    group = "royalties"
    group_dir = raw_dir / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    (group_dir / "royalties-municipio_2022@20230101.csv").write_text(
        "ANO;MES;UF;CODIGO_IBGE;MUNICIPIO;VALOR\n2022;12;RJ;3302403;MACAE;1000000,00\n",
        encoding="utf-8",
    )

    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir, datasets=["royalties_municipio"])
    assert not res.errors, res.errors
    assert res.converted == 1


def test_convert_unknown_dataset_anp(tmp_path: Path) -> None:
    res = converter.convert(tmp_path, tmp_path, datasets=["desconhecido_anp"])
    assert len(res.errors) == 1
    assert "dataset desconhecido: desconhecido_anp" in res.errors[0]
