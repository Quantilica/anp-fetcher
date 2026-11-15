"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
import functools
import json
import logging
from pathlib import Path
from typing import Any

import typer
from quantilica.cli.sdk import CheckPlan, FetcherApp, make_resolve_groups
from quantilica.cli.ui import get_console
from quantilica.core.registry import FetcherInfo
from quantilica.core.sync import FreshnessPolicy

from . import alerts, discover
from .catalog import GROUP_ALIASES, GROUPS, list_datasets, resolve_group
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


logger = logging.getLogger(__name__)
console = get_console()


def _out(text: str) -> None:
    """Imprime texto literal no console Rich compartilhado (sem markup/quebra)."""
    console.print(text, markup=False, highlight=False, emoji=False, soft_wrap=True)


def list_datasets_descoberto(group: str | None = None) -> list[dict[str, Any]]:
    """Entradas do catálogo; nos grupos mensais do SHPC, com os links da página da ANP.

    2023 a 2025 ficam como no catálogo estático. De 2026 em diante os nomes dos
    arquivos saem do padrão sem aviso; a página é consultada uma vez por processo e, se
    falhar, vale a URL presumida do catálogo (com aviso no log). O comando ``list`` não
    consulta a página.

    Args:
        group (str | None): Id ou alias do grupo; ``None`` lista tudo, sem descoberta.

    Returns:
        list[dict[str, Any]]: Entradas do grupo.
    """
    entries = list_datasets(group)
    canon = resolve_group(group) if group is not None else None
    if canon is None:
        return entries  # type: ignore[return-value]
    return discover.entries_for_group(canon, entries)  # type: ignore[return-value]


_DEFAULT_OUTPUT = Path("/data/anp")

# Exit do ``sync`` do host quando parte dos arquivos baixou e parte falhou.
_SYNC_PARTIAL = 3


