---
dataset:
  id: previsao-pat-pap
  fonte: anp
  titulo: Previsão de atividade, investimento e produção (PAT/PAP), por bacia
  resumo: Previsões para o quinquênio 2025-2029 de atividades físicas, investimentos e produção de petróleo e gás por bacia e ambiente, conforme os Programas Anuais de Trabalho e Orçamento (PAT) e de Produção (PAP) dos contratados.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual, segundo o metadado da ANP; cada arquivo é substituído a cada atualização do quinquênio
  cobertura:
    inicio: '2025'
    fim: '2029'
  unidade: 'depende do arquivo: um tipo de atividade em uma bacia e ambiente, em um ano (`previsao-pat-pap-atividade-bacia`); um tipo de atividade em um ano (`previsao-pat-pap-investimento-atividade`); uma bacia e ambiente em um ano (`previsao-pat-pap-investimento-bacia` e `previsao-pat-pap-producao`)'
  granularidade:
    espacial: bacia sedimentar (17) e ambiente, terra ou mar (22 pares), exceto no arquivo de investimento por atividade, que não tem recorte espacial
    temporal: ano previsto (2025 a 2029), na coluna `ANO`; sem partição no lake
  formato_bruto: quatro CSV em UTF-8 com marca de ordem de bytes (BOM), separados por vírgula, com os decimais entre aspas
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 27
  unidades_de_medida:
    ANO: ano civil (AAAA)
    INVESTIMENTO R$: R$ (reais; texto, ponto de milhar e vírgula decimal)
    INVESTIMENTO US$: US$ (dólares; texto, ponto de milhar e vírgula decimal)
    QUANTIDADE ATIVIDADE: 'depende de `UNIDADE DA ATIVIDADE`: unidade, km ou km² (texto, vírgula decimal)'
    PERCENTUAL INJEÇÃO TOTAL: '% (texto, vírgula decimal)'
    PERCENTUAL INJEÇÃO SEM CO2: '% (texto, vírgula decimal)'
    VOLUME PETRÓLEO: m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO PETRÓLEO: m³ por dia (texto, ponto de milhar e vírgula decimal)
    VOLUME GÁS: mil m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO GÁS: mil m³ por dia (texto, ponto de milhar e vírgula decimal)
    VOLUME GÁS SEM CO2: mil m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO GÁS SEM CO2: mil m³ por dia (texto, ponto de milhar e vírgula decimal)
    VOLUME PETRÓLEO EQUIVALENTE: m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO PETRÓLEO EQUIVALENTE: m³ por dia (texto, ponto de milhar e vírgula decimal)
    VOLUME INJEÇÃO ÁGUA: m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO INJEÇÃO ÁGUA: m³ por dia (texto, ponto de milhar e vírgula decimal)
    VOLUME INJEÇÃO GÁS: mil m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO INJEÇÃO GÁS: mil m³ por dia (texto, ponto de milhar e vírgula decimal)
    VOLUME INJEÇÃO GÁS SEM CO2: mil m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO INJEÇAÕ GÁS SEM CO2: mil m³ por dia (texto, ponto de milhar e vírgula decimal)
    VOLUME QUEIMA: mil m³ (texto, ponto de milhar e vírgula decimal)
    VAZÃO QUEIMA: mil m³ por dia (texto, ponto de milhar e vírgula decimal)
  dados_pessoais: nenhum
  eras:
  - desde: '2024'
    mudanca: a previsão de investimento por bacia e por atividade foi divulgada em um único arquivo, depois desdobrado em três (a página da ANP não informa a data da mudança); esse arquivo antigo não está no catálogo do fetcher
  - desde: '2026'
    mudanca: os quatro arquivos atuais e seus metadados foram criados em junho de 2026, com a previsão 2025-2029 coletada em 2026-11-15
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Previsão de atividade, investimento e produção (PAT/PAP), por bacia

## Resumo

