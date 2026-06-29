"""ANP Dados Abertos catalog.

Covers datasets published at:
https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/
"""

from ._catalog_base import DatasetEntry, GroupInfo, _static

_SOURCE = "dados-abertos"
_BASE = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos"

_SHPC_DSAS = f"{_BASE}/shpc/dsas"
_SHPC_DSAN = f"{_BASE}/shpc/dsan"
_SHPC_QUS = f"{_BASE}/shpc/qus"
_VDPB = f"{_BASE}/vdpb"
_VDPB_MUNI = f"{_VDPB}/vaehdpm"
_VDPB_HIST = f"{_BASE}/arquivos-vendas-anuais-de-etanol-hidratado-e-derivados-de-petroleo-por-estado"
_PPPD = f"{_BASE}/pppd"


def _sem_entry(
    group: str,
    base_id: str,
    name_prefix: str,
    year: int,
    sem: int,
    url: str,
    ext: str,
) -> DatasetEntry:
    return DatasetEntry(
        id=f"{base_id}-{year}-{sem:02d}",
        base_id=base_id,
        name=f"{name_prefix} — {sem}º sem. {year}",
        url=url,
        ext=ext,
        group=group,
        source=_SOURCE,
        year=year,
        semester=sem,
        month=None,
    )


def _mon_entry(
    group: str,
    base_id: str,
    name_prefix: str,
    year: int,
    month: int,
    url: str,
    ext: str,
) -> DatasetEntry:
    import calendar
    month_name = calendar.month_name[month].capitalize()
    # Portuguese month names
    _PT = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro",
    }
    return DatasetEntry(
        id=f"{base_id}-{year}-{month:02d}",
        base_id=base_id,
        name=f"{name_prefix} — {_PT[month]} {year}",
        url=url,
        ext=ext,
        group=group,
        source=_SOURCE,
        year=year,
        semester=None,
        month=month,
    )


# ---------------------------------------------------------------------------
# shpc-ca — SHPC Combustíveis Automotivos (Semestral 2004-2025)
#
# URL exceptions:
#   2022-01: precos-semestrais-ca.zip  (standard would be ca-2022-01.zip)
# Ext: year >= 2022 → zip; year <= 2021 → csv
# ---------------------------------------------------------------------------

def _ca_entry(year: int, sem: int) -> DatasetEntry:
    ext = "zip" if year >= 2022 else "csv"
    if (year, sem) == (2022, 1):
        url = f"{_SHPC_DSAS}/ca/precos-semestrais-ca.zip"
    else:
        url = f"{_SHPC_DSAS}/ca/ca-{year}-{sem:02d}.{ext}"
    return _sem_entry("shpc-ca", "shpc-ca", "Preços combustíveis automotivos", year, sem, url, ext)


_shpc_ca_entries: list[DatasetEntry] = [
    _ca_entry(year, sem)
    for year in range(2025, 2003, -1)
    for sem in (2, 1)
]

# ---------------------------------------------------------------------------
# shpc-glp — SHPC GLP P13 (Semestral 2004-2025)
#
# URL exceptions:
#   2022-01: precos-semestrais-glp-2022-01.csv
#   2021-01: precos-semestrais-glp2021-01.csv   (no hyphen before year)
# All CSV.
# ---------------------------------------------------------------------------

def _glp_sem_entry(year: int, sem: int) -> DatasetEntry:
    if (year, sem) == (2022, 1):
        url = f"{_SHPC_DSAS}/glp/precos-semestrais-glp-2022-01.csv"
    elif (year, sem) == (2021, 1):
        url = f"{_SHPC_DSAS}/glp/precos-semestrais-glp2021-01.csv"
    else:
        url = f"{_SHPC_DSAS}/glp/glp-{year}-{sem:02d}.csv"
    return _sem_entry("shpc-glp", "shpc-glp", "Preços GLP P13", year, sem, url, "csv")


_shpc_glp_entries: list[DatasetEntry] = [
    _glp_sem_entry(year, sem)
    for year in range(2025, 2003, -1)
    for sem in (2, 1)
]

# ---------------------------------------------------------------------------
# Monthly SHPC helpers
#
# 2023-2025 URL: .../shpc/dsan/{year}/precos-{product}-{month:02d}.csv
# 2026 URL:      .../shpc/dsan/{year}/{month:02d}-dados-abertos-precos-{product}.{ext}
# Exception: April 2026 is xlsx for all three monthly products.
# ---------------------------------------------------------------------------

