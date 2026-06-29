"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from quantilica.core.cli import (
    get_console,
    make_batch_progress,
    make_download_progress,
    setup_rich_logging,
)
from quantilica.core.http import ProgressCallback
from rich.console import Group
from rich.live import Live
from rich.progress import Progress, TaskID
from rich.table import Table

from .catalog import (
    ALL_GROUP_KEYS,
    GROUP_ALIASES,
    GROUPS,
    SHPC_GROUP_KEYS,
    list_datasets,
    resolve_group,
)
from .download import download_entry
from .storage import DataRepository

app = typer.Typer(help="Dados da ANP (Agência Nacional do Petróleo).")
console = get_console()

_DEFAULT_OUTPUT = Path("/data/anp")

_ALL_KEYS = ALL_GROUP_KEYS + list(GROUP_ALIASES) + ["shpc"]


def _expand_group(key: str) -> list[str]:
    """Expand a group key (or macro-alias 'shpc') to canonical group ids."""
    if key == "shpc":
        return SHPC_GROUP_KEYS
    canon = resolve_group(key)
    if canon is None:
        return []
    return [canon]


def _file_callback(
    file_progress: Progress,
    task_id: TaskID,
    description: str,
) -> ProgressCallback:
    def callback(downloaded: int, total_bytes: int) -> None:
        if downloaded == 0 and total_bytes == 0:
            file_progress.reset(task_id)
            file_progress.update(task_id, description=description, visible=True)
            return
        if total_bytes:
            file_progress.update(task_id, total=total_bytes)
        file_progress.update(task_id, completed=downloaded)

    return callback


@app.command("sync")
def sync(
    groups: Annotated[
        list[str] | None,
        typer.Argument(
            help=(
                "Grupos a baixar. Dados estatísticos: ie, pp, pb, ppg, vdpb. "
                "Dados abertos: shpc (todos os grupos SHPC), shpc-ca, shpc-glp, "
                "shpc-diesel-gnv, shpc-gasolina-etanol, shpc-glp-mensal, shpc-4s, "
                "vdpb-abertos, pp-abertos. Padrão: todos."
            ),
        ),
    ] = None,
    output: Annotated[
        Path, typer.Option("-o", "--output", help="Diretório de saída")
    ] = _DEFAULT_OUTPUT,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Listar arquivos sem baixar")
    ] = False,
    verbose: Annotated[
        bool, typer.Option("--verbose", help="Logs detalhados")
    ] = False,
) -> None:
    """Sincronizar dados da ANP (estatísticos e dados abertos)."""
    setup_rich_logging(verbose, console=console)

    target_groups: list[str] = []
    for g in (groups or ALL_GROUP_KEYS):
        expanded = _expand_group(g)
        if not expanded:
            console.print(f"[red]Grupo desconhecido: {g!r}[/red]")
            console.print(f"Grupos válidos: {', '.join(_ALL_KEYS)}")
            raise typer.Exit(1)
        for canon in expanded:
            if canon not in target_groups:
                target_groups.append(canon)

    entries = [e for g in target_groups for e in list_datasets(g)]
    total = len(entries)

    if dry_run:
        table = Table("Grupo", "ID", "URL", title="Arquivos a baixar (dry-run)")
        for e in entries:
            table.add_row(e["group"], e["id"], e["url"])
        console.print(table)
        console.print(f"\n[bold]{total}[/bold] arquivo(s) listado(s).")
        return

    repo = DataRepository(output)
    batch_prog, overall = make_batch_progress(total)
    file_prog, file_task = make_download_progress()

    downloaded = 0
    errors: list[tuple[str, str]] = []

    try:
        with Live(Group(overall, file_prog), console=console, refresh_per_second=10):
            for entry in entries:
                cb = _file_callback(file_prog, file_task, entry["id"])
                try:
                    download_entry(entry, repo, progress=cb)
                    downloaded += 1
                except Exception as exc:
                    errors.append((entry["id"], str(exc)))
                finally:
                    batch_prog.advance()
            file_prog.update(file_task, visible=False)
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrompido.[/yellow]")
        raise typer.Exit(130)

    console.print(f"\n[green]Concluído:[/green] {downloaded}/{total} arquivo(s) baixado(s).")
    if errors:
        console.print(f"[red]{len(errors)} erro(s):[/red]")
        for eid, emsg in errors:
            console.print(f"  {eid}: {emsg}")


@app.command("discover")
def discover(
    verbose: Annotated[
        bool, typer.Option("--verbose", help="Logs detalhados")
    ] = False,
) -> None:
    """Listar todos os datasets disponíveis no catálogo."""
    setup_rich_logging(verbose, console=console)

    for group_id, group_info in GROUPS.items():
        table = Table(
            "ID", "Partição", "Extensão", "URL",
            title=f"[bold]{group_id}[/bold] — {group_info['name']}",
        )
        for entry in group_info["entries"]:
            if entry["semester"] is not None:
                partition = f"{entry['year']}-S{entry['semester']}"
            elif entry["month"] is not None:
                partition = f"{entry['year']}-{entry['month']:02d}"
            elif entry["year"] is not None:
                partition = str(entry["year"])
            else:
                partition = "—"
            table.add_row(entry["id"], partition, entry["ext"], entry["url"])
        console.print(table)

    total = sum(len(g["entries"]) for g in GROUPS.values())
    console.print(f"\n[bold]{total}[/bold] dataset(s) no catálogo.")
