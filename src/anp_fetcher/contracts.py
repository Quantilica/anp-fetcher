"""DataContracts para grupos-chave da ANP.

Contratos definidos a partir de amostras reais convertidas (ver
``wrangling.extract_schema`` para regenerar). A validação é best-effort:
no ``wrangling`` o contrato é aplicado apenas quando o grupo tem um
contrato registrado, e falhas são logadas como warning sem abortar a
conversão (schemas da ANP variam entre períodos).
"""

import polars as pl
from quantilica.analytics.schema import DataContract, Field

_SHPC_FIELDS = [
    Field("Regiao - Sigla", pl.Utf8),
    Field("Estado - Sigla", pl.Utf8),
    Field("Municipio", pl.Utf8),
    Field("Revenda", pl.Utf8),
    Field("CNPJ da Revenda", pl.Utf8),
    Field("Nome da Rua", pl.Utf8),
    Field("Numero Rua", pl.Utf8),
    Field("Complemento", pl.Utf8),
    Field("Bairro", pl.Utf8),
    Field("Cep", pl.Utf8),
    Field("Produto", pl.Utf8),
    Field("Data da Coleta", pl.Utf8),
    Field("Valor de Venda", pl.Float64),
    Field("Valor de Compra", pl.Float64),
    Field("Unidade de Medida", pl.Utf8),
    Field("Bandeira", pl.Utf8),
]

_RESERVAS_FIELDS = [
    Field("Ano", pl.Int64),
    Field("Campo/Área de desenvolvimento", pl.Utf8),
    Field("Bacia", pl.Utf8),
    Field("Estado", pl.Utf8),
    Field("VOIP (bbl)", pl.Float64),
    Field("VGIP (m³)", pl.Float64),
    Field("Petróleo Acumulado (bbl)", pl.Float64),
    Field("Gás Natural Acumulado (m³)", pl.Float64),
    Field("Fração Recuperada de Petróleo", pl.Float64),
    Field("Situação", pl.Utf8),
]

CONTRACTS: dict[str, DataContract] = {
    "shpc-ca": DataContract("shpc-ca", _SHPC_FIELDS),
    "shpc-glp": DataContract("shpc-glp", _SHPC_FIELDS),
    "shpc-diesel-gnv": DataContract("shpc-diesel-gnv", _SHPC_FIELDS),
    "shpc-gasolina-etanol": DataContract("shpc-gasolina-etanol", _SHPC_FIELDS),
    "shpc-glp-mensal": DataContract("shpc-glp-mensal", _SHPC_FIELDS),
    "shpc-4s": DataContract("shpc-4s", _SHPC_FIELDS),
    "reservas-nacionais": DataContract("reservas-nacionais", _RESERVAS_FIELDS),
}
