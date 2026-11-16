---
dataset:
  id: processos-sancionadores
  fonte: anp
  titulo: Processos sancionadores de exploração de petróleo e gás natural
  resumo: 'Relação mensal dos processos administrativos sancionadores em trâmite na Superintendência de Exploração: empresa autuada, CNPJ, processo, auto de infração, motivo, situação e multa.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (metadados da ANP); o lake guarda uma fotografia por mês
  cobertura:
    inicio: 2023-02
    fim: em-curso
  unidade: um processo administrativo sancionador em trâmite no mês de referência
  granularidade:
    espacial: não informada (sem bloco, bacia ou município; o motivo cita blocos em texto livre)
    temporal: mês do arquivo (fotografia); `DATA DO AUTO` é a data do auto de infração
  formato_bruto: CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho; 9 colunas
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave:
    - ano
    - mes
    - Nº PROCESSO
    colunas: 9
  unidades_de_medida:
    ' MULTA APLICADA   ': R$ (reais)
  dados_pessoais:
  - coluna: EMPRESA
    categoria: razão social de empresa autuada (pessoa jurídica)
  - coluna: CNPJ/CPF
    categoria: CNPJ de pessoa jurídica (o campo admite CPF)
  eras:
  - desde: 2023-02
    mudanca: '9 colunas: `EMPRESA`, `CNPJ/CPF`, `Nº PROCESSO`, `Nº DF`, `DATA DO AUTO`, `MOTIVO`, `SITUAÇÃO PROCESSUAL`, ` MULTA APLICADA   ` e ` RECURSO ` (as duas últimas com espaços no cabeçalho); a estrutura é a mesma em todos os seis arquivos da amostra, até 2026-07'
  - desde: 2026-07
    mudanca: '`Nº DF` passa a vir com espaços como separador (`218 000 25 33 647146`) em vez de pontos'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Processos sancionadores de exploração de petróleo e gás natural

## Resumo

