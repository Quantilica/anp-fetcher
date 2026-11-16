---
dataset:
  id: pp-abertos
  fonte: anp
  titulo: Processamento de petróleo e produção de derivados (dados abertos)
  resumo: Petróleo processado e derivados produzidos por mês, por refinaria, central petroquímica, unidade de xisto e outros produtores, de 1990 em diante, em m³.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/processamento-de-petroleo-e-producao-de-derivados
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; a página informa atualização até o último dia do mês seguinte (arquivos atualizados em 29/10/2026, com dados até setembro de 2026)
  cobertura:
    inicio: 1990-01
    fim: 2026-09
  unidade: uma refinaria (ou central petroquímica, unidade de xisto ou outro produtor) e um produto ou matéria-prima num mês
  granularidade:
    espacial: refinaria ou unidade produtora, com UF (exceto no arquivo de outros produtores)
    temporal: mês (`ANO` e `MÊS`)
  formato_bruto: CSV com separador `;`, vírgula decimal e UTF-8 com BOM; seis arquivos
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 10
  unidades_de_medida:
    PRODUÇÃO: m³ (mil m³ no arquivo de gás combustível)
    PROCESSADO: m³
  dados_pessoais:
  - coluna: REFINARIA
    categoria: nome de refinaria ou empresa (pessoa jurídica)
  - coluna: PRODUTOR
    categoria: nome de unidade produtora (pessoa jurídica)
  eras:
  - desde: '1990'
    mudanca: processamento de petróleo e derivados por refinaria desde janeiro de 1990
  - desde: '2000'
    mudanca: gás combustível desde janeiro de 2000; nos arquivos de processamento e de derivados, a refinaria da Bahia aparece como `RLAM` até 1999 e como `REFMAT` de 2000 em diante, e a do Rio Grande do Norte como `RPCC` até 1999 e `3R POTIGUAR` de 2000 em diante
  - desde: '2001'
    mudanca: centrais petroquímicas e xisto desde 2001; outros produtores desde 2003
  - desde: '2021'
    mudanca: segundo os metadados, até 2020 a fonte eram as próprias empresas (Manguinhos, Petrobras, Riograndense, Univen e Dax Oil; só a Petrobras no gás combustível e no xisto) e, a partir de 2021, a ANP conforme a Resolução ANP nº 729/2018
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Processamento de petróleo e produção de derivados (dados abertos)

## Resumo

