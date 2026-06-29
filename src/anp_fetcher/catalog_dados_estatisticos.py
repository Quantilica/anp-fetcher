"""ANP Dados Estatísticos catalog.

Covers the five thematic groups published at:
https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos
"""

from ._catalog_base import DatasetEntry, GroupInfo, _annual, _static

_SOURCE = "dados-estatisticos"
_BASE = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de"
_PP_PATH = "arquivos-processamento-de-petroleo-e-producao-de-derivados"
_VDPB_PATH = "arquivos-vendas-de-derivados-de-petroleo-e-biocombustiveis"


def _s(group: str, id_: str, name: str, path: str, ext: str) -> DatasetEntry:
    return _static(group, _SOURCE, id_, name, f"{_BASE}/{path}", ext)


def _a(
    group: str,
    base_id: str,
    name_prefix: str,
    path_template: str,
    years: list[int],
    ext_map: dict[int, str] | str,
) -> list[DatasetEntry]:
    return _annual(group, _SOURCE, base_id, name_prefix,
                   f"{_BASE}/{path_template}", years, ext_map)


# ---------------------------------------------------------------------------
# ie — Importações e Exportações
# ---------------------------------------------------------------------------

_ie_entries: list[DatasetEntry] = [
    _s("ie", "ie-m3", "Importações e Exportações (m³)",
       "ie/importacoes-exportacoes-m3.xlsx", "xlsx"),
    _s("ie", "ie-b", "Importações e Exportações (barris)",
       "ie/importacoes-exportacoes-b.xlsx", "xlsx"),
]

# ---------------------------------------------------------------------------
# pp — Processamento de Petróleo e Produção de Derivados
# ---------------------------------------------------------------------------

_pp_entries: list[DatasetEntry] = [
    _s("pp", "processamento-petroleo-m3", "Volume de petróleo refinado (m³)",
       f"{_PP_PATH}/processamento-petroleo-m3.xls", "xls"),
    _s("pp", "processamento-petroleo-b", "Volume de petróleo refinado (barris)",
       f"{_PP_PATH}/processamento-petroleo-b.xls", "xls"),
    _s("pp", "producao-derivados-m3", "Produção nacional de derivados (m³)",
       f"{_PP_PATH}/producao-derivados-m3.xls", "xls"),
    _s("pp", "producao-derivados-b", "Produção nacional de derivados (barris)",
       f"{_PP_PATH}/producao-derivados-b.xls", "xls"),
]

# ---------------------------------------------------------------------------
# pb — Produção de Biocombustíveis
# ---------------------------------------------------------------------------

_pb_entries: list[DatasetEntry] = [
    _s("pb", "producao-biodiesel-m3", "Produção de biodiesel (m³)",
       "pb/producao-biodiesel-m3.xls", "xls"),
    _s("pb", "producao-biodiesel-b", "Produção de biodiesel (barris)",
       "pb/producao-biodiesel-b.xls", "xls"),
    _s("pb", "producao-etanol-m3", "Produção de etanol (m³)",
       "pb/producao-etanol-m3.xls", "xls"),
    _s("pb", "producao-etanol-b", "Produção de etanol (barris)",
       "pb/producao-etanol-b.xls", "xls"),
]

# ---------------------------------------------------------------------------
# ppg — Produção de Petróleo e Gás Natural
# ---------------------------------------------------------------------------

_ppg_static: list[DatasetEntry] = [
    _s("ppg", "producao-petroleo-m3", "Produção nacional de petróleo e LGN (m³)",
       "ppg/producao-petroleo-m3.xls", "xls"),
    _s("ppg", "producao-petroleo-b", "Produção nacional de petróleo e LGN (barris)",
       "ppg/producao-petroleo-b.xls", "xls"),
    _s("ppg", "producao-gas-natural-m3", "Produção nacional de gás natural (mil m³)",
       "ppg/producao-gas-natural-m3.xls", "xls"),
]

_poco_entries = _a(
    "ppg", "producao-poco", "Produção por poço",
    "ppg/pp/producao-pocos-{year}.{ext}",
    list(range(2005, 2024)), "zip",
)

