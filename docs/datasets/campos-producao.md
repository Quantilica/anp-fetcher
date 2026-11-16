---
dataset:
  id: campos-producao
  fonte: anp
  titulo: Campos em desenvolvimento e produção — cadastro, concessionários, devolvidos e vértices
  resumo: 'Cadastro dos campos de petróleo e gás natural em desenvolvimento e produção no Brasil, em quatro tabelas: campos, concessionários por campo, campos devolvidos e vértices dos polígonos.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo o metadado da ANP; cada arquivo é um retrato do cadastro na data da coleta (2026-11-15), sem histórico
  cobertura:
    inicio: '1941'
    fim: em-curso
  unidade: 'depende da tabela: um campo (`campos-producao`); um concessionário em um campo (`campos-producao-concessionarios`); um campo devolvido (`campos-producao-devolvidos`); um vértice do polígono de um campo (`campos-producao-vertices`)'
  granularidade:
    espacial: campo de produção (código do campo), com bacia, estado e ambiente (terra ou mar); os vértices dão o polígono do campo
    temporal: 'sem série temporal: datas de assinatura do contrato, início e término da produção são atributos do campo; os devolvidos trazem o mês da última produção'
  formato_bruto: quatro CSV em UTF-8 com marca de ordem de bytes (BOM), separados por vírgula
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 23
  unidades_de_medida:
    PARTICIPACAO (%): '% (texto, vírgula decimal)'
    NUM_VERTICE: adimensional (ordem do vértice)
  dados_pessoais:
  - coluna: RAZAO_SOCIAL/CONCESSIONARIO
    categoria: razão social e CNPJ de pessoa jurídica (empresa concessionária)
  - coluna: CNPJ
    categoria: razão social e CNPJ de pessoa jurídica (empresa concessionária)
  - coluna: OPERADOR
    categoria: nome de empresa operadora (pessoa jurídica) ou indicador de operador
  eras:
  - desde: '2026'
    mudanca: layout dos quatro CSV na coleta de 2026-11-15; o metadado da ANP (criado em junho de 2026) descreve as mesmas colunas, e o fetcher só guarda a versão corrente de cada arquivo
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Campos em desenvolvimento e produção — cadastro, concessionários, devolvidos e vértices

## Resumo

Quatro tabelas cadastrais da fase de desenvolvimento e produção publicadas pela ANP: a relação dos campos (contrato, operador, situação e datas), os concessionários de cada campo com a participação no contrato, os campos devolvidos à ANP e as coordenadas dos vértices que delimitam as áreas dos campos. Cada tabela é um retrato do momento da coleta, não uma série histórica: o arquivo é substituído a cada atualização (mensal, segundo a ANP). Os dados vêm do SIGEP e do sistema Do Poço ao Posto, e as quatro tabelas se ligam por `CODIGO_CAMPO`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/campos-producao` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo o metadado da ANP; cada arquivo é um retrato do cadastro na data da coleta (2026-11-15), sem histórico |
| Cobertura | 1941 a em-curso |
| Unidade (uma linha) | depende da tabela: um campo (`campos-producao`); um concessionário em um campo (`campos-producao-concessionarios`); um campo devolvido (`campos-producao-devolvidos`); um vértice do polígono de um campo (`campos-producao-vertices`) |
| Granularidade | espacial: campo de produção (código do campo), com bacia, estado e ambiente (terra ou mar); os vértices dão o polígono do campo; temporal: sem série temporal: datas de assinatura do contrato, início e término da produção são atributos do campo; os devolvidos trazem o mês da última produção |
| Formato bruto | quatro CSV em UTF-8 com marca de ordem de bytes (BOM), separados por vírgula |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 23 |
| Unidades de medida | `PARTICIPACAO (%)`: % (texto, vírgula decimal); `NUM_VERTICE`: adimensional (ordem do vértice) |
| Dados pessoais | `RAZAO_SOCIAL/CONCESSIONARIO` (razão social e CNPJ de pessoa jurídica (empresa concessionária)); `CNPJ` (razão social e CNPJ de pessoa jurídica (empresa concessionária)); `OPERADOR` (nome de empresa operadora (pessoa jurídica) ou indicador de operador) |
| Eras | 2026: layout dos quatro CSV na coleta de 2026-11-15; o metadado da ANP (criado em junho de 2026) descreve as mesmas colunas, e o fetcher só guarda a versão corrente de cada arquivo |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Quatro arquivos CSV na página de dados abertos da fase de desenvolvimento e produção da ANP, subseção de informações sobre campos, em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-campos/`: `extracao-campo.csv` (61.784 bytes), `extracao-campo-concessionarios.csv` (62.503), `extracao-campo-devolvido.csv` (7.580) e `extracao-vertices.csv` (918.602). Tamanhos conferidos na coleta de 2026-11-15.
- Fonte do dado, segundo os metadados: ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, com relatórios elaborados em Power BI; contato demandas_sdp@anp.gov.br. Metadados em `.docx` (criados em junho de 2026) um para cada tabela, na mesma página.
- O servidor da ANP não informa a data de modificação dos arquivos (`Last-Modified` ausente); o sufixo `@AAAAMMDD` do bruto é a data da coleta.

