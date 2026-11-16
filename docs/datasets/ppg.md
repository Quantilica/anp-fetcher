---
dataset:
  id: ppg
  fonte: anp
  titulo: Produção de petróleo e gás natural — séries nacionais, por poço e por campo
  resumo: Produção nacional mensal de petróleo, LGN e gás natural (2000 em diante), produção por poço (2005 a 2023) e por campo (2009 a 2016), publicadas nos dados estatísticos da ANP.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/dados-estatisticos
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal para as séries nacionais (atualizadas até 29/10/2026 na coleta); anual (ZIP por ano) para poços; as planilhas por campo cobrem 2009 a 2016 e não são mais atualizadas
  cobertura:
    inicio: '2000'
    fim: em-curso
  unidade: 'depende da tabela: um mês de um bloco de série nacional por ano (colunas `ANO <aaaa>`, em `ppg-historico`); um poço em um mês (`ppg` e `ppg-presal`); um campo em um mês (`ppg`, planilhas de campo)'
  granularidade:
    espacial: Brasil (total nacional, nas séries; os filtros por estado e localização da planilha ficam em `(Tudo)`); poço, com campo, bacia e estado (por poço); campo, bacia e estado (por campo)
    temporal: 'mês: coluna `Mês` e uma coluna por ano (séries nacionais); `Período` AAAA/MM (por poço e por campo, 2009)'
  formato_bruto: XLSX (as séries nacionais, com extensão `.xls`, e as planilhas por campo, `.xls` em 2009 e `.xlsx` em 2016) e ZIP anual de XLSX por ambiente (por poço)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 61
  unidades_de_medida:
    Óleo (bbl/dia): bbl/dia
    Condensado (bbl/dia): bbl/dia
    Petróleo (bbl/dia): bbl/dia
    Água (bbl/dia): bbl/dia
    Gás Natural (Mm³/dia) Associado: mil m³/dia
    Gás Natural (Mm³/dia) Não Associado: mil m³/dia
    Gás Natural (Mm³/dia) Gás Total: mil m³/dia
    Volume Gás Royalties (Mm³/dia): mil m³/dia
    Total Gás Natural (Mm³/dia): mil m³/dia
    Tempo de Produção (hs por mês): horas por mês
    Grau API: °API
    PCS GP (kJ/m³): kJ/m³
    Densidade GLP Gás: kg/m³
    Densidade GLP Líquido: kg/m³
    OLEO_M3: m³ (período não informado)
    CONDENSADO_M3: m³ (período não informado)
    AGUA_M3: m³ (período não informado)
    VARIAÇÃO DO ACUMULADO NO ANO (%): '%'
    ANO 2000: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2001: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2002: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2003: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2004: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2005: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2006: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2007: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2008: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2009: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2010: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2011: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2012: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2013: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2014: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2015: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2016: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2017: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2018: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2019: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2020: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2021: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2022: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2023: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2024: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2025: m³, barris ou mil m³ (conforme `tabela`)
    ANO 2026: m³, barris ou mil m³ (conforme `tabela`)
    GAS_ASSOCIADO_M3: unidade não informada pela fonte
    GAS_N_ASSOCIADO_M3: unidade não informada pela fonte
    NOM_BACIA: —
    NOM_CAMPO: —
  dados_pessoais:
  - coluna: Operador
    categoria: nome fantasia de empresa operadora (pessoa jurídica)
  eras:
  - desde: '2000'
    mudanca: 'séries nacionais: uma coluna por ano de 2000 a 2026 e variação do acumulado do ano; cada planilha empilha vários blocos (petróleo e LGN; no gás, produção, reinjeção, queima e perda, consumo próprio e disponível)'
  - desde: '2005'
    mudanca: 'produção por poço em ZIP anual de XLSX (2005 a 2023): o de 2009 tem mar e terra; o de 2017 acrescenta pré-sal; `Instalação Destino` vazia em terra em 2009'
  - desde: '2009'
    mudanca: 'produção por campo: planilha de 2009 com `Estado`, `Bacia`, `Campo`, `Operador`, `Número do Contrato`, `Período`, petróleo em bbl/dia e gás total em Mm³/dia'
  - desde: '2016'
    mudanca: 'produção por campo: cabeçalho em caixa alta e volumes em m³ (`NOM_BACIA`, `NOM_CAMPO`, `PERIODO`, `OLEO_M3`, ...)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de petróleo e gás natural — séries nacionais, por poço e por campo

