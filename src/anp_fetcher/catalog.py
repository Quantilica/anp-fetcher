"""ANP unified dataset catalog.

Aggregates all groups from all catalog modules:
- catalog_dados_estatisticos:   ANP dados-estatísticos (XLS/XLSX) — Fase 1
- catalog_dados_abertos:        ANP dados-abertos (CSV, SHPC, etc.) — Fase 2
- catalog_fase_exploracao:      Fase de Exploração (9 grupos) — Onda 4
- catalog_fase_producao:        Fase de Desenvolvimento e Produção (10 grupos)
- catalog_reservas:             Reservas nacionais de petróleo e gás (XLSX)

Public API is stable across phases.
"""

from ._catalog_base import DatasetEntry, GroupInfo
from .catalog_dados_abertos import GROUP_ALIASES_DA, GROUPS_DA
from .catalog_dados_estatisticos import GROUP_ALIASES_DE, GROUPS_DE
from .catalog_fase_exploracao import (
    GROUP_ALIASES_FASE_EXPLORACAO,
    GROUPS_FASE_EXPLORACAO,
)
from .catalog_fase_producao import (
    GROUP_ALIASES_FASE_PRODUCAO,
    GROUPS_FASE_PRODUCAO,
)
from .catalog_reservas import GROUP_ALIASES_RESERVAS, GROUPS_RESERVAS

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

GROUPS: dict[str, GroupInfo] = {
    **GROUPS_DE,
    **GROUPS_DA,
    **GROUPS_FASE_EXPLORACAO,
    **GROUPS_FASE_PRODUCAO,
    **GROUPS_RESERVAS,
}

GROUP_ALIASES: dict[str, str] = {
    **GROUP_ALIASES_DE,
    **GROUP_ALIASES_DA,
    **GROUP_ALIASES_FASE_EXPLORACAO,
    **GROUP_ALIASES_FASE_PRODUCAO,
    **GROUP_ALIASES_RESERVAS,
}

ALL_GROUP_KEYS: list[str] = list(GROUPS)

SHPC_GROUP_KEYS: list[str] = [k for k in GROUPS if k.startswith("shpc-")]


def resolve_group(key: str) -> str | None:
    """Resolve a group key or alias to a canonical group id.

    Args:
        key (str): The group key or alias to resolve.

    Returns:
        str | None: The canonical group id, or None if not found.
    """
    if key in GROUPS:
        return key
    return GROUP_ALIASES.get(key)


def list_datasets(group: str | None = None) -> list[DatasetEntry]:
    """Return all dataset entries, optionally filtered by group.

    Args:
        group (str | None): Optional group key to filter by.

    Returns:
        list[DatasetEntry]: A list of dataset entries.

    Raises:
        ValueError: If an unknown group is provided.
    """
    if group is not None:
        canon = resolve_group(group)
        if canon is None:
            raise ValueError(f"Unknown group: {group!r}")
        return list(GROUPS[canon]["entries"])
    return [entry for info in GROUPS.values() for entry in info["entries"]]
