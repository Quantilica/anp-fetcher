---
dataset:
  id: pml
  fonte: anp
  titulo: Programa de Monitoramento dos Lubrificantes (PML) — resultados das amostras coletadas
  resumo: 'Resultados da conformidade de registro e qualidade das amostras de óleos lubrificantes coletadas pelo Programa de Monitoramento dos Lubrificantes (PML) da ANP, de 2016 a 2026: 13.726 amostras, por detentor do registro, marca, lote, município e boletim.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/o-programa-de-monitoramento-dos-lubrificantes-pml
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semestral (metadado e página da ANP); dados abertos atualizados em 15/05/2026 e metadados em 15/06/2026
  cobertura:
    inicio: '2016'
    fim: '2026'
  unidade: uma amostra de óleo lubrificante coletada e avaliada em um boletim do PML
  granularidade:
    espacial: município e UF de coleta da amostra, em texto (sem código IBGE); detentor do registro por razão social e CNPJ
    temporal: ano e número do boletim de publicação (de 2016 a 2026, na coluna `ANO`); a data de fabricação do produto é um atributo em texto
  formato_bruto: um CSV em UTF-8 com marca de ordem de bytes (BOM), separado por ponto e vírgula
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 18
  unidades_de_medida:
    ANO: ano civil (AAAA)
  dados_pessoais:
  - coluna: DETENTOR
    categoria: razão social e CNPJ do detentor do registro do lubrificante (pessoa jurídica)
  - coluna: CNPJ_DETENTOR
    categoria: razão social e CNPJ do detentor do registro do lubrificante (pessoa jurídica)
  eras:
  - desde: '2016'
    mudanca: 18 colunas em um só arquivo; município como `Município, UF, Brasil`, data de fabricação em `DD/MM/AA` e CNPJ formatado
  - desde: '2022'
    mudanca: a data de fabricação passa a `DD/MM/AAAA` (525 das 944 linhas de 2022) e, de 2023 em diante, o município vem só com o nome (as linhas com `, UF, Brasil` caem de 334 em 2022 para 4 em 2023 e 0 em 2025)
  - desde: '2025'
    mudanca: 'os resultados de conformidade passam a vir em maiúsculas (`CONFORME`: 469 das 679 linhas de 2025 e as 341 de 2026) e o CNPJ do detentor, só com dígitos (215 e 117 linhas)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Programa de Monitoramento dos Lubrificantes (PML) — resultados das amostras coletadas

## Resumo

