"""Tests for Hive lake conversion of ANP open data."""

from __future__ import annotations

from importlib.metadata import entry_points
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

from quantilica.analytics.lake import check_dataset, scan_dataset  # noqa: E402
from typer.testing import CliRunner  # noqa: E402

from anp_fetcher.lake import (  # noqa: E402
    SOURCE_ID,
    converter,
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
    assert df["ano"][0] == "2024"
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
