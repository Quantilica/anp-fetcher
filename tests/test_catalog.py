"""Tests for anp_fetcher.catalog."""

import pytest

from anp_fetcher.catalog import (
    ALL_GROUP_KEYS,
    GROUP_ALIASES,
    GROUPS,
    SHPC_GROUP_KEYS,
    DatasetEntry,
    list_datasets,
    resolve_group,
)

_DE_GROUPS = {"ie", "pp", "pb", "ppg", "vdpb"}
_DA_GROUPS = {
    "shpc-ca", "shpc-glp", "shpc-diesel-gnv", "shpc-gasolina-etanol",
    "shpc-glp-mensal", "shpc-4s", "vdpb-abertos", "pp-abertos",
}
_ALL_GROUPS = _DE_GROUPS | _DA_GROUPS


def test_all_groups_present():
    assert set(GROUPS) == _ALL_GROUPS


def test_shpc_group_keys():
    assert set(SHPC_GROUP_KEYS) == {g for g in _ALL_GROUPS if g.startswith("shpc-")}


def test_each_group_has_name_and_entries():
    for key, info in GROUPS.items():
        assert info["name"], f"Group {key!r} missing name"
        assert len(info["entries"]) > 0, f"Group {key!r} has no entries"


def test_entry_fields_complete():
    required = {"id", "base_id", "name", "url", "ext", "group", "source",
                "year", "semester", "month"}
    for entry in list_datasets():
        missing = required - entry.keys()
        assert not missing, f"Entry {entry['id']!r} missing fields: {missing}"


def test_entry_source_field():
    for entry in list_datasets():
        assert entry["source"] in ("dados-estatisticos", "dados-abertos"), (
            f"Entry {entry['id']!r} has invalid source: {entry['source']!r}"
        )


def test_de_entries_have_correct_source():
    for group_id in _DE_GROUPS:
        for entry in GROUPS[group_id]["entries"]:
            assert entry["source"] == "dados-estatisticos", (
                f"Entry {entry['id']!r} should have source 'dados-estatisticos'"
            )


def test_da_entries_have_correct_source():
    for group_id in _DA_GROUPS:
        for entry in GROUPS[group_id]["entries"]:
            assert entry["source"] == "dados-abertos", (
                f"Entry {entry['id']!r} should have source 'dados-abertos'"
            )


def test_entry_urls_start_with_https():
    for entry in list_datasets():
        assert entry["url"].startswith("https://"), (
            f"Entry {entry['id']!r} has non-https URL: {entry['url']}"
        )


def test_static_entries_year_is_none():
    for group_id in ["ie", "pp", "pb"]:
        for entry in GROUPS[group_id]["entries"]:
            assert entry["year"] is None, (
                f"Static entry {entry['id']!r} has year={entry['year']}"
            )
    for entry in GROUPS["shpc-4s"]["entries"]:
        assert entry["year"] is None
    for entry in GROUPS["vdpb-abertos"]["entries"]:
        assert entry["year"] is None
    for entry in GROUPS["pp-abertos"]["entries"]:
        assert entry["year"] is None


def test_annual_entries_have_year():
    for entry in GROUPS["ppg"]["entries"]:
        if entry["base_id"] in ("producao-poco", "producao-campo"):
            assert entry["year"] is not None
            assert isinstance(entry["year"], int)
            assert entry["semester"] is None
            assert entry["month"] is None


def test_producao_poco_years():
    poco = [e for e in GROUPS["ppg"]["entries"] if e["base_id"] == "producao-poco"]
    years = {e["year"] for e in poco}
    assert years == set(range(2005, 2024))
    assert all(e["ext"] == "zip" for e in poco)


def test_producao_campo_years_and_ext():
    campo = [e for e in GROUPS["ppg"]["entries"] if e["base_id"] == "producao-campo"]
    years = {e["year"] for e in campo}
    assert years == set(range(2009, 2017))
    ext_2016 = next(e["ext"] for e in campo if e["year"] == 2016)
    assert ext_2016 == "xlsx"
    ext_2015 = next(e["ext"] for e in campo if e["year"] == 2015)
    assert ext_2015 == "xls"


def test_vdpb_static_entries():
    static = [e for e in GROUPS["vdpb"]["entries"] if e["year"] is None]
    ids = {e["id"] for e in static}
    assert "vendas-combustiveis-m3" in ids
    assert "vendas-combustiveis-b" in ids


def test_vendas_municipais_ext_exceptions():
    etanol = [
        e for e in GROUPS["vdpb"]["entries"]
        if e["base_id"] == "vendas-municipais-etanol-hidratado"
    ]
    e2000 = next(e for e in etanol if e["year"] == 2000)
    assert e2000["ext"] == "xlsx"
    e2001 = next(e for e in etanol if e["year"] == 2001)
    assert e2001["ext"] == "xls"

    gas_c = [
        e for e in GROUPS["vdpb"]["entries"]
        if e["base_id"] == "vendas-municipais-gasolina-c"
    ]
    e2010 = next(e for e in gas_c if e["year"] == 2010)
    assert e2010["ext"] == "xlsx"
    e2011 = next(e for e in gas_c if e["year"] == 2011)
    assert e2011["ext"] == "xls"


# ---------------------------------------------------------------------------
# SHPC semestral
# ---------------------------------------------------------------------------

def test_shpc_ca_count():
    entries = GROUPS["shpc-ca"]["entries"]
    assert len(entries) == 44  # 2 semesters × 22 years (2004-2025)


def test_shpc_ca_has_semester_field():
    for entry in GROUPS["shpc-ca"]["entries"]:
        assert entry["semester"] in (1, 2)
        assert entry["month"] is None
        assert entry["year"] is not None


