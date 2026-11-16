---
dataset:
  id: declaracoes-comercialidade
  fonte: anp
  titulo: Declarações de comercialidade na fase de exploração
  resumo: 'Relação mensal das declarações de comercialidade feitas em blocos sob contrato: PAD, bloco, bacia, operador, rodada, data da declaração e campo ou área de desenvolvimento.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (metadados da ANP); o lake guarda uma fotografia por mês
  cobertura:
    inicio: 2023-02
    fim: em-curso
  unidade: uma declaração de comercialidade (PAD, bloco e área de desenvolvimento) acumulada até o mês do arquivo
  granularidade:
    espacial: bloco e bacia; ambiente (terra ou mar) a partir de 2023-12; sem coordenadas
    temporal: mês do arquivo (fotografia); `DATA DECLARAÇÃO COMERCIALIDADE` é a data do evento
  formato_bruto: CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 12
  dados_pessoais:
  - coluna: OPERADOR
    categoria: nome de empresas (pessoas jurídicas) operadoras
  - coluna: OPERADOR_DC
    categoria: nome de empresas (pessoas jurídicas) operadoras
  eras:
  - desde: 2023-02
    mudanca: '7 colunas: `BLOCO` (singular) e `CAMPO/ ÁREA DE DESENVOLVIMENTO`, sem `AMBIENTE`; as datas do arquivo de 2023-02 vêm como `aaaa-mm-dd hh:mm:ss`'
  - desde: 2023-12
    mudanca: '8 colunas: `BLOCO(S)`, `AMBIENTE` e `ÁREA DE DESENVOLVIMENTO` (a coluna `CAMPO/ ÁREA DE DESENVOLVIMENTO` perde o prefixo); a amostra não tem os meses entre 2023-03 e 2023-12'
  - desde: 2024-11
    mudanca: '9 colunas: entra `REGIME CONTRATUAL`; a amostra não tem os meses entre 2023-12 e 2024-11'
  - desde: 2026-07
    mudanca: '10 colunas: entra `OPERADOR_DC`; `RODADA` e `REGIME CONTRATUAL` podem trazer mais de um valor separado por vírgula (por exemplo, `BID11, BID13` e `Concessão, Concessão`)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Declarações de comercialidade na fase de exploração

## Resumo

