# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Alterado
- Os testes exigem `quantilica-cli>=0.19.0`, a versão em que o `sync` sai com código diferente de zero quando algum arquivo falha; o aviso de grupo removido depende desse comportamento do host.

## [2.6.0] - 2026-11-11

### Adicionado
- O fetcher declara os fatos da fonte (`FetcherInfo`: id canônico, apelidos, órgão, licença, página e cadência) para o registro de fetchers da Quantilica.

### Alterado
- Requer `quantilica-core>=0.19.0` (e `quantilica-cli>=0.17.0` como host).

### Corrigido
- O aviso de grupo inteiro em HTTP 404 continua saindo quando o `sync` do host termina com erro de arquivo. **Mudança de contrato:** o código de saída do `sync` com grupo morto passa de 3 para **4** (`ANP_DEAD_GROUP_EXIT` continua valendo; `0` deixa só o aviso), porque o `quantilica-cli` passa a usar o 3 para "download parcial" (parte dos arquivos baixou e parte falhou). Precedência: 1 (nada baixou) > 4 (grupo morto) > 3 (parcial) > 0. Instale este fetcher antes ou junto do `quantilica-cli` 0.19.0: o cli novo com este fetcher antigo perde o alerta de grupo morto quando há erro de arquivo.

## [2.5.0] - 2026-11-06

### Adicionado

- `sync` avisa e sai com código 3 (a partir da próxima versão, 4) quando todas as entradas de um grupo respondem
  HTTP 404 (a ANP provavelmente mudou o endereço e o grupo parou de ser coletado
  sem ninguém notar). Vale para o sync completo e para `sync --from-plan`. O
  `check` registra o aviso mas mantém o código 0, para não derrubar o modo de
  plano. `ANP_DEAD_GROUP_EXIT=0` deixa só o aviso, sem o código. Grupo que só
  tem entradas do ano corrente não alerta (o primeiro mês do ano ainda não saiu).
- `reader.read_file` lê ZIP com vários CSV (um por mês), empilhando-os em ordem
  de nome; os JSON gêmeos do ZIP são ignorados.

### Corrigido

- `pmqc`: a ANP mudou o endereço e todos os arquivos antigos davam 404. O catálogo
  passa a usar os ZIP atuais: um por ano de 2016 a 2025 (`pmqc_AAAA.zip`, com os
  CSV e JSON de cada mês) e um por mês em 2026 (`pmqc_2026_MM.zip`). Os ids
  (`pmqc-csv-AAAA-MM`) e o prefixo `pmqc-csv` dos arquivos do mês seguem os mesmos;
  os ZIP anuais entram como `pmqc-csv-AAAA`. O JSON deixa de ser baixado à parte
  (vem dentro do ZIP).
- `anp convert`: o ZIP anual do `pmqc` vira os meses do dataset `pmqc` (partições
  `ano=/mes=` iguais às dos mensais, um Parquet por CSV do ZIP). Mês que já existe
  como arquivo mensal avulso fica com o avulso, sem duplicar linhas.
- Listas fixas no catálogo agora acompanham a data: `pmqc` (meses do ano
  corrente, com defasagem de um mês), `producao-terra` (trimestres encerrados do
  ano corrente) e `reservas-nacionais` (um boletim por ano até o anterior ao
  corrente). O que a ANP ainda não publicou continua sendo 404 pulado.
- Mais listas fixas passam a seguir a data, sem mudar ids nem caminhos:
  SHPC mensal (diesel-GNV, gasolina-etanol e GLP, até o mês anterior),
  `producao-zona` (até dois meses atrás), `producao-mar` (um arquivo por ano até o
  corrente), `sondas-operacao`, `intervencoes-pocos` (novo biênio a cada dois
  anos) e `situacao-pocos`, cujo arquivo traz o ano no nome
  (`situacao-pocos-1939-AAAA.csv`; os dois anos anteriores ficam como alternativa).
