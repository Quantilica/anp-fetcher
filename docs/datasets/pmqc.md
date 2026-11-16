---
dataset:
  id: pmqc
  fonte: anp
  titulo: PMQC — Programa de Monitoramento da Qualidade dos Combustíveis (ensaios por amostra)
  resumo: Resultados dos ensaios físico-químicos de amostras de gasolina, etanol e óleo diesel coletadas em postos pela ANP desde 2016, com a conformidade de cada ensaio.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pmqc-programa-de-monitoramento-da-qualidade-dos-combustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo os metadados da ANP; arquivos anuais de 2016 a 2025 (ZIP com um CSV por mês) e mensais em 2026 (publicados em 13/10/2026 pela página oficial)
  cobertura:
    inicio: 2016-02
    fim: 2026-10
  unidade: um ensaio físico-químico de uma amostra coletada num posto, repetido por ponto de coordenada geográfica (`Latitude`, `Longitude`)
  granularidade:
    espacial: posto revendedor (CNPJ, endereço, município, UF e coordenadas em SIRGAS 2000)
    temporal: data da coleta da amostra (dia)
  formato_bruto: ZIP (anual de 2016 a 2025; mensal em 2026) com um CSV e um JSON por mês; CSV com separador `;`, UTF-8 e CRLF
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 19
  dados_pessoais:
  - coluna: RazaoSocialPosto
    categoria: razão social de pessoa jurídica (posto)
  - coluna: CnpjPosto
    categoria: CNPJ de pessoa jurídica
  - coluna: Endereço
    categoria: localização do posto (endereço e coordenadas)
  - coluna: Complemento
    categoria: localização do posto (endereço e coordenadas)
  - coluna: Bairro
    categoria: localização do posto (endereço e coordenadas)
  - coluna: Município
    categoria: localização do posto (endereço e coordenadas)
  - coluna: Latitude
    categoria: localização do posto (endereço e coordenadas)
  - coluna: Longitude
    categoria: localização do posto (endereço e coordenadas)
  eras:
  - desde: '2016'
    mudanca: arquivo anual com um CSV por mês, a partir de fevereiro de 2016; ensaios auxiliares de campo (`Pres. Bar.`, `Temp. da Amostra`, `ME a 15ºC`, `Ponto de Fulgor estimado`) e `Massa Específica a 20ºC` com grau ordinal aparecem em 2016 e 2017 e não na amostra de 2021
  - desde: '2017'
    mudanca: parte das linhas traz `DataColeta` com hora (`2017-07-20 00:00:00`), como também em 2021; o produto `DMA - MGO` aparece em 2016 e 2017
  - desde: '2026'
    mudanca: arquivos mensais (`pmqc_2026_<MM>.zip`); a ANP publicou em outubro de 2026 a versão revisada com abertura integral dos ensaios conformes e não conformes (antes só o "cadastro positivo", amostras julgadas conformes) e passou a documentar a regra de conformidade da amostra
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# PMQC — Programa de Monitoramento da Qualidade dos Combustíveis (ensaios por amostra)

## Resumo