Fotografia mensal das declarações de comercialidade de descobertas feitas nos blocos sob contrato da fase de exploração: o concessionário notifica a ANP de que a descoberta é comercial, e a área passa a ser uma área de desenvolvimento (campo). Cada linha liga o plano de avaliação de descobertas (PAD) ao bloco, à bacia, ao operador, à rodada, à data da declaração e ao nome do campo ou da área de desenvolvimento. É o relatório «Declarações de Comercialidade» do painel dinâmico da fase de exploração da ANP.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/declaracoes-comercialidade` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (metadados da ANP); o lake guarda uma fotografia por mês |
| Cobertura | 2023-02 a em-curso |
| Unidade (uma linha) | uma declaração de comercialidade (PAD, bloco e área de desenvolvimento) acumulada até o mês do arquivo |
| Granularidade | espacial: bloco e bacia; ambiente (terra ou mar) a partir de 2023-12; sem coordenadas; temporal: mês do arquivo (fotografia); `DATA DECLARAÇÃO COMERCIALIDADE` é a data do evento |
| Formato bruto | CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 12 |
| Unidades de medida | — |
| Dados pessoais | `OPERADOR` (nome de empresas (pessoas jurídicas) operadoras); `OPERADOR_DC` (nome de empresas (pessoas jurídicas) operadoras) |
| Eras | 2023-02: 7 colunas: `BLOCO` (singular) e `CAMPO/ ÁREA DE DESENVOLVIMENTO`, sem `AMBIENTE`; as datas do arquivo de 2023-02 vêm como `aaaa-mm-dd hh:mm:ss`; 2023-12: 8 colunas: `BLOCO(S)`, `AMBIENTE` e `ÁREA DE DESENVOLVIMENTO` (a coluna `CAMPO/ ÁREA DE DESENVOLVIMENTO` perde o prefixo); a amostra não tem os meses entre 2023-03 e 2023-12; 2024-11: 9 colunas: entra `REGIME CONTRATUAL`; a amostra não tem os meses entre 2023-12 e 2024-11; 2026-07: 10 colunas: entra `OPERADOR_DC`; `RODADA` e `REGIME CONTRATUAL` podem trazer mais de um valor separado por vírgula (por exemplo, `BID11, BID13` e `Concessão, Concessão`) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Exploração (SEP); os dados vêm do SIGEP (Sistema de Informações Gerenciais de Exploração e Produção) e são o extrato do relatório «Declarações de Comercialidade» do painel dinâmico da fase de exploração (metadados da ANP). A página oficial publica um CSV por mês, em ponto e vírgula.
- **Catálogo do fetcher:** 42 arquivos mensais, de 2023-02 a 2026-07 (conferido em 2026-11-15). A página oficial lista arquivos até out/2026 e o catálogo do fetcher vai só até jul/2026; os meses seguintes entram quando o catálogo for atualizado.
- **Codificação:** os arquivos variam, e os da amostra são ISO-8859-1 ou UTF-8 com BOM; o conversor lê os dois (conferido na amostra: sem texto corrompido nas colunas).
- **Cada arquivo é uma fotografia do mês, não um incremento:** o arquivo de um mês repete as linhas dos meses anteriores que continuam valendo e acrescenta ou retira as que mudaram.

## Conteúdo

- **O que é uma linha:** uma declaração de comercialidade, identificada pelo par PAD e área de desenvolvimento. O acumulado cresce com o tempo: de 249 linhas em 2023-02 a 272 em 2026-07 na amostra (descontadas as 2 linhas de rodapé dos arquivos que as têm).
- **`CÓDIGO DO PAD` não é único:** na amostra, 2025-09 tem 268 linhas e 238 códigos distintos, porque um PAD pode dar origem a mais de uma área de desenvolvimento ou cobrir mais de um bloco.
- **Datas:** `DATA DECLARAÇÃO COMERCIALIDADE` cobre declarações antigas (por exemplo, 19/12/2005 e 21/07/2006 na amostra) e recentes (27/10/2025 no arquivo de 2026-07).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `2023-02` (7); `2023-03` (7); `2023-12` (8) |
| 2024 | `2024-11` (9) |
| 2025 | `2025-09` (9) |
| 2026 | `2026-07` (10) |

## Variáveis

As descrições vêm dos metadados da ANP (documento «Declarações de comercialidade na fase de exploração», seção Colunas), com os nomes antigos das colunas mapeados para os do dicionário. `OPERADOR_DC` não consta do dicionário. O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `CÓDIGO DO PAD` | `CÓDIGO DO PAD` | texto | Código do PAD (Plano de Avaliação de Descobertas), que corresponde ao nome da acumulação principal da área do PAD | — | todo |
| `BLOCO` | `BLOCO` | texto | Nome do bloco exploratório: parte de uma bacia sedimentar, de superfície poligonal, onde se fazem atividades de exploração ou produção de petróleo e gás natural | — | 2023-02 a 2023-03 |
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar onde está o bloco | — | todo |
| `OPERADOR` | `OPERADOR` | texto | Empresa designada pelos consorciados para conduzir as operações na área sob contrato (nome fantasia) | — | todo |
| `RODADA` | `RODADA` | texto | Rodada de licitação (ou ciclo de oferta permanente) de origem do bloco; pode listar mais de uma, separadas por vírgula, quando a linha reúne blocos de rodadas diferentes | — | todo |
| `DATA DECLARAÇÃO COMERCIALIDADE` | `DATA DECLARAÇÃO COMERCIALIDADE` | texto | Data da declaração de comercialidade, em que o concessionário comunica à ANP a descoberta comercial (dd/mm/aaaa; no arquivo de 2023-02, aaaa-mm-dd hh:mm:ss) | — | todo |
| `CAMPO/ ÁREA DE DESENVOLVIMENTO` | `CAMPO/ ÁREA DE DESENVOLVIMENTO` | texto | Nome do campo ou da área de desenvolvimento (nome da coluna na versão mais antiga do arquivo; equivale a ÁREA DE DESENVOLVIMENTO) | — | 2023-02 a 2023-03 |
| `BLOCO(S)` | `BLOCO(S)` | texto | Nome do bloco ou dos blocos exploratórios da área; vários blocos aparecem separados por vírgula | — | 2023-12 a 2026-07 |
| `AMBIENTE` | `AMBIENTE` | texto | Localização do bloco por ambiente: terra ou mar (a caixa do texto varia entre os arquivos: TERRA, Terra, MAR, Mar) | — | 2023-12 a 2026-07 |
| `ÁREA DE DESENVOLVIMENTO` | `ÁREA DE DESENVOLVIMENTO` | texto | Nome da área de desenvolvimento: área produtora de petróleo ou gás natural, de um ou mais reservatórios, a profundidades variáveis | — | 2023-12 a 2026-07 |
| `REGIME CONTRATUAL` | `REGIME CONTRATUAL` | texto | Modalidade do regime contratual da área: Concessão ou Partilha | — | 2024-11 a 2026-07 |
| `OPERADOR_DC` | `OPERADOR_DC` | texto | Operador no momento da declaração de comercialidade (descrição deduzida do nome e dos valores observados: difere de `OPERADOR` em 93 das 272 linhas de 2026-07); não consta do dicionário da ANP | — | 2026-07 |

## No lake

- Dataset `anp/declaracoes-comercialidade`, particionado por `ano` e `mes` (mês do arquivo no catálogo); um Parquet por arquivo, `declaracoes-comercialidade_AAAA-MM.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (maiúsculas, acentos e espaços). Datas, números e percentuais ficam como vêm no CSV (vírgula decimal, datas dd/mm/aaaa).
- O conversor não descarta as linhas em branco nem a linha de rodapé do painel (ver Cuidados).