Quatro arquivos da fase de desenvolvimento e produção da ANP com as previsões consolidadas para o quinquênio, apresentadas pelos contratados nos Programas Anuais de Trabalho e Orçamento (PAT) e Programas Anuais de Produção (PAP): o quantitativo de atividades por bacia e tipo de atividade, o investimento por bacia, o investimento por tipo de atividade e a produção, injeção e queima previstas por bacia. Os valores vão de 2025 a 2029 e são previsões, não realizações. A ANP também os apresenta no Painel Dinâmico de Consulta das Previsões de Atividades, Investimentos e Produções na Fase de Produção. O dataset irmão com o que foi realizado é `atividades-investimentos`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/previsao-pat-pap` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual, segundo o metadado da ANP; cada arquivo é substituído a cada atualização do quinquênio |
| Cobertura | 2025 a 2029 |
| Unidade (uma linha) | depende do arquivo: um tipo de atividade em uma bacia e ambiente, em um ano (`previsao-pat-pap-atividade-bacia`); um tipo de atividade em um ano (`previsao-pat-pap-investimento-atividade`); uma bacia e ambiente em um ano (`previsao-pat-pap-investimento-bacia` e `previsao-pat-pap-producao`) |
| Granularidade | espacial: bacia sedimentar (17) e ambiente, terra ou mar (22 pares), exceto no arquivo de investimento por atividade, que não tem recorte espacial; temporal: ano previsto (2025 a 2029), na coluna `ANO`; sem partição no lake |
| Formato bruto | quatro CSV em UTF-8 com marca de ordem de bytes (BOM), separados por vírgula, com os decimais entre aspas |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 27 |
| Unidades de medida | `ANO`: ano civil (AAAA); `INVESTIMENTO R$`: R$ (reais; texto, ponto de milhar e vírgula decimal); `INVESTIMENTO US$`: US$ (dólares; texto, ponto de milhar e vírgula decimal); `QUANTIDADE ATIVIDADE`: depende de `UNIDADE DA ATIVIDADE`: unidade, km ou km² (texto, vírgula decimal); `PERCENTUAL INJEÇÃO TOTAL`: % (texto, vírgula decimal); `PERCENTUAL INJEÇÃO SEM CO2`: % (texto, vírgula decimal); `VOLUME PETRÓLEO`: m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO PETRÓLEO`: m³ por dia (texto, ponto de milhar e vírgula decimal); `VOLUME GÁS`: mil m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO GÁS`: mil m³ por dia (texto, ponto de milhar e vírgula decimal); `VOLUME GÁS SEM CO2`: mil m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO GÁS SEM CO2`: mil m³ por dia (texto, ponto de milhar e vírgula decimal); `VOLUME PETRÓLEO EQUIVALENTE`: m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO PETRÓLEO EQUIVALENTE`: m³ por dia (texto, ponto de milhar e vírgula decimal); `VOLUME INJEÇÃO ÁGUA`: m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO INJEÇÃO ÁGUA`: m³ por dia (texto, ponto de milhar e vírgula decimal); `VOLUME INJEÇÃO GÁS`: mil m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO INJEÇÃO GÁS`: mil m³ por dia (texto, ponto de milhar e vírgula decimal); `VOLUME INJEÇÃO GÁS SEM CO2`: mil m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO INJEÇAÕ GÁS SEM CO2`: mil m³ por dia (texto, ponto de milhar e vírgula decimal); `VOLUME QUEIMA`: mil m³ (texto, ponto de milhar e vírgula decimal); `VAZÃO QUEIMA`: mil m³ por dia (texto, ponto de milhar e vírgula decimal) |
| Dados pessoais | nenhum |
| Eras | 2024: a previsão de investimento por bacia e por atividade foi divulgada em um único arquivo, depois desdobrado em três (a página da ANP não informa a data da mudança); esse arquivo antigo não está no catálogo do fetcher; 2026: os quatro arquivos atuais e seus metadados foram criados em junho de 2026, com a previsão 2025-2029 coletada em 2026-11-15 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Quatro arquivos CSV na página de dados abertos da fase de desenvolvimento e produção da ANP, subseção "Previsão de Atividade, Investimento e Produção", em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-previsao/`: `previsao-atividade-bacia.csv` (52.453 bytes), `investimento-bacia.csv` (5.499), `investimento-atividade.csv` (11.795) e `previsao-producao.csv` (20.868). Tamanhos conferidos na coleta de 2026-11-15.
- Fonte do dado, segundo os metadados (`.docx`, criados em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, com relatórios em Power BI; periodicidade anual; contato demandas_sdp@anp.gov.br.
- Segundo a página oficial, a forma de divulgação mudou porque a previsão de investimentos detalhada ao mesmo tempo por atividade e por bacia poderia afetar a vantagem competitiva dos operadores; o arquivo único de investimento/atividade de 2024 foi desdobrado em investimento por bacia, investimento por tipo de atividade e quantitativo de atividades por bacia e atividade (o quantitativo não tem restrição, segundo a ANP).
- O servidor não informa a data de modificação; o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15).

## Conteúdo

- **`previsao-pat-pap-atividade-bacia` (764 linhas):** quantidade prevista por bacia, ambiente, ano e tipo de atividade, com a unidade física. As linhas `Sem Atividade` (104, com quantidade 0,00 e `sem unidade`) marcam bacia e ano sem atividade prevista.
- **`previsao-pat-pap-investimento-bacia` (110 linhas):** investimento previsto por bacia, ambiente e ano, em reais e dólares: 22 pares bacia-ambiente (17 bacias) por 5 anos. A soma anual é de R$ 139,9 bilhões (2025), 153,2 (2026), 127,5 (2027), 107,8 (2028) e 81,1 (2029).
- **`previsao-pat-pap-investimento-atividade` (156 linhas):** investimento previsto por tipo de atividade e ano (34 tipos). A soma anual é igual à do arquivo por bacia (conferido na amostra), então os dois arquivos reapresentam o mesmo total em recortes diferentes.
- **`previsao-pat-pap-producao` (110 linhas):** produção prevista de petróleo, gás, gás sem CO2 e petróleo equivalente, injeção de água e de gás (inclusive sem CO2), percentuais de injeção e queima, em volume anual e em vazão diária, por bacia, ambiente e ano. A soma do volume de petróleo previsto vai de 217,3 milhões de m³ em 2025 a 266,0 milhões em 2028 e 257,7 milhões em 2029; Santos em mar concentra a maior parte (189,4 milhões de m³ em 2027).
- **Previsão, não observação.** Os valores vêm de programas apresentados pelos contratados; a comparação com o realizado deve usar `producao-mar`, `producao-terra` e `atividades-investimentos`.

## Variáveis

As descrições vêm dos metadados `.docx` da ANP de cada arquivo ("Atividades por Bacia", "Investimentos por Bacia", "Investimentos por Atividades" e "Previsão de Produção"); os valores observados vêm da amostra do lake (2026-11-15), que cobre os quatro arquivos inteiros. O metadado dá os valores como número, mas o lake os guarda como texto.
A coluna *Arquivos* diz em quais arquivos a coluna aparece.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar a que se referem os dados da linha; 17 bacias nos arquivos de atividade e investimento por bacia e de produção (Campos, Santos, Potiguar, Recôncavo, Espírito Santo e outras); ausente no arquivo de investimento por atividade. | — | — | `previsao-pat-pap-atividade-bacia`, `previsao-pat-pap-investimento-bacia`, `previsao-pat-pap-producao` |
| `AMBIENTE` | `AMBIENTE` | texto | Ambiente geográfico da bacia ou da produção: `MAR` ou `TERRA`; a mesma bacia pode ter linhas nos dois; ausente no arquivo de investimento por atividade. | — | — | `previsao-pat-pap-atividade-bacia`, `previsao-pat-pap-investimento-bacia`, `previsao-pat-pap-producao` |
| `ANO` | `ANO` | texto | Ano da previsão (atividade, investimento ou produção prevista), de 2025 a 2029. | — | — | `previsao-pat-pap-atividade-bacia`, `previsao-pat-pap-investimento-atividade`, `previsao-pat-pap-investimento-bacia` e mais 1 |
| `TIPO ATIVIDADE` | `TIPO ATIVIDADE` | texto | Tipo de atividade prevista, em texto (34 valores, como `Perfuração - produtor`, `Completação para produção` e `Coleta - linhas - lançamento (inclui risers)`); `Sem Atividade` (104 linhas, quantidade 0,00 e `sem unidade`) marca bacia e ano sem atividade prevista; só no arquivo `previsao-pat-pap-atividade-bacia`. | — | — | `previsao-pat-pap-atividade-bacia` |
| `QUANTIDADE ATIVIDADE` | `QUANTIDADE ATIVIDADE` | texto | Quantidade relativa à atividade física prevista, em texto com vírgula decimal (`1,00`); a unidade está em `UNIDADE DA ATIVIDADE`; só no arquivo `previsao-pat-pap-atividade-bacia`. | — | — | `previsao-pat-pap-atividade-bacia` |
| `UNIDADE DA ATIVIDADE` | `UNIDADE DA ATIVIDADE` | texto | Unidade física da quantidade prevista: `Unidade` (518 linhas), `Kilômetro` (95), `Kilômetro Quadrado` (47) ou `sem unidade` (104, linhas `Sem Atividade`); só no arquivo `previsao-pat-pap-atividade-bacia`. | — | — | `previsao-pat-pap-atividade-bacia` |
| `ATIVIDADE` | `ATIVIDADE` | texto | Tipo de atividade a ser realizada, para a qual se prevê o investimento (34 tipos, os mesmos de `TIPO ATIVIDADE`); só no arquivo `previsao-pat-pap-investimento-atividade`. | — | — | `previsao-pat-pap-investimento-atividade` |
| `INVESTIMENTO R$` | `INVESTIMENTO R$` | texto | Valor previsto a ser investido, em reais, na bacia (`previsao-pat-pap-investimento-bacia`) ou na atividade (`previsao-pat-pap-investimento-atividade`), como texto com ponto de milhar e vírgula decimal (`7.243.187.751,60`). | — | — | `previsao-pat-pap-investimento-atividade`, `previsao-pat-pap-investimento-bacia` |
| `INVESTIMENTO US$` | `INVESTIMENTO US$` | texto | Valor previsto a ser investido, em dólares dos Estados Unidos, no mesmo formato de texto; o metadado da ANP grafa a coluna `INVESTIMENTO U$$`. | — | — | `previsao-pat-pap-investimento-atividade`, `previsao-pat-pap-investimento-bacia` |
| `VOLUME PETRÓLEO` | `VOLUME PETRÓLEO` | texto | Volume de petróleo previsto para o ano, em m³ (texto com ponto de milhar e vírgula decimal); só no arquivo de produção. | — | — | `previsao-pat-pap-producao` |
| `VAZÃO PETRÓLEO` | `VAZÃO PETRÓLEO` | texto | Vazão de petróleo prevista para o ano, em m³ por dia; aproximadamente o volume dividido por 365 (razão de 364,8 a 365,1 na amostra). | — | — | `previsao-pat-pap-producao` |
| `VOLUME GÁS` | `VOLUME GÁS` | texto | Volume de gás previsto para o ano, em mil m³. | — | — | `previsao-pat-pap-producao` |
| `VAZÃO GÁS` | `VAZÃO GÁS` | texto | Vazão de gás prevista para o ano, em mil m³ por dia. | — | — | `previsao-pat-pap-producao` |
| `VOLUME GÁS SEM CO2` | `VOLUME GÁS SEM CO2` | texto | Volume de gás previsto para o ano, descontado o CO2, em mil m³. | — | — | `previsao-pat-pap-producao` |
| `VAZÃO GÁS SEM CO2` | `VAZÃO GÁS SEM CO2` | texto | Vazão de gás prevista para o ano, descontado o CO2, em mil m³ por dia. | — | — | `previsao-pat-pap-producao` |
| `VOLUME PETRÓLEO EQUIVALENTE` | `VOLUME PETRÓLEO EQUIVALENTE` | texto | Volume de petróleo equivalente previsto para o ano, em m³. | — | — | `previsao-pat-pap-producao` |
| `VAZÃO PETRÓLEO EQUIVALENTE` | `VAZÃO PETRÓLEO EQUIVALENTE` | texto | Vazão de petróleo equivalente prevista para o ano, em m³ por dia. | — | — | `previsao-pat-pap-producao` |
| `VOLUME INJEÇÃO ÁGUA` | `VOLUME INJEÇÃO ÁGUA` | texto | Volume de injeção de água previsto para o ano, em m³. | — | — | `previsao-pat-pap-producao` |
| `VAZÃO INJEÇÃO ÁGUA` | `VAZÃO INJEÇÃO ÁGUA` | texto | Vazão de injeção de água prevista para o ano, em m³ por dia. | — | — | `previsao-pat-pap-producao` |
| `VOLUME INJEÇÃO GÁS` | `VOLUME INJEÇÃO GÁS` | texto | Volume de injeção de gás previsto para o ano, em mil m³. | — | — | `previsao-pat-pap-producao` |
| `VAZÃO INJEÇÃO GÁS` | `VAZÃO INJEÇÃO GÁS` | texto | Vazão de injeção de gás prevista para o ano, em mil m³ por dia. | — | — | `previsao-pat-pap-producao` |
| `PERCENTUAL INJEÇÃO TOTAL` | `PERCENTUAL INJEÇÃO TOTAL` | texto | Percentual de injeção total de gás em relação à produção total de gás, em % (texto, vírgula decimal). | — | — | `previsao-pat-pap-producao` |
| `VOLUME INJEÇÃO GÁS SEM CO2` | `VOLUME INJEÇÃO GÁS SEM CO2` | texto | Volume de injeção de gás previsto para o ano, descontado o CO2, em mil m³. | — | — | `previsao-pat-pap-producao` |
| `VAZÃO INJEÇAÕ GÁS SEM CO2` | `VAZÃO INJEÇAÕ GÁS SEM CO2` | texto | Vazão de injeção de gás prevista para o ano, descontado o CO2, em mil m³ por dia; o nome da coluna no CSV tem o erro de grafia `INJEÇAÕ` (o metadado traz `INJEÇÃO`). | — | — | `previsao-pat-pap-producao` |
| `PERCENTUAL INJEÇÃO SEM CO2` | `PERCENTUAL INJEÇÃO SEM CO2` | texto | Percentual de injeção total de gás em relação à produção total de gás, descontado o CO2 de ambos os valores, em % (texto, vírgula decimal). | — | — | `previsao-pat-pap-producao` |
| `VOLUME QUEIMA` | `VOLUME QUEIMA` | texto | Volume de queima previsto para o ano, em mil m³ (gás queimado). | — | — | `previsao-pat-pap-producao` |
| `VAZÃO QUEIMA` | `VAZÃO QUEIMA` | texto | Vazão de queima prevista para o ano, em mil m³ por dia. | — | — | `previsao-pat-pap-producao` |

## No lake

- Dataset `anp/previsao-pat-pap`, sem partição: um Parquet por arquivo, `previsao-pat-pap-atividade-bacia.parquet`, `previsao-pat-pap-investimento-atividade.parquet`, `previsao-pat-pap-investimento-bacia.parquet` e `previsao-pat-pap-producao.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte, inclusive o erro de grafia `VAZÃO INJEÇAÕ GÁS SEM CO2`. O conversor remove a marca de ordem de bytes.