O Programa de Monitoramento da Qualidade dos Combustíveis (PMQC) monitora a conformidade da gasolina, do etanol e do óleo diesel comercializados na revenda, por meio de laboratórios contratados pela ANP. O programa não tem caráter fiscalizatório e não gera autuações: seu objetivo é levantar os indicadores gerais da qualidade dos combustíveis e identificar focos de não conformidade. Os arquivos trazem os resultados integrais das amostras, conformes e não conformes (desde a revisão de outubro de 2026, a abertura integral dos dados). Cada linha é um ensaio de uma amostra, com o posto, o produto, o resultado e a coluna `Conforme` por ensaio; atenção, as linhas se repetem por coordenada geográfica (veja Cuidados de uso).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pmqc` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pmqc-programa-de-monitoramento-da-qualidade-dos-combustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo os metadados da ANP; arquivos anuais de 2016 a 2025 (ZIP com um CSV por mês) e mensais em 2026 (publicados em 13/10/2026 pela página oficial) |
| Cobertura | 2016-02 a 2026-10 |
| Unidade (uma linha) | um ensaio físico-químico de uma amostra coletada num posto, repetido por ponto de coordenada geográfica (`Latitude`, `Longitude`) |
| Granularidade | espacial: posto revendedor (CNPJ, endereço, município, UF e coordenadas em SIRGAS 2000); temporal: data da coleta da amostra (dia) |
| Formato bruto | ZIP (anual de 2016 a 2025; mensal em 2026) com um CSV e um JSON por mês; CSV com separador `;`, UTF-8 e CRLF |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 19 |
| Unidades de medida | — |
| Dados pessoais | `RazaoSocialPosto` (razão social de pessoa jurídica (posto)); `CnpjPosto` (CNPJ de pessoa jurídica); `Endereço` (localização do posto (endereço e coordenadas)); `Complemento` (localização do posto (endereço e coordenadas)); `Bairro` (localização do posto (endereço e coordenadas)); `Município` (localização do posto (endereço e coordenadas)); `Latitude` (localização do posto (endereço e coordenadas)); `Longitude` (localização do posto (endereço e coordenadas)) |
| Eras | 2016: arquivo anual com um CSV por mês, a partir de fevereiro de 2016; ensaios auxiliares de campo (`Pres. Bar.`, `Temp. da Amostra`, `ME a 15ºC`, `Ponto de Fulgor estimado`) e `Massa Específica a 20ºC` com grau ordinal aparecem em 2016 e 2017 e não na amostra de 2021; 2017: parte das linhas traz `DataColeta` com hora (`2017-07-20 00:00:00`), como também em 2021; o produto `DMA - MGO` aparece em 2016 e 2017; 2026: arquivos mensais (`pmqc_2026_<MM>.zip`); a ANP publicou em outubro de 2026 a versão revisada com abertura integral dos ensaios conformes e não conformes (antes só o "cadastro positivo", amostras julgadas conformes) e passou a documentar a regra de conformidade da amostra |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pmqc/pmqc_<AAAA>.zip` (2016 a 2025, um ZIP anual) e `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pmqc/pmqc_2026_<MM>.zip` (2026, um ZIP por mês), 20 entradas de 2016 a 2026-10; a página oficial indica publicação em 13/10/2026 para os arquivos até setembro de 2026.
- Cada ZIP traz um CSV e um JSON por mês (por exemplo, `2016/PMQC_2016_02.csv` e `.json`; o ZIP de 2016 começa em fevereiro); o conversor lê só os CSV, e os JSON não entram no lake. Tamanhos conferidos na amostra (2026-11-15): 2016, 15.421.851 bytes; 2017, 27.420.985; 2021, 15.952.024; 2026-01, 1.156.082; 2026-06, 839.339.
- No bruto, os arquivos se chamam `pmqc-csv_<AAAA>@AAAAMMDD.zip` e `pmqc-csv_2026-<MM>@AAAAMMDD.zip`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Documentação (versão revisada de outubro de 2026, ANP/SBQ): metadados e "Orientações para análise dos dados abertos do PMQC", ambos documentos Word (https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pmqc/pmqc-metadados e https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pmqc/orientacoes-analises-pmqc.docx), mais um tutorial para carregar os dados no Excel (https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pmqc/pmqc-tutorial.pdf). Dados oriundos do sistema laboratorial (LIMS) da ANP.

## Conteúdo

- **Linha = ensaio × amostra × ponto de coordenada.** A fonte repete cada ensaio de uma amostra para cada ponto de coordenada registrado: no arquivo de setembro de 2017, a amostra 322995 (um posto de Brasília, gasolina aditivada) tem 288 linhas, 18 ensaios por 16 pares `Latitude` e `Longitude`. Sem as colunas de coordenada, as 4.644.955 linhas da amostra viram 2.194.423 linhas distintas (47%).
- **Dimensão da amostra do lake (37 arquivos mensais).** 230.253 amostras (`IdNumeric`) coletadas em 34.593 CNPJs de posto, de 2016-02 a 2026-06: 2016 (11 meses), 2017 (12), 2021 (12) e 2026 (janeiro e junho); 42 nomes de ensaio.
- **Produtos.** 3 grupos (Gasolina, Etanol e Óleo Diesel) e 10 valores de `Produto`; os mais frequentes são GASOLINA C COMUM (1.564.805 linhas), ETANOL HIDRATADO COMUM (980.878) e ÓLEO DIESEL B S10 - COMUM (840.832).
- **Conformidade.** `Conforme` é `Não` em 16.640 linhas (0,36%), que correspondem a 8.055 ensaios distintos; os ensaios com mais `Não` são Teor de Biodiesel (3.885 linhas), Teor de Etanol (1.662), Ponto de Fulgor (1.562) e Teor Alcoólico (1.452). A amostra tem 6.527 amostras com ao menos um ensaio `Não`.
- **Resultado.** Tipo misto: números com ponto decimal, textos qualitativos (`LII`, `Amarelo`, `Incolor`, `Não detectado`) e limites (`<2`, `< 1.5`, `<1.5`, `<0.1`).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2016 | 11 arquivos, de 19 a 19 colunas |
| 2017 | 12 arquivos, de 19 a 19 colunas |
| 2021 | 12 arquivos, de 19 a 19 colunas |
| 2026 | `pmqc-csv-01` (19); `pmqc-csv-06` (19) |

