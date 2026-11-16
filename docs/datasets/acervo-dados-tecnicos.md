---
dataset:
  id: acervo-dados-tecnicos
  fonte: anp
  titulo: Acervo de dados técnicos (BDEP)
  resumo: 'Listagens do acervo de dados técnicos da ANP: programas geofísicos, dados e levantamentos geoquímicos, estudos, dados do PROMAR e poços e sísmicas que se tornaram públicos a cada ano.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acervo-de-dados-tecnicos
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'varia por tabela: «conforme a demanda» para programas geofísicos, geoquímica, estudos e PROMAR; anual para as listagens públicas desde 2023; série histórica, sem atualização salvo correções, para 2019 a 2022'
  cobertura:
    inicio: '1961'
    fim: '2026'
  unidade: 'uma entrada do acervo: um programa geofísico, um dado ou levantamento geoquímico, um estudo, um item do PROMAR, um poço ou um levantamento sísmico (conforme a tabela)'
  granularidade:
    espacial: bacia sedimentar, bloco, campo, estado; coordenadas latitude e longitude nos dados geoquímicos e poços
    temporal: 'data de aquisição (programas: de 1961 a 2026-07 no arquivo; levantamentos geoquímicos: de 1999 a 2020), ano de conclusão (estudos) e ano em que o dado se tornou público (listagens de 2019 a 2023)'
  formato_bruto: 15 CSV, separador ponto e vírgula, UTF-8 com BOM ou UTF-16, uma linha de cabeçalho; metadados em PDF por tabela
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 129
  unidades_de_medida:
    Topo (m): m (metros)
    Base (m): m (metros)
    LATITUDE: graus decimais
    LONGITUDE: graus decimais
    VOLUME: GB (gigabytes)
    TAMANHO (GB): GB (gigabytes)
    LATITUDE_BASE_DD: graus decimais
    LONGITUDE_BASE_DD: graus decimais
    PROFUNDIDADE_VERTICAL_M: m (metros)
    PROFUNDIDADE_SONDADOR_M: m (metros)
    PROFUNDIDADE_MEDIDA_M: m (metros)
    MESA_ROTATIVA: m (metros)
    COTA_ALTIMETRICA_M: m (metros)
    LAMINA_D_AGUA_M: m (metros)
  dados_pessoais:
  - coluna: OPERADOR
    categoria: nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo
  - coluna: EMPRESA
    categoria: nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo
  - coluna: E.A.D
    categoria: nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo
  - coluna: Operadora
    categoria: nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo
  eras:
  - desde: '2019'
    mudanca: listagens de poços públicos de 2019 a 2021 com `INICIO`, `TERMINO` e `CONCLUSAO` com hora (`dd/mm/aaaa 00:00`) e `TIPO` em texto; só o arquivo de 2019 tem `TITULARIDADE`
  - desde: '2022'
    mudanca: 'poços públicos de 2022 e 2023: datas sem hora; `TIPO` passa a trazer o código da categoria (`7`, `8`, `9`, `1`) em vez do texto'
  - desde: '2023'
    mudanca: 'poços públicos de 2023: entra `ATINGIU_PRESAL`; sísmicos públicos de 2023 passam a ter a estrutura dos programas geofísicos (15 colunas)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Acervo de dados técnicos (BDEP)

## Resumo

