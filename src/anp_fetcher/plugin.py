"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import datetime as dt
import functools
import logging
from pathlib import Path
from typing import Any

import typer
from quantilica.cli.sdk import CheckPlan, FetcherApp, make_resolve_groups
from quantilica.core.registry import FetcherInfo
from quantilica.core.sync import FreshnessPolicy

from . import alerts
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


logger = logging.getLogger(__name__)

_DEFAULT_OUTPUT = Path("/data/anp")


class AnpFetcherApp(FetcherApp):
    """``FetcherApp`` que avisa quando um grupo inteiro responde HTTP 404."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._dead_groups: set[str] = set()
        super().__init__(*args, **kwargs)
        self._wrap_sync()

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
                # é preservado (o grupo morto define o código se o sync saiu 0 ou 1).
                original_exit = exc
            finally:
                dead = alerts.report(self._dead_groups)
            code = alerts.exit_code()
            original_code = original_exit.exit_code if original_exit else 0
            # 1 = nada baixou: com grupo morto é o caso do contrato do ANP (os 404
            # viram erros de arquivo), então vale o código do grupo morto. Qualquer
            # outro código do sync (3 parcial, 130...) é preservado.
            if (
                original_exit is not None
                and original_code
                and not (original_code == 1 and dead and code)
            ):
                if dead:
                    logger.error(
                        "[Alerta] grupo(s) inteiro(s) em 404: %s (exit %d)",
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

        return sync


fetcher = AnpFetcherApp(
    default_output=_DEFAULT_OUTPUT,
    name="anp-fetcher",
    help="Dados da ANP (Agência Nacional do Petróleo).",
    info=FetcherInfo(
        id="anp",
        nome="ANP - Dados Estatísticos e Dados Abertos",
        orgao="Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)",
        homepage="https://www.gov.br/anp/",
        cadencia="monthly",
        dominio="energia",
    ),
    groups_dict=GROUPS,
    aliases_dict=GROUP_ALIASES,
    list_datasets=list_datasets,
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


fetcher.command_convert(convert)
fetcher.command_pipeline(convert)

app = fetcher.app
