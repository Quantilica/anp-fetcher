---
dataset:
  id: blocos-contrato
  fonte: anp
  titulo: Blocos sob contrato na fase de exploração
  resumo: 'Relação mensal dos blocos exploratórios sob contrato de E&P: operador, consórcio, bacia, rodada, período exploratório, vencimentos e poços perfurados.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (metadados da ANP); o lake guarda uma fotografia por mês
  cobertura:
    inicio: 2023-04
    fim: em-curso
  unidade: um bloco exploratório sob contrato em um mês de referência (uma linha por bloco em cada arquivo mensal)
  granularidade:
    espacial: bloco exploratório, com bacia, ambiente (terra ou mar) e grupo de bacias; sem coordenadas
    temporal: mês do arquivo (fotografia); as datas dentro do arquivo são datas de contrato
  formato_bruto: CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave:
    - ano
    - mes
    - BLOCO
    colunas: 22
  unidades_de_medida:
    ÁREA (MIL km²): mil km²
    UTs COMPROMISSADAS: unidades de trabalho (UT)
    QTD POÇOS PERFURADOS: poços (contagem)
  dados_pessoais:
  - coluna: OPERADOR
    categoria: nome de empresas (pessoas jurídicas) operadoras e contratadas
  - coluna: CONTRATADOS
    categoria: nome de empresas (pessoas jurídicas) operadoras e contratadas
  eras:
  - desde: 2023-04
    mudanca: '20 colunas: sem `BACIAS AGRUPADAS` nem `REGIME CONTRATUAL`, e `BACIA` vem antes de `AMBIENTE`'
  - desde: 2024-02
    mudanca: '22 colunas: entram `BACIAS AGRUPADAS` e `REGIME CONTRATUAL` e a ordem passa a `AMBIENTE`, `BACIAS AGRUPADAS`, `BACIA`; a amostra não tem os meses entre 2023-05 e 2024-02, então o mês exato da mudança não foi conferido'
  - desde: 2024-12
    mudanca: '`REGIME CONTRATUAL` passa a trazer também `OP4_BE` e `OPartilha` (valores de rodada/ciclo da oferta permanente no lugar do regime) em parte dos blocos'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Blocos sob contrato na fase de exploração

## Resumo

