---
dataset:
  id: producao-el
  fonte: anp
  titulo: Produção de petróleo e gás natural por estado e localização
  resumo: Séries mensais, de 1997 em diante, de produção de petróleo, LGN e gás natural, e de queima e perda, consumo próprio e gás disponível, por unidade da federação e localização (terra ou mar).
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-estado-e-localizacao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; a ANP atualiza os arquivos até o último dia do mês subsequente ao de referência
  cobertura:
    inicio: 1997-01
    fim: em-curso
  unidade: 'um mês, uma unidade da federação e uma localização (terra ou mar): o volume produzido, queimado, consumido ou disponível; na série de LGN, um mês e uma unidade da federação'
  granularidade:
    espacial: unidade da federação (11 estados produtores) e grande região, com localização terra ou mar (menos no LGN)
    temporal: mês (`ANO` e `MÊS`)
  formato_bruto: seis CSV em UTF-8 com BOM, separados por ponto e vírgula, decimal em vírgula
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 10
  unidades_de_medida:
    PRODUÇÃO: m³ (petróleo, LGN) ou mil m³ (gás natural)
    QUEIMADO: mil m³
    CONSUMO: mil m³
    DISPONÍVEL: mil m³
  dados_pessoais: nenhum
  eras:
  - desde: '1997'
    mudanca: séries de petróleo, LGN e gás natural, em m³ (petróleo e LGN) e mil m³ (gás), desde janeiro de 1997
  - desde: '2000'
    mudanca: séries de queima e perda, consumo próprio e gás disponível, em mil m³, desde janeiro de 2000
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de petróleo e gás natural por estado e localização

## Resumo

Seis séries mensais da ANP, por unidade da federação e, exceto para o LGN, por localização (terra ou mar): produção de petróleo (m³), de LGN (m³) e de gás natural (mil m³), a partir de 1997; e queima e perda, consumo próprio na E&P e gás natural disponível (mil m³), a partir de 2000. Os dados saem do Boletim Mensal de Produção (BMP) das operadoras, conforme o Decreto nº 2.705/1998, e são atualizados até o último dia do mês seguinte ao de referência. Petróleo é óleo mais condensado, sem LGN; LGN é o líquido de gás natural (GLP e C5+) separado nas UPGNs, sem condensado.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/producao-el` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-estado-e-localizacao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; a ANP atualiza os arquivos até o último dia do mês subsequente ao de referência |
| Cobertura | 1997-01 a em-curso |
| Unidade (uma linha) | um mês, uma unidade da federação e uma localização (terra ou mar): o volume produzido, queimado, consumido ou disponível; na série de LGN, um mês e uma unidade da federação |
| Granularidade | espacial: unidade da federação (11 estados produtores) e grande região, com localização terra ou mar (menos no LGN); temporal: mês (`ANO` e `MÊS`) |
| Formato bruto | seis CSV em UTF-8 com BOM, separados por ponto e vírgula, decimal em vírgula |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 10 |
| Unidades de medida | `PRODUÇÃO`: m³ (petróleo, LGN) ou mil m³ (gás natural); `QUEIMADO`: mil m³; `CONSUMO`: mil m³; `DISPONÍVEL`: mil m³ |
| Dados pessoais | nenhum |
| Eras | 1997: séries de petróleo, LGN e gás natural, em m³ (petróleo e LGN) e mil m³ (gás), desde janeiro de 1997; 2000: séries de queima e perda, consumo próprio e gás disponível, em mil m³, desde janeiro de 2000 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Seis CSV em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ppgn-el/`: `producao-petroleo-m3.csv`, `producao-lgn-m3.csv`, `producao-gas-natural-1000m3.csv`, `queima-e-perda-gn-1000m3.csv`, `consumo-proprio-gn1000m3.csv` e `gn-disponivel-1000m3.csv`. Dados atualizados em 29/10/2026, segundo a página, e metadados em PDF para cada série (atualizados em 10/3/2026).
- Fonte do dado, segundo os metadados: ANP, Boletim Mensal de Produção (Decreto nº 2.705/1998); catálogo de origem dos dados estatísticos da ANP; responsável ANP/SDC (Superintendência de Defesa da Concorrência); contato sdc@anp.gov.br. Os arquivos contêm dados históricos desde 1997, diferentemente das planilhas estatísticas da ANP.
- **Série que o fetcher não coleta:** a página lista também a reinjeção de gás natural (2000 a 2026, mil m³; `reinjecao-gn-1000m3`, URL sem extensão), com metadado próprio, que não está no catálogo.
- No bruto: `producao-estado-localizacao/pel-<série>@AAAAMMDD.csv`, com o sufixo da data da coleta. Os seis arquivos estão inteiros na amostra.