## Variáveis

As descrições vêm do documento de metadados revisado da ANP (outubro de 2026), que traz também a tabela de tipo de `Resultado` por ensaio. Os nomes das colunas do lake são os do cabeçalho do CSV, com maiúsculas e acentos (`Endereço`, `Município`).
Todas as colunas são texto, inclusive `DataColeta`, `IdNumeric`, `Latitude`, `Longitude` e `Resultado`.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `DataColeta` | `DataColeta` | texto | Data em que a coleta do combustível foi realizada (ISO 8601, `AAAA-MM-DD`); em parte dos arquivos de 2017 e 2021 vem com hora (`2017-07-20 00:00:00`) | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `IdNumeric` | `IdNumeric` | texto | Identificador da amostra. Repete-se em uma linha por ensaio realizado na amostra; não é chave da linha (a granularidade da fonte é amostra por ensaio) | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `GrupoProduto` | `GrupoProduto` | texto | Família do combustível | Gasolina = gasolina; Etanol = etanol; Óleo Diesel = óleo diesel | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Produto` | `Produto` | texto | Produto específico (por exemplo, GASOLINA C COMUM, GASOLINA C COMUM ADITIVADA, GASOLINA C PREMIUM, ETANOL HIDRATADO COMUM, ÓLEO DIESEL B S10 - COMUM); a amostra traz ainda `DMA - MGO` (diesel marítimo) em 2016 e 2017, que não está na lista dos metadados | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `RazaoSocialPosto` | `RazaoSocialPosto` | texto | Razão social do posto revendedor onde a amostra foi coletada | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `CnpjPosto` | `CnpjPosto` | texto | CNPJ do posto revendedor (14 dígitos, com máscara `00.000.000/0000-00`) | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Distribuidora` | `Distribuidora` | texto | Distribuidora associada ao posto; `BANDEIRA BRANCA` quando o posto não tem bandeira exclusiva | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Endereço` | `Endereço` | texto | Logradouro do posto | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Complemento` | `Complemento` | texto | Complemento do endereço do posto; pode vir vazio | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Bairro` | `Bairro` | texto | Bairro do posto | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Município` | `Município` | texto | Município do posto; `NÃO INFORMADO` em 1.896 linhas da amostra | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Latitude` | `Latitude` | texto | Latitude do posto (SIRGAS 2000, EPSG:4674), em graus decimais; pode vir vazia (388.466 linhas da amostra). Pode variar entre as linhas repetidas de um mesmo ensaio (veja Cuidados de uso) | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Longitude` | `Longitude` | texto | Longitude do posto (SIRGAS 2000, EPSG:4674), em graus decimais; pode vir vazia. Pode variar entre as linhas repetidas de um mesmo ensaio | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Uf` | `Uf` | texto | Unidade da Federação do posto (sigla) | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `RegiaoPolitica` | `RegiaoPolitica` | texto | Região política do posto; os metadados escrevem `CENTRO-OESTE`, o arquivo traz `CENTRO OESTE` | CENTRO OESTE = Centro-Oeste; NORDESTE = Nordeste; NORTE = Norte; SUDESTE = Sudeste; SUL = Sul | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Ensaio` | `Ensaio` | texto | Nome do ensaio físico-químico (vocabulário controlado, 42 nomes na amostra; o mesmo ensaio pode ter duas grafias, como `Massa Específica a 20°C` e `Massa Específica a 20ºC`) | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Resultado` | `Resultado` | texto | Resultado do ensaio, serializado como texto, com `.` como separador decimal. Inclui valores qualitativos (`Límpido e isento de impurezas (LII)`, `Amarelo`, `Não detectado`) e limites de quantificação (`< 2.0`, `<5`); vazio em 1.900 linhas da amostra | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `UnidadeEnsaio` | `UnidadeEnsaio` | texto | Unidade do ensaio (`°C`, `mg/kg`, `% volume`, `kg/m³`, `% massa`, `µS/m`, `mg/100 mL`); vazia nos ensaios qualitativos | — | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |
| `Conforme` | `Conforme` | texto | Avaliação de conformidade do ensaio (não da amostra) | Sim = ensaio conforme; Não = ensaio não conforme | todo | `pmqc-csv-01`, `pmqc-csv-06`, `pmqc_01` e mais 11 |

## No lake

- Dataset `anp/pmqc`, particionado por `ano` e `mes`; um Parquet por CSV mensal do ZIP, no padrão `ano=<AAAA>/mes=<MM>/pmqc-csv_<AAAA>__pmqc_<AAAA>_<MM>.parquet` (ZIP anual) ou `ano=2026/mes=<MM>/pmqc-csv_2026-<MM>.parquet` (ZIP mensal de 2026).
- As 19 colunas do CSV ficam como texto; só os JSON do ZIP não entram no lake.

## Cuidados de uso

- **As linhas se repetem por coordenada: deduplique antes de contar.** 53% das linhas da amostra diferem das irmãs só em `Latitude` e `Longitude` (ver Conteúdo). Para contar ensaios, use `SELECT DISTINCT` sem as colunas de coordenada (ou agregue por `IdNumeric`, `Ensaio`, `Resultado`); para contar amostras, `count(DISTINCT IdNumeric)`. Os metadados citam apenas replicatas de mesmo `Resultado`, e não essa repetição por ponto de coordenada.
- **`Conforme` vale por ensaio, não por amostra.** Uma amostra só é não conforme se ao menos um ensaio for `Não`, ressalvada a regra dos ensaios complementares do Aspecto para etanol e diesel (documento de orientações da ANP); um `Não` isolado em Aspecto não reprova a amostra. Agregue por `IdNumeric` antes de contar "amostras reprovadas".
- **Resultado é texto misto.** Não converta cegamente para número: use `try_cast`. Limites (`<2`, `< 1.5`, `<1.5`) e `Não detectado` são valores válidos, e a grafia dos limites varia; há 1.900 linhas com `Resultado` vazio.
- **Nomes de ensaio mudam de grafia.** `Massa Específica a 20°C` (símbolo de grau) e `Massa Específica a 20ºC` (ordinal) designam o mesmo ensaio, em 2016 e 2017; agrupe os dois.
- **Datas com e sem hora.** `DataColeta` tem 10 caracteres em 2016 e 2026 e, em 2017 e 2021, parte das linhas (36.841 e 42.463) traz `AAAA-MM-DD 00:00:00`; use `CAST(substr(DataColeta, 1, 10) AS DATE)`.
- **Região e localização.** `RegiaoPolitica` grafa `CENTRO OESTE` (sem hífen); `Município` é `NÃO INFORMADO` em 1.896 linhas e `Latitude` e `Longitude` faltam em 388.466 (8,4%). Coordenadas em SIRGAS 2000.
- **Regras e teores mudam no tempo.** O teor de etanol na gasolina e o de biodiesel no diesel são definidos pelo CNPE e variam (por exemplo, gasolina C com 30% de etanol anidro a partir de agosto de 2025, e biodiesel acima de 10% no diesel recente); compare o resultado com a data de coleta e a resolução da ANP vigente (RANP nº 807/2020 para gasolina, nº 907/2022 para etanol e nº 968/2024 para diesel).
- **Resumo do que a amostra não cobre.** O lake tem só 37 dos 125 meses do período de 2016 a 2026-10 (amostra); a série completa pode ter outras grafias e coberturas de ensaio.
- **Dados pessoais.** Há razão social, CNPJ, endereço e coordenadas de postos revendedores (pessoas jurídicas); em empresas individuais a razão social pode trazer o nome do titular.

## Exemplos

Número de amostras e de amostras com algum ensaio não conforme por grupo de produto em 2021, com as linhas repetidas por coordenada já eliminadas:

```python
import duckdb

duckdb.sql("""
    WITH ensaios AS (
        SELECT DISTINCT * EXCLUDE (Latitude, Longitude)
        FROM read_parquet('lake/anp/pmqc/**/*.parquet', hive_partitioning = true, union_by_name = true)
        WHERE ano = 2021
    )
    SELECT GrupoProduto,
           count(DISTINCT IdNumeric) AS amostras,
           count(DISTINCT IdNumeric) FILTER (WHERE Conforme = 'Não') AS com_ensaio_nao_conforme
    FROM ensaios
    GROUP BY GrupoProduto
    ORDER BY GrupoProduto
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pmqc-programa-de-monitoramento-da-qualidade-dos-combustiveis
- Metadados (Word, versão de outubro de 2026): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pmqc/pmqc-metadados
- Orientações para análise dos dados abertos do PMQC (Word): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pmqc/orientacoes-analises-pmqc.docx
- Resoluções ANP nº 807/2020 (gasolina), nº 907/2022 (etanol) e nº 968/2024 (diesel), citadas nos documentos de orientações.
