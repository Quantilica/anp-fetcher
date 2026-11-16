---
dataset:
  id: vdpb
  fonte: anp
  titulo: Vendas de derivados de petróleo e biocombustíveis — planilhas dos dados estatísticos
  resumo: Vendas municipais anuais de asfalto, etanol hidratado, gasolina C e gasolina de aviação (2000 a 2024) e totais mensais das vendas das distribuidoras (2000 a 2026), em m³ e barris.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual nas planilhas municipais (a última é a de 2024); mensal nas planilhas de totais (atualizadas em 29/10/2026, com dados até setembro de 2026)
  cobertura:
    inicio: '2000'
    fim: 2026-09
  unidade: 'duas formas: um município (ou linha de estado ou de total) num ano para um produto, nas planilhas municipais; e um mês (ou o total do ano) de uma tabela, com os anos em colunas, nas planilhas de totais'
  granularidade:
    espacial: município nas planilhas municipais; Brasil nas de totais (só o total geral de cada tabela dinâmica, sem UF)
    temporal: ano (planilhas municipais, partição `ano`) e mês e ano (planilhas de totais)
  formato_bruto: XLS e XLSX; as municipais são uma planilha por produto e ano com cabeçalho de quatro linhas, e as de totais são `vendas-combustiveis-m3.xls` e `vendas-combustiveis-b.xls`, com as 10 tabelas dinâmicas em uma aba
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 38
  unidades_de_medida:
    Vendas: litro ou quilo, conforme a coluna `unidade`
    ANO 2000: conforme `tabela`
    ANO 2001: conforme `tabela`
    ANO 2002: conforme `tabela`
    ANO 2003: conforme `tabela`
    ANO 2004: conforme `tabela`
    ANO 2005: conforme `tabela`
    ANO 2006: conforme `tabela`
    ANO 2007: conforme `tabela`
    ANO 2008: conforme `tabela`
    ANO 2009: conforme `tabela`
    ANO 2010: conforme `tabela`
    ANO 2011: conforme `tabela`
    ANO 2012: conforme `tabela`
    ANO 2013: conforme `tabela`
    ANO 2014: conforme `tabela`
    ANO 2015: conforme `tabela`
    ANO 2016: conforme `tabela`
    ANO 2017: conforme `tabela`
    ANO 2018: conforme `tabela`
    ANO 2019: conforme `tabela`
    ANO 2020: conforme `tabela`
    ANO 2021: conforme `tabela`
    ANO 2022: conforme `tabela`
    ANO 2023: conforme `tabela`
    ANO 2024: conforme `tabela`
    ANO 2025: conforme `tabela`
    ANO 2026: conforme `tabela`
    VARIAÇÃO DO ACUMULADO NO ANO (%): '%'
  dados_pessoais: nenhum
  eras:
  - desde: '2000'
    mudanca: primeiros arquivos municipais (2000) e primeiros totais mensais (janeiro de 2000)
  - desde: '2007'
    mudanca: até 2006 a fonte era o Demonstrativo de Controle de Produtos (DCP) e as vendas incluem o consumo próprio das distribuidoras; a partir de 2007 a fonte é o Sistema de Informações de Movimentação de Produtos (SIMP) e só entram as vendas
  - desde: '2010'
    mudanca: o produto de etanol passa a se chamar `ETANOL HIDRATADO` no título da planilha municipal (de 2000 a 2009 é `ALCOOL HIDRATADO`)
  - desde: '2017'
    mudanca: as planilhas municipais passam a ser `.xlsx` (até 2016 são `.xls`, com exceções)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Vendas de derivados de petróleo e biocombustíveis — planilhas dos dados estatísticos

## Resumo

