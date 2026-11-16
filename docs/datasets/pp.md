---
dataset:
  id: pp
  fonte: anp
  titulo: Processamento de petróleo e produção de derivados — planilhas dos dados estatísticos
  resumo: Totais mensais do petróleo refinado e da produção de derivados, gases combustíveis, derivados de xisto e de centrais petroquímicas e de outros produtores, de 2000 em diante, em m³ e barris.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/processamento-de-petroleo-e-producao-de-derivados
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; planilhas atualizadas em 29/10/2026, com dados até setembro de 2026
  cobertura:
    inicio: 2000-01
    fim: 2026-09
  unidade: uma linha de mês (ou de total do ano) de uma tabela da planilha; os valores de cada ano ficam nas colunas `ANO AAAA`
  granularidade:
    espacial: Brasil (só o total geral de cada tabela dinâmica)
    temporal: mês (linhas) e ano (colunas `ANO AAAA`)
  formato_bruto: 'XLS: uma aba por planilha, com as tabelas dinâmicas em sequência e índice, títulos, notas e rodapés; quatro arquivos (`processamento-petroleo-m3.xls`, `processamento-petroleo-b.xls`, `producao-derivados-m3.xls`, `producao-derivados-b.xls`)'
  lake:
    estado: convertido
    particoes: []
    chave:
    - planilha
    - tabela
    - Mês
    colunas: 32
  unidades_de_medida:
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
    mudanca: petróleo refinado, derivados por refinaria e por UF e gases combustíveis desde janeiro de 2000
  - desde: '2001'
    mudanca: derivados de centrais petroquímicas e de xisto desde 2001; derivados de outros produtores desde 2003
  - desde: '2021'
    mudanca: segundo a fonte das planilhas, até 2020 os dados vinham das próprias empresas (Manguinhos, Petrobras, Riograndense, Univen e Dax Oil; Petrobras nos gases combustíveis e no xisto) e, a partir de 2021, da ANP conforme a Resolução ANP nº 729/2018; em 01/10/2021 a operação da Refinaria Landulpho Alves (RLAM) passou da Petrobras para a Refinaria de Mataripe S/A (nota da planilha)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Processamento de petróleo e produção de derivados — planilhas dos dados estatísticos

## Resumo

