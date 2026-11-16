---
dataset:
  id: revendedores
  fonte: anp
  titulo: Cadastro de revendedores varejistas de combustíveis automotivos (postos em operação)
  resumo: Cadastro dos postos revendedores varejistas de combustíveis automotivos em operação, com autorização, endereço e bandeira, em um arquivo único atualizado diariamente pela ANP.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: diária, segundo os metadados da ANP; um único arquivo reescrito a cada atualização (página oficial atualizada em 13/11/2026)
  cobertura:
    inicio: '2000'
    fim: em-curso
  unidade: um posto revendedor varejista de combustíveis automotivos em operação (um CNPJ e um código SIMP)
  granularidade:
    espacial: estabelecimento (endereço completo, município e UF)
    temporal: retrato da data da publicação; as datas de autorização e de vinculação vão de 2000 a 2026
  formato_bruto: CSV com separador `;`, UTF-8 sem BOM e CRLF, com cabeçalho na primeira linha
  lake:
    estado: convertido
    particoes: []
    chave:
    - CODIGOISIMP
    colunas: 13
  dados_pessoais:
  - coluna: RAZAOSOCIAL
    categoria: razão social de pessoa jurídica (posto), às vezes com o nome do titular
  - coluna: CNPJ
    categoria: CNPJ de pessoa jurídica
  - coluna: ENDERECO
    categoria: endereço do estabelecimento
  - coluna: COMPLEMENTO
    categoria: endereço do estabelecimento
  - coluna: BAIRRO
    categoria: endereço do estabelecimento
  - coluna: CEP
    categoria: endereço do estabelecimento
  eras:
  - desde: '2026'
    mudanca: formato único observado no arquivo de 15/11/2026, com 13 colunas; os registros de autorização vão de 2000 a 2026 (não foi possível conferir versões antigas do arquivo)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Cadastro de revendedores varejistas de combustíveis automotivos (postos em operação)

## Resumo

Cadastro dos revendedores varejistas de combustíveis automotivos (postos de combustíveis) que estão em operação, mantido pela ANP no SIMP. Cada linha é um posto, identificado pelo código SIMP e pelo CNPJ, com o número e a data de publicação da autorização, o endereço, a bandeira (a distribuidora à qual o posto está vinculado ou `BANDEIRA BRANCA`) e a data de vinculação. É um retrato do momento da publicação: não traz postos que deixaram de operar nem o histórico de bandeiras.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/revendedores` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | diária, segundo os metadados da ANP; um único arquivo reescrito a cada atualização (página oficial atualizada em 13/11/2026) |
| Cobertura | 2000 a em-curso |
| Unidade (uma linha) | um posto revendedor varejista de combustíveis automotivos em operação (um CNPJ e um código SIMP) |
| Granularidade | espacial: estabelecimento (endereço completo, município e UF); temporal: retrato da data da publicação; as datas de autorização e de vinculação vão de 2000 a 2026 |
| Formato bruto | CSV com separador `;`, UTF-8 sem BOM e CRLF, com cabeçalho na primeira linha |
| Estado no lake | convertido |
| Partições | — |
| Chave | `CODIGOISIMP` |
| Colunas | 13 |
| Unidades de medida | — |
| Dados pessoais | `RAZAOSOCIAL` (razão social de pessoa jurídica (posto), às vezes com o nome do titular); `CNPJ` (CNPJ de pessoa jurídica); `ENDERECO` (endereço do estabelecimento); `COMPLEMENTO` (endereço do estabelecimento); `BAIRRO` (endereço do estabelecimento); `CEP` (endereço do estabelecimento) |
| Eras | 2026: formato único observado no arquivo de 15/11/2026, com 13 colunas; os registros de autorização vão de 2000 a 2026 (não foi possível conferir versões antigas do arquivo) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos/dados-cadastrais-revendedores-varejistas-combustiveis-automoveis.csv`, o único arquivo do catálogo para este conjunto; a página oficial indica "atualizado em 13/11/2026" e frequência diária (metadados).
- O arquivo lido em 2026-11-15 tem 7.908.076 bytes e 45.841 linhas (cabeçalho mais 45.840 postos). No bruto, o nome é `revendedores-varejistas@AAAAMMDD.csv`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Metadados em PDF (imagem, sem texto selecionável): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos/metadados-revendedores-varejistas-combustiveis-automoveis.pdf, que descreve as 13 colunas e indica "fonte do dado" em branco.

## Conteúdo

- **Um posto por linha.** `CODIGOISIMP` e `CNPJ` não se repetem na amostra (45.840 valores distintos em cada), de modo que o arquivo tem um registro por posto.
- **Só postos em operação.** A página oficial descreve o conjunto como os revendedores "que estão em operação"; o arquivo não tem coluna de situação nem postos cancelados.
- **Datas.** `DATAPUBLICACAO` vai de 18/08/2000 a 11/11/2026 e `DATAVINCULACAO` de 18/08/2000 a 12/11/2026 (todas válidas no formato `dd/mm/aaaa`).
- **Bandeiras.** 64 valores distintos de `BANDEIRA`; `BANDEIRA BRANCA` responde por 21.962 dos 45.840 postos, seguida de VIBRA (6.957), IPIRANGA (5.639) e RAIZEN (4.801).
- **Geografia.** Os 45.840 postos estão nas 27 UFs, com SP (8.388), MG (5.046) e BA (3.729) à frente, e em 5.254 nomes de município distintos.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `revendedores-varejistas` (13) |