Seis arquivos CSV da ANP sobre o refino no Brasil: o petróleo processado por refinaria e tipo de matéria-prima (nacional, importado e outras cargas), a produção de derivados por refinaria e produto, a de gás combustível por refinaria, e a de derivados das centrais petroquímicas, das unidades de xisto e de outros produtores. Todos são mensais, em m³ (mil m³ no gás combustível), e todos vão até setembro de 2026. Os totais mensais, em planilha, estão no grupo `pp`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pp-abertos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/processamento-de-petroleo-e-producao-de-derivados |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; a página informa atualização até o último dia do mês seguinte (arquivos atualizados em 29/10/2026, com dados até setembro de 2026) |
| Cobertura | 1990-01 a 2026-09 |
| Unidade (uma linha) | uma refinaria (ou central petroquímica, unidade de xisto ou outro produtor) e um produto ou matéria-prima num mês |
| Granularidade | espacial: refinaria ou unidade produtora, com UF (exceto no arquivo de outros produtores); temporal: mês (`ANO` e `MÊS`) |
| Formato bruto | CSV com separador `;`, vírgula decimal e UTF-8 com BOM; seis arquivos |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 10 |
| Unidades de medida | `PRODUÇÃO`: m³ (mil m³ no arquivo de gás combustível); `PROCESSADO`: m³ |
| Dados pessoais | `REFINARIA` (nome de refinaria ou empresa (pessoa jurídica)); `PRODUTOR` (nome de unidade produtora (pessoa jurídica)) |
| Eras | 1990: processamento de petróleo e derivados por refinaria desde janeiro de 1990; 2000: gás combustível desde janeiro de 2000; nos arquivos de processamento e de derivados, a refinaria da Bahia aparece como `RLAM` até 1999 e como `REFMAT` de 2000 em diante, e a do Rio Grande do Norte como `RPCC` até 1999 e `3R POTIGUAR` de 2000 em diante; 2001: centrais petroquímicas e xisto desde 2001; outros produtores desde 2003; 2021: segundo os metadados, até 2020 a fonte eram as próprias empresas (Manguinhos, Petrobras, Riograndense, Univen e Dax Oil; só a Petrobras no gás combustível e no xisto) e, a partir de 2021, a ANP conforme a Resolução ANP nº 729/2018 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa seis CSV de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pppd/`: `processamento-petroleo-m3-1990-2025.csv`, `producao-derivados-petroleo-por-refinaria-m3-1990-2025.csv`, `producao-gas-combustivel-1000m3-2000-2025.csv`, `producao-derivados-centrais-petroquimicas-m3-2001-2025.csv`, `producao-derivados-xisto-m3-2001-2025.csv` e `producao-derivados-outros-produtores-m3-2001-2026.csv`. O ano final dos nomes está defasado: todos têm dados até setembro de 2026 (conferido em 2026-11-15).
- Metadados em PDF, um por arquivo (todos em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pppd/`, atualizados em 10/03/2026): `metadados-processamento-petroleo.pdf`, `metadados-producao-derivados-petroleo-por-refinaria.pdf`, `metadados-producao-gas-combustivel.pdf`, `metadados-producao-derivados-centrais-petroquimicas.pdf`, `metadados-producao-derivados-xisto.pdf` e `metadados-producao-derivados-por-outros-produtores.pdf`.
- Órgão responsável: Superintendência de Defesa da Concorrência (ANP/SDC). Notas dos metadados: petróleo nacional e importado incluem condensado; `OUTRAS CARGAS` incluem resíduos de petróleo, de terminais e de derivados reprocessados; as quantidades negativas indicam que a quantidade produzida foi inferior à transferida para compor outros derivados; GLP inclui a produção das UPGNs de LUBNOR, REDUC I e II, Catu e Candeias; coque inclui o energético e o não energético; `OUTROS NÃO ENERGÉTICOS` inclui diluentes, resíduos não energéticos e GLP não energético.
- Segundo a nota das planilhas de totais, em 01/10/2021 a operação da Refinaria Landulpho Alves (RLAM) passou da Petrobras para a Refinaria de Mataripe S/A.

## Conteúdo

- **Seis arquivos, seis recortes.** Cada arquivo do lake tem seu período, sua unidade e suas colunas de recorte (conferidos na amostra de 2026-11-15):

| Arquivo no lake (`pp-a-…`) | Conteúdo | Período | Unidade | Linhas |
|---|---|---|---|---|
| `processamento-m3` | petróleo processado por refinaria e matéria-prima (`PROCESSADO`) | 1990-01 a 2026-09 | m³ | 23.420 |
| `derivados-refinaria` | derivados por refinaria e produto (15 produtos) | 1990-01 a 2026-09 | m³ | 115.069 |
| `gas-combustivel` | gás combustível por refinaria | 2000-01 a 2026-09 | mil m³ | 4.460 |
| `petroquimica` | derivados por central petroquímica (3 centrais da Braskem) e produto (3 produtos) | 2001-01 a 2026-09 | m³ | 2.781 |
| `xisto` | derivados de xisto (`SIX`, Paraná) por produto (5 produtos) | 2001-01 a 2026-09 | m³ | 1.545 |
| `outros-produtores` | derivados de outros produtores (6 produtores, sem coluna de UF) por produto (3 produtos) | 2003-01 a 2026-09 | m³ | 5.116 |

- **Produtos e refinarias.** O arquivo de derivados por refinaria tem 21 refinarias em 10 UFs; o de processamento, 21 também (a grafia muda: veja Cuidados de uso). O de outros produtores não tem coluna de UF, embora o metadado a liste.
- **Matéria-prima.** Em 2024, `PETRÓLEO NACIONAL` foi 99,79 milhões de m³, `PETRÓLEO IMPORTADO`, 13,97 milhões e `OUTRAS CARGAS`, 1,99 milhão (soma 115.743.524 m³, praticamente igual à da planilha de totais do grupo `pp`, 115.743.517 m³: diferença de cerca de 6,5 m³).
- **Zeros.** Há muitas linhas com produção zero (65.747 de 115.069 em derivados por refinaria, porque as refinarias aparecem com produtos que não fabricam; 4.659 de 5.116 em outros produtores).
- **Chave.** `ANO`, `MÊS`, `REFINARIA` e `MATÉRIA PRIMA` não se repetem em `processamento-m3`; `ANO`, `MÊS`, central e produto não se repetem em `petroquimica`; `ANO`, `MÊS` e refinaria não se repetem em `gas-combustivel`; `ANO`, `MÊS`, `PRODUTOR` e `PRODUTO` não se repetem em `outros-produtores`. Em `derivados-refinaria`, 12 linhas repetem a chave (`SSOIL`, 2008; veja Cuidados de uso). Como as colunas diferem, a chave do conjunto não é declarada.