Fotografia mensal dos blocos exploratórios que estão sob contrato de exploração e produção de petróleo e gás natural com a ANP. Para cada bloco, traz o número do contrato, o operador e as empresas contratadas com sua participação, a bacia, o ambiente (terra ou mar), a rodada de licitação de origem, o período exploratório em curso, se há ou houve plano de avaliação de descobertas (PAD), as datas de assinatura, suspensão e vencimento dos períodos exploratórios, as unidades de trabalho comprometidas e os poços já perfurados. É o relatório «Blocos sob Contrato» do painel dinâmico da fase de exploração da ANP.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/blocos-contrato` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (metadados da ANP); o lake guarda uma fotografia por mês |
| Cobertura | 2023-04 a em-curso |
| Unidade (uma linha) | um bloco exploratório sob contrato em um mês de referência (uma linha por bloco em cada arquivo mensal) |
| Granularidade | espacial: bloco exploratório, com bacia, ambiente (terra ou mar) e grupo de bacias; sem coordenadas; temporal: mês do arquivo (fotografia); as datas dentro do arquivo são datas de contrato |
| Formato bruto | CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `ano`, `mes`, `BLOCO` |
| Colunas | 22 |
| Unidades de medida | `ÁREA (MIL km²)`: mil km²; `UTs COMPROMISSADAS`: unidades de trabalho (UT); `QTD POÇOS PERFURADOS`: poços (contagem) |
| Dados pessoais | `OPERADOR` (nome de empresas (pessoas jurídicas) operadoras e contratadas); `CONTRATADOS` (nome de empresas (pessoas jurídicas) operadoras e contratadas) |
| Eras | 2023-04: 20 colunas: sem `BACIAS AGRUPADAS` nem `REGIME CONTRATUAL`, e `BACIA` vem antes de `AMBIENTE`; 2024-02: 22 colunas: entram `BACIAS AGRUPADAS` e `REGIME CONTRATUAL` e a ordem passa a `AMBIENTE`, `BACIAS AGRUPADAS`, `BACIA`; a amostra não tem os meses entre 2023-05 e 2024-02, então o mês exato da mudança não foi conferido; 2024-12: `REGIME CONTRATUAL` passa a trazer também `OP4_BE` e `OPartilha` (valores de rodada/ciclo da oferta permanente no lugar do regime) em parte dos blocos |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Exploração (SEP); os dados vêm do SIGEP (Sistema de Informações Gerenciais de Exploração e Produção) e são o extrato do relatório «Blocos sob Contrato» do painel dinâmico da fase de exploração (metadados da ANP). A página oficial publica um CSV por mês, em ponto e vírgula.
- **Catálogo do fetcher:** 40 arquivos mensais, de 2023-04 a 2026-07 (conferido em 2026-11-15). A página oficial lista arquivos até out/2026 e o catálogo do fetcher vai só até jul/2026; os meses seguintes entram quando o catálogo for atualizado.
- A página oficial lista também fev/2023 e mar/2023 (endereço diferente, `blocos-sob-contrato.csv`); o catálogo do fetcher começa em abr/2023.
- **Codificação:** os arquivos variam, e os da amostra são ISO-8859-1 ou UTF-8 com BOM; o conversor lê os dois (conferido na amostra: sem texto corrompido nas colunas).
- **Cada arquivo é uma fotografia do mês, não um incremento:** o arquivo de um mês repete as linhas dos meses anteriores que continuam valendo e acrescenta ou retira as que mudaram.

## Conteúdo

- **O que é uma linha:** um bloco sob contrato num mês. Na amostra, `BLOCO` é único dentro de cada arquivo (275 linhas de dados em 2023-04, 251 em 2024-02, 420 em 2024-12, 400 em 2025-10 e 419 em 2026-07, sem as 2 linhas de rodapé que os quatro primeiros arquivos carregam), enquanto `CONTRATO` repete quando um contrato reúne mais de um bloco (400 linhas e 398 contratos distintos em 2025-10).
- **Fase e período:** `PERÍODO` diz em que etapa o bloco está (valores observados: 1º PE, 2º PE, SUSPENSO e PRORROGADO POR PAD) e `FASE EXPLORATÓRIA VENCIMENTO` o prazo final; `PRESENÇA PAD` marca blocos com plano de avaliação de descobertas (266 de 2.043 linhas da amostra).
- **Ambiente:** 1.261 linhas de terra e 782 de mar na amostra (soma dos seis arquivos da amostra, sem as linhas de rodapé).
- **Metadados da ANP:** descrevem 21 campos (inclusive `BACIAS AGRUPADAS`); o arquivo atual tem 22 colunas, e `REGIME CONTRATUAL` não consta do dicionário deste conjunto.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `2023-04` (20); `2023-05` (20) |
| 2024 | `2024-02` (22); `2024-12` (22) |
| 2025 | `2025-10` (22) |
| 2026 | `2026-07` (22) |

## Variáveis

As descrições vêm dos metadados da ANP (documento «Blocos sob contrato», seção Colunas); onde o nome da coluna do arquivo difere do nome do dicionário, vale a descrição do dicionário para o campo correspondente. A descrição de `REGIME CONTRATUAL`, ausente deste dicionário, vem dos dicionários dos demais conjuntos da fase de exploração (PADs e declarações de comercialidade).
O dicionário define o tipo como texto, data, número inteiro e número decimal, mas o lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `BLOCO` | `BLOCO` | texto | Nome do bloco exploratório: parte de uma bacia sedimentar, de superfície poligonal, onde se fazem atividades de exploração ou produção de petróleo e gás natural | — | todo |
| `CONTRATO` | `CONTRATO` | texto | Código do contrato de E&P assinado entre o agente econômico e a ANP (número do processo, sem pontuação); um contrato pode cobrir mais de um bloco | — | todo |
| `OPERADOR` | `OPERADOR` | texto | Empresa designada pelos consorciados para conduzir as operações na área sob contrato (nome fantasia) | — | todo |
| `CONTRATADOS` | `CONTRATADOS` | texto | Empresas contratadas e sua participação percentual no contrato; o operador vem marcado com asterisco (observado nos valores) | — | todo |
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar onde está o bloco | — | todo |
| `AMBIENTE` | `AMBIENTE` | texto | Localização do bloco por ambiente: terra ou mar (a caixa do texto varia entre os arquivos: TERRA, Terra, MAR, Mar) | — | todo |
| `ÁREA (MIL km²)` | `ÁREA (MIL km²)` | texto | Área do bloco delimitada pelo polígono contratual, ou a parcela que o concessionário retém após devoluções parciais, em mil km² (vírgula decimal) | — | todo |
| `RODADA` | `RODADA` | texto | Rodada de licitação (ou ciclo de oferta permanente) de origem do bloco; pode listar mais de uma, separadas por vírgula, quando a linha reúne blocos de rodadas diferentes | — | todo |
| `PERÍODO` | `PERÍODO` | texto | Período exploratório em que o bloco está (1º PE, 2º PE, 3º PE, período único, SUSPENSO ou PRORROGADO POR PAD, conforme os valores observados) | — | todo |
| `PRESENÇA PAD` | `PRESENÇA PAD` | texto | Indica se há ou houve plano de avaliação de descobertas (PAD): «HÁ/HOUVE PAD» ou «NÃO HÁ/HOUVE PAD» | — | todo |
| `DATA ASSINATURA CONTRATO` | `DATA ASSINATURA CONTRATO` | texto | Data em que o contrato de E&P foi assinado (dd/mm/aaaa) | — | todo |
| `DATA INÍCIO SUSPENSÃO` | `DATA INÍCIO SUSPENSÃO` | texto | Data em que a suspensão do contrato começou (dd/mm/aaaa); vazia se o contrato não está ou não esteve suspenso | — | todo |
| `1º PE VENCIMENTO` | `1º PE VENCIMENTO` | texto | Data de vencimento do 1º período exploratório | — | todo |
| `2º PE VENCIMENTO` | `2º PE VENCIMENTO` | texto | Data de vencimento do 2º período exploratório | — | todo |
| `3º PE VENCIMENTO` | `3º PE VENCIMENTO` | texto | Data de vencimento do 3º período exploratório | — | todo |
| `ÚLTIMO PAD VENCIMENTO` | `ÚLTIMO PAD VENCIMENTO` | texto | Data de vencimento do último plano de avaliação de descobertas (PAD) | — | todo |
| `FASE EXPLORATÓRIA VENCIMENTO` | `FASE EXPLORATÓRIA VENCIMENTO` | texto | Data de vencimento da fase exploratória: a do último período exploratório ou a do último PAD, quando a fase está prorrogada por PAD | — | todo |
| `UTs COMPROMISSADAS` | `UTs COMPROMISSADAS` | texto | Unidades de trabalho (UT) comprometidas no programa exploratório mínimo do contrato; a UT é a unidade que converte os diferentes trabalhos exploratórios | — | todo |
| `QTD POÇOS PERFURADOS` | `QTD POÇOS PERFURADOS` | texto | Número de poços perfurados na área contratada até a divulgação do arquivo | — | todo |
| `POÇOS PERFURADOS` | `POÇOS PERFURADOS` | texto | Nome(s) ANP do(s) poço(s) perfurado(s) na área contratada (categorias 1 a 6 da RANP nº 699/2017), separados por vírgula | — | todo |
| `BACIAS AGRUPADAS` | `BACIAS AGRUPADAS` | texto | Agrupamento das bacias sedimentares: Margem Equatorial, Margem Leste, Maduras (terrestres) e Nova Fronteira (terrestres); o dicionário da ANP lista as bacias de cada grupo | — | 2024-02 a 2026-07 |
| `REGIME CONTRATUAL` | `REGIME CONTRATUAL` | texto | Modalidade do regime contratual da área: Concessão ou Partilha | — | 2024-02 a 2026-07 |

## No lake

- Dataset `anp/blocos-contrato`, particionado por `ano` e `mes` (mês do arquivo no catálogo); um Parquet por arquivo, `blocos-contrato_AAAA-MM.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (maiúsculas, acentos e espaços). Datas, números e percentuais ficam como vêm no CSV (vírgula decimal, datas dd/mm/aaaa).
- O conversor não descarta as linhas em branco nem a linha de rodapé do painel (ver Cuidados).

