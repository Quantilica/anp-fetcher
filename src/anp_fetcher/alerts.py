"""Aviso de grupo inteiro indisponível (todas as entradas em HTTP 404).

Um 404 isolado é normal (mês ainda não publicado) e o sync o trata como pulado.
Quando **todas** as entradas de um grupo dão 404 a ANP quase certamente mudou o
endereço e o grupo parou de ser coletado sem ninguém notar (foi o que aconteceu
com o ``pmqc``). Este módulo detecta o caso e deixa o aviso visível no log.

O ``sync`` sai com :data:`DEAD_GROUP_EXIT_CODE` (padrão 4) quando há grupo morto,
depois de terminar o trabalho; o ``check`` só registra o aviso e sai com 0, porque
no modo de plano um ``check`` com código diferente de zero faz o cron cair num
``sync`` completo. ``ANP_DEAD_GROUP_EXIT=0`` mantém o aviso e desliga o código.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import re
from collections import defaultdict
from collections.abc import Iterable
from typing import Any

logger = logging.getLogger(__name__)

# 4 e não 3: o 3 é o "download parcial" do ``sync`` do host (quantilica-cli), que o
# cron trata como alerta; o grupo morto é falha. Precedência no ``sync``:
# 1 (nada baixou) > 4 (grupo morto) > 3 (parcial) > 0.
DEAD_GROUP_EXIT_CODE = 4
_ENV_EXIT = "ANP_DEAD_GROUP_EXIT"
_HTTP_404 = re.compile(r"\bHTTP 404\b")


def exit_code() -> int:
    """Código de saída do ``sync`` com grupo morto (``0`` desliga)."""
    raw = os.environ.get(_ENV_EXIT)
    if raw is None or not raw.strip():
        return DEAD_GROUP_EXIT_CODE
    try:
        return max(0, int(raw))
    except ValueError:
        return DEAD_GROUP_EXIT_CODE


def _settled(year: Any, today: dt.date) -> bool:
    """Se a entrada não é do ano corrente (estática ou de ano já encerrado).

    Um grupo que só tem entradas do ano corrente e todas em 404 é, em geral, o
    início do ano (o primeiro mês ainda não saiu) e não mudança de endereço.
    """
    return not isinstance(year, int) or year < today.year


def _dead(pairs: Iterable[tuple[str, Any, bool]], today: dt.date) -> list[str]:
    total: dict[str, int] = defaultdict(int)
    dead: dict[str, int] = defaultdict(int)
    settled_dead: set[str] = set()
    for group, year, is_404 in pairs:
        total[group] += 1
        if is_404:
            dead[group] += 1
            if _settled(year, today):
                settled_dead.add(group)
    return sorted(
        g for g, n in total.items() if g and dead[g] == n and g in settled_dead
    )


def dead_groups_from_plan(
    items: Iterable[Any], today: dt.date | None = None
) -> list[str]:
    """Grupos cujas entradas do plano são todas ``skip-unavailable``/``remote-404``.

    Só conta se o grupo tem ao menos uma entrada estática ou de ano encerrado.
    """
    today = today or dt.date.today()
    return _dead(
        (
            (
                item.dataset,
                (item.entry or {}).get("year"),
                item.action == "skip-unavailable" and item.reason == "remote-404",
            )
            for item in items
        ),
        today,
    )


def dead_groups_from_errors(
    entries: Iterable[dict[str, Any]],
    errors: Iterable[tuple[str, str]],
    today: dt.date | None = None,
) -> list[str]:
    """Grupos em que todas as entradas tentadas falharam com HTTP 404."""
    today = today or dt.date.today()
    failed = {eid for eid, message in errors if _HTTP_404.search(message)}
    return _dead(
        (
            (str(e.get("group")), e.get("year"), str(e.get("id")) in failed)
            for e in entries
        ),
        today,
    )


def report(groups: Iterable[str]) -> list[str]:
    """Registra o aviso de cada grupo morto e devolve a lista ordenada."""
    dead = sorted(set(groups))
    for group in dead:
        logger.warning(
            "[Alerta] grupo '%s' inteiro em HTTP 404: a ANP provavelmente "
            "mudou o endereço; o grupo não está sendo coletado.",
            group,
        )
    return dead
