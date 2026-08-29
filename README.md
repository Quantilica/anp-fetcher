# anp-fetcher: Coletor de dados estatísticos da ANP

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square) ![Python](https://img.shields.io/badge/python-3.12+-blue.svg?style=flat-square)

Utilitário de linha de comando para baixar dados públicos da [ANP](https://www.gov.br/anp/) (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis) — séries estatísticas e datasets de dados abertos. Descobre datasets a partir de um catálogo declarativo e faz o download organizado por grupo, com manifestos de proveniência via `quantilica-core`.

Para a documentação completa, consulte [https://docs.quantilica.com](https://docs.quantilica.com).

## Instalação

```bash
pip install anp-fetcher
```

Com [uv](https://github.com/astral-sh/uv):

```bash
uv add anp-fetcher
```

**Requisitos:** Python 3.12+

## Uso

### Listar os datasets disponíveis

```bash
anp-fetcher list
```

### Sincronizar (baixar) datasets

```bash
# Baixar todos os grupos
anp-fetcher sync

# Baixar grupos específicos (estatísticos: ie, pp, pb, ppg, vdpb)
anp-fetcher sync ie pp -o ./dados/anp

# Listar os arquivos que seriam baixados, sem baixar
anp-fetcher sync --dry-run
```

Grupos de dados abertos incluem `shpc` (Sistema de Levantamento de Preços) e suas
subdivisões (`shpc-glp`, `shpc-gasolina-etanol`, etc.), `vdpb-abertos` e `pp-abertos`,
além dos grupos de E&P: fase de exploração (`blocos-contrato`, `pocos-exploratorios`,
`pads-concluidos`, `pads-andamento`, `declaracoes-comercialidade`, `prorrogacoes-708`,
`prorrogacoes-815`, `prorrogacoes-878`, `processos-sancionadores`), fase de produção
(`producao-mar`, `producao-terra`, `producao-zona`, `plataformas-operacao`,
`campos-producao`, `situacao-pocos`, `sondas-operacao`, `intervencoes-pocos`,
`previsao-pat-pap`, `atividades-investimentos`) e `reservas-nacionais`.

Use `anp-fetcher list` para ver todos os grupos e aliases (ex.: `blocos` → `blocos-contrato`,
`reservas` → `reservas-nacionais`).

### Converter para Parquet

Após o `sync`, os dados brutos podem ser convertidos para Parquet (requer o
extra `[analysis]`):

```bash
# Converter todos os grupos
anp-fetcher convert -i ./dados/anp -o ./dados/anp

# Converter grupos específicos (aceita aliases)
anp-fetcher convert reservas-nacionais shpc -i ./dados/anp -o ./dados/anp

# Pipeline completo: sync + convert dos grupos escolhidos
anp-fetcher pipeline reservas-nacionais -o ./dados/anp
```

A conversão é **idempotente** (pula o que já foi convertido), lê CSV/XLS/XLSX/ZIP,
normaliza dtypes (números com vírgula decimal, strings sem espaços) e injeta a
proveniência do `DownloadManifest` nos metadados do Parquet (`quantilica.*`).
Grupos-chave (SHPC, reservas) têm `DataContract` de validação aplicado.

### Integração com `quantilica-cli`

Se o `quantilica-cli` estiver instalado no mesmo ambiente, o `anp-fetcher` é detectado
automaticamente como plugin:

```bash
quantilica anp list
```

## API Python

```python
from anp_fetcher.catalog import list_datasets

for entry in list_datasets(group="ie"):
    print(entry["id"], entry["url"])
```

## Desenvolvimento

```bash
git clone https://github.com/Quantilica/anp-fetcher.git
cd anp-fetcher
uv sync --group dev
uv run ruff check src/ tests/
uv run pytest
```

## Licença

MIT — veja [LICENSE](LICENSE).
