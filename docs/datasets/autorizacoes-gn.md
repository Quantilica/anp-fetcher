---
dataset:
  id: autorizacoes-gn
  fonte: anp
  titulo: Autorizações de construção e operação de instalações de gás natural
  resumo: Autorizações concedidas pela ANP para construção e operação de instalações de gás natural (gasodutos de transporte, pontos de entrega, compressão e outras), desde 1998, em um arquivo atualizado semestralmente.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-autorizacoes-gas-natural
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semestral, segundo os metadados da ANP (de 22/04/2025); a página oficial indica o arquivo atualizado em 20/10/2026
  cobertura:
    inicio: '1998'
    fim: '2026'
  unidade: um ato administrativo (autorização ou despacho) sobre uma instalação de gás natural
  granularidade:
    espacial: instalação (gasoduto, trecho e nome); sem coordenadas, às vezes com o município no texto do trecho
    temporal: data da outorga e data da publicação no D.O.U. (`dd/mm/aaaa`)
  formato_bruto: CSV com separador `,` e UTF-8, com cabeçalho e campos de texto entre aspas (alguns com quebras de linha); a ANP publica também um `.xlsx`
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 14
  unidades_de_medida:
    Extensao: km
    Diametro: polegadas
    Capacidade: milhões de m³ por dia (Mm³/dia)
  dados_pessoais:
  - coluna: Empresa
    categoria: razão social de pessoa jurídica
  eras:
  - desde: '1998'
    mudanca: 'ato mais antigo: outorga de 23/12/1998 (autorização de operação provisória do Gasoduto Guamaré-Pecém, da Petrobras); o arquivo vai até outorgas de setembro de 2026'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Autorizações de construção e operação de instalações de gás natural

## Resumo

Relação das autorizações que a ANP concedeu para construção e operação de instalações de transporte e movimentação de gás natural, segregadas por empresa, tipo de instalação, tipo de autorização (construção ou operação) e características, como extensão, diâmetro e capacidade. Cada linha é um ato administrativo (autorização ou despacho) com seu número, a data da outorga e a publicação no Diário Oficial da União, e uma observação sobre atos correlatos (por exemplo, revogações). A fonte publica o mesmo conteúdo em CSV e em XLSX; o lake converte só o CSV.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/autorizacoes-gn` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-autorizacoes-gas-natural |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semestral, segundo os metadados da ANP (de 22/04/2025); a página oficial indica o arquivo atualizado em 20/10/2026 |
| Cobertura | 1998 a 2026 |
| Unidade (uma linha) | um ato administrativo (autorização ou despacho) sobre uma instalação de gás natural |
| Granularidade | espacial: instalação (gasoduto, trecho e nome); sem coordenadas, às vezes com o município no texto do trecho; temporal: data da outorga e data da publicação no D.O.U. (`dd/mm/aaaa`) |
| Formato bruto | CSV com separador `,` e UTF-8, com cabeçalho e campos de texto entre aspas (alguns com quebras de linha); a ANP publica também um `.xlsx` |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 14 |
| Unidades de medida | `Extensao`: km; `Diametro`: polegadas; `Capacidade`: milhões de m³ por dia (Mm³/dia) |
| Dados pessoais | `Empresa` (razão social de pessoa jurídica) |
| Eras | 1998: ato mais antigo: outorga de 23/12/1998 (autorização de operação provisória do Gasoduto Guamaré-Pecém, da Petrobras); o arquivo vai até outorgas de setembro de 2026 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/autorizacoes-gas-natural/autorizacoes-construcao-operacao-gas-natural.csv` e a versão `.xlsx` do mesmo conteúdo; o lake converte só o CSV (a versão `.xlsx` fica no bruto). A página oficial indica ambos atualizados em 20/10/2026.
- O CSV lido em 2026-11-15 tem 313.251 bytes e 981 linhas de dados; o `.xlsx`, 128.206 bytes. No bruto, os nomes são `autorizacoes-gn-csv@AAAAMMDD.csv` e `autorizacoes-gn-xlsx@AAAAMMDD.xlsx`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Metadados em PDF (de 22/04/2025): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/autorizacoes-gas-natural/metadados-autorizacoes-gas-natural.pdf; fonte: Superintendência de Infraestrutura e Movimentação (SIM/ANP); escopo nacional; codificação UTF-8.

## Conteúdo

- **981 atos de 71 grafias de empresa (68 em maiúsculas distintas).** As maiores são a Transportadora Associada de Gás (TAG, em nove grafias, 366 linhas somadas), o Consórcio Malhas Sudeste Nordeste (240) e a TBG (73), além da Petrobras (60).
- **Tipos.** `TipoDaAutorizacao`: 502 `Operação`, 259 `Construção` e variações como `Operação (Renovação)` (64), `Operação (Pré-Operação)` (40) e `Operação (Provisória)` (33); `TipoDoAto`: 959 autorizações e 22 despachos.
- **Datas.** `DataDaOutorga` vai de 23/12/1998 a 11/09/2026 e `DataDePublicacaoDOU` de 24/12/1998 a 14/09/2026; o ano com mais atos é 2022 (111), seguido de 2010 (101) e 2009 (88).
- **Características.** `Extensao` vem preenchida em 363 linhas, `Diametro` em 365 e `Capacidade` em 651 (as demais ficam vazias porque se aplicam só a gasodutos e a algumas instalações).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `autorizacoes-gn-csv` (14) |

## Variáveis

