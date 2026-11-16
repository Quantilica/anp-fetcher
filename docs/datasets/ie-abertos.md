---
dataset:
  id: ie-abertos
  fonte: anp
  titulo: Importações e exportações de petróleo, gás natural, derivados e etanol (dados abertos)
  resumo: Volume e valor mensais de importação e exportação de petróleo, derivados e etanol e de importação de gás natural, de 2000 em diante.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; a página da ANP informa atualização até o último dia do mês seguinte ao de referência (arquivos atualizados em 29/10/2026 com dados até setembro de 2026)
  cobertura:
    inicio: 2000-01
    fim: 2026-09
  unidade: um produto numa operação comercial (importação ou exportação) num mês
  granularidade:
    espacial: Brasil (sem recorte por UF, porto ou país)
    temporal: mês (`ANO` e `MÊS`)
  formato_bruto: CSV com separador `;`, vírgula decimal, UTF-8 com BOM e fim de linha CRLF; quatro arquivos
  lake:
    estado: convertido
    particoes: []
    chave:
    - ANO
    - MÊS
    - PRODUTO
    - OPERAÇÃO COMERCIAL
    colunas: 8
  unidades_de_medida:
    IMPORTADO / EXPORTADO: m³
    DISPÊNDIO / RECEITA: US$ FOB
    IMPORTADO: mil m³
    DISPÊNDIO: US$ FOB
  dados_pessoais: nenhum
  eras:
  - desde: '2000'
    mudanca: petróleo, gás natural e derivados desde janeiro de 2000; o arquivo de etanol começa em janeiro de 2012
  - desde: '2006'
    mudanca: segundo a nota da planilha de dados estatísticos, a partir de novembro de 2006 a série de exportações de derivados passou a incluir `COMBUSTÍVEIS PARA AERONAVES` e `COMBUSTÍVEIS PARA NAVIOS`, e toda a série desde janeiro de 2000 foi revisada; no CSV os dois produtos têm linhas de exportação desde 2000
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Importações e exportações de petróleo, gás natural, derivados e etanol (dados abertos)

## Resumo

Séries mensais do comércio exterior brasileiro de petróleo, gás natural, derivados de petróleo e etanol, publicadas pela ANP em quatro arquivos CSV (petróleo, gás natural, derivados e etanol). Cada linha traz o volume importado ou exportado de um produto num mês e o dispêndio (importação) ou a receita (exportação) em US$ FOB. O gás natural só tem importação, em mil m³; as demais séries estão em m³. Os mesmos números aparecem, em forma de planilha com anos nas colunas, no grupo `ie` (dados estatísticos).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/ie-abertos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; a página da ANP informa atualização até o último dia do mês seguinte ao de referência (arquivos atualizados em 29/10/2026 com dados até setembro de 2026) |
| Cobertura | 2000-01 a 2026-09 |
| Unidade (uma linha) | um produto numa operação comercial (importação ou exportação) num mês |
| Granularidade | espacial: Brasil (sem recorte por UF, porto ou país); temporal: mês (`ANO` e `MÊS`) |
| Formato bruto | CSV com separador `;`, vírgula decimal, UTF-8 com BOM e fim de linha CRLF; quatro arquivos |
| Estado no lake | convertido |
| Partições | — |
| Chave | `ANO`, `MÊS`, `PRODUTO`, `OPERAÇÃO COMERCIAL` |
| Colunas | 8 |
| Unidades de medida | `IMPORTADO / EXPORTADO`: m³; `DISPÊNDIO / RECEITA`: US$ FOB; `IMPORTADO`: mil m³; `DISPÊNDIO`: US$ FOB |
| Dados pessoais | nenhum |
| Eras | 2000: petróleo, gás natural e derivados desde janeiro de 2000; o arquivo de etanol começa em janeiro de 2012; 2006: segundo a nota da planilha de dados estatísticos, a partir de novembro de 2006 a série de exportações de derivados passou a incluir `COMBUSTÍVEIS PARA AERONAVES` e `COMBUSTÍVEIS PARA NAVIOS`, e toda a série desde janeiro de 2000 foi revisada; no CSV os dois produtos têm linhas de exportação desde 2000 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa quatro CSV de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/`: `petroleo/importacoes-exportacoes-petroleo-2000-2025.csv`, `gn/importacao-gas-natural-2000-2025.csv`, `derivados/importacoes-exportacoes-derivados-2000-2025.csv` e `etanol/importacoes-exportacoes-etanol-2012-2025.csv`. O ano final do nome do arquivo está defasado: os quatro trazem dados até setembro de 2026 (conferido em 2026-11-15).
- Metadados em PDF (atualizados em 10/03/2026), um por arquivo: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/petroleo/metadados-importacao-exportacao-petroleo-1.pdf`, `.../gn/metadados-importacao-gas-natural-1.pdf`, `.../derivados/metadados-importacao-exportacao-derivados-1.pdf` e `.../etanol/metadados-importacao-exportacao-etanol-1.pdf`.
- Fonte do dado, segundo os metadados: Secretaria de Comércio Exterior (Ministério da Economia) para petróleo, derivados e etanol; ANP (Portaria nº 043, de 15/04/1998) para o gás natural. Órgão responsável: Superintendência de Defesa da Concorrência (ANP/SDC).
- Notas dos metadados: o petróleo inclui óleo e condensado e não inclui LGN (e inclui as importações de condensado das centrais petroquímicas); GLP inclui propano e butano; `OUTROS NÃO ENERGÉTICOS` inclui outras correntes; `SOLVENTE` reúne vários códigos NCM (hexano, aguarrás, benzeno, tolueno, xilenos e outros); as importações de gás natural começaram em julho de 1999 e as de GNL em novembro de 2008; os volumes de gás natural referem-se a 20 °C e 1 atm.

