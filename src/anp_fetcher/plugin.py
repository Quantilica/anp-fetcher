"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Annotated, Any

import typer
from quantilica.cli.sdk import FetcherApp

from .catalog import GROUP_ALIASES, GROUPS, list_datasets
from .storage import DataRepository


def path_builder(
    output_dir: Path, entry: dict[str, Any], last_modified: dt.date | None
) -> Path:
    return DataRepository(output_dir).path_for_entry(entry, last_modified=last_modified)


fetcher = FetcherApp(
    name="anp-fetcher",
    help="Dados da ANP (Agência Nacional do Petróleo).",
    groups_dict=GROUPS,
    aliases_dict=GROUP_ALIASES,
    list_datasets=list_datasets,
    path_builder=path_builder,
)

app = fetcher.app


@app.command("convert")
def cmd_convert(
    input: Annotated[
        Path,
        typer.Option("-i", "--input", help="Diretório de origem com arquivos brutos"),
    ] = Path("/data/anp"),
    output: Annotated[
        Path,
        typer.Option("-o", "--output", help="Diretório de destino para Parquet"),
    ] = Path("/data/anp"),
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Converter arquivos brutos da ANP para Parquet."""
    from quantilica.cli.ui import setup_rich_logging

    setup_rich_logging(
        verbose,
        console=fetcher.app.console if hasattr(fetcher.app, "console") else None,
    )

    try:
        from .reader import convert_anp
    except ImportError:
        from quantilica.cli.ui import get_console

        get_console().print(
            "[red]Erro:[/red] convert requer extras de análise: "
            "pip install anp-fetcher[analysis]"
        )
        raise typer.Exit(1) from None

    convert_anp(input, output)

    from quantilica.cli.ui import get_console

    get_console().print("[green]✓[/green] Conversão concluída.")


@app.command("pipeline")
def cmd_pipeline(
    ctx: typer.Context,
    groups: Annotated[
        list[str] | None,
        typer.Argument(
            help="Grupos a baixar. Use 'list' para ver disponíveis. Omitir para todos."
        ),
    ] = None,
    output: Annotated[
        Path | None, typer.Option("-o", "--output", help="Diretório de saída")
    ] = None,
    parquet_dir: Annotated[
        Path | None,
        typer.Option(
            "--parquet-dir",
            help="Diretório para os Parquet (padrão: igual a --output)",
        ),
    ] = None,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Listar arquivos sem baixar")
    ] = False,
    workers: Annotated[int, typer.Option("--workers", help="Downloads paralelos")] = 4,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Pipeline completo: sync seguido de convert."""
    from quantilica.cli.ui import get_console, setup_rich_logging
    from rich.rule import Rule

    console = get_console()
    setup_rich_logging(verbose, console=console)

    parquet_out = parquet_dir or output or Path("/data/anp")

    console.print(Rule("[bold]Passo 1/2: Download[/bold]"))
    sync_cmd = next(c.callback for c in app.registered_commands if c.name == "sync")
    ctx.invoke(
        sync_cmd,
        groups=groups,
        output=output,
        dry_run=dry_run,
        workers=workers,
        verbose=verbose,
    )

    if dry_run:
        return

    console.print(Rule("[bold]Passo 2/2: Conversão[/bold]"))

    try:
        from .reader import convert_anp
    except ImportError:
        console.print(
            "[red]Erro:[/red] pipeline (conversão) requer extras de análise: "
            "pip install anp-fetcher[analysis]"
        )
        raise typer.Exit(1) from None

    convert_anp(output or Path("/data/anp"), parquet_out)
    console.print(f"[green]✓[/green] Parquet salvo em [dim]{parquet_out}[/dim]")