## Resumo

Três famílias de planilhas da página de dados estatísticos da ANP: as séries mensais nacionais de produção de petróleo e LGN (em m³ e em barris) e de gás natural (mil m³, com reinjeção, queima e perda, consumo próprio e gás disponível), por ano de 2000 em diante; a produção anual detalhada por poço, em ZIP de XLSX por ambiente (terra, mar e, a partir de 2017, pré-sal); e a produção por campo, em planilhas de 2009 a 2016. As séries nacionais vêm do Boletim Mensal de Produção (Decreto nº 2.705/1998) e os dados por poço do SIGEP.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/ppg` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/dados-estatisticos |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal para as séries nacionais (atualizadas até 29/10/2026 na coleta); anual (ZIP por ano) para poços; as planilhas por campo cobrem 2009 a 2016 e não são mais atualizadas |
| Cobertura | 2000 a em-curso |
| Unidade (uma linha) | depende da tabela: um mês de um bloco de série nacional por ano (colunas `ANO <aaaa>`, em `ppg-historico`); um poço em um mês (`ppg` e `ppg-presal`); um campo em um mês (`ppg`, planilhas de campo) |
| Granularidade | espacial: Brasil (total nacional, nas séries; os filtros por estado e localização da planilha ficam em `(Tudo)`); poço, com campo, bacia e estado (por poço); campo, bacia e estado (por campo); temporal: mês: coluna `Mês` e uma coluna por ano (séries nacionais); `Período` AAAA/MM (por poço e por campo, 2009) |
| Formato bruto | XLSX (as séries nacionais, com extensão `.xls`, e as planilhas por campo, `.xls` em 2009 e `.xlsx` em 2016) e ZIP anual de XLSX por ambiente (por poço) |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 61 |
| Unidades de medida | `Óleo (bbl/dia)`: bbl/dia; `Condensado (bbl/dia)`: bbl/dia; `Petróleo (bbl/dia)`: bbl/dia; `Água (bbl/dia)`: bbl/dia; `Gás Natural (Mm³/dia) Associado`: mil m³/dia; `Gás Natural (Mm³/dia) Não Associado`: mil m³/dia; `Gás Natural (Mm³/dia) Gás Total`: mil m³/dia; `Volume Gás Royalties (Mm³/dia)`: mil m³/dia; `Total Gás Natural (Mm³/dia)`: mil m³/dia; `Tempo de Produção (hs por mês)`: horas por mês; `Grau API`: °API; `PCS GP (kJ/m³)`: kJ/m³; `Densidade GLP Gás`: kg/m³; `Densidade GLP Líquido`: kg/m³; `OLEO_M3`: m³ (período não informado); `CONDENSADO_M3`: m³ (período não informado); `AGUA_M3`: m³ (período não informado); `VARIAÇÃO DO ACUMULADO NO ANO (%)`: %; `ANO 2000`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2001`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2002`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2003`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2004`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2005`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2006`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2007`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2008`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2009`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2010`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2011`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2012`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2013`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2014`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2015`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2016`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2017`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2018`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2019`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2020`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2021`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2022`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2023`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2024`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2025`: m³, barris ou mil m³ (conforme `tabela`); `ANO 2026`: m³, barris ou mil m³ (conforme `tabela`); `GAS_ASSOCIADO_M3`: unidade não informada pela fonte; `GAS_N_ASSOCIADO_M3`: unidade não informada pela fonte; `NOM_BACIA`: —; `NOM_CAMPO`: — |
| Dados pessoais | `Operador` (nome fantasia de empresa operadora (pessoa jurídica)) |
| Eras | 2000: séries nacionais: uma coluna por ano de 2000 a 2026 e variação do acumulado do ano; cada planilha empilha vários blocos (petróleo e LGN; no gás, produção, reinjeção, queima e perda, consumo próprio e disponível); 2005: produção por poço em ZIP anual de XLSX (2005 a 2023): o de 2009 tem mar e terra; o de 2017 acrescenta pré-sal; `Instalação Destino` vazia em terra em 2009; 2009: produção por campo: planilha de 2009 com `Estado`, `Bacia`, `Campo`, `Operador`, `Número do Contrato`, `Período`, petróleo em bbl/dia e gás total em Mm³/dia; 2016: produção por campo: cabeçalho em caixa alta e volumes em m³ (`NOM_BACIA`, `NOM_CAMPO`, `PERIODO`, `OLEO_M3`, ...) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Séries nacionais:** três planilhas em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/ppg/`: `producao-petroleo-m3.xls` (150.265 bytes), `producao-petroleo-b.xls` (181.177) e `producao-gas-natural-m3.xls` (373.070). A extensão é `.xls`, mas os arquivos são XLSX (ZIP/OOXML). Cada uma traz blocos empilhados: petróleo e LGN (as de petróleo) e, na de gás, produção, reinjeção, queima e perda, consumo próprio na E&P e gás disponível. As notas da planilha dão a fonte: ANP, Boletim Mensal de Produção, Decreto nº 2.705/1998; petróleo é óleo mais condensado, sem LGN; volumes do gás à temperatura de 20 °C e pressão de 1 atm.
- **Por poço:** 19 ZIP anuais de 2005 a 2023 em `.../de/ppg/pp/producao-pocos-<ano>.zip`; cada ZIP traz um XLSX por ambiente (`<ano>_producao_mar.xlsx`, `<ano>_producao_terra.xlsx` e, em 2017, `<ano>_producao_presal.xlsx`). Na amostra, o ZIP de 2009 tem 13,8 MB e o de 2017, 19,1 MB. Metadados da ANP para a série 2005-2017 (PDF) e para a posterior (a mesma lista de colunas, ampliada).
- **Por campo:** 8 planilhas de 2009 a 2016 em `.../de/ppg/pc/producao-campo-<ano>.xls` (2009 a 2015) e `.xlsx` (2016); a página oficial as chama de "panorama anual da produção por campo". Não foi encontrado metadado da ANP para elas.
- Três coisas que a ANP tem na mesma página e o fetcher não baixa: a série de reinjeção como arquivo próprio (ela vem como bloco dentro da planilha de gás), os meses de 2024 em diante por poço (a página manda usar a Consulta de Dados Públicos) e a produção por poço em CSV nos dados abertos (veja `producao-poco-abertos`).
- No bruto, o arquivo é `producao-petroleo-gas/<nome>@AAAAMMDD.<ext>`, com o sufixo da data da coleta. A amostra tem 2 das 3 séries nacionais (a de gás natural foi lida à parte, fora da amostra), os ZIP de 2009 e 2017 e as planilhas por campo de 2009 e 2016.

## Conteúdo

- **Séries nacionais (dataset `ppg-historico`, sem partição).** Cada planilha vira uma tabela larga: `planilha`, `tabela`, `tabela_fonte`, `Mês` e uma coluna `ANO <aaaa>` por ano (2000 a 2026), mais `VARIAÇÃO DO ACUMULADO NO ANO (%)`. Cada bloco tem 13 linhas (12 meses e `Total do Ano`): a amostra de petróleo tem 26 linhas por planilha (petróleo e LGN). Os blocos de gás natural, lidos à parte, têm cinco tabelas (produção, reinjeção, queima e perda, consumo próprio e disponível), 13 linhas cada. Os valores são o total do Brasil (filtros `(Tudo)` da planilha).
- **Por poço (dataset `ppg`, partição `ano`).** Um Parquet por ambiente e ano (`producao-poco_<ano>__<ano>_producao_mar|terra.parquet`) com 20 colunas: `Estado`, `Bacia`, `Nome Poço ANP`, `Nome Poço Operador`, `Campo`, `Operador`, `Número do Contrato`, `Período`, `Óleo`, `Condensado`, `Petróleo`, `Gás Natural` (associado, não associado e total), `Volume Gás Royalties`, `Água`, `Instalação Destino`, `Tipo Instalação`, `Tempo de Produção (hs por mês)` e `ambiente`. Amostra: 2009 (mar 9.821 linhas; terra 93.773) e 2017 (mar 16.448; terra 132.668). O pré-sal de 2017 (986 linhas na amostra) fica em `ppg-presal`, partição `ano`.
- **Por campo (dataset `ppg`, partição `ano`).** Um Parquet por planilha: 2009 (3.804 linhas, 8 colunas) e 2016 (3.574 linhas, 8 colunas com outro cabeçalho).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2009 | `ppg` (8); `ppg` (20); `ppg` (20) |
| 2016 | `ppg` (8) |
| 2017 | `ppg` (20); `ppg` (20); `ppg-presal` (20) |

## Variáveis

As descrições das colunas por poço vêm do metadado "Dados de Produção por Poço (2005-2017)" da ANP; as das planilhas nacionais, das notas da própria planilha; as de campo, dos valores observados e dos nomes das colunas (a ANP não publica metadado para elas), quando indicado "deduzida" ou "não informada". As três famílias compartilham colunas só em parte: veja a coluna *Arquivos*.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Estado` | `Estado` | texto | Estado da federação onde foi perfurado o poço (nome por extenso; o metadado fala em sigla). | — | todo | `ppg`, `ppg-presal` |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar onde foi perfurado o poço. | — | todo | `ppg`, `ppg-presal` |
| `Campo` | `Campo` | texto | Nome do campo de produção onde foi perfurado o poço. | — | todo | `ppg`, `ppg-presal` |
| `Operador` | `Operador` | texto | Nome fantasia do operador (concessionário). | — | todo | `ppg`, `ppg-presal` |
| `Número do Contrato` | `Número do Contrato` | texto | Número do contrato de concessão celebrado com a ANP. | — | todo | `ppg`, `ppg-presal` |
| `Período` | `Período` | texto | Período (ano e mês, AAAA/MM). | — | todo | `ppg`, `ppg-presal` |
| `Petróleo (bbl/dia)` | `Petróleo (bbl/dia)` | texto | Volume de petróleo (óleo mais condensado), em barris por dia. | — | todo | `ppg`, `ppg-presal` |
| `Total Gás Natural (Mm³/dia)` | `Total Gás Natural (Mm³/dia)` | texto | Volume total de gás natural do campo, em milhares de m³ por dia. | — | 2009 | `ppg` |
| `Nome Poço ANP` | `Nome Poço ANP` | texto | Nome do poço segundo a Resolução ANP nº 699/2017. | — | todo | `ppg`, `ppg-presal` |
| `Nome Poço Operador` | `Nome Poço Operador` | texto | Nome do poço no cadastro próprio do operador. | — | todo | `ppg`, `ppg-presal` |
| `Óleo (bbl/dia)` | `Óleo (bbl/dia)` | texto | Volume de óleo, em barris por dia. | — | todo | `ppg`, `ppg-presal` |
| `Condensado (bbl/dia)` | `Condensado (bbl/dia)` | texto | Volume de condensado, em barris por dia. | — | todo | `ppg`, `ppg-presal` |
| `Gás Natural (Mm³/dia) Associado` | `Gás Natural (Mm³/dia) Associado` | texto | Volume de gás natural associado, em milhares de m³ por dia. | — | todo | `ppg`, `ppg-presal` |
| `Gás Natural (Mm³/dia) Não Associado` | `Gás Natural (Mm³/dia) Não Associado` | texto | Volume de gás natural não associado, em milhares de m³ por dia. | — | todo | `ppg`, `ppg-presal` |
| `Gás Natural (Mm³/dia) Gás Total` | `Gás Natural (Mm³/dia) Gás Total` | texto | Volume de gás natural total (associado mais não associado), em milhares de m³ por dia. | — | todo | `ppg`, `ppg-presal` |
| `Volume Gás Royalties (Mm³/dia)` | `Volume Gás Royalties (Mm³/dia)` | texto | Volume de gás sobre o qual incidem royalties, em milhares de m³ por dia (no metadado da ANP o nome atual é `(m³/mês)` e a descrição diz `Mm³/dia`). | — | todo | `ppg`, `ppg-presal` |
| `Água (bbl/dia)` | `Água (bbl/dia)` | texto | Volume de água produzida, em barris por dia. | — | todo | `ppg`, `ppg-presal` |
| `Instalação Destino` | `Instalação Destino` | texto | Nome da instalação destinatária dos volumes produzidos no poço. | — | todo | `ppg`, `ppg-presal` |
| `Tipo Instalação` | `Tipo Instalação` | texto | Tipo da instalação destinatária (`UEP` ou `INSTALACAO EMB/DESEMB` na amostra de 2023). | — | todo | `ppg`, `ppg-presal` |
| `Tempo de Produção (hs por mês)` | `Tempo de Produção (hs por mês)` | texto | Número de horas que o poço produziu no mês. | — | todo | `ppg`, `ppg-presal` |
| `ambiente` | `ambiente` | texto | Ambiente do arquivo de origem dentro do ZIP: `mar`, `terra` ou `presal` (coluna acrescentada pelo conversor, a partir do nome do membro do ZIP). O pré-sal é um subconjunto de mar. | — | todo | `ppg`, `ppg-presal` |
| `NOM_BACIA` | `NOM_BACIA` | texto | Nome da bacia sedimentar do campo. | — | 2016 | `ppg` |
| `NOM_CAMPO` | `NOM_CAMPO` | texto | Nome do campo. | — | 2016 | `ppg` |
| `PERIODO` | `PERIODO` | texto | Período (ano e mês, AAAA/MM). | — | 2016 | `ppg` |
| `OLEO_M3` | `OLEO_M3` | texto | Volume de óleo do campo no período, em m³ (o cabeçalho diz `M3`; o arquivo não informa se é por mês ou por dia). | — | 2016 | `ppg` |
| `CONDENSADO_M3` | `CONDENSADO_M3` | texto | Volume de condensado do campo no período, em m³. | — | 2016 | `ppg` |
| `GAS_ASSOCIADO_M3` | `GAS_ASSOCIADO_M3` | texto | Volume de gás natural associado do campo no período; o cabeçalho diz `M3`, mas a unidade não é informada pela fonte (milhares de m³ nas séries irmãs). | — | 2016 | `ppg` |
| `GAS_N_ASSOCIADO_M3` | `GAS_N_ASSOCIADO_M3` | texto | Volume de gás natural não associado do campo no período; unidade como em `GAS_ASSOCIADO_M3`. | — | 2016 | `ppg` |
| `AGUA_M3` | `AGUA_M3` | texto | Volume de água produzida do campo no período, em m³. | — | 2016 | `ppg` |
| `planilha` | `planilha` | texto | Nome da planilha de origem, sem extensão: `producao-petroleo-m3`, `producao-petroleo-b` ou `producao-gas-natural-m3` (coluna acrescentada pelo conversor). | — | — | `ppg-historico` |
| `tabela` | `tabela` | texto | Título do bloco de dados dentro da planilha, com a unidade (por exemplo, `Produção nacional de LGN por Unidade da Federação (m³)`); a unidade dos valores de `ANO <aaaa>` é a do título (coluna do conversor). | — | — | `ppg-historico` |
| `tabela_fonte` | `tabela_fonte` | texto | Título completo do bloco no cabeçalho da planilha, com o período, como `... - 2000-2026 (m³)` (coluna do conversor). | — | — | `ppg-historico` |
| `Mês` | `Mês` | texto | Mês por extenso (`Janeiro` a `Dezembro`) ou `Total do Ano`; a linha de total convive com as de mês na mesma coluna. | — | — | `ppg-historico` |
| `ANO 2000` | `ANO 2000` | decimal | Volume nacional do mês no ano 2000, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2001` | `ANO 2001` | decimal | Volume nacional do mês no ano 2001, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2002` | `ANO 2002` | decimal | Volume nacional do mês no ano 2002, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2003` | `ANO 2003` | decimal | Volume nacional do mês no ano 2003, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2004` | `ANO 2004` | decimal | Volume nacional do mês no ano 2004, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2005` | `ANO 2005` | decimal | Volume nacional do mês no ano 2005, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2006` | `ANO 2006` | decimal | Volume nacional do mês no ano 2006, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2007` | `ANO 2007` | decimal | Volume nacional do mês no ano 2007, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2008` | `ANO 2008` | decimal | Volume nacional do mês no ano 2008, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2009` | `ANO 2009` | decimal | Volume nacional do mês no ano 2009, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2010` | `ANO 2010` | decimal | Volume nacional do mês no ano 2010, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2011` | `ANO 2011` | decimal | Volume nacional do mês no ano 2011, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2012` | `ANO 2012` | decimal | Volume nacional do mês no ano 2012, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2013` | `ANO 2013` | decimal | Volume nacional do mês no ano 2013, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2014` | `ANO 2014` | decimal | Volume nacional do mês no ano 2014, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2015` | `ANO 2015` | decimal | Volume nacional do mês no ano 2015, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2016` | `ANO 2016` | decimal | Volume nacional do mês no ano 2016, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2017` | `ANO 2017` | decimal | Volume nacional do mês no ano 2017, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2018` | `ANO 2018` | decimal | Volume nacional do mês no ano 2018, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2019` | `ANO 2019` | decimal | Volume nacional do mês no ano 2019, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2020` | `ANO 2020` | decimal | Volume nacional do mês no ano 2020, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2021` | `ANO 2021` | decimal | Volume nacional do mês no ano 2021, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2022` | `ANO 2022` | decimal | Volume nacional do mês no ano 2022, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2023` | `ANO 2023` | decimal | Volume nacional do mês no ano 2023, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2024` | `ANO 2024` | decimal | Volume nacional do mês no ano 2024, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2025` | `ANO 2025` | decimal | Volume nacional do mês no ano 2025, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `ANO 2026` | `ANO 2026` | decimal | Volume nacional do mês no ano 2026, na unidade do título de `tabela` (m³, barris ou mil m³); vazio nos meses ainda não publicados. | — | — | `ppg-historico` |
| `VARIAÇÃO DO ACUMULADO NO ANO (%)` | `VARIAÇÃO DO ACUMULADO NO ANO (%)` | decimal | Variação percentual do somatório de janeiro até o mês no ano corrente (2026) em relação ao mesmo período do ano anterior (nota 1 da planilha); vazia nas linhas de total. | — | — | `ppg-historico` |

## No lake

- Datasets `anp/ppg` (`ano=<ano>/producao-poco_<ano>__<ano>_producao_<ambiente>.parquet` e `ano=<ano>/producao-campo_<ano>.parquet`), `anp/ppg-presal` (`ano=<ano>/producao-poco_<ano>__<ano>_producao_presal.parquet`) e `anp/ppg-historico` (sem partição: `producao-petroleo-m3.parquet`, `producao-petroleo-b.parquet` e `producao-gas-natural-m3.parquet`).
- Os valores são texto nas tabelas por poço e por campo e `decimal` nas séries nacionais (`ANO <aaaa>` e a variação). A coluna `ambiente` (`mar`, `terra`, `presal`) é acrescentada pelo conversor a partir do nome do XLSX dentro do ZIP.

## Cuidados de uso

- **Três famílias, três esquemas.** As séries nacionais são largas (uma coluna por ano) e empilham blocos de tabelas e de unidades diferentes na mesma tabela; sempre filtre por `tabela` e remova `Total do Ano` antes de somar meses. Poços e campos são longos (uma linha por poço ou campo e mês).
- **Ponto decimal, não vírgula.** Nas planilhas por poço e por campo os números vêm em texto com ponto decimal (`811.3496`, em 101.172 das 132.668 linhas de petróleo de 2017 da amostra), ao contrário dos CSV de `producao-poco-abertos` (vírgula e ponto de milhar).
- **Unidade muda entre as eras de campo.** Em 2009, petróleo em bbl/dia e gás total em Mm³/dia (valores diários); em 2016, `OLEO_M3`, `CONDENSADO_M3`, `GAS_*_M3` e `AGUA_M3` em m³, sem dizer se o período é mês ou dia, e sem dizer a unidade do gás. Não compare as duas eras diretamente.
- **Mais de uma linha por poço e mês.** Em 2017, terra tem 132.668 linhas e 130.465 pares `(Nome Poço ANP, Período)` distintos; a chave do dataset fica vazia.
- **Pré-sal é subconjunto de mar.** `ppg-presal` repete poços que também estão no XLSX de mar; não some os dois.
- **Meses futuros em branco.** Nas séries nacionais, as colunas de 2026 têm valores só até setembro (a coleta é de 2026-11-15, com dados atualizados em 29/10/2026); outubro a dezembro vêm vazios, e o `Total do Ano` de 2026 soma só até setembro.
- **Instalação ausente.** `Instalação Destino` está vazia em todas as 93.773 linhas de terra de 2009 e em 6.018 das 16.448 de mar de 2017.
- **Não coletado pelo fetcher:** os anos de poços a partir de 2024 e a reinjeção como arquivo próprio. Os ZIP de 2018 a 2023 estão no catálogo mas não na amostra.
- **Dados pessoais.** Não há: poços, campos e empresas operadoras.

## Exemplos

Produção nacional de petróleo (m³) por mês de 2025, a partir da série `producao-petroleo-m3` (o bloco de petróleo; o de LGN fica na mesma tabela e é descartado pelo filtro em `tabela`):

```python
import duckdb

duckdb.sql("""
    SELECT "Mês" AS mes, round("ANO 2025") AS petroleo_m3
    FROM read_parquet('lake/anp/ppg-historico/producao-petroleo-m3.parquet')
    WHERE tabela LIKE 'Produção nacional de petróleo%' AND "Mês" <> 'Total do Ano'
""").show()
```

## Referências

- Dados estatísticos da ANP (produção de petróleo e gás natural): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/dados-estatisticos
- Metadados da produção por poço: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-petroleo-e-gas-natural-por-poco/metadados-dados-producao-poco-2005-2017.pdf
