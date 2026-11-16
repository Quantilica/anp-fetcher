---
dataset:
  id: pb
  fonte: anp
  titulo: Produção de biocombustíveis — planilhas dos dados estatísticos (biodiesel e etanol)
  resumo: Totais mensais da produção nacional de biodiesel B100 (desde 2005) e de etanol anidro e hidratado (desde 2012), em m³ e barris, em quatro planilhas.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; planilhas atualizadas em 27 e 28/10/2026, com dados até setembro de 2026
  cobertura:
    inicio: 2005-01
    fim: 2026-09
  unidade: uma linha de mês (ou de total do ano) de uma tabela da planilha; os valores de cada ano ficam nas colunas `ANO AAAA`
  granularidade:
    espacial: Brasil (só o total geral de cada tabela dinâmica)
    temporal: mês (linhas) e ano (colunas `ANO AAAA`)
  formato_bruto: 'XLS: uma aba por planilha, com as tabelas dinâmicas em sequência e índice, títulos, notas e rodapés; quatro arquivos (`producao-biodiesel-m3.xls`, `producao-biodiesel-b.xls`, `producao-etanol-m3.xls`, `producao-etanol-b.xls`)'
  lake:
    estado: convertido
    particoes: []
    chave:
    - planilha
    - tabela
    - Mês
    colunas: 27
  unidades_de_medida:
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
  - desde: '2005'
    mudanca: 'biodiesel B100 desde 2005 (primeiros volumes pequenos: 736 m³ no ano, segundo o CSV equivalente)'
  - desde: '2012'
    mudanca: etanol anidro e hidratado desde janeiro de 2012; as colunas `ANO 2005` a `ANO 2011` não existem nas planilhas de etanol
  - desde: '2022'
    mudanca: 'nota do metadado e da planilha: com a comercialização direta de biodiesel entre produtores e distribuidores (fim dos leilões da ANP), a ANP deixou de divulgar a produção por produtor e UF e passou a divulgar até o nível de região; no lake, as tabelas por produtor têm dados só até dezembro de 2023, e a por grandes regiões segue até setembro de 2026 (o metadado em PDF fala em janeiro de 2022 e a planilha em janeiro de 2023 como início)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de biocombustíveis — planilhas dos dados estatísticos (biodiesel e etanol)

## Resumo

Quatro planilhas Excel da ANP com a produção de biodiesel puro (B100) e de etanol (anidro e hidratado), cada uma em m³ e em barris. Em cada tabela as linhas são os meses (mais o total do ano) e as colunas são os anos: biodiesel de 2005 a 2026 e etanol de 2012 a 2026. As planilhas têm também as tabelas por estado e produtor e por região e produtor de biodiesel, até 2023, mas o lake guarda só o total geral de cada tabela dinâmica, sem a abertura por UF, produtor ou tipo de etanol. Os mesmos dados, com UF e produtor, estão em CSV no grupo `pb-abertos`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pb` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; planilhas atualizadas em 27 e 28/10/2026, com dados até setembro de 2026 |
| Cobertura | 2005-01 a 2026-09 |
| Unidade (uma linha) | uma linha de mês (ou de total do ano) de uma tabela da planilha; os valores de cada ano ficam nas colunas `ANO AAAA` |
| Granularidade | espacial: Brasil (só o total geral de cada tabela dinâmica); temporal: mês (linhas) e ano (colunas `ANO AAAA`) |
| Formato bruto | XLS: uma aba por planilha, com as tabelas dinâmicas em sequência e índice, títulos, notas e rodapés; quatro arquivos (`producao-biodiesel-m3.xls`, `producao-biodiesel-b.xls`, `producao-etanol-m3.xls`, `producao-etanol-b.xls`) |
| Estado no lake | convertido |
| Partições | — |
| Chave | `planilha`, `tabela`, `Mês` |
| Colunas | 27 |
| Unidades de medida | `ANO 2005`: conforme `tabela`; `ANO 2006`: conforme `tabela`; `ANO 2007`: conforme `tabela`; `ANO 2008`: conforme `tabela`; `ANO 2009`: conforme `tabela`; `ANO 2010`: conforme `tabela`; `ANO 2011`: conforme `tabela`; `ANO 2012`: conforme `tabela`; `ANO 2013`: conforme `tabela`; `ANO 2014`: conforme `tabela`; `ANO 2015`: conforme `tabela`; `ANO 2016`: conforme `tabela`; `ANO 2017`: conforme `tabela`; `ANO 2018`: conforme `tabela`; `ANO 2019`: conforme `tabela`; `ANO 2020`: conforme `tabela`; `ANO 2021`: conforme `tabela`; `ANO 2022`: conforme `tabela`; `ANO 2023`: conforme `tabela`; `ANO 2024`: conforme `tabela`; `ANO 2025`: conforme `tabela`; `ANO 2026`: conforme `tabela`; `VARIAÇÃO DO ACUMULADO NO ANO (%)`: % |
| Dados pessoais | nenhum |
| Eras | 2005: biodiesel B100 desde 2005 (primeiros volumes pequenos: 736 m³ no ano, segundo o CSV equivalente); 2012: etanol anidro e hidratado desde janeiro de 2012; as colunas `ANO 2005` a `ANO 2011` não existem nas planilhas de etanol; 2022: nota do metadado e da planilha: com a comercialização direta de biodiesel entre produtores e distribuidores (fim dos leilões da ANP), a ANP deixou de divulgar a produção por produtor e UF e passou a divulgar até o nível de região; no lake, as tabelas por produtor têm dados só até dezembro de 2023, e a por grandes regiões segue até setembro de 2026 (o metadado em PDF fala em janeiro de 2022 e a planilha em janeiro de 2023 como início) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa quatro planilhas de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/pb/`: `producao-biodiesel-m3.xls`, `producao-biodiesel-b.xls`, `producao-etanol-m3.xls` e `producao-etanol-b.xls`; a página de dados estatísticos as lista como «Produção de biodiesel» e «Produção de etanol» em metros cúbicos e barris (atualizadas em 28/10/2026).
- Fonte, segundo as notas: ANP, conforme a Resolução ANP nº 729/2018; biodiesel B100 conforme a Resolução ANP nº 45/2014; produtores são unidades produtoras autorizadas pela ANP. As informações são preliminares e podem sofrer ajustes.
- As notas das planilhas listam a evolução da mistura obrigatória de biodiesel ao óleo diesel (de 2% em 2008 a 14% desde março de 2025, segundo a nota da planilha) e de etanol anidro à gasolina C.
- Não há metadados de colunas à parte para as planilhas; a descrição vem do índice e das notas da própria planilha. Os metadados em PDF existem para os CSV equivalentes (`pb-abertos`).

