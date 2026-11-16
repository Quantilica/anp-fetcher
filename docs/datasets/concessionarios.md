---
dataset:
  id: concessionarios
  fonte: anp
  titulo: Relação de concessionários
  resumo: Contratos de E&P ativos com suas empresas signatárias e participações, por rodada e fase, e a tabela do grupo e do país de origem de cada concessionário.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/relacao-de-concessionarios
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semestral (metadados da ANP para a tabela de países de origem)
  cobertura:
    inicio: 2026-07
    fim: 2026-07
  unidade: uma empresa signatária de um contrato (`rc-relacao`) ou um concessionário com seu grupo e país (`rc-pais-origem`)
  granularidade:
    espacial: bacia sedimentar e ambiente (terra ou mar) do contrato; país de origem do grupo
    temporal: situação dos contratos na data de atualização do arquivo (1/7/2026 segundo a página); sem série temporal
  formato_bruto: dois CSV (relacao-concessionarios.csv e relacao-pais-origem-concessionarios.csv), separador ponto e vírgula, ISO-8859-1, uma linha de cabeçalho
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 12
  unidades_de_medida:
    '% Participação': '% (percentual, 0 a 100)'
  dados_pessoais:
  - coluna: CNPJ
    categoria: CNPJ de pessoa jurídica
  - coluna: Nome Fantasia
    categoria: nome de empresa ou grupo empresarial (pessoa jurídica)
  - coluna: Razão Social
    categoria: nome de empresa ou grupo empresarial (pessoa jurídica)
  - coluna: Grupo
    categoria: nome de empresa ou grupo empresarial (pessoa jurídica)
  - coluna: Nome
    categoria: nome de empresa ou grupo empresarial (pessoa jurídica)
  eras: []
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Relação de concessionários

## Resumo

A relação dos concessionários consolida os contratos ativos de exploração e produção na ANP, organizados por rodada de licitação, com a fase em que cada contrato se encontra, as empresas signatárias e suas participações. O grupo traz duas tabelas: a relação de contratos e signatárias (`rc-relacao`, uma linha por contrato e empresa) e a relação do grupo e do país de origem de cada concessionário ou contratado (`rc-pais-origem`), que cobre contratos de concessão, partilha de produção e cessão onerosa.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/concessionarios` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/relacao-de-concessionarios |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semestral (metadados da ANP para a tabela de países de origem) |
| Cobertura | 2026-07 a 2026-07 |
| Unidade (uma linha) | uma empresa signatária de um contrato (`rc-relacao`) ou um concessionário com seu grupo e país (`rc-pais-origem`) |
| Granularidade | espacial: bacia sedimentar e ambiente (terra ou mar) do contrato; país de origem do grupo; temporal: situação dos contratos na data de atualização do arquivo (1/7/2026 segundo a página); sem série temporal |
| Formato bruto | dois CSV (relacao-concessionarios.csv e relacao-pais-origem-concessionarios.csv), separador ponto e vírgula, ISO-8859-1, uma linha de cabeçalho |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 12 |
| Unidades de medida | `% Participação`: % (percentual, 0 a 100) |
| Dados pessoais | `CNPJ` (CNPJ de pessoa jurídica); `Nome Fantasia` (nome de empresa ou grupo empresarial (pessoa jurídica)); `Razão Social` (nome de empresa ou grupo empresarial (pessoa jurídica)); `Grupo` (nome de empresa ou grupo empresarial (pessoa jurídica)); `Nome` (nome de empresa ou grupo empresarial (pessoa jurídica)) |
| Eras | nenhuma |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** a tabela de países de origem é da Superintendência de Promoção de Licitações (SPL), com dados do SIGEP (Sistema de Informações Gerenciais de Exploração e Produção); contato rodadas@anp.gov.br (metadados da ANP).
- **Catálogo do fetcher:** 2 arquivos, `rc-relacao` e `rc-pais-origem` (conferido em 2026-11-15). A página oficial indica atualização em 1/7/2026 para os dois arquivos.
- **Metadados da tabela de relação:** o arquivo «metadados-relacao-concessionarios.pdf» da página oficial traz o mesmo texto dos metadados da tabela de países de origem (título «Relação do País de origem dos Concessionários» e colunas `Nome Fantasia`, `Razão Social`, `Grupo` e `País`); o dicionário das colunas de `rc-relacao` (`BID`, `Número Contrato`, `Fase`...) não é publicado, e suas descrições aqui são deduzidas do nome e dos valores observados (conferido em 2026-11-15).

## Conteúdo

| Arquivo no lake | Conteúdo | Linhas |
|---|---|---|
| `rc-relacao` | contratos ativos: rodada de origem (`BID`), número do contrato, fase, nome fantasia, bacia, signatária (CNPJ e nome), participação e ambiente | 1.102 |
| `rc-pais-origem` | concessionários e contratados com razão social, grupo e país de origem do grupo | 118 |

- **Contratos:** 883 contratos em 44 identificadores de rodada ou ciclo (`BID`); cada um tem exatamente uma linha de operador (prefixo `(Operador) -` em `Nome`) e a soma das participações é 100% em todos.
- **Fase e ambiente:** 589 linhas em `Exploração`, 508 em `Produção` e 5 em `Avaliação`; 645 em terra e 457 no mar.
- **País de origem:** 75 dos 118 concessionários têm grupo brasileiro (`BRASIL`); os demais se distribuem em 18 países (Noruega 6; China, Reino Unido e Estados Unidos 4 cada).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `rc-pais-origem` (4); `rc-relacao` (9) |

## Variáveis

As descrições de `rc-pais-origem` vêm dos metadados da ANP; as de `rc-relacao` são deduzidas do nome da coluna e dos valores observados, porque o dicionário dessa tabela não está acessível (ver Origem). O lake guarda tudo como texto. A coluna *Arquivos* diz em qual tabela a coluna aparece; `Nome Fantasia` está nas duas, com sentidos diferentes.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Nome Fantasia` | `Nome Fantasia` | texto | Nome fantasia do contrato (em `rc-relacao`: por exemplo, `Carapitanga`, nome do campo ou da área) ou do concessionário (em `rc-pais-origem`: por exemplo, `Petrobras`) | — | — | `rc-pais-origem`, `rc-relacao` |
| `Razão Social` | `Razão Social` | texto | Razão social do concessionário ou contratado | — | — | `rc-pais-origem` |
| `Grupo` | `Grupo` | texto | Nome do grupo a que pertence o concessionário ou contratado | — | — | `rc-pais-origem` |
| `País` | `País` | texto | País de origem do grupo a que pertence o concessionário ou contratado (em maiúsculas e sem acento, por exemplo, `BRASIL`, `NORUEGA`) | — | — | `rc-pais-origem` |
| `BID` | `BID` | texto | Identificador da rodada ou do ciclo de licitação de origem do contrato (por exemplo, `AM1`, `BID0`, `BID11`, `OP4_BE`); descrição deduzida do nome e dos valores observados; o dicionário da ANP para esta tabela não está acessível | — | — | `rc-relacao` |
| `Número Contrato` | `Número Contrato` | texto | Número do contrato de E&P, sem pontuação (17 dígitos na maioria; um contrato por valor, com uma linha por empresa signatária) | — | — | `rc-relacao` |
| `Fase` | `Fase` | texto | Fase em que se encontra o contrato: `Exploração`, `Avaliação` ou `Produção` (valores observados; a página da ANP diz que a tabela mostra a fase de cada contrato) | — | — | `rc-relacao` |
| `Bacia` | `Bacia` | texto | Bacia sedimentar do contrato | — | — | `rc-relacao` |
| `CNPJ` | `CNPJ` | texto | CNPJ da empresa signatária, só dígitos, sem zeros à esquerda (12 a 14 dígitos: o zero inicial se perdeu na fonte; complete com zeros à esquerda até 14 dígitos); descrição deduzida do nome | — | — | `rc-relacao` |
| `Nome` | `Nome` | texto | Empresa signatária do contrato; o operador vem com o prefixo `(Operador) - ` | — | — | `rc-relacao` |
| `% Participação` | `% Participação` | texto | Participação percentual da empresa no contrato, com vírgula decimal (por exemplo, `100,00`); a soma por contrato é 100 em todos os contratos do lake | — | — | `rc-relacao` |
| `Ambiente` | `Ambiente` | texto | Ambiente do contrato: `Terra` ou `Mar` | — | — | `rc-relacao` |

