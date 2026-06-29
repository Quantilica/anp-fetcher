"""Tests for anp_fetcher.storage."""

import datetime as dt
from pathlib import Path

import pytest

from anp_fetcher.catalog import GROUPS, list_datasets
from anp_fetcher.storage import DataRepository, _GROUP_DIRS


def test_group_dirs_cover_all_groups():
    assert set(_GROUP_DIRS) == set(GROUPS)


def test_path_for_static_entry(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(e for e in list_datasets("ie") if e["year"] is None)
    path = repo.path_for_entry(entry)
    assert path.parent.name == "importacoes-exportacoes"
    assert path.name.startswith(entry["base_id"])
    assert path.suffix == f".{entry['ext']}"


def test_path_for_static_entry_with_date(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(e for e in list_datasets("ie") if e["id"] == "ie-m3")
    date = dt.date(2026, 5, 29)
    path = repo.path_for_entry(entry, last_modified=date)
    assert "ie-m3@20260529" in path.name
    assert path.suffix == ".xlsx"


def test_path_for_annual_entry(tmp_path):
    repo = DataRepository(tmp_path)
    entries = [e for e in list_datasets("ppg") if e["base_id"] == "producao-poco"]
    entry_2023 = next(e for e in entries if e["year"] == 2023)
    path = repo.path_for_entry(entry_2023)
    assert path.parent.name == "producao-petroleo-gas"
    assert "producao-poco" in path.name
    assert "2023" in path.name
    assert path.suffix == ".zip"


def test_path_for_annual_entry_with_date(tmp_path):
    repo = DataRepository(tmp_path)
    entries = [e for e in list_datasets("ppg") if e["base_id"] == "producao-poco"]
    entry_2023 = next(e for e in entries if e["year"] == 2023)
    date = dt.date(2026, 1, 15)
    path = repo.path_for_entry(entry_2023, last_modified=date)
    assert "producao-poco_2023@20260115" in path.name


def test_path_for_semestral_entry(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(
        e for e in list_datasets("shpc-ca")
        if e["year"] == 2024 and e["semester"] == 1
    )
    date = dt.date(2026, 6, 1)
    path = repo.path_for_entry(entry, last_modified=date)
    assert path.parent.name == "shpc-combustiveis-automotivos"
    assert "shpc-ca_2024-01@20260601" in path.name
    assert path.suffix == ".zip"


def test_path_for_semestral_entry_second_semester(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(
        e for e in list_datasets("shpc-glp")
        if e["year"] == 2021 and e["semester"] == 2
    )
    date = dt.date(2026, 6, 1)
    path = repo.path_for_entry(entry, last_modified=date)
    assert path.parent.name == "shpc-glp"
    assert "shpc-glp_2021-02@20260601" in path.name


def test_path_for_monthly_entry(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(
        e for e in list_datasets("shpc-diesel-gnv")
        if e["year"] == 2025 and e["month"] == 3
    )
    date = dt.date(2026, 6, 1)
    path = repo.path_for_entry(entry, last_modified=date)
    assert path.parent.name == "shpc-diesel-gnv"
    assert "shpc-diesel-gnv_2025-03@20260601" in path.name


def test_path_for_shpc_4s_static(tmp_path):
    repo = DataRepository(tmp_path)
    entry = next(e for e in list_datasets("shpc-4s") if "diesel" in e["id"])
    path = repo.path_for_entry(entry)
    assert path.parent.name == "shpc-ultimas-4-semanas"
    assert path.suffix == ".csv"


def test_path_for_vdpb_abertos(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("vdpb-abertos")[0]
    path = repo.path_for_entry(entry)
    assert path.parent.name == "vendas-abertos"


def test_path_for_pp_abertos(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("pp-abertos")[0]
    path = repo.path_for_entry(entry)
    assert path.parent.name == "processamento-abertos"


def test_path_subdirs_correct(tmp_path):
    repo = DataRepository(tmp_path)
    expected = {
        "ie": "importacoes-exportacoes",
        "pp": "processamento-petroleo",
        "pb": "producao-biocombustiveis",
        "ppg": "producao-petroleo-gas",
        "vdpb": "vendas",
        "shpc-ca": "shpc-combustiveis-automotivos",
        "shpc-glp": "shpc-glp",
        "shpc-diesel-gnv": "shpc-diesel-gnv",
        "shpc-gasolina-etanol": "shpc-gasolina-etanol",
        "shpc-glp-mensal": "shpc-glp-mensal",
        "shpc-4s": "shpc-ultimas-4-semanas",
        "vdpb-abertos": "vendas-abertos",
        "pp-abertos": "processamento-abertos",
        # Onda 3a
        "producao-el":            "producao-estado-localizacao",
        "pb-abertos":             "producao-biocombustiveis-abertos",
        "ie-abertos":             "importacoes-exportacoes-abertos",
        "comercializacao-gn":     "comercializacao-gas-natural",
        "movimentacao-terminais": "movimentacao-terminais",
        "armazenagem-terminais":  "armazenagem-terminais",
        "incidentes":             "incidentes-operacionais",
        "rodadas":                "rodadas-licitacoes",
        "concessionarios":        "concessionarios",
        "revendedores":           "revendedores-varejistas",
        "revendas-glp":           "revendas-glp",
        "registro-lubrificantes": "registro-lubrificantes",
        "pml":                    "pml",
        "fiscalizacao":           "fiscalizacao-abastecimento",
        "royalties":              "participacoes-governamentais",
    }
    for group_id, dir_name in expected.items():
        entry = list_datasets(group_id)[0]
        path = repo.path_for_entry(entry)
        assert path.parent.name == dir_name, (
            f"Group {group_id!r}: expected dir {dir_name!r}, got {path.parent.name!r}"
        )


def test_paths_are_absolute(tmp_path):
    repo = DataRepository(tmp_path)
    for entry in list_datasets("ie"):
        path = repo.path_for_entry(entry)
        assert path.is_absolute()


def test_different_entries_produce_different_paths(tmp_path):
    repo = DataRepository(tmp_path)
    ie_entries = list_datasets("ie")
    paths = [repo.path_for_entry(e) for e in ie_entries]
    assert len(paths) == len(set(paths)), "Duplicate paths for different entries"


def test_semestral_different_semesters_different_paths(tmp_path):
    repo = DataRepository(tmp_path)
    entries = list_datasets("shpc-ca")
    date = dt.date(2026, 6, 1)
    paths = [repo.path_for_entry(e, last_modified=date) for e in entries]
    assert len(paths) == len(set(paths)), "Duplicate paths for semestral entries"


def test_path_for_royalties_annual(tmp_path):
    repo = DataRepository(tmp_path)
    entries = list_datasets("royalties")
    ru_2020 = next(e for e in entries if e["id"] == "royalties-uniao-2020")
    date = dt.date(2026, 6, 29)
    path = repo.path_for_entry(ru_2020, last_modified=date)
    assert path.parent.name == "participacoes-governamentais"
    assert "royalties-uniao_2020@20260629" in path.name


def test_path_for_royalties_static_pe(tmp_path):
    repo = DataRepository(tmp_path)
    pe = next(e for e in list_datasets("royalties") if e["id"] == "pe-campo")
    path = repo.path_for_entry(pe)
    assert path.parent.name == "participacoes-governamentais"
    assert path.name.startswith("pe-campo")
    assert path.suffix == ".csv"


def test_royalties_annual_entries_produce_distinct_paths(tmp_path):
    repo = DataRepository(tmp_path)
    date = dt.date(2026, 6, 29)
    paths = [repo.path_for_entry(e, last_modified=date) for e in list_datasets("royalties")]
    assert len(paths) == len(set(paths)), "Duplicate paths in royalties group"


def test_path_for_producao_el(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("producao-el")[0]
    path = repo.path_for_entry(entry)
    assert path.parent.name == "producao-estado-localizacao"
    assert path.suffix == ".csv"


def test_path_for_fiscalizacao(tmp_path):
    repo = DataRepository(tmp_path)
    entry = list_datasets("fiscalizacao")[0]
    path = repo.path_for_entry(entry)
    assert path.parent.name == "fiscalizacao-abastecimento"
    assert path.suffix == ".xlsx"
