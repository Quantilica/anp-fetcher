"""ANP Dados Abertos — Onda 3a catalog.

Covers 15 new groups added in the third phase:
producao-el, pb-abertos, ie-abertos, comercializacao-gn, movimentacao-terminais,
armazenagem-terminais, incidentes, rodadas, concessionarios, revendedores,
revendas-glp, registro-lubrificantes, pml, fiscalizacao, royalties.
"""

from collections.abc import Callable

from ._catalog_base import DatasetEntry, GroupInfo, _static

_SOURCE = "dados-abertos"
_BASE = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos"
_ANP = "https://www.gov.br/anp/pt-br"

# ---------------------------------------------------------------------------
# producao-el — Produção de Petróleo e Gás Natural por Estado e Localização
# 7 CSVs estáticos, atualização mensal, cobertura 1997-2026.
# Nota: reinjecao-gn-1000m3.csv tem link quebrado na página — incluído assim mesmo.
# ---------------------------------------------------------------------------

_PPGN_EL = f"{_BASE}/ppgn-el"

_producao_el_entries: list[DatasetEntry] = [
    _static("producao-el", _SOURCE, "pel-petroleo",
            "Produção de petróleo por estado e localização (m³) 1997-2026",
            f"{_PPGN_EL}/producao-petroleo-m3.csv", "csv"),
    _static("producao-el", _SOURCE, "pel-lgn",
            "Produção de LGN por estado e localização (m³) 1997-2026",
            f"{_PPGN_EL}/producao-lgn-m3.csv", "csv"),
    _static("producao-el", _SOURCE, "pel-gas-natural",
            "Produção de gás natural por estado e localização (mil m³) 1997-2026",
            f"{_PPGN_EL}/producao-gas-natural-1000m3.csv", "csv"),
    _static("producao-el", _SOURCE, "pel-reinjecao",
            "Reinjeção de gás natural por estado e localização (mil m³) 2000-2026",
            f"{_PPGN_EL}/reinjecao-gn-1000m3.csv", "csv"),
    _static("producao-el", _SOURCE, "pel-queima-perda",
            "Queima e perda de gás natural por estado e localização (mil m³) 2000-2026",
            f"{_PPGN_EL}/queima-e-perda-gn-1000m3.csv", "csv"),
    _static("producao-el", _SOURCE, "pel-consumo-proprio",
            "Consumo próprio de gás natural por estado e localização (mil m³) 2000-2026",
            f"{_PPGN_EL}/consumo-proprio-gn1000m3.csv", "csv"),
    _static("producao-el", _SOURCE, "pel-gn-disponivel",
            "Gás natural disponível por estado e localização (mil m³) 2000-2026",
            f"{_PPGN_EL}/gn-disponivel-1000m3.csv", "csv"),
]

# ---------------------------------------------------------------------------
# pb-abertos — Produção de Biocombustíveis (dados abertos CSV)
# 3 CSVs estáticos, atualização mensal.
# Complementa o grupo "pb" (dados-estatísticos, XLS).
# ---------------------------------------------------------------------------

_PB_ABERTOS = f"{_BASE}/arquivos-producao-de-biocombustiveis"

_pb_abertos_entries: list[DatasetEntry] = [
    _static("pb-abertos", _SOURCE, "pba-biodiesel-2005-2023",
            "Produção de biodiesel B100 (m³) 2005-2023",
            f"{_PB_ABERTOS}/producao-biodiesel-m3-2005-2023.csv", "csv"),
    _static("pb-abertos", _SOURCE, "pba-biodiesel-2024-2026",
            "Produção de biodiesel B100 (m³) 2024-2026",
            f"{_PB_ABERTOS}/producao-biodiesel-m3-2024-2026.csv", "csv"),
    _static("pb-abertos", _SOURCE, "pba-etanol",
            "Produção de etanol anidro e hidratado (m³) 2012-2026",
            f"{_PB_ABERTOS}/producao-etanol-anidro-hidratado-m3-2012-2026.csv", "csv"),
]

# ---------------------------------------------------------------------------
# ie-abertos — Importações e Exportações (dados abertos CSV)
# 4 CSVs estáticos (um por subpasta/produto), atualização mensal.
# Versão granular do grupo "ie" (dados-estatísticos, XLS).
# ---------------------------------------------------------------------------

_IE_BASE = f"{_BASE}/ie"

