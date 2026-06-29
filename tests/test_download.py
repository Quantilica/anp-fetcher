"""Tests for anp_fetcher.download."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from anp_fetcher.catalog import list_datasets
from anp_fetcher.download import download_all, download_entry
from anp_fetcher.storage import DataRepository


def test_download_entry_dry_run(tmp_path):
    """Dry-run must not call download_file and must return a valid path."""
    repo = DataRepository(tmp_path)
    entry = list_datasets("ie")[0]

    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        path = download_entry(entry, repo, dry_run=True)

    assert isinstance(path, Path)
    assert not path.exists()


def test_download_entry_calls_download_with_manifest(tmp_path):
    """Verify download_entry delegates to client.download_with_manifest."""
    repo = DataRepository(tmp_path)
    entry = list_datasets("ie")[0]
    fake_path = tmp_path / "importacoes-exportacoes" / "ie-m3.xlsx"

    with (
        patch("anp_fetcher.download._safe_head_date", return_value=None),
        patch(
            "anp_fetcher.download.client.download_with_manifest",
            return_value=fake_path,
        ) as mock_dl,
    ):
        result = download_entry(entry, repo)

    mock_dl.assert_called_once()
    call_kwargs = mock_dl.call_args
    assert call_kwargs.args[0] == entry["url"]
    assert call_kwargs.kwargs["source_id"] == "anp"
    assert call_kwargs.kwargs["producer"] == "anp-fetcher"


def test_download_all_dry_run_returns_paths(tmp_path):
    """download_all dry-run should return one path per entry without downloading."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["ie"], dry_run=True)

    ie_entries = list_datasets("ie")
    assert len(paths) == len(ie_entries)
    for path in paths:
        assert not path.exists()


def test_download_all_unknown_group_raises(tmp_path):
    with pytest.raises(ValueError, match="Unknown group"):
        download_all(tmp_path, groups=["nonexistent"])


def test_download_all_alias_accepted(tmp_path):
    """Group aliases (e.g., 'importacoes-exportacoes') should work in download_all."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["importacoes-exportacoes"], dry_run=True)

    assert len(paths) == len(list_datasets("ie"))


def test_download_all_shpc_ca_dry_run(tmp_path):
    """shpc-ca dry-run should return 44 paths."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["shpc-ca"], dry_run=True)

    assert len(paths) == 44
    for path in paths:
        assert not path.exists()


def test_download_all_shpc_glp_dry_run(tmp_path):
    """shpc-glp dry-run should return 44 paths."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["shpc-glp"], dry_run=True)

    assert len(paths) == 44


def test_download_all_shpc_monthly_dry_run(tmp_path):
    """Monthly SHPC groups should return 41 paths each."""
    for group_id in ("shpc-diesel-gnv", "shpc-gasolina-etanol", "shpc-glp-mensal"):
        with patch("anp_fetcher.download._safe_head_date", return_value=None):
            paths = download_all(tmp_path, groups=[group_id], dry_run=True)
        assert len(paths) == 41, f"{group_id}: expected 41, got {len(paths)}"


def test_download_all_vdpb_abertos_dry_run(tmp_path):
    """vdpb-abertos dry-run should return 23 paths."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["vdpb-abertos"], dry_run=True)

    assert len(paths) == 23


def test_download_all_pp_abertos_dry_run(tmp_path):
    """pp-abertos dry-run should return 6 paths."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["pp-abertos"], dry_run=True)

    assert len(paths) == 6


def test_download_all_producao_el_dry_run(tmp_path):
    """producao-el dry-run should return 7 paths."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["producao-el"], dry_run=True)

    assert len(paths) == 7


def test_download_all_royalties_dry_run(tmp_path):
    """royalties dry-run should return 79 paths."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths = download_all(tmp_path, groups=["royalties"], dry_run=True)

    assert len(paths) == 79
    for path in paths:
        assert not path.exists()


def test_download_all_3a_static_groups_dry_run(tmp_path):
    """Each Onda 3a static group should return the expected number of paths."""
    expected = {
        "pb-abertos": 3,
        "ie-abertos": 4,
        "comercializacao-gn": 3,
        "movimentacao-terminais": 1,
        "armazenagem-terminais": 1,
        "incidentes": 5,
        "rodadas": 3,
        "concessionarios": 2,
        "revendedores": 1,
        "revendas-glp": 1,
        "registro-lubrificantes": 1,
        "pml": 1,
        "fiscalizacao": 2,
    }
    for group_id, count in expected.items():
        with patch("anp_fetcher.download._safe_head_date", return_value=None):
            paths = download_all(tmp_path, groups=[group_id], dry_run=True)
        assert len(paths) == count, f"{group_id}: expected {count}, got {len(paths)}"


def test_download_all_3a_aliases(tmp_path):
    """Onda 3a aliases should resolve correctly in download_all."""
    with patch("anp_fetcher.download._safe_head_date", return_value=None):
        paths_alias = download_all(tmp_path, groups=["participacoes-governamentais"], dry_run=True)
        paths_canon = download_all(tmp_path, groups=["royalties"], dry_run=True)

    assert len(paths_alias) == len(paths_canon)
