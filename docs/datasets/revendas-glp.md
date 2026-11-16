---
dataset:
  id: revendas-glp
  fonte: anp
  titulo: Cadastro de revendas de GLP (gás de cozinha)
  resumo: Cadastro das revendas de GLP autorizadas pela ANP, com autorização, endereço, distribuidora vinculada e classe de armazenamento, em um arquivo único atualizado diariamente.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: diária, segundo os metadados da ANP; um único arquivo reescrito a cada atualização (página oficial atualizada em 13/11/2026)
  cobertura:
    inicio: '2004'
    fim: em-curso
  unidade: uma vinculação entre uma revenda de GLP (autorização, CNPJ e endereço) e uma distribuidora
  granularidade:
    espacial: estabelecimento (endereço completo, município e UF)
    temporal: retrato da data da publicação; as datas de autorização e de vinculação vão de 2004 a 2026 (com algumas datas inválidas)
  formato_bruto: CSV com separador `;`, UTF-8 sem BOM e CRLF, com cabeçalho na primeira linha
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 14
  dados_pessoais:
  - coluna: RAZAOSOCIAL
    categoria: razão social de pessoa jurídica (revenda), às vezes com o nome do titular
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
    mudanca: formato único observado no arquivo de 15/11/2026, com 14 colunas (não foi possível conferir versões antigas do arquivo)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Cadastro de revendas de GLP (gás de cozinha)

## Resumo

Cadastro dos revendedores de gás liquefeito de petróleo (GLP, o gás de cozinha) mantido pela ANP no SIMP. Cada linha é a vinculação de uma revenda a uma distribuidora (ou a condição `INDEPENDENTE`): traz o código SIMP, a autorização e sua data, a razão social, o CNPJ, o endereço, a distribuidora, a data da vinculação e a classe de armazenamento de GLP do estabelecimento. Uma revenda vinculada a mais de uma distribuidora aparece em mais de uma linha.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/revendas-glp` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | diária, segundo os metadados da ANP; um único arquivo reescrito a cada atualização (página oficial atualizada em 13/11/2026) |
| Cobertura | 2004 a em-curso |
| Unidade (uma linha) | uma vinculação entre uma revenda de GLP (autorização, CNPJ e endereço) e uma distribuidora |
| Granularidade | espacial: estabelecimento (endereço completo, município e UF); temporal: retrato da data da publicação; as datas de autorização e de vinculação vão de 2004 a 2026 (com algumas datas inválidas) |
| Formato bruto | CSV com separador `;`, UTF-8 sem BOM e CRLF, com cabeçalho na primeira linha |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 14 |
| Unidades de medida | — |
| Dados pessoais | `RAZAOSOCIAL` (razão social de pessoa jurídica (revenda), às vezes com o nome do titular); `CNPJ` (CNPJ de pessoa jurídica); `ENDERECO` (endereço do estabelecimento); `COMPLEMENTO` (endereço do estabelecimento); `BAIRRO` (endereço do estabelecimento); `CEP` (endereço do estabelecimento) |
| Eras | 2026: formato único observado no arquivo de 15/11/2026, com 14 colunas (não foi possível conferir versões antigas do arquivo) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo-glp/cadastro-revendas-glp.csv`, o único arquivo do catálogo; a página oficial indica "atualizado em 13/11/2026" e frequência diária (metadados).
- O arquivo lido em 2026-11-15 tem 11.808.891 bytes e 57.243 linhas (cabeçalho mais 57.242 linhas de dados). No bruto, o nome é `revendas-glp@AAAAMMDD.csv`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Metadados em PDF (imagem, sem texto selecionável): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo-glp/metadados-revenda-glp.pdf, que descreve 13 colunas; o arquivo traz também a coluna `CLASSE`, descrita como "Classe de Armazenamento".

## Conteúdo

- **Uma vinculação por linha.** São 57.242 linhas, 57.239 CNPJs distintos e 50.329 razões sociais distintas: três CNPJs aparecem duas vezes, com distribuidoras diferentes ou datas de vinculação diferentes. Por isso não há chave simples.
- **Distribuidoras.** 19 valores de `DISTRIBUIDORA`; `INDEPENDENTE` tem 15.616 linhas, seguida de SUPERGASBRAS ENERGIA (8.453), NACIONAL GAS BUTANO (8.060), LIQUIGAS (5.956) e ULTRAGAZ (5.738).
- **Classe de armazenamento.** `CLASSE` tem 114 combinações distintas; as mais frequentes são `1 AREA  - Classe II - NBR 15514` (18.546), `1 AREA  - Classe III - NBR 15514` (14.150) e `1 AREA  - Classe I - NBR 15514` (9.877); parte dos registros cita a Portaria DNC 27/96 em vez da NBR 15514.
- **Geografia.** Todas as 27 UFs, com SP (9.503), MG (6.735) e RS (4.650) à frente, e 5.161 nomes de município distintos.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `revendas-glp` (14) |

## Variáveis

