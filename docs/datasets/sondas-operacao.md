---
dataset:
  id: sondas-operacao
  fonte: anp
  titulo: Sondas em operação por período
  resumo: Relação anual das sondas de perfuração e intervenção em operação no Brasil, de 2013 a 2025, com os campos em que atuaram e o operador.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'anual na prática: o fetcher lê um CSV por ano, de 2013 a 2025 (13 arquivos); o metadado da ANP indica atualização mensal'
  cobertura:
    inicio: '2013'
    fim: '2025'
  unidade: uma sonda que operou no Brasil em um ano (`ano` da partição, tirado do nome do arquivo)
  granularidade:
    espacial: sonda, com os campos em que operou e o operador; sem coordenadas
    temporal: ano do arquivo (partição `ano`)
  formato_bruto: CSV em UTF-8 com BOM, separado por vírgula, de 4 colunas
  lake:
    estado: convertido
    particoes:
    - ano
    chave:
    - ano
    - Sigla_da_sonda
    colunas: 4
  dados_pessoais:
  - coluna: Operador_da_sonda
    categoria: nome de empresa que usou a sonda (pessoa jurídica)
  eras:
  - desde: '2013'
    mudanca: um arquivo por ano (`sondas_em_operacao_por_periodo_<ano>.csv`) de 2013 a 2025, sempre com as mesmas 4 colunas (nos 6 anos da amostra)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Sondas em operação por período

## Resumo

Para cada ano, a lista das sondas que operaram em poços no Brasil, com a sigla e o nome da sonda, o(s) campo(s) em que operaram no ano e o operador que as contratou. Não traz datas nem poços: é um inventário anual das sondas ativas. Os dados vêm do SIGEP e do Do Poço ao Posto.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/sondas-operacao` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual na prática: o fetcher lê um CSV por ano, de 2013 a 2025 (13 arquivos); o metadado da ANP indica atualização mensal |
| Cobertura | 2013 a 2025 |
| Unidade (uma linha) | uma sonda que operou no Brasil em um ano (`ano` da partição, tirado do nome do arquivo) |
| Granularidade | espacial: sonda, com os campos em que operou e o operador; sem coordenadas; temporal: ano do arquivo (partição `ano`) |
| Formato bruto | CSV em UTF-8 com BOM, separado por vírgula, de 4 colunas |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | `ano`, `Sigla_da_sonda` |
| Colunas | 4 |
| Unidades de medida | — |
| Dados pessoais | `Operador_da_sonda` (nome de empresa que usou a sonda (pessoa jurídica)) |
| Eras | 2013: um arquivo por ano (`sondas_em_operacao_por_periodo_<ano>.csv`) de 2013 a 2025, sempre com as mesmas 4 colunas (nos 6 anos da amostra) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- 13 CSV em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-pocos/`, `sondas_em_operacao_por_periodo_<ano>.csv`, de 2013 a 2025. Na amostra, de 12.636 bytes (2019) a 20.735 (2025). O fetcher não tem arquivo de 2026.
- Fonte do dado, segundo o metadado "Sondas em Operação por Período" (DOCX, criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; contato demandas_sdp@anp.gov.br.
- No bruto: `sondas-operacao/sondas-operacao_<ano>@AAAAMMDD.csv`, com o sufixo da data da coleta.

## Conteúdo

- **Uma linha por sonda e ano.** Na amostra: 217 sondas em 2013, 185 em 2014, 135 em 2016, 125 em 2019, 128 em 2022 e 200 em 2025; em cada ano a sigla é única.
- **Campos e operadores.** `Campo` lista os campos atendidos no ano (por exemplo, `ACAUÃ / CARDEAL / FAZE...` para uma sonda terrestre); em 2025 há 170 combinações distintas de campos e 50 operadores.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2013 | `sondas-operacao` (4) |
| 2014 | `sondas-operacao` (4) |
| 2016 | `sondas-operacao` (4) |
| 2019 | `sondas-operacao` (4) |
| 2022 | `sondas-operacao` (4) |
| 2025 | `sondas-operacao` (4) |

## Variáveis

As descrições vêm do metadado "Sondas em Operação por Período" (DOCX da ANP, criado em junho de 2026), que descreve só três das quatro colunas (`Sigla_da_sonda`, `Nome_da_sonda` e `Campo`); a de `Operador_da_sonda` é deduzida do nome e dos valores observados.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Sigla_da_sonda` | `Sigla_da_sonda` | texto | Sigla da sonda, conforme a denominação do operador. | — | todo |
| `Nome_da_sonda` | `Nome_da_sonda` | texto | Nome da sonda, conforme a denominação do operador. | — | todo |
| `Campo` | `Campo` | texto | Nome do(s) campo(s) em que a sonda operou no período indicado no nome do arquivo (texto com `/` entre os nomes quando há mais de um; truncado nos exemplos longos). | — | todo |
| `Operador_da_sonda` | `Operador_da_sonda` | texto | Operador (empresa) que usou a sonda no período; o metadado da ANP não descreve esta coluna. | — | todo |

## No lake

- Dataset `anp/sondas-operacao`, particionado por `ano`: um Parquet por CSV, `ano=<ano>/sondas-operacao_<ano>.parquet`.
- Todas as colunas são texto, com os nomes da fonte (`_` entre as palavras).

## Cuidados de uso

- **Sem datas.** O arquivo só diz que a sonda operou no ano; não há início, fim, poço ou intervenção. Para o uso de sondas por poço, veja `intervencoes-pocos` (coluna `Sonda`).
- **`Campo` é uma lista.** Os campos vêm concatenados com ` / ` e podem passar de 100 caracteres; use `string_split(Campo, ' / ')` para abrir.
- **Chave (conferida na amostra).** `Sigla_da_sonda` é única dentro de cada ano nos seis arquivos da amostra; a mesma sonda se repete entre anos, e `Nome_da_sonda` é único em 2025 (200 nomes distintos).
- **Anos não coletados.** O catálogo não tem 2026; os anos de 2015, 2017, 2018, 2020, 2021, 2023 e 2024 estão no catálogo, mas fora da amostra e sem conferência do conteúdo.
- **Dados pessoais.** Não há: nomes de sondas e de empresas.

## Exemplos

Número de sondas por ano e a quantidade que atuou em apenas um campo (a coluna `Campo` é uma lista separada por ` / `):

```python
import duckdb

duckdb.sql("""
    SELECT ano, count(*) AS sondas,
           count(*) FILTER (WHERE strpos(Campo, ' / ') = 0) AS em_um_so_campo
    FROM read_parquet('lake/anp/sondas-operacao/ano=*/*.parquet', hive_partitioning = true)
    GROUP BY ano
    ORDER BY ano
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos), informações sobre poços: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadado "Sondas em Operação por Período" (DOCX): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-pocos/metadado-sonda-em-operacao-por-periodo.docx