- `tancagem`: acrescenta 2026-09 (`maio-a-setembro.csv`, que a ANP publicou num
  arquivo só para maio a setembro).

## [2.4.1] - 2026-11-05

### Corrigido

- Dados abertos: URLs renomeadas pela ANP. `vdpb-a-segmento` passa a
  `vendas-combustiveis-segmento-m3.csv` (sem sufixo de anos) e
  `pp-a-outros-produtores` a `producao-derivados-outros-produtores-m3-2001-2026.csv`;
  ambas davam 404.

## [2.4.0] - 2026-11-05

### Corrigido

- `anp convert` sem o extra `analysis` agora explica como instalá-lo
  (`quantilica install anp --extra analysis`) em vez de um `ImportError` cru.
- `reader.normalize_dtypes`: valor não vazio que não converte para número ou
  data agora levanta `ValueError` com a coluna e exemplos; antes virava nulo
  sem aviso. Valor vazio continua nulo.
- `reader.read_csv`: arquivo separado por vírgula num grupo de `;` (ex.:
  `vendas-biodiesel-b100-m3.csv`) era lido como uma coluna só; o separador
  agora é detectado pelo cabeçalho.
- `reader.read_file`: lê o `.zip` com um arquivo de dados (SHPC semestral de
  2022 em diante); antes só o ZIP com nome `.csv`, `.xls` ou `.xlsx` era aberto e
  o `.zip` falhava com "Formato não suportado".
- Catálogo SHPC mensal: acrescenta abril a setembro de 2026 com os nomes que a
  ANP publicou (abril sem extensão; junho, agosto e setembro com `2026-MM` no
  nome), conferidos na página da série histórica em 26/10/2026. O catálogo é
  fixo e para de acompanhar a fonte a cada mês novo; descobrir os links na
  própria página evitaria isso.

### Alterado

- Saída padrão do plugin fixa em `/data/anp`.
- SHPC: `Data da Coleta` passa a `Date` (formato `dd/mm/aaaa`), na
  especificação e no `DataContract`, que sobe para a versão 2. Com isso o lake
  reconverte os arquivos SHPC já convertidos; sem a versão nova eles seriam
  pulados e o dataset ficaria com a data ora texto, ora `Date`.
- `vdpb-abertos`, `ie-abertos`, `pp-abertos` e `pb-abertos`: colunas de valor
  (`VENDAS`, `PRODUÇÃO`, `PROCESSADO`, `IMPORTADO / EXPORTADO`,
  `DISPÊNDIO / RECEITA`, `P13`, `OUTROS` e afins) convertidas para número;
  antes ficavam como texto com vírgula decimal.
  Esses grupos não têm contrato: reconverta-os uma vez com `--force` para
  que os arquivos antigos do lake também fiquem numéricos.

## [2.3.0] - 2026-11-04

### Alterado
- Roteamento do grupo `royalties` explícito por `base_id` (`DATASET_ROUTES` em `lake.py`),
  no lugar de trechos do nome (`"pe_" in name`): `royalties-uniao|estado|municipio` vão para
  `royalties_*`, os quatro `pe-*` para `participacoes_especiais` (nova coluna `recorte`:
  uniao/estado/municipio/campo, pois os esquemas diferem) e `preco-ref-gn|petroleo` para
  `preco_referencia_gn`/`preco_referencia_petroleo`. Base fora da tabela fica no dataset do
  grupo. Reconversão: os parquets `preco-ref-*` que antes caíam em `royalties/` devem ser
  removidos de lá e reconvertidos com `--force`; `participacoes_especiais` ganha `recorte`.

**Sondado e não implementado (TC-05, BDEP):**

