"""ANP Fase de Desenvolvimento e Produção catalog.

Dados (CSV) da fase de produção: produção de petróleo e gás (mar, terra e
por zona), campos em produção, poços, sondas, intervenções, previsão de
atividades/investimentos (PAT/PAP) e atividades realizadas.

Publicados em ``gov.br/anp/.../arquivos-fase-de-desenvolvimento-e-producao``.
A nomenclatura muda por era (ex.: produção em terra) — o catálogo usa
listas literais verificadas no HTML do portal.
"""

from ._catalog_base import DatasetEntry, GroupInfo, _annual, _static

_SOURCE = "dados-abertos"
_BASE = (
    "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/"
    "arquivos/arquivos-fase-de-desenvolvimento-e-producao"
)
_PROD = f"{_BASE}/arquivos-producao-de-petroleo-e-gas-natural-nacional"


def _csv(
    group: str,
    id_: str,
    name: str,
    url: str,
) -> DatasetEntry:
    return _static(group, _SOURCE, id_, name, url, "csv")


# ---------------------------------------------------------------------------
# Produção em mar — anual (2019–2026) + faixas históricas (1941–2018)
# ---------------------------------------------------------------------------
_PM = f"{_PROD}/pm"

_producao_mar_entries: list[DatasetEntry] = [
    _csv(
        "producao-mar",
        f"producao-mar-{year}",
        f"Produção em Mar — {year}",
        f"{_PM}/producao-mar-{year}.csv",
    )
    for year in (2019, 2020, 2021, 2022, 2023, 2025, 2026)
]
_producao_mar_entries.append(
    _csv(
        "producao-mar",
        "producao-mar-2024",
        "Produção em Mar — 2024",
        f"{_PM}/producao_por_poco_2024.csv",
    )
)
for y1, y2 in (
    (2016, 2018),
    (2013, 2015),
    (2010, 2012),
    (2005, 2009),
    (2001, 2004),
    (1998, 2000),
    (1994, 1997),
    (1989, 1993),
    (1980, 1988),
    (1941, 1979),
):
    _producao_mar_entries.append(
        _csv(
            "producao-mar",
            f"producao-mar-{y1}-{y2}",
            f"Produção em Mar — {y1} a {y2}",
            f"{_PM}/producao-mar-{y1}-{y2}.csv",
        )
    )


# ---------------------------------------------------------------------------
# Produção em terra — nomenclatura muda por era
# ---------------------------------------------------------------------------
_PT = f"{_PROD}/pt"


