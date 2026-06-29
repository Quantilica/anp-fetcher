"""Download functions for ANP Dados Estatísticos."""

import contextlib
import datetime as dt
from pathlib import Path

from quantilica.core.http import HttpClient, ProgressCallback
from quantilica.core.progress import batch_progress, file_progress

from .catalog import DatasetEntry, list_datasets, resolve_group
from .storage import DataRepository

client = HttpClient(
    timeout=180.0,
    verify=True,
    headers={
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/142.0.0.0 Safari/537.36"
        ),
    },
)


def _safe_head_date(url: str) -> dt.date | None:
    with contextlib.suppress(Exception):
        return client.head_last_modified_date(url)
    return None


def download_file(
    url: str,
    output: Path,
    *,
    progress: ProgressCallback | None = None,
) -> Path:
    """Download a single file, writing atomically with a manifest."""
    dataset_id = output.parent.name
    return client.download_with_manifest(
        url,
        output,
        source_id="anp",
        dataset_id=dataset_id,
        producer="anp-fetcher",
        progress=progress,
    )


def download_entry(
    entry: DatasetEntry,
    repo: DataRepository,
    *,
    dry_run: bool = False,
    show_progress: bool = False,
    progress: ProgressCallback | None = None,
) -> Path:
    """Download one dataset entry and return the destination path."""
    last_modified = _safe_head_date(entry["url"])
    output = repo.path_for_entry(entry, last_modified=last_modified)
    if dry_run:
        return output
    if progress is not None:
        return download_file(entry["url"], output, progress=progress)
    if show_progress:
        with file_progress(output.name) as progress_cb:
            return download_file(entry["url"], output, progress=progress_cb)
    return download_file(entry["url"], output)


def download_group(
    group_id: str,
    output: Path,
    *,
    dry_run: bool = False,
    show_progress: bool = False,
) -> list[Path]:
    """Download all datasets for one group. Returns list of destination paths."""
    canon = resolve_group(group_id)
    if canon is None:
        raise ValueError(f"Unknown group: {group_id!r}")
    entries = list_datasets(canon)
    repo = DataRepository(output)
    paths: list[Path] = []
    with batch_progress("anp-fetcher", total=len(entries)) as batch_pbar:
        for entry in entries:
            path = download_entry(
                entry, repo, dry_run=dry_run, show_progress=show_progress
            )
            paths.append(path)
            batch_pbar.update()
    return paths


def download_all(
    output: Path,
    *,
    groups: list[str] | None = None,
    dry_run: bool = False,
    show_progress: bool = False,
) -> list[Path]:
    """Download all (or selected) groups. Returns list of destination paths."""
    from .catalog import ALL_GROUP_KEYS

    target_groups = groups if groups is not None else ALL_GROUP_KEYS
    resolved: list[str] = []
    for g in target_groups:
        canon = resolve_group(g)
        if canon is None:
            raise ValueError(f"Unknown group: {g!r}")
        resolved.append(canon)

    paths: list[Path] = []
    for group_id in resolved:
        paths.extend(
            download_group(group_id, output, dry_run=dry_run, show_progress=show_progress)
        )
    return paths
