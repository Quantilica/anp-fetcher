import logging
import subprocess
import tempfile
from pathlib import Path

import polars as pl

logger = logging.getLogger(__name__)

NUMERIC_COLUMNS = ["Valor de Venda", "Valor de Compra"]


def _decompress(filepath: Path) -> Path:
    """Decompress a zip or 7z file and return the first extracted file."""
    logger.info("Decompressing %s", filepath)
    tmp_dir = Path(tempfile.mkdtemp(prefix="anp_"))
    command = ["7z", "e", str(filepath), f"-o{tmp_dir}"]
    result = subprocess.run(command, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"7z failed decompressing {filepath}: "
            f"{result.stderr.decode(errors='replace')}"
        )
    extracted = list(tmp_dir.iterdir())
    if not extracted:
        raise RuntimeError(f"7z produced no files from {filepath}")
    return extracted[0]


def _read_and_clean_shpc(filepath: Path) -> pl.DataFrame:
    """Read a SHPC CSV file and apply strict types."""
    # Sniff encoding and separator could be complex, but ANP is usually utf-8 or latin1
    try:
        # First attempt with utf-8
        df = pl.read_csv(
            filepath, separator=";", encoding="utf8", infer_schema_length=0
        )
    except Exception:
        # Fallback to latin-1
        df = pl.read_csv(
            filepath, separator=";", encoding="latin1", infer_schema_length=0
        )

    # Standardize column names if needed, but assuming they match SHPC_COLUMNS
    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            df = df.with_columns(
                pl.col(col).str.replace(",", ".").cast(pl.Float64, strict=False)
            )

    # For all other columns, strip whitespace and cast to Categorical/String
    for col in df.columns:
        if col not in NUMERIC_COLUMNS:
            df = df.with_columns(pl.col(col).str.strip_chars())

    return df


def convert_anp(input_dir: Path, output_dir: Path) -> None:
    """Procura arquivos brutos da ANP e converte para Parquet.

    Args:
        input_dir (Path): The directory containing raw ANP files.
        output_dir (Path): The directory where Parquet files will be saved.
    """
    if not input_dir.exists():
        logger.warning("Input directory %s does not exist.", input_dir)
        return

    shpc_dirs = [
        d for d in input_dir.iterdir() if d.is_dir() and d.name.startswith("shpc-")
    ]

    for shpc_dir in shpc_dirs:
        for file in shpc_dir.glob("*"):
            if file.is_dir():
                continue

            filepath = file

            # Decompress if zip
            if filepath.suffix.lower() == ".zip":
                try:
                    filepath = _decompress(filepath)
                except Exception as e:
                    logger.error("Failed to decompress %s: %s", file, e)
                    continue

            if filepath.suffix.lower() == ".csv":
                logger.info("Converting %s", file)
                try:
                    df = _read_and_clean_shpc(filepath)

                    # Create output path
                    out_path = output_dir / shpc_dir.name / f"{file.stem}.parquet"
                    out_path.parent.mkdir(parents=True, exist_ok=True)

                    df.write_parquet(out_path)
                except Exception as e:
                    logger.error("Failed to convert %s: %s", file, e)
