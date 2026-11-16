---
dataset:
  id: pads-concluidos
  fonte: anp
  titulo: PADs concluídos na fase de exploração
  resumo: 'Relação mensal acumulada dos planos de avaliação de descobertas (PADs) concluídos: bloco, bacia, operador, rodada, datas e se houve declaração de comercialidade.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (metadados da ANP); o lake guarda uma fotografia por mês
  cobertura:
    inicio: 2023-02
    fim: em-curso
  unidade: um PAD concluído, acumulado até o mês do arquivo (uma linha por PAD e área em cada arquivo mensal)
  granularidade:
    espacial: bloco e bacia; ambiente e grupo de bacias a partir de 2023-12; sem coordenadas
    temporal: mês do arquivo (fotografia); início e término são datas do PAD
  formato_bruto: CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 13
  dados_pessoais:
  - coluna: OPERADOR
    categoria: nome de empresas (pessoas jurídicas) operadoras
  eras:
  - desde: 2023-02
    mudanca: 9 colunas, com `CAMPO/ÁREA DE DESENVOLVIMENTO` (sem espaço depois da barra); datas como `aaaa-mm-dd hh:mm:ss` em 2023-02; `DECLAROU COMERCIALIDADE` com `Nao` sem acento
  - desde: 2023-12
    mudanca: '11 colunas: entram `BACIAS AGRUPADAS` e `AMBIENTE`; a coluna passa a se chamar `ÁREA DE DESENVOLVIMENTO`; `Não` com acento; a amostra não tem os meses entre 2023-03 e 2023-12'
  - desde: 2024-10
    mudanca: '12 colunas: entra `REGIME CONTRATUAL`; a amostra não tem os meses entre 2023-12 e 2024-10'
  - desde: 2026-07
    mudanca: as datas passam a vir com hora, `dd/mm/aaaa hh:mm`, e o arquivo é UTF-8 com BOM
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# PADs concluídos na fase de exploração

## Resumo

Fotografia mensal acumulada dos planos de avaliação de descobertas (PADs) concluídos na fase de exploração. Cada linha traz o PAD, o bloco, a bacia, o operador, a rodada, as datas de início e término efetivos, se o PAD terminou com declaração de comercialidade e, quando houve, o campo ou a área de desenvolvimento resultante. É o relatório «Planos de Avaliação de Descobertas (PADs) Concluídos» do painel dinâmico da fase de exploração da ANP.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pads-concluidos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (metadados da ANP); o lake guarda uma fotografia por mês |
| Cobertura | 2023-02 a em-curso |
| Unidade (uma linha) | um PAD concluído, acumulado até o mês do arquivo (uma linha por PAD e área em cada arquivo mensal) |
| Granularidade | espacial: bloco e bacia; ambiente e grupo de bacias a partir de 2023-12; sem coordenadas; temporal: mês do arquivo (fotografia); início e término são datas do PAD |
| Formato bruto | CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 13 |
| Unidades de medida | — |
| Dados pessoais | `OPERADOR` (nome de empresas (pessoas jurídicas) operadoras) |
| Eras | 2023-02: 9 colunas, com `CAMPO/ÁREA DE DESENVOLVIMENTO` (sem espaço depois da barra); datas como `aaaa-mm-dd hh:mm:ss` em 2023-02; `DECLAROU COMERCIALIDADE` com `Nao` sem acento; 2023-12: 11 colunas: entram `BACIAS AGRUPADAS` e `AMBIENTE`; a coluna passa a se chamar `ÁREA DE DESENVOLVIMENTO`; `Não` com acento; a amostra não tem os meses entre 2023-03 e 2023-12; 2024-10: 12 colunas: entra `REGIME CONTRATUAL`; a amostra não tem os meses entre 2023-12 e 2024-10; 2026-07: as datas passam a vir com hora, `dd/mm/aaaa hh:mm`, e o arquivo é UTF-8 com BOM |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Exploração (SEP); os dados vêm do SIGEP (Sistema de Informações Gerenciais de Exploração e Produção) e são o extrato do relatório «Planos de Avaliação de Descobertas (PADs) Concluídos» do painel dinâmico da fase de exploração (metadados da ANP). A página oficial publica um CSV por mês, em ponto e vírgula.
- **Catálogo do fetcher:** 41 arquivos mensais, de 2023-02 a 2026-07 (conferido em 2026-11-15). A página oficial lista arquivos até out/2026 e o catálogo do fetcher vai só até jul/2026; os meses seguintes entram quando o catálogo for atualizado.
- O catálogo não tem o arquivo de set/2025.
- **Codificação:** os arquivos variam, e os da amostra são ISO-8859-1 ou UTF-8 com BOM; o conversor lê os dois (conferido na amostra: sem texto corrompido nas colunas).
- **Cada arquivo é uma fotografia do mês, não um incremento:** o arquivo de um mês repete as linhas dos meses anteriores que continuam valendo e acrescenta ou retira as que mudaram.

