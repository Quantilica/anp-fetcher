---
dataset:
  id: prorrogacoes-815
  fonte: anp
  titulo: Prorrogação de prazos da fase de exploração — Resolução ANP nº 815/2020
  resumo: 'Relação mensal dos blocos exploratórios com o período exploratório prorrogado pela Resolução ANP nº 815/2020: bloco, contrato, operador, etapa prorrogada e data da efetivação.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (metadados da ANP); o lake guarda uma fotografia por mês
  cobertura:
    inicio: 2023-02
    fim: em-curso
  unidade: um bloco com prorrogação do período exploratório, no mês de referência (uma linha por bloco em cada arquivo mensal)
  granularidade:
    espacial: bloco exploratório (sem bacia nem coordenadas neste conjunto)
    temporal: mês do arquivo (fotografia); `Efetivação da Prorrogação`/`Data de Adesão à Resolução` é a data do evento
  formato_bruto: CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 7
  dados_pessoais:
  - coluna: Operador
    categoria: nome de empresas (pessoas jurídicas) operadoras
  eras:
  - desde: 2023-02
    mudanca: colunas `Bloco`, `Contrato`, `Operador`, `Etapa Prorrogada`, `PAD` e `Efetivação da Prorrogação`; a amostra tem 2 linhas de rodapé (ver Cuidados)
  - desde: 2026-07
    mudanca: '`Efetivação da Prorrogação` passa a se chamar `Data de Adesão à Resolução`, que é o nome do dicionário da ANP; a amostra não tem os meses entre 2025-09 e 2026-07, então o mês exato da mudança não foi conferido'
  - desde: 2023-12
    mudanca: o cabeçalho de `Etapa Prorrogada` passa a ter um espaço no fim (`Etapa Prorrogada `), e o lake guarda as duas grafias como colunas separadas; a amostra não tem os meses entre 2023-03 e 2023-12
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Prorrogação de prazos da fase de exploração — Resolução ANP nº 815/2020

## Resumo

Fotografia mensal dos contratos de exploração e produção de petróleo e gás natural, na fase de exploração, cujo período exploratório foi prorrogado ao abrigo da Resolução ANP nº 815/2020. Cada linha é um bloco, com o nome do contrato, o operador, a etapa prorrogada e a data de efetivação da prorrogação (adesão à resolução), além do PAD, quando a etapa prorrogada é um plano de avaliação de descobertas. É o relatório «Resolução ANP nº 815/2020» do painel dinâmico da fase de exploração da ANP.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/prorrogacoes-815` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (metadados da ANP); o lake guarda uma fotografia por mês |
| Cobertura | 2023-02 a em-curso |
| Unidade (uma linha) | um bloco com prorrogação do período exploratório, no mês de referência (uma linha por bloco em cada arquivo mensal) |
| Granularidade | espacial: bloco exploratório (sem bacia nem coordenadas neste conjunto); temporal: mês do arquivo (fotografia); `Efetivação da Prorrogação`/`Data de Adesão à Resolução` é a data do evento |
| Formato bruto | CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 7 |
| Unidades de medida | — |
| Dados pessoais | `Operador` (nome de empresas (pessoas jurídicas) operadoras) |
| Eras | 2023-02: colunas `Bloco`, `Contrato`, `Operador`, `Etapa Prorrogada`, `PAD` e `Efetivação da Prorrogação`; a amostra tem 2 linhas de rodapé (ver Cuidados); 2026-07: `Efetivação da Prorrogação` passa a se chamar `Data de Adesão à Resolução`, que é o nome do dicionário da ANP; a amostra não tem os meses entre 2025-09 e 2026-07, então o mês exato da mudança não foi conferido; 2023-12: o cabeçalho de `Etapa Prorrogada` passa a ter um espaço no fim (`Etapa Prorrogada `), e o lake guarda as duas grafias como colunas separadas; a amostra não tem os meses entre 2023-03 e 2023-12 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Exploração (SEP); os dados vêm do SIGEP (Sistema de Informações Gerenciais de Exploração e Produção) e são o extrato do relatório «Resolução ANP nº 815/2020» do painel dinâmico da fase de exploração (metadados da ANP). A página oficial publica um CSV por mês, em ponto e vírgula.
- **Catálogo do fetcher:** 42 arquivos mensais, de 2023-02 a 2026-07 (conferido em 2026-11-15). A página oficial lista arquivos até out/2026 e o catálogo do fetcher vai só até jul/2026; os meses seguintes entram quando o catálogo for atualizado.
- **Codificação:** os arquivos variam, e os da amostra são ISO-8859-1 ou UTF-8 com BOM; o conversor lê os dois (conferido na amostra: sem texto corrompido nas colunas).
- **Cada arquivo é uma fotografia do mês, não um incremento:** o arquivo de um mês repete as linhas dos meses anteriores que continuam valendo e acrescenta ou retira as que mudaram.

## Conteúdo

- **O que é uma linha:** um bloco (ou grupo de blocos) cujo período exploratório foi prorrogado pela Resolução ANP nº 815/2020. De 124 linhas de dados em 2023-02 a 132 em 2026-07 na amostra (sem as linhas de rodapé).
- **Etapa prorrogada:** `Período único` (228 linhas somadas da amostra), `1º e 2º PE` (148), `PAD` (111) e `2º PE` (32), contando as duas grafias da coluna; `PAD` traz o nome do plano em 28 linhas por arquivo.
- **`Bloco` não é único:** em 2026-07, `ES-M-525` aparece duas vezes; por isso o dataset não declara chave.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `2023-02` (6); `2023-03` (6); `2023-12` (6) |
| 2024 | `2024-11` (6) |
| 2025 | `2025-09` (6) |
| 2026 | `2026-07` (6) |

## Variáveis

As descrições vêm dos metadados da ANP para a Resolução nº 815/2020 (documento da própria resolução). O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Bloco` | `Bloco` | texto | Nome do bloco exploratório com o período exploratório prorrogado (em casos de vários blocos, o nome vem composto, por exemplo `SOL-T-191 e SOL-T-192`) | — | todo |
| `Contrato` | `Contrato` | texto | Nome fantasia do contrato de E&P (por exemplo, bloco e rodada, como `TUC-T-174_R11`); o dicionário da ANP mistura «nome fantasia» e «código do contrato», mas os valores observados são nomes, não o número do processo | — | todo |
| `Operador` | `Operador` | texto | Empresa que opera o contrato de E&P (nome fantasia) | — | todo |
| `Etapa Prorrogada` | `Etapa Prorrogada` | texto | Etapa do período exploratório que foi prorrogada: período único, 1º e 2º PE, 2º PE ou PAD (a grafia varia: `Período único` e `Período Único`) | — | 2023-02 a 2023-03 |
| `PAD` | `PAD` | texto | Nome do plano de avaliação de descobertas (PAD) a que a prorrogação se refere, quando houve PAD; texto livre | — | todo |
| `Efetivação da Prorrogação` | `Efetivação da Prorrogação` | texto | Data de efetivação da prorrogação (dd/mm/aaaa); nome da coluna até pelo menos o arquivo de 2025 da amostra, depois chamada `Data de Adesão à Resolução` | — | 2023-02 a 2025-09 |
| `Etapa Prorrogada ` | `Etapa Prorrogada ` | texto | Etapa do período exploratório que foi prorrogada: período único, 1º e 2º PE, 2º PE ou PAD (a grafia varia: `Período único` e `Período Único`) (o nome da coluna tem espaços no início ou no fim) | — | 2023-12 a 2026-07 |
| `Data de Adesão à Resolução` | `Data de Adesão à Resolução` | texto | Data em que o contrato aderiu à resolução, isto é, em que a prorrogação foi efetivada (dd/mm/aaaa) | — | 2026-07 |