## Cuidados de uso

- **Números em texto.** Quantidades, volumes, vazões, percentuais e valores vêm como `1.045,68` ou `7.243.187.751,60`; tire o ponto de milhar, troque a vírgula por ponto e converta (`replace(replace(col, '.', ''), ',', '.')::DOUBLE`).
- **Unidades diferentes.** Petróleo e petróleo equivalente em m³; gás, gás sem CO2, injeção de gás e queima em mil m³; vazões em m³/dia ou mil m³/dia; não some petróleo e gás sem converter. O petróleo equivalente é uma conversão da própria fonte; a regra de conversão não é informada nos metadados.
- **Nome de coluna com erro.** O CSV traz `VAZÃO INJEÇAÕ GÁS SEM CO2`; o metadado da ANP grafa `VAZÃO INJEÇÃO GÁS SEM CO2`. O lake preserva a grafia do CSV.
- **Empilhar mistura tabelas.** Ler os quatro Parquet com `union_by_name` deixa nulos nas colunas dos outros arquivos (por exemplo, `BACIA` e `AMBIENTE` nulos no investimento por atividade). Leia cada arquivo separadamente ou una por (`BACIA`, `AMBIENTE`, `ANO`).
- **Investimento por bacia e por atividade repete o total.** Somar os dois arquivos conta cada real duas vezes.
- **`Sem Atividade`.** É um valor de `TIPO ATIVIDADE` com quantidade zero, não um tipo de atividade real; exclua ao contar tipos de atividade.
- **Horizonte móvel.** A previsão é de cinco anos e é substituída a cada atualização anual (a edição anterior sai da página); a coleta de 2026-11-15 cobre 2025-2029. Para comparar edições diferentes, use as coletas datadas guardadas no bruto.
- **Detalhe restrito.** Por decisão da ANP, o investimento não é divulgado ao mesmo tempo por bacia e atividade.
- **Sem dados pessoais.** Não há nomes de pessoas nem de empresas.

