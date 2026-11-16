---
dataset:
  id: atividades-investimentos
  fonte: anp
  titulo: Atividades e investimentos realizados na fase de produção, por bacia
  resumo: Atividades físicas realizadas e investimentos (em reais e dólares) por bacia, ambiente, ano e tipo de atividade na fase de produção, de 2022 a 2025, conforme os Programas Anuais de Trabalho e Orçamento (PAT).
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual, segundo o metadado da ANP; cada arquivo é substituído a cada atualização
  cobertura:
    inicio: '2022'
    fim: '2025'
  unidade: 'um tipo de atividade em uma bacia e ambiente, em um ano: a quantidade realizada (`atividades-investimentos-atividade`) ou o investimento realizado (`atividades-investimentos-investimento`)'
  granularidade:
    espacial: bacia sedimentar (15), com ambiente terra ou mar; sem campo, bloco, estado ou município
    temporal: ano (2022 a 2025), na coluna `Ano`; sem partição no lake
  formato_bruto: dois CSV em UTF-8 com marca de ordem de bytes (BOM), separados por vírgula, com os decimais entre aspas
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 8
  unidades_de_medida:
    Quantidade realizada: 'depende de `Unidade da Atividade`: unidade, km ou km² (texto, vírgula decimal)'
    Investimento R$: R$ (reais; texto com ponto de milhar e vírgula decimal)
    Investimento US$: US$ (dólares; texto com ponto de milhar e vírgula decimal)
    Ano: ano civil (AAAA)
  dados_pessoais: nenhum
  eras:
  - desde: '2022'
    mudanca: série de 2022 a 2025 nos dois arquivos; o metadado da ANP (criado em junho de 2026) fala em "quinquênio", mas os arquivos coletados em 2026-11-15 trazem quatro anos
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Atividades e investimentos realizados na fase de produção, por bacia

## Resumo