def _dsan_url(year: int, month: int, product_old: str, product_new: str) -> tuple[str, str]:
    """Return (url, ext) for a monthly SHPC entry."""
    if year <= 2025:
        return f"{_SHPC_DSAN}/{year}/precos-{product_old}-{month:02d}.csv", "csv"
    # 2026+
    ext = "xlsx" if month == 4 else "csv"
    return f"{_SHPC_DSAN}/{year}/{month:02d}-dados-abertos-precos-{product_new}.{ext}", ext


# Monthly date grid: Jan 2023 – May 2026 (41 entries per product)
_MONTHLY_DATES: list[tuple[int, int]] = (
    [(y, m) for y in (2023, 2024, 2025) for m in range(1, 13)]
    + [(2026, m) for m in range(1, 6)]
)

# ---------------------------------------------------------------------------
# shpc-diesel-gnv — Diesel (S-500, S-10) + GNV (Mensal 2023-2026)
# ---------------------------------------------------------------------------

_shpc_diesel_entries: list[DatasetEntry] = []
for _y, _m in _MONTHLY_DATES:
    _url, _ext = _dsan_url(_y, _m, "diesel-gnv", "diesel-gnv")
    _shpc_diesel_entries.append(
        _mon_entry("shpc-diesel-gnv", "shpc-diesel-gnv",
                   "Preços diesel (S-500, S-10) + GNV", _y, _m, _url, _ext)
    )

# ---------------------------------------------------------------------------
# shpc-gasolina-etanol — Gasolina C + Etanol Hidratado (Mensal 2023-2026)
#
# Extra URL exception: February 2026 has a typo in the official filename:
#   "02-cados-abertos-preco-gasolina-etanol.csv"  (cados, not dados; preco, not precos)
# ---------------------------------------------------------------------------

_shpc_gas_etanol_entries: list[DatasetEntry] = []
for _y, _m in _MONTHLY_DATES:
    if (_y, _m) == (2026, 2):
        _url = f"{_SHPC_DSAN}/2026/02-cados-abertos-preco-gasolina-etanol.csv"
        _ext = "csv"
    else:
        _url, _ext = _dsan_url(_y, _m, "gasolina-etanol", "gasolina-etanol")
    _shpc_gas_etanol_entries.append(
        _mon_entry("shpc-gasolina-etanol", "shpc-gasolina-etanol",
                   "Preços gasolina C + etanol hidratado", _y, _m, _url, _ext)
    )

# ---------------------------------------------------------------------------
# shpc-glp-mensal — GLP P13 (Mensal 2023-2026)
# ---------------------------------------------------------------------------

_shpc_glp_mensal_entries: list[DatasetEntry] = []
for _y, _m in _MONTHLY_DATES:
    _url, _ext = _dsan_url(_y, _m, "glp", "glp")
    _shpc_glp_mensal_entries.append(
        _mon_entry("shpc-glp-mensal", "shpc-glp-mensal",
                   "Preços GLP P13 (mensal)", _y, _m, _url, _ext)
    )

# ---------------------------------------------------------------------------
# shpc-4s — Últimas 4 Semanas (3 arquivos estáticos, conteúdo atualizado semanalmente)
# ---------------------------------------------------------------------------

_shpc_4s_entries: list[DatasetEntry] = [
    _static("shpc-4s", _SOURCE, "shpc-4s-diesel-gnv",
            "Preços últimas 4 semanas — Diesel + GNV",
            f"{_SHPC_QUS}/ultimas-4-semanas-diesel-gnv.csv", "csv"),
    _static("shpc-4s", _SOURCE, "shpc-4s-gasolina-etanol",
            "Preços últimas 4 semanas — Gasolina C + Etanol",
            f"{_SHPC_QUS}/ultimas-4-semanas-gasolina-etanol.csv", "csv"),
    _static("shpc-4s", _SOURCE, "shpc-4s-glp",
            "Preços últimas 4 semanas — GLP P13",
            f"{_SHPC_QUS}/ultimas-4-semanas-glp.csv", "csv"),
]

# ---------------------------------------------------------------------------
# vdpb-abertos — Vendas de Derivados de Petróleo e Biocombustíveis (dados abertos)
# ---------------------------------------------------------------------------

