"""Shared types and helper constructors for ANP dataset catalogs."""

import datetime as dt
from typing import NotRequired, TypedDict


class DatasetEntry(TypedDict):
    """Represents a single ANP dataset entry."""

    id: str
    base_id: str
    name: str
    url: str
    ext: str
    group: str
    source: str  # "dados-estatisticos" | "dados-abertos"
    year: int | None
    semester: int | None  # 1 or 2 — for semestral series
    month: int | None  # 1-12 — for monthly series
    fallback_urls: NotRequired[list[str]]


class GroupInfo(TypedDict):
    """Contains metadata and entries for a dataset group."""

    name: str
    entries: list[DatasetEntry]


def _static(
    group: str,
    source: str,
    id_: str,
    name: str,
    url: str,
    ext: str,
) -> DatasetEntry:
    return DatasetEntry(
        id=id_,
        base_id=id_,
        name=name,
        url=url,
        ext=ext,
        group=group,
        source=source,
        year=None,
        semester=None,
        month=None,
    )


def _annual(
    group: str,
    source: str,
    base_id: str,
    name_prefix: str,
    url_template: str,
    years: list[int],
    ext_map: dict[int, str] | str,
) -> list[DatasetEntry]:
    """Build year-partitioned entries from a URL template.

    The template accepts ``{year}`` and ``{ext}`` placeholders.
    """
    entries: list[DatasetEntry] = []
    for year in years:
        ext = ext_map[year] if isinstance(ext_map, dict) else ext_map
        entries.append(
            DatasetEntry(
                id=f"{base_id}-{year}",
                base_id=base_id,
                name=f"{name_prefix} {year}",
                url=url_template.format(year=year, ext=ext),
                ext=ext,
                group=group,
                source=source,
                year=year,
                semester=None,
                month=None,
            )
        )
    return entries


def _last_published_month(today: dt.date, year: int, *, lag_months: int) -> int:
    """Último mês (1-12) de ``year`` que já deveria estar publicado em ``today``.

    Devolve 12 para anos anteriores ao corrente e 0 para anos posteriores. No ano
    corrente, é o mês de ``today`` menos ``lag_months`` (mínimo 0).
    """
    if year < today.year:
        return 12
    if year > today.year:
        return 0
    return max(0, today.month - lag_months)


def _quarters_ended(today: dt.date, year: int) -> int:
    """Trimestres (0-4) de ``year`` que já terminaram em ``today``."""
    if year < today.year:
        return 4
    if year > today.year:
        return 0
    return (today.month - 1) // 3
