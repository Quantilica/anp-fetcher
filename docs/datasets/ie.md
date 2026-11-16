---
dataset:
  id: ie
  fonte: anp
  titulo: Importações e exportações — planilhas dos dados estatísticos (m³ e barris)
  resumo: Totais mensais, por ano, da importação e exportação de petróleo, derivados, gás natural e etanol, em duas planilhas (m³ e barris), de 2000 em diante.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; planilhas atualizadas em 29/10/2026 com dados até setembro de 2026
  cobertura:
    inicio: 2000-01
    fim: 2026-09
  unidade: uma linha de mês (ou de total do ano) de uma tabela da planilha; os valores de cada ano ficam nas colunas `ANO AAAA`
  granularidade:
    espacial: Brasil (sem recorte por UF, porto ou país)
    temporal: mês (linhas) e ano (colunas `ANO AAAA`)
  formato_bruto: XLSX com uma aba (`Plan1`) que reúne as 19 tabelas dinâmicas em sequência, com índice, títulos, notas e rodapés; dois arquivos, `importacoes-exportacoes-m3.xlsx` e `importacoes-exportacoes-b.xlsx`
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
    mudanca: tabelas de petróleo, derivados e gás natural desde janeiro de 2000
  - desde: '2006'
    mudanca: 'nota da planilha: a partir de novembro de 2006 a série de exportações de derivados passou a incluir `Combustíveis para Aeronaves` e `Combustíveis para Navios`, e toda a série desde janeiro de 2000 foi revisada'
  - desde: '2012'
    mudanca: tabelas de etanol anidro e hidratado desde janeiro de 2012 (colunas `ANO 2000` a `ANO 2011` vazias nessas tabelas)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Importações e exportações — planilhas dos dados estatísticos (m³ e barris)

## Resumo

Duas planilhas Excel da ANP (uma em metros cúbicos, outra em barris) com 19 tabelas cada: volume importado e exportado e dispêndio ou receita em US$ FOB de petróleo, derivados, gás natural e etanol, e o preço médio do petróleo importado. Em cada tabela, as linhas são os meses (mais o total do ano) e as colunas são os anos, de 2000 (2012 no etanol) a 2026. O lake guarda cada tabela como uma tabela larga de 13 linhas e só o total geral da tabela dinâmica (o filtro de produto fica em «Tudo»): não há abertura por produto de derivado. Os mesmos números, em formato longo, estão em `ie-abertos`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/ie` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; planilhas atualizadas em 29/10/2026 com dados até setembro de 2026 |
| Cobertura | 2000-01 a 2026-09 |
| Unidade (uma linha) | uma linha de mês (ou de total do ano) de uma tabela da planilha; os valores de cada ano ficam nas colunas `ANO AAAA` |
| Granularidade | espacial: Brasil (sem recorte por UF, porto ou país); temporal: mês (linhas) e ano (colunas `ANO AAAA`) |
| Formato bruto | XLSX com uma aba (`Plan1`) que reúne as 19 tabelas dinâmicas em sequência, com índice, títulos, notas e rodapés; dois arquivos, `importacoes-exportacoes-m3.xlsx` e `importacoes-exportacoes-b.xlsx` |
| Estado no lake | convertido |
| Partições | — |
| Chave | `planilha`, `tabela`, `Mês` |
| Colunas | 32 |
| Unidades de medida | `ANO 2000`: conforme `tabela`; `ANO 2001`: conforme `tabela`; `ANO 2002`: conforme `tabela`; `ANO 2003`: conforme `tabela`; `ANO 2004`: conforme `tabela`; `ANO 2005`: conforme `tabela`; `ANO 2006`: conforme `tabela`; `ANO 2007`: conforme `tabela`; `ANO 2008`: conforme `tabela`; `ANO 2009`: conforme `tabela`; `ANO 2010`: conforme `tabela`; `ANO 2011`: conforme `tabela`; `ANO 2012`: conforme `tabela`; `ANO 2013`: conforme `tabela`; `ANO 2014`: conforme `tabela`; `ANO 2015`: conforme `tabela`; `ANO 2016`: conforme `tabela`; `ANO 2017`: conforme `tabela`; `ANO 2018`: conforme `tabela`; `ANO 2019`: conforme `tabela`; `ANO 2020`: conforme `tabela`; `ANO 2021`: conforme `tabela`; `ANO 2022`: conforme `tabela`; `ANO 2023`: conforme `tabela`; `ANO 2024`: conforme `tabela`; `ANO 2025`: conforme `tabela`; `ANO 2026`: conforme `tabela`; `VARIAÇÃO DO ACUMULADO NO ANO (%)`: % |
| Dados pessoais | nenhum |
| Eras | 2000: tabelas de petróleo, derivados e gás natural desde janeiro de 2000; 2006: nota da planilha: a partir de novembro de 2006 a série de exportações de derivados passou a incluir `Combustíveis para Aeronaves` e `Combustíveis para Navios`, e toda a série desde janeiro de 2000 foi revisada; 2012: tabelas de etanol anidro e hidratado desde janeiro de 2012 (colunas `ANO 2000` a `ANO 2011` vazias nessas tabelas) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa duas planilhas de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/ie/`: `importacoes-exportacoes-m3.xlsx` (id `ie-m3`) e `importacoes-exportacoes-b.xlsx` (id `ie-b`); a página de dados estatísticos da ANP as lista como «Importações & exportações (metros cúbicos)» e «(barris)», atualizadas em 29/10/2026.
- Fonte do dado, segundo as notas das planilhas: Secretaria de Comércio Exterior (Ministério da Economia) para petróleo, derivados e etanol; ANP para gás natural. Petróleo inclui óleo e condensado e não inclui LGN; as importações de gás natural só estão em barris equivalentes de petróleo (bep) na planilha de barris e em 10³ m³ na de m³; dólar em valor corrente; FOB significa sem frete no custo da mercadoria.
- Não há metadados de colunas à parte: a descrição vem do índice e das notas da própria planilha. Os arquivos de dados abertos equivalentes (grupo `ie-abertos`) têm metadados em PDF.

