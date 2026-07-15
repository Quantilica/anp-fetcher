"""Standalone command-line interface for anp-fetcher."""

import argparse
import sys
from pathlib import Path

from quantilica.core.logging import configure_cli_logging

from . import __version__
from .catalog import (
    ALL_GROUP_KEYS,
    GROUP_ALIASES,
    SHPC_GROUP_KEYS,
    list_datasets,
    resolve_group,
)
from .download import download_all

_DEFAULT_OUTPUT = Path("/data/anp")
_ALL_KEYS = ALL_GROUP_KEYS + list(GROUP_ALIASES) + ["shpc"]


def _expand_groups(keys: list[str]) -> list[str]:
    """Expand keys (including macro-alias 'shpc') to canonical group ids."""
    result: list[str] = []
    for key in keys:
        if key == "shpc":
            for canon in SHPC_GROUP_KEYS:
                if canon not in result:
                    result.append(canon)
        else:
            canon = resolve_group(key)
            if canon and canon not in result:
                result.append(canon)
    return result


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="anp-fetcher",
        description="Download de dados da ANP (estatísticos e dados abertos).",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # sync
    sync_parser = subparsers.add_parser("sync", help="Sincronizar datasets")
    sync_parser.add_argument(
        "groups",
        nargs="*",
        metavar="GRUPO",
        help=(
            "Grupos a baixar. Dados estatísticos: ie, pp, pb, ppg, vdpb. "
            "Dados abertos: shpc (todos os grupos SHPC), shpc-ca, shpc-glp, "
            "shpc-diesel-gnv, shpc-gasolina-etanol, shpc-glp-mensal, shpc-4s, "
            "vdpb-abertos, pp-abertos. Padrão: todos."
        ),
    )
    sync_parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=_DEFAULT_OUTPUT,
        metavar="DIR",
        help="Diretório de saída (padrão: /data/anp)",
    )
    sync_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Listar arquivos sem baixar",
    )
    sync_parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Logs detalhados",
    )

    # discover
    discover_parser = subparsers.add_parser(
        "discover", help="Listar datasets no catálogo"
    )
    discover_parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Logs detalhados",
    )

    return parser


def _handle_sync(args: argparse.Namespace) -> None:
    configure_cli_logging(args.verbose)

    raw_groups: list[str] = args.groups or []
    if raw_groups:
        for g in raw_groups:
            if g != "shpc" and resolve_group(g) is None:
                print(f"Erro: grupo desconhecido: {g!r}", file=sys.stderr)
                print(f"Grupos válidos: {', '.join(_ALL_KEYS)}", file=sys.stderr)
                sys.exit(1)
        groups = _expand_groups(raw_groups)
    else:
        groups = None

    if args.dry_run:
        entries = (
            list_datasets()
            if groups is None
            else [e for g in groups for e in list_datasets(g)]
        )
        for e in entries:
            print(f"{e['group']}\t{e['id']}\t{e['url']}")
        print(f"\n{len(entries)} arquivo(s) listado(s).")
        return

    download_all(args.output, groups=groups, show_progress=True)


def _handle_discover(args: argparse.Namespace) -> None:
    configure_cli_logging(args.verbose)
    from .catalog import GROUPS

    for group_id, group_info in GROUPS.items():
        print(f"\n=== {group_id} — {group_info['name']} ===")
        for entry in group_info["entries"]:
            if entry["semester"] is not None:
                partition = f"{entry['year']}-S{entry['semester']}"
            elif entry["month"] is not None:
                partition = f"{entry['year']}-{entry['month']:02d}"
            elif entry["year"] is not None:
                partition = str(entry["year"])
            else:
                partition = "—"
            print(
                f"  {entry['id']:55s}  {partition:10s}  [{entry['ext']}]  {entry['url']}"
            )
    total = sum(len(g["entries"]) for g in GROUPS.values())
    print(f"\n{total} dataset(s) no catálogo.")


def main(argv: list[str] | None = None) -> None:
    parser = _get_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "sync":
            _handle_sync(args)
        elif args.command == "discover":
            _handle_discover(args)
        else:
            parser.print_help()
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130)