## Conteúdo

- **`campos-producao` (444 campos na amostra):** um campo por linha, com contrato (nome e número), rodada de origem, operador, situação e datas. Situações: `Produção` (305), `Em Devolução` (78), `Desenvolvimento` (41) e `Em devolução, licitado` (20).
- **`campos-producao-concessionarios` (536 linhas):** um concessionário por campo, com razão social, CNPJ, participação percentual e indicador de operador (`S`/`N`). Repete os atributos do campo (nome, bacia, ambiente, estado, rodada e situação).
- **`campos-producao-devolvidos` (150 linhas):** campos devolvidos (`Devolvido`) ou em devolução (`Em Devolução`), com o mês do último Boletim Mensal de Produção, quando há. 78 dos 150 códigos também estão em `campos-producao`.
- **`campos-producao-vertices` (9.765 linhas):** coordenadas dos vértices dos polígonos de 460 campos (444 deles são os de `campos-producao`), em graus, minutos e segundos. Inclui áreas com nome técnico, como `AnC_Jubarte_Sudoeste`.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `campos-producao-concessionarios` (11); `campos-producao-devolvidos` (6); `campos-producao-vertices` (8); `campos-producao` (15) |

## Variáveis

As descrições vêm dos metadados `.docx` da ANP de cada tabela (títulos "Campos", "Campos Devolvidos", "Campos por Concessionários" e "Lista de coordenadas de vértices de áreas na fase de produção"); as observações sobre o conteúdo observado vêm da amostra do lake (2026-11-15). Os metadados dão `CODIGO_CAMPO`, `NUMERO_CONTRATO` e `CNPJ` como número, mas o lake os guarda como texto.
A coluna *Arquivos* diz em quais tabelas a coluna aparece.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `CODIGO_CAMPO` | `CODIGO_CAMPO` | texto | Código do campo cadastrado no SIGEP (Sistema de Informações Gerenciais de Exploração e Produção) da ANP. | — | — | `campos-producao`, `campos-producao-concessionarios`, `campos-producao-devolvidos` e mais 1 |
| `CAMPO` | `CAMPO` | texto | Nome do campo. | — | — | `campos-producao`, `campos-producao-concessionarios`, `campos-producao-devolvidos` e mais 1 |
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar do campo. | — | — | `campos-producao`, `campos-producao-concessionarios`, `campos-producao-devolvidos` e mais 1 |
| `AMBIENTE` | `AMBIENTE` | texto | Ambiente geográfico da produção: terra ou mar (`Mar`/`Terra` nos cadastros de campos e concessionários; `MAR`/`TERRA` nos devolvidos e nos vértices). | — | — | `campos-producao`, `campos-producao-concessionarios`, `campos-producao-devolvidos` e mais 1 |
| `ESTADO` | `ESTADO` | texto | Estado da Federação (nome por extenso) em que o campo se localiza; vazio em alguns campos (3 de 444 na amostra de `campos-producao`). | — | — | `campos-producao`, `campos-producao-concessionarios` |
| `RODADA` | `RODADA` | texto | Rodada de licitação (ou processo) de origem do contrato do campo, em código, como `BID0` (252 campos; 251 com contrato assinado em 06/08/1998, a Rodada Zero), `BID9`, `AM1`, `OP1_BE` e `Xisto_2022`. | — | — | `campos-producao`, `campos-producao-concessionarios` |
| `SITUACAO` | `SITUACAO` | texto | Situação operacional do campo (em `campos-producao-devolvidos`: `Devolvido` ou `Em Devolução`; em `campos-producao-concessionarios`: `Produção`, `Desenvolvimento`, `Em Devolução` ou `Em devolução, licitado`). | — | — | `campos-producao-concessionarios`, `campos-producao-devolvidos` |
| `RAZAO_SOCIAL/CONCESSIONARIO` | `RAZAO_SOCIAL/CONCESSIONARIO` | texto | Razão social da empresa concessionária do campo. | — | — | `campos-producao-concessionarios` |
| `CNPJ` | `CNPJ` | texto | CNPJ da empresa concessionária, só dígitos (14). | — | — | `campos-producao-concessionarios` |
| `PARTICIPACAO (%)` | `PARTICIPACAO (%)` | texto | Participação percentual da empresa no contrato do campo (texto com vírgula decimal, como `05,00` ou `100,00`). | — | — | `campos-producao-concessionarios` |
| `OPERADOR` | `OPERADOR` | texto | Empresa operadora do campo (em `campos-producao-concessionarios`, indicador `S`/`N` de que o concessionário da linha é o operador; em `campos-producao-vertices`, razão social do operador, vazia em parte das linhas). | — | — | `campos-producao`, `campos-producao-concessionarios`, `campos-producao-vertices` |
| `ULTIMO_MES_PRODUCAO` | `ULTIMO_MES_PRODUCAO` | texto | Mês do último Boletim Mensal de Produção enviado do campo (MM/AAAA, texto); vazio em 51 dos 150 campos da amostra. | — | — | `campos-producao-devolvidos` |
| `NUM_VERTICE` | `NUM_VERTICE` | texto | Número sequencial do vértice na lista de vértices do campo. | — | — | `campos-producao-vertices` |
| `LATITUDE` | `LATITUDE` | texto | Latitude do vértice, em graus, minutos e segundos no formato `-GG:MM:SS,SSS` (texto). | — | — | `campos-producao-vertices` |
| `LONGITUDE` | `LONGITUDE` | texto | Longitude do vértice, em graus, minutos e segundos no formato `-GG:MM:SS,SSS` (texto). | — | — | `campos-producao-vertices` |
| `SIGLA_CAMPO` | `SIGLA_CAMPO` | texto | Sigla do campo na ANP. | — | — | `campos-producao` |
| `NOME_CONTRATO` | `NOME_CONTRATO` | texto | Nome fantasia do contrato de E&P ao qual o campo pertence. | — | — | `campos-producao` |
| `NUMERO_CONTRATO` | `NUMERO_CONTRATO` | texto | Número (código) do contrato de E&P ao qual o campo pertence. | — | — | `campos-producao` |
| `SITUACAO_CAMPO` | `SITUACAO_CAMPO` | texto | Situação operacional do campo: `Produção`, `Desenvolvimento`, `Em Devolução` ou `Em devolução, licitado`. | — | — | `campos-producao` |
| `DATA_ASSINATURA` | `DATA_ASSINATURA` | texto | Data de assinatura do contrato (DD/MM/AAAA, texto). | — | — | `campos-producao` |
| `TERMINO_FASE` | `TERMINO_FASE` | texto | Data do término do contrato, segundo o metadado da ANP (DD/MM/AAAA, texto); vazia em 5 campos da amostra. | — | — | `campos-producao` |
| `DATA_INICIO_PRODUCAO` | `DATA_INICIO_PRODUCAO` | texto | Data de início da produção do campo (DD/MM/AAAA, texto); vazia nos campos ainda sem produção. | — | — | `campos-producao` |
| `DATA_TERMINO_PRODUCAO` | `DATA_TERMINO_PRODUCAO` | texto | Previsão de término da produção do campo; apesar de o metadado dizer "data", o arquivo traz só o ano (AAAA). | — | — | `campos-producao` |

