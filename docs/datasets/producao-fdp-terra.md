---
dataset:
  id: producao-fdp-terra
  fonte: anp
  titulo: Produção de petróleo e gás natural em terra, por poço e mês (fase de desenvolvimento e produção)
  resumo: Produção e injeção mensais por poço terrestre no Brasil, de 1941 em diante, em 107 arquivos da ANP (históricos, semestrais e trimestrais), particionados por ano e período.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal na fonte (o arquivo corrente é atualizado a cada mês, com defasagem de dois meses após o mês de produção); os arquivos são publicados por trimestre (2016 em diante), semestre, ano ou faixa de anos
  cobertura:
    inicio: 1941-12
    fim: em-curso
  unidade: 'um poço terrestre em um mês de referência: uma linha de produção ou de injeção, com os volumes do mês'
  granularidade:
    espacial: poço (nome ANP), com campo, bacia, estado e instalação; ambiente terra
    temporal: mês de referência (`Mês/Ano`, MM/AAAA)
  formato_bruto: CSV (UTF-8 com BOM ou, no arquivo de 2019 em mar, Latin-1), separado por vírgula, com decimal em vírgula e CRLF
  lake:
    estado: convertido
    particoes:
    - ano
    - semestre
    - mes
    chave: []
    colunas: 41
  unidades_de_medida:
    Produção de Óleo (m³): m³ por mês
    Produção de Condensado (m³): m³ por mês
    Produção de Água (m³): m³ por mês
    Injeção de Água para Recuperação Secundária (m³): m³ por mês
    Injeção de Água para Descarte (m³): m³ por mês
    Injeção de Polímeros (m³): m³ por mês
    Injeção de Outros Fluidos (m³): m³ por mês
    Produção de Gás Associado (Mm³): mil m³ por mês
    Produção de Gás Não Associado (Mm³): mil m³ por mês
    Injeção de Gás (Mm³): mil m³ por mês
    Injeção de Gás Carbônico (Mm³): mil m³ por mês
    Injeção de Nitrogênio (Mm³): mil m³ por mês
    Injeção de Vapor de Água (t): t por mês
  dados_pessoais: nenhum
  eras:
  - desde: '1941'
    mudanca: arquivos históricos plurianuais (1941-1966 a 1981-1982) e anuais (1983 a 1988), em `producao-fdp-terra-anual` (1941-1966 na amostra)
  - desde: '1989'
    mudanca: arquivos semestrais de 1989 a 2015 (partições `ano` e `semestre`); a coluna `Ano` do CSV é descartada porque `ano` é partição
  - desde: '2016'
    mudanca: 'arquivos trimestrais de 2016 a 2026 (partições `ano` e `mes`, em que `mes` é o último mês do trimestre: 03, 06, 09 ou 12)'
  - desde: '2022'
    mudanca: os cabeçalhos passam a vir entre colchetes, inclusive `[Ano]`; `Ambiente` passa de `Terra` a `TERRA`
  - desde: '2026'
    mudanca: no arquivo do 1º trimestre de 2026 da amostra, volumes a partir de mil usam ponto de milhar (`2.229,59`)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de petróleo e gás natural em terra, por poço e mês (fase de desenvolvimento e produção)

## Resumo

