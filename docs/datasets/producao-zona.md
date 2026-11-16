---
dataset:
  id: producao-zona
  fonte: anp
  titulo: Produção de petróleo e gás natural por zona produtora
  resumo: Produção e injeção mensais por poço e zona produtora, em vazão média diária, de outubro de 2014 em diante, com a unidade estratigráfica da zona até junho de 2025.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; o fetcher lê um CSV por mês, de 2014-10 a 2026-09 (144 arquivos), com defasagem de dois meses
  cobertura:
    inicio: 2014-10
    fim: em-curso
  unidade: 'uma zona produtora de um poço em um mês: vazões médias diárias do mês de produção e de injeção'
  granularidade:
    espacial: zona produtora de um poço (nome ANP), com campo, bacia e ambiente
    temporal: mês de referência (`Data`)
  formato_bruto: CSV em UTF-8 com BOM, separado por vírgula, com valores entre aspas e decimal em vírgula (e ponto de milhar nos arquivos recentes)
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 27
  unidades_de_medida:
    Óleo (m³/d): m³/dia
    Condensado (m³/d): m³/dia
    Petróleo (m³/d): m³/dia
    Água (m³/d): m³/dia
    Água injetada para descarte (m³/d): m³/dia
    Água injetada para rec. secundária (m³/d): m³/dia
    Outros fluidos injetados (m³/d): m³/dia
    Gás associado (Mil m³/d): mil m³/dia
    Gás não associado (Mil m³/d): mil m³/dia
    Gás total (Mil m³/d): mil m³/dia
    Gás injetado (Mil m³/d): mil m³/dia
    CO2 injetado (Mil m³/d): mil m³/dia
    N2 injetado (Mil m³/d): mil m³/dia
    Vapor injetado (t/d): t/dia
  dados_pessoais: nenhum
  eras:
  - desde: 2014-10
    mudanca: 27 colunas, com a estratigrafia da zona (`Pré-sal`, `Período`, `Época`, `Idade`, `Grupo`, `Formação`, `Membro`); `Data` no formato MM/AAAA
  - desde: 2025-07
    mudanca: '20 colunas: a estratigrafia e a marca de pré-sal saem do arquivo; no arquivo de 2025-09, conferido fora da amostra, `Zona` traz códigos numéricos e os valores têm ponto de milhar'
  - desde: 2026-04
    mudanca: '`Data` passa a vir como DD/MM/AAAA, sempre dia 01 (`01/09/2026`)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de petróleo e gás natural por zona produtora

## Resumo

