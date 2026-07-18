# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

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