## Cuidados de uso

- **Empilhar meses duplica linhas.** Cada arquivo repete o estado completo do mês; para a situação atual use só a partição `ano`/`mes` mais recente, e para uma série compare os meses entre si. Não some linhas de meses diferentes.
- **Linhas de rodapé e linhas vazias viram dados.** Os arquivos do painel trazem, depois dos dados, uma linha em branco e uma linha de texto com os filtros do painel (por exemplo, «Nenhum filtro aplicado» ou «Filtros aplicados: ...»), que o conversor grava como duas linhas quase totalmente nulas, uma delas com o texto na primeira coluna. Na amostra, os rodapés estão nos arquivos de 2023-03, 2023-12 e 2024-11 e não estão nos de 2023-02, 2025-09 e 2026-07. Descarte as linhas em que a coluna de identificação seja nula ou comece por «Filtro»/«Nenhum filtro».
- **Formato de data muda entre meses.** O mesmo campo aparece como `dd/mm/aaaa`, como `aaaa-mm-dd hh:mm:ss` e como `dd/mm/aaaa hh:mm`, conforme o arquivo (ver as eras). Normalize antes de converter para data.
- **Colunas entram e saem com o tempo** (ver as eras); ao empilhar meses use `union_by_name` e espere nulos nas colunas novas.
- **Rodapé com texto de filtro.** O texto «Filtros aplicados: CAMPO não é Gavião Mateiro-errado» é uma anotação do painel (um filtro de campo mal nomeado), não um dado.
- **Dois nomes de coluna para o mesmo campo.** `BLOCO`/`BLOCO(S)` e `CAMPO/ ÁREA DE DESENVOLVIMENTO`/`ÁREA DE DESENVOLVIMENTO` são o mesmo campo em eras diferentes; junte-os com `coalesce` ao empilhar meses.
- **`AMBIENTE` e `REGIME CONTRATUAL` escritos de formas diferentes** (`Terra`, `Mar`, `Concessão`, `Partilha`), sem a variação de caixa dos conjuntos de blocos sob contrato; confira antes de filtrar.

## Exemplos

Número de declarações de comercialidade por ano, na fotografia de 2026-07 da amostra:

```python
import duckdb

duckdb.sql("""
    SELECT right("DATA DECLARAÇÃO COMERCIALIDADE", 4) AS ano_declaracao, count(*) AS declaracoes
    FROM read_parquet('lake/anp/declaracoes-comercialidade/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '07' AND "BACIA" IS NOT NULL
    GROUP BY ALL
    ORDER BY 1 DESC
    LIMIT 5
""").show()
```

## Referências

- Dados abertos da ANP, Fase de Exploração (Declarações de Comercialidade): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
- Metadados «Declarações de Comercialidade na Fase de Exploração» (ANP/SEP): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/painel-dinamico-da-fase-de-exploracao/dcfe/metadado-declaracoes-comercialidade.pdf
