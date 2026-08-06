"""Download functions for ANP Dados Estatísticos."""

import contextlib
import datetime as dt
from pathlib import Path

from quantilica.core.http import HttpClient, ProgressCallback
from quantilica.core.logging import get_logger
from quantilica.core.progress import batch_progress, file_progress

from .catalog import DatasetEntry, list_datasets, resolve_group
from .storage import DataRepository

logger = get_logger(__name__)

# (entry, exception) pairs for datasets that failed to download.
DownloadError = tuple[DatasetEntry, Exception]

client = HttpClient(
    timeout=180.0,
    verify=True,
    attempts=5,
    retry_base_delay=2.0,
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
    urls_to_try = [entry["url"]]
    if "fallback_urls" in entry and entry["fallback_urls"]:
        urls_to_try.extend(entry["fallback_urls"])

    from quantilica.core.http import HttpStatusError

    last_err = None

    for url in urls_to_try:
        try:
            last_modified = _safe_head_date(url)
            output = repo.path_for_entry(entry, last_modified=last_modified)

            # Use original ext for output filename but override
            # extension if url has different one
            if url != entry["url"]:
                # change suffix of output path
                actual_ext = url.split(".")[-1]
                if output.name.endswith(f".{entry['ext']}"):
                    new_name = (
                        output.name[: -(len(entry["ext"]) + 1)] + f".{actual_ext}"
                    )
                    output = output.with_name(new_name)

            if dry_run:
                return output
            if progress is not None:
                return download_file(url, output, progress=progress)
            if show_progress:
                with file_progress(output.name) as progress_cb:
                    return download_file(url, output, progress=progress_cb)
            return download_file(url, output)
        except HttpStatusError as exc:
            if exc.status_code == 404:
                last_err = exc
                continue
            raise

    # If we get here, all URLs returned 404
    # Just raise the last 404 error
    if last_err:
        raise last_err
    from quantilica.core.exceptions import FetchError

    raise FetchError(f"No valid URLs for {entry['id']}")


def download_group(
    group_id: str,
    output: Path,
    *,
    dry_run: bool = False,
    show_progress: bool = False,
    errors: list[DownloadError] | None = None,
    workers: int = 4,
) -> list[Path]:
    """Download all datasets for one group.

    Returns the destination paths of the entries that succeeded (in
    dry-run mode, every entry "succeeds"). A failure downloading one entry
    is logged and does not stop the rest of the group; pass ``errors`` (a
    list) to collect the ``(entry, exception)`` pairs for entries that
    failed.
    """
    import concurrent.futures
    import threading

    canon = resolve_group(group_id)
    if canon is None:
        raise ValueError(f"Unknown group: {group_id!r}")
    entries = list_datasets(canon)
    repo = DataRepository(output)
    paths: list[Path] = []
    lock = threading.Lock()

    def _worker(entry: DatasetEntry) -> Path | None:
        try:
            return download_entry(
                entry, repo, dry_run=dry_run, show_progress=show_progress
            )
        except Exception as exc:
            logger.warning("Failed to download %s: %s", entry["id"], exc)
            if errors is not None:
                with lock:
                    errors.append((entry, exc))
            return None

    with batch_progress("anp-fetcher", total=len(entries)) as batch_pbar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_worker, entry): entry for entry in entries}
            for future in concurrent.futures.as_completed(futures):
                path = future.result()
                if path:
                    with lock:
                        paths.append(path)
                batch_pbar.update()
    return paths


def download_all(
    output: Path,
    *,
    groups: list[str] | None = None,
    dry_run: bool = False,
    show_progress: bool = False,
    errors: list[DownloadError] | None = None,
    workers: int = 4,
) -> list[Path]:
    """Download all (or selected) groups.

    Returns the destination paths of every entry that succeeded across all
    groups. A group whose entries all fail (or that has no entries) does not
    stop the remaining groups; pass ``errors`` (a list) to collect the
    ``(entry, exception)`` pairs for every failed entry, across all groups.
    """
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
            download_group(
                group_id,
                output,
                dry_run=dry_run,
                show_progress=show_progress,
                errors=errors,
                workers=workers,
            )
        )
    return paths
