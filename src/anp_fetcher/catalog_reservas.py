"""ANP Reservas Nacionais de Petróleo e Gás Natural catalog.

Tabelas de dados BAR (Boletim Anual de Reservas) em XLSX, publicadas em
``gov.br/anp/.../dados-estatisticos/arquivos-reservas-nacionais...``.
Apenas 2020 em diante têm tabela tabular (XLSX); anos anteriores são PDF-only.
"""

import datetime as dt

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "dados-estatisticos"
_BASE = (
    "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/"
    "arquivos-reservas-nacionais-de-petroleo-e-gas-natural"
)


def _reserva_entry(year: int, filename: str) -> DatasetEntry:
    return DatasetEntry(
        id=f"reservas-nacionais-{year}",
        base_id="reservas-nacionais",
        name=f"Reservas Nacionais de Petróleo e Gás Natural — {year}",
        url=f"{_BASE}/{filename}",
        ext="xlsx",
        group="reservas-nacionais",
        source=_SOURCE,
        year=year,
        semester=None,
        month=None,
    )


def _reservas_entries_list(today: dt.date | None = None) -> list[DatasetEntry]:
    """Boletim de cada ano de 2021 até o ano anterior ao corrente.

    O BAR de um ano sai no ano seguinte; o ainda não publicado dá 404, tratado
    como pulado no sync.
    """
    today = today or dt.date.today()
    entries = [
        _reserva_entry(year, f"tabela-dados-bar-{year}.xlsx")
        for year in range(2021, max(2021, today.year - 1) + 1)
    ]
    entries.append(_reserva_entry(2020, "tabela-de-dados-bar-2020.xlsx"))
    return entries


_reservas_entries: list[DatasetEntry] = _reservas_entries_list()

GROUPS_RESERVAS: dict[str, GroupInfo] = {
    "reservas-nacionais": {
        "name": "Reservas Nacionais de Petróleo e Gás Natural",
        "entries": _reservas_entries,
    },
}

GROUP_ALIASES_RESERVAS: dict[str, str] = {
    "reservas": "reservas-nacionais",
    "bar": "reservas-nacionais",
}