def _terra_entry(year: int, quarter: int | None, filename: str) -> DatasetEntry:
    part = f"-{quarter:02d}" if quarter is not None else ""
    return DatasetEntry(
        id=f"producao-terra-{year}{part}",
        base_id=f"producao-terra{part}",
        name=f"Produção em Terra — {year}"
        + (f" (trimestre {quarter})" if quarter is not None else ""),
        url=f"{_PT}/{year}/{filename}",
        ext="csv",
        group="producao-terra",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


def _terra_entries() -> list[DatasetEntry]:
    entries: list[DatasetEntry] = []
    # 2025/2026: producao_por_poco_terra_{YYYY}_{N}_trim.csv (2026: 1º-2º trim.)
    for quarter in range(1, 5):
        entries.append(
            _terra_entry(
                2025, quarter, f"producao_por_poco_terra_2025_{quarter}_trim.csv"
            )
        )
    for quarter in (1, 2):
        entries.append(
            _terra_entry(
                2026, quarter, f"producao_por_poco_terra_2026_{quarter}_trim.csv"
            )
        )
    # 2024: Q4 producao_por_poco_terra_trim_4.csv; Q1–Q3
    # producao-por-poco-terra-trim-{N}.csv
    entries.append(_terra_entry(2024, 4, "producao_por_poco_terra_trim_4.csv"))
    for quarter in (1, 2, 3):
        entries.append(
            _terra_entry(2024, quarter, f"producao-por-poco-terra-trim-{quarter}.csv")
        )
    # 2023: producao-terra-{N}-trim.csv
    for quarter in range(1, 5):
        entries.append(
            _terra_entry(2023, quarter, f"producao-terra-{quarter}-trim.csv")
        )
    # 2022: Q1/Q2 producao-terra-2022-{N}-trim.csv; Q3/Q4 producao-terra-{N}-trim.csv
    for quarter in (1, 2):
        entries.append(
            _terra_entry(2022, quarter, f"producao-terra-2022-{quarter}-trim.csv")
        )
    for quarter in (3, 4):
        entries.append(
            _terra_entry(2022, quarter, f"producao-terra-{quarter}-trim.csv")
        )
    # 2021: producao-terra-2021-{N}-trim.csv (Q2 com sufixo estranho)
    entries.append(_terra_entry(2021, 1, "producao-terra-2021-1-trim.csv"))
    entries.append(_terra_entry(2021, 2, "producao-terra-2021-2-trim-ago21.csv"))
    for quarter in (3, 4):
        entries.append(
            _terra_entry(2021, quarter, f"producao-terra-2021-{quarter}-trim.csv")
        )
    # 2016–2020: producao-terra-{year}-{N}trim.csv (2019 Q1/Q3 com anomalias)
    for year in (2016, 2017, 2018, 2020):
        for quarter in range(1, 5):
            entries.append(
                _terra_entry(year, quarter, f"producao-terra-{year}-{quarter}trim.csv")
            )
    entries.append(_terra_entry(2019, 1, "producaoterra20191trim.csv"))
    entries.append(_terra_entry(2019, 2, "producao-terra-2019-2trim.csv"))
    entries.append(_terra_entry(2019, 3, "producao-terra-2019-3trim.csv"))
    entries.append(_terra_entry(2019, 4, "producao-terra-2019-4trim.csv"))
    # 2000–2015: semestral producao-terra-{year}-{N}sem.csv
    for year in range(2000, 2016):
        for sem in (1, 2):
            entries.append(
                DatasetEntry(
                    id=f"producao-terra-{year}-s{sem}",
                    base_id=f"producao-terra-s{sem}",
                    name=f"Produção em Terra — {year} (semestre {sem})",
                    url=f"{_PT}/{year}/producao-terra-{year}-{sem}sem.csv",
                    ext="csv",
                    group="producao-terra",
                    source=_SOURCE,
                    year=year,
                    semester=sem,
                    month=None,
                )
            )
    # 1983–1988: anual sob pt/1988-1983/
    for year in range(1983, 1989):
        entries.append(
            DatasetEntry(
                id=f"producao-terra-{year}",
                base_id="producao-terra",
                name=f"Produção em Terra — {year}",
                url=f"{_PT}/1988-1983/producao-terra-{year}.csv",
                ext="csv",
                group="producao-terra",
                source=_SOURCE,
                year=year,
                semester=None,
                month=None,
            )
        )
    # 1941–1982: faixas sob pt/1982-1941/
    for y1, y2 in (
        (1981, 1982),
        (1978, 1980),
        (1975, 1977),
        (1970, 1974),
        (1967, 1970),
        (1941, 1966),
    ):
        entries.append(
            _csv(
                "producao-terra",
                f"producao-terra-{y1}-{y2}",
                f"Produção em Terra — {y1} a {y2}",
                f"{_PT}/1982-1941/producao-terra-{y1}-{y2}.csv",
            )
        )
    return entries


# ---------------------------------------------------------------------------
# Produção por zona — mensal 10/2014 → hoje
# ---------------------------------------------------------------------------
_PZ = f"{_BASE}/producao-por-zona"

_PZ_OVERRIDES: dict[tuple[int, int], str] = {
    (2026, 3): "Produo_Zona_032026.csv",  # typo: sem separador e sem 'o'
    (2022, 2): "producao_zona_03-2022.csv",  # ANP publica março sob rótulo fev
    (2023, 4): "producao_zona_03-2023.csv",  # idem (abril rotulado com março)
}


def _producao_zona_entries() -> list[DatasetEntry]:
    entries: list[DatasetEntry] = []
    for year in range(2014, 2027):
        if year == 2014:
            months = range(10, 13)  # out/2014
        elif year == 2026:
            months = range(1, 7)  # até jun/2026 (scraping 2026-08-29)
        else:
            months = range(1, 13)
        for month in months:
            filename = _PZ_OVERRIDES.get(
                (year, month), f"producao_zona_{month:02d}-{year}.csv"
            )
            entries.append(
                DatasetEntry(
                    id=f"producao-zona-{year}-{month:02d}",
                    base_id="producao-zona",
                    name=f"Produção por Zona — {year}-{month:02d}",
                    url=f"{_PZ}/{filename}",
                    ext="csv",
                    group="producao-zona",
                    source=_SOURCE,
                    year=year,
                    semester=None,
                    month=month,
                )
            )
    return entries


# ---------------------------------------------------------------------------
# Snapshots e séries auxiliares
# ---------------------------------------------------------------------------
_plataformas_entries = [
    _csv(
        "plataformas-operacao",
        "plataformas-operacao",
        "Lista de Plataformas em Operação",
        f"{_BASE}/lpo/dados-abertos-plataformas-operacao.csv",
    )
]

_campos_entries = [
    _csv(
        "campos-producao",
        "campos-producao",
        "Campos em Desenvolvimento e Produção",
        f"{_BASE}/informacoes-sobre-campos/extracao-campo.csv",
    ),
    _csv(
        "campos-producao",
        "campos-producao-devolvidos",
        "Campos Devolvidos",
        f"{_BASE}/informacoes-sobre-campos/extracao-campo-devolvido.csv",
    ),
    _csv(
        "campos-producao",
        "campos-producao-concessionarios",
        "Concessionários dos Campos",
        f"{_BASE}/informacoes-sobre-campos/extracao-campo-concessionarios.csv",
    ),
    _csv(
        "campos-producao",
        "campos-producao-vertices",
        "Vértices dos Campos",
        f"{_BASE}/informacoes-sobre-campos/extracao-vertices.csv",
    ),
]

_situacao_pocos_entries = [
    _csv(
        "situacao-pocos",
        "situacao-pocos",
        "Situação de Poços (1939–2026)",
        f"{_BASE}/informacoes-sobre-pocos/situacao-pocos-1939-2026.csv",
    )
]

_sondas_entries = _annual(
    "sondas-operacao",
    _SOURCE,
    "sondas-operacao",
    "Sondas em Operação",
    f"{_BASE}/informacoes-sobre-pocos/sondas_em_operacao_por_periodo_{{year}}.csv",
    list(range(2013, 2026)),
    "csv",
)

_intervencoes_entries = [
    _csv(
        "intervencoes-pocos",
        f"intervencoes-pocos-{y1}-{y2}",
        f"Intervenções em Poços — {y1} a {y2}",
        f"{_BASE}/informacoes-sobre-pocos/intervencao_em_pocos_{y1}-{y2}.csv",
    )
    for y1, y2 in (
        (2013, 2014),
        (2015, 2016),
        (2017, 2018),
        (2019, 2020),
        (2021, 2022),
        (2023, 2024),
        (2025, 2026),
    )
]

_previsao_entries = [
    _csv(
        "previsao-pat-pap",
        "previsao-pat-pap-atividade-bacia",
        "Previsão de Atividade por Bacia (PAT/PAP)",
        f"{_BASE}/arquivos-previsao/previsao-atividade-bacia.csv",
    ),
    _csv(
        "previsao-pat-pap",
        "previsao-pat-pap-investimento-bacia",
        "Previsão de Investimento por Bacia (PAT/PAP)",
        f"{_BASE}/arquivos-previsao/investimento-bacia.csv",
    ),
    _csv(
        "previsao-pat-pap",
        "previsao-pat-pap-investimento-atividade",
        "Previsão de Investimento por Tipo de Atividade (PAT/PAP)",
        f"{_BASE}/arquivos-previsao/investimento-atividade.csv",
    ),
    _csv(
        "previsao-pat-pap",
        "previsao-pat-pap-producao",
        "Previsão de Produção (PAT/PAP)",
        f"{_BASE}/arquivos-previsao/previsao-producao.csv",
    ),
]

_atividades_entries = [
    _csv(
        "atividades-investimentos",
        "atividades-investimentos-atividade",
        "Atividades Realizadas",
        f"{_BASE}/atividades-e-investimentos-realizados/atividade-realizada.csv",
    ),
    _csv(
        "atividades-investimentos",
        "atividades-investimentos-investimento",
        "Investimentos Realizados",
        f"{_BASE}/atividades-e-investimentos-realizados/investimento-realizado.csv",
    ),
]

GROUPS_FASE_PRODUCAO: dict[str, GroupInfo] = {
    "producao-mar": {
        "name": "Produção de Petróleo e Gás em Mar",
        "entries": _producao_mar_entries,
    },
    "producao-terra": {
        "name": "Produção de Petróleo e Gás em Terra",
        "entries": _terra_entries(),
    },
    "producao-zona": {
        "name": "Produção de Petróleo e Gás por Zona",
        "entries": _producao_zona_entries(),
    },
    "plataformas-operacao": {
        "name": "Lista de Plataformas em Operação",
        "entries": _plataformas_entries,
    },
    "campos-producao": {
        "name": "Campos em Desenvolvimento e Produção",
        "entries": _campos_entries,
    },
    "situacao-pocos": {
        "name": "Situação de Poços",
        "entries": _situacao_pocos_entries,
    },
    "sondas-operacao": {
        "name": "Sondas em Operação",
        "entries": _sondas_entries,
    },
    "intervencoes-pocos": {
        "name": "Intervenções em Poços",
        "entries": _intervencoes_entries,
    },
    "previsao-pat-pap": {
        "name": "Previsão de Atividade, Investimento e Produção (PAT/PAP)",
        "entries": _previsao_entries,
    },
    "atividades-investimentos": {
        "name": "Atividades e Investimentos Realizados",
        "entries": _atividades_entries,
    },
}

GROUP_ALIASES_FASE_PRODUCAO: dict[str, str] = {
    "mar": "producao-mar",
    "terra": "producao-terra",
    "zona": "producao-zona",
    "plataformas": "plataformas-operacao",
    "campos": "campos-producao",
    "situacao": "situacao-pocos",
    "sondas": "sondas-operacao",
    "intervencoes": "intervencoes-pocos",
    "previsao": "previsao-pat-pap",
    "atividades": "atividades-investimentos",
}