## Variáveis

As descrições vêm dos metadados da ANP (um PDF por arquivo). `ANO` e `MÊS` são texto; os volumes são decimais (a vírgula decimal é convertida). `PRODUÇÃO` e `PROCESSADO` são colunas diferentes de arquivos diferentes (`PROCESSADO` só no de processamento).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `ANO` | `ANO` | texto | Ano de referência, com quatro dígitos | — | — | `pp-a-derivados-refinaria`, `pp-a-gas-combustivel`, `pp-a-outros-produtores` e mais 3 |
| `MÊS` | `MÊS` | texto | Mês de referência, abreviado em três letras maiúsculas | JAN = janeiro; FEV = fevereiro; MAR = março; ABR = abril; MAI = maio; JUN = junho; JUL = julho; AGO = agosto; SET = setembro; OUT = outubro; NOV = novembro; DEZ = dezembro | — | `pp-a-derivados-refinaria`, `pp-a-gas-combustivel`, `pp-a-outros-produtores` e mais 3 |
| `UNIDADE DA FEDERAÇÃO` | `UNIDADE DA FEDERAÇÃO` | texto | Nome da unidade da federação onde fica a refinaria, central petroquímica ou unidade produtora (por exemplo `RIO DE JANEIRO`, `SÃO PAULO`), em maiúsculas | — | — | `pp-a-derivados-refinaria`, `pp-a-gas-combustivel`, `pp-a-petroquimica` e mais 2 |
| `REFINARIA` | `REFINARIA` | texto | Nome ou sigla da refinaria (por exemplo `REDUC`, `REPLAN`, `RNEST`, `MANGUINHOS`, `DAX OIL`); a grafia de algumas refinarias muda entre arquivos e ao longo dos anos (veja Cuidados de uso) | — | — | `pp-a-derivados-refinaria`, `pp-a-gas-combustivel`, `pp-a-processamento-m3` |
| `PRODUTO` | `PRODUTO` | texto | Nome do produto: no arquivo de derivados por refinaria, um de 15 produtos (`ASFALTO`, `COQUE`, `GASOLINA A`, `GASOLINA DE AVIAÇÃO`, `GLP`, `LUBRIFICANTE`, `NAFTA`, `OUTROS ENERGÉTICOS`, `OUTROS NÃO ENERGÉTICOS`, `PARAFINA`, `QUEROSENE DE AVIAÇÃO`, `QUEROSENE ILUMINANTE`, `SOLVENTE`, `ÓLEO COMBUSTÍVEL`, `ÓLEO DIESEL`); `GAS COMBUSTIVEL` no de gás combustível; `GASOLINA A`, `GLP` e `ÓLEO DIESEL` nas centrais petroquímicas; cinco produtos no xisto (`DIESEL`, `GLP`, `NAFTA`, `OUTROS NÃO ENERGÉTICOS`, `ÓLEO COMBUSTÍVEL`); `GASOLINA A`, `SOLVENTE` e `ÓLEO DIESEL` nos outros produtores | — | — | `pp-a-derivados-refinaria`, `pp-a-gas-combustivel`, `pp-a-outros-produtores` e mais 2 |
| `PRODUÇÃO` | `PRODUÇÃO` | decimal | Volume produzido no mês: em m³ (derivados, centrais petroquímicas, xisto e outros produtores) ou em mil m³ (gás combustível); pode ser negativo (veja Cuidados de uso) | — | — | `pp-a-derivados-refinaria`, `pp-a-gas-combustivel`, `pp-a-outros-produtores` e mais 2 |
| `PRODUTOR` | `PRODUTOR` | texto | Nome da unidade produtora: `SIX` (unidade produtora de derivados de xisto, no Paraná) no arquivo de xisto; `CAPIXABA`, `COPAPE`, `CPB`, `DECAL`, `NEOVG` e `NORQUIMA` no de outros produtores | — | — | `pp-a-outros-produtores`, `pp-a-xisto` |
| `CENTRAL PETROQUÍMICA` | `CENTRAL PETROQUÍMICA` | texto | Nome da central petroquímica | BRASKEM - BA = Braskem, Bahia; BRASKEM - RS = Braskem, Rio Grande do Sul; BRASKEM - SP = Braskem, São Paulo | — | `pp-a-petroquimica` |
| `MATÉRIA PRIMA` | `MATÉRIA PRIMA` | texto | Tipo de matéria-prima processada | PETRÓLEO NACIONAL = petróleo e condensado nacionais; PETRÓLEO IMPORTADO = petróleo e condensado importados; OUTRAS CARGAS = resíduos de petróleo, de terminais e de derivados reprocessados nas unidades de destilação | — | `pp-a-processamento-m3` |
| `PROCESSADO` | `PROCESSADO` | decimal | Volume de petróleo refinado (processado) no mês, em m³ | — | — | `pp-a-processamento-m3` |