def test_shpc_ca_ext_by_year():
    for entry in GROUPS["shpc-ca"]["entries"]:
        expected_ext = "zip" if entry["year"] >= 2022 else "csv"
        assert entry["ext"] == expected_ext, (
            f"{entry['id']}: expected {expected_ext}, got {entry['ext']}"
        )


def test_shpc_ca_2022_01_url_exception():
    e = next(e for e in GROUPS["shpc-ca"]["entries"]
             if e["year"] == 2022 and e["semester"] == 1)
    assert "precos-semestrais-ca.zip" in e["url"]


def test_shpc_glp_count():
    assert len(GROUPS["shpc-glp"]["entries"]) == 44


def test_shpc_glp_all_csv():
    for entry in GROUPS["shpc-glp"]["entries"]:
        assert entry["ext"] == "csv"


def test_shpc_glp_url_exceptions():
    entries = GROUPS["shpc-glp"]["entries"]
    e2022_01 = next(e for e in entries if e["year"] == 2022 and e["semester"] == 1)
    assert "precos-semestrais-glp-2022-01" in e2022_01["url"]
    e2021_01 = next(e for e in entries if e["year"] == 2021 and e["semester"] == 1)
    assert "precos-semestrais-glp2021-01" in e2021_01["url"]


# ---------------------------------------------------------------------------
# SHPC mensal
# ---------------------------------------------------------------------------

def test_shpc_monthly_count():
    # 12+12+12+5 = 41 months per product
    for group_id in ("shpc-diesel-gnv", "shpc-gasolina-etanol", "shpc-glp-mensal"):
        assert len(GROUPS[group_id]["entries"]) == 41, f"{group_id} count wrong"


def test_shpc_monthly_has_month_field():
    for group_id in ("shpc-diesel-gnv", "shpc-gasolina-etanol", "shpc-glp-mensal"):
        for entry in GROUPS[group_id]["entries"]:
            assert entry["month"] in range(1, 13)
            assert entry["semester"] is None
            assert entry["year"] is not None


def test_shpc_monthly_april_2026_is_xlsx():
    for group_id in ("shpc-diesel-gnv", "shpc-gasolina-etanol", "shpc-glp-mensal"):
        e = next(
            e for e in GROUPS[group_id]["entries"]
            if e["year"] == 2026 and e["month"] == 4
        )
        assert e["ext"] == "xlsx", f"{group_id} April 2026 should be xlsx"


def test_shpc_gasolina_etanol_feb_2026_typo_url():
    e = next(
        e for e in GROUPS["shpc-gasolina-etanol"]["entries"]
        if e["year"] == 2026 and e["month"] == 2
    )
    assert "cados-abertos-preco-gasolina-etanol" in e["url"]


# ---------------------------------------------------------------------------
# SHPC últimas 4 semanas
# ---------------------------------------------------------------------------

def test_shpc_4s_entries():
    entries = GROUPS["shpc-4s"]["entries"]
    assert len(entries) == 3
    ids = {e["id"] for e in entries}
    assert "shpc-4s-diesel-gnv" in ids
    assert "shpc-4s-gasolina-etanol" in ids
    assert "shpc-4s-glp" in ids


# ---------------------------------------------------------------------------
# vdpb-abertos and pp-abertos
# ---------------------------------------------------------------------------

def test_vdpb_abertos_count():
    assert len(GROUPS["vdpb-abertos"]["entries"]) == 23


def test_pp_abertos_count():
    assert len(GROUPS["pp-abertos"]["entries"]) == 6


def test_vdpb_abertos_all_csv():
    for entry in GROUPS["vdpb-abertos"]["entries"]:
        assert entry["ext"] == "csv"


def test_pp_abertos_all_csv():
    for entry in GROUPS["pp-abertos"]["entries"]:
        assert entry["ext"] == "csv"


# ---------------------------------------------------------------------------
# Aliases and resolution
# ---------------------------------------------------------------------------

def test_group_aliases_resolve():
    assert resolve_group("importacoes-exportacoes") == "ie"
    assert resolve_group("processamento-petroleo") == "pp"
    assert resolve_group("producao-biocombustiveis") == "pb"
    assert resolve_group("producao-petroleo-gas") == "ppg"
    assert resolve_group("vendas") == "vdpb"
    assert resolve_group("precos-combustiveis") == "shpc-ca"
    assert resolve_group("vendas-abertos") == "vdpb-abertos"
    assert resolve_group("processamento-abertos") == "pp-abertos"


def test_resolve_canonical_keys():
    for key in ALL_GROUP_KEYS:
        assert resolve_group(key) == key


def test_resolve_unknown_returns_none():
    assert resolve_group("nonexistent") is None


def test_list_datasets_all():
    all_entries = list_datasets()
    assert len(all_entries) > 0
    groups_present = {e["group"] for e in all_entries}
    assert groups_present == set(ALL_GROUP_KEYS)


def test_list_datasets_filtered():
    ie_entries = list_datasets("ie")
    assert all(e["group"] == "ie" for e in ie_entries)
    assert len(ie_entries) == 2

    ie_via_alias = list_datasets("importacoes-exportacoes")
    assert ie_entries == ie_via_alias


def test_list_datasets_unknown_group_raises():
    with pytest.raises(ValueError, match="Unknown group"):
        list_datasets("bogus")


def test_no_duplicate_ids():
    all_entries = list_datasets()
    ids = [e["id"] for e in all_entries]
    assert len(ids) == len(set(ids)), "Duplicate entry IDs found"
