"""A extração de ZIP/7z não deixa pasta no temp do sistema (``quantilica_extract_*``).

O ZIP tem subpasta: a raiz da extração não é o ``parent`` do arquivo devolvido,
e era essa raiz que ficava para trás.
"""

from __future__ import annotations

import tempfile
import warnings
import zipfile
from collections.abc import Iterator
from pathlib import Path

import polars as pl
import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

from anp_fetcher.lake import converter  # noqa: E402
from anp_fetcher.reader import extracted_data, read_file  # noqa: E402
from anp_fetcher.storage import _GROUP_DIRS  # noqa: E402
from anp_fetcher.wrangling import convert_one, spec_for  # noqa: E402

# O aviso do core quando ``decompress_archive`` cria a pasta sozinho.
SEM_AVISO_DO_CORE = r".*decompress_archive\(\)"

CSV = "Municipio;Valor de Venda\nSAO PAULO;5,49\n"


@pytest.fixture
def temp_isolado(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Path]:
    """TMPDIR só deste teste; o ``tempfile`` esquece o cache do temp anterior."""
    temp = tmp_path / "tmpdir"
    temp.mkdir()
    monkeypatch.setenv("TMPDIR", str(temp))
    monkeypatch.delenv("QUANTILICA_LAKE_SCRATCH", raising=False)
    monkeypatch.setattr(tempfile, "tempdir", None)
    assert Path(tempfile.gettempdir()) == temp
    yield temp


@pytest.fixture(autouse=True)
def sem_aviso_do_core() -> Iterator[None]:
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "error", category=DeprecationWarning, message=SEM_AVISO_DO_CORE
        )
        yield


def _zip_com_subpasta(path: Path, member: str = "pasta/interna/dados.csv") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr(member, CSV)
    return path


def _sobras(temp: Path) -> list[str]:
    return sorted(p.name for p in temp.iterdir())


def test_extracted_data_remove_a_raiz_com_subpasta(
    tmp_path: Path, temp_isolado: Path
) -> None:
    raw = _zip_com_subpasta(tmp_path / "raw.zip")
    with extracted_data(raw) as inner:
        assert inner.name == "dados.csv"
        assert inner.parent != temp_isolado  # está numa subpasta da raiz
        assert inner.read_text() == CSV
        assert [p.name for p in temp_isolado.iterdir()]  # existe dentro do with
    assert _sobras(temp_isolado) == []


def test_extracted_data_remove_a_raiz_em_excecao(
    tmp_path: Path, temp_isolado: Path
) -> None:
    raw = _zip_com_subpasta(tmp_path / "raw.zip")
    with pytest.raises(ValueError, match="boom"):
        with extracted_data(raw):
            raise ValueError("boom")
    assert _sobras(temp_isolado) == []


def test_extracted_data_converte_storage_error_em_runtime_error(
    tmp_path: Path, temp_isolado: Path
) -> None:
    ruim = tmp_path / "ruim.zip"
    ruim.write_bytes(b"isto nao e um zip")
    with pytest.raises(RuntimeError, match="falha ao descompactar"):
        with extracted_data(ruim):
            pass
    assert _sobras(temp_isolado) == []


def test_wrangling_convert_one_zip_com_subpasta_nao_deixa_residuo(
    tmp_path: Path, temp_isolado: Path
) -> None:
    raw = _zip_com_subpasta(tmp_path / "in" / "shpc-ca_2025-05@20250601.zip")
    written = convert_one("shpc-ca", raw, tmp_path / "out")
    assert len(written) == 1
    assert pl.read_parquet(written[0])["Valor de Venda"][0] == 5.49
    assert _sobras(temp_isolado) == []


def test_wrangling_zip_ilegivel_nao_deixa_residuo(
    tmp_path: Path, temp_isolado: Path
) -> None:
    raw = tmp_path / "in" / "shpc-ca_2025-05@20250601.zip"
    raw.parent.mkdir()
    with zipfile.ZipFile(raw, "w") as zf:
        zf.writestr("sub/leia-me.txt", "sem dados")  # nenhum csv/xls
    assert convert_one("shpc-ca", raw, tmp_path / "out") == []
    assert _sobras(temp_isolado) == []


def test_read_file_zip_com_subpasta_nao_deixa_residuo(
    tmp_path: Path, temp_isolado: Path
) -> None:
    raw = _zip_com_subpasta(tmp_path / "shpc-ca_2025-05@20250601.zip")
    frame = read_file(raw, spec_for("shpc-ca"))
    assert frame.height == 1
    assert _sobras(temp_isolado) == []


def test_lake_build_zip_com_subpasta_nao_deixa_residuo(
    tmp_path: Path, temp_isolado: Path
) -> None:
    header = "Estado;Bacia;Nome Poço;Período;Óleo (bbl/dia)"
    linhas = "\n".join(f"BA;Recôncavo;P-{i}-BA;2005/01;{i},5" for i in range(3))
    raw = tmp_path / "raw" / _GROUP_DIRS["producao-poco-abertos"]
    raw.mkdir(parents=True)
    with zipfile.ZipFile(raw / "producao-poco-da_2005@20261105.zip", "w") as zf:
        zf.writestr("2005/2005_producao_mar.csv", f"{header}\n{linhas}\n")
        zf.writestr("2005/2005_producao_terra.csv", f"{header}\n{linhas}\n")
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 2
    assert _sobras(temp_isolado) == []