Dois conjuntos de planilhas da ANP sobre as vendas de combustíveis pelas distribuidoras. O primeiro são as vendas anuais por município de quatro produtos (asfalto, etanol hidratado, gasolina C e gasolina de aviação), uma planilha por produto e ano, de 2000 a 2024. O segundo são duas planilhas de totais mensais (em m³ e em barris), com 10 tabelas cada (derivados por produto, óleo diesel por tipo e por segmento, GLP por vasilhame, etanol e gasolina por segmento, óleo diesel das produtoras), com meses nas linhas e anos nas colunas, de 2000 a 2026. Os mesmos dados, em CSV com mais recortes, estão em `vdpb-abertos`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/vdpb` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual nas planilhas municipais (a última é a de 2024); mensal nas planilhas de totais (atualizadas em 29/10/2026, com dados até setembro de 2026) |
| Cobertura | 2000 a 2026-09 |
| Unidade (uma linha) | duas formas: um município (ou linha de estado ou de total) num ano para um produto, nas planilhas municipais; e um mês (ou o total do ano) de uma tabela, com os anos em colunas, nas planilhas de totais |
| Granularidade | espacial: município nas planilhas municipais; Brasil nas de totais (só o total geral de cada tabela dinâmica, sem UF); temporal: ano (planilhas municipais, partição `ano`) e mês e ano (planilhas de totais) |
| Formato bruto | XLS e XLSX; as municipais são uma planilha por produto e ano com cabeçalho de quatro linhas, e as de totais são `vendas-combustiveis-m3.xls` e `vendas-combustiveis-b.xls`, com as 10 tabelas dinâmicas em uma aba |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 38 |
| Unidades de medida | `Vendas`: litro ou quilo, conforme a coluna `unidade`; `ANO 2000`: conforme `tabela`; `ANO 2001`: conforme `tabela`; `ANO 2002`: conforme `tabela`; `ANO 2003`: conforme `tabela`; `ANO 2004`: conforme `tabela`; `ANO 2005`: conforme `tabela`; `ANO 2006`: conforme `tabela`; `ANO 2007`: conforme `tabela`; `ANO 2008`: conforme `tabela`; `ANO 2009`: conforme `tabela`; `ANO 2010`: conforme `tabela`; `ANO 2011`: conforme `tabela`; `ANO 2012`: conforme `tabela`; `ANO 2013`: conforme `tabela`; `ANO 2014`: conforme `tabela`; `ANO 2015`: conforme `tabela`; `ANO 2016`: conforme `tabela`; `ANO 2017`: conforme `tabela`; `ANO 2018`: conforme `tabela`; `ANO 2019`: conforme `tabela`; `ANO 2020`: conforme `tabela`; `ANO 2021`: conforme `tabela`; `ANO 2022`: conforme `tabela`; `ANO 2023`: conforme `tabela`; `ANO 2024`: conforme `tabela`; `ANO 2025`: conforme `tabela`; `ANO 2026`: conforme `tabela`; `VARIAÇÃO DO ACUMULADO NO ANO (%)`: % |
| Dados pessoais | nenhum |
| Eras | 2000: primeiros arquivos municipais (2000) e primeiros totais mensais (janeiro de 2000); 2007: até 2006 a fonte era o Demonstrativo de Controle de Produtos (DCP) e as vendas incluem o consumo próprio das distribuidoras; a partir de 2007 a fonte é o Sistema de Informações de Movimentação de Produtos (SIMP) e só entram as vendas; 2010: o produto de etanol passa a se chamar `ETANOL HIDRATADO` no título da planilha municipal (de 2000 a 2009 é `ALCOOL HIDRATADO`); 2017: as planilhas municipais passam a ser `.xlsx` (até 2016 são `.xls`, com exceções) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa duas planilhas de totais de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/` (`vendas-combustiveis-m3.xls` e `vendas-combustiveis-b.xls`) e 100 planilhas municipais de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/arquivos-vendas-de-derivados-de-petroleo-e-biocombustiveis/<produto>/` (`asfalto-municipio-<AAAA>.xls`, `etanol-hidratado-municipio-<AAAA>.xls`, `gasolina-c-municipio-<AAAA>.xls` e `gasolina-aviacao-municipio-<AAAA>.xls`, de 2000 a 2024).
- Fonte do dado, segundo as notas das planilhas: ANP, conforme a Resolução ANP nº 729/2018; até 2006 a fonte foi o DCP e daí em diante o SIMP; até 2006 incluem consumo próprio das distribuidoras. As planilhas de totais trazem também as misturas obrigatórias de biodiesel ao diesel e de etanol anidro à gasolina C ao longo do tempo.
- Nas notas das planilhas de totais: «vasilhame: Até P13 inclui P2, P5, P7, P8 e P13; Outros inclui P20, P45, P90 e granel», e as informações são preliminares e podem sofrer ajustes. A conversão de m³ para barril usa o fator 6,28981.
- Os metadados em PDF existem para os arquivos de dados abertos (`vdpb-abertos`); para as planilhas não há dicionário à parte, e as descrições vêm dos títulos e das notas das próprias planilhas.

## Conteúdo

- **Planilhas municipais** (dataset `anp/vdpb`, partição `ano`): 100 arquivos (4 produtos × 25 anos, 2000 a 2024), 306.650 linhas. Cada planilha tem quatro linhas de título (órgão, produto, `UNIDADE DE MEDIDA` e `ANO`), o cabeçalho (`CÓDIGO IBGE`, `Município`, `Vendas`) e as linhas de dados; o conversor acrescenta `produto`, `produto_fonte` e `unidade`.
- **Linhas que não são município.** Das 306.650 linhas, 303.499 têm código IBGE de 7 dígitos (5.978 municípios distintos); as demais são linhas de estado (nome do estado, da UF ou `ESTADO <nome>`, sem código) e de total (`TOTAL BRASIL`, `Total TO`, `TOTAL GERAL`). Em 83 das 97 combinações de ano e produto cuja linha de total do Brasil foi identificada pelo nome, a soma de `Vendas` das linhas com código de 7 dígitos coincide com esse total; nas outras 14 há diferenças (por exemplo, etanol de 2000 a 2002 e asfalto de 2011 e 2012); outras três combinações trazem o total com outro rótulo (`Total Geral` na coluna de código, por exemplo) e não entraram na comparação.
- **Unidades.** Asfalto em quilos (`QUILO`); etanol hidratado, gasolina C e gasolina de aviação em litros (`LITRO`).
- **Três planilhas repetidas pela fonte.** `gasolina-c` de 2004, `asfalto` de 2006 e `gasolina-aviacao` de 2014 são idênticas (byte a byte) às de 2003, 2007 e 2015, respectivamente, e trazem o ano dessas no título (`ANO 2003`, `ANO: 2007`, `ANO: 2015`). Na partição `ano` do lake, esses três anos de cada produto repetem os dados do ano vizinho.
- **Planilhas de totais** (dataset `anp/vdpb-historico`, sem partição): duas planilhas, `vendas-combustiveis-m3` e `vendas-combustiveis-b`, com 10 tabelas de 13 linhas cada (260 linhas no total), em formato largo (uma coluna por ano, de `ANO 2000` a `ANO 2026`). O lake só tem o total geral de cada tabela dinâmica (filtros em «Tudo»): não há abertura por UF, produto, segmento ou vasilhame. Os pares «por Unidade da Federação» e «por Grande Região» têm valores idênticos (conferido nos derivados por produto).

| Tabela (`tabela`, sem a unidade) | Planilhas e unidades | Anos com dado | Último mês do último ano | `Total do Ano` (ou `Média do Ano`) do último ano vazio em |
|---|---|---|---|---|
| Vendas, pelas distribuidoras, dos derivados combustíveis de petróleo por Unidade da Federação e produto | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2000 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, dos derivados combustíveis de petróleo por Grande Região e produto | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2000 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, de óleo diesel por tipo e Unidade da Federação | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2013 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, de óleo diesel por tipo e Grande Região | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2013 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, de GLP por Unidade da Federação e Vasilhame | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2007 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, de GLP por Região e Vasilhame | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2007 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, de etanol hidratado por segmento e Unidade da Federação | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2012 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, de gasolina C por segmento e Unidade da Federação | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2012 a 2026 | setembro | — |
| Vendas, pelas distribuidoras, de óleo diesel por segmento e Unidade da Federação | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2012 a 2026 | setembro | — |
| Vendas, pelas produtoras, de óleo diesel por Unidade da Federação | `vendas-combustiveis-b` (b), `vendas-combustiveis-m3` (m³) | 2025 a 2026 | setembro | — |

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2000 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2001 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2002 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2003 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2004 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2005 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2006 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2007 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2008 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2009 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2010 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2011 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2012 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2013 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2014 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2015 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2016 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2017 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2018 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2019 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2020 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2021 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2022 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2023 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |
| 2024 | `vdpb` (6); `vdpb` (6); `vdpb` (6); `vdpb` (6) |

## Variáveis

As descrições das colunas municipais vêm dos títulos e do cabeçalho das planilhas (e dos metadados do arquivo CSV equivalente); as das planilhas de totais, do índice e das notas. `Vendas` é texto: converta com `try_cast(Vendas AS DOUBLE)`.
Os nomes `CÓDIGO IBGE`, `Município`, `Vendas`, `produto`, `produto_fonte`, `unidade` e `ano` são das planilhas municipais; `planilha`, `tabela`, `tabela_fonte`, `Mês`, `ANO AAAA` e `VARIAÇÃO DO ACUMULADO NO ANO (%)` são das de totais (veja a coluna Arquivos).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `CÓDIGO IBGE` | `CÓDIGO IBGE` | texto | Código IBGE do município (7 dígitos); vazio, nulo ou `0` nas linhas de estado e de total, e `Total Geral` em uma linha de 2022 (veja Cuidados de uso) | — | todo | `vdpb` |
| `Município` | `Município` | texto | Nome do município, em maiúsculas e em geral sem acentos; nas linhas sem código traz o nome do estado (`ACRE`, `AC` ou `ESTADO ACRE`, conforme o ano) ou o total (`TOTAL BRASIL`, `Total TO`) | — | todo | `vdpb` |
| `Vendas` | `Vendas` | texto | Volume vendido no ano, em texto: litros (etanol hidratado, gasolina C e gasolina de aviação) ou quilos (asfalto), conforme a coluna `unidade`; vazio nas linhas de estado de alguns anos | — | todo | `vdpb` |
| `produto` | `produto` | texto | Produto da planilha, no formato do nome do arquivo (criado pelo conversor) | asfalto = asfalto; etanol-hidratado = etanol hidratado; gasolina-aviacao = gasolina de aviação; gasolina-c = gasolina C | todo | `vdpb` |
| `produto_fonte` | `produto_fonte` | texto | Produto como escrito no título da planilha (por exemplo `ASFALTO`, `ALCOOL HIDRATADO` até 2009 e `ETANOL HIDRATADO` depois, `GASOLINA DE AVIAÇÃO`, `GASOLINA C`); criado pelo conversor a partir do título | — | todo | `vdpb` |
| `unidade` | `unidade` | texto | Unidade de medida declarada no título da planilha (`UNIDADE DE MEDIDA:`); criada pelo conversor | LITRO = litro; QUILO = quilo (kg) | todo | `vdpb` |
| `planilha` | `PLANILHA` | texto | Nome do arquivo de origem, sem extensão (por exemplo `ie-m3` ou `ie-b`), acrescentado pelo conversor | — | — | `vdpb-historico` |
| `tabela` | `TABELA` | texto | Título da tabela dentro da planilha, sem o período e com a unidade entre parênteses (`m³`, `b`, `bep`, `10³ m³`, `US$ FOB`); nome normalizado pelo conversor a partir de `tabela_fonte` | — | — | `vdpb-historico` |
| `tabela_fonte` | `TABELA_FONTE` | texto | Título da tabela como está no índice da planilha, com o período da série e a unidade (por exemplo, `Importação de petróleo - 2000-2026 (m³)`) | — | — | `vdpb-historico` |
| `Mês` | `MÊS` | texto | Mês da linha, por extenso (`Janeiro` a `Dezembro`), mais as linhas de resumo `Total do Ano` e, nas tabelas de preço médio, `Média do Ano` | — | — | `vdpb-historico` |
| `ANO 2000` | `ANO 2000` | decimal | Valor da tabela no ano 2000, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2001` | `ANO 2001` | decimal | Valor da tabela no ano 2001, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2002` | `ANO 2002` | decimal | Valor da tabela no ano 2002, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2003` | `ANO 2003` | decimal | Valor da tabela no ano 2003, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2004` | `ANO 2004` | decimal | Valor da tabela no ano 2004, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2005` | `ANO 2005` | decimal | Valor da tabela no ano 2005, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2006` | `ANO 2006` | decimal | Valor da tabela no ano 2006, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2007` | `ANO 2007` | decimal | Valor da tabela no ano 2007, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2008` | `ANO 2008` | decimal | Valor da tabela no ano 2008, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2009` | `ANO 2009` | decimal | Valor da tabela no ano 2009, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2010` | `ANO 2010` | decimal | Valor da tabela no ano 2010, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2011` | `ANO 2011` | decimal | Valor da tabela no ano 2011, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2012` | `ANO 2012` | decimal | Valor da tabela no ano 2012, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2013` | `ANO 2013` | decimal | Valor da tabela no ano 2013, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2014` | `ANO 2014` | decimal | Valor da tabela no ano 2014, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2015` | `ANO 2015` | decimal | Valor da tabela no ano 2015, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2016` | `ANO 2016` | decimal | Valor da tabela no ano 2016, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2017` | `ANO 2017` | decimal | Valor da tabela no ano 2017, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2018` | `ANO 2018` | decimal | Valor da tabela no ano 2018, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2019` | `ANO 2019` | decimal | Valor da tabela no ano 2019, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2020` | `ANO 2020` | decimal | Valor da tabela no ano 2020, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2021` | `ANO 2021` | decimal | Valor da tabela no ano 2021, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2022` | `ANO 2022` | decimal | Valor da tabela no ano 2022, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2023` | `ANO 2023` | decimal | Valor da tabela no ano 2023, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2024` | `ANO 2024` | decimal | Valor da tabela no ano 2024, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2025` | `ANO 2025` | decimal | Valor da tabela no ano 2025, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `ANO 2026` | `ANO 2026` | decimal | Valor da tabela no ano 2026, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `vdpb-historico` |
| `VARIAÇÃO DO ACUMULADO NO ANO (%)` | `VARIAÇÃO DO ACUMULADO NO ANO (%)` | decimal | Variação percentual do acumulado de janeiro até o mês da linha, no ano corrente, em relação ao mesmo período do ano anterior (nota da planilha); vazia nas linhas de resumo e nos meses sem dado | — | — | `vdpb-historico` |