As descrições vêm do documento de metadados da ANP (22/04/2025). Os nomes das colunas do lake são os do cabeçalho do CSV. A fonte traz os números como texto com casa decimal (`57.0`, `213.0`) e todas as colunas ficam como texto no lake.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Empresa` | `Empresa` | texto | Razão social da empresa autorizada; a grafia varia (por exemplo, a TAG aparece com nove formas) | — | — |
| `TipoDaAutorizacao` | `TipoDaAutorizacao` | texto | Tipo da autorização: em geral Autorização de Construção ou de Operação, com variações (17 valores: `Operação`, `Construção`, `Operação (Renovação)`, `Operação (Pré-Operação)`, `Revogação` e outros) | — | — |
| `TipoDeInstalacao` | `TipoDeInstalacao` | texto | Tipo da instalação alvo da autorização (por exemplo, Gasoduto de Transporte, Linha Tronco, Ramais, Pontos de Entrega, Estações de Regulagem de Pressão, Áreas de recebimento/lançamento de PIG); 130 valores distintos na amostra, muitos descritivos | — | — |
| `NomeDaInstalacao` | `NomeDaInstalacao` | texto | Nome da instalação alvo da autorização; em parte das linhas é texto descritivo longo | — | — |
| `Gasoduto` | `Gasoduto` | texto | Quando aplicável, indica o gasoduto principal ao qual se refere a instalação autorizada | — | — |
| `Trecho` | `Trecho` | texto | Quando aplicável, indica o trecho do gasoduto principal ao qual se refere a instalação autorizada | — | — |
| `Extensao` | `Extensao` | texto | Quando aplicável, extensão do trecho ou do gasoduto principal ao qual se refere a instalação autorizada, em quilômetros (km); texto com ponto decimal (`213.0`) | — | — |
| `Diametro` | `Diametro` | texto | Quando aplicável, diâmetro nominal do trecho ou do gasoduto principal, em polegadas (pol); texto com número inteiro | — | — |
| `Capacidade` | `Capacidade` | texto | Capacidade máxima projetada para a instalação, em milhões de metros cúbicos por dia (Mm³/dia); texto com ponto decimal (`4.67`) | — | — |
| `TipoDoAto` | `TipoDoAto` | texto | Tipo do ato administrativo | Autorização = 959 linhas; Despacho = 22 linhas | — |
| `NumeroDoAto` | `NumeroDoAto` | texto | Numeração sequencial do ato administrativo; a numeração reinicia a cada ano. Texto com um decimal (`151.0`) | — | — |
| `DataDaOutorga` | `DataDaOutorga` | texto | Data da assinatura do ato administrativo, no formato `dd/mm/aaaa` | — | — |
| `DataDePublicacaoDOU` | `DataDePublicacaoDOU` | texto | Data de publicação do ato administrativo no Diário Oficial da União (D.O.U.), no formato `dd/mm/aaaa` | — | — |
| `Observacao` | `Observacao` | texto | Campo livre de observação; normalmente descreve atos administrativos correlatos (por exemplo, `Revoga a Aut. 402, 29/11/2004`) | — | — |

## No lake

- Dataset `anp/autorizacoes-gn`, sem partições: um Parquet, `autorizacoes-gn-csv.parquet`, com as 14 colunas do CSV, todas como texto.
- O arquivo `.xlsx` da mesma página (mesmo conteúdo) não gera Parquet; o lake guarda só a versão CSV.

## Cuidados de uso

- **Cada linha é um ato, não uma instalação.** A mesma instalação aparece em várias linhas (construção, operação, renovação, ampliação, revogação); para saber o que está em vigor é preciso ler `TipoDaAutorizacao` e a `Observacao`, que cita revogações em texto livre (por exemplo, `Revoga a Aut. 321 de 30/05/2022`).
- **Não é só autorização.** `TipoDaAutorizacao` inclui `Revogação` (7 linhas), `Revogação de Autorização de Operação` (5), `Revogação de Autorização de Construção` (4) e `Reclassificação` (3).
- **`NumeroDoAto` não é único.** A numeração reinicia a cada ano e um mesmo ato aparece em várias linhas (uma por instalação); combine o número com o ano da outorga e a empresa.
- **Nomes de empresa inconsistentes.** A TAG aparece em nove grafias, algumas com nota (`( Incorporou Transportadora Capixaba de Gás S.A – TCG )`); normalize antes de agrupar.
- **Texto livre em `NomeDaInstalacao`, `TipoDeInstalacao` e `Trecho`.** Há 130 tipos de instalação distintos, descrições com typos (`Aautorizada a operar ...`) e três linhas sem `NomeDaInstalacao`.
- **Colunas numéricas são texto.** `Extensao`, `Diametro`, `Capacidade` e `NumeroDoAto` têm formato `213.0`; converta com `try_cast`. As datas são texto `dd/mm/aaaa`, todas válidas na amostra.
- **Dados pessoais.** Só há razões sociais de empresas autorizadas.

## Exemplos

Número de atos por ano de outorga e tipo de ato, nos últimos anos:

```python
import duckdb

duckdb.sql("""
    SELECT year(strptime(DataDaOutorga, '%d/%m/%Y')) AS ano, TipoDoAto, count(*) AS atos
    FROM read_parquet('lake/anp/autorizacoes-gn/*.parquet')
    WHERE year(strptime(DataDaOutorga, '%d/%m/%Y')) >= 2022
    GROUP BY ALL
    ORDER BY ano, TipoDoAto
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-autorizacoes-gas-natural
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/autorizacoes-gas-natural/metadados-autorizacoes-gas-natural.pdf