## Conteúdo

- **Estrutura.** Quatro planilhas (`planilha`): `producao-biodiesel-m3`, `producao-biodiesel-b`, `producao-etanol-m3` e `producao-etanol-b`. Cada tabela tem 13 linhas (`Janeiro` a `Dezembro` e `Total do Ano`); são 130 linhas no total (10 tabelas).
- **Só o total.** Todas as tabelas são dinâmicas com filtros em «Tudo» (região, estado, produtor, tipo de etanol); o lake só tem o total geral. Por isso as tabelas «por estado e produtor» e «por região e produtor» trazem os mesmos totais, e as de etanol «por UF» e «por Grande Região» também (conferido: 7.532.435,703 m³ de biodiesel em 2023 nas três tabelas; 36.961.311,282 m³ de etanol em 2024 nas duas).
- **Coerência com o CSV.** A soma de 2023 do CSV de biodiesel (`pb-abertos`, 7.532.436 m³) e a de 2024 do CSV de etanol (36.961.311 m³) batem com os totais das planilhas.
- **Cobertura.** Biodiesel de 2005 a 2023 (por produtor) e até 2026 (por grandes regiões); etanol de 2012 a 2026; em 2026 há dados de janeiro a setembro.

| Tabela (`tabela`, sem a unidade) | Planilhas e unidades | Anos com dado | Último mês do último ano | `Total do Ano` (ou `Média do Ano`) do último ano vazio em |
|---|---|---|---|---|
| Produção de biodiesel - B100 por Grandes Regiões | `producao-biodiesel-b` (b), `producao-biodiesel-m3` (m³) | 2005 a 2026 | setembro | — |
| Produção de biodiesel - B100 por estado e produtor | `producao-biodiesel-b` (b), `producao-biodiesel-m3` (m³) | 2005 a 2023 | dezembro | — |
| Produção de biodiesel - B100 por região e produtor | `producao-biodiesel-b` (b), `producao-biodiesel-m3` (m³) | 2005 a 2023 | dezembro | — |
| Produção de etanol anidro e hidratado por Unidade da Federação | `producao-etanol-b` (b), `producao-etanol-m3` (m³) | 2012 a 2026 | setembro | — |
| Produção de etanol anidro e hidratado por Grande Região | `producao-etanol-b` (b), `producao-etanol-m3` (m³) | 2012 a 2026 | setembro | — |

## Variáveis