Dois arquivos da fase de desenvolvimento e produção da ANP, com a mesma chave (bacia, ambiente, ano e atividade): as atividades realizadas, com a quantidade e a unidade física, e os investimentos realizados, em reais e em dólares. Os dados vêm dos Programas Anuais de Trabalho e Orçamento (PAT) apresentados pelos contratados, extraídos do SIGEP e do Do Poço ao Posto e organizados em relatórios Power BI. Cada linha é um tipo de atividade em uma bacia e um ambiente, em um ano (126 a 134 linhas por ano, 509 por arquivo). A ANP também publica a série como painel dinâmico. O irmão com os valores previstos é o dataset `previsao-pat-pap`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/atividades-investimentos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual, segundo o metadado da ANP; cada arquivo é substituído a cada atualização |
| Cobertura | 2022 a 2025 |
| Unidade (uma linha) | um tipo de atividade em uma bacia e ambiente, em um ano: a quantidade realizada (`atividades-investimentos-atividade`) ou o investimento realizado (`atividades-investimentos-investimento`) |
| Granularidade | espacial: bacia sedimentar (15), com ambiente terra ou mar; sem campo, bloco, estado ou município; temporal: ano (2022 a 2025), na coluna `Ano`; sem partição no lake |
| Formato bruto | dois CSV em UTF-8 com marca de ordem de bytes (BOM), separados por vírgula, com os decimais entre aspas |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 8 |
| Unidades de medida | `Quantidade realizada`: depende de `Unidade da Atividade`: unidade, km ou km² (texto, vírgula decimal); `Investimento R$`: R$ (reais; texto com ponto de milhar e vírgula decimal); `Investimento US$`: US$ (dólares; texto com ponto de milhar e vírgula decimal); `Ano`: ano civil (AAAA) |
| Dados pessoais | nenhum |
| Eras | 2022: série de 2022 a 2025 nos dois arquivos; o metadado da ANP (criado em junho de 2026) fala em "quinquênio", mas os arquivos coletados em 2026-11-15 trazem quatro anos |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Dois arquivos CSV na página de dados abertos da fase de desenvolvimento e produção da ANP, subseção "Atividades e investimentos realizados", em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/atividades-e-investimentos-realizados/`: `atividade-realizada.csv` (36.444 bytes) e `investimento-realizado.csv` (43.627). Tamanhos conferidos na coleta de 2026-11-15; o catálogo do fetcher tem os dois arquivos (`atividades-investimentos-atividade` e `atividades-investimentos-investimento`).
- Fonte do dado, segundo os metadados (`metadados-atividade-realizada.docx` e `metadados-investimentos-realizados.docx`, criados em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP (Sistema de Informações Gerenciais de Exploração e Produção) e do Do Poço ao Posto (DPP), com relatórios em Power BI; periodicidade anual; contato demandas_sdp@anp.gov.br.
- Os mesmos dados aparecem no Painel Dinâmico de Atividades e Investimentos Realizados na Fase de Produção da ANP; os CSV são a versão em arquivo.
- O servidor não informa a data de modificação; o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15).

## Conteúdo

- **Atividades (`atividades-investimentos-atividade`, 509 linhas):** quantidade realizada de cada tipo de atividade por bacia, ambiente e ano, com a unidade física (`Unidade`, `Kilômetro` ou `Kilômetro Quadrado`). Por ano: 126 linhas em 2022, 116 em 2023, 133 em 2024 e 134 em 2025.
- **Investimentos (`atividades-investimentos-investimento`, 509 linhas):** valor investido em cada atividade, em reais e em dólares, nas mesmas 509 combinações de bacia, ambiente, ano e atividade (as duas tabelas se ligam por essa chave, conferido na amostra). A soma de `Investimento R$` é de R$ 46,7 bilhões em 2022, R$ 65,8 bilhões em 2023, R$ 98,4 bilhões em 2024 e R$ 151,9 bilhões em 2025 (R$ 362,8 bilhões no total; US$ 67,5 bilhões).
- **Bacias e ambientes:** 18 pares bacia-ambiente. Campos (95 linhas em mar) e Santos (80 em mar) lideram em número de linhas, seguidas de Recôncavo (66 em terra) e Potiguar (56 em terra).
- **Atividades:** 33 tipos, de perfuração, completação, recompletação e abandono de poços a instalação de unidades de produção (UEP), coleta, escoamento, sísmica e recuperação ambiental.
- Todas as colunas são texto no lake: os números trazem vírgula decimal e, nos valores em reais e dólares, ponto de milhar.

## Variáveis

As descrições vêm dos metadados `.docx` da ANP ("Atividades Realizadas" e "Investimentos Realizados"); os valores observados vêm da amostra do lake (2026-11-15), que cobre os dois arquivos inteiros. O metadado dá `ANO` e os valores como número, mas o lake os guarda como texto.
A coluna *Arquivos* diz em qual dos dois arquivos cada coluna aparece.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar a que se referem os dados da linha; 15 bacias (Campos, Santos, Potiguar, Recôncavo, Espírito Santo, Sergipe e outras). | — | — | `atividades-investimentos-atividade`, `atividades-investimentos-investimento` |
| `Ambiente` | `Ambiente` | texto | Ambiente geográfico da bacia: `TERRA` ou `MAR`; a mesma bacia pode ter linhas nos dois (Espírito Santo, Potiguar, Sergipe). | — | — | `atividades-investimentos-atividade`, `atividades-investimentos-investimento` |
| `Ano` | `Ano` | texto | Ano da atividade realizada (arquivo de atividades) ou do investimento realizado (arquivo de investimentos); de 2022 a 2025. | — | — | `atividades-investimentos-atividade`, `atividades-investimentos-investimento` |
| `Atividade` | `Atividade` | texto | Tipo de atividade realizada, em texto (33 tipos, como `Perfuração - produtor`, `Recompletação para produção`, `UEP - instalação`, `Abandono Permanente`). | — | — | `atividades-investimentos-atividade`, `atividades-investimentos-investimento` |
| `Quantidade realizada` | `Quantidade realizada` | texto | Quantidade relativa à atividade física informada, em texto com vírgula decimal (`1,00`, `22,79`); a unidade está em `Unidade da Atividade`; só no arquivo de atividades. A parte fracionária reflete, deduzida dos valores, a participação do contratado. | — | — | `atividades-investimentos-atividade` |
| `Unidade da Atividade` | `Unidade da Atividade` | texto | Unidade física da quantidade: `Unidade` (397 linhas), `Kilômetro` (78) ou `Kilômetro Quadrado` (34); só no arquivo de atividades. | — | — | `atividades-investimentos-atividade` |
| `Investimento R$` | `Investimento R$` | texto | Valor investido na atividade, em reais, como texto com ponto de milhar e vírgula decimal (`33.176,00`); só no arquivo de investimentos. | — | — | `atividades-investimentos-investimento` |
| `Investimento US$` | `Investimento US$` | texto | Valor investido na atividade, em dólares dos Estados Unidos, no mesmo formato de texto (`6.380,00`); só no arquivo de investimentos. O metadado da ANP grafa a coluna `INVESTIMENTO U$$`. | — | — | `atividades-investimentos-investimento` |

## No lake

- Dataset `anp/atividades-investimentos`, sem partição: um Parquet por arquivo, `atividades-investimentos-atividade.parquet` e `atividades-investimentos-investimento.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (com maiúsculas, espaços e `R$`/`US$`). O conversor remove a marca de ordem de bytes.

