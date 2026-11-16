---
dataset:
  id: movimentacao-gn
  fonte: anp
  titulo: Movimentação de gás natural em gasodutos de transporte (dados consolidados diários)
  resumo: Volumes diários solicitados, programados e realizados, pressão, alocação e perdas do gás natural movimentado nos gasodutos de transporte, por carregador e ponto, em arquivos mensais desde 2021.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-consolidados-movimentacao-de-gas-natural-em-gasodutos-de-transporte
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo os metadados da ANP (versão de 12/06/2026); o catálogo do fetcher vai de janeiro de 2021 a junho de 2026, e a página oficial já lista os meses até outubro de 2026 (publicado em 10/11/2026) e dezembro de 2022
  cobertura:
    inicio: 2021-01
    fim: 2026-06
  unidade: o valor de uma variável (por exemplo, volume realizado) de um carregador, contrato e ponto de uma instalação de transporte em um dia
  granularidade:
    espacial: instalação de transporte e ponto de recebimento ou entrega (com município e UF do ponto; sem coordenadas)
    temporal: dia operacional
  formato_bruto: CSV largo, separador `;`, ISO-8859 (latin-1) e CRLF; 13 colunas de identificação mais uma coluna por dia do mês
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 17
  unidades_de_medida:
    valor: mil m³, % ou kgf/cm², conforme a coluna `unidade`
  dados_pessoais:
  - coluna: Nome do Operador da instalação de Gasoduto
    categoria: razão social ou nome de pessoa jurídica
  - coluna: Nome do Carregador que usa a Instalação de Gasoduto
    categoria: razão social ou nome de pessoa jurídica
  - coluna: Nome do Contrato da Instalação de Gasoduto
    categoria: razão social ou nome de pessoa jurídica
  eras:
  - desde: '2021'
    mudanca: 'arquivos de janeiro a dezembro de 2021 (amostra: janeiro e fevereiro): nomes de variável sem unidade (`Volume Realizado`), `unidade` vazia, com 12 variáveis (`Volume Solicitado`, `Volume Programado`, `Volume Realizado`, `Alocação`, `Pressão Média`, `Gás de Uso no Sistema`, `Gás Não Contado`, `Perdas Operacionais`, `Perdas Extraordinárias`, `Desequilíbrio Diário`, `Desequilíbrio Diário Acumulado` e `Empacotamento`); cabeçalho `Tipo da Instalação do Gasoduto`'
  - desde: '2022'
    mudanca: 'amostra de maio de 2022: nomes de variável com unidade (`Solicitado (mil m³)`, `Programado (mil m³)`, `Realizado (mil m³)`) e variáveis de alocação por carregador (`Alocação Delta (%)`, `Alocação Petrobras (%)`)'
  - desde: '2023'
    mudanca: 'amostra de outubro de 2023: volta o prefixo `Volume` (`Volume Realizado (mil m³)`) e há alocações por carregador (`Alocação Compagas`, `Galp`, `Mercurio`, `SCGAS`, `SULGAS`, `Tradener`); a ANP revisou os dados de janeiro a abril de 2024 por causa da entrada em operação de um novo ponto de recebimento da TBG em Guaruva (Santa Catarina), segundo a página'
  - desde: '2025'
    mudanca: 'amostra de fevereiro de 2025: 44 carregadores distintos, contra 6 em 2021, 14 em 2022, 27 em 2023 e 64 em 2026 (o número de carregadores cresce a cada ano da amostra)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Movimentação de gás natural em gasodutos de transporte (dados consolidados diários)

## Resumo