## Conteúdo

- **Quatro arquivos, uma estrutura.** O lake tem um Parquet por arquivo: `iea-petroleo` (642 linhas), `iea-gas-natural` (321), `iea-derivados` (9.630) e `iea-etanol` (708), num total de 11.301 linhas.
- **Petróleo.** `PRODUTO` = `PETRÓLEO`, com importação e exportação, de 2000-01 a 2026-09 (321 meses, 2 linhas por mês).
- **Gás natural.** `PRODUTO` = `GÁS NATURAL`, só `IMPORTAÇÃO`, de 2000-01 a 2026-09. É o único arquivo que usa as colunas `IMPORTADO` e `DISPÊNDIO` (e não `IMPORTADO / EXPORTADO` e `DISPÊNDIO / RECEITA`), e o volume está em mil m³, não em m³.
- **Derivados.** 16 produtos: `ASFALTO`, `COMBUSTÍVEIS PARA AERONAVES` e `COMBUSTÍVEIS PARA NAVIOS` (só exportação), `COQUE`, `GASOLINA A`, `GASOLINA DE AVIAÇÃO`, `GLP`, `LUBRIFICANTE`, `NAFTA`, `OUTROS NÃO ENERGÉTICOS`, `PARAFINA`, `QUEROSENE DE AVIAÇÃO`, `QUEROSENE ILUMINANTE`, `SOLVENTE`, `ÓLEO COMBUSTÍVEL` e `ÓLEO DIESEL`; 30 pares produto-operação, de 2000-01 a 2026-09, sempre completos (321 meses cada).
- **Etanol.** `ETANOL ANIDRO` e `ETANOL HIDRATADO`, importação e exportação, de 2012-01 a 2026-09 (177 meses, 4 linhas por mês).
- **Chave.** `ANO`, `MÊS`, `PRODUTO` e `OPERAÇÃO COMERCIAL` não se repetem nas 11.301 linhas dos quatro arquivos juntos.
- **Zeros.** 1.798 linhas têm volume zero (o produto não foi movimentado no mês) e 4 linhas de derivados têm volume positivo e valor zero.

## Variáveis