O acervo de dados técnicos da ANP, armazenado no BDEP (Banco de Dados de Exploração e Produção), reúne dados de poços, dados sísmicos e não sísmicos, levantamentos geoquímicos, estudos de interpretação e seus relatórios. A página dos dados abertos publica só as informações sobre os dados (metadados do acervo), não os dados em si. Os dados técnicos se tornam públicos ao fim de um período de sigilo, de dois a dez anos conforme o tipo, e desde 2019 a ANP publica a cada ano as listagens de poços e sísmicas que se tornaram públicos. O grupo traz 15 tabelas: programas geofísicos, dados geoquímicos, levantamentos geoquímicos, estudos, dados marítimos do PROMAR, e as listagens anuais de poços públicos e de levantamentos sísmicos públicos de 2019 a 2023.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/acervo-dados-tecnicos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acervo-de-dados-tecnicos |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | varia por tabela: «conforme a demanda» para programas geofísicos, geoquímica, estudos e PROMAR; anual para as listagens públicas desde 2023; série histórica, sem atualização salvo correções, para 2019 a 2022 |
| Cobertura | 1961 a 2026 |
| Unidade (uma linha) | uma entrada do acervo: um programa geofísico, um dado ou levantamento geoquímico, um estudo, um item do PROMAR, um poço ou um levantamento sísmico (conforme a tabela) |
| Granularidade | espacial: bacia sedimentar, bloco, campo, estado; coordenadas latitude e longitude nos dados geoquímicos e poços; temporal: data de aquisição (programas: de 1961 a 2026-07 no arquivo; levantamentos geoquímicos: de 1999 a 2020), ano de conclusão (estudos) e ano em que o dado se tornou público (listagens de 2019 a 2023) |
| Formato bruto | 15 CSV, separador ponto e vírgula, UTF-8 com BOM ou UTF-16, uma linha de cabeçalho; metadados em PDF por tabela |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 129 |
| Unidades de medida | `Topo (m)`: m (metros); `Base (m)`: m (metros); `LATITUDE`: graus decimais; `LONGITUDE`: graus decimais; `VOLUME`: GB (gigabytes); `TAMANHO (GB)`: GB (gigabytes); `LATITUDE_BASE_DD`: graus decimais; `LONGITUDE_BASE_DD`: graus decimais; `PROFUNDIDADE_VERTICAL_M`: m (metros); `PROFUNDIDADE_SONDADOR_M`: m (metros); `PROFUNDIDADE_MEDIDA_M`: m (metros); `MESA_ROTATIVA`: m (metros); `COTA_ALTIMETRICA_M`: m (metros); `LAMINA_D_AGUA_M`: m (metros) |
| Dados pessoais | `OPERADOR` (nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo); `EMPRESA` (nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo); `E.A.D` (nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo); `Operadora` (nome de empresa (pessoa jurídica) operadora, contratada ou responsável pelo estudo) |
| Eras | 2019: listagens de poços públicos de 2019 a 2021 com `INICIO`, `TERMINO` e `CONCLUSAO` com hora (`dd/mm/aaaa 00:00`) e `TIPO` em texto; só o arquivo de 2019 tem `TITULARIDADE`; 2022: poços públicos de 2022 e 2023: datas sem hora; `TIPO` passa a trazer o código da categoria (`7`, `8`, `9`, `1`) em vez do texto; 2023: poços públicos de 2023: entra `ATINGIU_PRESAL`; sísmicos públicos de 2023 passam a ter a estrutura dos programas geofísicos (15 colunas) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Dados Técnicos (SDT), a partir do BDEP; contato geofisica_sdt@anp.gov.br e sdt_crf@anp.gov.br (metadados da ANP). As listagens públicas por ano têm contato geoprocessamento@anp.gov.br.
- **Catálogo do fetcher:** 15 arquivos, `adt-programas-geofisicos`, `adt-dados-geoquimicos`, `adt-levantamentos-geoquimicos`, `adt-estudos`, `adt-promar`, `adt-pocos-publicos-2019` a `-2023` e `adt-sismicos-publicos-2019` a `-2023` (conferido em 2026-11-15). A amostra do lake tinha 6; os outros 9 foram baixados e convertidos à parte.
- **Datas de atualização (página oficial):** programas geofísicos, 14/8/2026; PROMAR, 22/7/2026; dados de geoquímica e estudos, 6/8/2021; levantamentos geoquímicos, 20/4/2022; metadados do acervo, 11/3/2026.
- **Poços públicos:** a tabela de poços do acervo está no sistema de consulta de dados públicos da ANP, fora do conjunto; as listagens por ano aqui incluem só os que se tornaram públicos naquele ano.
- **Metadados:** cada tabela tem um PDF com a ficha e as colunas. Há metadados para poços (2023 e 2019-2022), sísmicos (2023, 2022, 2021 e 2019-2020), programas geofísicos, geoquímica, levantamentos, estudos e PROMAR.

## Conteúdo

As 15 tabelas e seus formatos:

| Arquivo no lake | Conteúdo | Linhas | Colunas |
|---|---|---|---|
| `adt-programas-geofisicos` | programas geofísicos não sísmicos e sísmicos (aquisição, tecnologia, confidencialidade e bloco) | 3.908 | 15 |
| `adt-dados-geoquimicos` | análises geoquímicas de poço, com o tipo de análise marcado em colunas `X` | 4.665 | 36 |
| `adt-levantamentos-geoquimicos` | levantamentos geoquímicos (nome, bacia, natureza, datas, ambiente e shapefile) | 69 | 8 |
| `adt-estudos` | estudos geológicos, geofísicos e geoquímicos do acervo | 43 | 7 |
| `adt-promar` | dados técnicos marítimos gratuitos do PROMAR (poços e sísmica 2D e 3D, com tamanho em GB) | 5.417 | 4 |
| `adt-pocos-publicos-2019` a `-2023` | poços perfurados que se tornaram públicos em cada ano | 213, 218, 174, 141 e 106 | 58 a 59 |
| `adt-sismicos-publicos-2019` a `-2023` | levantamentos sísmicos que se tornaram públicos em cada ano | 138, 340, 225, 155 e 52 | 5, 7, 7, 5 e 15 |