Dados consolidados enviados pelos transportadores à ANP sobre a movimentação de gás natural nos gasodutos de transporte, com publicação prevista no § 2º do art. 1º da Resolução ANP nº 40/2016. Para cada instalação de transporte, ponto de recebimento ou entrega, carregador e contrato, a ANP publica por dia o volume solicitado, programado e realizado, a alocação, a pressão média, o gás de uso no sistema, o gás não contado, as perdas, o desequilíbrio diário e acumulado e o empacotamento. O arquivo da fonte é largo (uma coluna por dia do mês); o lake o converte para o formato longo, com uma linha por variável e dia.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/movimentacao-gn` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-consolidados-movimentacao-de-gas-natural-em-gasodutos-de-transporte |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo os metadados da ANP (versão de 12/06/2026); o catálogo do fetcher vai de janeiro de 2021 a junho de 2026, e a página oficial já lista os meses até outubro de 2026 (publicado em 10/11/2026) e dezembro de 2022 |
| Cobertura | 2021-01 a 2026-06 |
| Unidade (uma linha) | o valor de uma variável (por exemplo, volume realizado) de um carregador, contrato e ponto de uma instalação de transporte em um dia |
| Granularidade | espacial: instalação de transporte e ponto de recebimento ou entrega (com município e UF do ponto; sem coordenadas); temporal: dia operacional |
| Formato bruto | CSV largo, separador `;`, ISO-8859 (latin-1) e CRLF; 13 colunas de identificação mais uma coluna por dia do mês |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 17 |
| Unidades de medida | `valor`: mil m³, % ou kgf/cm², conforme a coluna `unidade` |
| Dados pessoais | `Nome do Operador da instalação de Gasoduto` (razão social ou nome de pessoa jurídica); `Nome do Carregador que usa a Instalação de Gasoduto` (razão social ou nome de pessoa jurídica); `Nome do Contrato da Instalação de Gasoduto` (razão social ou nome de pessoa jurídica) |
| Eras | 2021: arquivos de janeiro a dezembro de 2021 (amostra: janeiro e fevereiro): nomes de variável sem unidade (`Volume Realizado`), `unidade` vazia, com 12 variáveis (`Volume Solicitado`, `Volume Programado`, `Volume Realizado`, `Alocação`, `Pressão Média`, `Gás de Uso no Sistema`, `Gás Não Contado`, `Perdas Operacionais`, `Perdas Extraordinárias`, `Desequilíbrio Diário`, `Desequilíbrio Diário Acumulado` e `Empacotamento`); cabeçalho `Tipo da Instalação do Gasoduto`; 2022: amostra de maio de 2022: nomes de variável com unidade (`Solicitado (mil m³)`, `Programado (mil m³)`, `Realizado (mil m³)`) e variáveis de alocação por carregador (`Alocação Delta (%)`, `Alocação Petrobras (%)`); 2023: amostra de outubro de 2023: volta o prefixo `Volume` (`Volume Realizado (mil m³)`) e há alocações por carregador (`Alocação Compagas`, `Galp`, `Mercurio`, `SCGAS`, `SULGAS`, `Tradener`); a ANP revisou os dados de janeiro a abril de 2024 por causa da entrada em operação de um novo ponto de recebimento da TBG em Guaruva (Santa Catarina), segundo a página; 2025: amostra de fevereiro de 2025: 44 carregadores distintos, contra 6 em 2021, 14 em 2022, 27 em 2023 e 64 em 2026 (o número de carregadores cresce a cada ano da amostra) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-movimentacao-de-gas-natural-em-gasodutos-de-transporte/<AAAA>/<arquivo>.csv`, um por mês, 66 entradas de 2021-01 a 2026-06; os nomes variam (`gn-janeiro-2023.csv`, `gn_novembro_2023.csv`, `gn-marco.csv`, `gn_junho_2026.csv`).
- Tamanhos conferidos na amostra (2026-11-15): 2021-01, 775.278 bytes; 2021-02, 738.476; 2022-05, 931.670; 2023-10, 1.107.461; 2025-02, 3.065.384; 2026-06, 4.288.595.
- No bruto, o nome é `movimentacao-gn_<AAAA>-<MM>@AAAAMMDD.csv`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Metadados em PDF (versão 12/06/2026): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-movimentacao-de-gas-natural-em-gasodutos-de-transporte/metadados-gn-sim.pdf. Fonte do dado: relatórios operacionais enviados mensalmente pelos transportadores à ANP por FTP, em planilha XLS; órgão responsável: Superintendência de Infraestrutura e Movimentação (SIM/ANP).
- A página oficial lista os meses até outubro de 2026 (publicado em 10/11/2026) e dezembro de 2022 como o primeiro mês, e informa datas de atualização por arquivo (por exemplo, setembro de 2025 a abril de 2026 atualizados em 10/11/2026 ou 19/10/2026), o que mostra revisão retroativa; o catálogo do fetcher não inclui julho a outubro de 2026.