## Conteúdo

- **Estrutura.** Cada planilha (`planilha` = `ie-m3` ou `ie-b`) tem 19 tabelas de 13 linhas: `Janeiro` a `Dezembro` e `Total do Ano` (nas tabelas de preço médio, `Média do Ano`). São 494 linhas no total, 247 por planilha.
- **Colunas de ano.** As colunas `ANO 2000` a `ANO 2026` guardam o valor do mês naquele ano; os meses ainda sem dado (outubro a dezembro de 2026) ficam vazios, e as tabelas de etanol não têm valores antes de 2012.
- **Só o total.** As tabelas de derivados por produto (importação, exportação, dispêndio e receita) são tabelas dinâmicas com o filtro de produto em «Tudo»; o lake só tem o total geral. Para abertura por produto, use `ie-abertos`.
- **Relação entre as planilhas.** Nas tabelas de importação de petróleo, derivados e etanol conferidas (janeiro de 2000, 2024 e 2025), o valor em barris é o valor em m³ multiplicado por 6,28981; por isso os valores em m³ têm casas decimais.
- **Tabelas, unidades e cobertura.** (As tabelas de valor, US$ FOB, são iguais nas duas planilhas.)

| Tabela (`tabela`, sem a unidade) | Planilhas e unidades | Anos com dado | Último mês do último ano | `Total do Ano` (ou `Média do Ano`) do último ano vazio em |
|---|---|---|---|---|
| Importação de petróleo | `ie-b` (b), `ie-m3` (m³) | 2000 a 2026 | setembro | — |
| Dispêndio com a importação de petróleo | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2000 a 2026 | setembro | `ie-b` |
| Preço médio do petróleo importado | `ie-b` (US$/b FOB), `ie-m3` (US$/m³ FOB) | 2000 a 2026 | setembro | — |
| Exportação de petróleo | `ie-b` (b), `ie-m3` (m³) | 2000 a 2026 | setembro | — |
| Receita com a exportação de petróleo | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2000 a 2026 | setembro | — |
| Importação de derivados de petróleo por produto | `ie-b` (b), `ie-m3` (m³) | 2000 a 2026 | setembro | — |
| Dispêndio com a importação de derivados de petróleo por produto | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2000 a 2026 | setembro | — |
| Exportação de derivados de petróleo por produto | `ie-b` (b), `ie-m3` (m³) | 2000 a 2026 | setembro | — |
| Receita com a exportação de derivados de petróleo por produto | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2000 a 2026 | setembro | — |
| Importação de gás natural | `ie-b` (bep), `ie-m3` (10³ m³) | 2000 a 2026 | setembro | — |
| Dispêndio com a importação de gás natural | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2000 a 2026 | setembro | — |
| Importação de etanol anidro | `ie-b` (b), `ie-m3` (m³) | 2012 a 2026 | setembro | — |
| Dispêndio com a importação de etanol anidro | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2012 a 2026 | setembro | — |
| Importação de etanol hidratado | `ie-b` (b), `ie-m3` (m³) | 2012 a 2026 | setembro | — |
| Dispêndio com a importação de etanol hidratado | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2012 a 2026 | setembro | — |
| Exportação de etanol anidro | `ie-b` (b), `ie-m3` (m³) | 2012 a 2026 | setembro | — |
| Receita com a exportação de etanol anidro | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2012 a 2026 | setembro | — |
| Exportação de etanol hidratado | `ie-b` (b), `ie-m3` (m³) | 2012 a 2026 | setembro | — |
| Receita com a exportação de etanol hidratado | `ie-b` (US$ FOB), `ie-m3` (US$ FOB) | 2012 a 2026 | setembro | — |

