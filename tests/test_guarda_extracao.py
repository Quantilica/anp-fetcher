"""A guarda de sessão (``conftest.py``) confere as sobras ``quantilica_extract_*``.

Este teste de propósito não isola o ``TMPDIR`` (como faz
``test_extracao_sem_residuo.py``): usa o da sessão, e a guarda falha a suíte ao fim
se a conversão do ZIP com subpasta deixar a raiz da extração para trás.
"""

from __future__ import annotations

import tempfile
import zipfile
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

from anp_fetcher.wrangling import convert_one  # noqa: E402

CSV = "Municipio;Valor de Venda\nSAO PAULO;5,49\n"


def test_convert_one_zip_com_subpasta_no_temp_da_sessao(
    tmp_path: Path, guarda_extracao_sem_residuo: Path
) -> None:
    assert Path(tempfile.gettempdir()) == guarda_extracao_sem_residuo
    raw = tmp_path / "in" / "shpc-ca_2025-05@20250601.zip"
    raw.parent.mkdir()
    with zipfile.ZipFile(raw, "w") as zf:
        zf.writestr("pasta/interna/dados.csv", CSV)
    assert len(convert_one("shpc-ca", raw, tmp_path / "out")) == 1
