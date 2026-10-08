# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Alterado
- `cli.py` protege o import do plugin; sem o host a CLI standalone sai com
  código 1 e orienta `quantilica install <fonte>`.
- `reader.decompress` agora delega a descompressão de arquivos brutos para `quantilica.core.files.decompress_archive`, eliminando lógica local duplicada.

## [1.4.1] - 2026-10-02

### Alterado

- **Onda 3A (padronização/deduplicação):** `reader.normalize_dtypes` delega a
  conversão de números brasileiros a
  `quantilica.analytics.reader.normalize_brazilian_numbers` (eliminada a
  reimplantação local de vírgula decimal/sentinela).
- **Onda 3A:** `reader.write_parquet` delega ao
  `quantilica.analytics.writer.to_parquet` canônico — escrita atômica
  (write-temp-rename) e, com manifest do download reconstruído do sidecar do
  arquivo bruto, proveniência `quantilica.*` injetada no Parquet + sidecar
  `.manifest.json` escrito ao lado do destino.
- **Onda 3A:** `plugin.py` usa o resolver canônico `make_resolve_groups`
  (`quantilica.cli.sdk`, já instanciado como resolutor de grupos por grupos de
  dados); removido o loop duplicado de resolução de grupos.
- Extra `[analysis]`: pin elevado para `quantilica-analytics>=0.3.0`
  (`normalize_brazilian_numbers` + `to_parquet` + `manifest_to_metadata`).

## [1.4.0] - 2026-08-29

### Adicionado
- Camada de extração e tratamento de dados (padrão `pdet-fetcher`): `reader.py`
  (leitura tipada de CSV/XLS/XLSX/ZIP, normalização de dtypes, Parquet com
  proveniência do manifest) e `wrangling.py` (`convert_group` idempotente por
  grupo + `extract_schema`). Comando `convert` agora aceita `[GROUPS]...` e o
  `pipeline` repassa a seleção ao passo de conversão. Extra `[analysis]` ganhou
  `fastexcel` (leitura XLS/XLSX). Grupos-chave (SHPC, reservas) validados por
  `DataContract`.
- 20 novos grupos de dados de E&P e reservas, ampliando o catálogo de 43 para
  63 grupos (~1.1k para ~1.7k datasets):
  - **Fase de Exploração** (9 grupos, mensal desde 02/2023):
    `blocos-contrato`, `declaracoes-comercialidade`, `pads-concluidos`,
    `pads-andamento`, `pocos-exploratorios`, `prorrogacoes-708`,
    `prorrogacoes-815`, `prorrogacoes-878`, `processos-sancionadores` —
    mapeamento literal extraído do HTML do portal (nomenclatura irregular).
  - **Fase de Desenvolvimento e Produção** (10 grupos): `producao-mar`,
    `producao-terra`, `producao-zona`, `plataformas-operacao`,
    `campos-producao`, `situacao-pocos`, `sondas-operacao`,
    `intervencoes-pocos`, `previsao-pat-pap`, `atividades-investimentos`.
  - **Reservas** (1 grupo): `reservas-nacionais` (XLSX 2020–2025).
- Expansão do catálogo de Dados Abertos com 8 grupos (64 novos datasets):
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