## Variáveis

As descrições vêm do documento de metadados da ANP (PDF em imagem, 13 colunas, "Código SIMP" ... "Data Vinculação"). Os nomes das colunas do lake são os do cabeçalho do arquivo, em maiúsculas e sem espaços (por exemplo, o metadado "Código SIMP" é a coluna `CODIGOISIMP`).
Todas as colunas são texto; os códigos e rótulos de `BANDEIRA` não têm tabela na fonte.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CODIGOISIMP` | `CODIGOISIMP` | texto | Código da revenda no SIMP (Sistema de Informações de Movimentação de Produtos da ANP) | — | — |
| `AUTORIZACAO` | `AUTORIZACAO` | texto | Número da autorização da revenda (formato `PR/UF` seguido de dígitos na amostra) | — | — |
| `DATAPUBLICACAO` | `DATAPUBLICACAO` | texto | Data em que foi publicada a autorização da revenda, no formato `dd/mm/aaaa` | — | — |
| `RAZAOSOCIAL` | `RAZAOSOCIAL` | texto | Razão social da revenda | — | — |
| `CNPJ` | `CNPJ` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) da revenda, com 14 dígitos e sem pontuação | — | — |
| `ENDERECO` | `ENDERECO` | texto | Endereço (logradouro e número, separados por vírgula) da revenda | — | — |
| `COMPLEMENTO` | `COMPLEMENTO` | texto | Complemento do endereço da revenda; vazio quando não há | — | — |
| `BAIRRO` | `BAIRRO` | texto | Bairro onde está estabelecida a revenda | — | — |
| `CEP` | `CEP` | texto | Código de endereçamento postal do local da revenda, sem hífen; os CEPs que começam em zero perdem o zero (7 dígitos) | — | — |
| `UF` | `UF` | texto | Unidade da Federação onde está estabelecida a revenda | — | — |
| `MUNICIPIO` | `MUNICIPIO` | texto | Município onde está estabelecida a revenda, em maiúsculas e em geral sem acentos | — | — |
| `BANDEIRA` | `BANDEIRA` | texto | Distribuidora à qual a revenda é vinculada, ou `BANDEIRA BRANCA` para as revendas que não estão vinculadas a um distribuidor | — | — |
| `DATAVINCULACAO` | `DATAVINCULACAO` | texto | Data de vinculação da revenda ao distribuidor (bandeira), no formato `dd/mm/aaaa` | — | — |

## No lake

- Dataset `anp/revendedores`, sem partições: um Parquet, `revendedores-varejistas.parquet`, com as 13 colunas do CSV, todas como texto (CNPJ, CEP e datas inclusive).
- Um novo download substitui o retrato anterior no bruto (com outra data no sufixo); o lake não guarda histórico de postos que saíram do cadastro.

## Cuidados de uso

- **É um retrato, não uma série.** Cada arquivo traz o cadastro do dia; postos que deixaram de operar somem e a bandeira anterior de um posto não aparece (só a vinculação vigente, em `DATAVINCULACAO`).
- **CEP sem zero à esquerda.** Dos 45.840 CEPs, 43.129 têm 8 dígitos, 2.707 têm 7 (o zero inicial se perdeu), 1 tem 5 e 3 valem `0`. Complete com zeros à esquerda até 8 dígitos antes de juntar com outras bases e trate `0` como ausente.
- **Complemento vazio.** 32.520 linhas têm `COMPLEMENTO` nulo e 70 têm texto vazio; trate os dois como ausência.
- **Valores estranhos em `BANDEIRA`.** Há valores curtos que parecem abreviações ou erros de cadastro (`SP` em 314 postos, `FAN` em 157, `UNI` em 2 e `GP` em 1); não foram verificados na fonte. `BANDEIRA BRANCA` indica posto sem vínculo com distribuidora.
- **Dados pessoais.** A razão social e o endereço identificam o posto (pessoa jurídica); em empresas individuais a razão social pode trazer o nome do titular. Os dados são públicos da ANP, mas evite divulgação que exponha pessoa física.
- **`DATAPUBLICACAO` e `DATAVINCULACAO` são texto `dd/mm/aaaa`.** Converta com `strptime`; na amostra todas as linhas preenchidas são datas válidas (uma linha tem `AUTORIZACAO`, `DATAPUBLICACAO` e `DATAVINCULACAO` nulas).

## Exemplos

Postos em operação por bandeira, separando os de bandeira branca:

```python
import duckdb

duckdb.sql("""
    SELECT BANDEIRA, count(*) AS postos
    FROM read_parquet('lake/anp/revendedores/*.parquet')
    GROUP BY BANDEIRA
    ORDER BY postos DESC
    LIMIT 10
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos/metadados-revendedores-varejistas-combustiveis-automoveis.pdf
- Lei nº 9.847/1999, citada pela página como base da regulação do abastecimento nacional de combustíveis pela ANP.