## Cuidados de uso

- **Empilhar meses duplica linhas.** Cada arquivo repete o estado completo do mês; para a situação atual use só a partição `ano`/`mes` mais recente, e para uma série compare os meses entre si. Não some linhas de meses diferentes.
- **Linhas de rodapé e linhas vazias viram dados.** Os arquivos do painel trazem, depois dos dados, uma linha em branco e uma linha de texto com os filtros do painel (por exemplo, «Nenhum filtro aplicado» ou «Filtros aplicados: ...»), que o conversor grava como duas linhas quase totalmente nulas, uma delas com o texto na primeira coluna. Na amostra, os rodapés estão nos arquivos de 2023-04, 2023-05, 2024-02 e 2024-12 e não estão nos de 2025-10 e 2026-07. Descarte as linhas em que a coluna de identificação seja nula ou comece por «Filtro»/«Nenhum filtro».
- **Formato de data muda entre meses.** O mesmo campo aparece como `dd/mm/aaaa`, como `aaaa-mm-dd hh:mm:ss` e como `dd/mm/aaaa hh:mm`, conforme o arquivo (ver as eras). Normalize antes de converter para data.
- **Colunas entram e saem com o tempo** (ver as eras); ao empilhar meses use `union_by_name` e espere nulos nas colunas novas.
- **`REGIME CONTRATUAL` com valores que não são regime.** Nos arquivos de 2024-12 e 2025-10 da amostra, 181 e 184 linhas trazem `OP4_BE` (nome do ciclo de oferta permanente, o mesmo valor de `RODADA`) e uma traz `OPartilha`, em vez de Concessão ou Partilha; o defeito está no CSV da fonte (conferido no arquivo bruto de 2024-12). Em 2026-07 só restam `Concessão`, `Partilha` e `OPartilha`.
- **Nomes de coluna diferentes do dicionário.** O arquivo traz `DATA ASSINATURA CONTRATO` e `QTD POÇOS PERFURADOS`, e o dicionário escreve `DATA DA ASSINATURA CONTRATO` e `QTD DE POÇOS PERFURADOS`.
- **`CONTRATADOS` é texto composto.** Participações e operador (asterisco) vêm numa só cadeia, por exemplo `*Petrobras - 50%, BP Energy - 50%`; separe por vírgula e extraia os percentuais para analisar o consórcio.
- **Operador e contratados são pessoas jurídicas.** Os nomes de empresas são informação pública do contrato; não há dado de pessoa física na amostra.

## Exemplos

Número de blocos sob contrato em cada ambiente na fotografia mais recente da amostra (2026-07):

```python
import duckdb

duckdb.sql("""
    SELECT "AMBIENTE" AS ambiente, count(*) AS blocos,
           round(sum(replace("ÁREA (MIL km²)", ',', '.')::DOUBLE), 1) AS area_mil_km2
    FROM read_parquet('lake/anp/blocos-contrato/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '07' AND "BLOCO" IS NOT NULL
    GROUP BY ALL
    ORDER BY blocos DESC
""").show()
```

## Referências

- Dados abertos da ANP, Fase de Exploração (Blocos sob Contrato): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
- Metadados «Blocos sob contrato» (ANP/SEP): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/painel-dinamico-da-fase-de-exploracao/bsc/metadados-blocos-sob-contrato.pdf