## Conteúdo

- **Um valor por mês, UF e localização.** Cada série tem uma coluna de valor própria (`PRODUÇÃO`, `QUEIMADO`, `CONSUMO` ou `DISPONÍVEL`), e o conversor guarda uma tabela por série. Contagens de linhas na amostra e primeiro e último mês:

| Arquivo no lake | Série | Linhas | Período | Coluna de valor |
|---|---|---|---|---|
| `pel-petroleo` | produção de petróleo (m³) | 7.920 | 1997-01 a 2026-12 (veja Cuidados de uso) | `PRODUÇÃO` |
| `pel-lgn` | produção de LGN (m³), sem localização | 3.567 (357 por estado, em geral) | 1997-01 a 2026-09 | `PRODUÇÃO` |
| `pel-gas-natural` | produção de gás natural (mil m³) | 7.775 | 1997-01 a 2026-09 | `PRODUÇÃO` |
| `pel-queima-perda` | queima e perda de gás natural (mil m³) | 7.043 | 2000-01 a 2026-09 | `QUEIMADO` |
| `pel-consumo-proprio` | consumo próprio de gás natural na E&P (mil m³) | 7.034 | 2000-01 a 2026-09 | `CONSUMO` |
| `pel-gn-disponivel` | gás natural disponível (mil m³) | 7.049 | 2000-01 a 2026-09 | `DISPONÍVEL` |

- **Chave (conferida na amostra, por série).** `(ANO, MÊS, UNIDADE DA FEDERAÇÃO, LOCALIZAÇÃO)` é única em cinco séries e `(ANO, MÊS, UNIDADE DA FEDERAÇÃO)` na de LGN. Como as séries têm colunas diferentes, a chave do dataset fica vazia.
- **Estados.** São 11 unidades da federação na produção de petróleo: Alagoas, Amazonas, Bahia, Ceará, Espírito Santo, Maranhão, Paraná, Rio de Janeiro, Rio Grande do Norte, Sergipe e São Paulo; o LGN tem 10 (sem o Maranhão). O total de gás natural de 2025 na tabela (65.421.555 mil m³) é igual ao `Total do Ano` de 2025 da planilha nacional de gás do `ppg`.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `pel-consumo-proprio` (7); `pel-gas-natural` (7); `pel-gn-disponivel` (7); `pel-lgn` (6); `pel-petroleo` (7); `pel-queima-perda` (7) |

## Variáveis

As descrições vêm dos metadados em PDF da ANP de cada série ("Produção nacional de petróleo", "... de LGN", "... de gás natural", "Queima e perda de gás natural", "Consumo próprio de gás natural na E&P" e "Gás natural disponível"), que descrevem as mesmas seis colunas comuns e a coluna de valor de cada série.
A coluna *Arquivos* mostra as séries em que cada coluna aparece (`PRODUÇÃO` está em três, as demais colunas de valor, em uma só).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `ANO` | `ANO` | texto | Ano de referência. | — | — | `pel-consumo-proprio`, `pel-gas-natural`, `pel-gn-disponivel` e mais 3 |
| `MÊS` | `MÊS` | texto | Mês de referência, abreviado em maiúsculas (`JAN` a `DEZ`). | — | — | `pel-consumo-proprio`, `pel-gas-natural`, `pel-gn-disponivel` e mais 3 |
| `GRANDE REGIÃO` | `GRANDE REGIÃO` | texto | Grande região do Brasil, com o prefixo `REGIÃO ` (Norte, Nordeste, Sudeste ou Sul; não há produção nas demais). | — | — | `pel-consumo-proprio`, `pel-gas-natural`, `pel-gn-disponivel` e mais 3 |
| `UNIDADE DA FEDERAÇÃO` | `UNIDADE DA FEDERAÇÃO` | texto | Unidade da Federação (nome por extenso, em maiúsculas). | — | — | `pel-consumo-proprio`, `pel-gas-natural`, `pel-gn-disponivel` e mais 3 |
| `PRODUTO` | `PRODUTO` | texto | Nome do produto: `PETRÓLEO`, `LGN` ou `GÁS NATURAL`. | — | — | `pel-consumo-proprio`, `pel-gas-natural`, `pel-gn-disponivel` e mais 3 |
| `LOCALIZAÇÃO` | `LOCALIZAÇÃO` | texto | Localização da produção: `TERRA` ou `MAR` (ausente na tabela de LGN). | — | — | `pel-consumo-proprio`, `pel-gas-natural`, `pel-gn-disponivel` e mais 2 |
| `CONSUMO` | `CONSUMO` | texto | Volume de gás natural consumido na própria E&P no mês, em mil m³ (áreas de produção e UPGNs, segundo as notas do metadado). | — | — | `pel-consumo-proprio` |
| `PRODUÇÃO` | `PRODUÇÃO` | texto | Volume produzido no mês: em m³ para petróleo (`pel-petroleo`) e LGN (`pel-lgn`) e em mil m³ para gás natural (`pel-gas-natural`). | — | — | `pel-gas-natural`, `pel-lgn`, `pel-petroleo` |
| `DISPONÍVEL` | `DISPONÍVEL` | texto | Volume de gás natural disponível no mês, em mil m³; pode ser negativo (o metadado não descreve o cálculo). | — | — | `pel-gn-disponivel` |
| `QUEIMADO` | `QUEIMADO` | texto | Volume de gás natural queimado e/ou perdido no mês, em mil m³ (no metadado da ANP a coluna se chama `QUEIMA E PERDA`; no arquivo, `QUEIMADO`). | — | — | `pel-queima-perda` |