Sem dicionário de dados à parte, as descrições vêm do índice e das notas das planilhas. As colunas `ANO AAAA` são uma por ano (de 2005 a 2026 nas planilhas de biodiesel; de 2012 a 2026 nas de etanol); o valor é a produção do mês e do ano, na unidade de `tabela`.
`planilha`, `tabela` e `tabela_fonte` são texto; `Mês` é texto por extenso; as colunas de ano e a variação são decimais.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `planilha` | `PLANILHA` | texto | Nome do arquivo de origem, sem extensão (por exemplo `ie-m3` ou `ie-b`), acrescentado pelo conversor | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `tabela` | `TABELA` | texto | Título da tabela dentro da planilha, sem o período e com a unidade entre parênteses (`m³`, `b`, `bep`, `10³ m³`, `US$ FOB`); nome normalizado pelo conversor a partir de `tabela_fonte` | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `tabela_fonte` | `TABELA_FONTE` | texto | Título da tabela como está no índice da planilha, com o período da série e a unidade (por exemplo, `Importação de petróleo - 2000-2026 (m³)`) | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `Mês` | `MÊS` | texto | Mês da linha, por extenso (`Janeiro` a `Dezembro`), mais as linhas de resumo `Total do Ano` e, nas tabelas de preço médio, `Média do Ano` | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2005` | `ANO 2005` | decimal | Valor da tabela no ano 2005, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3` |
| `ANO 2006` | `ANO 2006` | decimal | Valor da tabela no ano 2006, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3` |
| `ANO 2007` | `ANO 2007` | decimal | Valor da tabela no ano 2007, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3` |
| `ANO 2008` | `ANO 2008` | decimal | Valor da tabela no ano 2008, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3` |
| `ANO 2009` | `ANO 2009` | decimal | Valor da tabela no ano 2009, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3` |
| `ANO 2010` | `ANO 2010` | decimal | Valor da tabela no ano 2010, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3` |
| `ANO 2011` | `ANO 2011` | decimal | Valor da tabela no ano 2011, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3` |
| `ANO 2012` | `ANO 2012` | decimal | Valor da tabela no ano 2012, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2013` | `ANO 2013` | decimal | Valor da tabela no ano 2013, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2014` | `ANO 2014` | decimal | Valor da tabela no ano 2014, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2015` | `ANO 2015` | decimal | Valor da tabela no ano 2015, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2016` | `ANO 2016` | decimal | Valor da tabela no ano 2016, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2017` | `ANO 2017` | decimal | Valor da tabela no ano 2017, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2018` | `ANO 2018` | decimal | Valor da tabela no ano 2018, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2019` | `ANO 2019` | decimal | Valor da tabela no ano 2019, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2020` | `ANO 2020` | decimal | Valor da tabela no ano 2020, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2021` | `ANO 2021` | decimal | Valor da tabela no ano 2021, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2022` | `ANO 2022` | decimal | Valor da tabela no ano 2022, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2023` | `ANO 2023` | decimal | Valor da tabela no ano 2023, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2024` | `ANO 2024` | decimal | Valor da tabela no ano 2024, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2025` | `ANO 2025` | decimal | Valor da tabela no ano 2025, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `ANO 2026` | `ANO 2026` | decimal | Valor da tabela no ano 2026, para o mês da linha; a unidade está em `tabela` (m³ ou barris); vazio quando o mês ainda não tem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |
| `VARIAÇÃO DO ACUMULADO NO ANO (%)` | `VARIAÇÃO DO ACUMULADO NO ANO (%)` | decimal | Variação percentual do acumulado de janeiro até o mês da linha, no ano corrente, em relação ao mesmo período do ano anterior (nota da planilha); vazia nas linhas de resumo e nos meses sem dado | — | — | `producao-biodiesel-b`, `producao-biodiesel-m3`, `producao-etanol-b` e mais 1 |

## No lake

- Dataset `anp/pb`, sem partições; um Parquet por planilha (`producao-biodiesel-m3.parquet`, `producao-biodiesel-b.parquet`, `producao-etanol-m3.parquet` e `producao-etanol-b.parquet`), cada um com as tabelas empilhadas (`tabela` as distingue).
- As colunas `planilha`, `tabela` e `tabela_fonte` são acrescentadas pelo conversor; os demais nomes vêm do cabeçalho das planilhas.

## Cuidados de uso

- **Tabelas repetidas.** As tabelas por estado e produtor e por região e produtor (e as de etanol por UF e por grande região) têm os mesmos totais; use só uma por assunto, ou você conta duas vezes. As planilhas em m³ e em barris também são a mesma informação (barris = m³ × 6,28981; conferido nos totais anuais).
- **`Total do Ano` não é um mês.** Filtre `Mês` antes de somar. No ano em curso o total cobre só os meses publicados.
- **Tabelas por produtor terminam em 2023.** Para 2024 em diante só há o total por grandes regiões (biodiesel) e o etanol por UF/região.
- **Dados preliminares.** A ANP avisa que as informações podem sofrer ajustes nas atualizações seguintes.
- **Tabela larga.** Os anos estão em colunas; desempilhe as colunas `ANO AAAA` para séries longas.
- **Dados pessoais.** Nenhum: são totais nacionais.

## Exemplos

Produção mensal de etanol anidro e hidratado (m³) em 2024, 2025 e 2026:

```python
import duckdb

duckdb.sql("""
    SELECT "Mês", "ANO 2024", "ANO 2025", "ANO 2026"
    FROM read_parquet('lake/anp/pb/producao-etanol-m3.parquet')
    WHERE tabela = 'Produção de etanol anidro e hidratado por Grande Região (m³)'
""").show()
```

## Referências

- Página dos dados abertos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis
- Página dos dados estatísticos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos
- Grupo `pb-abertos`: os mesmos dados em CSV, com UF e produtor (biodiesel até 2023).
