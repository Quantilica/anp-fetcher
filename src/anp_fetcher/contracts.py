"""DataContracts para grupos-chave da ANP.

Contratos definidos a partir de amostras reais convertidas (ver
``wrangling.extract_schema`` para regenerar). A validação é best-effort:
no ``wrangling`` o contrato é aplicado apenas quando o grupo tem um
contrato registrado, e falhas são logadas como warning sem abortar a
conversão (schemas da ANP variam entre períodos).
"""

try:
    import polars as pl
    from quantilica.analytics.schema import DataContract, Field
except ImportError as exc:
    raise ImportError(
        "anp_fetcher.contracts requer o extra 'analysis': "
        "uv add 'anp-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

# Versão 2: `Data da Coleta` passou de texto a `Date`; a versão nova força o
# lake a reconverter os arquivos já convertidos com a versão 1.
_SHPC_VERSION = 2

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
    Field("Data da Coleta", pl.Date),
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
    **{
        group: DataContract(group, _SHPC_FIELDS, version=_SHPC_VERSION)
        for group in (
            "shpc-ca",
            "shpc-glp",
            "shpc-diesel-gnv",
            "shpc-gasolina-etanol",
            "shpc-glp-mensal",
            "shpc-4s",
        )
    },
    "reservas-nacionais": DataContract("reservas-nacionais", _RESERVAS_FIELDS),
}
