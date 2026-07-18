# anp-fetcher: Coletor de dados estatísticos da ANP

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square) ![Python](https://img.shields.io/badge/python-3.12+-blue.svg?style=flat-square)

Utilitário de linha de comando para baixar dados públicos da [ANP](https://www.gov.br/anp/) (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis) — séries estatísticas e datasets de dados abertos. Descobre datasets a partir de um catálogo declarativo e faz o download organizado por grupo, com manifestos de proveniência via `quantilica-core`.

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
anp-fetcher discover
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
subdivisões (`shpc-glp`, `shpc-gasolina-etanol`, etc.), `vdpb-abertos` e `pp-abertos`.

### Integração com `quantilica-cli`

Se o `quantilica-cli` estiver instalado no mesmo ambiente, o `anp-fetcher` é detectado
automaticamente como plugin:

```bash
quantilica anp discover
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