Quatro planilhas Excel da ANP: o volume de petróleo refinado nas refinarias nacionais e a produção nacional de derivados de petróleo, cada uma em m³ e em barris. Juntas têm 16 tabelas: petróleo refinado por refinaria e por UF (com a origem nacional ou importada), derivados por refinaria e por UF e produto, gases combustíveis, derivados de centrais petroquímicas, de xisto e de outros produtores. As linhas são os meses (mais o total do ano) e as colunas os anos, de 2000 a 2026. O lake guarda só o total geral de cada tabela dinâmica, sem abertura por refinaria, UF ou produto; os dados detalhados estão em `pp-abertos`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pp` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/processamento-de-petroleo-e-producao-de-derivados |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; planilhas atualizadas em 29/10/2026, com dados até setembro de 2026 |
| Cobertura | 2000-01 a 2026-09 |
| Unidade (uma linha) | uma linha de mês (ou de total do ano) de uma tabela da planilha; os valores de cada ano ficam nas colunas `ANO AAAA` |
| Granularidade | espacial: Brasil (só o total geral de cada tabela dinâmica); temporal: mês (linhas) e ano (colunas `ANO AAAA`) |
| Formato bruto | XLS: uma aba por planilha, com as tabelas dinâmicas em sequência e índice, títulos, notas e rodapés; quatro arquivos (`processamento-petroleo-m3.xls`, `processamento-petroleo-b.xls`, `producao-derivados-m3.xls`, `producao-derivados-b.xls`) |
| Estado no lake | convertido |
| Partições | — |
| Chave | `planilha`, `tabela`, `Mês` |
| Colunas | 32 |
| Unidades de medida | `ANO 2000`: conforme `tabela`; `ANO 2001`: conforme `tabela`; `ANO 2002`: conforme `tabela`; `ANO 2003`: conforme `tabela`; `ANO 2004`: conforme `tabela`; `ANO 2005`: conforme `tabela`; `ANO 2006`: conforme `tabela`; `ANO 2007`: conforme `tabela`; `ANO 2008`: conforme `tabela`; `ANO 2009`: conforme `tabela`; `ANO 2010`: conforme `tabela`; `ANO 2011`: conforme `tabela`; `ANO 2012`: conforme `tabela`; `ANO 2013`: conforme `tabela`; `ANO 2014`: conforme `tabela`; `ANO 2015`: conforme `tabela`; `ANO 2016`: conforme `tabela`; `ANO 2017`: conforme `tabela`; `ANO 2018`: conforme `tabela`; `ANO 2019`: conforme `tabela`; `ANO 2020`: conforme `tabela`; `ANO 2021`: conforme `tabela`; `ANO 2022`: conforme `tabela`; `ANO 2023`: conforme `tabela`; `ANO 2024`: conforme `tabela`; `ANO 2025`: conforme `tabela`; `ANO 2026`: conforme `tabela`; `VARIAÇÃO DO ACUMULADO NO ANO (%)`: % |
| Dados pessoais | nenhum |
| Eras | 2000: petróleo refinado, derivados por refinaria e por UF e gases combustíveis desde janeiro de 2000; 2001: derivados de centrais petroquímicas e de xisto desde 2001; derivados de outros produtores desde 2003; 2021: segundo a fonte das planilhas, até 2020 os dados vinham das próprias empresas (Manguinhos, Petrobras, Riograndense, Univen e Dax Oil; Petrobras nos gases combustíveis e no xisto) e, a partir de 2021, da ANP conforme a Resolução ANP nº 729/2018; em 01/10/2021 a operação da Refinaria Landulpho Alves (RLAM) passou da Petrobras para a Refinaria de Mataripe S/A (nota da planilha) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa quatro planilhas de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/arquivos-processamento-de-petroleo-e-producao-de-derivados/`: `processamento-petroleo-m3.xls`, `processamento-petroleo-b.xls`, `producao-derivados-m3.xls` e `producao-derivados-b.xls` (a página de dados estatísticos as lista como «Volume de petróleo refinado» e «Produção nacional de derivados de petróleo», atualizadas em 29/10/2026).
- Notas das planilhas: as quantidades negativas indicam que a quantidade produzida foi inferior à transferida para compor outros derivados; GLP inclui as UPGNs de LUBNOR, REDUC I e II, Catu e Candeias; coque inclui o energético e o não energético; `Outros não energéticos` inclui diluentes, resíduos não energéticos e GLP não energético; petróleo nacional e importado incluem condensado, e `Outras cargas` incluem resíduos reprocessados nas unidades de destilação.
- Não há metadados de colunas à parte para as planilhas; a descrição vem do índice e das notas. Os metadados em PDF existem para os CSV equivalentes (`pp-abertos`). Órgão responsável: Superintendência de Defesa da Concorrência (ANP/SDC).

## Conteúdo

- **Estrutura.** Quatro planilhas (`planilha`): `processamento-petroleo-m3` e `-b` (2 tabelas cada) e `producao-derivados-m3` e `-b` (6 tabelas cada). Cada tabela tem 13 linhas (`Janeiro` a `Dezembro` e `Total do Ano`); são 208 linhas no total (16 tabelas).
- **Só o total.** Todas as tabelas são dinâmicas com filtros em «Tudo» (refinaria, UF, produto, origem); o lake só tem o total geral. Por isso as tabelas «por refinaria» e «por Unidade da Federação» trazem os mesmos totais (conferido: 115.743.517 m³ de petróleo refinado em 2024 nas duas), e é preciso usar só uma delas.
- **Coerência com o CSV.** O total de 2024 do CSV de processamento de petróleo (`pp-abertos`, 115.743.524 m³) é praticamente o da planilha (115.743.517 m³).
- **Gases combustíveis.** Estão em 10³ m³ na planilha em m³ e em bep (barris equivalentes de petróleo) na de barris; não são comparáveis com as demais tabelas.