class AnpFetcherApp(FetcherApp):
    """``FetcherApp`` que avisa quando um grupo inteiro responde HTTP 404."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._dead_groups: set[str] = set()
        super().__init__(*args, **kwargs)
        self._wrap_sync()
        self._wrap_list()

    def download_datasets(self, entries, output_dir, workers=4, *, force=False):
        """Baixa e guarda os grupos em que toda entrada deu HTTP 404."""
        result = super().download_datasets(
            entries, output_dir, workers=workers, force=force
        )
        self._dead_groups.update(alerts.dead_groups_from_errors(entries, result[2]))
        return result

    def check_datasets(self, entries, output_dir, workers=4):
        """Verifica o frescor e avisa dos grupos mortos (exit code inalterado)."""
        plan = super().check_datasets(entries, output_dir, workers=workers)
        alerts.report(alerts.dead_groups_from_plan(plan.items))
        return plan

    def _wrap_list(self) -> None:
        """``list`` só mostra o catálogo: não consulta a página do SHPC."""
        for command in self.app.registered_commands:
            if command.name == "list" and command.callback is not None:
                command.callback = self._without_discovery(command.callback)

    @staticmethod
    def _without_discovery(original: Any) -> Any:
        @functools.wraps(original)
        def listing(*args: Any, **kwargs: Any) -> None:
            with discover.discovery_disabled():
                original(*args, **kwargs)

        return listing

    def _wrap_sync(self) -> None:
        """``sync`` sai != 0 com grupo morto, preservando o código do ``sync``."""
        for command in self.app.registered_commands:
            if command.name == "sync" and command.callback is not None:
                command.callback = self._sync_with_alert(command.callback)

    def _sync_with_alert(self, original: Any) -> Any:
        @functools.wraps(original)
        def sync(*args: Any, **kwargs: Any) -> None:
            self._dead_groups.clear()
            plan_path = kwargs.get("from_plan")
            if plan_path is not None:
                try:
                    plan = CheckPlan.from_json(
                        Path(plan_path).read_text(encoding="utf-8")
                    )
                except (OSError, ValueError):
                    pass  # o sync original reporta o plano inválido
                else:
                    self._dead_groups.update(alerts.dead_groups_from_plan(plan.items))
            original_exit: typer.Exit | None = None
            try:
                original(*args, **kwargs)
            except typer.Exit as exc:
                # Erro de arquivo (3 parcial, 1 nada baixou) ou outro código: o
                # aviso de grupo morto sai de qualquer jeito, e o código original
                # é preservado conforme a precedência abaixo.
                original_exit = exc
            finally:
                dead = alerts.report(self._dead_groups)
            code = alerts.exit_code()
            original_code = original_exit.exit_code if original_exit else 0
            # Precedência: 1 (nada baixou) e outros códigos (sinais etc.) do sync >
            # 4 (grupo morto) > 3 (download parcial) > 0.
            if original_exit is not None and original_code not in (0, _SYNC_PARTIAL):
                if dead:
                    logger.error(
                        "[Alerta] grupo(s) inteiro(s) em 404: %s (sync saiu com %d)",
                        ", ".join(dead),
                        original_code,
                    )
                raise original_exit
            if dead and code:
                logger.error(
                    "[Alerta] grupo(s) inteiro(s) em 404: %s (exit %d)",
                    ", ".join(dead),
                    code,
                )
                raise typer.Exit(code)
            if original_exit is not None and original_code:
                raise original_exit

        return sync


fetcher = AnpFetcherApp(
    default_output=_DEFAULT_OUTPUT,
    name="anp-fetcher",
    help="Dados da ANP (Agência Nacional do Petróleo).",
    info=FetcherInfo(
        id="anp",
        nome="ANP - Dados Estatísticos e Dados Abertos",
        orgao="Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)",
        licenca=(
            "Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) "
            "e Decreto 8.777/2016"
        ),
        homepage="https://www.gov.br/anp/",
        cadencia="monthly",
        dominio="energia",
    ),
    groups_dict=GROUPS,
    aliases_dict=GROUP_ALIASES,
    list_datasets=list_datasets_descoberto,
    path_builder=path_builder,
    freshness_policy=FreshnessPolicy.REMOTE_ONLY,
)


def convert(
    input_dir: Path,
    lake_dir: Path,
    *,
    dataset: list[str] | None = None,
    force: bool = False,
) -> Any:
    """Converte arquivos brutos da ANP para o lake Hive (Parquet)."""
    try:
        from anp_fetcher import lake
    except ImportError as exc:
        raise ImportError(
            "Conversão para o lake requer o extra 'analysis'. "
            "Instale com: quantilica install anp --extra analysis"
        ) from exc

    return lake.converter.convert(input_dir, lake_dir, datasets=dataset, force=force)


def discover_cmd(
    as_json: bool = typer.Option(False, "--json", help="Saída em JSON"),
    fail_on_change: bool = typer.Option(
        False, "--fail-on-change", help="Sai com código 1 se houver novidade ou atraso"
    ),
) -> None:
    """Compara a página do SHPC mensal com o catálogo (meses novos e atraso da ANP)."""
    try:
        report = discover.discover()
    except Exception as exc:
        _out(f"Não consegui ler a página do SHPC: {exc}")
        raise typer.Exit(2) from None
    if as_json:
        _out(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        _out(f"{report.known} link(s) mensais do SHPC na página.")
        for item in report.new_months:
            _out(
                f"NOVO     {item['group']} {item['year']}-{item['month']:02d}: "
                f"{item['url']}"
            )
        for url in report.unclassified:
            _out(f"NAO RECONHECIDO {url}")
        for item in report.late:
            _out(
                f"ATRASO   {item['group']} {item['year']}-{item['month']:02d} "
                "ainda não está na página"
            )
        if report.url_differs:
            _out(
                f"{len(report.url_differs)} arquivo(s) com nome fora do padrão "
                "presumido pelo catálogo (o sync usa o nome da página; detalhes em "
                "--json)."
            )
        if not report.has_changes:
            _out("Sem novidades em relação ao catálogo.")
    if fail_on_change and report.has_changes:
        raise typer.Exit(1)


fetcher.attach_command(discover_cmd, name="discover")
fetcher.command_convert(convert)
fetcher.command_pipeline(convert)

app = fetcher.app