## Conteúdo

- **Uma linha por variável, ponto, carregador e dia.** O CSV da fonte tem uma linha por variável, ponto e carregador, com 28 a 31 colunas de dia; o conversor as transpõe, de modo que um mês vira de 57.596 a 335.190 linhas na amostra (63.767 em janeiro de 2021; 335.190 em junho de 2026).
- **Dimensão da amostra.** 909.623 linhas nos 6 meses amostrados (2021-01, 2021-02, 2022-05, 2023-10, 2025-02, 2026-06), de 179 dias, 49 códigos de instalação de transporte, 5 operadores e 84 nomes de carregador (6 em 2021, 64 em 2026).
- **Variáveis.** 23 identificadores em `variavel`: volumes (`volume-solicitado`, `volume-programado`, `volume-realizado` e, em 2022, `solicitado`, `programado`, `realizado`), `pressao-media`, `alocacao` (e 9 por carregador), `gas-de-uso-no-sistema`, `gas-nao-contado`, `perdas-operacionais`, `perdas-extraordinarias`, `desequilibrio-diario`, `desequilibrio-diario-acumulado` e `empacotamento`; 40 grafias em `variavel_fonte`.
- **Pontos e conjuntos de transporte.** 709.459 linhas (78%) têm ponto de gasoduto identificado (564.238 pontos de entrega e 145.221 de recebimento); as demais referem-se ao conjunto de transporte (volumes de uso no sistema, perdas, empacotamento).
- **Valores.** `valor` é nulo em 55.042 linhas (célula vazia na fonte) e negativo em 40.934 (desequilíbrios, perdas e ajustes, como `-0,003`); 442.110 linhas valem zero.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2021 | `movimentacao-gn-01` (17); `movimentacao-gn-02` (17) |
| 2022 | `movimentacao-gn-05` (17) |
| 2023 | `movimentacao-gn-10` (17) |
| 2025 | `movimentacao-gn-02` (17) |
| 2026 | `movimentacao-gn-06` (17) |

## Variáveis