As descrições vêm dos metadados da ANP (um PDF por arquivo). `ANO` e `MÊS` são texto; `MÊS` vem abreviado (`JAN` a `DEZ`). Os volumes e valores são decimais (a vírgula decimal do CSV é convertida).
`IMPORTADO` e `DISPÊNDIO` existem só no arquivo de gás natural; as outras colunas numéricas, só nos outros três arquivos (por isso ficam vazias nas linhas do arquivo que não as usa).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `ANO` | `ANO` | texto | Ano de referência, com quatro dígitos | — | — | `iea-derivados`, `iea-etanol`, `iea-gas-natural` e mais 1 |
| `MÊS` | `MÊS` | texto | Mês de referência, abreviado em três letras maiúsculas | JAN = janeiro; FEV = fevereiro; MAR = março; ABR = abril; MAI = maio; JUN = junho; JUL = julho; AGO = agosto; SET = setembro; OUT = outubro; NOV = novembro; DEZ = dezembro | — | `iea-derivados`, `iea-etanol`, `iea-gas-natural` e mais 1 |
| `PRODUTO` | `PRODUTO` | texto | Nome do produto: petróleo, gás natural, um dos 16 derivados de petróleo (por exemplo `ÓLEO DIESEL`, `GLP`, `NAFTA`) ou o tipo de etanol (`ETANOL ANIDRO`, `ETANOL HIDRATADO`), conforme o arquivo | — | — | `iea-derivados`, `iea-etanol`, `iea-gas-natural` e mais 1 |
| `OPERAÇÃO COMERCIAL` | `OPERAÇÃO COMERCIAL` | texto | Tipo de operação comercial | IMPORTAÇÃO = importação; EXPORTAÇÃO = exportação | — | `iea-derivados`, `iea-etanol`, `iea-gas-natural` e mais 1 |
| `IMPORTADO / EXPORTADO` | `IMPORTADO / EXPORTADO` | decimal | Volume importado ou exportado no mês, em m³ (petróleo, derivados e etanol) | — | — | `iea-derivados`, `iea-etanol`, `iea-petroleo` |
| `DISPÊNDIO / RECEITA` | `DISPÊNDIO / RECEITA` | decimal | Dispêndio (importação) ou receita (exportação) do mês, em US$ FOB (valor corrente, sem frete) | — | — | `iea-derivados`, `iea-etanol`, `iea-petroleo` |
| `IMPORTADO` | `IMPORTADO` | decimal | Volume de gás natural importado no mês, em mil m³ (1.000 m³); inclui o GNL em volume na forma gasosa | — | — | `iea-gas-natural` |
| `DISPÊNDIO` | `DISPÊNDIO` | decimal | Dispêndio com a importação de gás natural no mês, em US$ FOB | — | — | `iea-gas-natural` |

## No lake

- Dataset `anp/ie-abertos`, sem partições; um Parquet por arquivo da fonte (`iea-petroleo.parquet`, `iea-gas-natural.parquet`, `iea-derivados.parquet`, `iea-etanol.parquet`).
- O lake guarda o conteúdo como está na fonte: sem somar meses, sem converter unidades.

## Cuidados de uso

- **Unidades diferentes no mesmo dataset.** Petróleo, derivados e etanol estão em m³; o gás natural está em mil m³. Não some `IMPORTADO / EXPORTADO` com `IMPORTADO` sem converter.
- **Nome do arquivo defasado.** A URL dos arquivos diz `2000-2025` (e `2012-2025` no etanol), mas o conteúdo vai até setembro de 2026; use `ANO` e `MÊS`, não o nome do arquivo, para saber a cobertura.
- **Mês abreviado.** Para ordenar no tempo, converta `MÊS` (`JAN` a `DEZ`) em número.
- **Valores correntes.** `DISPÊNDIO / RECEITA` é em dólares correntes (US$ FOB), sem deflacionar.
- **Dado preliminar.** Os últimos meses podem ser revistos nas atualizações seguintes; a ANP não marca quais.
- **Dados pessoais.** Nenhum: são totais nacionais por produto.

## Exemplos

Volume (m³) e dispêndio (US$ FOB) da importação anual de óleo diesel:

```python
import duckdb

duckdb.sql("""
    SELECT ANO,
           sum("IMPORTADO / EXPORTADO") AS m3,
           sum("DISPÊNDIO / RECEITA") AS usd_fob
    FROM read_parquet('lake/anp/ie-abertos/*.parquet', union_by_name = true)
    WHERE PRODUTO = 'ÓLEO DIESEL' AND "OPERAÇÃO COMERCIAL" = 'IMPORTAÇÃO'
    GROUP BY ANO
    ORDER BY ANO
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/petroleo/metadados-importacao-exportacao-petroleo-1.pdf, https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/gn/metadados-importacao-gas-natural-1.pdf, https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/derivados/metadados-importacao-exportacao-derivados-1.pdf e https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/etanol/metadados-importacao-exportacao-etanol-1.pdf
- Grupo `ie`: os mesmos dados em planilhas dos dados estatísticos (anos nas colunas).
