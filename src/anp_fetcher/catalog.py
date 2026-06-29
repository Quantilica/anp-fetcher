"""ANP unified dataset catalog.

Aggregates all groups from all catalog modules:
- catalog_dados_estatisticos:   ANP dados-estatísticos (XLS/XLSX) — Fase 1
- catalog_dados_abertos:        ANP dados-abertos (CSV, SHPC, etc.) — Fase 2
- catalog_dados_abertos_3a:     ANP dados-abertos — Onda 3a (15 grupos)

Public API is stable across phases.
"""

from ._catalog_base import DatasetEntry, GroupInfo
from .catalog_dados_abertos import GROUP_ALIASES_DA, GROUPS_DA
from .catalog_dados_abertos_3a import GROUP_ALIASES_DA_3A, GROUPS_DA_3A
from .catalog_dados_estatisticos import GROUP_ALIASES_DE, GROUPS_DE

__all__ = [
    "DatasetEntry",
    "GroupInfo",
    "GROUPS",
    "GROUP_ALIASES",
    "ALL_GROUP_KEYS",
    "SHPC_GROUP_KEYS",
    "resolve_group",
    "list_datasets",
]

GROUPS: dict[str, GroupInfo] = {**GROUPS_DE, **GROUPS_DA, **GROUPS_DA_3A}

GROUP_ALIASES: dict[str, str] = {**GROUP_ALIASES_DE, **GROUP_ALIASES_DA, **GROUP_ALIASES_DA_3A}

ALL_GROUP_KEYS: list[str] = list(GROUPS)

SHPC_GROUP_KEYS: list[str] = [k for k in GROUPS if k.startswith("shpc-")]


def resolve_group(key: str) -> str | None:
    """Resolve a group key or alias to a canonical group id. Returns None if not found."""
    if key in GROUPS:
        return key
    return GROUP_ALIASES.get(key)


def list_datasets(group: str | None = None) -> list[DatasetEntry]:
    """Return all dataset entries, optionally filtered by group."""
    if group is not None:
        canon = resolve_group(group)
        if canon is None:
            raise ValueError(f"Unknown group: {group!r}")
        return list(GROUPS[canon]["entries"])
    return [entry for info in GROUPS.values() for entry in info["entries"]]