_vdpb_abertos_entries: list[DatasetEntry] = [
    # Série histórica nacional
    _static("vdpb-abertos", _SOURCE, "vdpb-a-combustiveis-m3",
            "Vendas de derivados de petróleo e etanol (m³) 1990-2025",
            f"{_VDPB}/vendas-derivados-petroleo-e-etanol/vendas-combustiveis-m3-1990-2025.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-segmento",
            "Vendas de combustíveis por segmento (m³) 2012-2025",
            f"{_VDPB}/vcs/vendas-combustiveis-segmento-m3-2012-2025.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-glp-tipo",
            "Vendas de GLP por tipo de vasilhame (m³) 2007-2025",
            f"{_VDPB}/vct/vendas-glp-tipo-vasilhame-m3-2007-2025.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-diesel-tipo",
            "Vendas de óleo diesel por tipo (m³) 2013-2025",
            f"{_VDPB}/vct/vendas-oleo-diesel-tipo-m3-2013-2025.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-diesel-produtor",
            "Vendas de óleo diesel por produtor (m³) 2025-2026",
            f"{_VDPB}/vendas-por-produtor/vendas-oleo-diesel-produtores-m3-2025-2026.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-biodiesel",
            "Vendas de biodiesel B100 (m³)",
            f"{_VDPB}/vendas-de-biodiesel/vendas-biodiesel-b100-m3.csv", "csv"),
    # Vendas anuais por município
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-asfalto",
            "Vendas anuais de asfalto por município 1992-2024",
            f"{_VDPB_MUNI}/asfalto/vendas-anuais-de-asfalto-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-etanol-hidratado",
            "Vendas anuais de etanol hidratado por município 1990-2024",
            f"{_VDPB_MUNI}/etanol-hidratado/vendas-anuais-de-etanol-hidratado-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-gasolina-c",
            "Vendas anuais de gasolina C por município 1990-2024",
            f"{_VDPB_MUNI}/gasolina-c/vendas-anuais-de-gasolina-c-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-gasolina-aviacao",
            "Vendas anuais de gasolina de aviação por município 1990-2024",
            f"{_VDPB_MUNI}/gasolina-de-aviacao/vendas-anuais-de-gasolina-de-aviacao-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-glp",
            "Vendas anuais de GLP por município 1990-2024",
            f"{_VDPB_MUNI}/glp/vendas-anuais-de-glp-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-oleo-combustivel",
            "Vendas anuais de óleo combustível por município 1990-2024",
            f"{_VDPB_MUNI}/oleo-combustivel/vendas-anuais-de-oleo-combustivel-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-oleo-diesel",
            "Vendas anuais de óleo diesel por município 1990-2024",
            f"{_VDPB_MUNI}/oleo-diesel/vendas-anuais-de-oleo-diesel-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-querosene-aviacao",
            "Vendas anuais de querosene de aviação por município 1990-2024",
            f"{_VDPB_MUNI}/querosene-de-aviacao/vendas-anuais-de-querosene-de-aviacao-por-municipio.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-muni-querosene-iluminante",
            "Vendas anuais de querosene iluminante por município 1990-2024",
            f"{_VDPB_MUNI}/querosene-iluminante/vendas-anuais-de-querosene-iluminante-por-municipio.csv", "csv"),
    # Séries históricas por estado (1947-1989)
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-etanol",
            "Vendas de etanol hidratado por estado 1980-1989",
            f"{_VDPB_HIST}/vendas-etanol-hidratado-por-estado-1980-1989.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-gasolina-c",
            "Vendas de gasolina C por estado 1947-1989",
            f"{_VDPB_HIST}/vendas-gasolina-c-por-estado-1947-1989.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-gasolina-aviacao",
            "Vendas de gasolina de aviação por estado 1947-1989",
            f"{_VDPB_HIST}/vendas-gasolina-aviacao-por-estado-1947-1989.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-glp",
            "Vendas de GLP por estado 1953-1989",
            f"{_VDPB_HIST}/vendas-glp-por-estado-1953-1989.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-oleo-combustivel",
            "Vendas de óleo combustível por estado 1947-1989",
            f"{_VDPB_HIST}/vendas-oleo-combustivel-por-estado-1947-1989.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-oleo-diesel",
            "Vendas de óleo diesel por estado 1947-1989",
            f"{_VDPB_HIST}/vendas-oleo-diesel-por-estado-1947-1989.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-querosene-aviacao",
            "Vendas de querosene de aviação por estado 1959-1989",
            f"{_VDPB_HIST}/vendas-querosene-aviacao-por-estado-1959-1989.csv", "csv"),
    _static("vdpb-abertos", _SOURCE, "vdpb-a-hist-querosene-iluminante",
            "Vendas de querosene iluminante por estado 1947-1989",
            f"{_VDPB_HIST}/vendas-querosene-iluminante-por-estado-1947-1989.csv", "csv"),
]