## Cuidados de uso

- **Números em texto.** `Quantidade realizada`, `Investimento R$` e `Investimento US$` vêm como `1,00` ou `33.176,00`; tire o ponto de milhar, troque a vírgula por ponto e converta (`replace(replace(col, '.', ''), ',', '.')::DOUBLE`).
- **Quantidades heterogêneas.** A unidade muda por atividade (poços em unidades, linhas em quilômetros, recuperação ambiental em km²); só some a quantidade dentro de um mesmo tipo de atividade, e nunca entre unidades diferentes. Há quantidades fracionárias (`22,79` poços de perfuração em Campos), que a fonte não explica; a explicação mais plausível (deduzida) é a ponderação pela participação do contratado.
- **Dados de duas tabelas.** Quantidades e investimentos estão em arquivos separados; empilhar os dois (como o `read_parquet` com `union_by_name` faz) deixa nulos nas colunas do outro arquivo. Una por (`Bacia`, `Ambiente`, `Ano`, `Atividade`).
- **Cobertura.** Há apenas quatro anos (2022 a 2025), embora o metadado fale em quinquênio. Os dados vêm dos PAT dos contratados; este dataset não é a produção nem o gasto contábil de cada campo.
- **Detalhe restrito.** Os arquivos não trazem campo, empresa ou contrato; o menor recorte é bacia mais ambiente. Para as previsões (dataset `previsao-pat-pap`), a página da ANP explica que o detalhamento simultâneo de investimento por atividade e por bacia poderia afetar a vantagem competitiva dos operadores; para os valores realizados, a fonte não dá o motivo.
- **Sem dados pessoais.** Não há nomes de pessoas nem de empresas.

## Exemplos

Investimento médio por poço produtor perfurado em 2025, por bacia (liga as duas tabelas pela chave e converte os textos em número):

```python
import duckdb

duckdb.sql("""
    SELECT a."Bacia", a."Ambiente",
           replace(replace(a."Quantidade realizada", '.', ''), ',', '.')::DOUBLE AS pocos,
           round(replace(replace(i."Investimento R$", '.', ''), ',', '.')::DOUBLE
                 / replace(replace(a."Quantidade realizada", '.', ''), ',', '.')::DOUBLE / 1e6, 1) AS milhoes_reais_por_poco
    FROM read_parquet('lake/anp/atividades-investimentos/atividades-investimentos-atividade.parquet') a
    JOIN read_parquet('lake/anp/atividades-investimentos/atividades-investimentos-investimento.parquet') i
      USING ("Bacia", "Ambiente", "Ano", "Atividade")
    WHERE a."Ano" = '2025' AND a."Atividade" = 'Perfuração - produtor'
    ORDER BY pocos DESC
    LIMIT 6
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadados (.docx): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/atividades-e-investimentos-realizados/metadados-atividade-realizada.docx e https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/atividades-e-investimentos-realizados/metadados-investimentos-realizados.docx
- Painel Dinâmico de Atividades e Investimentos Realizados na Fase de Produção (ANP), indicado na página de dados abertos.
