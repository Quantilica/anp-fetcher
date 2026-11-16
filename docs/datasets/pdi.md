---
dataset:
  id: pdi
  fonte: anp
  titulo: Pesquisa, Desenvolvimento e Inovação (PD&I) — obrigação, PRH-ANP, projetos e unidades credenciadas
  resumo: 'Dados abertos da cláusula de PD&I dos contratos de exploração e produção: obrigação anual por campo, aportes ao PRH-ANP, projetos pelos regulamentos RT 3/2015 e RT 5/2005 e áreas, temas e subtemas das unidades de pesquisa credenciadas.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-pesquisa-e-desenvolvimento-e-inovacao-pd-i
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'varia por arquivo: obrigação anual; PRH-ANP semestral; projetos RT 3/2015 e unidades de pesquisa trimestral; RT 5/2005 sem atualização (segundo os metadados da ANP)'
  cobertura:
    inicio: 1992-09
    fim: 2026-07
  unidade: 'depende do arquivo: uma obrigação de um campo e grupo econômico em um ano (`pdi-obrigacao`); um aporte de empresa, em linha de uma tabela larga (`pdi-prh`); um projeto (`pdi-projetos-rt-3-2015`, `pdi-projetos-rt-5-2005`); uma área, tema e subtema de um credenciamento (`pdi-unidades-pesquisa`)'
  granularidade:
    espacial: campo (obrigação), empresa e instituição executora (projetos); UF da unidade de pesquisa (credenciamentos); sem município
    temporal: ano da obrigação (1998 a 2025), data de início e de término dos projetos (1992 a 2026) e ano do credenciamento (de 2013); sem partição no lake
  formato_bruto: quatro CSV (obrigação em UTF-8 com BOM, separado por vírgula; os outros três em ISO-8859-1, separados por ponto e vírgula) e uma planilha XLSX (unidades de pesquisa)
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 41
  unidades_de_medida:
    Valor da Obrigação: R$ (reais; texto `R$ ` + dígitos, vírgula decimal)
    VALOR CLAUSULA: R$ (reais; texto, ponto de milhar e vírgula decimal)
    PRAZO: não informada pelo metadado (provavelmente meses; inteiro em texto)
    Ano: ano civil (AAAA)
    coluna_2: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_3: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_4: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_5: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_6: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_7: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_8: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_9: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos
    coluna_10: R$ (reais; texto) nas linhas de empresa
  dados_pessoais:
  - coluna: Grupo Econômico
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: Aportes realizados pelas Petrolíferas no PRH-ANP - Cláusula PD&I
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: EMPRESA RESPONSÁVEL
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: DEMAIS PROPONENTES
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: EMPRESA PETROLÍFERA EXECUTORA
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: EMPRESA BRASILEIRA EXECUTORA
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: INSTITUIÇÃO EXECUTORA
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: UNIDADE DE PESQUISA EXECUTORA
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: EMPRESA PETROLÍFERA
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  - coluna: INSTITUIÇÃO CREDENCIADA EXECUTORA
    categoria: nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)
  eras:
  - desde: '1992'
    mudanca: projetos pelo Regulamento Técnico ANP nº 5/2005 (datas de início de 1992 a 2017); revogado pela Resolução ANP nº 50/2015, com regra de transição que permitiu contratar projetos por ele até 31/03/2017, e por isso sem nova atualização
  - desde: '2016'
    mudanca: projetos pelo Regulamento Técnico ANP nº 3/2015 (datas de início de 2016 a 2026, atualizados trimestralmente), com áreas, temas e subtemas conforme o Anexo I da Resolução ANP nº 918/2023
  - desde: '2023'
    mudanca: 'credenciamento de unidades de pesquisa conforme a Resolução ANP nº 917/2023; o PRH-ANP traz os aportes de 2019 a 2026, conforme a Resolução ANP nº 918/2023 (metadado: RANP nº 918/23)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Pesquisa, Desenvolvimento e Inovação (PD&I) — obrigação, PRH-ANP, projetos e unidades credenciadas

## Resumo