Produção mensal de óleo, condensado, gás e água, e injeção de fluidos, por zona produtora de cada poço, em média diária do mês, com campo, bacia, ambiente e, até junho de 2025, a posição estratigráfica da zona (período, época e idade geológicos; grupo, formação e membro) e a marca de pré-sal. Os dados vêm do SIGEP e do Do Poço ao Posto, em relatórios em Power BI; um poço com várias zonas aparece em várias linhas no mês.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/producao-zona` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; o fetcher lê um CSV por mês, de 2014-10 a 2026-09 (144 arquivos), com defasagem de dois meses |
| Cobertura | 2014-10 a em-curso |
| Unidade (uma linha) | uma zona produtora de um poço em um mês: vazões médias diárias do mês de produção e de injeção |
| Granularidade | espacial: zona produtora de um poço (nome ANP), com campo, bacia e ambiente; temporal: mês de referência (`Data`) |
| Formato bruto | CSV em UTF-8 com BOM, separado por vírgula, com valores entre aspas e decimal em vírgula (e ponto de milhar nos arquivos recentes) |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 27 |
| Unidades de medida | `Óleo (m³/d)`: m³/dia; `Condensado (m³/d)`: m³/dia; `Petróleo (m³/d)`: m³/dia; `Água (m³/d)`: m³/dia; `Água injetada para descarte (m³/d)`: m³/dia; `Água injetada para rec. secundária (m³/d)`: m³/dia; `Outros fluidos injetados (m³/d)`: m³/dia; `Gás associado (Mil m³/d)`: mil m³/dia; `Gás não associado (Mil m³/d)`: mil m³/dia; `Gás total (Mil m³/d)`: mil m³/dia; `Gás injetado (Mil m³/d)`: mil m³/dia; `CO2 injetado (Mil m³/d)`: mil m³/dia; `N2 injetado (Mil m³/d)`: mil m³/dia; `Vapor injetado (t/d)`: t/dia |
| Dados pessoais | nenhum |
| Eras | 2014-10: 27 colunas, com a estratigrafia da zona (`Pré-sal`, `Período`, `Época`, `Idade`, `Grupo`, `Formação`, `Membro`); `Data` no formato MM/AAAA; 2025-07: 20 colunas: a estratigrafia e a marca de pré-sal saem do arquivo; no arquivo de 2025-09, conferido fora da amostra, `Zona` traz códigos numéricos e os valores têm ponto de milhar; 2026-04: `Data` passa a vir como DD/MM/AAAA, sempre dia 01 (`01/09/2026`) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa 144 CSV mensais de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/producao-por-zona/producao_zona_<MM>-<AAAA>.csv`, de 10-2014 a 09-2026. Três nomes fogem do padrão no catálogo do fetcher: o de fevereiro de 2022 é publicado como `producao_zona_03-2022.csv` e o de abril de 2023 como `producao_zona_03-2023.csv` (rótulos da ANP de mês anterior), e o de março de 2026 chama-se `Produo_Zona_032026.csv`.
- Fonte do dado, segundo o metadado "Produção por Zona" (DOCX, criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; atualização mensal; contato demandas_sdp@anp.gov.br.
- No bruto: `producao-zona/producao-zona_<AAAA>-<MM>@AAAAMMDD.csv`, com o sufixo da data da coleta. Tamanhos na amostra: de 2,2 MB (2026-09) a 3,5 MB (2014-11).

## Conteúdo

- **Uma linha por zona de um poço e mês.** Em 2023-10 (amostra), 8.205 poços ocupam 16.408 linhas, com 266 campos; em 2026-09, 6.795 poços e 13.468 linhas. Os volumes são vazões médias diárias do mês (`m³/d` ou `Mil m³/d`), não volumes mensais.
- **Estratigrafia (2014-10 a 2025-06).** `Pré-sal`, `Período`, `Época`, `Idade`, `Grupo`, `Formação` e `Membro` descrevem a zona; `Membro` está vazio na maioria das linhas (2.635 de 15.847 em 2017-10). Em 2025-07 em diante essas sete colunas deixam de existir.
- **Partição.** `ano` e `mes` vêm do nome do arquivo (o mês de referência do catálogo), e não da coluna `Data`; para os arquivos com rótulo trocado, a partição segue o catálogo.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2014 | `producao-zona-10` (27); `producao-zona-11` (27) |
| 2017 | `producao-zona-10` (27) |
| 2020 | `producao-zona-10` (27) |
| 2023 | `producao-zona-10` (27) |
| 2026 | `producao-zona-09` (20) |

## Variáveis

As descrições vêm do metadado "Produção por Zona" da ANP (DOCX, criado em junho de 2026). O metadado dá os volumes de gás como `(m³/d)`, mas as colunas dos arquivos dizem `(Mil m³/d)`; segue-se o nome da coluna. A coluna *Período* mostra em que meses cada coluna existe (as sete colunas de estratigrafia só até 2025-06).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Zona` | `Zona` | texto | Zona produtora (texto livre: nome da zona, como `CP/PRINCIPAL` ou `ET 1`, código, como `3874`, ou, em alguns arquivos antigos, o nome de um poço). | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Pré-sal` | `Pré-sal` | texto | Indicação se a zona pertence ou não ao pré-sal (`S` ou `N`). | — | 2014-10 a 2023-10 | `producao-zona-10`, `producao-zona-11` |
| `Período` | `Período` | texto | Período geológico da zona produtora, conforme a geocronologia cadastrada na ANP (não confundir com período de tempo da produção). | — | 2014-10 a 2023-10 | `producao-zona-10`, `producao-zona-11` |
| `Época` | `Época` | texto | Época geológica da zona produtora, conforme a geocronologia cadastrada. | — | 2014-10 a 2023-10 | `producao-zona-10`, `producao-zona-11` |
| `Idade` | `Idade` | texto | Idade geológica da zona produtora, conforme a geocronologia cadastrada. | — | 2014-10 a 2023-10 | `producao-zona-10`, `producao-zona-11` |
| `Grupo` | `Grupo` | texto | Grupo da unidade estratigráfica da zona produtora, conforme a litoestratigrafia cadastrada. | — | 2014-10 a 2023-10 | `producao-zona-10`, `producao-zona-11` |
| `Formação` | `Formação` | texto | Formação da unidade estratigráfica da zona produtora, conforme a litoestratigrafia cadastrada. | — | 2014-10 a 2023-10 | `producao-zona-10`, `producao-zona-11` |
| `Membro` | `Membro` | texto | Membro da unidade estratigráfica da zona produtora, conforme a litoestratigrafia cadastrada (vazio na maioria das linhas). | — | 2014-10 a 2023-10 | `producao-zona-10`, `producao-zona-11` |
| `Nome poço ANP` | `Nome poço ANP` | texto | Nome do poço, atribuído conforme a Resolução ANP nº 699/2017. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Campo` | `Campo` | texto | Nome do campo. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar em que se localiza o poço. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Ambiente` | `Ambiente` | texto | Ambiente geográfico da produção: `TERRA` ou `MAR`. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Data` | `Data` | texto | Data da produção: `MM/AAAA` até fevereiro de 2026 e `01/MM/AAAA` (dia 1) a partir de abril de 2026 (texto). | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Óleo (m³/d)` | `Óleo (m³/d)` | texto | Volume de óleo produzido no mês, em m³ por dia (média diária do mês). | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Condensado (m³/d)` | `Condensado (m³/d)` | texto | Volume de condensado produzido no mês, em m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Petróleo (m³/d)` | `Petróleo (m³/d)` | texto | Volume de petróleo (óleo mais condensado) produzido no mês, em m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Gás associado (Mil m³/d)` | `Gás associado (Mil m³/d)` | texto | Volume de gás associado produzido no mês, em mil m³ por dia (o metadado escreve `m³/d` no nome). | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Gás não associado (Mil m³/d)` | `Gás não associado (Mil m³/d)` | texto | Volume de gás não associado produzido no mês, em mil m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Gás total (Mil m³/d)` | `Gás total (Mil m³/d)` | texto | Volume de gás total produzido no mês, em mil m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Água (m³/d)` | `Água (m³/d)` | texto | Volume de água produzida no mês, em m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Água injetada para descarte (m³/d)` | `Água injetada para descarte (m³/d)` | texto | Volume de água injetada para descarte no mês, em m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Água injetada para rec. secundária (m³/d)` | `Água injetada para rec. secundária (m³/d)` | texto | Volume de água injetada para recuperação secundária no mês, em m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Vapor injetado (t/d)` | `Vapor injetado (t/d)` | texto | Massa de vapor injetada no mês, em toneladas por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Gás injetado (Mil m³/d)` | `Gás injetado (Mil m³/d)` | texto | Volume de gás injetado no mês, em mil m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `CO2 injetado (Mil m³/d)` | `CO2 injetado (Mil m³/d)` | texto | Volume de gás carbônico injetado no mês, em mil m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `N2 injetado (Mil m³/d)` | `N2 injetado (Mil m³/d)` | texto | Volume de nitrogênio injetado no mês, em mil m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |
| `Outros fluidos injetados (m³/d)` | `Outros fluidos injetados (m³/d)` | texto | Volume de outros tipos de fluidos injetado no mês, em m³ por dia. | — | todo | `producao-zona-09`, `producao-zona-10`, `producao-zona-11` |

## No lake

- Dataset `anp/producao-zona`, particionado por `ano` e `mes`: um Parquet por CSV, `ano=<AAAA>/mes=<MM>/producao-zona_<AAAA>-<MM>.parquet`.
- Todas as colunas são texto, com os nomes da fonte (acentos, `Mil m³/d`).

## Cuidados de uso

- **Layout muda em julho de 2025.** Os arquivos até 2025-06 têm 27 colunas e os de 2025-07 em diante, 20; ao empilhar, use `union_by_name` e trate as colunas de estratigrafia como ausentes depois dessa data. O período da produção (`Período`) é geológico, não é o mês.
- **Formato da data muda duas vezes.** `Data` é `10/2014` (MM/AAAA) até 2026-02 e `01/09/2026` (DD/MM/AAAA, dia 1) a partir de 2026-04; o arquivo de março de 2026, de nome fora do padrão, não foi conferido. Normalize com os dois formatos ou use as partições `ano` e `mes`.
- **Ponto de milhar nos arquivos recentes.** Em 2026-09 (amostra), 219 linhas de `Óleo (m³/d)` têm ponto de milhar (`1.075,20`); em 2014-10 e 2023-10 não há. Remova o ponto antes de trocar a vírgula, apenas nos arquivos que o usam.
- **`Zona` sem padrão.** Pode ser nome de zona, código numérico (`3874` em 2025-09) ou até um nome de poço (`1-BRSA-57ES` em 2017-10). Para identificar zonas, use o par `Nome poço ANP` e `Zona`, e confira por arquivo.
- **Sem chave.** `(Zona, Nome poço ANP)` é único em 2014-10, mas repete em 2023-10 (15.904 pares em 16.408 linhas) e em 2026-09 (12.987 em 13.468). A chave do dataset fica vazia.
- **Colunas zeradas.** Nas amostras de 2014-10 e 2026-09, as colunas de injeção valem `0,00` em todas as linhas; em 2026-09 a água produzida tem valores (5.224 distintos) e em 2014-10 vale `0,00` em todas as linhas, o que parece incompleto para um mês de produção; a fonte não explica.
- **Mesmo arquivo em duas partições.** O catálogo do fetcher aponta 2022-02 e 2022-03 (e 2023-03 e 2023-04) para o mesmo URL, por rótulos trocados na página da ANP; as duas partições do lake guardam então o mesmo conteúdo, e o mês real está em `Data`. Nesses casos, deduplique por `Data`.
- **Dados pessoais.** Não há: poços, campos, zonas e bacias.

## Exemplos

Petróleo e água produzidos por campo em setembro de 2026, por vazão diária (colunas em texto; o ponto de milhar nos valores recentes é tirado antes da troca da vírgula):

```python
import duckdb

duckdb.sql("""
    SELECT Campo, count(DISTINCT "Nome poço ANP") AS pocos,
           round(sum(replace(replace("Petróleo (m³/d)", '.', ''), ',', '.')::DOUBLE), 1) AS petroleo_m3_dia,
           round(sum(replace(replace("Água (m³/d)", '.', ''), ',', '.')::DOUBLE), 1) AS agua_m3_dia
    FROM read_parquet('lake/anp/producao-zona/ano=2026/mes=09/*.parquet')
    GROUP BY Campo
    ORDER BY petroleo_m3_dia DESC
    LIMIT 10
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos), seção "Produção por zona": https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadado "Produção por Zona" (DOCX): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/producao-por-zona/metadados-producao-zona.docx
