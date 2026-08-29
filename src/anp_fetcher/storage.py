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
    "ie": "importacoes-exportacoes",
    "pp": "processamento-petroleo",
    "pb": "producao-biocombustiveis",
    "ppg": "producao-petroleo-gas",
    "vdpb": "vendas",
    # dados-abertos — SHPC
    "shpc-ca": "shpc-combustiveis-automotivos",
    "shpc-glp": "shpc-glp",
    "shpc-diesel-gnv": "shpc-diesel-gnv",
    "shpc-gasolina-etanol": "shpc-gasolina-etanol",
    "shpc-glp-mensal": "shpc-glp-mensal",
    "shpc-4s": "shpc-ultimas-4-semanas",
    # dados-abertos — vendas e processamento
    "vdpb-abertos": "vendas-abertos",
    "pp-abertos": "processamento-abertos",
    # dados-abertos — Onda 3a
    "producao-el": "producao-estado-localizacao",
    "pb-abertos": "producao-biocombustiveis-abertos",
    "ie-abertos": "importacoes-exportacoes-abertos",
    "comercializacao-gn": "comercializacao-gas-natural",
    "movimentacao-terminais": "movimentacao-terminais",
    "armazenagem-terminais": "armazenagem-terminais",
    "incidentes": "incidentes-operacionais",
    "rodadas": "rodadas-licitacoes",
    "concessionarios": "concessionarios",
    "revendedores": "revendedores-varejistas",
    "revendas-glp": "revendas-glp",
    "registro-lubrificantes": "registro-lubrificantes",
    "pml": "pml",
    "fiscalizacao": "fiscalizacao-abastecimento",
    "royalties": "participacoes-governamentais",
    # dados-abertos — Onda 3b
    "movimentacao-gn": "movimentacao-gn",
    "tancagem": "tancagem-abastecimento",
    "pmqc": "qualidade-combustiveis-pmqc",
    "movimentacao-derivados": "movimentacao-derivados",
    "producao-poco-abertos": "producao-poco-abertos",
    # dados-abertos — Onda 3c
    "producao-fdp-mar": "producao-fdp-mar",
    "producao-fdp-terra": "producao-fdp-terra",
    # dados-abertos — Expansão
    "autorizacoes-gn": "autorizacoes-gas-natural",
    "distribuidores": "distribuidores-combustiveis",
    "multas": "multas-aplicadas",
    "fiscalizacao-conteudo-local": "fiscalizacao-conteudo-local",
    "aditamento-conteudo-local": "aditamento-conteudo-local",
    "acervo-dados-tecnicos": "acervo-dados-tecnicos",
    "amostras-rochas-fluidos": "amostras-rochas-fluidos",
    "pdi": "pesquisa-desenvolvimento-inovacao",
    # dados-abertos — Fase de Exploração (Onda 4)
    "blocos-contrato": "fase-exploracao-blocos-contrato",
    "declaracoes-comercialidade": "fase-exploracao-declaracoes-comercialidade",
    "pads-concluidos": "fase-exploracao-pads-concluidos",
    "pads-andamento": "fase-exploracao-pads-andamento",
    "pocos-exploratorios": "fase-exploracao-pocos-exploratorios",
    "prorrogacoes-708": "fase-exploracao-prorrogacoes-708",
    "prorrogacoes-815": "fase-exploracao-prorrogacoes-815",
    "prorrogacoes-878": "fase-exploracao-prorrogacoes-878",
    "processos-sancionadores": "fase-exploracao-processos-sancionadores",
    # dados-abertos — Fase de Desenvolvimento e Produção
    "producao-mar": "producao-mar",
    "producao-terra": "producao-terra",
    "producao-zona": "producao-zona",
    "plataformas-operacao": "plataformas-operacao",
    "campos-producao": "campos-producao",
    "situacao-pocos": "situacao-pocos",
    "sondas-operacao": "sondas-operacao",
    "intervencoes-pocos": "intervencoes-pocos",
    "previsao-pat-pap": "previsao-pat-pap",
    "atividades-investimentos": "atividades-investimentos",
    # dados-estatísticos — Reservas
    "reservas-nacionais": "reservas-nacionais",
}


class DataRepository(BaseDataRepository):
    """Manages local storage for anp-fetcher files."""

    def __init__(self, root: Path | str):
        """Initialize the data repository.

        Args:
            root (Path | str): The root directory for storage.
        """
        super().__init__(root)

    def path_for_entry(
        self,
        entry: DatasetEntry,
        *,
        last_modified: dt.date | None = None,
    ) -> Path:
        """Compute the local path for a dataset entry.

        Args:
            entry (DatasetEntry): The dataset entry to process.
            last_modified (dt.date | None, optional): The last modified date of
                the dataset. Defaults to None.

        Returns:
            Path: The computed local path for the dataset.
        """
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
            filename = build_stamped_filename(
                base_id, partition, ext=ext, timestamp=last_modified
            )
        elif month is not None:
            partition = f"{year}-{month:02d}"
            filename = build_stamped_filename(
                base_id, partition, ext=ext, timestamp=last_modified
            )
        else:
            filename = build_stamped_filename(
                base_id, year, ext=ext, timestamp=last_modified
            )

        return self.storage.path_for(f"{group_dir}/{filename}")
