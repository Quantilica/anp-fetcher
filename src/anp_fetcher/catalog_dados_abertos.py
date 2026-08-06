"""ANP Dados Abertos catalog.

Covers all datasets published under "dados abertos" at the ANP website.
"""

from collections.abc import Callable

from ._catalog_base import DatasetEntry, GroupInfo, _static

_SOURCE = "dados-abertos"
_BASE = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos"
_ANP = "https://www.gov.br/anp/pt-br"

# Shared helper constants and functions for dados-abertos entries
_PT_LOWER = {
    1: "janeiro",
    2: "fevereiro",
    3: "marco",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro",
}


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
    _PT = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
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


# ===========================================================================
# SHPC (Sistema de Levantamento de Preços) — Ondas 2
# ===========================================================================

_SHPC_DSAS = f"{_BASE}/shpc/dsas"
_SHPC_DSAN = f"{_BASE}/shpc/dsan"
_SHPC_QUS = f"{_BASE}/shpc/qus"

# ---------------------------------------------------------------------------
# shpc-ca — SHPC Combustíveis Automotivos (Semestral 2004-2025)
# ---------------------------------------------------------------------------


def _ca_entry(year: int, sem: int) -> DatasetEntry:
    ext = "zip" if year >= 2022 else "csv"
    if (year, sem) == (2022, 1):
        url = f"{_SHPC_DSAS}/ca/precos-semestrais-ca.zip"
    else:
        url = f"{_SHPC_DSAS}/ca/ca-{year}-{sem:02d}.{ext}"
    return _sem_entry(
        "shpc-ca", "shpc-ca", "Preços combustíveis automotivos", year, sem, url, ext
    )


_shpc_ca_entries: list[DatasetEntry] = [
    _ca_entry(year, sem) for year in range(2025, 2003, -1) for sem in (2, 1)
]

# ---------------------------------------------------------------------------
# shpc-glp — SHPC GLP P13 (Semestral 2004-2025)
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
    _glp_sem_entry(year, sem) for year in range(2025, 2003, -1) for sem in (2, 1)
]

# ---------------------------------------------------------------------------
# Monthly SHPC helpers and definitions
# ---------------------------------------------------------------------------


def _dsan_url(
    year: int, month: int, product_old: str, product_new: str
) -> tuple[str, str, list[str]]:
    if year <= 2025:
        return f"{_SHPC_DSAN}/{year}/precos-{product_old}-{month:02d}.csv", "csv", []
    # For 2026 onwards, default to csv but add xlsx as fallback (and vice versa)
    ext = "csv"
    fallback_ext = "xlsx"
    url = f"{_SHPC_DSAN}/{year}/{month:02d}-dados-abertos-precos-{product_new}.{ext}"
    fallback_url = (
        f"{_SHPC_DSAN}/{year}/"
        f"{month:02d}-dados-abertos-precos-{product_new}.{fallback_ext}"
    )
    return url, ext, [fallback_url]


_MONTHLY_DATES: list[tuple[int, int]] = [
    (y, m) for y in (2023, 2024, 2025) for m in range(1, 13)
] + [(2026, m) for m in range(1, 6)]

# shpc-diesel-gnv
_shpc_diesel_entries: list[DatasetEntry] = []
for _y, _m in _MONTHLY_DATES:
    _url, _ext, _fallbacks = _dsan_url(_y, _m, "diesel-gnv", "diesel-gnv")
    _shpc_diesel_entries.append(
        _mon_entry(
            "shpc-diesel-gnv",
            "shpc-diesel-gnv",
            "Preços diesel (S-500, S-10) + GNV",
            _y,
            _m,
            _url,
            _ext,
        )
    )
    if _fallbacks:
        _shpc_diesel_entries[-1]["fallback_urls"] = _fallbacks

# shpc-gasolina-etanol
_shpc_gas_etanol_entries: list[DatasetEntry] = []
for _y, _m in _MONTHLY_DATES:
    _fallbacks = []
    if (_y, _m) == (2026, 2):
        _url = f"{_SHPC_DSAN}/2026/02-cados-abertos-preco-gasolina-etanol.csv"
        _ext = "csv"
    else:
        _url, _ext, _fallbacks = _dsan_url(_y, _m, "gasolina-etanol", "gasolina-etanol")
    _shpc_gas_etanol_entries.append(
        _mon_entry(
            "shpc-gasolina-etanol",
            "shpc-gasolina-etanol",
            "Preços gasolina C + etanol hidratado",
            _y,
            _m,
            _url,
            _ext,
        )
    )
    if _fallbacks:
        _shpc_gas_etanol_entries[-1]["fallback_urls"] = _fallbacks

# shpc-glp-mensal
_shpc_glp_mensal_entries: list[DatasetEntry] = []
for _y, _m in _MONTHLY_DATES:
    _url, _ext, _fallbacks = _dsan_url(_y, _m, "glp", "glp")
    _shpc_glp_mensal_entries.append(
        _mon_entry(
            "shpc-glp-mensal",
            "shpc-glp-mensal",
            "Preços GLP P13 (mensal)",
            _y,
            _m,
            _url,
            _ext,
        )
    )
    if _fallbacks:
        _shpc_glp_mensal_entries[-1]["fallback_urls"] = _fallbacks

# ---------------------------------------------------------------------------
# shpc-4s — Últimas 4 Semanas
# ---------------------------------------------------------------------------

_shpc_4s_entries: list[DatasetEntry] = [
    _static(
        "shpc-4s",
        _SOURCE,
        "shpc-4s-diesel-gnv",
        "Preços últimas 4 semanas — Diesel + GNV",
        f"{_SHPC_QUS}/ultimas-4-semanas-diesel-gnv.csv",
        "csv",
    ),
    _static(
        "shpc-4s",
        _SOURCE,
        "shpc-4s-gasolina-etanol",
        "Preços últimas 4 semanas — Gasolina C + Etanol",
        f"{_SHPC_QUS}/ultimas-4-semanas-gasolina-etanol.csv",
        "csv",
    ),
    _static(
        "shpc-4s",
        _SOURCE,
        "shpc-4s-glp",
        "Preços últimas 4 semanas — GLP P13",
        f"{_SHPC_QUS}/ultimas-4-semanas-glp.csv",
        "csv",
    ),
]


# ===========================================================================
# Vendas e Processamento — Onda 2
# ===========================================================================

_VDPB = f"{_BASE}/vdpb"
_VDPB_MUNI = f"{_VDPB}/vaehdpm"
_VDPB_HIST = (
    f"{_BASE}/arquivos-vendas-anuais-de-etanol-hidratado"
    "-e-derivados-de-petroleo-por-estado"
)
_PPPD = f"{_BASE}/pppd"

# ---------------------------------------------------------------------------
# vdpb-abertos — Vendas de Derivados e Biocombustíveis
# ---------------------------------------------------------------------------