_ie_abertos_entries: list[DatasetEntry] = [
    _static("ie-abertos", _SOURCE, "iea-petroleo",
            "Importações e exportações de petróleo (m³) 2000-2025",
            f"{_IE_BASE}/petroleo/importacoes-exportacoes-petroleo-2000-2025.csv", "csv"),
    _static("ie-abertos", _SOURCE, "iea-gas-natural",
            "Importação de gás natural (mil m³) 2000-2025",
            f"{_IE_BASE}/gn/importacao-gas-natural-2000-2025.csv", "csv"),
    _static("ie-abertos", _SOURCE, "iea-derivados",
            "Importações e exportações de derivados de petróleo (m³) 2000-2025",
            f"{_IE_BASE}/derivados/importacoes-exportacoes-derivados-2000-2025.csv", "csv"),
    _static("ie-abertos", _SOURCE, "iea-etanol",
            "Importações e exportações de etanol (m³) 2012-2025",
            f"{_IE_BASE}/etanol/importacoes-exportacoes-etanol-2012-2025.csv", "csv"),
]

# ---------------------------------------------------------------------------
# comercializacao-gn — Comercialização de Gás Natural
# 3 CSVs estáticos, atualização mensal.
# URL base fora do padrão /dados-abertos/arquivos/ — está em /assuntos/.
# ---------------------------------------------------------------------------

_COM_GN = (
    f"{_ANP}/assuntos/movimentacao-estocagem-e-comercializacao-de-gas-natural"
    "/acompanhamento-do-mercado-de-gas-natural/ppg"
)

_comercializacao_gn_entries: list[DatasetEntry] = [
    _static("comercializacao-gn", _SOURCE, "cgn-distribuidoras",
            "Comercialização de gás natural — distribuidoras e consumidores livres",
            f"{_COM_GN}/distribuidoras-consumidores-livres.csv", "csv"),
    _static("comercializacao-gn", _SOURCE, "cgn-produtores",
            "Comercialização de gás natural — vendas entre produtores",
            f"{_COM_GN}/vendas-entre-produtores.csv", "csv"),
    _static("comercializacao-gn", _SOURCE, "cgn-comercializadores",
            "Comercialização de gás natural — vendas aos comercializadores",
            f"{_COM_GN}/vendas-aos-comercializadores.csv", "csv"),
]

# ---------------------------------------------------------------------------
# movimentacao-terminais — Movimentação dos Terminais Aquaviários
# 1 CSV estático, atualização mensal (desde set/2022).
# ---------------------------------------------------------------------------

_MOV_TERM = f"{_BASE}/arquivos-movimentacao-dos-terminais-aquaviarios"

_movimentacao_terminais_entries: list[DatasetEntry] = [
    _static("movimentacao-terminais", _SOURCE, "movterm",
            "Movimentação dos terminais aquaviários de derivados de petróleo",
            f"{_MOV_TERM}/dados-abertos-movimentacao-terminais-aquaviarios.csv", "csv"),
]

# ---------------------------------------------------------------------------
# armazenagem-terminais — Capacidade de Armazenagem de Terminais
# 1 CSV estático, atualização anual.
# ---------------------------------------------------------------------------

_CAT = f"{_BASE}/cat"

_armazenagem_terminais_entries: list[DatasetEntry] = [
    _static("armazenagem-terminais", _SOURCE, "armazterm",
            "Capacidade de armazenagem de terminais de derivados de petróleo",
            f"{_CAT}/capacidade-armazenagem-terminais.csv", "csv"),
]

# ---------------------------------------------------------------------------
# incidentes — Incidentes de Segurança Operacional (E&P)
# 5 CSVs em modelo relacional (tabela fato + 4 dimensões), atualização irregular.
# ---------------------------------------------------------------------------

_ISSM = f"{_BASE}/issm"

_incidentes_entries: list[DatasetEntry] = [
    _static("incidentes", _SOURCE, "issm-incidentes",
            "Incidentes de segurança operacional em E&P — tabela principal",
            f"{_ISSM}/incidentes.csv", "csv"),
    _static("incidentes", _SOURCE, "issm-classificacao",
            "Incidentes de segurança operacional — classificação",
            f"{_ISSM}/incidentes-classificacao.csv", "csv"),
    _static("incidentes", _SOURCE, "issm-feridos",
            "Incidentes de segurança operacional — feridos",
            f"{_ISSM}/incidentes-feridos.csv", "csv"),
    _static("incidentes", _SOURCE, "issm-substancias",
            "Incidentes de segurança operacional — substâncias envolvidas",
            f"{_ISSM}/incidentes-substancias.csv", "csv"),
    _static("incidentes", _SOURCE, "issm-tipo",
            "Incidentes de segurança operacional — tipos de incidente",
            f"{_ISSM}/incidentes-tipo.csv", "csv"),
]

# ---------------------------------------------------------------------------
# rodadas — Rodadas de Licitações de Petróleo e Gás Natural
# 3 CSVs estáticos (9ª–17ª rodadas), raramente atualizados.
# ---------------------------------------------------------------------------

_RLPGN = f"{_BASE}/rlpgn"

