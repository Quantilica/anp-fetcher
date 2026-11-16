---
dataset:
  id: producao-fdp-mar
  fonte: anp
  titulo: Produção de petróleo e gás natural em mar, por poço e mês (fase de desenvolvimento e produção)
  resumo: Produção e injeção mensais por poço marítimo no Brasil, de 1954 em diante, nos mesmos 18 arquivos da ANP de `producao-mar`, particionados por ano.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal na fonte (o arquivo corrente é atualizado a cada mês, com defasagem de dois meses após o mês de produção); os arquivos são publicados por trimestre (2016 em diante), semestre, ano ou faixa de anos
  cobertura:
    inicio: 1954-12
    fim: em-curso
  unidade: 'um poço marítimo em um mês de referência: uma linha de produção ou de injeção, com os volumes do mês'
  granularidade:
    espacial: poço (nome ANP), com campo, bacia, estado e instalação; ambiente mar
    temporal: mês de referência (`Mês/Ano`, MM/AAAA)
  formato_bruto: CSV (UTF-8 com BOM ou, no arquivo de 2019 em mar, Latin-1), separado por vírgula, com decimal em vírgula e CRLF
  lake:
    estado: convertido
    particoes:
    - ano
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
  - desde: '1954'
    mudanca: arquivos plurianuais (1941-1979 a 2016-2018) e anuais (2019 a 2021) com cabeçalho sem colchetes; a coluna `Ano` do CSV é descartada pelo conversor porque `ano` é partição; o arquivo de 1941-1979 não informa a instalação
  - desde: '2019'
    mudanca: o arquivo de 2019 está em Latin-1, e os de 2019 e 2020 trazem a maior parte das linhas inteiras entre aspas, que no lake viram linhas vazias (veja Cuidados de uso)
  - desde: '2022'
    mudanca: os cabeçalhos passam a vir entre colchetes, inclusive `[Ano]`, que então é mantida como coluna; `Ambiente` passa de `Mar` a `MAR`
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de petróleo e gás natural em mar, por poço e mês (fase de desenvolvimento e produção)

## Resumo

