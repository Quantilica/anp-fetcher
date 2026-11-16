---
dataset:
  id: producao-terra
  fonte: anp
  titulo: Produção de petróleo e gás natural em terra, por poço e mês
  resumo: Produção e injeção mensais por poço terrestre no Brasil, de 1941 em diante, em 83 arquivos da ANP (trimestrais, semestrais, anuais e históricos) separados em três tabelas no lake.
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
    chave: []
    colunas: 42
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
    mudanca: arquivos históricos plurianuais (1941-1966 a 1981-1982) e anuais (1983 a 1988); lote antigo sem arquivos de 1989 a 1999 neste grupo
  - desde: '2000'
    mudanca: arquivos semestrais de 2000 a 2015 (`ano/semestre`); a coluna `Ano` do CSV é descartada porque `ano` é partição
  - desde: '2016'
    mudanca: arquivos trimestrais de 2016 a 2026 (nome `producao-terra-<N>trim`, depois `producao_por_poco_terra_<ano>_<N>_trim`); não há arquivo de 2020 neste grupo
  - desde: '2022'
    mudanca: os cabeçalhos passam a vir entre colchetes, inclusive `[Ano]`; `Ambiente` passa de `Terra` a `TERRA`
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de petróleo e gás natural em terra, por poço e mês

## Resumo