## No lake

- Dataset `anp/producao-el`, sem partições: um Parquet por série, `pel-petroleo.parquet`, `pel-lgn.parquet`, `pel-gas-natural.parquet`, `pel-queima-perda.parquet`, `pel-consumo-proprio.parquet` e `pel-gn-disponivel.parquet`.
- Todas as colunas são texto, inclusive `ANO` e os volumes (vírgula decimal, sem ponto de milhar nas amostras). Os nomes são os da fonte (maiúsculas e acentos), sem a marca de ordem de bytes.

## Cuidados de uso

- **Meses futuros com zero na série de petróleo.** `pel-petroleo` tem linhas para outubro a dezembro de 2026 (22 por mês, todas com `PRODUÇÃO` igual a `0`), embora o dado só vá até setembro; as outras cinco séries terminam em setembro de 2026. Zeros desses meses não são produção nula: descarte os meses posteriores ao último publicado.
- **Zero é frequente.** 2.447 das 7.920 linhas de petróleo valem `0` (inclusive os três meses acima, 66 linhas): estados e localizações sem produção em um mês trazem a linha, com zero.
- **Gás disponível pode ser negativo.** `pel-gn-disponivel` tem 683 linhas com valor negativo (por exemplo `-2,2737` em Bahia, mar, 2000-01), compatível com consumo, queima e reinjeção maiores que a produção, mas o metadado não descreve o cálculo.
- **Nome da coluna de queima.** O metadado fala em `QUEIMA E PERDA`, mas o arquivo traz `QUEIMADO`; o valor soma queima e perda.
- **Texto com vírgula decimal.** `PRODUÇÃO` é texto (`4030`, `137599,3333`); troque a vírgula por ponto antes do cast. Os meses vêm abreviados em maiúsculas (`JAN`...), não como número.
- **Unidades diferentes por série.** Petróleo e LGN em m³; gás natural, queima, consumo e disponível em mil m³ (`1000m3` no nome do arquivo). Volumes de gás referem-se a 20 °C e 1 atm, segundo a planilha nacional.
- **LGN sem localização.** `pel-lgn` não tem a coluna `LOCALIZAÇÃO` (6 colunas no lake, contra 7 nas demais séries); o LGN é separado nas UPGNs, e a ANP não o divide em terra e mar.
- **Dados pessoais.** Não há: dados agregados por estado.

## Exemplos

Produção de petróleo em 2025 por estado e localização, em milhões de m³ (a coluna é texto com vírgula decimal):

```python
import duckdb

duckdb.sql("""
    SELECT "UNIDADE DA FEDERAÇÃO" AS uf, "LOCALIZAÇÃO" AS localizacao,
           round(sum(replace("PRODUÇÃO", ',', '.')::DOUBLE) / 1e6, 2) AS milhoes_m3
    FROM read_parquet('lake/anp/producao-el/pel-petroleo.parquet')
    WHERE ANO = '2025'
    GROUP BY 1, 2
    HAVING sum(replace("PRODUÇÃO", ',', '.')::DOUBLE) > 0
    ORDER BY milhoes_m3 DESC
""").show()
```

## Referências

- Produção de petróleo e gás natural por estado e localização (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-estado-e-localizacao
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ppgn-el/metadados-producao-petroleo.pdf e os demais `metadados-*.pdf` da mesma pasta