- `pocos_exploratorios_bdep`: `bdep.gov.br`, `www.bdep.gov.br`, `bdep.anp.gov.br`,
  `geo.anp.gov.br` e `sigep.anp.gov.br` não resolvem DNS (reverificado em 2026-11-04). A página
  de shapefiles da ANP (`.../dados-tecnicos/shapefile-de-dados`) lista só rodadas/blocos
  (`brc`, `op`, `a3`, `a4`), sem camada de poços; sem fonte, sem geometria L5 nem stub.
  Pista: `situacao-pocos` já traz `Latitude_da_base`/`Longitude_da_base` em graus
  `-18:22:40,186`, mas sem datum declarado (EPSG:4674 seria suposição); depende de decisão.
- Os CSVs reais de royalties/PE têm `competencia`/`caixa` como data serial do Excel e nenhum
  `codigo_ibge` (município só por nome minúsculo sem acento): a junção por IBGE não existe
  na fonte.

## [2.2.0] - 2026-11-04

### Adicionado
- O roteamento do Lake dá prioridade às participações especiais e passa a aceitar aliases canônicos de dataset.
- Sem `Last-Modified` na resposta, o arquivo baixado recebe o carimbo da data do download no nome.

### Alterado
- Exige `quantilica-core>=0.16.0`.

## [2.1.2] - 2026-10-30

### Adicionado
- Método opcional `inventory()` no conversor do lake: para cada arquivo bruto, informa
  o dataset que o `convert` vai alimentar ou o motivo de ignorá-lo — gêmeo de outro
  formato, arquivo não tabular (PDF, imagem, documento, mapa) ou versão anterior do
  mesmo formato. Ferramentas de auditoria de cobertura passam a usar esse mapa em vez
  de heurísticas por extensão e nome.

### Corrigido
- A descoberta de arquivos brutos ignora restos `.tmp` de escrita interrompida, que
  podiam ser lidos como se fossem dados.

## [2.1.1] - 2026-10-29

### Corrigido
- `read_csv` funciona com o polars 2, que removeu o argumento `n_threads` da leitura de
  CSV; a releitura tolerante falhava com `TypeError`.

## [2.1.0] - 2026-10-29

### Corrigido
- `read_file` decide o leitor pelo conteúdo quando a extensão engana: `.csv` que é ZIP
  (`shpc-ca_2014-01.csv`) é descompactado, e `.xlsx` que é texto com separador
  (`multas-2021.xlsx`) é lido como CSV.
- `convert` separa as granularidades de um mesmo grupo em datasets distintos: em
  `producao-terra`, `producao-fdp-terra` e `producao-poco-abertos` a série mensal fica com
  o nome do grupo e os arquivos anuais e históricos vão para `<grupo>-anual` e
  `<grupo>-historico`. Antes, partições de profundidades diferentes no mesmo dataset
  impediam o DuckDB de ler o lake ("Hive partition mismatch").
- `convert` converte um só formato de cada conteúdo publicado em vários (`-csv`,
  `-json`): CSV, depois XLSX, XLS e JSON, na versão mais recente.
- `read_file` lê JSON tabular (PMQC) e planilhas `.xls` que na verdade são xlsx
  (assinatura `PK`), que antes falhavam com "Formato não suportado" e "Invalid OLE".
- `read_csv` relê de forma tolerante (linhas com campo a mais, uma só thread) os CSVs
  que o leitor paralelo recusava.
- `read_file` lê como planilha o `.csv` que é um xlsx (`movterm.csv`), e `read_csv`
  tenta por último sem tratar aspas, que em `revendas-glp` fazem parte do nome
  (`MINA D"AGUA`) e antes engoliam linhas ("CSV malformed").

## [2.0.0] - 2026-10-27

### Alterado
- **Quebra de compatibilidade:** transição da saída analítica legada para o lake Parquet particionado no formato Hive (`ano=/mes=` para séries mensais como Preços de Combustíveis, `ano=` para anuais e sem partição para cadastros estáticos), com descritores `_dataset.json` e locks cooperativos.
- **Quebra de compatibilidade:** substituição das rotinas e flags analíticas anteriores pelos comandos padronizados `convert` e `pipeline` integrados via SDK do `FetcherApp` (`--lake`, `--dataset`, `--force`).