Produção mensal de petróleo, condensado, gás natural e água, e injeção de fluidos, por poço marítimos no Brasil, com campo, bacia, estado e instalação. Cada linha é um poço em um mês (produção ou injeção). Os volumes vêm dos Boletins Mensais de Produção que as operadoras enviam à ANP, extraídos do SIGEP e do Do Poço ao Posto, e cobrem de meados do século XX até o mês corrente. Os arquivos mais recentes são trimestrais, os do começo dos anos 2000 semestrais e os históricos plurianuais.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/producao-fdp-mar` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal na fonte (o arquivo corrente é atualizado a cada mês, com defasagem de dois meses após o mês de produção); os arquivos são publicados por trimestre (2016 em diante), semestre, ano ou faixa de anos |
| Cobertura | 1954-12 a em-curso |
| Unidade (uma linha) | um poço marítimo em um mês de referência: uma linha de produção ou de injeção, com os volumes do mês |
| Granularidade | espacial: poço (nome ANP), com campo, bacia, estado e instalação; ambiente mar; temporal: mês de referência (`Mês/Ano`, MM/AAAA) |
| Formato bruto | CSV (UTF-8 com BOM ou, no arquivo de 2019 em mar, Latin-1), separado por vírgula, com decimal em vírgula e CRLF |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 41 |
| Unidades de medida | `Produção de Óleo (m³)`: m³ por mês; `Produção de Condensado (m³)`: m³ por mês; `Produção de Água (m³)`: m³ por mês; `Injeção de Água para Recuperação Secundária (m³)`: m³ por mês; `Injeção de Água para Descarte (m³)`: m³ por mês; `Injeção de Polímeros (m³)`: m³ por mês; `Injeção de Outros Fluidos (m³)`: m³ por mês; `Produção de Gás Associado (Mm³)`: mil m³ por mês; `Produção de Gás Não Associado (Mm³)`: mil m³ por mês; `Injeção de Gás (Mm³)`: mil m³ por mês; `Injeção de Gás Carbônico (Mm³)`: mil m³ por mês; `Injeção de Nitrogênio (Mm³)`: mil m³ por mês; `Injeção de Vapor de Água (t)`: t por mês |
| Dados pessoais | nenhum |
| Eras | 1954: arquivos plurianuais (1941-1979 a 2016-2018) e anuais (2019 a 2021) com cabeçalho sem colchetes; a coluna `Ano` do CSV é descartada pelo conversor porque `ano` é partição; o arquivo de 1941-1979 não informa a instalação; 2019: o arquivo de 2019 está em Latin-1, e os de 2019 e 2020 trazem a maior parte das linhas inteiras entre aspas, que no lake viram linhas vazias (veja Cuidados de uso); 2022: os cabeçalhos passam a vir entre colchetes, inclusive `[Ano]`, que então é mantida como coluna; `Ambiente` passa de `Mar` a `MAR` |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa os mesmos 18 CSV de `producao-mar`, de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-producao-de-petroleo-e-gas-natural-nacional/pm/`: um por ano de 2019 a 2026 (`producao-mar-<ano>.csv`; o de 2024 se chama `producao_por_poco_2024.csv`) e dez plurianuais, de `producao-mar-1941-1979.csv` a `producao-mar-2016-2018.csv`. Os 18 URLs são idênticos aos de `producao-mar` (conferido no catálogo em 2026-11-15).
- Fonte do dado, segundo o metadado "Produção poço - MAR" (criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; atualização mensal; contato demandas_sdp@anp.gov.br.
- No bruto, o arquivo é `producao-fdp-mar/producao-fdp-mar_<ano>@AAAAMMDD.csv`, em que `<ano>` é o último ano do período do arquivo (o plurianual `1941-1979` fica como `1979`) e o sufixo é a data da coleta; o servidor não informa a data de modificação.

## Conteúdo

- **Um poço em um mês.** Cada linha traz a produção (óleo, condensado, gás associado e não associado, água) ou a injeção (gás, água, CO2, nitrogênio, vapor, polímeros, outros) de um poço marítimo, com campo, bacia, estado e instalação de destino.
- **Séries.** O arquivo `ano=1979` cobre dezembro de 1954 a dezembro de 1979 (301 meses na amostra); `ano=2000`, 1998 a 2000; `ano=2015`, 2013 a 2015; `ano=2019`, `2020` e `2023` são anuais. Contagens de linhas na amostra: 61.295, 28.095, 38.758, 22.173, 21.815 e 14.824.
- **Poços e campos.** Em 2023 a amostra tem 1.013 poços em 75 campos de 8 bacias, com `[Ambiente]` sempre `MAR`.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 1979 | `producao-fdp-mar` (20) |
| 2000 | `producao-fdp-mar` (20) |
| 2015 | `producao-fdp-mar` (20) |
| 2019 | `producao-fdp-mar` (20) |
| 2020 | `producao-fdp-mar` (20) |
| 2023 | `producao-fdp-mar` (21) |

## Variáveis

As descrições vêm dos metadados `.docx` da ANP "Produção poço - MAR" (criados em junho de 2026), um por ambiente, com colunas idênticas; a observação sobre as unidades e as grafias vem da amostra do lake (2026-11-15).
Os metadados descrevem a era mais nova, dos nomes sem colchetes: as colunas com colchetes têm a descrição do campo homônimo. O metadado diz que o ano é número e o mês/ano é data MM/AAAA; no lake todas as colunas são texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Mês/Ano` | `Mês/Ano` | texto | Mês e ano da produção, no formato MM/AAAA (texto). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Estado` | `Estado` | texto | Estado da Federação (nome por extenso) do poço; vazio em algumas linhas. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar em que se localiza o poço. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Campo` | `Campo` | texto | Nome do campo. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Poço` | `Poço` | texto | Nome do poço, atribuído conforme a Resolução ANP nº 699/2017. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Ambiente` | `Ambiente` | texto | Ambiente geográfico da produção, terra ou mar (`Mar`/`Terra` nos arquivos antigos e `MAR`/`TERRA` nos de 2022 em diante). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Instalação` | `Instalação` | texto | Instalação à qual o poço está interligado (`Não Informado` nos arquivos antigos, que não trazem instalação). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Produção de Óleo (m³)` | `Produção de Óleo (m³)` | texto | Volume de óleo produzido no mês, em m³ (texto com vírgula decimal). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Produção de Condensado (m³)` | `Produção de Condensado (m³)` | texto | Volume de condensado produzido no mês, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Produção de Gás Associado (Mm³)` | `Produção de Gás Associado (Mm³)` | texto | Volume de gás natural associado produzido no mês, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Produção de Gás Não Associado (Mm³)` | `Produção de Gás Não Associado (Mm³)` | texto | Volume de gás natural não associado produzido no mês, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Produção de Água (m³)` | `Produção de Água (m³)` | texto | Volume de água produzida no mês, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Gás (Mm³)` | `Injeção de Gás (Mm³)` | texto | Volume de gás natural injetado para recuperação secundária e/ou armazenamento, em milhares de m³ (o metadado da ANP escreve `(m³)` no nome e `milhares de metros cúbicos` na descrição). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Água para Recuperação Secundária (m³)` | `Injeção de Água para Recuperação Secundária (m³)` | texto | Volume de água injetada para recuperação secundária, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Água para Descarte (m³)` | `Injeção de Água para Descarte (m³)` | texto | Volume de água injetada para descarte, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Gás Carbônico (Mm³)` | `Injeção de Gás Carbônico (Mm³)` | texto | Volume de gás carbônico injetado, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Nitrogênio (Mm³)` | `Injeção de Nitrogênio (Mm³)` | texto | Volume de nitrogênio injetado, em milhares de m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Vapor de Água (t)` | `Injeção de Vapor de Água (t)` | texto | Vapor de água injetado, em toneladas (o metadado fala em "volume", mas a unidade é massa). Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Polímeros (m³)` | `Injeção de Polímeros (m³)` | texto | Volume de polímeros injetado, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `Injeção de Outros Fluidos (m³)` | `Injeção de Outros Fluidos (m³)` | texto | Volume de outros tipos de fluidos injetado, em m³. Cabeçalho sem colchetes, nos arquivos até 2021. | — | 1979 a 2020 |
| `[Ano]` | `[Ano]` | texto | Ano de referência da produção (texto). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Mês/Ano]` | `[Mês/Ano]` | texto | Mês e ano da produção, no formato MM/AAAA (texto). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Estado]` | `[Estado]` | texto | Estado da Federação (nome por extenso) do poço; vazio em algumas linhas. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Bacia]` | `[Bacia]` | texto | Nome da bacia sedimentar em que se localiza o poço. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Campo]` | `[Campo]` | texto | Nome do campo. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Poço]` | `[Poço]` | texto | Nome do poço, atribuído conforme a Resolução ANP nº 699/2017. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Ambiente]` | `[Ambiente]` | texto | Ambiente geográfico da produção, terra ou mar (`Mar`/`Terra` nos arquivos antigos e `MAR`/`TERRA` nos de 2022 em diante). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Instalação]` | `[Instalação]` | texto | Instalação à qual o poço está interligado (`Não Informado` nos arquivos antigos, que não trazem instalação). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Produção de Óleo (m³)]` | `[Produção de Óleo (m³)]` | texto | Volume de óleo produzido no mês, em m³ (texto com vírgula decimal). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Produção de Condensado (m³)]` | `[Produção de Condensado (m³)]` | texto | Volume de condensado produzido no mês, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Produção de Gás Associado (Mm³)]` | `[Produção de Gás Associado (Mm³)]` | texto | Volume de gás natural associado produzido no mês, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Produção de Gás Não Associado (Mm³)]` | `[Produção de Gás Não Associado (Mm³)]` | texto | Volume de gás natural não associado produzido no mês, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Produção de Água (m³)]` | `[Produção de Água (m³)]` | texto | Volume de água produzida no mês, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Gás (Mm³)]` | `[Injeção de Gás (Mm³)]` | texto | Volume de gás natural injetado para recuperação secundária e/ou armazenamento, em milhares de m³ (o metadado da ANP escreve `(m³)` no nome e `milhares de metros cúbicos` na descrição). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Água para Recuperação Secundária (m³)]` | `[Injeção de Água para Recuperação Secundária (m³)]` | texto | Volume de água injetada para recuperação secundária, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Água para Descarte (m³)]` | `[Injeção de Água para Descarte (m³)]` | texto | Volume de água injetada para descarte, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Gás Carbônico (Mm³)]` | `[Injeção de Gás Carbônico (Mm³)]` | texto | Volume de gás carbônico injetado, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Nitrogênio (Mm³)]` | `[Injeção de Nitrogênio (Mm³)]` | texto | Volume de nitrogênio injetado, em milhares de m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Vapor de Água (t)]` | `[Injeção de Vapor de Água (t)]` | texto | Vapor de água injetado, em toneladas (o metadado fala em "volume", mas a unidade é massa). Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Polímeros (m³)]` | `[Injeção de Polímeros (m³)]` | texto | Volume de polímeros injetado, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |
| `[Injeção de Outros Fluidos (m³)]` | `[Injeção de Outros Fluidos (m³)]` | texto | Volume de outros tipos de fluidos injetado, em m³. Cabeçalho com colchetes, nos arquivos de 2022 em diante. | — | 2023 |

## No lake

- Dataset `anp/producao-fdp-mar`, particionado por `ano`: um Parquet por CSV, `ano=<ano>/producao-fdp-mar_<ano>.parquet`. Nos arquivos plurianuais, `ano` é o **último** ano da faixa (`ano=1979` contém 1954 a 1979, `ano=2015` contém 2013 a 2015); o ano do dado está em `Mês/Ano`.
- Todas as colunas são texto, com o cabeçalho da fonte (inclusive os colchetes de 2022 em diante). A coluna `Ano` do CSV não chega ao lake, exceto na forma `[Ano]`, porque `ano` já é partição.

## Cuidados de uso

- **Valores em texto, com vírgula decimal e, em arquivos recentes, ponto de milhar.** Todas as colunas são texto: `1234,567` precisa de `replace(',', '.')` e cast antes de somar. No arquivo do 1º trimestre de 2026 da amostra (`producao-fdp-terra`), valores a partir de mil vêm com ponto de milhar (`2.229,59`, em 6.628 linhas de água, por exemplo); nos arquivos de 2025 e anteriores da amostra não há ponto algum. Tire o ponto de milhar antes de trocar a vírgula (`replace(replace(x, '.', ''), ',', '.')`), mas só nos arquivos que o usam.
- **Valores negativos.** Há três linhas de produção de água negativa (por exemplo `-0,0268`) no arquivo de 2013 a 2015 de mar da amostra; a fonte não explica.
- **Uma linha por poço, mês e tipo de registro, sem chave.** Em 2023 (amostra de `producao-mar` com 14.824 linhas), `(mês, poço)` aparece em 9.574 pares distintos: as linhas de produção (colunas `Produção...` preenchidas) e as de injeção (colunas `Injeção...` preenchidas) ficam em registros separados, e só 20 linhas têm os dois grupos preenchidos. Por isso a chave do dataset fica vazia; some por poço e mês antes de ligar a outras tabelas.
- **Ausente é diferente de zero.** Em linhas de produção, as colunas de injeção vêm vazias (e vice-versa); `0` é um volume informado. Nos arquivos históricos (1941 a 1979) todas as colunas de injeção estão vazias.
- **Unidades.** `(m³)` é metro cúbico e `(Mm³)` é mil metros cúbicos (milhares de m³), a notação da ANP; gás e líquidos não estão na mesma unidade. O volume é do mês de referência, não uma vazão diária.
- **Defeito do arquivo de origem: linhas inteiras entre aspas.** Em alguns CSV, a maioria das linhas de dados vem com a linha toda dentro de aspas (por exemplo `"2019,01/2019,Alagoas,Alagoas,PARU,..."`), e o leitor do conversor as trata como um único campo. Nas amostras: `producao-mar-2019` (15.155 de 22.173 linhas) e `producao-mar-2020`, e em terra o arquivo trimestral de 2021. Nos datasets sem a coluna `Ano` essas linhas viram linhas totalmente vazias; em `producao-mar`, a linha inteira fica dentro da coluna `Ano`. Os volumes dessas linhas se perdem no lake. Conferido só nas amostras.
- **Cabeçalho muda de grafia.** A partir de 2022 os nomes das colunas chegam entre colchetes (`[Ano]`, `[Mês/Ano]`, `[Poço]`...), e o conversor não os remove: o mesmo campo vira duas colunas no esquema (`Poço` e `[Poço]`), cada uma preenchida só nos arquivos da sua era (sem colchetes até 2021, com colchetes de 2022 em diante). Ao empilhar, una por nome com `union_by_name` e `coalesce` dos pares, ou renomeie removendo os colchetes.
- **Duplicata no lake.** `producao-fdp-mar` e `producao-mar` convertem os mesmos 18 arquivos; empilhar os dois dobra os volumes. A diferença é só o esquema: este tem a partição `ano`, mas, nos plurianuais, ela é o último ano da faixa.
- **Perda de linhas em 2019 e 2020.** Como a coluna `Ano` é descartada, as linhas que o CSV traz inteiras entre aspas aparecem como linhas totalmente vazias: 15.155 das 22.173 em `ano=2019` e 13.972 das 21.815 em `ano=2020` (22.173 menos 7.018 e 21.815 menos 7.843 com `Mês/Ano` preenchido). Elas têm de ser lidas do CSV de origem.
- **Sem instalação nos arquivos antigos.** No arquivo de 1941-1979, `Instalação` vale `Não Informado` em todas as linhas e as colunas de injeção estão vazias.
- **`Ambiente` em duas grafias.** `Mar` nos arquivos até 2021 e `MAR` de 2022 em diante; use `upper()`.
- **Dados pessoais.** Não há dados pessoais: nomes de poços, campos e instalações, sem dados de pessoas.

## Exemplos

Produção mensal de óleo e de gás associado por bacia, no arquivo trimestral mais recente da amostra (os valores vêm em texto, com vírgula decimal, e a coluna tem colchetes nesta era):

```python
import duckdb

duckdb.sql("""
    SELECT "[Bacia]" AS bacia,
           round(sum(replace("[Produção de Óleo (m³)]", ',', '.')::DOUBLE)) AS oleo_m3,
           round(sum(replace("[Produção de Gás Associado (Mm³)]", ',', '.')::DOUBLE)) AS gas_associado_mil_m3,
           count(DISTINCT "[Poço]") AS pocos
    FROM read_parquet('lake/anp/producao-fdp-mar/ano=2023/*.parquet')
    WHERE "[Mês/Ano]" = '12/2023' AND "[Produção de Óleo (m³)]" IS NOT NULL
    GROUP BY 1
    ORDER BY oleo_m3 DESC
""").show()
```

## Referências

- Produção de petróleo e gás natural, fase de desenvolvimento e produção (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadados (.docx) "Produção poço - MAR": https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/arquivos-producao-de-petroleo-e-gas-natural-nacional/metadados-mar.docx
