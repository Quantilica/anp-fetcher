"""Standalone command-line interface for anp-fetcher."""

import sys

from .plugin import app


def main(argv: list[str] | None = None) -> None:
    """Entry point for the standalone CLI.

    Args:
        argv (list[str] | None): Optional list of command-line arguments.
    """
    if argv is not None:
        sys.argv = [sys.argv[0]] + argv
    try:
        app()
    except KeyboardInterrupt:
        sys.exit(130)
