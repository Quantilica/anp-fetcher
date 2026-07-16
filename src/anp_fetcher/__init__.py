"""anp-fetcher — Download de dados da ANP (estatísticos e dados abertos)."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("anp-fetcher")
except PackageNotFoundError:
    __version__ = "0.0.0"

from .catalog import (
    GROUPS,
    SHPC_GROUP_KEYS,
    DatasetEntry,
    GroupInfo,
    list_datasets,
    resolve_group,
)
from .download import download_all, download_entry, download_file
from .storage import DataRepository

__all__ = [
    "__version__",
    "GROUPS",
    "SHPC_GROUP_KEYS",
    "DatasetEntry",
    "GroupInfo",
    "DataRepository",
    "download_all",
    "download_entry",
    "download_file",
    "list_datasets",
    "resolve_group",
]
