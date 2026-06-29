"""Shared types and helper constructors for ANP dataset catalogs."""

from typing import TypedDict


class DatasetEntry(TypedDict):
    id: str
    base_id: str
    name: str
    url: str
    ext: str
    group: str
    source: str          # "dados-estatisticos" | "dados-abertos"
    year: int | None
    semester: int | None  # 1 or 2 — for semestral series
    month: int | None     # 1-12 — for monthly series


class GroupInfo(TypedDict):
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
    """Build year-partitioned entries from a URL template with {year} and {ext} placeholders."""
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