## No lake

- Dois datasets: `anp/vdpb`, particionado por `ano`, um Parquet por planilha municipal (`ano=<AAAA>/vendas-municipais-<produto>_<AAAA>.parquet`), e `anp/vdpb-historico`, sem partição, um Parquet por planilha de totais (`vendas-combustiveis-m3.parquet` e `vendas-combustiveis-b.parquet`).
- As colunas `produto`, `produto_fonte`, `unidade` (e `planilha`, `tabela`, `tabela_fonte`) são acrescentadas pelo conversor. `ano` vem do nome do arquivo.

## Cuidados de uso

- **Linhas de estado e de total no meio dos municípios.** Somar `Vendas` sem filtro conta cada venda duas ou três vezes (município, estado, total). Filtre `regexp_full_match("CÓDIGO IBGE", '[0-9]{7}')`; duas linhas de gasolina de aviação (2001 e 2003) têm Brasília como `53000108`, com 8 dígitos, e ficam de fora do filtro.
- **Anos repetidos.** As partições `ano=2004` de gasolina C, `ano=2006` de asfalto e `ano=2014` de gasolina de aviação contêm os dados de 2003, 2007 e 2015. Use os arquivos CSV (`vdpb-abertos`) para esses anos: lá os valores de 2004, 2006 e 2014 são outros (por exemplo, gasolina C de 2004: 23,17 bilhões de litros contra 21,79 bilhões de 2003).
- **`Vendas` em texto.** Está vazia em 354 linhas, quase todas de estado (sem código); as unidades mudam entre produtos (`unidade`).
- **Município repetido.** A combinação `ano`, `produto` e `CÓDIGO IBGE` repete-se em 45 casos entre as linhas com código válido.
- **Quebra de série em 2007.** Até 2006 os volumes incluem o consumo próprio das distribuidoras e vêm de outra fonte (DCP).
- **Planilhas de totais.** Não some tabelas diferentes nem as duas planilhas (m³ e barris); em `Total do Ano`, o ano corrente cobre só os meses publicados; em barris, os valores são os de m³ multiplicados por 6,28981 (conferido nos totais anuais das 10 tabelas).
- **Dados pessoais.** Nenhum: são totais por município, estado e Brasil.

## Exemplos

Os cinco municípios com maiores vendas de gasolina C em 2024 (litros), sem as linhas de estado e de total:

```python
import duckdb

duckdb.sql("""
    SELECT "Município", try_cast(Vendas AS DOUBLE) AS litros
    FROM read_parquet('lake/anp/vdpb/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2024 AND produto = 'gasolina-c'
      AND regexp_full_match("CÓDIGO IBGE", '[0-9]{7}')
    ORDER BY litros DESC
    LIMIT 5
""").show()
```

Vendas mensais totais dos derivados combustíveis (m³) em 2024, 2025 e 2026:

```python
import duckdb

duckdb.sql("""
    SELECT "Mês", "ANO 2024", "ANO 2025", "ANO 2026"
    FROM read_parquet('lake/anp/vdpb-historico/vendas-combustiveis-m3.parquet')
    WHERE tabela = 'Vendas, pelas distribuidoras, dos derivados combustíveis de petróleo por Unidade da Federação e produto (m³)'
""").show()
```

## Referências

- Página dos dados abertos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis
- Página dos dados estatísticos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos
- Grupo `vdpb-abertos`: os mesmos dados em CSV, com mais produtos e recortes.