| Tabela (`tabela`, sem a unidade) | Planilhas e unidades | Anos com dado | Último mês do último ano | `Total do Ano` (ou `Média do Ano`) do último ano vazio em |
|---|---|---|---|---|
| Volume de petróleo refinado por refinaria e origem (nacional e importada) | `processamento-petroleo-b` (b), `processamento-petroleo-m3` (m³) | 2000 a 2026 | setembro | — |
| Volume de petróleo refinado por Unidade da Federação e origem (nacional e importada) | `processamento-petroleo-b` (b), `processamento-petroleo-m3` (m³) | 2000 a 2026 | setembro | — |
| Produção de derivados de petróleo por refinaria e produto | `producao-derivados-b` (b), `producao-derivados-m3` (m³) | 2000 a 2026 | setembro | — |
| Produção de derivados de petróleo (nas refinarias) por Unidade da Federação e produto | `producao-derivados-b` (b), `producao-derivados-m3` (m³) | 2000 a 2026 | setembro | `producao-derivados-m3` |
| Produção de gases combustíveis por refinaria | `producao-derivados-b` (bep), `producao-derivados-m3` (10³ m³) | 2000 a 2026 | setembro | `producao-derivados-m3` |
| Produção de derivados de petróleo por central petroquímica e produto | `producao-derivados-b` (b), `producao-derivados-m3` (m³) | 2001 a 2026 | setembro | `producao-derivados-m3` |
| Produção de derivados de xisto por produto | `producao-derivados-b` (b), `producao-derivados-m3` (m³) | 2001 a 2026 | setembro | `producao-derivados-m3` |
| Produção de derivados de petróleo por outros tipos de produtores e produto | `producao-derivados-b` (b), `producao-derivados-m3` (m³) | 2003 a 2026 | setembro | `producao-derivados-m3` |

## Variáveis

Sem dicionário de dados à parte, as descrições vêm do índice e das notas das planilhas. As colunas `ANO AAAA` são uma por ano (2000 a 2026); o valor é o volume do mês e do ano, na unidade de `tabela`.
`planilha`, `tabela` e `tabela_fonte` são texto; `Mês` é texto por extenso; as colunas de ano e a variação são decimais.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `planilha` | `PLANILHA` | texto | Nome do arquivo de origem, sem extensão (por exemplo `ie-m3` ou `ie-b`), acrescentado pelo conversor | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `tabela` | `TABELA` | texto | Título da tabela dentro da planilha, sem o período e com a unidade entre parênteses (`m³`, `b`, `bep`, `10³ m³`, `US$ FOB`); nome normalizado pelo conversor a partir de `tabela_fonte` | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `tabela_fonte` | `TABELA_FONTE` | texto | Título da tabela como está no índice da planilha, com o período da série e a unidade (por exemplo, `Importação de petróleo - 2000-2026 (m³)`) | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `Mês` | `MÊS` | texto | Mês da linha, por extenso (`Janeiro` a `Dezembro`), mais as linhas de resumo `Total do Ano` e, nas tabelas de preço médio, `Média do Ano` | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2000` | `ANO 2000` | decimal | Valor da tabela no ano 2000, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2001` | `ANO 2001` | decimal | Valor da tabela no ano 2001, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2002` | `ANO 2002` | decimal | Valor da tabela no ano 2002, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2003` | `ANO 2003` | decimal | Valor da tabela no ano 2003, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2004` | `ANO 2004` | decimal | Valor da tabela no ano 2004, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2005` | `ANO 2005` | decimal | Valor da tabela no ano 2005, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2006` | `ANO 2006` | decimal | Valor da tabela no ano 2006, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2007` | `ANO 2007` | decimal | Valor da tabela no ano 2007, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2008` | `ANO 2008` | decimal | Valor da tabela no ano 2008, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2009` | `ANO 2009` | decimal | Valor da tabela no ano 2009, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2010` | `ANO 2010` | decimal | Valor da tabela no ano 2010, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2011` | `ANO 2011` | decimal | Valor da tabela no ano 2011, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2012` | `ANO 2012` | decimal | Valor da tabela no ano 2012, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2013` | `ANO 2013` | decimal | Valor da tabela no ano 2013, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2014` | `ANO 2014` | decimal | Valor da tabela no ano 2014, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2015` | `ANO 2015` | decimal | Valor da tabela no ano 2015, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2016` | `ANO 2016` | decimal | Valor da tabela no ano 2016, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2017` | `ANO 2017` | decimal | Valor da tabela no ano 2017, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2018` | `ANO 2018` | decimal | Valor da tabela no ano 2018, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2019` | `ANO 2019` | decimal | Valor da tabela no ano 2019, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2020` | `ANO 2020` | decimal | Valor da tabela no ano 2020, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2021` | `ANO 2021` | decimal | Valor da tabela no ano 2021, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2022` | `ANO 2022` | decimal | Valor da tabela no ano 2022, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2023` | `ANO 2023` | decimal | Valor da tabela no ano 2023, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2024` | `ANO 2024` | decimal | Valor da tabela no ano 2024, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2025` | `ANO 2025` | decimal | Valor da tabela no ano 2025, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `ANO 2026` | `ANO 2026` | decimal | Valor da tabela no ano 2026, para o mês da linha; a unidade está em `tabela` (m³, barris, 10³ m³ ou bep); vazio quando o mês ainda não tem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |
| `VARIAÇÃO DO ACUMULADO NO ANO (%)` | `VARIAÇÃO DO ACUMULADO NO ANO (%)` | decimal | Variação percentual do acumulado de janeiro até o mês da linha, no ano corrente, em relação ao mesmo período do ano anterior (nota da planilha); vazia nas linhas de resumo e nos meses sem dado | — | — | `processamento-petroleo-b`, `processamento-petroleo-m3`, `producao-derivados-b` e mais 1 |