_campo_ext: dict[int, str] = {y: "xls" for y in range(2009, 2016)}
_campo_ext[2016] = "xlsx"
_campo_entries = _a(
    "ppg", "producao-campo", "Produção por campo",
    "ppg/pc/producao-campo-{year}.{ext}",
    list(range(2009, 2017)), _campo_ext,
)

_ppg_entries: list[DatasetEntry] = _ppg_static + _poco_entries + _campo_entries

# ---------------------------------------------------------------------------
# vdpb — Vendas de Derivados de Petróleo e Biocombustíveis (estatísticos)
# ---------------------------------------------------------------------------

_vdpb_static: list[DatasetEntry] = [
    _s("vdpb", "vendas-combustiveis-m3", "Vendas de derivados combustíveis (m³)",
       "vdpb/vendas-combustiveis-m3.xls", "xls"),
    _s("vdpb", "vendas-combustiveis-b", "Vendas de derivados combustíveis (barris)",
       "vdpb/vendas-combustiveis-b.xls", "xls"),
]

_YEARS_VDPB = list(range(2000, 2025))

_asfalto_ext: dict[int, str] = {y: "xlsx" if y >= 2017 else "xls" for y in _YEARS_VDPB}
_asfalto_entries = _a(
    "vdpb", "vendas-municipais-asfalto", "Vendas municipais - Asfalto",
    f"{_VDPB_PATH}/asfalto/asfalto-municipio-{{year}}.{{ext}}",
    _YEARS_VDPB, _asfalto_ext,
)

_etanol_h_ext: dict[int, str] = {y: "xlsx" if y >= 2017 else "xls" for y in _YEARS_VDPB}
_etanol_h_ext[2000] = "xlsx"
_etanol_h_entries = _a(
    "vdpb", "vendas-municipais-etanol-hidratado", "Vendas municipais - Etanol hidratado",
    f"{_VDPB_PATH}/etanol-hidratado/etanol-hidratado-municipio-{{year}}.{{ext}}",
    _YEARS_VDPB, _etanol_h_ext,
)

_gas_c_ext: dict[int, str] = {y: "xlsx" if y >= 2017 else "xls" for y in _YEARS_VDPB}
_gas_c_ext[2010] = "xlsx"
_gas_c_ext[2000] = "xlsx"
_gas_c_entries = _a(
    "vdpb", "vendas-municipais-gasolina-c", "Vendas municipais - Gasolina C",
    f"{_VDPB_PATH}/gasolina-c/gasolina-c-municipio-{{year}}.{{ext}}",
    _YEARS_VDPB, _gas_c_ext,
)

_gas_av_ext: dict[int, str] = {y: "xlsx" if y >= 2017 else "xls" for y in _YEARS_VDPB}
_gas_av_entries = _a(
    "vdpb", "vendas-municipais-gasolina-aviacao", "Vendas municipais - Gasolina de aviação",
    f"{_VDPB_PATH}/gasolina-de-aviacao/gasolina-aviacao-municipio-{{year}}.{{ext}}",
    _YEARS_VDPB, _gas_av_ext,
)

_vdpb_entries: list[DatasetEntry] = (
    _vdpb_static
    + _asfalto_entries
    + _etanol_h_entries
    + _gas_c_entries
    + _gas_av_entries
)

# ---------------------------------------------------------------------------
# Exported groups
# ---------------------------------------------------------------------------

GROUPS_DE: dict[str, GroupInfo] = {
    "ie": GroupInfo(name="Importações e Exportações", entries=_ie_entries),
    "pp": GroupInfo(
        name="Processamento de Petróleo e Produção de Derivados",
        entries=_pp_entries,
    ),
    "pb": GroupInfo(name="Produção de Biocombustíveis", entries=_pb_entries),
    "ppg": GroupInfo(name="Produção de Petróleo e Gás Natural", entries=_ppg_entries),
    "vdpb": GroupInfo(
        name="Vendas de Derivados de Petróleo e Biocombustíveis",
        entries=_vdpb_entries,
    ),
}

GROUP_ALIASES_DE: dict[str, str] = {
    "importacoes-exportacoes": "ie",
    "processamento-petroleo": "pp",
    "producao-biocombustiveis": "pb",
    "producao-petroleo-gas": "ppg",
    "vendas": "vdpb",
}