O Programa de Monitoramento dos Lubrificantes (PML) acompanha sistematicamente a qualidade dos óleos lubrificantes comercializados no país e orienta as ações de fiscalização da ANP. Laboratórios contratados pela ANP coletam e enviam as amostras ao Centro de Pesquisas e Análises Tecnológicas (CPT), que faz integralmente a análise dos registros dos produtos, os ensaios físico-químicos e a avaliação dos resultados. Os resultados saem em boletins, e este arquivo reúne todos: uma linha por amostra, com o detentor do registro (empresa e CNPJ), a marca comercial, o grau SAE, o número de registro, o nível de desempenho, o lote, a data de fabricação, os resultados de conformidade final, do registro e da qualidade, o resumo das não conformidades, o município e a UF de coleta e o boletim e o ano de publicação. A atualização é semestral.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pml` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/o-programa-de-monitoramento-dos-lubrificantes-pml |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semestral (metadado e página da ANP); dados abertos atualizados em 15/05/2026 e metadados em 15/06/2026 |
| Cobertura | 2016 a 2026 |
| Unidade (uma linha) | uma amostra de óleo lubrificante coletada e avaliada em um boletim do PML |
| Granularidade | espacial: município e UF de coleta da amostra, em texto (sem código IBGE); detentor do registro por razão social e CNPJ; temporal: ano e número do boletim de publicação (de 2016 a 2026, na coluna `ANO`); a data de fabricação do produto é um atributo em texto |
| Formato bruto | um CSV em UTF-8 com marca de ordem de bytes (BOM), separado por ponto e vírgula |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 18 |
| Unidades de medida | `ANO`: ano civil (AAAA) |
| Dados pessoais | `DETENTOR` (razão social e CNPJ do detentor do registro do lubrificante (pessoa jurídica)); `CNPJ_DETENTOR` (razão social e CNPJ do detentor do registro do lubrificante (pessoa jurídica)) |
| Eras | 2016: 18 colunas em um só arquivo; município como `Município, UF, Brasil`, data de fabricação em `DD/MM/AA` e CNPJ formatado; 2022: a data de fabricação passa a `DD/MM/AAAA` (525 das 944 linhas de 2022) e, de 2023 em diante, o município vem só com o nome (as linhas com `, UF, Brasil` caem de 334 em 2022 para 4 em 2023 e 0 em 2025); 2025: os resultados de conformidade passam a vir em maiúsculas (`CONFORME`: 469 das 679 linhas de 2025 e as 341 de 2026) e o CNPJ do detentor, só com dígitos (215 e 117 linhas) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Um arquivo CSV na página de dados abertos do PML da ANP: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-pml/dados-abertos-pml.csv` (3.535.004 bytes, conferido na coleta de 2026-11-15). Metadados em PDF na mesma pasta: `metadados-pml.pdf`.
- Fonte do dado, segundo o metadado: Boletim de Monitoramento de Lubrificantes e Microsoft Power BI (o Painel Dinâmico do PML da ANP traz informações adicionais); contato registrodelubrificantes@anp.gov.br. O arquivo é substituído a cada atualização semestral.
- A página oficial indica a atualização dos dados abertos em 15/05/2026 (a página e o metadado, em 15/06/2026); o servidor não informa a data de modificação do arquivo, e o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15).

## Conteúdo

- **O que é uma linha:** uma amostra de lubrificante avaliada em um boletim: 13.726 linhas e 13.697 códigos de `AMOSTRA` distintos (29 códigos repetidos, 8 deles em linhas idênticas).
- **Boletins por ano de publicação:** 165 amostras em 2016 (1º boletim), 1.555 em 2017 (5 boletins), 1.000 em 2018, 2.534 em 2019, 1.805 em 2020, 1.914 em 2021, 944 em 2022, 1.355 em 2023, 1.434 em 2024, 679 em 2025 e 341 em 2026 (1º boletim).
- **Conformidade:** 2.599 amostras (18,9%) estão `NÃO CONFORME` no resultado final; a proporção cai de 26,1% (2016) e 28,5% (2017) para 13,8% (2025) e 14,4% (2026). As causas mais frequentes no `RESUMO` são `Produto sem registro.` (850 linhas) e `Aditivação fora de especificação.` (642), além de viscosidades e índice de basicidade fora de especificação.
- **Geografia:** coletas em 21 UFs, lideradas por São Paulo (2.449 linhas), Minas Gerais (2.196), Rio de Janeiro (1.561) e Paraná (1.223); 158 detentores de registro e 1.425 números de registro.
- **Níveis de desempenho:** `SL` (6.918 linhas), `SN` (3.189), `CI-4` (1.010) e `CH-4` (871) são os mais comuns, entre 22 valores.

## Variáveis