_vdpb_abertos_entries: list[DatasetEntry] = [
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-combustiveis-m3",
        "Vendas de derivados de petróleo e etanol (m³) 1990-2025",
        f"{_VDPB}/vendas-derivados-petroleo-e-etanol/vendas-combustiveis-m3-1990-2025.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-segmento",
        "Vendas de combustíveis por segmento (m³) 2012-2025",
        f"{_VDPB}/vcs/vendas-combustiveis-segmento-m3-2012-2025.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-glp-tipo",
        "Vendas de GLP por tipo de vasilhame (m³) 2007-2025",
        f"{_VDPB}/vct/vendas-glp-tipo-vasilhame-m3-2007-2025.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-diesel-tipo",
        "Vendas de óleo diesel por tipo (m³) 2013-2025",
        f"{_VDPB}/vct/vendas-oleo-diesel-tipo-m3-2013-2025.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-diesel-produtor",
        "Vendas de óleo diesel por produtor (m³) 2025-2026",
        f"{_VDPB}/vendas-por-produtor/vendas-oleo-diesel-produtores-m3-2025-2026.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-biodiesel",
        "Vendas de biodiesel B100 (m³)",
        f"{_VDPB}/vendas-de-biodiesel/vendas-biodiesel-b100-m3.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-asfalto",
        "Vendas anuais de asfalto por município 1992-2024",
        f"{_VDPB_MUNI}/asfalto/vendas-anuais-de-asfalto-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-etanol-hidratado",
        "Vendas anuais de etanol hidratado por município 1990-2024",
        f"{_VDPB_MUNI}/etanol-hidratado/vendas-anuais-de-etanol-hidratado-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-gasolina-c",
        "Vendas anuais de gasolina C por município 1990-2024",
        f"{_VDPB_MUNI}/gasolina-c/vendas-anuais-de-gasolina-c-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-gasolina-aviacao",
        "Vendas anuais de gasolina de aviação por município 1990-2024",
        f"{_VDPB_MUNI}/gasolina-de-aviacao/vendas-anuais-de-gasolina-de-aviacao-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-glp",
        "Vendas anuais de GLP por município 1990-2024",
        f"{_VDPB_MUNI}/glp/vendas-anuais-de-glp-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-oleo-combustivel",
        "Vendas anuais de óleo combustível por município 1990-2024",
        f"{_VDPB_MUNI}/oleo-combustivel/vendas-anuais-de-oleo-combustivel-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-oleo-diesel",
        "Vendas anuais de óleo diesel por município 1990-2024",
        f"{_VDPB_MUNI}/oleo-diesel/vendas-anuais-de-oleo-diesel-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-querosene-aviacao",
        "Vendas anuais de querosene de aviação por município 1990-2024",
        f"{_VDPB_MUNI}/querosene-de-aviacao/vendas-anuais-de-querosene-de-aviacao-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-muni-querosene-iluminante",
        "Vendas anuais de querosene iluminante por município 1990-2024",
        f"{_VDPB_MUNI}/querosene-iluminante/vendas-anuais-de-querosene-iluminante-por-municipio.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-etanol",
        "Vendas de etanol hidratado por estado 1980-1989",
        f"{_VDPB_HIST}/vendas-etanol-hidratado-por-estado-1980-1989.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-gasolina-c",
        "Vendas de gasolina C por estado 1947-1989",
        f"{_VDPB_HIST}/vendas-gasolina-c-por-estado-1947-1989.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-gasolina-aviacao",
        "Vendas de gasolina de aviação por estado 1947-1989",
        f"{_VDPB_HIST}/vendas-gasolina-aviacao-por-estado-1947-1989.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-glp",
        "Vendas de GLP por estado 1953-1989",
        f"{_VDPB_HIST}/vendas-glp-por-estado-1953-1989.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-oleo-combustivel",
        "Vendas de óleo combustível por estado 1947-1989",
        f"{_VDPB_HIST}/vendas-oleo-combustivel-por-estado-1947-1989.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-oleo-diesel",
        "Vendas de óleo diesel por estado 1947-1989",
        f"{_VDPB_HIST}/vendas-oleo-diesel-por-estado-1947-1989.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-querosene-aviacao",
        "Vendas de querosene de aviação por estado 1959-1989",
        f"{_VDPB_HIST}/vendas-querosene-aviacao-por-estado-1959-1989.csv",
        "csv",
    ),
    _static(
        "vdpb-abertos",
        _SOURCE,
        "vdpb-a-hist-querosene-iluminante",
        "Vendas de querosene iluminante por estado 1947-1989",
        f"{_VDPB_HIST}/vendas-querosene-iluminante-por-estado-1947-1989.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# pp-abertos — Processamento de Petróleo e Produção de Derivados
# ---------------------------------------------------------------------------

_pp_abertos_entries: list[DatasetEntry] = [
    _static(
        "pp-abertos",
        _SOURCE,
        "pp-a-processamento-m3",
        "Processamento de petróleo (m³) 1990-2025",
        f"{_PPPD}/processamento-petroleo-m3-1990-2025.csv",
        "csv",
    ),
    _static(
        "pp-abertos",
        _SOURCE,
        "pp-a-derivados-refinaria",
        "Produção de derivados por refinaria (m³) 1990-2025",
        f"{_PPPD}/producao-derivados-petroleo-por-refinaria-m3-1990-2025.csv",
        "csv",
    ),
    _static(
        "pp-abertos",
        _SOURCE,
        "pp-a-gas-combustivel",
        "Produção de gás combustível por refinaria (mil m³) 2000-2025",
        f"{_PPPD}/producao-gas-combustivel-1000m3-2000-2025.csv",
        "csv",
    ),
    _static(
        "pp-abertos",
        _SOURCE,
        "pp-a-petroquimica",
        "Produção de derivados por central petroquímica (m³) 2001-2025",
        f"{_PPPD}/producao-derivados-centrais-petroquimicas-m3-2001-2025.csv",
        "csv",
    ),
    _static(
        "pp-abertos",
        _SOURCE,
        "pp-a-xisto",
        "Produção de derivados de xisto (m³) 2001-2025",
        f"{_PPPD}/producao-derivados-xisto-m3-2001-2025.csv",
        "csv",
    ),
    _static(
        "pp-abertos",
        _SOURCE,
        "pp-a-outros-produtores",
        "Produção de derivados por outros produtores (m³) 2003-2025",
        f"{_PPPD}/producao-derivados-outros-produtores-m3-2001-2025.csv",
        "csv",
    ),
]


# ===========================================================================
# Logística, Infraestrutura e Regulação — Onda 3a
# ===========================================================================

# ---------------------------------------------------------------------------
# producao-el — Produção por Estado e Localização
# ---------------------------------------------------------------------------

_PPGN_EL = f"{_BASE}/ppgn-el"
_producao_el_entries: list[DatasetEntry] = [
    _static(
        "producao-el",
        _SOURCE,
        "pel-petroleo",
        "Produção de petróleo por estado e localização (m³) 1997-2026",
        f"{_PPGN_EL}/producao-petroleo-m3.csv",
        "csv",
    ),
    _static(
        "producao-el",
        _SOURCE,
        "pel-lgn",
        "Produção de LGN por estado e localização (m³) 1997-2026",
        f"{_PPGN_EL}/producao-lgn-m3.csv",
        "csv",
    ),
    _static(
        "producao-el",
        _SOURCE,
        "pel-gas-natural",
        "Produção de gás natural por estado e localização (mil m³) 1997-2026",
        f"{_PPGN_EL}/producao-gas-natural-1000m3.csv",
        "csv",
    ),
    _static(
        "producao-el",
        _SOURCE,
        "pel-reinjecao",
        "Reinjeção de gás natural por estado e localização (mil m³) 2000-2026",
        f"{_PPGN_EL}/reinjecao-gn-1000m3.csv",
        "csv",
    ),
    _static(
        "producao-el",
        _SOURCE,
        "pel-queima-perda",
        "Queima e perda de gás natural por estado e localização (mil m³) 2000-2026",
        f"{_PPGN_EL}/queima-e-perda-gn-1000m3.csv",
        "csv",
    ),
    _static(
        "producao-el",
        _SOURCE,
        "pel-consumo-proprio",
        "Consumo próprio de gás natural por estado e localização (mil m³) 2000-2026",
        f"{_PPGN_EL}/consumo-proprio-gn1000m3.csv",
        "csv",
    ),
    _static(
        "producao-el",
        _SOURCE,
        "pel-gn-disponivel",
        "Gás natural disponível por estado e localização (mil m³) 2000-2026",
        f"{_PPGN_EL}/gn-disponivel-1000m3.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# pb-abertos — Produção de Biocombustíveis
# ---------------------------------------------------------------------------

_PB_ABERTOS = f"{_BASE}/arquivos-producao-de-biocombustiveis"
_pb_abertos_entries: list[DatasetEntry] = [
    _static(
        "pb-abertos",
        _SOURCE,
        "pba-biodiesel-2005-2023",
        "Produção de biodiesel B100 (m³) 2005-2023",
        f"{_PB_ABERTOS}/producao-biodiesel-m3-2005-2023.csv",
        "csv",
    ),
    _static(
        "pb-abertos",
        _SOURCE,
        "pba-biodiesel-2024-2026",
        "Produção de biodiesel B100 (m³) 2024-2026",
        f"{_PB_ABERTOS}/producao-biodiesel-m3-2024-2026.csv",
        "csv",
    ),
    _static(
        "pb-abertos",
        _SOURCE,
        "pba-etanol",
        "Produção de etanol anidro e hidratado (m³) 2012-2026",
        f"{_PB_ABERTOS}/producao-etanol-anidro-hidratado-m3-2012-2026.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# ie-abertos — Importações e Exportações (dados abertos CSV)
# ---------------------------------------------------------------------------

_IE_BASE = f"{_BASE}/ie"
_ie_abertos_entries: list[DatasetEntry] = [
    _static(
        "ie-abertos",
        _SOURCE,
        "iea-petroleo",
        "Importações e exportações de petróleo (m³) 2000-2025",
        f"{_IE_BASE}/petroleo/importacoes-exportacoes-petroleo-2000-2025.csv",
        "csv",
    ),
    _static(
        "ie-abertos",
        _SOURCE,
        "iea-gas-natural",
        "Importação de gás natural (mil m³) 2000-2025",
        f"{_IE_BASE}/gn/importacao-gas-natural-2000-2025.csv",
        "csv",
    ),
    _static(
        "ie-abertos",
        _SOURCE,
        "iea-derivados",
        "Importações e exportações de derivados de petróleo (m³) 2000-2025",
        f"{_IE_BASE}/derivados/importacoes-exportacoes-derivados-2000-2025.csv",
        "csv",
    ),
    _static(
        "ie-abertos",
        _SOURCE,
        "iea-etanol",
        "Importações e exportações de etanol (m³) 2012-2025",
        f"{_IE_BASE}/etanol/importacoes-exportacoes-etanol-2012-2025.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# comercializacao-gn — Comercialização de Gás Natural
# ---------------------------------------------------------------------------

_COM_GN = (
    f"{_ANP}/assuntos/movimentacao-estocagem-e-comercializacao-de-gas-natural"
    "/acompanhamento-do-mercado-de-gas-natural/ppg"
)
_comercializacao_gn_entries: list[DatasetEntry] = [
    _static(
        "comercializacao-gn",
        _SOURCE,
        "cgn-distribuidoras",
        "Comercialização de gás natural — distribuidoras e consumidores livres",
        f"{_COM_GN}/distribuidoras-consumidores-livres.csv",
        "csv",
    ),
    _static(
        "comercializacao-gn",
        _SOURCE,
        "cgn-produtores",
        "Comercialização de gás natural — vendas entre produtores",
        f"{_COM_GN}/vendas-entre-produtores.csv",
        "csv",
    ),
    _static(
        "comercializacao-gn",
        _SOURCE,
        "cgn-comercializadores",
        "Comercialização de gás natural — vendas aos comercializadores",
        f"{_COM_GN}/vendas-aos-comercializadores.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# movimentacao-terminais — Movimentação dos Terminais Aquaviários
# ---------------------------------------------------------------------------

_MOV_TERM = f"{_BASE}/arquivos-movimentacao-dos-terminais-aquaviarios"
_movimentacao_terminais_entries: list[DatasetEntry] = [
    _static(
        "movimentacao-terminais",
        _SOURCE,
        "movterm",
        "Movimentação dos terminais aquaviários de derivados de petróleo",
        f"{_MOV_TERM}/dados-abertos-movimentacao-terminais-aquaviarios.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# armazenagem-terminais — Capacidade de Armazenagem de Terminais
# ---------------------------------------------------------------------------

_CAT = f"{_BASE}/cat"
_armazenagem_terminais_entries: list[DatasetEntry] = [
    _static(
        "armazenagem-terminais",
        _SOURCE,
        "armazterm",
        "Capacidade de armazenagem de terminais de derivados de petróleo",
        f"{_CAT}/capacidade-armazenagem-terminais.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# incidentes — Incidentes de Segurança Operacional (E&P)
# ---------------------------------------------------------------------------

_ISSM = f"{_BASE}/issm"
_incidentes_entries: list[DatasetEntry] = [
    _static(
        "incidentes",
        _SOURCE,
        "issm-incidentes",
        "Incidentes de segurança operacional em E&P — tabela principal",
        f"{_ISSM}/incidentes.csv",
        "csv",
    ),
    _static(
        "incidentes",
        _SOURCE,
        "issm-classificacao",
        "Incidentes de segurança operacional — classificação",
        f"{_ISSM}/incidentes-classificacao.csv",
        "csv",
    ),
    _static(
        "incidentes",
        _SOURCE,
        "issm-feridos",
        "Incidentes de segurança operacional — feridos",
        f"{_ISSM}/incidentes-feridos.csv",
        "csv",
    ),
    _static(
        "incidentes",
        _SOURCE,
        "issm-substancias",
        "Incidentes de segurança operacional — substâncias envolvidas",
        f"{_ISSM}/incidentes-substancias.csv",
        "csv",
    ),
    _static(
        "incidentes",
        _SOURCE,
        "issm-tipo",
        "Incidentes de segurança operacional — tipos de incidente",
        f"{_ISSM}/incidentes-tipo.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# rodadas — Rodadas de Licitações
# ---------------------------------------------------------------------------

_RLPGN = f"{_BASE}/rlpgn"
_rodadas_entries: list[DatasetEntry] = [
    _static(
        "rodadas",
        _SOURCE,
        "rlpgn-blocos",
        "Rodadas de licitações — blocos ofertados (9ª–17ª rodadas)",
        f"{_RLPGN}/blocos-ofertados-rodadas.csv",
        "csv",
    ),
    _static(
        "rodadas",
        _SOURCE,
        "rlpgn-vencedoras",
        "Rodadas de licitações — ofertas vencedoras",
        f"{_RLPGN}/ofertas-vencedoras-rodadas.csv",
        "csv",
    ),
    _static(
        "rodadas",
        _SOURCE,
        "rlpgn-cessao",
        "Rodadas de licitações — processos de cessão de contratos",
        f"{_RLPGN}/processos-cessao-contratos.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# concessionarios — Relação de Concessionários
# ---------------------------------------------------------------------------

_RC = f"{_BASE}/rc"
_concessionarios_entries: list[DatasetEntry] = [
    _static(
        "concessionarios",
        _SOURCE,
        "rc-relacao",
        "Relação de concessionários — contratos ativos com percentuais por empresa",
        f"{_RC}/relacao-concessionarios.csv",
        "csv",
    ),
    _static(
        "concessionarios",
        _SOURCE,
        "rc-pais-origem",
        "Relação de concessionários — país de origem",
        f"{_RC}/relacao-pais-origem-concessionarios.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# revendedores — Cadastro Revendedores Varejistas
# ---------------------------------------------------------------------------

_REVENDEDORES = (
    f"{_BASE}/arquivos-dados-cadastrais-dos-revendedores-varejistas"
    "-de-combustiveis-automotivos"
)
_revendedores_entries: list[DatasetEntry] = [
    _static(
        "revendedores",
        _SOURCE,
        "revendedores-varejistas",
        "Cadastro de revendedores varejistas de combustíveis automotivos",
        f"{_REVENDEDORES}/dados-cadastrais-revendedores-varejistas-combustiveis-automoveis.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# revendas-glp — Cadastro de Revendas de GLP
# ---------------------------------------------------------------------------

_REVENDAS_GLP = (
    f"{_BASE}/arquivos-dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo-glp"
)
_revendas_glp_entries: list[DatasetEntry] = [
    _static(
        "revendas-glp",
        _SOURCE,
        "revendas-glp",
        "Cadastro de revendas de GLP (distribuidoras e revendedores)",
        f"{_REVENDAS_GLP}/cadastro-revendas-glp.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# registro-lubrificantes — Registro de Óleos e Graxas Lubrificantes
# ---------------------------------------------------------------------------

_REG_LUB = f"{_BASE}/arquivos-registro"
_registro_lubrificantes_entries: list[DatasetEntry] = [
    _static(
        "registro-lubrificantes",
        _SOURCE,
        "registro-lubrificantes",
        "Registro de óleos e graxas lubrificantes autorizados pela ANP",
        f"{_REG_LUB}/dados-abertos-registro-produtos.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# pml — Programa de Monitoramento dos Lubrificantes
# ---------------------------------------------------------------------------

_PML = f"{_BASE}/arquivos-pml"
_pml_entries: list[DatasetEntry] = [
    _static(
        "pml",
        _SOURCE,
        "pml",
        "PML — resultados do monitoramento de qualidade de lubrificantes",
        f"{_PML}/dados-abertos-pml.csv",
        "csv",
    ),
]

# ---------------------------------------------------------------------------
# fiscalizacao — Ações de Fiscalização do Abastecimento
# ---------------------------------------------------------------------------

_FISC = (
    f"{_ANP}/centrais-de-conteudo/paineis-dinamicos-da-anp"
    "/arquivos-dados-brutos-do-painel-dinamico-da-fiscalizacao"
    "-do-abastecimento-da-sfi"
)
_fiscalizacao_entries: list[DatasetEntry] = [
    _static(
        "fiscalizacao",
        _SOURCE,
        "fisc-1998-2018",
        "Ações de fiscalização do abastecimento — histórico 1998-2018",
        f"{_FISC}/dados-fisc-1998-2018.xlsx",
        "xlsx",
    ),
    _static(
        "fiscalizacao",
        _SOURCE,
        "fisc-2019",
        "Ações de fiscalização do abastecimento — a partir de 2019",
        f"{_FISC}/dados-fisc-a-partir-2019.xlsx",
        "xlsx",
    ),
]

# ---------------------------------------------------------------------------
# royalties — Participações Governamentais
# ---------------------------------------------------------------------------

_PG = f"{_BASE}/pg"


def _ru_url(year: int) -> str:
    if year == 2020:
        return f"{_PG}/2020/royalties-uniao-2020.csv"
    base = f"{_PG}/royalties-uniao"
    if year <= 2018:
        return f"{base}/royalties_uniao_{year}.csv"
    return f"{base}/royalties-uniao-{year}.csv"


def _re_url(year: int) -> str:
    base = f"{_PG}/royalties-estados"
    if year <= 2018:
        return f"{base}/royalties_estado_{year}.csv"
    if year in (2022, 2023):
        return f"{base}/royalties-estados-{year}.csv"
    return f"{base}/royalties-estado-{year}.csv"


def _rm_url(year: int) -> str:
    base = f"{_PG}/royalties-municipios"
    if year <= 2018:
        return f"{base}/royalties_municipio_{year}.csv"
    if year in (2022, 2023):
        return f"{base}/royalties-municipios-{year}.csv"
    return f"{base}/royalties-municipio-{year}.csv"


def _gn_ref_url(year: int) -> str:
    base = f"{_PG}/preco-referencia-gas-natural"
    if year <= 2019:
        return f"{base}/precorefgn_{year}.csv"
    if year == 2020:
        return f"{base}/precoref-gn-2020.csv"
    return f"{base}/preco-referencia-gn-{year}.csv"


def _petro_ref_url(year: int) -> str:
    base = f"{_PG}/preco-referencia-petroleo"
    if year <= 2019:
        return f"{base}/precorefpetro_{year}.csv"
    if year == 2020:
        return f"{base}/precoref-petro-2020-1.csv"
    return f"{base}/preco-referencia-petroleo-{year}.csv"


def _royalties_annual(
    base_id: str,
    name_prefix: str,
    years: list[int],
    url_fn: Callable[[int], str],
) -> list[DatasetEntry]:
    return [
        DatasetEntry(
            id=f"{base_id}-{y}",
            base_id=base_id,
            name=f"{name_prefix} {y}",
            url=url_fn(y),
            ext="csv",
            group="royalties",
            source=_SOURCE,
            year=y,
            semester=None,
            month=None,
        )
        for y in years
    ]


_PG_YEARS = list(range(2009, 2026))
_GN_REF_YEARS = list(range(2010, 2026))
_PETRO_REF_YEARS = list(range(2018, 2026))

_royalties_entries: list[DatasetEntry] = (
    _royalties_annual("royalties-uniao", "Royalties — União", _PG_YEARS, _ru_url)
    + _royalties_annual("royalties-estado", "Royalties — Estados", _PG_YEARS, _re_url)
    + _royalties_annual(
        "royalties-municipio", "Royalties — Municípios", _PG_YEARS, _rm_url
    )
    + [
        _static(
            "royalties",
            _SOURCE,
            "pe-uniao",
            "Participação especial — acumulado por União",
            f"{_PG}/participacao-especial/pe_uniao.csv",
            "csv",
        ),
        _static(
            "royalties",
            _SOURCE,
            "pe-estado",
            "Participação especial — acumulado por estado",
            f"{_PG}/participacao-especial/pe_estado.csv",
            "csv",
        ),
        _static(
            "royalties",
            _SOURCE,
            "pe-municipio",
            "Participação especial — acumulado por município",
            f"{_PG}/participacao-especial/pe_municipio.csv",
            "csv",
        ),
        _static(
            "royalties",
            _SOURCE,
            "pe-campo",
            "Participação especial — acumulado por campo",
            f"{_PG}/participacao-especial/pe_campo.csv",
            "csv",
        ),
    ]
    + _royalties_annual(
        "preco-ref-gn", "Preço de referência gás natural", _GN_REF_YEARS, _gn_ref_url
    )
    + _royalties_annual(
        "preco-ref-petroleo",
        "Preço de referência petróleo",
        _PETRO_REF_YEARS,
        _petro_ref_url,
    )
)


# ===========================================================================
# Logística, Qualidade e Poços — Onda 3b
# ===========================================================================

# ---------------------------------------------------------------------------
# movimentacao-gn — Movimentação de Gás Natural em Gasodutos
# ---------------------------------------------------------------------------

_MOV_GN_BASE = (
    f"{_BASE}/arquivos-movimentacao-de-gas-natural-em-gasodutos-de-transporte"
)


def _mov_gn_url(year: int, month: int) -> str:
    m_name = _PT_LOWER[month]
    if year == 2026:
        return f"{_MOV_GN_BASE}/2026/gn_{m_name}_2026.csv"
    elif year == 2025:
        if month in (1, 2):
            return f"{_MOV_GN_BASE}/2025/gn-{m_name}.csv"
        return f"{_MOV_GN_BASE}/2025/gn_{m_name}_2025.csv"
    elif year == 2024:
        if month == 12:
            return f"{_MOV_GN_BASE}/2024/gn_dezembro_2024.csv"
        return f"{_MOV_GN_BASE}/2024/gn-{m_name}.csv"
    elif year == 2023:
        if month == 11:
            return f"{_MOV_GN_BASE}/2023/gn_novembro_2023.csv"
        return f"{_MOV_GN_BASE}/2023/gn-{m_name}-2023.csv"
    elif year == 2022:
        return f"{_MOV_GN_BASE}/2022/gn-{m_name}.csv"
    else:  # 2021
        if month <= 4:
            return f"{_MOV_GN_BASE}/2021/gn-{m_name}-2021_rev1.csv"
        return f"{_MOV_GN_BASE}/2021/gn-{m_name}-2021.csv"


_mov_gn_entries: list[DatasetEntry] = []
for _y in range(2021, 2027):
    _max_m = 6 if _y == 2026 else 12
    for _m in range(1, _max_m + 1):
        _mov_gn_entries.append(
            _mon_entry(
                "movimentacao-gn",
                "movimentacao-gn",
                "Movimentação de gás natural em gasodutos",
                _y,
                _m,
                _mov_gn_url(_y, _m),
                "csv",
            )
        )

# ---------------------------------------------------------------------------
# tancagem — Tancagem do Abastecimento Nacional de Combustíveis
# ---------------------------------------------------------------------------

_TANC_BASE = (
    f"{_BASE}/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos"
)


def _tancagem_entries_list() -> list[DatasetEntry]:
    entries = []
    # 2026: Jan-Apr
    for m in range(1, 5):
        m_name = _PT_LOWER[m]
        entries.append(
            _mon_entry(
                "tancagem",
                "tancagem",
                "Tancagem do abastecimento",
                2026,
                m,
                f"{_TANC_BASE}/2026/{m_name}.csv",
                "csv",
            )
        )
    # 2025: Jan-Mar, maio-junho (month=6), julho-agosto (month=8),
    # setembro-a-novembro (month=11), dezembro
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2025,
            1,
            f"{_TANC_BASE}/2025/janeiro.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2025,
            2,
            f"{_TANC_BASE}/2025/fevereiro.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2025,
            3,
            f"{_TANC_BASE}/2025/marco.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento (Maio a Junho)",
            2025,
            6,
            f"{_TANC_BASE}/2025/maio-junho.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento (Julho a Agosto)",
            2025,
            8,
            f"{_TANC_BASE}/2025/julho-agosto.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento (Setembro a Novembro)",
            2025,
            11,
            f"{_TANC_BASE}/2025/setembro-a-novembro.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2025,
            12,
            f"{_TANC_BASE}/2025/dezembro.csv",
            "csv",
        )
    )

    # 2024: Jan, Feb, marco-julho (month=7), Aug, setembro-outubro (month=10), Nov, Dec
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2024,
            1,
            f"{_TANC_BASE}/2024/janeiro.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2024,
            2,
            f"{_TANC_BASE}/2024/fevereiro.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento (Março a Julho)",
            2024,
            7,
            f"{_TANC_BASE}/2024/marco-julho.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2024,
            8,
            f"{_TANC_BASE}/2024/agosto.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento (Setembro e Outubro)",
            2024,
            10,
            f"{_TANC_BASE}/2024/setembro-outubro.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2024,
            11,
            f"{_TANC_BASE}/2024/novembro.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2024,
            12,
            f"{_TANC_BASE}/2024/dezembro.csv",
            "csv",
        )
    )

    # 2023: Jan-Dec (except Jul)
    for m in (1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12):
        m_name = _PT_LOWER[m]
        entries.append(
            _mon_entry(
                "tancagem",
                "tancagem",
                "Tancagem do abastecimento",
                2023,
                m,
                f"{_TANC_BASE}/2023/{m_name}.csv",
                "csv",
            )
        )

    # 2022: Jun-Dec
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2022,
            6,
            f"{_TANC_BASE}/2022/tancagem_terminais_dados_abertos_junho_2022.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2022,
            7,
            f"{_TANC_BASE}/2022/tancagem_terminais_dados_abertos_julho_2022.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2022,
            8,
            f"{_TANC_BASE}/2022/tancagem_terminais_dados_abertos_v1.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2022,
            9,
            f"{_TANC_BASE}/2022/tancagem_terminais_dados_abertos_2022_09_01.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2022,
            10,
            f"{_TANC_BASE}/2022/tancagem_terminais_dados_abertos_outubro_2022-csv.xlsx",
            "xlsx",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2022,
            11,
            f"{_TANC_BASE}/2022/tancagem_terminais_dados_abertos_novembro_2022.csv",
            "csv",
        )
    )
    entries.append(
        _mon_entry(
            "tancagem",
            "tancagem",
            "Tancagem do abastecimento",
            2022,
            12,
            f"{_TANC_BASE}/2022/tancagem_terminais_dados_abertos_dezembro_2022.csv",
            "csv",
        )
    )

    return entries


_tancagem_entries = _tancagem_entries_list()

# ---------------------------------------------------------------------------
# pmqc — Monitoramento da Qualidade dos Combustíveis
# ---------------------------------------------------------------------------

_PMQC_BASE = f"{_BASE}/pmqc"


def _pmqc_entries_list() -> list[DatasetEntry]:
    entries = []
    for y in range(2016, 2027):
        max_m = 4 if y == 2026 else 12
        for m in range(1, max_m + 1):
            csv_ext = "csv"
            fallback_csv = None
            if y == 2026:
                csv_url = f"{_PMQC_BASE}/2026/pmqc_2026_{m:02d}.csv"
                fallback_csv = f"{_PMQC_BASE}/2026/pmqc-{m:02d}.csv"
            elif y == 2025:
                if m in (1, 2, 3):
                    csv_url = f"{_PMQC_BASE}/2025/pmqc-{m:02d}.csv"
                elif m in (4, 5, 6):
                    csv_url = f"{_PMQC_BASE}/2025/pmqc_2025_{m:02d}.csv"
                else:
                    csv_url = f"{_PMQC_BASE}/2025/pmqc-2025-m:02d.csv".replace(
                        "m:02d", f"{m:02d}"
                    )
            elif y in (2024, 2023):
                csv_url = f"{_PMQC_BASE}/{y}/pmqc-{m:02d}.csv"
            elif y == 2022:
                if m <= 6:
                    csv_url = f"{_PMQC_BASE}/2022/2022-{m:02d}-pmqc.csv"
                else:
                    csv_url = f"{_PMQC_BASE}/2022/pmqc_2022_{m:02d}.csv"
            elif y == 2021:
                if m in (4, 5):
                    csv_url = f"{_PMQC_BASE}/2021/2021-{m:02d}-pmqc-csv.csv"
                else:
                    csv_url = f"{_PMQC_BASE}/2021/2021-{m:02d}-pmqc.csv"
            elif y in (2020, 2019):
                csv_url = f"{_PMQC_BASE}/{y}/{y}-{m:02d}-pmqc.csv"
                fallback_csv = f"{_PMQC_BASE}/{y}/pmqc_{y}_{m:02d}.csv"
            elif y == 2018:
                csv_url = f"{_PMQC_BASE}/2018/pmqc_2018_{m:02d}.csv"
                fallback_csv = f"{_PMQC_BASE}/2018/pmqc-{m:02d}.csv"
            elif y == 2017:
                if m == 8:
                    csv_url = f"{_PMQC_BASE}/2017/pmqc_2017_08-1.csv"
                else:
                    csv_url = f"{_PMQC_BASE}/2017/pmqc_2017_{m:02d}.csv"
            else:  # 2016
                csv_url = f"{_PMQC_BASE}/2016/pmqc_2016_{m:02d}.csv"

            e_csv = _mon_entry(
                "pmqc",
                "pmqc-csv",
                "Qualidade combustíveis PMQC (CSV)",
                y,
                m,
                csv_url,
                csv_ext,
            )
            if fallback_csv:
                e_csv["fallback_urls"] = [fallback_csv]
            entries.append(e_csv)

            json_ext = "json"
            fallback_json = None
            if y == 2026:
                json_url = f"{_PMQC_BASE}/2026/pmqc_2026_{m:02d}.json"
                fallback_json = f"{_PMQC_BASE}/2026/pmqc-{m:02d}.json"
            elif y == 2025:
                if m <= 6:
                    json_url = f"{_PMQC_BASE}/2025/pmqc_2025_{m:02d}.json"
                else:
                    json_url = f"{_PMQC_BASE}/2025/pmqc-2025-{m:02d}.json"
            elif y == 2024:
                if m == 1:
                    json_url = f"{_PMQC_BASE}/2024/pmqc_2024_01.json"
                elif m == 2:
                    json_url = f"{_PMQC_BASE}/2024/pmqc-02_json.zip"
                    json_ext = "zip"
                else:
                    json_url = f"{_PMQC_BASE}/2024/pmqc-{m:02d}.json"
                    fallback_json = f"{_PMQC_BASE}/2024/pmqc_{y}_{m:02d}.json"
            elif y == 2023:
                if m >= 10:
                    json_url = f"{_PMQC_BASE}/2023/pmqc_2023_{m:02d}.json"
                else:
                    json_url = f"{_PMQC_BASE}/2023/pmqc-{m:02d}.json"
            elif y == 2022:
                if m <= 6:
                    json_url = f"{_PMQC_BASE}/2022/2022-{m:02d}-pmqc.json"
                else:
                    json_url = f"{_PMQC_BASE}/2022/pmqc_2022_{m:02d}.json"
            elif y == 2021:
                if m == 6:
                    json_url = f"{_PMQC_BASE}/2021/202106pmqc.csv"
                    json_ext = "csv"
                else:
                    json_url = f"{_PMQC_BASE}/2021/2021-{m:02d}-pmqc.json"
            elif y in (2020, 2019):
                json_url = f"{_PMQC_BASE}/{y}/{y}-{m:02d}-pmqc.json"
            elif y == 2018:
                json_url = f"{_PMQC_BASE}/2018/{y}-{m:02d}-pmqc.json"
            elif y == 2017:
                json_url = f"{_PMQC_BASE}/2017/pmqc_2017_{m:02d}.json"
            else:  # 2016
                if m == 12:
                    json_url = f"{_PMQC_BASE}/2016/pmqc_2016_12-1.json"
                else:
                    json_url = f"{_PMQC_BASE}/2016/pmqc_2016_{m:02d}.json"

            e_json = _mon_entry(
                "pmqc",
                "pmqc-json",
                "Qualidade combustíveis PMQC (JSON)",
                y,
                m,
                json_url,
                json_ext,
            )
            if fallback_json:
                e_json["fallback_urls"] = [fallback_json]
            entries.append(e_json)
    return entries


_pmqc_entries = _pmqc_entries_list()

# ---------------------------------------------------------------------------
# movimentacao-derivados — Logística de Derivados (ZIPs)
# ---------------------------------------------------------------------------

_MDPG_BASE = f"{_BASE}/mdpg"
_movimentacao_derivados_entries: list[DatasetEntry] = [
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-asfalto",
        "Movimentação de asfalto",
        f"{_MDPG_BASE}/asfalto.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-aviacao",
        "Movimentação de combustível de aviação",
        f"{_MDPG_BASE}/aviacao.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-liquidos",
        "Movimentação de combustíveis líquidos",
        f"{_MDPG_BASE}/liquidos.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-glp",
        "Movimentação de GLP",
        f"{_MDPG_BASE}/glp.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-lubrificante",
        "Movimentação de lubrificantes",
        f"{_MDPG_BASE}/lubrificante.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-solvente",
        "Movimentação de solventes",
        f"{_MDPG_BASE}/solvente.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-trr",
        "Movimentação TRR",
        f"{_MDPG_BASE}/trr.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-fornecedores",
        "Fornecedores e vendas diretas",
        f"{_MDPG_BASE}/fornecedores-vendas-diretas.zip",
        "zip",
    ),
    _static(
        "movimentacao-derivados",
        _SOURCE,
        "mdpg-logistica",
        "Movimentação logística de abastecimento",
        f"{_MDPG_BASE}/movimentacaologistica.zip",
        "zip",
    ),
]

# ---------------------------------------------------------------------------
# producao-poco-abertos — Produção por Poço
# ---------------------------------------------------------------------------

_POCOS_BASE = f"{_BASE}/arquivos-producao-de-petroleo-e-gas-natural-por-poco"


def _producao_poco_abertos_list() -> list[DatasetEntry]:
    entries = []
    # 2023: Jan-Dec (monthly)
    for m in range(1, 13):
        entries.append(
            _mon_entry(
                "producao-poco-abertos",
                "producao-poco-da",
                "Produção por poço",
                2023,
                m,
                f"{_POCOS_BASE}/2023/producao-{m:02d}.zip",
                "zip",
            )
        )
    # 2022: Jan-Dec (monthly)
    for m in range(1, 13):
        if m == 5:
            url = f"{_POCOS_BASE}/2022/2022_05_producao.zip"
        elif m == 11:
            url = f"{_POCOS_BASE}/2022/2022_11_producao.zip"
        elif m == 12:
            url = f"{_POCOS_BASE}/2022/2022_12_producao.zip"
        else:
            url = f"{_POCOS_BASE}/2022/producao-2022-{m:02d}.zip"
        entries.append(
            _mon_entry(
                "producao-poco-abertos",
                "producao-poco-da",
                "Produção por poço",
                2022,
                m,
                url,
                "zip",
            )
        )
    # 2021: Jan-Dec (monthly)
    for m in range(1, 13):
        if m <= 7:
            url = f"{_POCOS_BASE}/2021_{m:02d}_producao.zip"
        else:
            url = f"{_POCOS_BASE}/2021-{m:02d}-producao.zip"
        entries.append(
            _mon_entry(
                "producao-poco-abertos",
                "producao-poco-da",
                "Produção por poço",
                2021,
                m,
                url,
                "zip",
            )
        )
    # 2005-2020: annual
    for y in range(2005, 2021):
        entries.append(
            DatasetEntry(
                id=f"producao-poco-da-{y}",
                base_id="producao-poco-da",
                name=f"Produção por poço — {y}",
                url=f"{_POCOS_BASE}/producao-por-poco-{y}.zip",
                ext="zip",
                group="producao-poco-abertos",
                source=_SOURCE,
                year=y,
                semester=None,
                month=None,
            )
        )
    return entries


_producao_poco_abertos_entries = _producao_poco_abertos_list()


# ===========================================================================
# Fase de Desenvolvimento e Produção (FDP) — Onda 3c
# ===========================================================================

_FDP_BASE = (
    f"{_BASE}/arquivos-fase-de-desenvolvimento-e-producao/"
    "arquivos-producao-de-petroleo-e-gas-natural-nacional"
)

# ---------------------------------------------------------------------------
# producao-fdp-mar — Produção em Mar
# ---------------------------------------------------------------------------

_FDP_MAR_BASE = f"{_FDP_BASE}/pm"


def _fdp_mar_entries_list() -> list[DatasetEntry]:
    entries = []
    # 2026-2019: anual
    for y in range(2019, 2027):
        if y == 2024:
            url = f"{_FDP_MAR_BASE}/producao_por_poco_2024.csv"
        else:
            url = f"{_FDP_MAR_BASE}/producao-mar-{y}.csv"
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-mar-{y}",
                base_id="producao-fdp-mar",
                name=f"Produção em mar — {y}",
                url=url,
                ext="csv",
                group="producao-fdp-mar",
                source=_SOURCE,
                year=y,
                semester=None,
                month=None,
            )
        )

    # Consolidated ranges
    consolidations = [
        ("2016-2018", 2018),
        ("2013-2015", 2015),
        ("2010-2012", 2012),
        ("2005-2009", 2009),
        ("2001-2004", 2004),
        ("1998-2000", 2000),
        ("1994-1997", 1997),
        ("1989-1993", 1993),
        ("1980-1988", 1988),
        ("1941-1979", 1979),
    ]
    for range_str, end_year in consolidations:
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-mar-{range_str}",
                base_id="producao-fdp-mar",
                name=f"Produção em mar consolidada — {range_str}",
                url=f"{_FDP_MAR_BASE}/producao-mar-{range_str}.csv",
                ext="csv",
                group="producao-fdp-mar",
                source=_SOURCE,
                year=end_year,
                semester=None,
                month=None,
            )
        )
    return entries


_fdp_mar_entries = _fdp_mar_entries_list()

# ---------------------------------------------------------------------------
# producao-fdp-terra — Produção em Terra
# ---------------------------------------------------------------------------

_FDP_TERRA_BASE = f"{_FDP_BASE}/pt"


def _fdp_terra_entries_list() -> list[DatasetEntry]:
    entries = []
    # 2026: Q1 (month=3)
    entries.append(
        DatasetEntry(
            id="producao-fdp-terra-2026-q1",
            base_id="producao-fdp-terra",
            name="Produção em terra — 1º trim. 2026",
            url=f"{_FDP_TERRA_BASE}/2026/producao_por_poco_terra_2026_1_trim.csv",
            ext="csv",
            group="producao-fdp-terra",
            source=_SOURCE,
            year=2026,
            semester=None,
            month=3,
        )
    )

    # 2025: Q1-Q4 (months: 3, 6, 9, 12)
    for q in range(1, 5):
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-2025-q{q}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {q}º trim. 2025",
                url=f"{_FDP_TERRA_BASE}/2025/producao_por_poco_terra_2025_{q}_trim.csv",
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=2025,
                semester=None,
                month=q * 3,
            )
        )

    # 2024: Q1-Q4
    for q in range(1, 5):
        if q == 4:
            url = f"{_FDP_TERRA_BASE}/2024/producao_por_poco_terra_trim_4.csv"
        else:
            url = f"{_FDP_TERRA_BASE}/2024/producao-por-poco-terra-trim-{q}.csv"
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-2024-q{q}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {q}º trim. 2024",
                url=url,
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=2024,
                semester=None,
                month=q * 3,
            )
        )

    # 2023: Q1-Q4
    for q in range(1, 5):
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-2023-q{q}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {q}º trim. 2023",
                url=f"{_FDP_TERRA_BASE}/2023/producao-terra-{q}-trim.csv",
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=2023,
                semester=None,
                month=q * 3,
            )
        )

    # 2022: Q1-Q4
    for q in range(1, 5):
        if q in (1, 2):
            url = f"{_FDP_TERRA_BASE}/2022/producao-terra-2022-{q}-trim.csv"
        else:
            url = f"{_FDP_TERRA_BASE}/2022/producao-terra-{q}-trim.csv"
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-2022-q{q}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {q}º trim. 2022",
                url=url,
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=2022,
                semester=None,
                month=q * 3,
            )
        )

    # 2021: Q1-Q4
    for q in range(1, 5):
        if q == 2:
            url = f"{_FDP_TERRA_BASE}/2021/producao-terra-2021-2-trim-ago21.csv"
        else:
            url = f"{_FDP_TERRA_BASE}/2021/producao-terra-2021-{q}-trim.csv"
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-2021-q{q}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {q}º trim. 2021",
                url=url,
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=2021,
                semester=None,
                month=q * 3,
            )
        )

    # 2020: Q1-Q4
    for q in range(1, 5):
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-2020-q{q}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {q}º trim. 2020",
                url=f"{_FDP_TERRA_BASE}/2020/producao-terra-2020-{q}-trim.csv",
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=2020,
                semester=None,
                month=q * 3,
            )
        )

    # 2019: Q1-Q4
    for q in range(1, 5):
        if q == 1:
            url = f"{_FDP_TERRA_BASE}/2019/producaoterra20191trim.csv"
        elif q in (2, 3):
            url = f"{_FDP_TERRA_BASE}/2019/producao-terra-2019-{q}trim.csv"
        else:
            url = f"{_FDP_TERRA_BASE}/2019/producao-terra-2019-4-trim.csv"
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-2019-q{q}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {q}º trim. 2019",
                url=url,
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=2019,
                semester=None,
                month=q * 3,
            )
        )

    # 2018-2016: Q1-Q4
    for y in (2018, 2017, 2016):
        for q in range(1, 5):
            entries.append(
                DatasetEntry(
                    id=f"producao-fdp-terra-{y}-q{q}",
                    base_id="producao-fdp-terra",
                    name=f"Produção em terra — {q}º trim. {y}",
                    url=f"{_FDP_TERRA_BASE}/{y}/producao-terra-{y}-{q}trim.csv",
                    ext="csv",
                    group="producao-fdp-terra",
                    source=_SOURCE,
                    year=y,
                    semester=None,
                    month=q * 3,
                )
            )

    # 2015-1989: Semestrais
    for y in range(1989, 2016):
        for s in (1, 2):
            entries.append(
                DatasetEntry(
                    id=f"producao-fdp-terra-{y}-s{s}",
                    base_id="producao-fdp-terra",
                    name=f"Produção em terra — {s}º sem. {y}",
                    url=f"{_FDP_TERRA_BASE}/{y}/producao-terra-{y}-{s}sem.csv",
                    ext="csv",
                    group="producao-fdp-terra",
                    source=_SOURCE,
                    year=y,
                    semester=s,
                    month=None,
                )
            )

    # 1988-1983: Anual under pt/1988-1983/
    for y in range(1983, 1989):
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-{y}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra — {y}",
                url=f"{_FDP_TERRA_BASE}/1988-1983/producao-terra-{y}.csv",
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=y,
                semester=None,
                month=None,
            )
        )

    # Older consolidated ranges under pt/1982-1941/
    consolidations = [
        ("1981-1982", 1982),
        ("1978-1980", 1980),
        ("1975-1977", 1977),
        ("1970-1974", 1974),
        ("1967-1970", 1970),
        ("1941-1966", 1966),
    ]
    for range_str, end_year in consolidations:
        entries.append(
            DatasetEntry(
                id=f"producao-fdp-terra-{range_str}",
                base_id="producao-fdp-terra",
                name=f"Produção em terra consolidada — {range_str}",
                url=f"{_FDP_TERRA_BASE}/1982-1941/producao-terra-{range_str}.csv",
                ext="csv",
                group="producao-fdp-terra",
                source=_SOURCE,
                year=end_year,
                semester=None,
                month=None,
            )
        )
    return entries