## No lake

- Dataset `anp/pp`, sem partições; um Parquet por planilha (`processamento-petroleo-m3.parquet`, `processamento-petroleo-b.parquet`, `producao-derivados-m3.parquet`, `producao-derivados-b.parquet`), cada um com as tabelas empilhadas (`tabela` as distingue).
- As colunas `planilha`, `tabela` e `tabela_fonte` são acrescentadas pelo conversor; os demais nomes vêm do cabeçalho das planilhas.

## Cuidados de uso

- **Tabelas repetidas.** As tabelas «por refinaria e …» e «por Unidade da Federação e …» têm os mesmos totais; as planilhas em m³ e em barris também são a mesma informação (barris = m³ × 6,28981). Use uma só por assunto.
- **`Total do Ano` pode estar vazio no ano corrente.** Na planilha `producao-derivados-m3`, cinco das seis tabelas têm `Total do Ano` de 2026 vazio, embora os meses de janeiro a setembro estejam preenchidos; some os meses.
- **Gases combustíveis em unidade própria** (10³ m³ ou bep), e valores negativos possíveis nas tabelas de derivados (veja Origem e coleta).
- **Tabela larga.** Os anos estão em colunas; desempilhe as colunas `ANO AAAA` para séries longas.
- **Dados pessoais.** Nenhum: são totais nacionais.

## Exemplos

Petróleo refinado por mês (m³) em 2024, 2025 e 2026:

```python
import duckdb

duckdb.sql("""
    SELECT "Mês", "ANO 2024", "ANO 2025", "ANO 2026"
    FROM read_parquet('lake/anp/pp/processamento-petroleo-m3.parquet')
    WHERE tabela = 'Volume de petróleo refinado por refinaria e origem (nacional e importada) (m³)'
""").show()
```

## Referências

- Página dos dados abertos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/processamento-de-petroleo-e-producao-de-derivados
- Página dos dados estatísticos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos
- Grupo `pp-abertos`: os mesmos dados em CSV, com refinaria, UF e produto.