As descrições vêm do documento de metadados da ANP (PDF em imagem, 13 colunas) e dos valores observados; os nomes das colunas do lake são os do cabeçalho do arquivo, em maiúsculas e sem espaços (o metadado "Código SIMP" é `CODIGOISIMP`). O metadado chama `CLASSE` de "Classe de Armazenamento" e `DISTRIBUIDORA` de "Distribuidora".
Todas as colunas são texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CODIGOISIMP` | `CODIGOISIMP` | texto | Código da revenda no SIMP (Sistema de Informações de Movimentação de Produtos da ANP); vazio em 14 linhas da amostra | — | — |
| `AUTORIZACAO` | `AUTORIZACAO` | texto | Número da autorização da revenda (formatos como `GLP/BA0174939` e `001/GLP/MG0022110`) | — | — |
| `DATAPUBLICACAO` | `DATAPUBLICACAO` | texto | Data em que foi publicada a autorização da revenda, no formato `dd/mm/aaaa` | — | — |
| `RAZAOSOCIAL` | `RAZAOSOCIAL` | texto | Razão social da revenda | — | — |
| `CNPJ` | `CNPJ` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) da revenda, com 14 dígitos e sem pontuação | — | — |
| `ENDERECO` | `ENDERECO` | texto | Endereço (logradouro e número, separados por vírgula) da revenda | — | — |
| `COMPLEMENTO` | `COMPLEMENTO` | texto | Complemento do endereço da revenda; vazio quando não há | — | — |
| `BAIRRO` | `BAIRRO` | texto | Bairro onde está estabelecida a revenda | — | — |
| `CEP` | `CEP` | texto | Código de endereçamento postal do local da revenda, sem hífen; CEPs que começam em zero perdem o zero | — | — |
| `UF` | `UF` | texto | Unidade da Federação onde está estabelecida a revenda | — | — |
| `MUNICIPIO` | `MUNICIPIO` | texto | Município onde está estabelecida a revenda, em maiúsculas e em geral sem acentos | — | — |
| `DISTRIBUIDORA` | `DISTRIBUIDORA` | texto | Distribuidora à qual a revenda é vinculada, ou `INDEPENDENTE` para as revendas que não estão vinculadas a um distribuidor | — | — |
| `DATAVINCULACAO` | `DATAVINCULACAO` | texto | Data de vinculação da revenda ao distribuidor, no formato `dd/mm/aaaa` | — | — |
| `CLASSE` | `CLASSE` | texto | Classe de armazenamento de GLP da revenda: número de áreas, classe (I a VI ou Especial) e norma (NBR 15514 ou Portaria DNC 27/96); pode listar mais de uma área separada por vírgula | — | — |

## No lake

- Dataset `anp/revendas-glp`, sem partições: um Parquet, `revendas-glp.parquet`, com as 14 colunas do CSV, todas como texto.
- Um novo download substitui o retrato anterior no bruto; o lake não guarda histórico de revendas que saíram do cadastro.

## Cuidados de uso

- **É um retrato, não uma série.** O arquivo traz o cadastro do dia; revendas desligadas somem e vinculações anteriores a distribuidoras não aparecem.
- **Datas inválidas em `DATAVINCULACAO`.** Oito linhas têm ano anterior a 2000, entre elas anos impossíveis como `11/09/0204`, `03/03/0205` e `16/12/1208` (digitação errada na fonte); desconsidere vinculações com ano menor que 2000 ou valide com o ano da autorização.
- **Linhas sem código SIMP.** 14 linhas têm `CODIGOISIMP` vazio e uma mesma revenda pode ter dois registros (por exemplo, `CODIGOISIMP` 1052732, com vinculações a COPA ENERGIA em 2007 e INDEPENDENTE em 2021); não use `CODIGOISIMP` nem `CNPJ` isoladamente como chave.
- **`CLASSE` composta.** Em revendas com mais de uma área, a coluna repete a classe separada por vírgula (por exemplo, `1 AREA  - Classe II - NBR 15514 , 1 AREA  - Classe II - NBR 15514`).
- **CEP sem zero à esquerda.** Há CEPs com 7 dígitos (o zero inicial se perdeu) e valores como `0`; complete com zeros até 8 dígitos antes de juntar com outras bases.
- **Dados pessoais.** A razão social e o endereço identificam a revenda (pessoa jurídica); em empresas individuais a razão social pode trazer o nome do titular. Dados públicos da ANP, mas evite divulgação que exponha pessoa física.

## Exemplos

Número de revendas de GLP por distribuidora e UF do estabelecimento, mostrando só as cinco maiores distribuidoras:

```python
import duckdb

duckdb.sql("""
    SELECT DISTRIBUIDORA, count(*) AS vinculacoes, count(DISTINCT CNPJ) AS revendas,
           count(DISTINCT UF) AS ufs
    FROM read_parquet('lake/anp/revendas-glp/*.parquet')
    GROUP BY DISTRIBUIDORA
    ORDER BY vinculacoes DESC
    LIMIT 5
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo-glp/metadados-revenda-glp.pdf
- Lei nº 9.847/1999, citada pela página como base da regulação do abastecimento nacional de combustíveis pela ANP.
