"""Tests for anp_fetcher.catalog."""

import pytest
from anp_fetcher.catalog import (
    ALL_GROUP_KEYS,
    GROUPS,
    SHPC_GROUP_KEYS,
    list_datasets,
    resolve_group,
)

_DE_GROUPS = {"ie", "pp", "pb", "ppg", "vdpb"}
_DA_GROUPS = {
    # Wave 2
    "shpc-ca",
    "shpc-glp",
    "shpc-diesel-gnv",
    "shpc-gasolina-etanol",
    "shpc-glp-mensal",
    "shpc-4s",
    "vdpb-abertos",
    "pp-abertos",
    # Wave 3a
    "producao-el",
    "pb-abertos",
    "ie-abertos",
    "comercializacao-gn",
    "movimentacao-terminais",
    "armazenagem-terminais",
    "incidentes",
    "rodadas",
    "concessionarios",
    "revendedores",
    "revendas-glp",
    "registro-lubrificantes",
    "pml",
    "fiscalizacao",
    "royalties",
    # Wave 3b
    "movimentacao-gn",
    "tancagem",
    "pmqc",
    "movimentacao-derivados",
    "producao-poco-abertos",
    # Wave 3c
    "producao-fdp-mar",
    "producao-fdp-terra",
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
    required = {
        "id",
        "base_id",
        "name",
        "url",
        "ext",
        "group",
        "source",
        "year",
        "semester",
        "month",
    }
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
        e
        for e in GROUPS["vdpb"]["entries"]
        if e["base_id"] == "vendas-municipais-etanol-hidratado"
    ]
    e2000 = next(e for e in etanol if e["year"] == 2000)
    assert e2000["ext"] == "xlsx"
    e2001 = next(e for e in etanol if e["year"] == 2001)
    assert e2001["ext"] == "xls"

    gas_c = [
        e
        for e in GROUPS["vdpb"]["entries"]
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
    e = next(
        e
        for e in GROUPS["shpc-ca"]["entries"]
        if e["year"] == 2022 and e["semester"] == 1
    )
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
            e
            for e in GROUPS[group_id]["entries"]
            if e["year"] == 2026 and e["month"] == 4
        )
        assert e["ext"] == "xlsx", f"{group_id} April 2026 should be xlsx"


