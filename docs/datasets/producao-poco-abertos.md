---
dataset:
  id: producao-poco-abertos
  fonte: anp
  titulo: Produção de petróleo e gás natural por poço (dados abertos)
  resumo: Produção mensal de petróleo e gás natural por poço, com campo, operador, instalação e características do óleo e do gás, de 2005 a 2023, em ZIP anuais e mensais da ANP.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-poco
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (publicado com dois meses de defasagem); o fetcher lê ZIP anuais de 2005 a 2020 e ZIP mensais de 2021 a 2023
  cobertura:
    inicio: 2005-01
    fim: 2023-12
  unidade: um registro de produção de um poço em um mês (`Período`), com instalação de destino e, quando há, a corrente de petróleo; um mesmo poço pode ter mais de uma linha no mês
  granularidade:
    espacial: poço (nome ANP), com campo, bacia e estado; ambiente terra, mar ou pré-sal
    temporal: mês de referência (`Período`, AAAA/MM)
  formato_bruto: ZIP com CSV por ambiente (terra, mar e, desde 2020, pré-sal), separados por vírgula, com decimal em vírgula e ponto de milhar; os ZIP anuais contêm um CSV por ambiente por ano (2005 a 2019) ou por mês (2020)
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 49
  unidades_de_medida:
    Óleo (bbl/dia): bbl/dia
    Condensado (bbl/dia): bbl/dia
    Petróleo (bbl/dia): bbl/dia
    Água (bbl/dia): bbl/dia
    Gás Natural (Mm³/dia) Associado: mil m³/dia
    Gás Natural (Mm³/dia) Não Associado: mil m³/dia
    Gás Natural (Mm³/dia) Gás Total: mil m³/dia
    Volume Gás Royalties (Mm³/dia): mil m³/dia
    Total Gás Natural (Mm³/dia): mil m³/dia
    Tempo de Produção (hs por mês): horas por mês
    Grau API: °API
    PCS GP (kJ/m³): kJ/m³
    Densidade GLP Gás: kg/m³
    Densidade GLP Líquido: kg/m³
    OLEO_M3: m³ (período não informado)
    CONDENSADO_M3: m³ (período não informado)
    AGUA_M3: m³ (período não informado)
  dados_pessoais:
  - coluna: Operador
    categoria: nome fantasia de empresa operadora (pessoa jurídica)
  eras:
  - desde: '2005'
    mudanca: ZIP anuais de 2005 a 2020 com 20 colunas no lake (produção em bbl/dia e Mm³/dia, instalação de destino a partir de 2009 e tempo de produção); o ZIP de 2008 da amostra não preenche `Instalação Destino` nem `Tipo Instalação`
  - desde: '2020'
    mudanca: o ZIP de 2020 traz 12 CSV por ambiente e passa a ter 48 colunas, com corrente, grau API, frações de destilados, composição do gás, densidades e PCS; de setembro de 2020 em diante entra `Data de atualização` (49 colunas); aparece o arquivo de pré-sal
  - desde: '2021'
    mudanca: arquivos mensais (um ZIP por mês, com `producao_Mar`, `producao_Presal` e `producao_Terra`), 49 colunas
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de petróleo e gás natural por poço (dados abertos)

## Resumo