## No lake

- Dataset `anp/campos-producao`, sem partição: um Parquet por tabela, `campos-producao.parquet`, `campos-producao-concessionarios.parquet`, `campos-producao-devolvidos.parquet` e `campos-producao-vertices.parquet`.
- Todas as colunas são texto. O conversor remove a marca de ordem de bytes e mantém os nomes do cabeçalho da fonte (maiúsculas, `_` e espaços, como `PARTICIPACAO (%)`).

## Cuidados de uso

- **Retrato, não histórico.** Cada arquivo substitui o anterior; um campo que sai da lista (devolvido, por exemplo) deixa de aparecer em `campos-producao`. Para a evolução, compare as coletas guardadas no bruto.
- **`ESTADO` vazio.** Aparece vazio em 3 campos de `campos-producao` e em 3 linhas de concessionários da amostra (campos em terra novos, como `URUBU-REI LESTE`).
- **`DATA_TERMINO_PRODUCAO` é só o ano.** O metadado fala em "data da previsão de término", mas os valores vão de 2006 a 2072, sem dia e mês; `TERMINO_FASE` e as demais datas vêm como `DD/MM/AAAA`. Todas são texto: converta com `strptime`.
- **Grafias diferentes entre tabelas.** `AMBIENTE` é `Mar`/`Terra` em campos e concessionários e `MAR`/`TERRA` em devolvidos e vértices; padronize com `upper()` antes de juntar. Os nomes de campo se repetem (429 nomes para 444 códigos): ligue as tabelas por `CODIGO_CAMPO`, nunca por `CAMPO`.
- **Campos devolvidos sem produção informada.** `ULTIMO_MES_PRODUCAO` está vazio em 51 dos 150 devolvidos; ao ordenar como texto, `01/1984` vem antes de `09/1960`, então converta antes de calcular mínimos e máximos.
- **Participação em texto.** `PARTICIPACAO (%)` vem como `05,00`, com vírgula decimal. A soma por campo não foi conferida contra 100.
- **Operador em vértices.** `OPERADOR` está vazio em parte dos vértices (146 de 9.765), em geral de áreas com nome técnico (`AnC_...`) ou campos sem operador cadastrado.
- **Unicidade (conferida na amostra).** `CODIGO_CAMPO` é único em `campos-producao` e em `campos-producao-devolvidos`; `(CODIGO_CAMPO, CNPJ)` é único nos concessionários e `(CODIGO_CAMPO, NUM_VERTICE)` nos vértices. Por serem quatro tabelas, a chave do dataset fica vazia.
- **Dados pessoais.** Razão social e CNPJ de empresas concessionárias são dados de pessoas jurídicas, públicos; não há pessoa física.

## Exemplos

Participação do operador em cada campo em produção, ligando o cadastro aos concessionários (a participação vem em texto, com vírgula decimal):

```python
import duckdb

duckdb.sql("""
    SELECT c.CODIGO_CAMPO, c.CAMPO, c.BACIA, k."RAZAO_SOCIAL/CONCESSIONARIO" AS operador,
           replace(k."PARTICIPACAO (%)", ',', '.')::DOUBLE AS participacao_pct
    FROM read_parquet('lake/anp/campos-producao/campos-producao.parquet') c
    JOIN read_parquet('lake/anp/campos-producao/campos-producao-concessionarios.parquet') k
      ON k.CODIGO_CAMPO = c.CODIGO_CAMPO AND k.OPERADOR = 'S'
    WHERE c.SITUACAO_CAMPO = 'Produção'
    ORDER BY participacao_pct DESC, c.CAMPO
    LIMIT 10
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadados (.docx) de campos, campos devolvidos, concessionários e vértices: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-campos/metadados-campos.docx (e os demais na mesma pasta)