## No lake

- Dataset `anp/prorrogacoes-815`, particionado por `ano` e `mes` (mês do arquivo no catálogo); um Parquet por arquivo, `prorrogacoes-815_AAAA-MM.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (maiúsculas, acentos e espaços). Datas, números e percentuais ficam como vêm no CSV (vírgula decimal, datas dd/mm/aaaa).
- O conversor não descarta as linhas em branco nem a linha de rodapé do painel (ver Cuidados).

## Cuidados de uso

- **Empilhar meses duplica linhas.** Cada arquivo repete o estado completo do mês; para a situação atual use só a partição `ano`/`mes` mais recente, e para uma série compare os meses entre si. Não some linhas de meses diferentes.
- **Linhas de rodapé e linhas vazias viram dados.** Os arquivos do painel trazem, depois dos dados, uma linha em branco e uma linha de texto com os filtros do painel (por exemplo, «Nenhum filtro aplicado» ou «Filtros aplicados: ...»), que o conversor grava como duas linhas quase totalmente nulas, uma delas com o texto na primeira coluna. Na amostra, os rodapés estão nos arquivos de 2023-02, 2023-03, 2023-12, 2024-11 e 2025-09 e não estão no de 2026-07. Descarte as linhas em que a coluna de identificação seja nula ou comece por «Filtro»/«Nenhum filtro».
- **Formato de data muda entre meses.** O mesmo campo aparece como `dd/mm/aaaa`, como `aaaa-mm-dd hh:mm:ss` e como `dd/mm/aaaa hh:mm`, conforme o arquivo (ver as eras). Normalize antes de converter para data.
- **Colunas entram e saem com o tempo** (ver as eras); ao empilhar meses use `union_by_name` e espere nulos nas colunas novas.
- **`Etapa Prorrogada` em duas colunas.** Em arquivos de 2023-12 em diante o cabeçalho tem um espaço final, e o conversor não o remove; ao empilhar meses, junte `Etapa Prorrogada` e `Etapa Prorrogada ` com `coalesce`.

## Exemplos

Número de blocos por etapa prorrogada na fotografia de 2026-07 (Resolução 815):

```python
import duckdb

duckdb.sql("""
    SELECT "Etapa Prorrogada " AS etapa, count(*) AS blocos
    FROM read_parquet('lake/anp/prorrogacoes-815/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '07' AND "Contrato" IS NOT NULL
    GROUP BY ALL
    ORDER BY blocos DESC
""").show()
```

## Referências

- Dados abertos da ANP, Fase de Exploração (Prorrogação de Prazos da Fase de Exploração): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
- Metadados da Resolução ANP nº 815/2020: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/prorrogacao-prazos-fase-exploracao/ranp-815-2020/metadado-ranp-n815-2020.pdf