As descrições das 18 colunas vêm do metadado `metadados-pml.pdf` da ANP ("Informações sobre o conjunto de dados"); os contadores vêm da amostra do lake (2026-11-15), que cobre o arquivo inteiro. O metadado dá `REGISTRO` e `ANO` como número, mas o lake os guarda como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `AMOSTRA` | `AMOSTRA` | texto | Identificador único da amostra, conforme cadastro (formato `CPT/ML00062/2014`); 29 códigos aparecem em duas linhas na amostra (8 delas são cópias exatas). | — | — |
| `DETENTOR` | `DETENTOR` | texto | Pessoa jurídica vinculada ao registro do produto, responsável legal por todas as atualizações e alterações cadastrais da empresa e do registro perante a ANP (razão social); 158 detentores. | — | — |
| `CNPJ_DETENTOR` | `CNPJ_DETENTOR` | texto | Número do CNPJ do detentor; em 13.253 de 13.726 linhas vem formatado (`05.524.572/0001-93`), em 332 só com dígitos e em 141 como `N.A`. | — | — |
| `MARCA_COMERCIAL` | `MARCA_COMERCIAL` | texto | Identificação do produto, conforme registro e rótulo (1.576 marcas distintas, como `ELAION F 50 E`). | — | — |
| `GRAU_SAE` | `GRAU_SAE` | texto | Classificação de viscosidade do óleo lubrificante (grau SAE), como `20W50`, `15W40`, `5W30`; `N.A.` em 1 linha. | — | — |
| `REGISTRO` | `REGISTRO` | texto | Número de registro do produto; cada marca comercial está vinculada a um único número de registro na ANP (1.425 registros distintos nas 13.726 linhas). | — | — |
| `NÍVEL_DESEMPENHO` | `NÍVEL_DESEMPENHO` | texto | Nível de desempenho do óleo (22 valores, como `SL`, `SN`, `CI-4`, `CH-4`, `SJ`, `ACEA`); a Resolução ANP nº 804/2019 estabelece como níveis mínimos API SL e ACEA vigente para motores do ciclo Otto e API CH-4 e ACEA vigente para o ciclo Diesel. | — | — |
| `LOTE` | `LOTE` | texto | Lote de fabricação, conforme exigência do §1º do art. 12 (da resolução citada no metadado); texto livre, `****` em parte das linhas; vazio em 1. | — | — |
| `DATA_FABRICAÇÃO` | `DATA_FABRICAÇÃO` | texto | Data de fabricação, conforme exigência do §1º do art. 12; texto com `DD/MM/AA` (8.968 linhas), `DD/MM/AAAA` (3.984) ou `NÃO IDENTIFICADO` (774). | — | — |
| `RESULTADO_FINAL` | `RESULTADO_FINAL` | texto | Avaliação final de conformidade da amostra: `CONFORME` ou `NÃO CONFORME`, em duas grafias (`Conforme`/`Não Conforme` em 12.916 linhas e `CONFORME`/`NÃO CONFORME` em 810). | — | — |
| `RESULTADO_REGISTRO` | `RESULTADO_REGISTRO` | texto | Avaliação quanto ao registro da amostra: `CONFORME` ou `NÃO CONFORME`, nas mesmas duas grafias. | — | — |
| `RESULTADO_QUALIDADE` | `RESULTADO_QUALIDADE` | texto | Avaliação quanto à qualidade da amostra: `CONFORME`, `NÃO CONFORME` ou `Sem Avaliação` (849 linhas, em duas grafias, `SEM AVALIAÇÃO` e `Sem Avaliação`). | — | — |
| `RESUMO` | `RESUMO` | texto | Resumo da situação da amostra, indicando as não conformidades identificadas (148 textos distintos, como `Amostra conforme.`, `Produto sem registro.`, `Aditivação fora de especificação.`, `Viscosidade cinemática a 100°C fora de especificação.`). | — | — |
| `MUNICÍPIO` | `MUNICÍPIO` | texto | Município de coleta da amostra; em 9.313 linhas vem como `Município, UF, Brasil` (`Curitiba, PARANÁ, Brasil`) e em 4.413 só com o nome do município (`Joinville`, 492 linhas); o texto da UF dentro do valor tem erros (`ABAETETUBA, PARÁRÁ, Brasil`). | — | — |
| `UF` | `UF` | texto | UF de coleta da amostra, por extenso e em maiúsculas (21 valores, como `SÃO PAULO`); a grafia `TOCATINS` (21 linhas) está errada na fonte. | — | — |
| `BOLETIM` | `BOLETIM` | texto | Identificação do boletim em que a amostra foi publicada, de `1º BOLETIM` a `5º BOLETIM`; 4 a 5 boletins por ano (2017 tem 5). | — | — |
| `ANO` | `ANO` | texto | Ano de publicação do boletim, de 2016 a 2026 (2026 só tem o 1º boletim). | — | — |
| `OBSERVAÇÃO` | `OBSERVAÇÃO` | texto | Informações gerais não apresentadas nos outros campos (33 textos distintos, em 1.099 linhas): avisos de que o nível de desempenho está obsoleto (`API SJ`, `API CG-4`, Resolução ANP nº 804/2019) e de empresas sem autorização de produção ou com registros cancelados. | — | — |

