"""ANP Reservas Nacionais de Petróleo e Gás Natural catalog.

Tabelas de dados BAR (Boletim Anual de Reservas) em XLSX, publicadas em
``gov.br/anp/.../dados-estatisticos/arquivos-reservas-nacionais...``.
Apenas 2020–2025 têm tabela tabular (XLSX); anos anteriores são PDF-only.
"""

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


_reservas_entries: list[DatasetEntry] = [
    _reserva_entry(year, f"tabela-dados-bar-{year}.xlsx")
    for year in (2021, 2022, 2023, 2024, 2025)
]
_reservas_entries.append(_reserva_entry(2020, "tabela-de-dados-bar-2020.xlsx"))

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
