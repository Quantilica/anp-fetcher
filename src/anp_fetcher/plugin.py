"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

import typer
from quantilica.cli.sdk import FetcherApp, make_resolve_groups

from .catalog import GROUP_ALIASES, GROUPS, list_datasets
from .storage import DataRepository

# Resolver canônico (elimina a duplicação de _resolve_groups):
resolve_groups = make_resolve_groups(
    GROUPS, {alias: [canon] for alias, canon in GROUP_ALIASES.items()}
)


def _resolve_groups(groups: list[str] | None) -> list[str]:
    """Resolve nomes de grupo/aliases para ids canônicos; None → todos.

    Delega ao ``make_resolve_groups`` canônico do ``quantilica.cli.sdk``.

    Args:
        groups (list[str] | None): Nomes ou aliases de grupo informados na CLI.

    Returns:
        list[str]: Ids canônicos dos grupos.

    Raises:
        typer.BadParameter: Se um grupo não for reconhecido.
    """
    try:
        return resolve_groups(groups)
    except ValueError as exc:
        raise typer.BadParameter(str(exc)) from None


def path_builder(
    output_dir: Path, entry: dict[str, Any], last_modified: dt.date | None
) -> Path:
    """Build the local file path for a dataset entry.

    NÃO usa o ``default_path_builder`` do SDK: o layout canônico dele usa
    ``entry["group"]`` como bucket e ``entry["id"]`` como slug, enquanto o
    layout ANP usa ``_GROUP_DIRS[group]`` + ``base_id`` (id varia por ano).
    O ``wrangling.py`` lê/escreve no mesmo layout — trocar o builder
    incompatibilizaria os dados existentes em disco.

    Args:
        output_dir (Path): The base output directory.
        entry (dict[str, Any]): The dataset entry dictionary.
        last_modified (dt.date | None): The last modified date of the remote file.

    Returns:
        Path: The constructed local file path.
    """
    return DataRepository(output_dir).path_for_entry(entry, last_modified=last_modified)


fetcher = FetcherApp(
    name="anp-fetcher",
    help="Dados da ANP (Agência Nacional do Petróleo).",
    groups_dict=GROUPS,
    aliases_dict=GROUP_ALIASES,
    list_datasets=list_datasets,
    path_builder=path_builder,
)


def convert(
    input_dir: Path,
    lake_dir: Path,
    *,
    dataset: list[str] | None = None,
    force: bool = False,
) -> Any:
    """Converte arquivos brutos da ANP para o lake Hive (Parquet)."""
    from anp_fetcher import lake

    return lake.converter.convert(input_dir, lake_dir, datasets=dataset, force=force)


fetcher.command_convert(convert)
fetcher.command_pipeline(convert)

app = fetcher.app