# ---------------------------------------------------------------------------
# pp-abertos — Processamento de Petróleo e Produção de Derivados (dados abertos)
# ---------------------------------------------------------------------------

_pp_abertos_entries: list[DatasetEntry] = [
    _static("pp-abertos", _SOURCE, "pp-a-processamento-m3",
            "Processamento de petróleo (m³) 1990-2025",
            f"{_PPPD}/processamento-petroleo-m3-1990-2025.csv", "csv"),
    _static("pp-abertos", _SOURCE, "pp-a-derivados-refinaria",
            "Produção de derivados por refinaria (m³) 1990-2025",
            f"{_PPPD}/producao-derivados-petroleo-por-refinaria-m3-1990-2025.csv", "csv"),
    _static("pp-abertos", _SOURCE, "pp-a-gas-combustivel",
            "Produção de gás combustível por refinaria (mil m³) 2000-2025",
            f"{_PPPD}/producao-gas-combustivel-1000m3-2000-2025.csv", "csv"),
    _static("pp-abertos", _SOURCE, "pp-a-petroquimica",
            "Produção de derivados por central petroquímica (m³) 2001-2025",
            f"{_PPPD}/producao-derivados-centrais-petroquimicas-m3-2001-2025.csv", "csv"),
    _static("pp-abertos", _SOURCE, "pp-a-xisto",
            "Produção de derivados de xisto (m³) 2001-2025",
            f"{_PPPD}/producao-derivados-xisto-m3-2001-2025.csv", "csv"),
    _static("pp-abertos", _SOURCE, "pp-a-outros-produtores",
            "Produção de derivados por outros produtores (m³) 2003-2025",
            f"{_PPPD}/producao-derivados-outros-produtores-m3-2001-2025.csv", "csv"),
]

# ---------------------------------------------------------------------------
# Exported groups and aliases
# ---------------------------------------------------------------------------

GROUPS_DA: dict[str, GroupInfo] = {
    "shpc-ca": GroupInfo(
        name="SHPC — Combustíveis Automotivos (semestral)",
        entries=_shpc_ca_entries,
    ),
    "shpc-glp": GroupInfo(
        name="SHPC — GLP P13 (semestral)",
        entries=_shpc_glp_entries,
    ),
    "shpc-diesel-gnv": GroupInfo(
        name="SHPC — Diesel (S-500, S-10) + GNV (mensal)",
        entries=_shpc_diesel_entries,
    ),
    "shpc-gasolina-etanol": GroupInfo(
        name="SHPC — Gasolina C + Etanol Hidratado (mensal)",
        entries=_shpc_gas_etanol_entries,
    ),
    "shpc-glp-mensal": GroupInfo(
        name="SHPC — GLP P13 (mensal)",
        entries=_shpc_glp_mensal_entries,
    ),
    "shpc-4s": GroupInfo(
        name="SHPC — Últimas 4 Semanas",
        entries=_shpc_4s_entries,
    ),
    "vdpb-abertos": GroupInfo(
        name="Vendas de Derivados de Petróleo e Biocombustíveis (dados abertos)",
        entries=_vdpb_abertos_entries,
    ),
    "pp-abertos": GroupInfo(
        name="Processamento de Petróleo e Produção de Derivados (dados abertos)",
        entries=_pp_abertos_entries,
    ),
}

# "shpc" as a macro-alias is handled at the CLI level (expands to all 6 shpc-* groups)
GROUP_ALIASES_DA: dict[str, str] = {
    "precos-combustiveis": "shpc-ca",
    "vendas-abertos": "vdpb-abertos",
    "processamento-abertos": "pp-abertos",
}