### Adicionado
- Módulo `anp_fetcher.lake` e entry point `quantilica.lake`: conversão direta dos arquivos abertos da ANP para o lake Parquet particionado no formato Hive.
- Comandos CLI `convert` e `pipeline` integrados via SDK do `FetcherApp`, com suporte a `--lake`, `--dataset` e `--force`.
- Extra `analysis` atualizado para `quantilica-analytics>=0.5.0`.
- Dependência de base `quantilica-core` atualizada para `>=0.13.0`.

## [1.4.3] - 2026-10-20

### Removido

- Catálogo `producao-terra` (Fase de Desenvolvimento e Produção): entradas
  trimestrais `producao-terra-2020-01..04` descontinuadas — os arquivos
  `producao-terra-2020-{q}trim.csv` nunca existiram no portal com esse
  nome (404 confirmado por probe GET Range em 2026-10-18); os arquivos
  reais de 2020 usam `producao-terra-{q}-trim.csv` e já são cobertos pelo
  grupo `producao-fdp-terra` (grupo: 86 → 82 entradas).


### Alterado
- Reutilização de `read_manifest_sidecar` e `default_output` de `quantilica-core`.
- Dependências atualizadas: `quantilica-core>=0.12.0` e `quantilica-analytics>=0.4.0`.
- Pin de `pytest-cov>=7.1` no grupo dev.

## [1.4.2] - 2026-10-14

### Corrigido

- `plugin.py`: a dica de instalação do extra `analysis` mandava `pip install anp-fetcher[analysis]`, que não funciona para fetchers do Fluxo B (fora do PyPI), e o Rich ainda engolia o `[analysis]` por tratá-lo como marcação, deixando só `pip install anp-fetcher`. Agora a mensagem é `quantilica install anp --extra analysis`. Nos guards de `reader.py`, `wrangling.py` e `contracts.py`, que atendem quem importa o pacote, a mensagem é `uv add 'anp-fetcher[analysis]' --index https://index.quantilica.com/simple/`.

### Alterado
- `README.md`: a seção de instalação deixa de mandar `pip install` (fetchers do Fluxo B não estão no PyPI) e passa a mostrar `quantilica install anp` (com `--extra analysis`) e `uv add --index` para uso como biblioteca.
- `cli.py` protege o import do plugin; sem o host a CLI standalone sai com
  código 1 e orienta `quantilica install <fonte>`.
- `reader.decompress` agora delega a descompressão de arquivos brutos para `quantilica.core.files.decompress_archive`, eliminando lógica local duplicada.
- `cli.py` ganha o bloco `if __name__ == "__main__": main()` (paridade com
  `bcb-sgs-fetcher`).
- `reader.py`, `contracts.py` e `wrangling.py`: imports de `polars`/
  `quantilica.analytics` agora falham com mensagem acionável orientando o
  extra `analysis` (`uv add 'anp-fetcher[analysis]' --index https://index.quantilica.com/simple/`).
- Extra `analysis` declara `polars>=1.0.0` explicitamente; `openpyxl>=3.1.5`
  sai de `dependencies` para o extra `analysis` (só era usado nos testes de
  leitura XLSX, nunca no núcleo).

## [1.4.1] - 2026-10-02

### Alterado

- **Padronização/deduplicação:** `reader.normalize_dtypes` delega a
  conversão de números brasileiros a
  `quantilica.analytics.reader.normalize_brazilian_numbers` (eliminada a
  reimplantação local de vírgula decimal/sentinela).
- **Padronização/deduplicação:** `reader.write_parquet` delega ao
  `quantilica.analytics.writer.to_parquet` canônico — escrita atômica
  (write-temp-rename) e, com manifest do download reconstruído do sidecar do
  arquivo bruto, proveniência `quantilica.*` injetada no Parquet + sidecar
  `.manifest.json` escrito ao lado do destino.
- **Padronização/deduplicação:** `plugin.py` usa o resolver canônico `make_resolve_groups`
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