Produção mensal de petróleo, condensado, gás natural e água, e injeção de fluidos, por poço terrestres no Brasil, com campo, bacia, estado e instalação. Cada linha é um poço em um mês (produção ou injeção). Os volumes vêm dos Boletins Mensais de Produção que as operadoras enviam à ANP, extraídos do SIGEP e do Do Poço ao Posto, e cobrem de meados do século XX até o mês corrente. Os arquivos mais recentes são trimestrais, os do começo dos anos 2000 semestrais e os históricos plurianuais.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/producao-terra` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal na fonte (o arquivo corrente é atualizado a cada mês, com defasagem de dois meses após o mês de produção); os arquivos são publicados por trimestre (2016 em diante), semestre, ano ou faixa de anos |
| Cobertura | 1941-12 a em-curso |
| Unidade (uma linha) | um poço terrestre em um mês de referência: uma linha de produção ou de injeção, com os volumes do mês |
| Granularidade | espacial: poço (nome ANP), com campo, bacia, estado e instalação; ambiente terra; temporal: mês de referência (`Mês/Ano`, MM/AAAA) |
| Formato bruto | CSV (UTF-8 com BOM ou, no arquivo de 2019 em mar, Latin-1), separado por vírgula, com decimal em vírgula e CRLF |
| Estado no lake | convertido |
| Partições | `ano`, `semestre` |
| Chave | — |
| Colunas | 42 |
| Unidades de medida | `Produção de Óleo (m³)`: m³ por mês; `Produção de Condensado (m³)`: m³ por mês; `Produção de Água (m³)`: m³ por mês; `Injeção de Água para Recuperação Secundária (m³)`: m³ por mês; `Injeção de Água para Descarte (m³)`: m³ por mês; `Injeção de Polímeros (m³)`: m³ por mês; `Injeção de Outros Fluidos (m³)`: m³ por mês; `Produção de Gás Associado (Mm³)`: mil m³ por mês; `Produção de Gás Não Associado (Mm³)`: mil m³ por mês; `Injeção de Gás (Mm³)`: mil m³ por mês; `Injeção de Gás Carbônico (Mm³)`: mil m³ por mês; `Injeção de Nitrogênio (Mm³)`: mil m³ por mês; `Injeção de Vapor de Água (t)`: t por mês |
| Dados pessoais | nenhum |
| Eras | 1941: arquivos históricos plurianuais (1941-1966 a 1981-1982) e anuais (1983 a 1988); lote antigo sem arquivos de 1989 a 1999 neste grupo; 2000: arquivos semestrais de 2000 a 2015 (`ano/semestre`); a coluna `Ano` do CSV é descartada porque `ano` é partição; 2016: arquivos trimestrais de 2016 a 2026 (nome `producao-terra-<N>trim`, depois `producao_por_poco_terra_<ano>_<N>_trim`); não há arquivo de 2020 neste grupo; 2022: os cabeçalhos passam a vir entre colchetes, inclusive `[Ano]`; `Ambiente` passa de `Terra` a `TERRA` |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa 83 CSV de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-producao-de-petroleo-e-gas-natural-nacional/pt/`, em pastas por período: `2025/` a `2016/` (trimestrais; nomes `producao_por_poco_terra_<ano>_<N>_trim.csv` de 2021 a 2026 e `producao-terra-<ano>-<N>trim.csv`, com variações, de 2016 a 2019), `2000/` a `2015/` (semestrais, `producao-terra-<ano>-<N>sem.csv`), `1988-1983/` (anuais) e `1982-1941/` (históricos plurianuais).
- Fonte do dado, segundo o metadado "Produção poço - TERRA" (criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; atualização mensal; contato demandas_sdp@anp.gov.br.
- **Sobreposição com `producao-fdp-terra`:** 80 dos 83 URLs são os mesmos do grupo `producao-fdp-terra`, que tem 107 arquivos (inclui 1989 a 1999 e 2020). Só `producao-terra` traz `producao-terra-2019-4trim.csv`, `producao_por_poco_terra_2026_2_trim.csv` e `producao_por_poco_terra_2026_3_trim.csv` (comparação dos nomes de arquivo no catálogo, 2026-11-15). O período de 2019 4º trimestre também aparece em `producao-fdp-terra` com outro nome de arquivo.
- No bruto, o arquivo é `producao-terra*/producao-terra-<...>@AAAAMMDD.csv`, em que o sufixo é a data da coleta; o servidor não informa a data de modificação.

## Conteúdo

- **Um poço em um mês.** Cada linha traz a produção (óleo, condensado, gás associado e não associado, água) ou a injeção de um poço terrestre, com campo, bacia, estado e instalação.
- **Três tabelas no lake**, por granularidade do arquivo (o conversor exige a mesma profundidade de partições):

| Dataset do lake | Partições | Arquivos de origem | Amostra |
|---|---|---|---|
| `producao-terra` | `ano`, `semestre` | semestrais, 2000 a 2015 | 2001 S1 (44.747 linhas), 2011 S2 (61.296) |
| `producao-terra-anual` | `ano` | trimestrais (2016 a 2026) e anuais (1983 a 1988), cada um em um Parquet do ano | 2021 2º tri (38.513), 2025 1º tri (29.802), 2025 2º tri (30.190) |
| `producao-terra-historico` | nenhuma | históricos plurianuais (1941-1966 a 1981-1982) | 1941-1966 (47.254 linhas, dez/1941 a dez/1966) |

- **Arquivos trimestrais no `-anual`.** Vários arquivos do mesmo ano (um por trimestre) ficam na partição `ano=<ano>`, com o número do trimestre no nome do Parquet (`producao-terra-02_2021.parquet` é o 2º trimestre).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2001 | `producao-terra` (20) |
| 2011 | `producao-terra` (20) |
| 2021 | `producao-terra-anual` (20) |
| 2025 | `producao-terra-anual` (21); `producao-terra-anual` (21) |

## Variáveis

As descrições vêm dos metadados `.docx` da ANP "Produção poço - TERRA" (criados em junho de 2026), um por ambiente, com colunas idênticas; a observação sobre as unidades e as grafias vem da amostra do lake (2026-11-15).
Os metadados descrevem a era mais nova, dos nomes sem colchetes: as colunas com colchetes têm a descrição do campo homônimo. O metadado diz que o ano é número e o mês/ano é data MM/AAAA; no lake todas as colunas são texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Mês/Ano` | `Mês/Ano` | texto | Mês e ano da produção, no formato MM/AAAA (texto). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Estado` | `Estado` | texto | Estado da Federação (nome por extenso) do poço; vazio em algumas linhas. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar em que se localiza o poço. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Campo` | `Campo` | texto | Nome do campo. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Poço` | `Poço` | texto | Nome do poço, atribuído conforme a Resolução ANP nº 699/2017. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Ambiente` | `Ambiente` | texto | Ambiente geográfico da produção, terra ou mar (`Mar`/`Terra` nos arquivos antigos e `MAR`/`TERRA` nos de 2022 em diante). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Instalação` | `Instalação` | texto | Instalação à qual o poço está interligado (`Não Informado` nos arquivos antigos, que não trazem instalação). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Produção de Óleo (m³)` | `Produção de Óleo (m³)` | texto | Volume de óleo produzido no mês, em m³ (texto com vírgula decimal). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Produção de Condensado (m³)` | `Produção de Condensado (m³)` | texto | Volume de condensado produzido no mês, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Produção de Gás Associado (Mm³)` | `Produção de Gás Associado (Mm³)` | texto | Volume de gás natural associado produzido no mês, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Produção de Gás Não Associado (Mm³)` | `Produção de Gás Não Associado (Mm³)` | texto | Volume de gás natural não associado produzido no mês, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Produção de Água (m³)` | `Produção de Água (m³)` | texto | Volume de água produzida no mês, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Gás (Mm³)` | `Injeção de Gás (Mm³)` | texto | Volume de gás natural injetado para recuperação secundária e/ou armazenamento, em milhares de m³ (o metadado da ANP escreve `(m³)` no nome e `milhares de metros cúbicos` na descrição). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Água para Recuperação Secundária (m³)` | `Injeção de Água para Recuperação Secundária (m³)` | texto | Volume de água injetada para recuperação secundária, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Água para Descarte (m³)` | `Injeção de Água para Descarte (m³)` | texto | Volume de água injetada para descarte, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Gás Carbônico (Mm³)` | `Injeção de Gás Carbônico (Mm³)` | texto | Volume de gás carbônico injetado, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Nitrogênio (Mm³)` | `Injeção de Nitrogênio (Mm³)` | texto | Volume de nitrogênio injetado, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Vapor de Água (t)` | `Injeção de Vapor de Água (t)` | texto | Vapor de água injetado, em toneladas (o metadado fala em "volume", mas a unidade é massa). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Polímeros (m³)` | `Injeção de Polímeros (m³)` | texto | Volume de polímeros injetado, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `Injeção de Outros Fluidos (m³)` | `Injeção de Outros Fluidos (m³)` | texto | Volume de outros tipos de fluidos injetado, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 2001 a 2021 | `producao-terra`, `producao-terra-anual`, `producao-terra-historico` |
| `[Ano]` | `[Ano]` | texto | Ano de referência da produção (texto). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Mês/Ano]` | `[Mês/Ano]` | texto | Mês e ano da produção, no formato MM/AAAA (texto). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Estado]` | `[Estado]` | texto | Estado da Federação (nome por extenso) do poço; vazio em algumas linhas. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Bacia]` | `[Bacia]` | texto | Nome da bacia sedimentar em que se localiza o poço. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Campo]` | `[Campo]` | texto | Nome do campo. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Poço]` | `[Poço]` | texto | Nome do poço, atribuído conforme a Resolução ANP nº 699/2017. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Ambiente]` | `[Ambiente]` | texto | Ambiente geográfico da produção, terra ou mar (`Mar`/`Terra` nos arquivos antigos e `MAR`/`TERRA` nos de 2022 em diante). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Instalação]` | `[Instalação]` | texto | Instalação à qual o poço está interligado (`Não Informado` nos arquivos antigos, que não trazem instalação). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Produção de Óleo (m³)]` | `[Produção de Óleo (m³)]` | texto | Volume de óleo produzido no mês, em m³ (texto com vírgula decimal). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Produção de Condensado (m³)]` | `[Produção de Condensado (m³)]` | texto | Volume de condensado produzido no mês, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Produção de Gás Associado (Mm³)]` | `[Produção de Gás Associado (Mm³)]` | texto | Volume de gás natural associado produzido no mês, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Produção de Gás Não Associado (Mm³)]` | `[Produção de Gás Não Associado (Mm³)]` | texto | Volume de gás natural não associado produzido no mês, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Produção de Água (m³)]` | `[Produção de Água (m³)]` | texto | Volume de água produzida no mês, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Gás (Mm³)]` | `[Injeção de Gás (Mm³)]` | texto | Volume de gás natural injetado para recuperação secundária e/ou armazenamento, em milhares de m³ (o metadado da ANP escreve `(m³)` no nome e `milhares de metros cúbicos` na descrição). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Água para Recuperação Secundária (m³)]` | `[Injeção de Água para Recuperação Secundária (m³)]` | texto | Volume de água injetada para recuperação secundária, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Água para Descarte (m³)]` | `[Injeção de Água para Descarte (m³)]` | texto | Volume de água injetada para descarte, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Gás Carbônico (Mm³)]` | `[Injeção de Gás Carbônico (Mm³)]` | texto | Volume de gás carbônico injetado, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Nitrogênio (Mm³)]` | `[Injeção de Nitrogênio (Mm³)]` | texto | Volume de nitrogênio injetado, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Vapor de Água (t)]` | `[Injeção de Vapor de Água (t)]` | texto | Vapor de água injetado, em toneladas (o metadado fala em "volume", mas a unidade é massa). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Polímeros (m³)]` | `[Injeção de Polímeros (m³)]` | texto | Volume de polímeros injetado, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `[Injeção de Outros Fluidos (m³)]` | `[Injeção de Outros Fluidos (m³)]` | texto | Volume de outros tipos de fluidos injetado, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2025 | `producao-terra-anual` |
| `Ano` | `Ano` | texto | Ano de referência da produção (texto). Cabeçalho sem colchetes, nos arquivos até 2021. | — | — | `producao-terra-historico` |

## No lake

- Datasets do lake com esquema comum: `anp/producao-terra` (partições `ano` e `semestre=S1|S2`), `anp/producao-terra-anual` (partição `ano`) e `anp/producao-terra-historico` (sem partição). Um Parquet por CSV.
- Todas as colunas são texto, com o cabeçalho da fonte (inclusive os colchetes de 2022 em diante). A coluna `Ano` do CSV não chega ao lake nos arquivos particionados por `ano`, exceto na forma `[Ano]`; em `producao-terra-historico`, que não é particionado, `Ano` existe.

## Cuidados de uso

- **Valores em texto, com vírgula decimal e, em arquivos recentes, ponto de milhar.** Todas as colunas são texto: `1234,567` precisa de `replace(',', '.')` e cast antes de somar. No arquivo do 1º trimestre de 2026 da amostra (`producao-fdp-terra`), valores a partir de mil vêm com ponto de milhar (`2.229,59`, em 6.628 linhas de água, por exemplo); nos arquivos de 2025 e anteriores da amostra não há ponto algum. Tire o ponto de milhar antes de trocar a vírgula (`replace(replace(x, '.', ''), ',', '.')`), mas só nos arquivos que o usam.
- **Valores negativos.** Há três linhas de produção de água negativa (por exemplo `-0,0268`) no arquivo de 2013 a 2015 de mar da amostra; a fonte não explica.
- **Uma linha por poço, mês e tipo de registro, sem chave.** Em 2023 (amostra de `producao-mar` com 14.824 linhas), `(mês, poço)` aparece em 9.574 pares distintos: as linhas de produção (colunas `Produção...` preenchidas) e as de injeção (colunas `Injeção...` preenchidas) ficam em registros separados, e só 20 linhas têm os dois grupos preenchidos. Por isso a chave do dataset fica vazia; some por poço e mês antes de ligar a outras tabelas.
- **Ausente é diferente de zero.** Em linhas de produção, as colunas de injeção vêm vazias (e vice-versa); `0` é um volume informado. Nos arquivos históricos (1941 a 1979) todas as colunas de injeção estão vazias.
- **Unidades.** `(m³)` é metro cúbico e `(Mm³)` é mil metros cúbicos (milhares de m³), a notação da ANP; gás e líquidos não estão na mesma unidade. O volume é do mês de referência, não uma vazão diária.
- **Defeito do arquivo de origem: linhas inteiras entre aspas.** Em alguns CSV, a maioria das linhas de dados vem com a linha toda dentro de aspas (por exemplo `"2019,01/2019,Alagoas,Alagoas,PARU,..."`), e o leitor do conversor as trata como um único campo. Nas amostras: `producao-mar-2019` (15.155 de 22.173 linhas) e `producao-mar-2020`, e em terra o arquivo trimestral de 2021. Nos datasets sem a coluna `Ano` essas linhas viram linhas totalmente vazias; em `producao-mar`, a linha inteira fica dentro da coluna `Ano`. Os volumes dessas linhas se perdem no lake. Conferido só nas amostras.
- **Cabeçalho muda de grafia.** A partir de 2022 os nomes das colunas chegam entre colchetes (`[Ano]`, `[Mês/Ano]`, `[Poço]`...), e o conversor não os remove: o mesmo campo vira duas colunas no esquema (`Poço` e `[Poço]`), cada uma preenchida só nos arquivos da sua era (sem colchetes até 2021, com colchetes de 2022 em diante). Ao empilhar, una por nome com `union_by_name` e `coalesce` dos pares, ou renomeie removendo os colchetes.
- **Lacunas neste grupo.** `producao-terra` não tem os semestres de 1989 a 1999 nem os trimestres de 2020, que estão em `producao-fdp-terra`, e tem 2026 2º e 3º trimestres que `producao-fdp-terra` não traz. Para a série completa, use `producao-fdp-terra`, acrescentando os trimestres de 2026 que só este grupo tem.
- **Duplicata no lake.** 80 arquivos são comuns aos dois grupos; empilhar os datasets dobra os volumes (na amostra, o arquivo do 1º trimestre de 2025 tem 29.802 linhas e 4.025.387 bytes nos dois).
- **Perda de linhas em 2021.** Na amostra do 2º trimestre de 2021 (`producao-terra-anual`, `ano=2021`), 23.619 das 38.513 linhas ficaram totalmente vazias por causa do defeito das aspas; só 14.894 têm dado.
- **`Ambiente` em duas grafias.** `Terra` até 2021 e `TERRA` de 2022 em diante.
- **Estado não cadastrado.** `[Estado]` traz o texto `(NÃO CADASTRADO)` em poços sem estado cadastrado (um poço no 2º trimestre de 2025 da amostra).
- **Ano da partição.** Nos arquivos plurianuais, `ano` é o último ano da faixa; nos anuais e trimestrais de 2016 em diante é o ano do dado.
- **Dados pessoais.** Não há dados pessoais: nomes de poços, campos e instalações, sem dados de pessoas.

## Exemplos

Produção mensal de óleo e de gás associado por bacia, no arquivo trimestral mais recente da amostra (os valores vêm em texto, com vírgula decimal, e a coluna tem colchetes nesta era):

```python
import duckdb

duckdb.sql("""
    SELECT "[Estado]" AS estado,
           round(sum(replace("[Produção de Óleo (m³)]", ',', '.')::DOUBLE)) AS oleo_m3,
           round(sum(replace("[Produção de Gás Associado (Mm³)]", ',', '.')::DOUBLE)) AS gas_associado_mil_m3,
           count(DISTINCT "[Poço]") AS pocos
    FROM read_parquet('lake/anp/producao-terra-anual/ano=2025/producao-terra-02_2025.parquet')
    WHERE "[Produção de Óleo (m³)]" IS NOT NULL
    GROUP BY 1
    ORDER BY oleo_m3 DESC
""").show()
```

## Referências

- Produção de petróleo e gás natural, fase de desenvolvimento e produção (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadados (.docx) "Produção poço - TERRA": https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-producao-de-petroleo-e-gas-natural-nacional/metadados-terra.docx
