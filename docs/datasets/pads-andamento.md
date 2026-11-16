---
dataset:
  id: pads-andamento
  fonte: anp
  titulo: PADs em andamento na fase de exploração
  resumo: 'Relação mensal dos planos de avaliação de descobertas (PADs) em andamento: bloco, bacia, operador, rodada, situação, início efetivo e término previsto.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (metadados da ANP); o lake guarda uma fotografia por mês
  cobertura:
    inicio: 2023-02
    fim: em-curso
  unidade: um PAD em andamento no mês de referência (uma linha por PAD em cada arquivo mensal)
  granularidade:
    espacial: bloco e bacia; ambiente e grupo de bacias a partir de 2024-01; sem coordenadas
    temporal: mês do arquivo (fotografia); início e término são datas do PAD
  formato_bruto: CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave:
    - ano
    - mes
    - CÓDIGO DO PAD
    colunas: 12
  dados_pessoais:
  - coluna: OPERADOR
    categoria: nome de empresas (pessoas jurídicas) operadoras e contratadas
  - coluna: CONTRATADOS
    categoria: nome de empresas (pessoas jurídicas) operadoras e contratadas
  eras:
  - desde: 2023-02
    mudanca: '8 colunas: `CÓDIGO DO PAD`, `BLOCO`, `BACIA`, `OPERADOR`, `RODADA`, `SITUAÇÃO`, `INÍCIO EFETIVO`, `TÉRMINO PREVISTO`; o arquivo de 2023-02 traz as datas como `aaaa-mm-dd hh:mm:ss`'
  - desde: 2024-01
    mudanca: '11 colunas: entram `BACIAS AGRUPADAS`, `AMBIENTE` e `CONTRATADOS`; a amostra não tem os meses entre 2023-03 e 2024-01'
  - desde: 2024-11
    mudanca: '12 colunas: entra `REGIME CONTRATUAL`'
  - desde: 2026-07
    mudanca: as datas passam a vir com hora, `dd/mm/aaaa hh:mm`, e o arquivo é UTF-8 com BOM
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# PADs em andamento na fase de exploração

## Resumo