As descrições das 12 primeiras colunas vêm do dicionário de campos do documento de metadados da ANP (versão de 12/06/2026); as de `variavel`, `unidade`, `variavel_fonte`, `data` e `valor` descrevem o formato longo gerado pelo conversor, que transpõe as colunas de dia e a coluna `Nome da Variável` da fonte. As definições de cada variável medida (volumes, alocação, pressão, gás de uso, perdas, desequilíbrios e empacotamento) estão nos metadados e resumidas em Conteúdo.
Definições (metadados da ANP): volume solicitado, o volume diário que o carregador pede ao transportador; programado, o que o transportador programa; realizado, o que o carregador efetivamente utiliza (todos em mil m³); alocação, a razão percentual entre o volume realizado do carregador e o somatório dos realizados de todos os carregadores, por ponto e dia; pressão média, em kgf/cm²; gás de uso no sistema, o volume usado na operação (gás combustível, gás não contado e perdas operacionais); gás não contado, erros de medição; perdas operacionais, perdas do curso normal da operação; perdas extraordinárias, gás liberado por danos ou mau funcionamento; desequilíbrio diário, a diferença entre injetado e retirado pelo carregador; desequilíbrio diário acumulado, o somatório dos desequilíbrios diários; empacotamento, o volume armazenado nas instalações de transporte.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Código da Instalação de Transporte` | `Código da Instalação de Transporte` | texto | Código ANP do conjunto de instalações necessárias à prestação do serviço de transporte dutoviário de gás natural, incluindo tubulações e instalações auxiliares | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Nome da Instalação de Transporte` | `Nome da Instalação de Transporte` | texto | Nome do conjunto de instalações de transporte (por exemplo, `GASBOL`, `GASPAL`, `GASBEL`, `GASDUC III`) | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Nome da Instalação de Gasoduto` | `Nome da Instalação de Gasoduto` | texto | Nome dos pontos nos gasodutos de transporte em que o gás natural é entregue ao transportador pelo carregador (ponto de recebimento), ou vice-versa (ponto de entrega); vazio quando a linha é do conjunto de transporte inteiro | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Código da Instalação de Gasoduto` | `Código da Instalação de Gasoduto` | texto | Código ANP dos pontos nos gasodutos de transporte em que o gás natural é entregue ao transportador pelo carregador, ou vice-versa | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Tipo da instalação de Gasoduto` | `Tipo da instalação de Gasoduto` | texto | Tipo do ponto no gasoduto de transporte. Na fonte de 2021 o cabeçalho é `Tipo da Instalação do Gasoduto` (com "do") | Ponto de Recebimento = ponto em que o carregador entrega o gás ao transportador; Ponto de Entrega = ponto em que o transportador entrega o gás | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Nome do Município da Instalação de Gasoduto` | `Nome do Município da Instalação de Gasoduto` | texto | Nome do município onde está localizado o gasoduto que movimenta gás natural desde instalações de processamento, estocagem ou outros gasodutos até instalações de estocagem, outros gasodutos e pontos de entrega a concessionários estaduais de distribuição | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Nome da UF da Instalação de Gasoduto` | `Nome da UF da Instalação de Gasoduto` | texto | Sigla da unidade da federação onde está localizado o gasoduto; os metadados chamam o campo de "Nome da UF", mas o arquivo traz a sigla | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Nome do Operador da instalação de Gasoduto` | `Nome do Operador da instalação de Gasoduto` | texto | Nome da empresa autorizada ou concessionária da atividade de transporte de gás natural por meio do duto (transportador) | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Código do Operador da Instalação de Gasoduto` | `Código do Operador da Instalação de Gasoduto` | texto | Código ANP da empresa autorizada ou concessionária da atividade de transporte; o mesmo operador aparece com mais de um código (veja Cuidados de uso) | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Nome do Carregador que usa a Instalação de Gasoduto` | `Nome do Carregador que usa a Instalação de Gasoduto` | texto | Nome do agente que utiliza ou pretende utilizar o serviço de movimentação de gás natural em gasodutos de transporte, mediante autorização da ANP (carregador); a grafia varia entre arquivos | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Código do Carregador que usa a Instalação de Gasoduto` | `Código do Carregador que usa a Instalação de Gasoduto` | texto | Código ANP do carregador. Em parte das linhas o código vem em notação científica do Excel (`1,50E+11`), que perdeu dígitos | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `Nome do Contrato da Instalação de Gasoduto` | `Nome do Contrato da Instalação de Gasoduto` | texto | Nome do contrato firmado entre o carregador e o transportador para prestação do serviço de transporte, incluindo aditivos; vazio em muitas linhas | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `variavel` | `variavel` | texto | Variável medida, em forma de identificador (por exemplo, `volume-realizado`, `pressao-media`, `alocacao`); resulta da normalização do nome da variável da fonte. Gerada pelo conversor | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `unidade` | `unidade` | texto | Unidade da variável, tirada do nome da variável na fonte; vazia nos arquivos de 2021, cujos nomes não trazem unidade. Gerada pelo conversor | mil m³ = volumes e perdas de gás; % = alocação; kgf/cm² = pressão média | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `variavel_fonte` | `Nome da Variável` | texto | Nome da variável como está na fonte (coluna `Nome da Variável`), incluindo a unidade entre parênteses nos arquivos recentes, com variações de grafia (por exemplo, `Gás Não Contado5 (mil m³)`). Gerada pelo conversor | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `data` | `colunas de data (dd/mm/aaaa)` | date32[day] | Dia operacional a que o valor se refere. Na fonte as datas são os nomes das colunas (`01/06/2026`, `02/06/2026` ...); o conversor as transforma em linhas | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |
| `valor` | `valor da célula` | decimal | Valor da variável no dia: volumes e perdas em mil m³ (duas casas decimais), pressão em kgf/cm², alocação em percentual (veja `unidade`); vazio quando a célula da fonte não está preenchida | — | todo | `movimentacao-gn-01`, `movimentacao-gn-02`, `movimentacao-gn-05` e mais 2 |

## No lake

- Dataset `anp/movimentacao-gn`, particionado por `ano` e `mes`; um Parquet por arquivo mensal da fonte, no padrão `ano=<AAAA>/mes=<MM>/movimentacao-gn_<AAAA>-<MM>.parquet`.
- O conversor transpõe o CSV largo: as colunas de dia viram as colunas `data` e `valor` e a coluna `Nome da Variável` vira `variavel` (identificador), `unidade` e `variavel_fonte` (nome original). Os acentos e a codificação ISO-8859 são lidos corretamente.

## Cuidados de uso

- **Variável com nome diferente conforme o ano.** `volume-solicitado`/`solicitado`, `volume-realizado`/`realizado` e `volume-programado`/`programado` são a mesma grandeza em períodos diferentes (`solicitado`, `programado` e `realizado` só em 2022 na amostra); agrupe as duas formas antes de montar séries. `variavel_fonte` tem 40 grafias, inclusive com erros (`Gás Não Contado5 (mil m³)`, `Alocação Petrobras(%)`, `Desequilibrio Diário (mil m³)` sem acento e `( mil m³)` com espaço).
- **`unidade` vazia em 2021.** Os nomes de variável de 2021 não trazem unidade; as unidades de 2021 são as dos mesmos nomes nos anos seguintes (mil m³, kgf/cm² e %).
- **Código do carregador em notação científica.** 32.231 linhas têm `Código do Carregador` como `3,34E+12`, `2,75E+13`, `3,42E+13` etc. (Excel), que não recuperam o código original; use o nome do carregador ou o código em linhas sem a notação.
- **Nomes e códigos inconsistentes.** A Petrobras aparece com quatro grafias (`Petróleo Brasileiro S.A. - PETROBRAS`, `PETROLEO BRASILEIRO S A PETROBRAS`, `PETROBRAS` e `Petrobras`), `AMBAR`/`Ambar`, a TBG com os códigos `5` e `3001891441` e a GOM com `1717813` e `2001717813`; normalize nomes e códigos antes de agrupar por empresa.
- **Revisões retroativas e arquivos faltando.** A ANP reescreve arquivos antigos (por exemplo, janeiro a abril de 2024 revisados e 2025 atualizados em novembro de 2026); o lake traz a versão do dia do download. O catálogo termina em junho de 2026 e a página oficial já tem julho a outubro de 2026.
- **Chave não única.** Mesmo com instalação, ponto, carregador, contrato, variável e data, há 5.675 linhas repetidas de 909.623 na amostra; some ou agregue com cuidado e verifique duplicatas por mês antes de somar volumes.
- **Valores nulos e zeros.** 55.042 linhas têm `valor` nulo e 442.110 têm zero; zero pode ser ausência de movimento ou dado não informado.
- **Dados pessoais.** Nomes de transportadores, carregadores e contratos são de empresas (pessoas jurídicas); não há pessoas físicas.

## Exemplos

Volume realizado nos pontos de entrega por instalação de transporte em junho de 2026 (mil m³), somando os dias (só pontos de entrega, para não contar o mesmo gás no recebimento e na entrega):

```python
import duckdb

duckdb.sql("""
    SELECT "Nome da Instalação de Transporte" AS instalacao,
           round(sum(valor)) AS volume_realizado_mil_m3
    FROM read_parquet('lake/anp/movimentacao-gn/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '06'
      AND variavel = 'volume-realizado'
      AND "Tipo da instalação de Gasoduto" = 'Ponto de Entrega'
    GROUP BY instalacao
    ORDER BY volume_realizado_mil_m3 DESC
    LIMIT 8
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-consolidados-movimentacao-de-gas-natural-em-gasodutos-de-transporte
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-movimentacao-de-gas-natural-em-gasodutos-de-transporte/metadados-gn-sim.pdf
- Resolução ANP nº 40/2016 (§ 2º do art. 1º), citada nos metadados como base da publicação dos dados.
