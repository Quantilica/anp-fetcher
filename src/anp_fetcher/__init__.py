"""anp-fetcher — Download de dados da ANP (estatísticos e dados abertos)."""

__version__ = "1.0.0"

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