## Conteúdo

- **O que é uma linha:** um PAD concluído, acumulado: o arquivo cresce a cada mês (387 linhas em 2023-02 e 412 em 2026-07 na amostra, sem contar as 2 linhas de rodapé dos arquivos que as têm).
- **`CÓDIGO DO PAD` não é único:** 2026-07 tem 412 linhas e 381 códigos distintos, porque um PAD pode ter mais de uma área de desenvolvimento.
- **Declaração de comercialidade:** em 2026-07, 269 linhas `Sim` e 143 `Não` (na amostra, `Nao` sem acento em 2023-02 e 2023-03).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `2023-02` (9); `2023-03` (9); `2023-12` (11) |
| 2024 | `2024-10` (12) |
| 2025 | `2025-08` (12) |
| 2026 | `2026-07` (12) |

## Variáveis

As descrições vêm dos metadados da ANP (documento «PADs concluídos na fase de exploração», seção Colunas). O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CÓDIGO DO PAD` | `CÓDIGO DO PAD` | texto | Código do PAD (Plano de Avaliação de Descobertas), que corresponde ao nome da acumulação principal da área do PAD | — | todo |
| `BLOCO` | `BLOCO` | texto | Nome do bloco exploratório: parte de uma bacia sedimentar, de superfície poligonal, onde se fazem atividades de exploração ou produção de petróleo e gás natural | — | todo |
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar onde está o bloco | — | todo |
| `OPERADOR` | `OPERADOR` | texto | Empresa designada pelos consorciados para conduzir as operações na área sob contrato (nome fantasia) | — | todo |
| `RODADA` | `RODADA` | texto | Rodada de licitação (ou ciclo de oferta permanente) de origem do bloco; pode listar mais de uma, separadas por vírgula, quando a linha reúne blocos de rodadas diferentes | — | todo |
| `INÍCIO EFETIVO` | `INÍCIO EFETIVO` | texto | Data do início efetivo do PAD | — | todo |
| `TÉRMINO EFETIVO` | `TÉRMINO EFETIVO` | texto | Data do término efetivo do PAD | — | todo |
| `DECLAROU COMERCIALIDADE` | `DECLAROU COMERCIALIDADE` | texto | Indica se houve declaração de comercialidade ao fim do PAD: `Sim` ou `Não` (na amostra, `Nao` sem acento em 2023-02 e 2023-03) | — | todo |
| `CAMPO/ÁREA DE DESENVOLVIMENTO` | `CAMPO/ÁREA DE DESENVOLVIMENTO` | texto | Nome do campo ou da área de desenvolvimento (nome da coluna na versão mais antiga do arquivo; equivale a ÁREA DE DESENVOLVIMENTO) | — | 2023-02 a 2023-03 |
| `BACIAS AGRUPADAS` | `BACIAS AGRUPADAS` | texto | Agrupamento das bacias sedimentares: Margem Equatorial, Margem Leste, Maduras (terrestres) e Nova Fronteira (terrestres); o dicionário da ANP lista as bacias de cada grupo | — | 2023-12 a 2026-07 |
| `AMBIENTE` | `AMBIENTE` | texto | Localização do bloco por ambiente: terra ou mar (a caixa do texto varia entre os arquivos: TERRA, Terra, MAR, Mar) | — | 2023-12 a 2026-07 |
| `ÁREA DE DESENVOLVIMENTO` | `ÁREA DE DESENVOLVIMENTO` | texto | Nome da área de desenvolvimento: área produtora de petróleo ou gás natural, de um ou mais reservatórios, a profundidades variáveis | — | 2023-12 a 2026-07 |
| `REGIME CONTRATUAL` | `REGIME CONTRATUAL` | texto | Modalidade do regime contratual da área: Concessão ou Partilha | — | 2024-10 a 2026-07 |

## No lake

- Dataset `anp/pads-concluidos`, particionado por `ano` e `mes` (mês do arquivo no catálogo); um Parquet por arquivo, `pads-concluidos_AAAA-MM.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (maiúsculas, acentos e espaços). Datas, números e percentuais ficam como vêm no CSV (vírgula decimal, datas dd/mm/aaaa).
- O conversor não descarta as linhas em branco nem a linha de rodapé do painel (ver Cuidados).