## Variáveis

Sem dicionário de dados à parte, as descrições vêm do índice e das notas das próprias planilhas. As colunas `ANO AAAA` são uma por ano; o nome da coluna traz o ano, e o valor é a medida descrita em `tabela` (volume, valor ou preço), para o mês da linha.
`planilha`, `tabela` e `tabela_fonte` são texto; `Mês` é texto por extenso; as colunas de ano e a variação são decimais.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `planilha` | `PLANILHA` | texto | Nome do arquivo de origem, sem extensão (por exemplo `ie-m3` ou `ie-b`), acrescentado pelo conversor | — | — | `ie-b`, `ie-m3` |
| `tabela` | `TABELA` | texto | Título da tabela dentro da planilha, sem o período e com a unidade entre parênteses (`m³`, `b`, `bep`, `10³ m³`, `US$ FOB`); nome normalizado pelo conversor a partir de `tabela_fonte` | — | — | `ie-b`, `ie-m3` |
| `tabela_fonte` | `TABELA_FONTE` | texto | Título da tabela como está no índice da planilha, com o período da série e a unidade (por exemplo, `Importação de petróleo - 2000-2026 (m³)`) | — | — | `ie-b`, `ie-m3` |
| `Mês` | `MÊS` | texto | Mês da linha, por extenso (`Janeiro` a `Dezembro`), mais as linhas de resumo `Total do Ano` e, nas tabelas de preço médio, `Média do Ano` | — | — | `ie-b`, `ie-m3` |
| `ANO 2000` | `ANO 2000` | decimal | Valor da tabela no ano 2000, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2001` | `ANO 2001` | decimal | Valor da tabela no ano 2001, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2002` | `ANO 2002` | decimal | Valor da tabela no ano 2002, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2003` | `ANO 2003` | decimal | Valor da tabela no ano 2003, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2004` | `ANO 2004` | decimal | Valor da tabela no ano 2004, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2005` | `ANO 2005` | decimal | Valor da tabela no ano 2005, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2006` | `ANO 2006` | decimal | Valor da tabela no ano 2006, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2007` | `ANO 2007` | decimal | Valor da tabela no ano 2007, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2008` | `ANO 2008` | decimal | Valor da tabela no ano 2008, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2009` | `ANO 2009` | decimal | Valor da tabela no ano 2009, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2010` | `ANO 2010` | decimal | Valor da tabela no ano 2010, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2011` | `ANO 2011` | decimal | Valor da tabela no ano 2011, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2012` | `ANO 2012` | decimal | Valor da tabela no ano 2012, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2013` | `ANO 2013` | decimal | Valor da tabela no ano 2013, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2014` | `ANO 2014` | decimal | Valor da tabela no ano 2014, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2015` | `ANO 2015` | decimal | Valor da tabela no ano 2015, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2016` | `ANO 2016` | decimal | Valor da tabela no ano 2016, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2017` | `ANO 2017` | decimal | Valor da tabela no ano 2017, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2018` | `ANO 2018` | decimal | Valor da tabela no ano 2018, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2019` | `ANO 2019` | decimal | Valor da tabela no ano 2019, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2020` | `ANO 2020` | decimal | Valor da tabela no ano 2020, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2021` | `ANO 2021` | decimal | Valor da tabela no ano 2021, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2022` | `ANO 2022` | decimal | Valor da tabela no ano 2022, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2023` | `ANO 2023` | decimal | Valor da tabela no ano 2023, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2024` | `ANO 2024` | decimal | Valor da tabela no ano 2024, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2025` | `ANO 2025` | decimal | Valor da tabela no ano 2025, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `ANO 2026` | `ANO 2026` | decimal | Valor da tabela no ano 2026, para o mês da linha; a unidade está em `tabela` (m³, barris, bep, 10³ m³, US$ FOB ou US$/m³ FOB); vazio quando o mês ainda não tem dado | — | — | `ie-b`, `ie-m3` |
| `VARIAÇÃO DO ACUMULADO NO ANO (%)` | `VARIAÇÃO DO ACUMULADO NO ANO (%)` | decimal | Variação percentual do acumulado de janeiro até o mês da linha, no ano corrente, em relação ao mesmo período do ano anterior (nota da planilha); vazia nas linhas de resumo e nos meses sem dado | — | — | `ie-b`, `ie-m3` |

## No lake

- Dataset `anp/ie`, sem partições; um Parquet por planilha (`ie-m3.parquet` e `ie-b.parquet`), cada um com as 19 tabelas empilhadas (`tabela` as distingue) e uma coluna por ano.
- As colunas `planilha`, `tabela` e `tabela_fonte` são acrescentadas pelo conversor; os demais nomes de coluna vêm do cabeçalho das planilhas (`Mês`, `ANO 2000`, ...).

## Cuidados de uso

- **Não some tabelas diferentes nem as duas planilhas.** `ie-m3` e `ie-b` trazem a mesma informação em unidades diferentes; os valores de US$ FOB repetem-se nas duas.
- **`Total do Ano` não é uma linha de mês.** Filtre `Mês` antes de somar ou agregue só o que precisa. No ano em curso, o total cobre apenas os meses já publicados.
- **Tabela larga.** Os anos estão em colunas; para séries longas, desempilhe (`UNPIVOT`) as colunas `ANO AAAA`.
- **Defeitos da fonte vistos na amostra.** Em `ie-b`, a coluna `ANO 2026` da tabela `Importação de etanol anidro (b)` traz os valores de etanol hidratado em m³ (21,679 em janeiro de 2026, o mesmo valor de `Importação de etanol hidratado (m³)` na planilha em m³), não os barris de etanol anidro (que seriam cerca de 879 mil); em `ie-b`, o `Total do Ano` de 2026 de `Dispêndio com a importação de petróleo (US$ FOB)` está vazio, e na planilha em m³ está preenchido (5,25 bilhões de US$).
- **Gás natural em unidades diferentes.** `bep` na planilha de barris e 10³ m³ na planilha de m³; não são comparáveis diretamente.
- **Dados pessoais.** Nenhum: são totais nacionais.

## Exemplos

Totais anuais de 2024 e 2025 (m³ ou US$ FOB, conforme a tabela) de todas as tabelas da planilha em m³:

```python
import duckdb

duckdb.sql("""
    SELECT tabela, "ANO 2024", "ANO 2025"
    FROM read_parquet('lake/anp/ie/ie-m3.parquet')
    WHERE "Mês" = 'Total do Ano'
    ORDER BY tabela
""").show()
```

## Referências

- Página dos dados abertos (mesmo assunto): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes
- Página dos dados estatísticos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos
- Grupo `ie-abertos`: os mesmos números em CSV, com abertura por produto e operação.