_rodadas_entries: list[DatasetEntry] = [
    _static("rodadas", _SOURCE, "rlpgn-blocos",
            "Rodadas de licitações — blocos ofertados (9ª–17ª rodadas)",
            f"{_RLPGN}/blocos-ofertados-rodadas.csv", "csv"),
    _static("rodadas", _SOURCE, "rlpgn-vencedoras",
            "Rodadas de licitações — ofertas vencedoras",
            f"{_RLPGN}/ofertas-vencedoras-rodadas.csv", "csv"),
    _static("rodadas", _SOURCE, "rlpgn-cessao",
            "Rodadas de licitações — processos de cessão de contratos",
            f"{_RLPGN}/processos-cessao-contratos.csv", "csv"),
]

# ---------------------------------------------------------------------------
# concessionarios — Relação de Concessionários
# 2 CSVs estáticos, atualização irregular.
# ---------------------------------------------------------------------------

_RC = f"{_BASE}/rc"

_concessionarios_entries: list[DatasetEntry] = [
    _static("concessionarios", _SOURCE, "rc-relacao",
            "Relação de concessionários — contratos ativos com percentuais por empresa",
            f"{_RC}/relacao-concessionarios.csv", "csv"),
    _static("concessionarios", _SOURCE, "rc-pais-origem",
            "Relação de concessionários — país de origem",
            f"{_RC}/relacao-pais-origem-concessionarios.csv", "csv"),
]

# ---------------------------------------------------------------------------
# revendedores — Cadastro Revendedores Varejistas de Combustíveis Automotivos
# 1 CSV estático, atualização semanal.
# ---------------------------------------------------------------------------

_REVENDEDORES = (
    f"{_BASE}/arquivos-dados-cadastrais-dos-revendedores-varejistas"
    "-de-combustiveis-automotivos"
)

_revendedores_entries: list[DatasetEntry] = [
    _static("revendedores", _SOURCE, "revendedores-varejistas",
            "Cadastro de revendedores varejistas de combustíveis automotivos",
            f"{_REVENDEDORES}/dados-cadastrais-revendedores-varejistas-combustiveis-automoveis.csv",
            "csv"),
]

# ---------------------------------------------------------------------------
# revendas-glp — Cadastro de Revendas de GLP
# 1 CSV estático, atualização mensal.
# ---------------------------------------------------------------------------

_REVENDAS_GLP = (
    f"{_BASE}/arquivos-dados-cadastrais-das-revendas"
    "-de-gas-liquefeito-de-petroleo-glp"
)

_revendas_glp_entries: list[DatasetEntry] = [
    _static("revendas-glp", _SOURCE, "revendas-glp",
            "Cadastro de revendas de GLP (distribuidoras e revendedores)",
            f"{_REVENDAS_GLP}/cadastro-revendas-glp.csv", "csv"),
]

# ---------------------------------------------------------------------------
# registro-lubrificantes — Registro de Óleos e Graxas Lubrificantes
# 1 CSV estático, atualização semanal.
# ---------------------------------------------------------------------------

_REG_LUB = f"{_BASE}/arquivos-registro"

_registro_lubrificantes_entries: list[DatasetEntry] = [
    _static("registro-lubrificantes", _SOURCE, "registro-lubrificantes",
            "Registro de óleos e graxas lubrificantes autorizados pela ANP",
            f"{_REG_LUB}/dados-abertos-registro-produtos.csv", "csv"),
]

# ---------------------------------------------------------------------------
# pml — Programa de Monitoramento dos Lubrificantes
# 1 CSV estático, atualização semestral.
# ---------------------------------------------------------------------------

_PML = f"{_BASE}/arquivos-pml"

_pml_entries: list[DatasetEntry] = [
    _static("pml", _SOURCE, "pml",
            "PML — resultados do monitoramento de qualidade de lubrificantes",
            f"{_PML}/dados-abertos-pml.csv", "csv"),
]

# ---------------------------------------------------------------------------
# fiscalizacao — Ações de Fiscalização do Abastecimento
# 2 XLSXs estáticos, atualização anual.
# URL base fora do padrão — está em /paineis-dinamicos-da-anp/.
# ---------------------------------------------------------------------------

_FISC = (
    f"{_ANP}/centrais-de-conteudo/paineis-dinamicos-da-anp"
    "/arquivos-dados-brutos-do-painel-dinamico-da-fiscalizacao"
    "-do-abastecimento-da-sfi"
)

_fiscalizacao_entries: list[DatasetEntry] = [
    _static("fiscalizacao", _SOURCE, "fisc-1998-2018",
            "Ações de fiscalização do abastecimento — histórico 1998-2018",
            f"{_FISC}/dados-fisc-1998-2018.xlsx", "xlsx"),
    _static("fiscalizacao", _SOURCE, "fisc-2019",
            "Ações de fiscalização do abastecimento — a partir de 2019",
            f"{_FISC}/dados-fisc-a-partir-2019.xlsx", "xlsx"),
]