Produção mensal de petróleo, condensado, gás natural e água, e injeção de fluidos, por poço terrestres no Brasil, com campo, bacia, estado e instalação. Cada linha é um poço em um mês (produção ou injeção). Os volumes vêm dos Boletins Mensais de Produção que as operadoras enviam à ANP, extraídos do SIGEP e do Do Poço ao Posto, e cobrem de meados do século XX até o mês corrente. Os arquivos mais recentes são trimestrais, os do começo dos anos 2000 semestrais e os históricos plurianuais.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/producao-fdp-terra` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal na fonte (o arquivo corrente é atualizado a cada mês, com defasagem de dois meses após o mês de produção); os arquivos são publicados por trimestre (2016 em diante), semestre, ano ou faixa de anos |
| Cobertura | 1941-12 a em-curso |
| Unidade (uma linha) | um poço terrestre em um mês de referência: uma linha de produção ou de injeção, com os volumes do mês |
| Granularidade | espacial: poço (nome ANP), com campo, bacia, estado e instalação; ambiente terra; temporal: mês de referência (`Mês/Ano`, MM/AAAA) |
| Formato bruto | CSV (UTF-8 com BOM ou, no arquivo de 2019 em mar, Latin-1), separado por vírgula, com decimal em vírgula e CRLF |
| Estado no lake | convertido |
| Partições | `ano`, `semestre`, `mes` |
| Chave | — |
| Colunas | 41 |
| Unidades de medida | `Produção de Óleo (m³)`: m³ por mês; `Produção de Condensado (m³)`: m³ por mês; `Produção de Água (m³)`: m³ por mês; `Injeção de Água para Recuperação Secundária (m³)`: m³ por mês; `Injeção de Água para Descarte (m³)`: m³ por mês; `Injeção de Polímeros (m³)`: m³ por mês; `Injeção de Outros Fluidos (m³)`: m³ por mês; `Produção de Gás Associado (Mm³)`: mil m³ por mês; `Produção de Gás Não Associado (Mm³)`: mil m³ por mês; `Injeção de Gás (Mm³)`: mil m³ por mês; `Injeção de Gás Carbônico (Mm³)`: mil m³ por mês; `Injeção de Nitrogênio (Mm³)`: mil m³ por mês; `Injeção de Vapor de Água (t)`: t por mês |
| Dados pessoais | nenhum |
| Eras | 1941: arquivos históricos plurianuais (1941-1966 a 1981-1982) e anuais (1983 a 1988), em `producao-fdp-terra-anual` (1941-1966 na amostra); 1989: arquivos semestrais de 1989 a 2015 (partições `ano` e `semestre`); a coluna `Ano` do CSV é descartada porque `ano` é partição; 2016: arquivos trimestrais de 2016 a 2026 (partições `ano` e `mes`, em que `mes` é o último mês do trimestre: 03, 06, 09 ou 12); 2022: os cabeçalhos passam a vir entre colchetes, inclusive `[Ano]`; `Ambiente` passa de `Terra` a `TERRA`; 2026: no arquivo do 1º trimestre de 2026 da amostra, volumes a partir de mil usam ponto de milhar (`2.229,59`) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa 107 CSV de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-producao-de-petroleo-e-gas-natural-nacional/pt/`, em pastas por período: `2026/` a `2016/` (trimestrais, `producao_por_poco_terra_<ano>_<N>_trim.csv` e variantes), `2015/` a `1989/` (semestrais, `producao-terra-<ano>-<N>sem.csv`), `1988-1983/` (anuais) e `1982-1941/` (históricos plurianuais). A ANP marcou a seção "Produção em terra" como atualizada em 3/11/2026 e lista o 3º trimestre de 2026.
- Fonte do dado, segundo o metadado "Produção poço - TERRA" (criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; atualização mensal; contato demandas_sdp@anp.gov.br.
- **Sobreposição com `producao-terra`:** 80 dos 107 URLs são os mesmos do grupo `producao-terra` (83 arquivos). Este grupo traz a mais os semestres de 1989 a 1999 e os trimestres de 2020, e **não** tem `producao_por_poco_terra_2026_2_trim.csv` nem `producao_por_poco_terra_2026_3_trim.csv`, que a ANP já lista na página (comparação dos nomes de arquivo no catálogo, 2026-11-15).
- No bruto, o arquivo é `producao-fdp-terra/producao-fdp-terra_<período>@AAAAMMDD.csv`, em que `<período>` é `<ano>`, `<ano>-S1/S2` ou `<ano>-<mês>` e o sufixo é a data da coleta; o servidor não informa a data de modificação.

## Conteúdo

- **Um poço em um mês.** Cada linha traz a produção (óleo, condensado, gás associado e não associado, água) ou a injeção de um poço terrestre, com campo, bacia, estado e instalação.
- **Duas tabelas no lake**, por profundidade de partição (o conversor exige a mesma profundidade em todos os arquivos de um dataset):

| Dataset do lake | Partições | Arquivos de origem | Amostra |
|---|---|---|---|
| `producao-fdp-terra` | `ano` e `semestre` (1989 a 2015) ou `ano` e `mes` (2016 em diante) | semestrais e trimestrais | 1995 S1 (41.532 linhas), 2008 S2 (56.245), 2019 2º tri (39.998), 2025 1º tri (29.802), 2026 1º tri (20.389) |
| `producao-fdp-terra-anual` | `ano` | históricos plurianuais (1941-1966 a 1981-1982) e anuais (1983 a 1988) | 1941-1966 em `ano=1966` (47.254 linhas, dez/1941 a dez/1966) |

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 1966 | `producao-fdp-terra-anual` (20) |
| 1995 | `producao-fdp-terra` (20) |
| 2008 | `producao-fdp-terra` (20) |
| 2019 | `producao-fdp-terra` (20) |
| 2025 | `producao-fdp-terra` (21) |
| 2026 | `producao-fdp-terra` (21) |

## Variáveis

As descrições vêm dos metadados `.docx` da ANP "Produção poço - TERRA" (criados em junho de 2026), um por ambiente, com colunas idênticas; a observação sobre as unidades e as grafias vem da amostra do lake (2026-11-15).
Os metadados descrevem a era mais nova, dos nomes sem colchetes: as colunas com colchetes têm a descrição do campo homônimo. O metadado diz que o ano é número e o mês/ano é data MM/AAAA; no lake todas as colunas são texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Mês/Ano` | `Mês/Ano` | texto | Mês e ano da produção, no formato MM/AAAA (texto). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Estado` | `Estado` | texto | Estado da Federação (nome por extenso) do poço; vazio em algumas linhas. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar em que se localiza o poço. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Campo` | `Campo` | texto | Nome do campo. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Poço` | `Poço` | texto | Nome do poço, atribuído conforme a Resolução ANP nº 699/2017. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Ambiente` | `Ambiente` | texto | Ambiente geográfico da produção, terra ou mar (`Mar`/`Terra` nos arquivos antigos e `MAR`/`TERRA` nos de 2022 em diante). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Instalação` | `Instalação` | texto | Instalação à qual o poço está interligado (`Não Informado` nos arquivos antigos, que não trazem instalação). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Produção de Óleo (m³)` | `Produção de Óleo (m³)` | texto | Volume de óleo produzido no mês, em m³ (texto com vírgula decimal). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Produção de Condensado (m³)` | `Produção de Condensado (m³)` | texto | Volume de condensado produzido no mês, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Produção de Gás Associado (Mm³)` | `Produção de Gás Associado (Mm³)` | texto | Volume de gás natural associado produzido no mês, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Produção de Gás Não Associado (Mm³)` | `Produção de Gás Não Associado (Mm³)` | texto | Volume de gás natural não associado produzido no mês, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Produção de Água (m³)` | `Produção de Água (m³)` | texto | Volume de água produzida no mês, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Gás (Mm³)` | `Injeção de Gás (Mm³)` | texto | Volume de gás natural injetado para recuperação secundária e/ou armazenamento, em milhares de m³ (o metadado da ANP escreve `(m³)` no nome e `milhares de metros cúbicos` na descrição). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Água para Recuperação Secundária (m³)` | `Injeção de Água para Recuperação Secundária (m³)` | texto | Volume de água injetada para recuperação secundária, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Água para Descarte (m³)` | `Injeção de Água para Descarte (m³)` | texto | Volume de água injetada para descarte, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Gás Carbônico (Mm³)` | `Injeção de Gás Carbônico (Mm³)` | texto | Volume de gás carbônico injetado, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Nitrogênio (Mm³)` | `Injeção de Nitrogênio (Mm³)` | texto | Volume de nitrogênio injetado, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Vapor de Água (t)` | `Injeção de Vapor de Água (t)` | texto | Vapor de água injetado, em toneladas (o metadado fala em "volume", mas a unidade é massa). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Polímeros (m³)` | `Injeção de Polímeros (m³)` | texto | Volume de polímeros injetado, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `Injeção de Outros Fluidos (m³)` | `Injeção de Outros Fluidos (m³)` | texto | Volume de outros tipos de fluidos injetado, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1966 a 2019-06 | `producao-fdp-terra`, `producao-fdp-terra-anual` |
| `[Ano]` | `[Ano]` | texto | Ano de referência da produção (texto). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Mês/Ano]` | `[Mês/Ano]` | texto | Mês e ano da produção, no formato MM/AAAA (texto). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Estado]` | `[Estado]` | texto | Estado da Federação (nome por extenso) do poço; vazio em algumas linhas. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Bacia]` | `[Bacia]` | texto | Nome da bacia sedimentar em que se localiza o poço. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Campo]` | `[Campo]` | texto | Nome do campo. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Poço]` | `[Poço]` | texto | Nome do poço, atribuído conforme a Resolução ANP nº 699/2017. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Ambiente]` | `[Ambiente]` | texto | Ambiente geográfico da produção, terra ou mar (`Mar`/`Terra` nos arquivos antigos e `MAR`/`TERRA` nos de 2022 em diante). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Instalação]` | `[Instalação]` | texto | Instalação à qual o poço está interligado (`Não Informado` nos arquivos antigos, que não trazem instalação). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Produção de Óleo (m³)]` | `[Produção de Óleo (m³)]` | texto | Volume de óleo produzido no mês, em m³ (texto com vírgula decimal). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Produção de Condensado (m³)]` | `[Produção de Condensado (m³)]` | texto | Volume de condensado produzido no mês, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Produção de Gás Associado (Mm³)]` | `[Produção de Gás Associado (Mm³)]` | texto | Volume de gás natural associado produzido no mês, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Produção de Gás Não Associado (Mm³)]` | `[Produção de Gás Não Associado (Mm³)]` | texto | Volume de gás natural não associado produzido no mês, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Produção de Água (m³)]` | `[Produção de Água (m³)]` | texto | Volume de água produzida no mês, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Gás (Mm³)]` | `[Injeção de Gás (Mm³)]` | texto | Volume de gás natural injetado para recuperação secundária e/ou armazenamento, em milhares de m³ (o metadado da ANP escreve `(m³)` no nome e `milhares de metros cúbicos` na descrição). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Água para Recuperação Secundária (m³)]` | `[Injeção de Água para Recuperação Secundária (m³)]` | texto | Volume de água injetada para recuperação secundária, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Água para Descarte (m³)]` | `[Injeção de Água para Descarte (m³)]` | texto | Volume de água injetada para descarte, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Gás Carbônico (Mm³)]` | `[Injeção de Gás Carbônico (Mm³)]` | texto | Volume de gás carbônico injetado, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Nitrogênio (Mm³)]` | `[Injeção de Nitrogênio (Mm³)]` | texto | Volume de nitrogênio injetado, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Vapor de Água (t)]` | `[Injeção de Vapor de Água (t)]` | texto | Vapor de água injetado, em toneladas (o metadado fala em "volume", mas a unidade é massa). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Polímeros (m³)]` | `[Injeção de Polímeros (m³)]` | texto | Volume de polímeros injetado, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |
| `[Injeção de Outros Fluidos (m³)]` | `[Injeção de Outros Fluidos (m³)]` | texto | Volume de outros tipos de fluidos injetado, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025-03 a 2026-03 | `producao-fdp-terra` |

## No lake

- Datasets do lake com esquema comum: `anp/producao-fdp-terra` (partições `ano`, `semestre=S1|S2` e `mes=03|06|09|12`; cada arquivo tem só uma das duas últimas) e `anp/producao-fdp-terra-anual` (partição `ano`). Um Parquet por CSV: `producao-fdp-terra_<período>.parquet`.
- Todas as colunas são texto, com o cabeçalho da fonte (inclusive os colchetes de 2022 em diante). A coluna `Ano` do CSV não chega ao lake, exceto na forma `[Ano]`, porque `ano` é partição. Nos arquivos plurianuais, `ano` é o último ano da faixa (o `1941-1966` fica em `ano=1966`).

## Cuidados de uso

- **Valores em texto, com vírgula decimal e, em arquivos recentes, ponto de milhar.** Todas as colunas são texto: `1234,567` precisa de `replace(',', '.')` e cast antes de somar. No arquivo do 1º trimestre de 2026 da amostra (`producao-fdp-terra`), valores a partir de mil vêm com ponto de milhar (`2.229,59`, em 6.628 linhas de água, por exemplo); nos arquivos de 2025 e anteriores da amostra não há ponto algum. Tire o ponto de milhar antes de trocar a vírgula (`replace(replace(x, '.', ''), ',', '.')`), mas só nos arquivos que o usam.
- **Valores negativos.** Há três linhas de produção de água negativa (por exemplo `-0,0268`) no arquivo de 2013 a 2015 de mar da amostra; a fonte não explica.
- **Uma linha por poço, mês e tipo de registro, sem chave.** Em 2023 (amostra de `producao-mar` com 14.824 linhas), `(mês, poço)` aparece em 9.574 pares distintos: as linhas de produção (colunas `Produção...` preenchidas) e as de injeção (colunas `Injeção...` preenchidas) ficam em registros separados, e só 20 linhas têm os dois grupos preenchidos. Por isso a chave do dataset fica vazia; some por poço e mês antes de ligar a outras tabelas.
- **Ausente é diferente de zero.** Em linhas de produção, as colunas de injeção vêm vazias (e vice-versa); `0` é um volume informado. Nos arquivos históricos (1941 a 1979) todas as colunas de injeção estão vazias.
- **Unidades.** `(m³)` é metro cúbico e `(Mm³)` é mil metros cúbicos (milhares de m³), a notação da ANP; gás e líquidos não estão na mesma unidade. O volume é do mês de referência, não uma vazão diária.
- **Defeito do arquivo de origem: linhas inteiras entre aspas.** Em alguns CSV, a maioria das linhas de dados vem com a linha toda dentro de aspas (por exemplo `"2019,01/2019,Alagoas,Alagoas,PARU,..."`), e o leitor do conversor as trata como um único campo. Nas amostras: `producao-mar-2019` (15.155 de 22.173 linhas) e `producao-mar-2020`, e em terra o arquivo trimestral de 2021. Nos datasets sem a coluna `Ano` essas linhas viram linhas totalmente vazias; em `producao-mar`, a linha inteira fica dentro da coluna `Ano`. Os volumes dessas linhas se perdem no lake. Conferido só nas amostras.
- **Cabeçalho muda de grafia.** A partir de 2022 os nomes das colunas chegam entre colchetes (`[Ano]`, `[Mês/Ano]`, `[Poço]`...), e o conversor não os remove: o mesmo campo vira duas colunas no esquema (`Poço` e `[Poço]`), cada uma preenchida só nos arquivos da sua era (sem colchetes até 2021, com colchetes de 2022 em diante). Ao empilhar, una por nome com `union_by_name` e `coalesce` dos pares, ou renomeie removendo os colchetes.
- **Duplicata no lake.** 80 arquivos são comuns a `producao-terra`; empilhar os dois grupos dobra os volumes (na amostra, o 1º trimestre de 2025 tem 29.802 linhas e 4.025.387 bytes nos dois).
- **Lacuna.** Os trimestres de 2026 posteriores ao 1º (que a ANP já publica) e o de 2019 com o nome `producao-terra-2019-4trim.csv` não estão neste grupo; veja `producao-terra` para eles.
- **`ano` e `semestre`/`mes` são partições.** Em `ano=2019/mes=06` estão abril a junho de 2019 (3 meses na amostra); `mes` é o último mês do trimestre, não o mês do dado. O mês do dado está em `Mês/Ano`.
- **`Ambiente` em duas grafias.** `Terra` até 2021 e `TERRA` de 2022 em diante.
- **Dados pessoais.** Não há dados pessoais: nomes de poços, campos e instalações, sem dados de pessoas.

## Exemplos

Produção mensal de óleo e de gás associado por bacia, no arquivo trimestral mais recente da amostra (os valores vêm em texto, com vírgula decimal, e a coluna tem colchetes nesta era):

```python
import duckdb

duckdb.sql("""
    SELECT "[Estado]" AS estado,
           round(sum(replace(replace("[Produção de Óleo (m³)]", '.', ''), ',', '.')::DOUBLE)) AS oleo_m3,
           round(sum(replace(replace("[Produção de Gás Associado (Mm³)]", '.', ''), ',', '.')::DOUBLE)) AS gas_associado_mil_m3,
           count(DISTINCT "[Poço]") AS pocos
    FROM read_parquet('lake/anp/producao-fdp-terra/ano=2026/mes=03/*.parquet')
    WHERE "[Produção de Óleo (m³)]" IS NOT NULL
    GROUP BY 1
    ORDER BY oleo_m3 DESC
""").show()
```

## Referências

- Produção de petróleo e gás natural, fase de desenvolvimento e produção (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadados (.docx) "Produção poço - TERRA": https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-producao-de-petroleo-e-gas-natural-nacional/metadados-terra.docx