A Lei nº 9.478/1997 deu à ANP a atribuição de estimular a pesquisa e a adoção de novas tecnologias, e os contratos de exploração e produção dispõem, desde a Rodada Zero, da Cláusula de PD&I, que obriga a aplicar um percentual da receita bruta da produção, segundo as condições de cada modalidade de contrato. A ANP é responsável por analisar, aprovar, acompanhar e fiscalizar a aplicação desses recursos. Este grupo reúne cinco arquivos da página de dados abertos de PD&I: a obrigação de investimento gerada por campo e empresa (`pdi-obrigacao`), os aportes das petrolíferas ao Programa de Recursos Humanos da ANP (`pdi-prh`), os projetos contratados pelo Regulamento Técnico ANP nº 3/2015 (`pdi-projetos-rt-3-2015`) e pelo anterior, nº 5/2005 (`pdi-projetos-rt-5-2005`), e as áreas, temas e subtemas em que cada unidade de pesquisa está credenciada (`pdi-unidades-pesquisa`).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pdi` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-pesquisa-e-desenvolvimento-e-inovacao-pd-i |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | varia por arquivo: obrigação anual; PRH-ANP semestral; projetos RT 3/2015 e unidades de pesquisa trimestral; RT 5/2005 sem atualização (segundo os metadados da ANP) |
| Cobertura | 1992-09 a 2026-07 |
| Unidade (uma linha) | depende do arquivo: uma obrigação de um campo e grupo econômico em um ano (`pdi-obrigacao`); um aporte de empresa, em linha de uma tabela larga (`pdi-prh`); um projeto (`pdi-projetos-rt-3-2015`, `pdi-projetos-rt-5-2005`); uma área, tema e subtema de um credenciamento (`pdi-unidades-pesquisa`) |
| Granularidade | espacial: campo (obrigação), empresa e instituição executora (projetos); UF da unidade de pesquisa (credenciamentos); sem município; temporal: ano da obrigação (1998 a 2025), data de início e de término dos projetos (1992 a 2026) e ano do credenciamento (de 2013); sem partição no lake |
| Formato bruto | quatro CSV (obrigação em UTF-8 com BOM, separado por vírgula; os outros três em ISO-8859-1, separados por ponto e vírgula) e uma planilha XLSX (unidades de pesquisa) |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 41 |
| Unidades de medida | `Valor da Obrigação`: R$ (reais; texto `R$ ` + dígitos, vírgula decimal); `VALOR CLAUSULA`: R$ (reais; texto, ponto de milhar e vírgula decimal); `PRAZO`: não informada pelo metadado (provavelmente meses; inteiro em texto); `Ano`: ano civil (AAAA); `coluna_2`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_3`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_4`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_5`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_6`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_7`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_8`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_9`: R$ (reais; texto, `R$ -` quando zero) nas linhas de empresa; ano na linha de rótulos; `coluna_10`: R$ (reais; texto) nas linhas de empresa |
| Dados pessoais | `Grupo Econômico` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `Aportes realizados pelas Petrolíferas no PRH-ANP - Cláusula PD&I` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `EMPRESA RESPONSÁVEL` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `DEMAIS PROPONENTES` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `EMPRESA PETROLÍFERA EXECUTORA` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `EMPRESA BRASILEIRA EXECUTORA` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `INSTITUIÇÃO EXECUTORA` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `UNIDADE DE PESQUISA EXECUTORA` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `EMPRESA PETROLÍFERA` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)); `INSTITUIÇÃO CREDENCIADA EXECUTORA` (nome de empresa, instituição ou unidade de pesquisa (pessoa jurídica)) |
| Eras | 1992: projetos pelo Regulamento Técnico ANP nº 5/2005 (datas de início de 1992 a 2017); revogado pela Resolução ANP nº 50/2015, com regra de transição que permitiu contratar projetos por ele até 31/03/2017, e por isso sem nova atualização; 2016: projetos pelo Regulamento Técnico ANP nº 3/2015 (datas de início de 2016 a 2026, atualizados trimestralmente), com áreas, temas e subtemas conforme o Anexo I da Resolução ANP nº 918/2023; 2023: credenciamento de unidades de pesquisa conforme a Resolução ANP nº 917/2023; o PRH-ANP traz os aportes de 2019 a 2026, conforme a Resolução ANP nº 918/2023 (metadado: RANP nº 918/23) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Cinco arquivos na página de dados abertos de PD&I da ANP, em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-pdi/`: `obrigacaopdi.csv` (32.981 bytes), `investimentos-prh.csv` (1.958), `projetos-rt-3-2015.csv` (4.026.880), `projetos-rt-5-2005.csv` (1.338.674) e `dados-abertos-unidades-pesquisa-area-tema-subtema.xlsx` (137.149; uma aba `Dados_Abertos_Unidades_Pesquisa`). Tamanhos conferidos na coleta de 2026-11-15.
- Fonte do dado, segundo os metadados em PDF: ANP/STM (Superintendência de Tecnologia e Meio Ambiente). Obrigação: a SPG informa à STM a receita bruta de produção para calcular a obrigação por campo e empresa; periodicidade anual; "até 2025" (atualizado em 02/03/2026). PRH-ANP: aportes registrados no SEI (RANP nº 918/23), semestral, atualizado em 16/06/2026; contato prh@anp.gov.br. Projetos RT 3/2015: I-Engine (https://engine.anp.gov.br), planos de trabalho (PTR) conforme a Resolução ANP nº 918/2023, trimestral, projetos iniciados até 30/06/2026; contato autorizacaopreviaped@anp.gov.br. Projetos RT 5/2005: tabelas da STM, sem atualização (atualizado em 09/03/2026). Unidades de pesquisa: SIPED (https://siped.anp.gov.br/), Resolução ANP nº 917/2023, trimestral; contato credenciamentoped@anp.gov.br.
- A página lista também "Unidades de Pesquisa Credenciadas (PD&I)", com colunas de sigla, instituição, unidade e coordenador, e seu metadado (`metadado-unidades-pesquisa.pdf`), mas o arquivo de dados dessa lista não está no catálogo do fetcher (o link `unidades-pesquisa-credenciadas` respondeu 403 na coleta de 2026-11-15, e a ficha não foi verificada); o catálogo tem só a planilha de áreas, temas e subtemas.
- O servidor não informa a data de modificação dos arquivos; o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15).

## Conteúdo

Os cinco arquivos do catálogo, todos no lake:

| Arquivo | Linhas | Colunas | Período | Observação |
|---|---|---|---|---|
| `pdi-obrigacao` | 780 | 4 | 1998 a 2025 | uma linha por campo, grupo econômico e ano; 59 campos e 17 grupos; `Valor da Obrigação` em texto `R$ 1884529,15` |
| `pdi-prh` | 18 | 10 | 2019 a 2026 | tabela larga de aportes por empresa e ano, lida com a linha de título como cabeçalho (colunas `coluna_2` a `coluna_10`) |
| `pdi-projetos-rt-3-2015` | 7.974 | 17 | início 2016 a 2026 | 5.682 projetos e 2.292 linhas totalmente vazias do fim do arquivo; todos têm `ÁREA`, `TEMA` e `SUBTEMA` |
| `pdi-projetos-rt-5-2005` | 10.102 | 9 | início 1992 a 2017 | 10.102 projetos; término de 1996 a 2023; só 1.091 têm autorização |
| `pdi-unidades-pesquisa` | 4.486 | 5 | credenciamentos de 2013 a 2026 | 1.166 credenciamentos em 26 UFs, uma linha por credenciamento, área, tema e subtema |

- **Obrigação (`pdi-obrigacao`):** a soma anual vai de R$ 1,9 milhão (1998) a R$ 4,4 bilhões (2022), com R$ 4,3 bilhões em 2025; o total do arquivo é R$ 38,8 bilhões. O campo com maior obrigação acumulada é `TUPI` (R$ 10,2 bilhões), seguido de `BÚZIOS_ECO` (R$ 3,1) e `RONCADOR` (R$ 3,0). `Petrobras` aparece em 504 das 780 linhas.
- **PRH-ANP (`pdi-prh`):** o total aportado de 2019 a 2026, na linha de totais, é R$ 468.404.806,28; a Petrobras responde por R$ 284 milhões, a Shell por R$ 55,3 milhões e a Equinor por R$ 30,6 milhões, entre 15 empresas.
- **Projetos RT 3/2015:** `PETROBRAS` é a responsável por 4.715 dos 5.682 projetos (`SHELL`, 359; `PETROGAL`, 111; `TOTAL`, 107). A soma de `VALOR CLAUSULA` é R$ 43,7 bilhões, com 4,3 bilhões em projetos iniciados em 2022, 6,2 em 2023, 12,8 em 2024 e 8,9 em 2025; `PESQUISA APLICADA` (2.898) e `DESENVOLVIMENTO EXPERIMENTAL` (1.158) são as qualificações mais comuns.
- **Projetos RT 5/2005:** `PETROBRAS` responde por 9.823 dos 10.102 projetos; os inícios chegam a 1.047 em 2005.

## Variáveis

As descrições vêm dos metadados em PDF da ANP de cada arquivo ("Obrigação de Investimentos em PD&I", "Investimentos realizados no PRH-ANP", "Projetos de PD&I - RT 3/2015", "Projetos de PD&I - RT 5/2005" e "Credenciamento de unidades de pesquisa: áreas, temas e subtemas"); as contagens vêm da amostra do lake (2026-11-15), que cobre os cinco arquivos inteiros. Os metadados dão valores e datas como número e data, mas o lake os guarda como texto.
As colunas `ÁREA`, `TEMA` e `SUBTEMA` (projetos RT 3/2015 e unidades de pesquisa) e `EMPRESA BRASILEIRA EXECUTORA` (RT 3/2015 e RT 5/2005) são compartilhadas; `Área`, de `pdi-obrigacao`, é outra coluna (campo). Os nomes das colunas `EMPRESA PETROLÍFERA EXECUTORA`, `VALOR CLAUSULA` e a do título do PRH têm espaços no início ou no fim na fonte; aqui constam sem eles. A coluna *Arquivos* diz em quais tabelas cada coluna aparece.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Área` | `Área` | texto | Nome do campo gerador da obrigação de investimento em PD&I (59 campos, como `ALBACORA`, `TUPI`, `BÚZIOS_ECO`); só em `pdi-obrigacao` (o nome da coluna tem acento e só a inicial maiúscula, diferente de `ÁREA` dos outros arquivos). | — | — | `pdi-obrigacao` |
| `Grupo Econômico` | `Grupo Econômico` | texto | Nome da empresa petrolífera (grupo econômico) que gerou a obrigação (17 grupos, como `Petrobras`, `Shell`, `Repsol Sinopec`); só em `pdi-obrigacao`. | — | — | `pdi-obrigacao` |
| `Valor da Obrigação` | `Valor da Obrigação` | texto | Valor da obrigação gerada, em reais, como texto `R$ ` seguido de dígitos com vírgula decimal e sem ponto de milhar (`R$ 1884529,15`); só em `pdi-obrigacao`. | — | — | `pdi-obrigacao` |
| `Ano` | `Ano` | texto | Ano em que a obrigação foi gerada (de 1998 a 2025); só em `pdi-obrigacao`. | — | — | `pdi-obrigacao` |
| `Aportes realizados pelas Petrolíferas no PRH-ANP - Cláusula PD&I` | `Aportes realizados pelas Petrolíferas no PRH-ANP - Cláusula PD&I` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Título do quadro, que o conversor tomou como nome da coluna; nas linhas de dados traz o nome da empresa aportante (`Equinor`, `Petrobras`, `Shell`, `Consórcio Libra` e outras), `Empresa` (linha de rótulos) ou `Total Aportado / Ano` (linha de totais). | — | — | `pdi-prh` |
| `coluna_2` | `coluna_2` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2019, em reais (`R$ 10.000.000,00`; `R$ -` quando não houve); a linha de rótulos `Ano/Aporte` traz esse texto e a de rótulos `Empresa` traz o ano `2019`. | — | — | `pdi-prh` |
| `coluna_3` | `coluna_3` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2020, em reais. | — | — | `pdi-prh` |
| `coluna_4` | `coluna_4` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2021, em reais. | — | — | `pdi-prh` |
| `coluna_5` | `coluna_5` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2022, em reais. | — | — | `pdi-prh` |
| `coluna_6` | `coluna_6` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2023, em reais. | — | — | `pdi-prh` |
| `coluna_7` | `coluna_7` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2024, em reais. | — | — | `pdi-prh` |
| `coluna_8` | `coluna_8` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2025, em reais. | — | — | `pdi-prh` |
| `coluna_9` | `coluna_9` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Aportes de 2026, em reais. | — | — | `pdi-prh` |
| `coluna_10` | `coluna_10` | texto | Parte do arquivo `pdi-prh`, que é uma tabela larga (uma coluna por ano de aporte) e foi lida pelo conversor com a linha de título como cabeçalho (ver Cuidados de uso). Total aportado pela petrolífera desde 2019, em reais (`Total por Empresa` no cabeçalho original); a última linha traz o total de todas as empresas, R$ 468.404.806,28. | — | — | `pdi-prh` |
| `Nº ANP` | `Nº ANP` | texto | Número do projeto atribuído no momento da primeira carga no I-Engine (`25098-5`); só em `pdi-projetos-rt-3-2015` (5.682 projetos distintos). | — | — | `pdi-projetos-rt-3` |
| `TITULO` | `TITULO` | texto | Título do projeto informado no Plano de Trabalho (PTR); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `EMPRESA RESPONSÁVEL` | `EMPRESA RESPONSÁVEL` | texto | Empresa petrolífera que realiza a carga do PTR no I-Engine (22 empresas, `PETROBRAS` em 4.715 projetos); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `DEMAIS PROPONENTES` | `DEMAIS PROPONENTES` | texto | Empresas petrolíferas que financiam o projeto, conforme o PTR, separadas por `; ` (50 combinações); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `QUALIFICAÇÃO` | `QUALIFICAÇÃO` | texto | Qualificação (tipo) do projeto, informada no PTR (14 valores, como `PESQUISA APLICADA`, `DESENVOLVIMENTO EXPERIMENTAL`, `PROTÓTIPO OU UNIDADE PILOTO`, `INFRAESTRUTURA`); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `OBJETIVO` | `OBJETIVO` | texto | Objetivo do projeto informado no PTR, em texto livre longo; só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `ÁREA` | `ÁREA` | texto | Área conforme o Anexo I da Resolução ANP nº 918/2023 (7 valores, como `EXPLORAÇÃO E PRODUÇÃO DE PETRÓLEO E GÁS NATURAL - ONSHORE E OFFSHORE`, `TEMAS TRANSVERSAIS`, `ABASTECIMENTO`); em `pdi-projetos-rt-3-2015` (informada no PTR) e em `pdi-unidades-pesquisa` (área em que a unidade está credenciada). | — | — | `pdi-projetos-rt-3`, `pdi-unidades-pesquisa` |
| `TEMA` | `TEMA` | texto | Tema conforme o Anexo I da Resolução ANP nº 918/2023 (24 valores); em `pdi-projetos-rt-3-2015` (informado no PTR) e em `pdi-unidades-pesquisa`. | — | — | `pdi-projetos-rt-3`, `pdi-unidades-pesquisa` |
| `SUBTEMA` | `SUBTEMA` | texto | Subtema conforme o Anexo I da Resolução ANP nº 918/2023 (137 valores no total); em `pdi-projetos-rt-3-2015` (informado no PTR) e em `pdi-unidades-pesquisa`. | — | — | `pdi-projetos-rt-3`, `pdi-unidades-pesquisa` |
| `EMPRESA PETROLÍFERA EXECUTORA` | `EMPRESA PETROLÍFERA EXECUTORA` | texto | Empresa petrolífera que executa o projeto, conforme o PTR (campo pode estar vazio; preenchido em 2.738 linhas); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `EMPRESA BRASILEIRA EXECUTORA` | `EMPRESA BRASILEIRA EXECUTORA` | texto | Empresa brasileira que executa o projeto, conforme o PTR (campo pode estar vazio); em `pdi-projetos-rt-3-2015` (496 linhas) e em `pdi-projetos-rt-5-2005` (62 linhas; o `-` da fonte vira vazio). | — | — | `pdi-projetos-rt-3`, `pdi-projetos-rt-5` |
| `INSTITUIÇÃO EXECUTORA` | `INSTITUIÇÃO EXECUTORA` | texto | Instituição credenciada que executa o projeto, conforme o PTR (campo pode estar vazio; 3.141 linhas); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `UNIDADE DE PESQUISA EXECUTORA` | `UNIDADE DE PESQUISA EXECUTORA` | texto | Unidade de pesquisa, vinculada a uma instituição credenciada, que executa o projeto, conforme o PTR (campo pode estar vazio; 3.128 linhas), como `UFRGS - LAMEF - LABORATÓRIO DE METALURGIA FÍSICA`; só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `Nº AUTORIZAÇÃO` | `Nº AUTORIZAÇÃO` | texto | Número da autorização informado no PTR, se o projeto passou por autorização (campo pode estar vazio; 581 linhas), como `1290/2024`; só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `DATA INÍCIO` | `DATA INÍCIO` | texto | Data de início do projeto informada no PTR (DD/MM/AAAA, texto), de 01/03/2016 a 01/07/2026; só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `PRAZO` | `PRAZO` | texto | Prazo de execução estimado do projeto, informado no PTR (inteiro em texto: 36, 24, 48, 12 e 30 são os mais comuns); o metadado não informa a unidade, e os valores sugerem meses (dedução); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `VALOR CLAUSULA` | `VALOR CLAUSULA` | texto | Valor de recursos da cláusula de PD&I estimado para a execução do projeto, informado no PTR, em reais, como texto `R$ 3.012.578,00` (ponto de milhar e vírgula decimal); só em `pdi-projetos-rt-3-2015`. | — | — | `pdi-projetos-rt-3` |
| `Nº PROJETO` | `Nº PROJETO` | texto | Número do projeto atribuído pela ANP (`18989-4`); só em `pdi-projetos-rt-5-2005` (10.102 projetos distintos). | — | — | `pdi-projetos-rt-5` |
| `TÍTULO` | `TÍTULO` | texto | Título do projeto; só em `pdi-projetos-rt-5-2005` (10.066 títulos distintos). | — | — | `pdi-projetos-rt-5` |
| `EMPRESA PETROLÍFERA` | `EMPRESA PETROLÍFERA` | texto | Empresa petrolífera responsável pelo projeto, uma ou mais separadas por `; ` (21 valores; `PETROBRAS` em 9.823 projetos); só em `pdi-projetos-rt-5-2005`. | — | — | `pdi-projetos-rt-5` |
| `DATA DE INÍCIO` | `DATA DE INÍCIO` | texto | Data de início do projeto (DD/MM/AAAA, texto), de 01/09/1992 a 31/03/2017; só em `pdi-projetos-rt-5-2005`. | — | — | `pdi-projetos-rt-5` |
| `DATA DE TÉRMINO` | `DATA DE TÉRMINO` | texto | Data de término do projeto (DD/MM/AAAA, texto), de 01/08/1996 a 01/12/2023; nunca anterior ao início; só em `pdi-projetos-rt-5-2005`. | — | — | `pdi-projetos-rt-5` |
| `INSTITUIÇÃO CREDENCIADA EXECUTORA` | `INSTITUIÇÃO CREDENCIADA EXECUTORA` | texto | Nome da instituição credenciada que executa o projeto (campo pode estar vazio; 4.894 linhas; o `-` da fonte vira vazio); só em `pdi-projetos-rt-5-2005`. | — | — | `pdi-projetos-rt-5` |
| `AUTORIZAÇÃO` | `AUTORIZAÇÃO` | texto | Número e ano da autorização, se houver (campo pode estar vazio; 1.091 linhas), como `053/2012`; só em `pdi-projetos-rt-5-2005`. | — | — | `pdi-projetos-rt-5` |
| `DATA DE PUBLICAÇÃO` | `DATA DE PUBLICAÇÃO` | texto | Data de publicação da autorização, se houver (DD/MM/AAAA, texto; vazia sem autorização; 1.090 linhas); só em `pdi-projetos-rt-5-2005`. | — | — | `pdi-projetos-rt-5` |
| `Nº CRED.` | `Nº CRED.` | texto | Número de credenciamento da unidade de pesquisa atribuído pela ANP, no formato `NNNN/AAAA` (`0985/2020`); 1.166 credenciamentos, de 0001/2013 a 1195/2026; só em `pdi-unidades-pesquisa`. Cada credenciamento repete em uma linha por área, tema e subtema. | — | — | `pdi-unidades-pesquisa` |
| `UF` | `UF` | texto | Unidade da Federação da unidade de pesquisa credenciada (sigla); 26 UFs, com mais credenciamentos no RJ (397), SP (176), MG (101) e RS (71); só em `pdi-unidades-pesquisa`. | — | — | `pdi-unidades-pesquisa` |

