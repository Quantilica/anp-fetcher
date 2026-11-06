"""Aviso de grupo inteiro indisponível (todas as entradas em HTTP 404).

Um 404 isolado é normal (mês ainda não publicado) e o sync o trata como pulado.
Quando **todas** as entradas de um grupo dão 404 a ANP quase certamente mudou o
endereço e o grupo parou de ser coletado sem ninguém notar (foi o que aconteceu
com o ``pmqc``). Este módulo detecta o caso e deixa o aviso visível no log.

O ``sync`` sai com :data:`DEAD_GROUP_EXIT_CODE` (padrão 3) quando há grupo morto,
depois de terminar o trabalho; o ``check`` só registra o aviso e sai com 0, porque
no modo de plano um ``check`` com código diferente de zero faz o cron cair num
``sync`` completo. ``ANP_DEAD_GROUP_EXIT=0`` mantém o aviso e desliga o código.
"""

from __future__ import annotations

import logging
import os
import re
from collections import defaultdict
from collections.abc import Iterable
from typing import Any

logger = logging.getLogger(__name__)

DEAD_GROUP_EXIT_CODE = 3
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


def dead_groups_from_plan(items: Iterable[Any]) -> list[str]:
    """Grupos cujas entradas do plano são todas ``skip-unavailable``/``remote-404``."""
    total: dict[str, int] = defaultdict(int)
    dead: dict[str, int] = defaultdict(int)
    for item in items:
        total[item.dataset] += 1
        if item.action == "skip-unavailable" and item.reason == "remote-404":
            dead[item.dataset] += 1
    return sorted(g for g, n in total.items() if g and dead[g] == n)


def dead_groups_from_errors(
    entries: Iterable[dict[str, Any]], errors: Iterable[tuple[str, str]]
) -> list[str]:
    """Grupos em que todas as entradas tentadas falharam com HTTP 404."""
    group_of = {str(e.get("id")): str(e.get("group")) for e in entries}
    total: dict[str, int] = defaultdict(int)
    for group in group_of.values():
        total[group] += 1
    dead: dict[str, int] = defaultdict(int)
    for eid, message in errors:
        if _HTTP_404.search(message) and eid in group_of:
            dead[group_of[eid]] += 1
    return sorted(g for g, n in total.items() if g and dead[g] == n)


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