## Exemplos

Produção de petróleo e investimento previstos para 2027, por bacia (liga os dois arquivos pela chave e converte os textos em número):

```python
import duckdb

duckdb.sql("""
    SELECT p."BACIA", p."AMBIENTE",
           round(replace(replace(p."VOLUME PETRÓLEO", '.', ''), ',', '.')::DOUBLE / 1e6, 2) AS petroleo_milhoes_m3,
           round(replace(replace(i."INVESTIMENTO R$", '.', ''), ',', '.')::DOUBLE / 1e9, 2) AS investimento_bilhoes_reais
    FROM read_parquet('lake/anp/previsao-pat-pap/previsao-pat-pap-producao.parquet') p
    JOIN read_parquet('lake/anp/previsao-pat-pap/previsao-pat-pap-investimento-bacia.parquet') i
      USING ("BACIA", "AMBIENTE", "ANO")
    WHERE p."ANO" = '2027'
    ORDER BY petroleo_milhoes_m3 DESC
    LIMIT 5
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadados (.docx), na pasta https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-previsao/: `metadado-atividade-bacia.docx`, `metadado-investimento-bacia.docx`, `metadado-investimento-atividade.docx` e `metadados-previsao-producao.docx`.
- Painel Dinâmico de Consulta das Previsões de Atividades, Investimentos e Produções na Fase de Produção (ANP), indicado na página de dados abertos.