## No lake

- Dataset `anp/pp-abertos`, sem partições; um Parquet por arquivo da fonte (`pp-a-processamento-m3.parquet`, `pp-a-derivados-refinaria.parquet`, `pp-a-gas-combustivel.parquet`, `pp-a-petroquimica.parquet`, `pp-a-xisto.parquet`, `pp-a-outros-produtores.parquet`).
- O lake guarda o conteúdo como está na fonte: sem unificar nomes de refinaria nem converter o mil m³ do gás combustível.

## Cuidados de uso

- **Unidade do gás combustível.** `PRODUÇÃO` está em mil m³ em `pp-a-gas-combustivel` e em m³ nos demais; o metadado ainda diz que «os valores estão expressos em metros cúbicos de gás». Não some com os derivados líquidos.
- **Nomes de refinaria inconsistentes.** A refinaria potiguar aparece como `RPCC` (1990–1999), `3R POTIGUAR (ex-RPCC)` (2000 em diante) em `processamento-m3` e `3R POTIGUAR (ex-3R POTIGUAR (ex-RPCC))` em `derivados-refinaria`; a da Bahia, como `RLAM` (1990–1999), `REFMAT` (2000 em diante) ou `RLAM (ATUALMENTE MATARIPE)` em `gas-combustivel`. Para seguir uma refinaria no tempo, mapeie os nomes.
- **UF inconsistente e linhas repetidas.** Em `derivados-refinaria`, as 12 linhas de querosene de aviação de `REFAP` em 2001 trazem a UF `SÃO PAULO`, e as outras 6.483 linhas da `REFAP`, `RIO GRANDE DO SUL`; e `SSOIL` / `GASOLINA DE AVIAÇÃO` aparece duas vezes em cada mês de 2008 (as duas com produção zero), o que repete a chave 12 vezes.
- **Valores negativos e zeros.** Os metadados avisam que quantidades negativas existem por transferência para outros derivados; zero não é lacuna, é produto não produzido no mês.
- **Arquivos defasados no nome.** Os nomes dizem `2025`, mas os dados vão até setembro de 2026.
- **Dados preliminares.** Os últimos meses podem ser revistos pela ANP.
- **Dados pessoais.** Nenhum: refinarias e unidades produtoras são pessoas jurídicas e os dados são agregados por unidade.

## Exemplos

Produção anual de óleo diesel (m³) por refinaria nos três últimos anos completos:

```python
import duckdb

duckdb.sql("""
    SELECT REFINARIA, ANO, sum("PRODUÇÃO") AS m3
    FROM read_parquet('lake/anp/pp-abertos/pp-a-derivados-refinaria.parquet')
    WHERE PRODUTO = 'ÓLEO DIESEL' AND ANO IN ('2023', '2024', '2025')
    GROUP BY ALL
    HAVING sum("PRODUÇÃO") > 0
    ORDER BY ANO, m3 DESC
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/processamento-de-petroleo-e-producao-de-derivados
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pppd/metadados-processamento-petroleo.pdf e os cinco demais em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pppd/`
- Grupo `pp`: totais mensais em planilha (dados estatísticos).