- **Ano nos nomes dos arquivos de poços e sísmicas** é o ano em que o dado se tornou público, e não o ano da perfuração ou da aquisição: o arquivo de poços de 2023 tem poços concluídos em 2021 (`CONCLUSAO` em 2021) e o de 2022, poços concluídos em 2020, na amostra.
- **Programas geofísicos:** 3.908 programas, 3.610 nomes distintos; a coluna `Tipo` é `Exclusivo` (1.595), `Não-Exclusivo` (1.015), `Exclusivo (Pré-98)` (1.184) ou `de Fomento` (114); `Inicio` vai de 01/01/1961 a 31/07/2026 e `Público em`, até 25/02/2041.
- **Dados geoquímicos:** 4.665 linhas para 3.598 poços; `Carbono Orgânico Total` e `Pirólise` são as análises mais marcadas (3.711 e 3.704 linhas).
- **PROMAR:** 5.417 itens (poços e sísmica 2D e 3D) das bacias marítimas Camamu-Almada, Campos, Ceará, Cumuruxatiba, Espírito Santo, Jequitinhonha, Potiguar, Santos e Sergipe-Alagoas.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | 15 arquivos, de 4 a 59 colunas |

## Variáveis

As descrições vêm dos metadados da ANP de cada tabela; nos casos em que o nome da coluna do arquivo difere do dicionário (por exemplo, `Tipo` em programas geofísicos, que o dicionário chama de «Natureza»), vale a descrição do dicionário para o campo correspondente. Colunas sem dicionário têm descrição deduzida do nome e dos valores. A coluna *Arquivos* diz em quais tabelas a coluna aparece (os poços e sísmicas de cada ano têm os nomes `adt-pocos-publicos-AAAA` e `adt-sismicos-publicos-AAAA`). Os nomes de coluna que diferem só na caixa (`TIPO` e `Tipo`, `BACIA` e `Bacia`) são colunas distintas no lake. O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Poço` | `Poço` | texto | Nome do poço em que foram adquiridos os dados geoquímicos | — | — | `adt-dados-geoquimicos` |
| `Extensão do Arquivo` | `Extensão do Arquivo` | texto | Extensão do arquivo que contém os dados (pdf, xls*, doc*, ppt*, png, jpg) | — | — | `adt-dados-geoquimicos` |
| `Fonte dos Dados` | `Fonte dos Dados` | texto | Local onde o dado está armazenado na ANP: LITOTECA (repositório de dados digitais oriundos de amostras de rochas e fluidos) ou SIGEP | — | — | `adt-dados-geoquimicos` |
| `Tipo de Geoquímica` | `Tipo de Geoquímica` | texto | Tipo de dado geoquímico: GEOQUIMICADEROCHA ou GEOQUIMICADEFLUIDO | — | — | `adt-dados-geoquimicos` |
| `Topo (m)` | `Topo (m)` | texto | Profundidade mínima do intervalo de aquisição de dados, em metros (vírgula decimal) | — | — | `adt-dados-geoquimicos` |
| `Base (m)` | `Base (m)` | texto | Profundidade máxima do intervalo de aquisição de dados, em metros (vírgula decimal) | — | — | `adt-dados-geoquimicos` |
| `Cromatografia Gasosa` | `Cromatografia Gasosa` | texto | Indica se houve análise de cromatografia gasosa (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Cromatografia Líquida` | `Cromatografia Líquida` | texto | Indica se houve análise de cromatografia líquida (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Relatório` | `Relatório` | texto | Indica se houve elaboração de relatório das análises (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Análise de Óleo` | `Análise de Óleo` | texto | Indica se houve análise de óleo (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Análise de Gás` | `Análise de Gás` | texto | Indica se houve análise de gás (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Análise de Fluidos` | `Análise de Fluidos` | texto | Indica se houve análise de fluidos (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Análise de Água` | `Análise de Água` | texto | Indica se houve análise de água (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Biomarcadores` | `Biomarcadores` | texto | Indica se houve análise de biomarcadores (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Aromáticos` | `Aromáticos` | texto | Indica se houve análise de aromáticos (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Saturados` | `Saturados` | texto | Indica se houve análise de saturados (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Isótopos` | `Isótopos` | texto | Indica se houve análise de isótopos (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Espectrometria de Massas` | `Espectrometria de Massas` | texto | Indica se houve análise de espectrometria de massas (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Diamantoides` | `Diamantoides` | texto | Indica se houve análise de diamantoides (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Carbono Orgânico Total` | `Carbono Orgânico Total` | texto | Indica se houve análise de carbono orgânico total (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Pirólise` | `Pirólise` | texto | Indica se houve análise de pirólise (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Inclusões Fluidas` | `Inclusões Fluidas` | texto | Indica se houve análise de inclusões fluidas (`X` quando sim); vazia em todas as linhas do arquivo | — | — | `adt-dados-geoquimicos` |
| `Sumário de Óleo Cru` | `Sumário de Óleo Cru` | texto | Indica se houve análise de sumário de óleo cru (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `PVT` | `PVT` | texto | Indica se houve análise de PVT (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Re/Os de Asfaltenos` | `Re/Os de Asfaltenos` | texto | Indica se houve análise de Re/Os de asfaltenos (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Litogeoquímica` | `Litogeoquímica` | texto | Indica se houve análise de litogeoquímica (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Reflectância de Vitrinita` | `Reflectância de Vitrinita` | texto | Indica se houve análise de reflectância de vitrinita (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `Viscosidade` | `Viscosidade` | texto | Indica se houve análise de viscosidade (`X` quando sim) | — | — | `adt-dados-geoquimicos` |
| `CADASTRO` | `CADASTRO` | texto | Em `dados-geoquimicos`: código único de cadastro do dado geoquímico. Em `pocos-publicos`: conjunto de algarismos que identifica o poço de forma unívoca e permanente (código API) | — | — | `adt-dados-geoquimicos`, `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020` e mais 3 |
| `OPERADOR` | `OPERADOR` | texto | Operador (concessionário) responsável pela aquisição ou pelo poço (nome fantasia) | — | — | `adt-dados-geoquimicos`, `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020` e mais 3 |
| `ESTADO` | `ESTADO` | texto | Sigla do estado onde se localiza o poço perfurado (em `pocos-publicos`, onde a perfuração foi iniciada) | — | — | `adt-dados-geoquimicos`, `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020` e mais 3 |
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar onde se situa o poço, o estudo ou o dado (`estudos` e `promar` também usam esta coluna) | — | — | `adt-dados-geoquimicos`, `adt-estudos`, `adt-pocos-publicos-2019` e mais 5 |
| `CAMPO` | `CAMPO` | texto | Nome do campo de produção onde se situa o poço (quando aplicável) | — | — | `adt-dados-geoquimicos`, `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020` e mais 3 |
| `TITULARIDADE` | `TITULARIDADE` | texto | Indica se o dado é Confidencial (em período de sigilo, com acesso restrito) ou Público, acessível a terceiros nos termos da norma vigente | — | — | `adt-dados-geoquimicos`, `adt-estudos`, `adt-pocos-publicos-2019` |
| `LATITUDE` | `LATITUDE` | texto | Latitude, em notação decimal, da coordenada geográfica do topo do poço (vírgula decimal) | — | — | `adt-dados-geoquimicos` |
| `LONGITUDE` | `LONGITUDE` | texto | Longitude, em notação decimal, da coordenada geográfica do topo do poço (vírgula decimal) | — | — | `adt-dados-geoquimicos` |
| `DATUM` | `DATUM` | texto | Sistema geodésico de referência das coordenadas; atualmente só o SIRGAS2000 é adotado no Brasil | — | — | `adt-dados-geoquimicos` |
| `DIRECAO` | `DIRECAO` | texto | Direção de perfuração do poço: vertical, direcional ou horizontal | — | — | `adt-dados-geoquimicos`, `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020` e mais 3 |
| `NOME DO ESTUDO` | `NOME DO ESTUDO` | texto | Título do estudo geológico, geofísico ou geoquímico | — | — | `adt-estudos` |
| `ESTUDO` | `ESTUDO` | texto | Tipo de estudo: Geológico, Geofísico, Geoquímico ou Misto | — | — | `adt-estudos` |
| `EMPRESA` | `EMPRESA` | texto | Nome fantasia ou sigla da empresa ou instituição responsável pelo estudo | — | — | `adt-estudos` |
| `NATUREZA DA AQUISIÇÃO` | `NATUREZA DA AQUISIÇÃO` | texto | Tipo de aquisição: Exclusivo, Não Exclusivo ou Fomento | — | — | `adt-estudos` |
| `DATA CONCLUSÃO` | `DATA CONCLUSÃO` | texto | Ano de conclusão do estudo | — | — | `adt-estudos` |
| `Nome` | `Nome` | texto | Nome do programa geofísico (programas geofísicos e sísmicos de 2023) ou do levantamento geoquímico (levantamentos) | — | — | `adt-levantamentos-geoquimicos`, `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Bacia` | `Bacia` | texto | Bacia onde ocorreu o levantamento ou o programa; `(múltiplas)` ou `(não informada)` em casos especiais | — | — | `adt-levantamentos-geoquimicos`, `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Natureza da atividade` | `Natureza da atividade` | texto | Tipo de aquisição: Exclusivo, Não-Exclusivo ou de Fomento | — | — | `adt-levantamentos-geoquimicos` |
| `Início Aquisição` | `Início Aquisição` | texto | Data de início da aquisição (dd/mm/aaaa) | — | — | `adt-levantamentos-geoquimicos` |
| `Término Aquisição` | `Término Aquisição` | texto | Data de término da aquisição (dd/mm/aaaa) | — | — | `adt-levantamentos-geoquimicos` |
| `Ambiente` | `Ambiente` | texto | Ambiente da aquisição: Terrestre ou Marítimo | — | — | `adt-levantamentos-geoquimicos` |
| `Confidencialidade` | `Confidencialidade` | texto | Indica se o programa ou levantamento é Confidencial (em sigilo) ou Público | — | — | `adt-levantamentos-geoquimicos`, `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Shape` | `Shape` | texto | Indica se o shapefile de levantamentos geoquímicos registra o levantamento (`Sim` ou `Não`) | — | — | `adt-levantamentos-geoquimicos` |
| `POCO` | `POCO` | texto | Nome do poço para a ANP, conforme a Resolução ANP nº 699/2017 (símbolos alfanuméricos que o identificam) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `POCO_OPERADOR` | `POCO_OPERADOR` | texto | Nome do poço no cadastro próprio do operador | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `BLOCO` | `BLOCO` | texto | Nome do bloco exploratório onde se situa o poço, quando aplicável | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `SIG_CAMPO` | `SIG_CAMPO` | texto | Sigla do campo de produção, quando aplicável | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TERRA_MAR` | `TERRA_MAR` | texto | Ambiente da perfuração: T (terra) ou M (mar) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `POCO_POS_ANP` | `POCO_POS_ANP` | texto | `S`: poço posterior à criação da ANP (pós-98); `N`: poço anterior (pré-98) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TIPO` | `TIPO` | texto | Em `pocos-publicos`: tipo de poço (Exploratório, categorias 1 a 6; Explotatório, 7 e 8; Especial, 9; Estocagem, 10), que nos arquivos de 2022 e 2023 vem como o código da categoria (`7`, `8`, `9`, `1`) e, em 2020, vazio em 203 de 218 linhas. Em `sismicos-publicos` 2019 a 2022: tipo de levantamento (2D ou 3D). Em `promar`: tipo do dado (POÇO, SISMICA_2D ou SISMICA_3D) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 7 |
| `CATEGORIA` | `CATEGORIA` | texto | Finalidade principal original do poço (há dez categorias; por exemplo, Pioneiro, Desenvolvimento, Injeção, Especial) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `RECLASSIFICACAO` | `RECLASSIFICACAO` | texto | Reclassificação do poço, quando aplicável (por exemplo, `EXTENSÃO PARA GÁS NATURAL`, `PRODUTOR COMERCIAL`) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `SITUACAO` | `SITUACAO` | texto | Qualificação do poço segundo o estado mecânico atual e a condição operacional (por exemplo, `PRODUZINDO`, `ARRASADO`) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `INICIO` | `INICIO` | texto | Data de início da perfuração do poço, quando a broca começou a avançar em subsuperfície (dd/mm/aaaa; nos arquivos de 2019 a 2021 com hora) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TERMINO` | `TERMINO` | texto | Data de término da perfuração, quando se atingiu a profundidade final sem perspectiva de continuidade | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `CONCLUSAO` | `CONCLUSAO` | texto | Data de conclusão do poço, quando terminaram as atividades diretamente relacionadas à perfuração | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `LATITUDE_BASE_4C` | `LATITUDE_BASE_4C` | texto | Latitude da coordenada da base do poço em graus, minutos e segundos (`-12:29:43,653`) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `LONGITUDE_BASE_4C` | `LONGITUDE_BASE_4C` | texto | Longitude da coordenada da base do poço em graus, minutos e segundos | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `LATITUDE_BASE_DD` | `LATITUDE_BASE_DD` | texto | Latitude da coordenada da base do poço em notação decimal (vírgula decimal) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `LONGITUDE_BASE_DD` | `LONGITUDE_BASE_DD` | texto | Longitude da coordenada da base do poço em notação decimal (vírgula decimal) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `DATUM_HORIZONTAL` | `DATUM_HORIZONTAL` | texto | Sistema geodésico de referência das coordenadas (SIRGAS2000) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TIPO_DE_COORDENADA_DE_BASE` | `TIPO_DE_COORDENADA_DE_BASE` | texto | Indica se a coordenada da base de perfuração é definitiva ou provisória | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PROFUNDIDADE_VERTICAL_M` | `PROFUNDIDADE_VERTICAL_M` | texto | Profundidade final vertical da perfuração, em metros (vírgula decimal; pode ser negativa em relação ao nível do mar) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PROFUNDIDADE_SONDADOR_M` | `PROFUNDIDADE_SONDADOR_M` | texto | Profundidade final do poço pelo sondador, em metros | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PROFUNDIDADE_MEDIDA_M` | `PROFUNDIDADE_MEDIDA_M` | texto | Profundidade medida da base do intervalo perfilado, em metros | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `REFERENCIA_DE_PROFUNDIDADE` | `REFERENCIA_DE_PROFUNDIDADE` | texto | Referência de profundidade do sondador, sempre MR (mesa rotativa) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `MESA_ROTATIVA` | `MESA_ROTATIVA` | texto | Elevação da mesa rotativa em relação ao nível médio do mar, em metros | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `COTA_ALTIMETRICA_M` | `COTA_ALTIMETRICA_M` | texto | Altitude acima do nível médio do mar, em metros | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `LAMINA_D_AGUA_M` | `LAMINA_D_AGUA_M` | texto | Profundidade da lâmina d'água na perfuração, em metros, quando aplicável | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `DATUM_VERTICAL` | `DATUM_VERTICAL` | texto | Datum vertical, sempre NM (nível médio do mar) | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `UNIDADE_ESTRATIGRAFICA` | `UNIDADE_ESTRATIGRAFICA` | texto | Caracterização hierarquizada de unidades geológicas; vazia em todas as linhas dos arquivos da amostra | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `GEOLOGIA_GRUPO_FINAL` | `GEOLOGIA_GRUPO_FINAL` | texto | Grupo estratigráfico final: unidade formal de categoria imediatamente superior à formação | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `GEOLOGIA_FORMACAO_FINAL` | `GEOLOGIA_FORMACAO_FINAL` | texto | Formação estratigráfica final, unidade fundamental da nomenclatura formal | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `GEOLOGIA_MEMBRO_FINAL` | `GEOLOGIA_MEMBRO_FINAL` | texto | Membro estratigráfico final, unidade formal imediatamente abaixo da formação | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `CDPE` | `CDPE` | texto | Indica se existe o dado CDPE (Consolidação de Documentos de Poços Exploratórios); `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `AGP` | `AGP` | texto | Indica se existe o dado AGP (Arquivo Geral de Poço); `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PC` | `PC` | texto | Indica se existe o Perfil Composto; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PAG` | `PAG` | texto | Indica se existe o PAG (Perfil de Acompanhamento Geológico); `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PERFIS_CONVENCIONAIS` | `PERFIS_CONVENCIONAIS` | texto | Indica se existem perfis de registro contínuo, sem avanço da perfuração; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `DURANTE_PERFURACAO` | `DURANTE_PERFURACAO` | texto | Indica se existem dados de perfilagem durante a perfuração (LWD); `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PERFIS_DIGITAIS` | `PERFIS_DIGITAIS` | texto | Indica se existem perfis digitais do poço; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PERFIS_PROCESSADOS` | `PERFIS_PROCESSADOS` | texto | Indica se existem perfis processados; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `PERFIS_ESPECIAIS` | `PERFIS_ESPECIAIS` | texto | Indica se existem perfis de amostragem discreta (sísmica de poço, testes a cabo, registro de pressão, canhoneio); `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `AMOSTRA_LATERAL` | `AMOSTRA_LATERAL` | texto | Indica se foi coletada amostra lateral; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `SISMICA` | `SISMICA` | texto | Indica se foi feita aquisição de sísmica de poço; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TABELA_TEMPO_PROFUNDIDADE` | `TABELA_TEMPO_PROFUNDIDADE` | texto | Indica se existe a tabela de relação tempo x profundidade; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `DADOS_DIRECIONAIS` | `DADOS_DIRECIONAIS` | texto | Indica se existem dados direcionais (profundidade, inclinação, azimute, afastamentos, coordenadas); `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TESTE_A_CABO` | `TESTE_A_CABO` | texto | Indica se existem dados de teste a cabo; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TESTE_DE_FORMACAO` | `TESTE_DE_FORMACAO` | texto | Indica se existe o dado de Teste de Formação; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `CANHONEIO` | `CANHONEIO` | texto | Indica se existem dados de canhoneio; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `TESTEMUNHO` | `TESTEMUNHO` | texto | Indica se foi coletado testemunho no poço; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `GEOQUIMICA` | `GEOQUIMICA` | texto | Indica se existem dados de análise geoquímica de poço; `Existe` ou vazio | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `SIG_SONDA` | `SIG_SONDA` | texto | Sigla da sonda usada na perfuração | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `NOM_SONDA` | `NOM_SONDA` | texto | Nome da sonda usada na perfuração | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `DHA_ATUALIZACAO` | `DHA_ATUALIZACAO` | texto | Data (com hora, nos arquivos antigos) de atualização do conjunto de dados | — | — | `adt-pocos-publicos-2019`, `adt-pocos-publicos-2020`, `adt-pocos-publicos-2021` e mais 2 |
| `ATINGIU_PRESAL` | `ATINGIU_PRESAL` | texto | Indica se a perfuração atingiu o pré-sal: `S` atingiu, `N` não atingiu, `I` não se aplica (poço terrestre); só no arquivo de 2023 | — | — | `adt-pocos-publicos-2023` |
| `Categoria` | `Categoria` | texto | Categoria do programa: Levantamento Geofísico ou Reprocessamento | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Tipo` | `Tipo` | texto | Tipo de aquisição do programa geofísico: Exclusivo, Exclusivo (Pré-98), Não-Exclusivo ou de Fomento (os metadados dos programas geofísicos chamam esta coluna de «Natureza») | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Autorização` | `Autorização` | texto | Autorização correspondente (por exemplo, `Aut. 12/2018`), exclusiva de dados exclusivos | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Inicio` | `Inicio` | texto | Data de início da aquisição ou das atividades (dd/mm/aaaa) | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Término Real` | `Término Real` | texto | Data de término da aquisição ou das atividades (dd/mm/aaaa) | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Público em` | `Público em` | texto | Data em que o programa se tornou (ou se tornará) público, findo o período de sigilo (dd/mm/aaaa) | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Ato Normativo` | `Ato Normativo` | texto | Ato normativo específico aplicado ao período de sigilo (`Res. 11/2011`, `Res. 1/2015`) ou `Normal`, sem ato específico | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Tecnologia` | `Tecnologia` | texto | Tecnologia geofísica utilizada (por exemplo, Sísmica 2D, Sísmica 3D, Gravimetria, Magnetometria, Eletromagnético) | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Bloco` | `Bloco` | texto | Bloco exploratório correspondente (`múltiplos` ou `(não informado)` em casos especiais) | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Campo` | `Campo` | texto | Campo de produção correspondente (`múltiplos` ou `(não informado)` em casos especiais) | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `E.A.D` | `E.A.D` | texto | Empresa de Aquisição de Dados (EAD) ou operadora que realizou as atividades | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `Operadora` | `Operadora` | texto | Operadora que contratou a EAD para o levantamento exclusivo (vazia nos demais) | — | — | `adt-programas-geofisicos`, `adt-sismicos-publicos-2023` |
| `NOME` | `NOME` | texto | Nome do dado de poço ou do programa sísmico (PROMAR) | — | — | `adt-promar` |
| `TAMANHO (GB)` | `TAMANHO (GB)` | texto | Tamanho do dado, em gigabytes (vírgula decimal) | — | — | `adt-promar` |
| `DT_GERACAO` | `DT_GERACAO` | texto | Data de geração do conjunto de dados (dd/mm/aaaa) | — | — | `adt-sismicos-publicos-2019`, `adt-sismicos-publicos-2020`, `adt-sismicos-publicos-2021` |
| `VOLUME` | `VOLUME` | texto | Tamanho do dado sísmico, em gigabytes (vírgula decimal); `Não informado` em parte das linhas de 2021 | — | — | `adt-sismicos-publicos-2019`, `adt-sismicos-publicos-2020`, `adt-sismicos-publicos-2021` |
| `PROJETO` | `PROJETO` | texto | Nome do projeto sísmico, associado ao levantamento | — | — | `adt-sismicos-publicos-2019`, `adt-sismicos-publicos-2020`, `adt-sismicos-publicos-2021` e mais 1 |
| `TIPO_PROCESSAMENTO` | `TIPO_PROCESSAMENTO` | texto | Tipo de processamento aplicado ao dado sísmico (por exemplo, Field Data, PSTM, PSDM) | — | — | `adt-sismicos-publicos-2019`, `adt-sismicos-publicos-2020` |
| `CONFIDENCIALIDADE` | `CONFIDENCIALIDADE` | texto | «Público» ou «Público em <ano>» (todos os dados da listagem de 2019 e 2020 são públicos) | — | — | `adt-sismicos-publicos-2019`, `adt-sismicos-publicos-2020` |
| `LEVANTAMENTO` | `LEVANTAMENTO` | texto | Nome do levantamento sísmico | — | — | `adt-sismicos-publicos-2019`, `adt-sismicos-publicos-2020` |
| `TIPO_PROC` | `TIPO_PROC` | texto | Tipo de processamento aplicado ao dado sísmico (por exemplo, Field Data, PSTM); nome da coluna nos arquivos de 2021 e 2022 | — | — | `adt-sismicos-publicos-2021`, `adt-sismicos-publicos-2022` |
| `PROGRAMA SÍSMICO` | `PROGRAMA SÍSMICO` | texto | Nome do programa sísmico (arquivo de 2021); descrição deduzida do nome e dos valores, que repetem os de `PROJETO`; não consta dos metadados | — | — | `adt-sismicos-publicos-2021` |
| `PÚBLICO EM` | `PÚBLICO EM` | texto | Data em que o dado se torna público (dd/mm/aaaa; arquivo de 2021); descrição deduzida do nome | — | — | `adt-sismicos-publicos-2021` |
| `CONF` | `CONF` | texto | Titularidade do dado: Público ou Confidencial (arquivo de 2022) | — | — | `adt-sismicos-publicos-2022` |
| `LEVANT` | `LEVANT` | texto | Nome do levantamento sísmico (nome da coluna no arquivo de 2022) | — | — | `adt-sismicos-publicos-2022` |

## No lake

- Dataset `anp/acervo-dados-tecnicos`, sem partições; um Parquet por tabela, no padrão `adt-<tabela>.parquet`.
- Todas as colunas são texto. Os números usam vírgula decimal, e as datas, `dd/mm/aaaa` (com ` 00:00` nas listagens de poços de 2019 a 2021).
- As colunas de presença de dados dos poços (`CDPE`, `PC`, `SISMICA`, etc.) trazem `Existe` ou vazio.

## Cuidados de uso

- **Não são os dados em si.** As tabelas listam o que existe no acervo (e o que está público), com bacia, poço e datas; os dados técnicos exigem pedido de acesso à ANP.
- **A estrutura muda entre tabelas e anos.** As listagens de sísmicos têm quatro estruturas (2019 e 2020, 2021, 2022 e 2023); coalesça `TIPO_PROCESSAMENTO`/`TIPO_PROC`, `LEVANTAMENTO`/`LEVANT`, `CONFIDENCIALIDADE`/`CONF` e `PÚBLICO EM`/`Público em` antes de empilhar. O arquivo de 2022 tem só 5 colunas, sem datas nem volume.
- **`TIPO` em poços é inconsistente.** Em 2020 a coluna vem vazia em 203 de 218 linhas, e em 2022 e 2023 traz o código da categoria (`7`, `8`, `9`, `1`) em vez do texto Exploratório/Explotatório; use `CATEGORIA` ou o primeiro dígito do nome do poço para classificar.
- **Campos de presença.** A ausência de dado aparece como campo vazio; só os campos de presença trazem a palavra `Existe`.
- **`Bacia`, `Bloco`, `Campo` com marcadores** `(múltiplas)`, `(não informado)` e `(não informada)` em programas geofísicos e sísmicos de 2023; filtre antes de ligar a tabelas de bacias.
- **Datas e números em texto** (`dd/mm/aaaa`, `1.935,00`, `-5,418273000000`); converta antes de calcular. Os valores de profundidade podem ser negativos em relação ao nível do mar.
- **Dado geoquímico antigo.** A tabela de dados geoquímicos foi publicada em 26/03/2018, antes do padrão ANP3 (Resolução ANP nº 725/2018, sucedido pela nº 916/2023); atualização em 6/8/2021.
- **Confidencialidade.** A coluna de titularidade indica se o dado ainda está em sigilo; as listagens públicas por ano só têm dados que já se tornaram públicos.
- **Nomes de empresas.** Operador, operadora, EAD e empresa de estudos são pessoas jurídicas; o acervo não traz pessoas físicas.

## Exemplos

Número de poços das listagens públicas por ano (arquivo) e por ambiente (terra ou mar), nos arquivos de 2020 a 2023:

```python
import duckdb

duckdb.sql("""
    SELECT regexp_extract(filename, 'pocos-publicos-([0-9]{4})', 1) AS ano_publico,
           "TERRA_MAR" AS ambiente, count(*) AS pocos
    FROM read_parquet('lake/anp/acervo-dados-tecnicos/adt-pocos-publicos-202*.parquet', filename = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ano_publico, ambiente
""").show()
```

## Referências

- Dados abertos da ANP, Acervo de Dados Técnicos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acervo-de-dados-tecnicos
- Metadados: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-acervo-de-dados-tecnicos/ (por exemplo, `metadados-pocos-publicos-1.pdf`, `metadados-sismicos-publicos-1.pdf`, `metadados-cgu-shapefile-programas-geofisicos.pdf`, `metadados-tabela-dados-geoquimica.pdf`)
- Dados técnicos que se tornam públicos no ano (ANP): https://www.gov.br/anp/pt-br/assuntos/exploracao-e-producao-de-oleo-e-gas/dados-tecnicos/mapas-e-p/dados-tecnicos-publicos-ano