# ---------------------------------------------------------------------------
# royalties — Participações Governamentais
#
# 79 arquivos em 6 sub-séries. ATENÇÃO: nomes de arquivo são altamente
# irregulares — underscore vs hyphen, singular vs plural, e subfolder
# diferente para o ano 2020 de royalties-uniao.
#
# Sub-séries:
#   royalties-uniao      (2009-2025, 17 arquivos)
#   royalties-estados    (2009-2025, 17 arquivos)
#   royalties-municipios (2009-2025, 17 arquivos)
#   participacao-especial (4 arquivos estáticos)
#   preco-referencia-gn  (2010-2025, 16 arquivos)
#   preco-referencia-petroleo (2018-2025, 8 arquivos)
#
# Nota: preco-minimo-petroleo (2009-2017) não está incluído — nomes
# de arquivo não confirmados na exploração.
# ---------------------------------------------------------------------------

_PG = f"{_BASE}/pg"


def _ru_url(year: int) -> str:
    """royalties-uniao URL — subfolder diferente para 2020."""
    if year == 2020:
        return f"{_PG}/2020/royalties-uniao-2020.csv"
    base = f"{_PG}/royalties-uniao"
    if year <= 2018:
        return f"{base}/royalties_uniao_{year}.csv"
    return f"{base}/royalties-uniao-{year}.csv"


def _re_url(year: int) -> str:
    """royalties-estado(s) URL — plural em 2022-2023."""
    base = f"{_PG}/royalties-estados"
    if year <= 2018:
        return f"{base}/royalties_estado_{year}.csv"
    if year in (2022, 2023):
        return f"{base}/royalties-estados-{year}.csv"
    return f"{base}/royalties-estado-{year}.csv"


def _rm_url(year: int) -> str:
    """royalties-municipio(s) URL — plural em 2022-2023."""
    base = f"{_PG}/royalties-municipios"
    if year <= 2018:
        return f"{base}/royalties_municipio_{year}.csv"
    if year in (2022, 2023):
        return f"{base}/royalties-municipios-{year}.csv"
    return f"{base}/royalties-municipio-{year}.csv"


def _gn_ref_url(year: int) -> str:
    """preco-referencia-gas-natural URL — 3 naming epochs."""
    base = f"{_PG}/preco-referencia-gas-natural"
    if year <= 2019:
        return f"{base}/precorefgn_{year}.csv"
    if year == 2020:
        return f"{base}/precoref-gn-2020.csv"
    return f"{base}/preco-referencia-gn-{year}.csv"


def _petro_ref_url(year: int) -> str:
    """preco-referencia-petroleo URL — 3 naming epochs; 2020 tem sufixo -1."""
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


_PG_YEARS = list(range(2009, 2026))   # 2009-2025
_GN_REF_YEARS = list(range(2010, 2026))  # 2010-2025
_PETRO_REF_YEARS = list(range(2018, 2026))  # 2018-2025

_royalties_entries: list[DatasetEntry] = (
    _royalties_annual("royalties-uniao", "Royalties — União", _PG_YEARS, _ru_url)
    + _royalties_annual("royalties-estado", "Royalties — Estados", _PG_YEARS, _re_url)
    + _royalties_annual("royalties-municipio", "Royalties — Municípios", _PG_YEARS, _rm_url)
    + [
        _static("royalties", _SOURCE, "pe-uniao",
                "Participação especial — acumulado por União",
                f"{_PG}/participacao-especial/pe_uniao.csv", "csv"),
        _static("royalties", _SOURCE, "pe-estado",
                "Participação especial — acumulado por estado",
                f"{_PG}/participacao-especial/pe_estado.csv", "csv"),
        _static("royalties", _SOURCE, "pe-municipio",
                "Participação especial — acumulado por município",
                f"{_PG}/participacao-especial/pe_municipio.csv", "csv"),
        _static("royalties", _SOURCE, "pe-campo",
                "Participação especial — acumulado por campo",
                f"{_PG}/participacao-especial/pe_campo.csv", "csv"),
    ]
    + _royalties_annual("preco-ref-gn", "Preço de referência gás natural", _GN_REF_YEARS, _gn_ref_url)
    + _royalties_annual("preco-ref-petroleo", "Preço de referência petróleo", _PETRO_REF_YEARS, _petro_ref_url)
)

# ---------------------------------------------------------------------------
# Exported groups and aliases
# ---------------------------------------------------------------------------

GROUPS_DA_3A: dict[str, GroupInfo] = {
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
}

GROUP_ALIASES_DA_3A: dict[str, str] = {
    "producao-estado":             "producao-el",
    "participacoes-governamentais": "royalties",
    "importacoes-exportacoes-csv": "ie-abertos",
    "producao-biocombustiveis-csv": "pb-abertos",
}
