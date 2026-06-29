"""File location management for anp-fetcher.

Filenames follow the ecosystem convention:
    {base_id}@{YYYYMMDD}.{ext}                    — static files
    {base_id}_{year}@{YYYYMMDD}.{ext}             — annual series
    {base_id}_{year}-{sem:02d}@{YYYYMMDD}.{ext}  — semestral series
    {base_id}_{year}-{month:02d}@{YYYYMMDD}.{ext} — monthly series
"""

import datetime as dt
from pathlib import Path

from quantilica.core.storage import (
    BaseDataRepository,
    build_stamped_filename,
    stamp_filename,
)

from .catalog import DatasetEntry

_GROUP_DIRS: dict[str, str] = {
    # dados-estatísticos
    "ie":   "importacoes-exportacoes",
    "pp":   "processamento-petroleo",
    "pb":   "producao-biocombustiveis",
    "ppg":  "producao-petroleo-gas",
    "vdpb": "vendas",
    # dados-abertos — SHPC
    "shpc-ca":             "shpc-combustiveis-automotivos",
    "shpc-glp":            "shpc-glp",
    "shpc-diesel-gnv":     "shpc-diesel-gnv",
    "shpc-gasolina-etanol":"shpc-gasolina-etanol",
    "shpc-glp-mensal":     "shpc-glp-mensal",
    "shpc-4s":             "shpc-ultimas-4-semanas",
    # dados-abertos — vendas e processamento
    "vdpb-abertos": "vendas-abertos",
    "pp-abertos":   "processamento-abertos",
    # dados-abertos — Onda 3a
    "producao-el":             "producao-estado-localizacao",
    "pb-abertos":              "producao-biocombustiveis-abertos",
    "ie-abertos":              "importacoes-exportacoes-abertos",
    "comercializacao-gn":      "comercializacao-gas-natural",
    "movimentacao-terminais":  "movimentacao-terminais",
    "armazenagem-terminais":   "armazenagem-terminais",
    "incidentes":              "incidentes-operacionais",
    "rodadas":                 "rodadas-licitacoes",
    "concessionarios":         "concessionarios",
    "revendedores":            "revendedores-varejistas",
    "revendas-glp":            "revendas-glp",
    "registro-lubrificantes":  "registro-lubrificantes",
    "pml":                     "pml",
    "fiscalizacao":            "fiscalizacao-abastecimento",
    "royalties":               "participacoes-governamentais",
}


class DataRepository(BaseDataRepository):
    """Manages local storage for anp-fetcher files."""

    def __init__(self, root: Path | str):
        super().__init__(root)

    def path_for_entry(
        self,
        entry: DatasetEntry,
        *,
        last_modified: dt.date | None = None,
    ) -> Path:
        """Compute the local path for a dataset entry."""
        group_dir = _GROUP_DIRS[entry["group"]]
        ext = entry["ext"]
        base_id = entry["base_id"]
        year = entry["year"]
        semester = entry["semester"]
        month = entry["month"]

        if year is None:
            filename = stamp_filename(base_id, ext, last_modified)
        elif semester is not None:
            partition = f"{year}-{semester:02d}"
            filename = build_stamped_filename(base_id, partition, ext=ext, timestamp=last_modified)
        elif month is not None:
            partition = f"{year}-{month:02d}"
            filename = build_stamped_filename(base_id, partition, ext=ext, timestamp=last_modified)
        else:
            filename = build_stamped_filename(base_id, year, ext=ext, timestamp=last_modified)

        return self.storage.path_for(f"{group_dir}/{filename}")