Produção mensal de petróleo (óleo e condensado, em barris por dia), gás natural (em milhares de m³ por dia) e água de cada poço em produção no Brasil, com localização (campo, bacia, estado), titularidade (operador e número do contrato), instalação de destino, tempo de produção e, desde 2020, características físico-químicas do petróleo (grau API, frações de destilados) e do gás (composição em volume, densidades e poder calorífico). Os dados vêm do SIGEP e são publicados com defasagem de dois meses: as operadoras enviam os Boletins Mensais de Produção (BMP) na primeira quinzena do mês seguinte, a ANP confere e valida na segunda quinzena e publica no mês subsequente. Cada ZIP traz um CSV por ambiente: terra, mar e pré-sal (este último é um subconjunto de mar).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/producao-poco-abertos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-poco |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (publicado com dois meses de defasagem); o fetcher lê ZIP anuais de 2005 a 2020 e ZIP mensais de 2021 a 2023 |
| Cobertura | 2005-01 a 2023-12 |
| Unidade (uma linha) | um registro de produção de um poço em um mês (`Período`), com instalação de destino e, quando há, a corrente de petróleo; um mesmo poço pode ter mais de uma linha no mês |
| Granularidade | espacial: poço (nome ANP), com campo, bacia e estado; ambiente terra, mar ou pré-sal; temporal: mês de referência (`Período`, AAAA/MM) |
| Formato bruto | ZIP com CSV por ambiente (terra, mar e, desde 2020, pré-sal), separados por vírgula, com decimal em vírgula e ponto de milhar; os ZIP anuais contêm um CSV por ambiente por ano (2005 a 2019) ou por mês (2020) |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 49 |
| Unidades de medida | `Óleo (bbl/dia)`: bbl/dia; `Condensado (bbl/dia)`: bbl/dia; `Petróleo (bbl/dia)`: bbl/dia; `Água (bbl/dia)`: bbl/dia; `Gás Natural (Mm³/dia) Associado`: mil m³/dia; `Gás Natural (Mm³/dia) Não Associado`: mil m³/dia; `Gás Natural (Mm³/dia) Gás Total`: mil m³/dia; `Volume Gás Royalties (Mm³/dia)`: mil m³/dia; `Total Gás Natural (Mm³/dia)`: mil m³/dia; `Tempo de Produção (hs por mês)`: horas por mês; `Grau API`: °API; `PCS GP (kJ/m³)`: kJ/m³; `Densidade GLP Gás`: kg/m³; `Densidade GLP Líquido`: kg/m³; `OLEO_M3`: m³ (período não informado); `CONDENSADO_M3`: m³ (período não informado); `AGUA_M3`: m³ (período não informado) |
| Dados pessoais | `Operador` (nome fantasia de empresa operadora (pessoa jurídica)) |
| Eras | 2005: ZIP anuais de 2005 a 2020 com 20 colunas no lake (produção em bbl/dia e Mm³/dia, instalação de destino a partir de 2009 e tempo de produção); o ZIP de 2008 da amostra não preenche `Instalação Destino` nem `Tipo Instalação`; 2020: o ZIP de 2020 traz 12 CSV por ambiente e passa a ter 48 colunas, com corrente, grau API, frações de destilados, composição do gás, densidades e PCS; de setembro de 2020 em diante entra `Data de atualização` (49 colunas); aparece o arquivo de pré-sal; 2021: arquivos mensais (um ZIP por mês, com `producao_Mar`, `producao_Presal` e `producao_Terra`), 49 colunas |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa 52 ZIP de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-petroleo-e-gas-natural-por-poco/`: um por ano de 2005 a 2020 (`producao-por-poco-<ano>.zip`, na pasta de cada período) e um por mês de 2021 a 2023 (`2021/`, `2022/` e `2023/`, com nomes que variam, como `2021_01_producao.zip`, `producao-2022-01.zip` e `producao-01.zip`). A página oficial diz "Produção por Poço 2024 em diante" e remete à Consulta de Dados Públicos da ANP, que o fetcher não coleta.
- Fonte do dado, segundo o metadado "Dados de Produção por Poço" (PDF, atualizado em 11/3/2026): Superintendência de Dados Técnicos (SDT) da ANP, a partir do SIGEP; periodicidade mensal; contato consulta_pocos@anp.gov.br. Há um segundo metadado para a série 2005-2017 (com as 20 primeiras colunas).
- **Dois conjuntos independentes de ZIP anuais:** o grupo `ppg` baixa ZIP por poço de 2005 a 2023 da página de dados estatísticos (`.../dados-estatisticos/de/ppg/pp/producao-pocos-<ano>.zip`), com decimal em ponto; as duas coleções cobrem os mesmos anos e podem se sobrepor. Não foi conferida a igualdade de conteúdo.
- No bruto: `producao-poco-abertos/producao-poco-da_<ano>@AAAAMMDD.zip` (anual) ou `producao-poco-da_<ano>-<mês>@AAAAMMDD.zip` (mensal); o sufixo é a data da coleta. Na amostra, de 0,3 MB (um mês) a 4,3 MB (2020).

## Conteúdo

- **Uma linha por registro de produção.** Cada linha traz a vazão média do mês de um poço (`Petróleo (bbl/dia)`, gás em Mm³/dia, água em bbl/dia), com a instalação de destino. Na amostra de janeiro de 2023 em mar, 601 poços ocupam 839 linhas: o mesmo poço pode repetir (por exemplo, `7-OATP-1-RJS` tem quatro linhas, com `Petróleo` de 275 a 14.373 bbl/dia, mesma instalação e mesma corrente). O metadado da ANP não explica a repetição.
- **Terra, mar e pré-sal.** O CSV de pré-sal contém só poços do polígono do pré-sal, que também estão no CSV de mar (em janeiro de 2023, os 346 poços de pré-sal estão todos em mar). Somar mar e pré-sal conta duas vezes.
- **Características do óleo e do gás (a partir de 2020).** `Corrente`, `Grau API`, as frações de destilados e a composição do gás vêm preenchidas só em parte das linhas (1.080 de 6.310 linhas de janeiro de 2023 não têm `Corrente`).

Quatro datasets do lake, por granularidade do arquivo e por ambiente:

| Dataset do lake | Partições | Conteúdo | Amostra |
|---|---|---|---|
| `producao-poco-abertos` | `ano`, `mes` | terra e mar de ZIP mensais (2021 a 2023) | 2021-03, 2022-02, 2023-01 e 2023-02 |
| `producao-poco-abertos-presal` | `ano`, `mes` | pré-sal de ZIP mensais | os mesmos quatro meses |
| `producao-poco-abertos-anual` | `ano` | terra e mar de ZIP anuais (2005 a 2020) | 2008 e 2020 (12 meses) |
| `producao-poco-abertos-anual-presal` | `ano` | pré-sal do ZIP de 2020 | 12 meses de 2020 |

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2008 | `producao-poco-abertos-anual` (20); `producao-poco-abertos-anual` (20) |
| 2020 | 36 arquivos, de 48 a 49 colunas |
| 2021 | `producao-poco-abertos` (49); `producao-poco-abertos` (49); `producao-poco-abertos-presal` (49) |
| 2022 | `producao-poco-abertos` (49); `producao-poco-abertos` (49); `producao-poco-abertos-presal` (49) |
| 2023 | `producao-poco-abertos` (49); `producao-poco-abertos` (49); `producao-poco-abertos` (49); `producao-poco-abertos` (49); `producao-poco-abertos-presal` (49); `producao-poco-abertos-presal` (49) |

## Variáveis

As descrições vêm do metadado "Dados de Produção por Poço" (PDF da ANP, atualizado em 11/3/2026, que traz também o nome antigo e o atual de cada coluna). O metadado dá `Número do Contrato` como texto, o período como `AAAA/MM` e os percentuais como número; no lake tudo é texto.
A coluna *Arquivos* mostra em que tabelas do lake a coluna aparece; `ambiente` é acrescentada pelo conversor.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Estado` | `Estado` | texto | Estado da federação onde foi perfurado o poço (nome por extenso; o metadado fala em sigla). | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar onde foi perfurado o poço. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Nome Poço ANP` | `Nome Poço ANP` | texto | Nome do poço segundo a Resolução ANP nº 699/2017. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Nome Poço Operador` | `Nome Poço Operador` | texto | Nome do poço no cadastro próprio do operador. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Campo` | `Campo` | texto | Nome do campo de produção onde foi perfurado o poço. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Operador` | `Operador` | texto | Nome fantasia do operador (concessionário). | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Número do Contrato` | `Número do Contrato` | texto | Número do contrato de concessão celebrado com a ANP. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Período` | `Período` | texto | Período (ano e mês, AAAA/MM). | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Óleo (bbl/dia)` | `Óleo (bbl/dia)` | texto | Volume de óleo, em barris por dia. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Condensado (bbl/dia)` | `Condensado (bbl/dia)` | texto | Volume de condensado, em barris por dia. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Petróleo (bbl/dia)` | `Petróleo (bbl/dia)` | texto | Volume de petróleo (óleo mais condensado), em barris por dia. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Gás Natural (Mm³/dia) Associado` | `Gás Natural (Mm³/dia) Associado` | texto | Volume de gás natural associado, em milhares de m³ por dia. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Gás Natural (Mm³/dia) Não Associado` | `Gás Natural (Mm³/dia) Não Associado` | texto | Volume de gás natural não associado, em milhares de m³ por dia. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Gás Natural (Mm³/dia) Gás Total` | `Gás Natural (Mm³/dia) Gás Total` | texto | Volume de gás natural total (associado mais não associado), em milhares de m³ por dia. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Volume Gás Royalties (Mm³/dia)` | `Volume Gás Royalties (Mm³/dia)` | texto | Volume de gás sobre o qual incidem royalties, em milhares de m³ por dia (no metadado da ANP o nome atual é `(m³/mês)` e a descrição diz `Mm³/dia`). | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Água (bbl/dia)` | `Água (bbl/dia)` | texto | Volume de água produzida, em barris por dia. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Instalação Destino` | `Instalação Destino` | texto | Nome da instalação destinatária dos volumes produzidos no poço. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Tipo Instalação` | `Tipo Instalação` | texto | Tipo da instalação destinatária (`UEP` ou `INSTALACAO EMB/DESEMB` na amostra de 2023). | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Tempo de Produção (hs por mês)` | `Tempo de Produção (hs por mês)` | texto | Número de horas que o poço produziu no mês. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Período da Carga` | `Período da Carga` | texto | Período (AAAA/MM) da carga cujas características do petróleo e do gás acompanham a linha; o metadado não descreve a coluna. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Corrente` | `Corrente` | texto | Denominação de um tipo de hidrocarboneto com características físico-químicas próprias, formado pela mistura de hidrocarbonetos de diferentes campos. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Grau API` | `Grau API` | texto | Grau API do óleo produzido. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Fração de Destilados Leves Corte` | `Fração de Destilados Leves Corte` | texto | Temperatura de corte da fração de destilados leves (texto, como `< 290ºC`). | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Fração de Destilados Leves Volume` | `Fração de Destilados Leves Volume` | texto | Percentual de destilados leves (texto com `%` e ponto decimal, como `34.8%`). | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Fração de Destilados Médios Corte` | `Fração de Destilados Médios Corte` | texto | Temperaturas de corte da fração de destilados médios (texto, como `290ºC a 380ºC`). | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Fração de Destilados Médios Volume` | `Fração de Destilados Médios Volume` | texto | Percentual de destilados médios (texto com `%` e ponto decimal). | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Fração de Destilados Pesados Corte` | `Fração de Destilados Pesados Corte` | texto | Temperatura de corte da fração de destilados pesados (texto, como `> 380ºC`). | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Fração de Destilados Pesados Volume` | `Fração de Destilados Pesados Volume` | texto | Percentual de destilados pesados (texto com `%` e ponto decimal). | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Metano` | `% em Volumes Metano` | texto | Percentual em volume de metano no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Etano` | `% em Volumes Etano` | texto | Percentual em volume de etano no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Propano` | `% em Volumes Propano` | texto | Percentual em volume de propano no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Iso-Butano` | `% em Volumes Iso-Butano` | texto | Percentual em volume de iso-butano no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Butano` | `% em Volumes Butano` | texto | Percentual em volume de butano no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Iso-Pentano` | `% em Volumes Iso-Pentano` | texto | Percentual em volume de iso-pentano no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes n-Pentano` | `% em Volumes n-Pentano` | texto | Percentual em volume de n-pentano no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Hexanos` | `% em Volumes Hexanos` | texto | Percentual em volume de hexanos no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Heptanos` | `% em Volumes Heptanos` | texto | Percentual em volume de heptanos no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Octanos` | `% em Volumes Octanos` | texto | Percentual em volume de octanos no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Nonanos` | `% em Volumes Nonanos` | texto | Percentual em volume de nonanos no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Decanos` | `% em Volumes Decanos` | texto | Percentual em volume de decanos no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Undecanos` | `% em Volumes Undecanos` | texto | Percentual em volume de undecanos no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Oxigênio` | `% em Volumes Oxigênio` | texto | Percentual em volume de oxigênio no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Nitrogênio` | `% em Volumes Nitrogênio` | texto | Percentual em volume de nitrogênio no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `% em Volumes Gás Carbônico` | `% em Volumes Gás Carbônico` | texto | Percentual em volume de gás carbônico no gás. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Densidade GLP Gás` | `Densidade GLP Gás` | texto | Densidade do GLP em forma gasosa, em kg/m³. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Densidade GLP Líquido` | `Densidade GLP Líquido` | texto | Densidade do GLP em forma líquida, em kg/m³. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `PCS GP (kJ/m³)` | `PCS GP (kJ/m³)` | texto | Poder calorífico superior do gás de pirólise (descrição do metadado), em kJ/m³. | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `Data de atualização` | `Data de atualização` | texto | Data de atualização do conjunto de dados de produção mensal por poço (DD/MM/AAAA). | — | 2020 a 2023-02 | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |
| `ambiente` | `ambiente` | texto | Ambiente do arquivo de origem dentro do ZIP: `mar`, `terra` ou `presal` (coluna acrescentada pelo conversor, a partir do nome do membro do ZIP). O pré-sal é um subconjunto de mar. | — | todo | `producao-poco-abertos`, `producao-poco-abertos-anual`, `producao-poco-abertos-anual-presal` e mais 1 |

## No lake

- Datasets `anp/producao-poco-abertos` (`ano=<ano>/mes=<mm>/producao-poco-da_<ano>-<mm>__<ano>_<mm>_producao_<ambiente>.parquet`), `anp/producao-poco-abertos-presal` (mesmo padrão), `anp/producao-poco-abertos-anual` (`ano=<ano>/producao-poco-da_<ano>__<ano>[_<mm>]_producao_<ambiente>.parquet`) e `anp/producao-poco-abertos-anual-presal`. Um Parquet por CSV do ZIP.
- Todas as colunas são texto; a coluna `ambiente` (`mar`, `terra` ou `presal`) é acrescentada pelo conversor a partir do nome do CSV dentro do ZIP.

## Cuidados de uso

- **Ponto de milhar e vírgula decimal.** Valores como `2.373,8445` aparecem em 3.269 das 9.672 linhas de mar de 2008 da amostra e nos arquivos mensais; troque o ponto por vazio e a vírgula por ponto antes do cast (`replace(replace(x, '.', ''), ',', '.')`). Nos ZIP do `ppg` o decimal é ponto, sem milhar.
- **Percentuais de destilados e cortes em texto.** `Fração de Destilados * Volume` vem como `34.8%` (ponto decimal e `%`) e `Corte` como `< 290ºC`, `290ºC a 380ºC`; o valor `%` sozinho e `< ºC` aparecem quando o dado falta. A composição do gás (`% em Volumes ...`) usa vírgula, sem o `%`.
- **Pré-sal é subconjunto de mar.** Não some o dataset `-presal` com o de mar.
- **Mais de uma linha por poço e mês.** Em janeiro de 2023, `(Nome Poço ANP, Período)` repete (5.909 pares distintos em 6.310 linhas, e 5.951 com a instalação), então a chave do dataset fica vazia e a soma por poço precisa ser confrontada com os totais da ANP.
- **Instalação vazia em parte das linhas.** `Instalação Destino` e `Tipo Instalação` têm lacunas (260 linhas de janeiro de 2023 sem `Tipo Instalação`) e não existem no ZIP de 2008 da amostra; `Tipo Instalação` assume `UEP` e `INSTALACAO EMB/DESEMB` em 2023, sem o termo `EMB/DESEMB` explicado no metadado.
- **Divergência de unidade no metadado.** O nome atual de `Volume Gás Royalties` é `(m³/mês)` no metadado, mas a descrição e o nome no arquivo dizem `(Mm³/dia)`. Os volumes são vazões diárias médias do mês, e `Tempo de Produção (hs por mês)` dá as horas produzidas.
- **Defasagem de dois meses e 2024 em diante fora.** Os dados saem no segundo mês depois do de produção; o fetcher não coleta os meses de 2024 em diante, que a ANP publica só na Consulta de Dados Públicos.
- **Dados pessoais.** Não há: nomes de poços, campos, instalações e empresas operadoras.

## Exemplos

Vazão de petróleo e de gás total somada por ambiente em janeiro de 2023 (terra e mar; o pré-sal está em outro dataset). As colunas são texto com ponto de milhar e vírgula decimal:

```python
import duckdb

duckdb.sql("""
    SELECT ambiente,
           count(*) AS linhas,
           round(sum(replace(replace("Petróleo (bbl/dia)", '.', ''), ',', '.')::DOUBLE)) AS petroleo_bbl_dia,
           round(sum(replace(replace("Gás Natural (Mm³/dia) Gás Total", '.', ''), ',', '.')::DOUBLE)) AS gas_mil_m3_dia
    FROM read_parquet('lake/anp/producao-poco-abertos/ano=2023/mes=01/*.parquet', union_by_name = true)
    GROUP BY ambiente
    ORDER BY ambiente
""").show()
```

## Referências

- Produção de petróleo e gás natural por poço (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-poco
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-petroleo-e-gas-natural-por-poco/metadados-dados-producao-poco.pdf e `metadados-dados-producao-poco-2005-2017.pdf`, na mesma pasta
