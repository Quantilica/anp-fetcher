# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Adicionado
- Expansão do catálogo de Dados Abertos com 8 novos grupos (64 novos datasets):
  - `autorizacoes-gn` (Autorizações de Construção e Operação de Gás Natural - CSV/XLSX)
  - `distribuidores` (Distribuidores de Combustíveis Líquidos e contratos homologados)
  - `multas` (Multas Aplicadas com Vencimento a partir de 2016 - MAV)
  - `fiscalizacao-conteudo-local` (Fiscalização de Conteúdo Local em E&P - Exploração e Desenvolvimento)
  - `aditamento-conteudo-local` (Planilha de Aditamento de Conteúdo Local - Resolução ANP 726/2018)
  - `acervo-dados-tecnicos` (BDEP - Acervo de Dados Técnicos, Sísmica, Geoquímica, PROMAR e Poços Públicos)
  - `amostras-rochas-fluidos` (Declarações Anuais de Acervo de Amostras e Valores Praticados pelas Depositárias)
  - `pdi` (Obrigações e Investimentos em Pesquisa, Desenvolvimento e Inovação - P,D&I)

## [1.3.0] - 2026-08-07

### Alterado
- Refatoração arquitetural: Remoção de dependências (`quantilica-cli` e `quantilica-catalog`) e limpeza de imports. Os fetchers agora são pacotes de extração puros, dependendo estritamente do `quantilica-core`.

## [1.1.2] - 2026-07-24

### Corrigido

- `cli.py` não suprimia os loggers verbosos de terceiros (`quantilica.core`,
  `httpx` via `log_step`) fora do modo `--verbose`, conforme
  `docs/docs/normas/cli-fetchers.md` §2.6 — padronizado com os demais
  fetchers do ecossistema.

## [1.1.1] - 2026-07-21

### Corrigido

- Removido o atalho `-v` de `--verbose` em `cli.py` (`sync` e `discover`),
  que violava `docs/docs/normas/cli-fetchers.md` §11.7 ("Nunca use `-v` como
  atalho de `--verbose`").

## [1.1.0] - 2026-07-17

### Adicionado

- Preparação para publicação no PyPI seguindo o padrão do ecossistema Quantilica:
  `py.typed` + classifier `Typing :: Typed`, licença PEP 639 (`license = "MIT"` +
  `license-files`), configuração de `ruff` (`E/F/I/UP/B`) e `pytest`, workflows de
  CI (teste com `uv` + `ruff` + `pytest`) e de publicação via Trusted Publishing (OIDC).
- README com instalação, uso da CLI e integração com `quantilica-cli`.

### Corrigido

- Dependência de `quantilica-core` trocada de `git+https://...` para
  `quantilica-core>=0.3.1` (versão publicada no PyPI). `typer`/`rich` (usados pelo
  `plugin.py`) são fornecidos pelo host `quantilica-cli`, não declarados pelo fetcher —
  a CLI standalone (`cli.py`) usa `argparse` e não precisa deles.
- Comando `sync` quebrava com `AttributeError: 'int' object has no attribute
  'get_time'`: `make_batch_progress`/`make_download_progress` estavam sendo
  chamadas fora do padrão usado pelos demais fetchers (`total` no lugar de
  `console`, retorno desempacotado como tupla). Corrigido para seguir o mesmo
  padrão de `comex-fetcher`/`pdet-fetcher`/`rtn-fetcher`.