_fdp_terra_entries = _fdp_terra_entries_list()


# ===========================================================================
# Consolidated Exports for all Dados Abertos
# ===========================================================================

GROUPS_DA: dict[str, GroupInfo] = {
    # Wave 2
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
    # Wave 3a
    "producao-el": GroupInfo(
        name="Produção de Petróleo e Gás Natural por Estado e Localização",
        entries=_producao_el_entries,
    ),
    "pb-abertos": GroupInfo(
        name="Produção de Biocombustíveis (dados abertos)",
        entries=_pb_abertos_entries,
    ),
    "ie-abertos": GroupInfo(
        name="Importações e Exportações de Petróleo e Derivados (dados abertos)",
        entries=_ie_abertos_entries,
    ),
    "comercializacao-gn": GroupInfo(
        name="Comercialização de Gás Natural",
        entries=_comercializacao_gn_entries,
    ),
    "movimentacao-terminais": GroupInfo(
        name="Movimentação dos Terminais Aquaviários",
        entries=_movimentacao_terminais_entries,
    ),
    "armazenagem-terminais": GroupInfo(
        name="Capacidade de Armazenagem de Terminais",
        entries=_armazenagem_terminais_entries,
    ),
    "incidentes": GroupInfo(
        name="Incidentes de Segurança Operacional (E&P)",
        entries=_incidentes_entries,
    ),
    "rodadas": GroupInfo(
        name="Rodadas de Licitações de Petróleo e Gás Natural",
        entries=_rodadas_entries,
    ),
    "concessionarios": GroupInfo(
        name="Relação de Concessionários",
        entries=_concessionarios_entries,
    ),
    "revendedores": GroupInfo(
        name="Cadastro de Revendedores Varejistas de Combustíveis Automotivos",
        entries=_revendedores_entries,
    ),
    "revendas-glp": GroupInfo(
        name="Cadastro de Revendas de GLP",
        entries=_revendas_glp_entries,
    ),
    "registro-lubrificantes": GroupInfo(
        name="Registro de Óleos e Graxas Lubrificantes",
        entries=_registro_lubrificantes_entries,
    ),
    "pml": GroupInfo(
        name="PML — Programa de Monitoramento dos Lubrificantes",
        entries=_pml_entries,
    ),
    "fiscalizacao": GroupInfo(
        name="Ações de Fiscalização do Abastecimento",
        entries=_fiscalizacao_entries,
    ),
    "royalties": GroupInfo(
        name="Participações Governamentais (Royalties e Participação Especial)",
        entries=_royalties_entries,
    ),
    # Wave 3b
    "movimentacao-gn": GroupInfo(
        name="Movimentação de Gás Natural em Gasodutos (dados abertos)",
        entries=_mov_gn_entries,
    ),
    "tancagem": GroupInfo(
        name="Tancagem do Abastecimento Nacional de Combustíveis (dados abertos)",
        entries=_tancagem_entries,
    ),
    "pmqc": GroupInfo(
        name="Programa de Monitoramento da Qualidade dos Combustíveis (dados abertos)",
        entries=_pmqc_entries,
    ),
    "movimentacao-derivados": GroupInfo(
        name="Movimentação de Derivados de Petróleo (dados abertos)",
        entries=_movimentacao_derivados_entries,
    ),
    "producao-poco-abertos": GroupInfo(
        name="Produção de Petróleo e Gás Natural por Poço (dados abertos)",
        entries=_producao_poco_abertos_entries,
    ),
    # Wave 3c
    "producao-fdp-mar": GroupInfo(
        name="Produção de Petróleo e Gás Natural — Mar (FDP, dados abertos)",
        entries=_fdp_mar_entries,
    ),
    "producao-fdp-terra": GroupInfo(
        name="Produção de Petróleo e Gás Natural — Terra (FDP, dados abertos)",
        entries=_fdp_terra_entries,
    ),
}

GROUP_ALIASES_DA: dict[str, str] = {
    # Wave 2
    "precos-combustiveis": "shpc-ca",
    "vendas-abertos": "vdpb-abertos",
    "processamento-abertos": "pp-abertos",
    # Wave 3a
    "producao-estado": "producao-el",
    "participacoes-governamentais": "royalties",
    "importacoes-exportacoes-csv": "ie-abertos",
    "producao-biocombustiveis-csv": "pb-abertos",
    # Wave 3b
    "mov-gas-gasoduto": "movimentacao-gn",
    "capacidade-tancagem": "tancagem",
    "qualidade-combustivel": "pmqc",
    "mov-derivados": "movimentacao-derivados",
    "producao-poco-da": "producao-poco-abertos",
    # Wave 3c
    "fdp-mar": "producao-fdp-mar",
    "fdp-terra": "producao-fdp-terra",
}