def test_shpc_gasolina_etanol_feb_2026_typo_url():
    e = next(
        e
        for e in GROUPS["shpc-gasolina-etanol"]["entries"]
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

# ---------------------------------------------------------------------------
# Onda 3a
# ---------------------------------------------------------------------------


def test_producao_el_count():
    assert len(GROUPS["producao-el"]["entries"]) == 7


def test_producao_el_all_csv():
    for e in GROUPS["producao-el"]["entries"]:
        assert e["ext"] == "csv"
        assert e["source"] == "dados-abertos"
        assert e["year"] is None
        assert "ppgn-el" in e["url"]


def test_pb_abertos_count():
    assert len(GROUPS["pb-abertos"]["entries"]) == 3


def test_ie_abertos_count():
    assert len(GROUPS["ie-abertos"]["entries"]) == 4


def test_ie_abertos_subfolders():
    urls = [e["url"] for e in GROUPS["ie-abertos"]["entries"]]
    assert any("/petroleo/" in u for u in urls)
    assert any("/gn/" in u for u in urls)
    assert any("/derivados/" in u for u in urls)
    assert any("/etanol/" in u for u in urls)


def test_comercializacao_gn_count():
    assert len(GROUPS["comercializacao-gn"]["entries"]) == 3


def test_comercializacao_gn_url_base():
    for e in GROUPS["comercializacao-gn"]["entries"]:
        assert "/assuntos/" in e["url"]  # URL fora do padrão /dados-abertos/arquivos/


def test_incidentes_count():
    assert len(GROUPS["incidentes"]["entries"]) == 5


def test_incidentes_ids():
    ids = {e["id"] for e in GROUPS["incidentes"]["entries"]}
    assert ids == {
        "issm-incidentes",
        "issm-classificacao",
        "issm-feridos",
        "issm-substancias",
        "issm-tipo",
    }


def test_rodadas_count():
    assert len(GROUPS["rodadas"]["entries"]) == 3


def test_concessionarios_count():
    assert len(GROUPS["concessionarios"]["entries"]) == 2


def test_fiscalizacao_count():
    assert len(GROUPS["fiscalizacao"]["entries"]) == 2


def test_fiscalizacao_xlsx():
    for e in GROUPS["fiscalizacao"]["entries"]:
        assert e["ext"] == "xlsx"
        assert "/paineis-dinamicos-da-anp/" in e["url"]


def test_royalties_count():
    assert len(GROUPS["royalties"]["entries"]) == 79


def test_royalties_uniao_url_irregularities():
    entries = [
        e for e in GROUPS["royalties"]["entries"] if e["base_id"] == "royalties-uniao"
    ]
    assert len(entries) == 17
    by_year = {e["year"]: e["url"] for e in entries}
    # underscore era for 2009-2018
    assert "royalties_uniao_2018.csv" in by_year[2018]
    # hyphen from 2019
    assert "royalties-uniao-2019.csv" in by_year[2019]
    # 2020 in different subfolder
    assert "/pg/2020/" in by_year[2020]


def test_royalties_estado_plural_2022_2023():
    entries = [
        e for e in GROUPS["royalties"]["entries"] if e["base_id"] == "royalties-estado"
    ]
    by_year = {e["year"]: e["url"] for e in entries}
    assert "royalties-estados-2022.csv" in by_year[2022]
    assert "royalties-estados-2023.csv" in by_year[2023]
    assert "royalties-estado-2024.csv" in by_year[2024]


def test_royalties_municipio_plural_2022_2023():
    entries = [
        e
        for e in GROUPS["royalties"]["entries"]
        if e["base_id"] == "royalties-municipio"
    ]
    by_year = {e["year"]: e["url"] for e in entries}
    assert "royalties-municipios-2022.csv" in by_year[2022]
    assert "royalties-municipios-2023.csv" in by_year[2023]


def test_royalties_pe_static():
    pe = [e for e in GROUPS["royalties"]["entries"] if e["id"].startswith("pe-")]
    assert len(pe) == 4
    ids = {e["id"] for e in pe}
    assert ids == {"pe-uniao", "pe-estado", "pe-municipio", "pe-campo"}
    for e in pe:
        assert e["year"] is None


def test_royalties_preco_ref_gn_epochs():
    entries = [
        e for e in GROUPS["royalties"]["entries"] if e["base_id"] == "preco-ref-gn"
    ]
    assert len(entries) == 16
    by_year = {e["year"]: e["url"] for e in entries}
    assert "precorefgn_2019.csv" in by_year[2019]  # underscore epoch
    assert "precoref-gn-2020.csv" in by_year[2020]  # transition
    assert "preco-referencia-gn-2021.csv" in by_year[2021]  # long name epoch


def test_royalties_preco_ref_petroleo_epochs():
    entries = [
        e
        for e in GROUPS["royalties"]["entries"]
        if e["base_id"] == "preco-ref-petroleo"
    ]
    assert len(entries) == 8
    by_year = {e["year"]: e["url"] for e in entries}
    assert "precorefpetro_2019.csv" in by_year[2019]
    assert "precoref-petro-2020-1.csv" in by_year[2020]
    assert "preco-referencia-petroleo-2021.csv" in by_year[2021]


def test_3a_all_static_have_no_partitions():
    static_groups = {
        "producao-el",
        "pb-abertos",
        "ie-abertos",
        "comercializacao-gn",
        "movimentacao-terminais",
        "armazenagem-terminais",
        "incidentes",
        "rodadas",
        "concessionarios",
        "revendedores",
        "revendas-glp",
        "registro-lubrificantes",
        "pml",
        "fiscalizacao",
    }
    for gid in static_groups:
        for e in GROUPS[gid]["entries"]:
            assert e["semester"] is None, f"{e['id']}: semester should be None"
            assert e["month"] is None, f"{e['id']}: month should be None"


def test_da_phases_source_all_dados_abertos():
    for gid in _DA_GROUPS:
        for e in GROUPS[gid]["entries"]:
            assert e["source"] == "dados-abertos", f"{e['id']}: wrong source"


def test_group_aliases_resolve():
    assert resolve_group("importacoes-exportacoes") == "ie"
    assert resolve_group("processamento-petroleo") == "pp"
    assert resolve_group("producao-biocombustiveis") == "pb"
    assert resolve_group("producao-petroleo-gas") == "ppg"
    assert resolve_group("vendas") == "vdpb"
    assert resolve_group("precos-combustiveis") == "shpc-ca"
    assert resolve_group("vendas-abertos") == "vdpb-abertos"
    assert resolve_group("processamento-abertos") == "pp-abertos"
    assert resolve_group("producao-estado") == "producao-el"
    assert resolve_group("participacoes-governamentais") == "royalties"
    assert resolve_group("mov-gas-gasoduto") == "movimentacao-gn"
    assert resolve_group("capacidade-tancagem") == "tancagem"
    assert resolve_group("qualidade-combustivel") == "pmqc"
    assert resolve_group("mov-derivados") == "movimentacao-derivados"
    assert resolve_group("producao-poco-da") == "producao-poco-abertos"
    assert resolve_group("fdp-mar") == "producao-fdp-mar"
    assert resolve_group("fdp-terra") == "producao-fdp-terra"
    assert resolve_group("importacoes-exportacoes-csv") == "ie-abertos"
    assert resolve_group("producao-biocombustiveis-csv") == "pb-abertos"


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


# ---------------------------------------------------------------------------
# Onda 3b & 3c specific tests
# ---------------------------------------------------------------------------


def test_movimentacao_gn_catalog():
    entries = GROUPS["movimentacao-gn"]["entries"]
    assert len(entries) == 66  # 12 * 5 + 6
    assert all(e["ext"] == "csv" for e in entries)
    assert all(e["month"] is not None for e in entries)


def test_tancagem_catalog():
    entries = GROUPS["tancagem"]["entries"]
    assert len(entries) == 36
    csv_entries = [e for e in entries if e["ext"] == "csv"]
    xlsx_entries = [e for e in entries if e["ext"] == "xlsx"]
    assert len(csv_entries) == 35
    assert len(xlsx_entries) == 1
    assert xlsx_entries[0]["year"] == 2022 and xlsx_entries[0]["month"] == 10


def test_pmqc_catalog():
    entries = GROUPS["pmqc"]["entries"]
    assert len(entries) == 248  # 124 months * 2 (csv + json)
    csv_entries = [e for e in entries if e["base_id"] == "pmqc-csv"]
    json_entries = [e for e in entries if e["base_id"] == "pmqc-json"]
    assert len(csv_entries) == 124
    assert len(json_entries) == 124
    # check custom extensions
    assert any(e["ext"] == "zip" for e in json_entries)
    assert any(e["ext"] == "csv" for e in json_entries)


def test_movimentacao_derivados_catalog():
    entries = GROUPS["movimentacao-derivados"]["entries"]
    assert len(entries) == 9
    assert all(e["ext"] == "zip" for e in entries)
    assert all(e["year"] is None for e in entries)


def test_producao_poco_abertos_catalog():
    entries = GROUPS["producao-poco-abertos"]["entries"]
    assert len(entries) == 52  # 12 * 3 (monthly) + 16 (annual)
    annual_entries = [e for e in entries if e["month"] is None]
    monthly_entries = [e for e in entries if e["month"] is not None]
    assert len(annual_entries) == 16
    assert len(monthly_entries) == 36
    assert all(e["ext"] == "zip" for e in entries)


def test_producao_fdp_mar_catalog():
    entries = GROUPS["producao-fdp-mar"]["entries"]
    assert len(entries) == 18
    assert all(e["ext"] == "csv" for e in entries)


def test_producao_fdp_terra_catalog():
    entries = GROUPS["producao-fdp-terra"]["entries"]
    assert len(entries) == 107
    assert all(e["ext"] == "csv" for e in entries)