## No lake

- Dataset `anp/concessionarios`, sem partições; um Parquet por tabela, `rc-relacao.parquet` e `rc-pais-origem.parquet`. Todas as colunas são texto.
- Os espaços à direita do identificador `BID` no CSV de origem (`AM1            `) foram removidos na conversão.

## Cuidados de uso

- **Instantâneo, não série.** Cada arquivo reflete o estado na data da atualização; para acompanhar mudanças é preciso guardar arquivos de datas diferentes.
- **CNPJ sem zero à esquerda.** 303 dos 1.102 CNPJs têm 12 ou 13 dígitos, porque a fonte não preserva o zero inicial; complete com zeros à esquerda até 14 dígitos antes de ligar a outras tabelas.
- **Uma linha por empresa, não por contrato.** `Número Contrato` se repete para cada signatária (1.102 linhas para 883 contratos); para contar contratos, use `count(distinct)`.
- **Operador no nome.** O operador é marcado no texto de `Nome` com o prefixo `(Operador) - `, e não em coluna própria.
- **Nome fantasia tem dois sentidos.** Em `rc-relacao` identifica o contrato e em `rc-pais-origem`, o concessionário.
- **Metadados da relação ausentes.** O dicionário das colunas de `rc-relacao` não é publicado (o arquivo de metadados da página repete o da tabela de países); trate as descrições como interpretação.
- **Países em maiúsculas e sem padrão de acento** (`CHINA, REPUBLICA POPULAR`); `País` pode precisar de normalização antes de ligar a tabelas de países.
- **Dados identificáveis.** CNPJ, razão social, grupo e participação são de pessoas jurídicas e públicos; o arquivo não traz pessoas físicas.

## Exemplos

Número de contratos por fase e ambiente na relação de concessionários:

```python
import duckdb

duckdb.sql("""
    SELECT "Fase" AS fase, "Ambiente" AS ambiente, count(DISTINCT "Número Contrato") AS contratos
    FROM read_parquet('lake/anp/concessionarios/rc-relacao.parquet')
    GROUP BY ALL
    ORDER BY contratos DESC
""").show()
```

## Referências

- Dados abertos da ANP, Relação de Concessionários: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/relacao-de-concessionarios
- Metadados da tabela de países de origem: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/rc/relacao-pais-origem-concessionarios.pdf