Fotografia mensal dos planos de avaliação de descobertas (PADs) em andamento. O PAD é o plano que o concessionário apresenta para avaliar uma descoberta de petróleo ou gás natural antes de declarar a sua comercialidade; enquanto ele está ativo, o prazo da fase de exploração do bloco pode ser prorrogado. Cada linha traz o PAD, o bloco, a bacia, o operador, a rodada, a situação do PAD, o início efetivo e o término previsto. É o relatório «Planos de Avaliação de Descobertas (PADs) em Andamento» do painel dinâmico da fase de exploração da ANP.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pads-andamento` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (metadados da ANP); o lake guarda uma fotografia por mês |
| Cobertura | 2023-02 a em-curso |
| Unidade (uma linha) | um PAD em andamento no mês de referência (uma linha por PAD em cada arquivo mensal) |
| Granularidade | espacial: bloco e bacia; ambiente e grupo de bacias a partir de 2024-01; sem coordenadas; temporal: mês do arquivo (fotografia); início e término são datas do PAD |
| Formato bruto | CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `ano`, `mes`, `CÓDIGO DO PAD` |
| Colunas | 12 |
| Unidades de medida | — |
| Dados pessoais | `OPERADOR` (nome de empresas (pessoas jurídicas) operadoras e contratadas); `CONTRATADOS` (nome de empresas (pessoas jurídicas) operadoras e contratadas) |
| Eras | 2023-02: 8 colunas: `CÓDIGO DO PAD`, `BLOCO`, `BACIA`, `OPERADOR`, `RODADA`, `SITUAÇÃO`, `INÍCIO EFETIVO`, `TÉRMINO PREVISTO`; o arquivo de 2023-02 traz as datas como `aaaa-mm-dd hh:mm:ss`; 2024-01: 11 colunas: entram `BACIAS AGRUPADAS`, `AMBIENTE` e `CONTRATADOS`; a amostra não tem os meses entre 2023-03 e 2024-01; 2024-11: 12 colunas: entra `REGIME CONTRATUAL`; 2026-07: as datas passam a vir com hora, `dd/mm/aaaa hh:mm`, e o arquivo é UTF-8 com BOM |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Exploração (SEP); os dados vêm do SIGEP (Sistema de Informações Gerenciais de Exploração e Produção) e são o extrato do relatório «Planos de Avaliação de Descobertas (PADs) em Andamento» do painel dinâmico da fase de exploração (metadados da ANP). A página oficial publica um CSV por mês, em ponto e vírgula.
- **Catálogo do fetcher:** 41 arquivos mensais, de 2023-02 a 2026-07 (conferido em 2026-11-15). A página oficial lista arquivos até out/2026 e o catálogo do fetcher vai só até jul/2026; os meses seguintes entram quando o catálogo for atualizado.
- O catálogo não tem o arquivo de jun/2023; a página oficial lista 10 arquivos em 2023 (conferido em 2026-11-15).
- **Codificação:** os arquivos variam, e os da amostra são ISO-8859-1 ou UTF-8 com BOM; o conversor lê os dois (conferido na amostra: sem texto corrompido nas colunas).
- **Cada arquivo é uma fotografia do mês, não um incremento:** o arquivo de um mês repete as linhas dos meses anteriores que continuam valendo e acrescenta ou retira as que mudaram.

## Conteúdo

- **O que é uma linha:** um PAD em andamento. Na amostra, `CÓDIGO DO PAD` é único dentro de cada arquivo (33 linhas em 2023-02, 34 em 2023-03, 32 em 2024-01, 30 em 2024-11, 28 em 2025-09 e 23 em 2026-07, sem as linhas de rodapé).
- **Quando um PAD sai:** ele deixa de aparecer em `pads-andamento` quando é concluído e passa a `pads-concluidos`; o total em andamento cai de 33 (2023-02) para 23 (2026-07) na amostra.
- **Situação:** os valores observados são `Ativo`, `Suspenso`, `Postergacao Declaracao de Comercialidade` (sem acentos) e, em 2024-01, `Prorrogado Cautelarmente` (2 PADs); em 2026-07 são 6 ativos, 10 suspensos e 7 com postergação.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `2023-02` (8); `2023-03` (8) |
| 2024 | `2024-01` (11); `2024-11` (12) |
| 2025 | `2025-09` (12) |
| 2026 | `2026-07` (12) |

## Variáveis

As descrições vêm dos metadados da ANP (documento «PADs em andamento na fase de exploração», seção Colunas). O dicionário troca as descrições de `SITUAÇÃO` e `TÉRMINO PREVISTO` (a situação é descrita como «Data do término previsto do PAD» e o término previsto como «Data do término efetivo do PAD»); as descrições abaixo seguem o conteúdo observado. O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CÓDIGO DO PAD` | `CÓDIGO DO PAD` | texto | Código do PAD (Plano de Avaliação de Descobertas), que corresponde ao nome da acumulação principal da área do PAD | — | todo |
| `BLOCO` | `BLOCO` | texto | Nome do bloco exploratório: parte de uma bacia sedimentar, de superfície poligonal, onde se fazem atividades de exploração ou produção de petróleo e gás natural | — | todo |
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar onde está o bloco | — | todo |
| `OPERADOR` | `OPERADOR` | texto | Empresa designada pelos consorciados para conduzir as operações na área sob contrato (nome fantasia) | — | todo |
| `RODADA` | `RODADA` | texto | Rodada de licitação (ou ciclo de oferta permanente) de origem do bloco; pode listar mais de uma, separadas por vírgula, quando a linha reúne blocos de rodadas diferentes | — | todo |
| `SITUAÇÃO` | `SITUAÇÃO` | texto | Situação do PAD no mês do arquivo (por exemplo, Ativo, Suspenso, Postergação da Declaração de Comercialidade); a descrição do dicionário da ANP para esta coluna está trocada com a de TÉRMINO PREVISTO | — | todo |
| `INÍCIO EFETIVO` | `INÍCIO EFETIVO` | texto | Data do início efetivo do PAD | — | todo |
| `TÉRMINO PREVISTO` | `TÉRMINO PREVISTO` | texto | Data prevista para o término do PAD (a descrição do dicionário da ANP para esta coluna, «Data do término efetivo do PAD», está trocada com a de SITUAÇÃO) | — | todo |
| `BACIAS AGRUPADAS` | `BACIAS AGRUPADAS` | texto | Agrupamento das bacias sedimentares: Margem Equatorial, Margem Leste, Maduras (terrestres) e Nova Fronteira (terrestres); o dicionário da ANP lista as bacias de cada grupo | — | 2024-01 a 2026-07 |
| `AMBIENTE` | `AMBIENTE` | texto | Localização do bloco por ambiente: terra ou mar (a caixa do texto varia entre os arquivos: TERRA, Terra, MAR, Mar) | — | 2024-01 a 2026-07 |
| `CONTRATADOS` | `CONTRATADOS` | texto | Empresas contratadas e sua participação percentual no contrato; o operador vem marcado com asterisco (observado nos valores) | — | 2024-01 a 2026-07 |
| `REGIME CONTRATUAL` | `REGIME CONTRATUAL` | texto | Modalidade do regime contratual da área: Concessão ou Partilha | — | 2024-11 a 2026-07 |

