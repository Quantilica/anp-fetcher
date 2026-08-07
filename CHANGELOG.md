# Changelog

## [1.3.0] - 2026-08-07
### Alterado
- Refatoração arquitetural: Remoção de dependências (`quantilica-cli` e `quantilica-catalog`) e limpeza de imports. Os fetchers agora são pacotes de extração puros, dependendo estritamente do `quantilica-core`.

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

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