## No lake

- Dataset `anp/pdi`, sem partição: um Parquet por arquivo, `pdi-obrigacao.parquet`, `pdi-prh.parquet`, `pdi-projetos-rt-3-2015.parquet`, `pdi-projetos-rt-5-2005.parquet` e `pdi-unidades-pesquisa.parquet`.
- Todas as colunas são texto. O conversor mantém os nomes do cabeçalho (acentos, `º`, espaços), inclusive os espaços no início ou no fim de três nomes (o esquema desta documentação os grava sem esses espaços), e converte o `-` usado como vazio no RT 5/2005 em valor nulo.
- `pdi-prh` não tem um cabeçalho de verdade: a primeira linha do CSV é o título do quadro, e o conversor a usa como nome da coluna 1 e nomeia as outras `coluna_2` a `coluna_10`; as duas linhas de rótulos (`Ano/Aporte` e `Empresa`, com os anos) viram linhas de dados.

## Cuidados de uso

- **`pdi-prh` é uma tabela larga mal lida.** As 18 linhas incluem uma linha `Ano/Aporte`, uma linha `Empresa` com os anos nas colunas e a linha `Total Aportado / Ano`; descarte essas três para obter só as empresas, e use os anos de `coluna_2` a `coluna_9` (2019 a 2026). Os valores são `R$ -` quando nada foi aportado e vazios para `CNOOC` antes de 2026.
- **Linhas vazias em `pdi-projetos-rt-3-2015`.** Das 7.974 linhas, 2.292 não têm nenhum campo (o CSV termina com linhas `;;;;`); filtre `"Nº ANP" IS NOT NULL`. A coluna `VALOR CLAUSULA` vem como texto vazio nessas linhas, não como nulo.
- **Valores monetários em texto, em dois formatos.** `Valor da Obrigação` vem como `R$ 1884529,15` (sem ponto de milhar) e `VALOR CLAUSULA` e o PRH como `R$ 3.012.578,00` (com ponto de milhar); tire `R$ `, o ponto de milhar e troque a vírgula antes de converter.
- **`Área` e `ÁREA` não são a mesma coisa.** Em `pdi-obrigacao` é o nome do campo; nos projetos RT 3/2015 e nas unidades é a área temática do Anexo I da Resolução 918/2023. Como diferem só na caixa, cuidado com consultas que ignoram caixa (o DuckDB, por exemplo, une as duas ao empilhar com `union_by_name`).
- **Datas em texto e fora da faixa.** `DATA INÍCIO` e as datas do RT 5/2005 vêm em `DD/MM/AAAA`; no RT 3/2015, a data mais recente (01/07/2026) é posterior ao rótulo "projetos iniciados até 30/06/2026" da página; ordene só depois de converter.
- **`PRAZO` sem unidade.** O metadado não diz a unidade; os valores (12, 24, 36, 48, 60) sugerem meses, mas isso é dedução.
- **Texto livre e empresas repetidas.** `DEMAIS PROPONENTES` e `EMPRESA PETROLÍFERA` listam empresas separadas por `; `; a grafia varia (`TOTAL`, `Total Energies`, `TotalEnergies`), e `TITULO`/`TÍTULO` e `OBJETIVO` não são padronizados. Os dois regulamentos usam colunas diferentes (`TÍTULO`, com acento, no RT 5/2005 e `TITULO`, sem acento, no RT 3/2015).
- **Obrigação não é gasto.** A obrigação é o valor devido pela receita da produção; o quanto foi efetivamente aplicado em projetos está em `pdi-projetos-rt-3-2015` (valor estimado no PTR) e no PRH; não são séries comparáveis diretamente.
- **Dados pessoais.** Há nomes de empresas, instituições e unidades de pesquisa (pessoas jurídicas); os arquivos do catálogo não trazem coordenadores nem outras pessoas físicas (os coordenadores estão em arquivo não coletado).
- **Chave.** `Nº ANP` e `Nº PROJETO` são únicos em seus arquivos (nas linhas não vazias), mas, por serem cinco tabelas, a chave do dataset fica vazia.

## Exemplos

Obrigação de investimento em PD&I por ano (a coluna vem como `R$ 1884529,15`, sem ponto de milhar, e é convertida em número):

```python
import duckdb

duckdb.sql("""
    SELECT "Ano",
           count(*) AS campos_com_obrigacao,
           round(sum(replace(replace("Valor da Obrigação", 'R$ ', ''), ',', '.')::DOUBLE) / 1e6, 1) AS milhoes_reais
    FROM read_parquet('lake/anp/pdi/pdi-obrigacao.parquet')
    WHERE "Ano" >= '2020'
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Dados abertos de PD&I (ANP): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-pesquisa-e-desenvolvimento-e-inovacao-pd-i
- Metadados (PDF), na pasta https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-pdi/: `metadado-obrigacao-pdi.pdf`, `metadado-investimento-prh.pdf`, `metadado-projeto-rt-3-2015.pdf`, `metadado-projeto-rt-5-2005.pdf`, `metadados-unidades-pesquisa-area-tema-subtema.pdf` e `metadado-unidades-pesquisa.pdf`.
- Regulamento Técnico ANP nº 3/2015; Resoluções ANP nº 50/2015, nº 917/2023 e nº 918/2023, citadas nos metadados.