Fotografia mensal dos processos administrativos sancionadores relativos à exploração de petróleo e gás natural em trâmite na Superintendência de Exploração (SEP) da ANP. Cada linha é um processo, com a empresa autuada e seu CNPJ, o número do processo e do documento de fiscalização, a data do auto de infração, o motivo da autuação, a situação do andamento, o valor da multa aplicada e se houve recurso. Os autuados têm direito a contraditório e ampla defesa, e a situação reflete o momento do arquivo.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/processos-sancionadores` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (metadados da ANP); o lake guarda uma fotografia por mês |
| Cobertura | 2023-02 a em-curso |
| Unidade (uma linha) | um processo administrativo sancionador em trâmite no mês de referência |
| Granularidade | espacial: não informada (sem bloco, bacia ou município; o motivo cita blocos em texto livre); temporal: mês do arquivo (fotografia); `DATA DO AUTO` é a data do auto de infração |
| Formato bruto | CSV mensal, separador ponto e vírgula, ISO-8859-1 ou UTF-8 com BOM, uma linha de cabeçalho; 9 colunas |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `ano`, `mes`, `Nº PROCESSO` |
| Colunas | 9 |
| Unidades de medida | ` MULTA APLICADA   `: R$ (reais) |
| Dados pessoais | `EMPRESA` (razão social de empresa autuada (pessoa jurídica)); `CNPJ/CPF` (CNPJ de pessoa jurídica (o campo admite CPF)) |
| Eras | 2023-02: 9 colunas: `EMPRESA`, `CNPJ/CPF`, `Nº PROCESSO`, `Nº DF`, `DATA DO AUTO`, `MOTIVO`, `SITUAÇÃO PROCESSUAL`, ` MULTA APLICADA   ` e ` RECURSO ` (as duas últimas com espaços no cabeçalho); a estrutura é a mesma em todos os seis arquivos da amostra, até 2026-07; 2026-07: `Nº DF` passa a vir com espaços como separador (`218 000 25 33 647146`) em vez de pontos |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Exploração (SEP); resultado da consolidação dos processos sancionadores de exploração em trâmite na SEP (metadados da ANP). Os dados são o relatório «Processos sancionadores de exploração de petróleo e gás natural» do painel dinâmico da fase de exploração.
- **Catálogo do fetcher:** 42 arquivos mensais, de 2023-02 a 2026-07 (conferido em 2026-11-15); a página oficial lista arquivos até out/2026
- **Codificação:** ISO-8859-1 nos arquivos da amostra; o conversor lê sem corromper o texto.
- **Cada arquivo é uma fotografia do mês:** o conjunto não acumula. Os processos que se encerram deixam de aparecer, e os arquivos de meses distantes trazem processos diferentes (na amostra, o arquivo de 2023-02 traz autos de 2019 e o de 2026-07, autos de 2025).

## Conteúdo

- **O que é uma linha:** um processo sancionador. `Nº PROCESSO` é único em cada arquivo da amostra (27 processos em 2023-02, 26 em 2023-03, 23 em 2023-12, 20 em 2024-11, 25 em 2025-09 e 33 em 2026-07).
- **Linhas em branco:** o arquivo de 2023-02 tem 118 linhas lidas, das quais 91 vazias; 2023-12 tem 100 (77 vazias), 2024-11 tem 91 (71) e 2026-07 tem 57 (24). São linhas `;;;;;;;;` do fim do CSV da fonte, que o conversor mantém.
- **Multa:** a coluna de multa está preenchida em 21 de 27 processos em 2023-02 e em 2 de 33 em 2026-07, porque os processos recentes ainda estão em instrução.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `2023-02` (9); `2023-03` (9); `2023-12` (9) |
| 2024 | `2024-11` (9) |
| 2025 | `2025-09` (9) |
| 2026 | `2026-07` (9) |

## Variáveis

As descrições vêm dos metadados da ANP (documento «Processos sancionadores de exploração de petróleo e gás natural», seção Colunas), cujos nomes têm o prefixo da seção do painel («DADOS GERAIS:», «ANDAMENTO DO PROCESSO:», «RESULTADO DO PROCESSO:»); o arquivo CSV não traz esse prefixo. O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `EMPRESA` | `EMPRESA` | texto | Nome da empresa autuada, com contrato ativo (razão social; o texto da fonte pode vir com espaço no início) | — | todo |
| `CNPJ/CPF` | `CNPJ/CPF` | texto | CNPJ (ou CPF) do concessionário ou contratado autuado, com pontuação; na amostra, todos os 154 valores têm 14 dígitos (CNPJ) | — | todo |
| `Nº PROCESSO` | `Nº PROCESSO` | texto | Número do processo administrativo sancionador (formato `48610.NNNNNN/AAAA-DD`) | — | todo |
| `Nº DF` | `Nº DF` | texto | Número do documento de fiscalização (DF); o separador varia entre pontos (`809.000.19.33.474076`) e espaços (`218 000 25 33 647146`) | — | todo |
| `DATA DO AUTO` | `DATA DO AUTO` | texto | Data do auto de infração que inicia o processo administrativo sancionador (dd/mm/aaaa) | — | todo |
| `MOTIVO` | `MOTIVO` | texto | Fundamentação da autuação: o descumprimento que originou o auto de infração (texto livre) | — | todo |
| `SITUAÇÃO PROCESSUAL` | `SITUAÇÃO PROCESSUAL` | texto | Situação do andamento do processo administrativo no mês do arquivo (texto livre, por exemplo, «Encaminhado para registro no Cadin.») | — | todo |
| ` MULTA APLICADA   ` | ` MULTA APLICADA   ` | texto | Valor da multa aplicada como resultado do processo, em reais, escrito como `R$ 65.000,00` (vazio enquanto não há multa); nome da coluna com espaços no início e no fim (o nome da coluna tem espaços no início ou no fim) | — | todo |
| ` RECURSO ` | ` RECURSO ` | texto | Indica se houve recurso (`SIM`, `NÃO.`) ou descreve a decisão sobre o recurso (texto livre, por exemplo, «Indeferimento do Recurso»); nome da coluna com espaços no início e no fim (o nome da coluna tem espaços no início ou no fim) | — | todo |

## No lake

- Dataset `anp/processos-sancionadores`, particionado por `ano` e `mes` (mês do arquivo no catálogo); um Parquet por arquivo, `processos-sancionadores_AAAA-MM.parquet`.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (maiúsculas, acentos e espaços). Datas, números e percentuais ficam como vêm no CSV (vírgula decimal, datas dd/mm/aaaa).
- O conversor não descarta as linhas em branco nem a linha de rodapé do painel (ver Cuidados).
- As colunas ` MULTA APLICADA   ` e ` RECURSO ` mantêm os espaços do cabeçalho original, no início e no fim do nome.

## Cuidados de uso

- **Cada arquivo é uma fotografia, e o conjunto não acumula.** Um processo concluído some do arquivo seguinte. Para a situação atual use só a partição mais recente; para o histórico de um processo, procure o `Nº PROCESSO` nos vários meses.
- **Linhas em branco viram dados.** O conversor mantém as linhas vazias do fim do CSV (91 de 118 em 2023-02). Descarte as linhas com `Nº PROCESSO` nulo.
- **Nomes de coluna com espaços.** ` MULTA APLICADA   ` e ` RECURSO ` têm espaços no início e no fim; ao consultar, cite o nome entre aspas duplas com os espaços exatos, ou renomeie.
- **Valor da multa em texto.** `R$ 65.000,00`: tire o prefixo, os pontos e troque a vírgula antes de converter. A coluna é vazia para processos sem multa aplicada.
- **A situação processual não é definitiva.** A fonte avisa que os autuados têm direito ao contraditório e à ampla defesa; só o julgamento definitivo comprova a infração. Não trate uma linha como infração confirmada.
- **`Nº DF` com dois formatos** (pontos e espaços); normalize antes de ligar a outras tabelas, como a de multas.
- **Dados identificáveis.** Há razão social e CNPJ da empresa autuada, e os campos de texto livre podem citar contratos e decisões. O campo `CNPJ/CPF` admite CPF; na amostra todos têm 14 dígitos (CNPJ).
- **Metadados com erros de grafia** (por exemplo, «Dados gerais referente àda situação»); a descrição das colunas abaixo é a do conteúdo.

## Exemplos

Número de processos sancionadores em trâmite e soma das multas aplicadas na fotografia de 2026-07, convertendo o texto «R$ 15.000,00» em número:

```python
import duckdb

duckdb.sql("""
    SELECT count(*) AS processos,
           count(" MULTA APLICADA   ") AS com_multa,
           sum(replace(replace(replace(" MULTA APLICADA   ", 'R$', ''), '.', ''), ',', '.')::DOUBLE) AS multa_total_reais
    FROM read_parquet('lake/anp/processos-sancionadores/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '07' AND "Nº PROCESSO" IS NOT NULL
""").show()
```

## Referências

- Dados abertos da ANP, Fase de Exploração (Processos Sancionadores): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
- Metadados «Processos sancionadores de exploração de petróleo e gás natural» (ANP/SEP): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/processos-sancionadores/processos-sancionadores.pdf
