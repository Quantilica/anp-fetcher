"""Tests for the optional lake inventory (``LakeConverter.inventory``)."""

from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")

core_lake = pytest.importorskip("quantilica.core.lake")
if not hasattr(core_lake, "Planned"):
    pytest.skip(
        "quantilica-core ainda sem o contrato do inventário (Planned)",
        allow_module_level=True,
    )

from anp_fetcher.lake import converter  # noqa: E402
from anp_fetcher.storage import _GROUP_DIRS  # noqa: E402

Planned = core_lake.Planned
converter_inventory = core_lake.converter_inventory

SHPC_CSV = (
    "Regiao;Estado;Municipio;Produto;Valor de Venda;Valor de Compra\n"
    "SE;SP;SAO PAULO;GLP;105,50;80,00\n"
)
ROYALTIES_CSV = "Campo;Valor\nX;1,5\n"


def _by_name(items: list[Planned]) -> dict[str, Planned]:
    return {Path(item.path).name: item for item in items}


def _write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_inventory_routes_files_to_their_datasets(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    _write(raw / _GROUP_DIRS["shpc-glp"] / "shpc-glp_2024-05@20240601.csv", SHPC_CSV)
    _write(
        raw / _GROUP_DIRS["royalties"] / "royalties_2024@20240601.csv", ROYALTIES_CSV
    )

    items = _by_name(converter.inventory(raw))

    assert items["shpc-glp_2024-05@20240601.csv"].dataset == "shpc-glp"
    assert items["shpc-glp_2024-05@20240601.csv"].skip_reason is None
    assert items["royalties_2024@20240601.csv"].dataset == "royalties"
    assert items["royalties_2024@20240601.csv"].skip_reason is None


def test_inventory_marks_twin_and_superseded(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    pmqc = raw / _GROUP_DIRS["pmqc"]
    _write(pmqc / "pmqc-csv_2024-01@20240101.csv", "A;B\n1;2\n")
    _write(pmqc / "pmqc-csv_2024-01@20240201.csv", "A;B\n1;2\n")
    _write(pmqc / "pmqc-json_2024-01@20240201.json", "[]")

    rochas = raw / _GROUP_DIRS["amostras-rochas-fluidos"]
    _write(rochas / "amostras-rochas-fluidos@20240601.csv", "A;B\n1;2\n")
    _write(rochas / "amostras-rochas-fluidos@20240601.zip", "PK")

    items = _by_name(converter.inventory(raw))

    assert items["pmqc-csv_2024-01@20240201.csv"].dataset == "pmqc"
    # Mesmo conteúdo em outro formato: o conversor fica com o CSV.
    assert items["pmqc-json_2024-01@20240201.json"].skip_reason == "gemeo"
    assert items["amostras-rochas-fluidos@20240601.zip"].skip_reason == "gemeo"
    # Mesmo formato, versão anterior.
    assert items["pmqc-csv_2024-01@20240101.csv"].skip_reason == "superado"


def test_inventory_marks_non_tabular_and_skips_leftovers(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    group_dir = raw / _GROUP_DIRS["shpc-glp"]
    _write(group_dir / "shpc-glp_2024-05@20240601.csv", SHPC_CSV)
    (group_dir / "layout@20240601.pdf").write_bytes(b"%PDF-1.4\n")
    (group_dir / "shpc-glp_2024-05@20240601.csv.manifest.json").write_text(
        "{}", encoding="utf-8"
    )
    (group_dir / ".shpc-glp_2024-05@20240601.csv.123.tmp").write_text(
        "resto", encoding="utf-8"
    )

    items = _by_name(converter.inventory(raw))

    assert set(items) == {"shpc-glp_2024-05@20240601.csv", "layout@20240601.pdf"}
    assert items["shpc-glp_2024-05@20240601.csv"].dataset == "shpc-glp"
    assert items["layout@20240601.pdf"].skip_reason == "nao_tabular"
    assert items["layout@20240601.pdf"].dataset is None


def test_inventory_separates_mixed_granularities(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    group_dir = raw / _GROUP_DIRS["producao-terra"]
    _write(group_dir / "producao-terra-s1_2000-01.csv", "Campo;Volume\nX;1,5\n")
    _write(group_dir / "producao-terra-01_2016.csv", "Campo;Volume\nX;1,5\n")
    _write(group_dir / "producao-terra-1941-1966.csv", "Campo;Volume\nX;1,5\n")

    items = _by_name(converter.inventory(raw))

    assert items["producao-terra-s1_2000-01.csv"].dataset == "producao-terra"
    assert items["producao-terra-01_2016.csv"].dataset == "producao-terra-anual"
    assert items["producao-terra-1941-1966.csv"].dataset == "producao-terra-historico"


def test_inventory_matches_convert(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    group_dir = raw / _GROUP_DIRS["shpc-glp"]
    _write(group_dir / "shpc-glp_2024-05@20240601.csv", SHPC_CSV)
    _write(group_dir / "shpc-glp_2024-05@20240601.json", "[]")
    (group_dir / "layout@20240601.pdf").write_bytes(b"%PDF-1.4\n")
    lake = tmp_path / "lake"

    items = converter.inventory(raw)
    res = converter.convert(raw, lake)
    # O PDF entra na descoberta do conversor e falha na leitura: não gera Parquet,
    # que é o que o inventário declara com "nao_tabular".
    assert res.converted == 1
    assert [e.split(":", 1)[0] for e in res.errors] == ["layout@20240601.pdf"]

    planned = {item.dataset for item in items if item.dataset}
    written = {p.name for p in (lake / "anp").iterdir() if p.is_dir()}
    assert planned == written == {"shpc-glp"}


def test_inventory_is_the_optional_contract_member(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    _write(raw / _GROUP_DIRS["shpc-glp"] / "shpc-glp_2024-05@20240601.csv", SHPC_CSV)

    items = converter_inventory(converter, raw)

    assert items is not None
    assert [Path(item.path).name for item in items] == ["shpc-glp_2024-05@20240601.csv"]


def test_inventory_covers_files_outside_group_dirs(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    _write(raw / "solto" / "dados.csv", "A;B\n1;2\n")
    (raw / "solto" / "manual.pdf").write_bytes(b"%PDF-1.4\n")

    items = _by_name(converter.inventory(raw))

    # O conversor não procura fora dos diretórios de grupo: o tabular fica sem
    # destino (a auditoria aponta a lacuna) e o documento é não tabular.
    assert items["dados.csv"].dataset is None
    assert items["dados.csv"].skip_reason is None
    assert items["manual.pdf"].skip_reason == "nao_tabular"


def test_inventory_of_missing_directory_is_empty(tmp_path: Path) -> None:
    assert converter.inventory(tmp_path / "nao-existe") == []