## Cuidados de uso

- **Empilhar meses duplica linhas.** Cada arquivo repete o estado completo do mês; para a situação atual use só a partição `ano`/`mes` mais recente, e para uma série compare os meses entre si. Não some linhas de meses diferentes.
- **Linhas de rodapé e linhas vazias viram dados.** Os arquivos do painel trazem, depois dos dados, uma linha em branco e uma linha de texto com os filtros do painel (por exemplo, «Nenhum filtro aplicado» ou «Filtros aplicados: ...»), que o conversor grava como duas linhas quase totalmente nulas, uma delas com o texto na primeira coluna. Na amostra, os rodapés estão nos arquivos de 2023-03, 2023-12, 2024-10 e 2025-08 e não estão nos de 2023-02 e 2026-07. Descarte as linhas em que a coluna de identificação seja nula ou comece por «Filtro»/«Nenhum filtro».
- **Formato de data muda entre meses.** O mesmo campo aparece como `dd/mm/aaaa`, como `aaaa-mm-dd hh:mm:ss` e como `dd/mm/aaaa hh:mm`, conforme o arquivo (ver as eras). Normalize antes de converter para data.
- **Colunas entram e saem com o tempo** (ver as eras); ao empilhar meses use `union_by_name` e espere nulos nas colunas novas.
- **`Sim`/`Não`/`Nao`.** O valor negativo muda de grafia entre as eras; normalize antes de contar.
- **`ÁREA DE DESENVOLVIMENTO` vazia** quando não houve declaração de comercialidade (cerca de um terço das linhas), e por isso não há campo ligado.
- **Dois nomes de coluna para o mesmo campo** (`CAMPO/ÁREA DE DESENVOLVIMENTO` e `ÁREA DE DESENVOLVIMENTO`); junte com `coalesce` ao empilhar meses.

## Exemplos

PADs concluídos com e sem declaração de comercialidade na fotografia de 2026-07:

```python
import duckdb

duckdb.sql("""
    SELECT "DECLAROU COMERCIALIDADE" AS declarou, count(*) AS pads
    FROM read_parquet('lake/anp/pads-concluidos/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '07' AND "BACIA" IS NOT NULL
    GROUP BY ALL
    ORDER BY pads DESC
""").show()
```

## Referências

- Dados abertos da ANP, Fase de Exploração (PADs Concluídos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
- Metadados «PADs Concluídos» (ANP/SEP): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/painel-dinamico-da-fase-de-exploracao/pads-concluidos/metadado-pads-concluidos.pdf