## No lake

- Dataset `anp/pads-andamento`, particionado por `ano` e `mes` (mês do arquivo no catálogo); um Parquet por arquivo, `pads-andamento_AAAA-MM.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (maiúsculas, acentos e espaços). Datas, números e percentuais ficam como vêm no CSV (vírgula decimal, datas dd/mm/aaaa).
- O conversor não descarta as linhas em branco nem a linha de rodapé do painel (ver Cuidados).

## Cuidados de uso

- **Empilhar meses duplica linhas.** Cada arquivo repete o estado completo do mês; para a situação atual use só a partição `ano`/`mes` mais recente, e para uma série compare os meses entre si. Não some linhas de meses diferentes.
- **Linhas de rodapé e linhas vazias viram dados.** Os arquivos do painel trazem, depois dos dados, uma linha em branco e uma linha de texto com os filtros do painel (por exemplo, «Nenhum filtro aplicado» ou «Filtros aplicados: ...»), que o conversor grava como duas linhas quase totalmente nulas, uma delas com o texto na primeira coluna. Na amostra, os rodapés estão nos arquivos de 2023-03, 2024-01 e 2024-11 e não estão nos de 2023-02, 2025-09 e 2026-07. Descarte as linhas em que a coluna de identificação seja nula ou comece por «Filtro»/«Nenhum filtro».
- **Formato de data muda entre meses.** O mesmo campo aparece como `dd/mm/aaaa`, como `aaaa-mm-dd hh:mm:ss` e como `dd/mm/aaaa hh:mm`, conforme o arquivo (ver as eras). Normalize antes de converter para data.
- **Colunas entram e saem com o tempo** (ver as eras); ao empilhar meses use `union_by_name` e espere nulos nas colunas novas.
- **Dicionário com descrições trocadas.** Ver a nota acima sobre `SITUAÇÃO` e `TÉRMINO PREVISTO`; use os valores observados.
- **`SITUAÇÃO` sem acentos** (`Postergacao Declaracao de Comercialidade`), como vem na fonte.
- **Nome do PAD sem padrão.** `CÓDIGO DO PAD` mistura formatos (`PA-1BRSA559ARJS_BM-S-24`, `PA_1BRSA1063SPS_S-M-623`, `PA ACAJA-BURIZINHO BT-REC-10`); não há como extrair bloco ou poço do código de forma confiável.

## Exemplos

Número de PADs em andamento por situação na fotografia de 2026-07:

```python
import duckdb

duckdb.sql("""
    SELECT "SITUAÇÃO" AS situacao, count(*) AS pads
    FROM read_parquet('lake/anp/pads-andamento/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '07' AND "SITUAÇÃO" IS NOT NULL
    GROUP BY ALL
    ORDER BY pads DESC
""").show()
```

## Referências

- Dados abertos da ANP, Fase de Exploração (PADs em Andamento): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
- Metadados «PADs em Andamento» (ANP/SEP): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/painel-dinamico-da-fase-de-exploracao/pads-andamento/metadado-pads-andamento.pdf