## No lake

- Dataset `anp/pml`, sem partição: um Parquet, `pml.parquet`, com as 13.726 linhas e as 18 colunas.
- Todas as colunas são texto. O conversor remove a marca de ordem de bytes e mantém os nomes do cabeçalho, com acentos e `_` (`NÍVEL_DESEMPENHO`, `DATA_FABRICAÇÃO`, `MUNICÍPIO`, `OBSERVAÇÃO`).

## Cuidados de uso

- **Duas grafias nos resultados (maiúsculas desde 2025).** `RESULTADO_FINAL`, `RESULTADO_REGISTRO` e `RESULTADO_QUALIDADE` misturam `Conforme`/`Não Conforme` e `CONFORME`/`NÃO CONFORME` (e `Sem Avaliação`/`SEM AVALIAÇÃO`); use `upper()` antes de contar.
- **Formatos que mudam com o tempo.** `DATA_FABRICAÇÃO` vem em `DD/MM/AA` (até 2022), `DD/MM/AAAA` (de 2022 em diante) ou `NÃO IDENTIFICADO` (774); `CNPJ_DETENTOR` vem formatado, só com dígitos (332, de 2025 em diante) ou como `N.A` (141); `MUNICÍPIO` vem com `, UF, Brasil` até 2022 e só com o nome depois, com erros dentro do texto (`PARÁRÁ`). Normalize antes de agrupar por município ou por data.
- **UF por extenso, com erro.** `TOCATINS` (21 linhas) é grafia errada; não há sigla nem código IBGE.
- **Amostras repetidas.** 29 códigos de `AMOSTRA` aparecem duas vezes, 8 com todas as colunas iguais; remova duplicatas exatas antes de contar amostras.
- **Resultados dependem da época.** Em 975 linhas a `OBSERVAÇÃO` diz que o produto foi avaliado conforme a norma vigente na data da coleta (por exemplo, `API SJ` e `API CG-4` hoje estão obsoletos, conforme a Resolução ANP nº 804/2019); não compare conformidade entre anos sem considerar a mudança de norma.
- **Amostra não é universo.** O PML coleta amostras para orientar a fiscalização; as proporções de não conformidade não representam necessariamente o mercado.
- **Chave.** `AMOSTRA` não é única (29 repetidas), então a chave do dataset fica vazia.
- **Dados pessoais.** `DETENTOR` e `CNPJ_DETENTOR` são de pessoas jurídicas, públicos; `OBSERVAÇÃO` cita razões sociais de empresas. Não há pessoa física identificada.

## Exemplos

Amostras e proporção de não conformes no resultado final, por ano de publicação (remove as linhas idênticas e junta as duas grafias do resultado):

```python
import duckdb

duckdb.sql("""
    SELECT "ANO",
           count(*) AS amostras,
           count(*) FILTER (WHERE upper("RESULTADO_FINAL") LIKE 'N%') AS nao_conformes,
           round(100.0 * count(*) FILTER (WHERE upper("RESULTADO_FINAL") LIKE 'N%') / count(*), 1) AS pct_nao_conformes
    FROM (SELECT DISTINCT * FROM read_parquet('lake/anp/pml/pml.parquet'))
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Programa de Monitoramento dos Lubrificantes (PML), dados abertos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/o-programa-de-monitoramento-dos-lubrificantes-pml
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-pml/metadados-pml.pdf
- Painel Dinâmico do Programa de Monitoramento de Lubrificantes (ANP), indicado na página; Resolução ANP nº 804/2019, citada no metadado.
