---
dataset:
  id: multas
  fonte: anp
  titulo: Multas aplicadas com vencimento a partir de 2016
  resumo: 'Relação anual das multas aplicadas pela ANP em ações de fiscalização, com vencimento a partir de 2016: processo, autuado, vencimento, valor aplicado e valor pago.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/multas-aplicadas-com-vencimento-a-partir-de-2016
  licenca: Creative Commons Atribuição (CC BY), segundo os metadados do conjunto («Licença de uso»); o rodapé do portal da ANP declara, para o conteúdo do site, a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual (metadados da ANP), com extração ao fim de cada exercício
  cobertura:
    inicio: '2016'
    fim: '2025'
  unidade: uma multa aplicada (um processo, com o autuado e o valor), por ano de vencimento
  granularidade:
    espacial: federal (unidade da ANP e UF na sigla da superintendência; sem município do autuado)
    temporal: ano de vencimento da multa (um arquivo por ano, e um para 2016 a 2019); status na data da extração
  formato_bruto: CSV anual (a ANP também publica XLSX), separador ponto e vírgula, UTF-8 com BOM ou CP850, com linhas de título antes do cabeçalho
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 17
  unidades_de_medida:
    Valor da Multa Aplicada: R$ (reais)
    Valor Total Pago (*) (**): R$ (reais)
    ' Valor  da Multa Aplicada ': R$ (reais)
    ' Valor Total Pago (*) (**)  ': R$ (reais)
    Valor  da Multa Aplicada: R$ (reais)
    'Valor Total Pago (*) (**) ': R$ (reais)
    Valor da Multa: R$ (reais)
    Valor Total Pago: R$ (reais)
    ' Valor da Multa ': R$ (reais)
    ' Valor Total Pago ': R$ (reais)
  dados_pessoais:
  - coluna: CNPJ/CPF
    categoria: CNPJ de pessoa jurídica e CPF de pessoa física (11 dígitos) do autuado
  - coluna: Razão Social
    categoria: razão social de empresa e nome de pessoa física autuada
  eras:
  - desde: '2016'
    mudanca: 10 colunas, com `Auto de Infração`, `Data Transito Julgado` e valores sem `R$` (`33000,00`); o arquivo 2016-2019 reúne quatro anos de vencimento
  - desde: '2020'
    mudanca: valores com `R$` e pontos de milhar (`R$ 5.000,00`); os nomes das colunas de valor ganham espaços no início e no fim
  - desde: '2022'
    mudanca: '`Número do DUF` substitui `Auto de Infração`; `Valor da Multa Aplicada` passa a `Valor da Multa` e `Valor Total Pago (*) (**)` a `Valor Total Pago`'
  - desde: '2023'
    mudanca: '9 colunas: sai `Data Transito Julgado`; `Vencimento` passa a `Vencimento da Multa`; valores `R$ -` para pagamento zero'
  - desde: '2024'
    mudanca: volta o nome `Vencimento`; os valores perdem o `R$` (`369000,00`); entra uma coluna sem nome com `SIM` em parte das linhas
  - desde: '2025'
    mudanca: '`Vencimento` passa a `Vencimento GRM`; a coluna sem nome desaparece'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Multas aplicadas com vencimento a partir de 2016

## Resumo

Relação das multas aplicadas administrativamente pela ANP, decorrentes de autuações em ações de fiscalização, com vencimento a partir de 2016. Cada linha é uma multa, com o status do processo, a unidade da ANP, o número do processo e do auto de infração ou DUF, o autuado (CNPJ ou CPF e razão social), o vencimento, o valor aplicado e o valor total pago. A fonte esclarece que o status e os demais dados representam a situação no momento da extração, feita anualmente ao final de cada exercício (as datas reais de extração variam, ver Origem). Há um arquivo por ano de vencimento (e um para 2016 a 2019).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/multas` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/multas-aplicadas-com-vencimento-a-partir-de-2016 |
| Licença | Creative Commons Atribuição (CC BY), segundo os metadados do conjunto («Licença de uso»); o rodapé do portal da ANP declara, para o conteúdo do site, a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual (metadados da ANP), com extração ao fim de cada exercício |
| Cobertura | 2016 a 2025 |
| Unidade (uma linha) | uma multa aplicada (um processo, com o autuado e o valor), por ano de vencimento |
| Granularidade | espacial: federal (unidade da ANP e UF na sigla da superintendência; sem município do autuado); temporal: ano de vencimento da multa (um arquivo por ano, e um para 2016 a 2019); status na data da extração |
| Formato bruto | CSV anual (a ANP também publica XLSX), separador ponto e vírgula, UTF-8 com BOM ou CP850, com linhas de título antes do cabeçalho |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 17 |
| Unidades de medida | `Valor da Multa Aplicada`: R$ (reais); `Valor Total Pago (*) (**)`: R$ (reais); ` Valor  da Multa Aplicada `: R$ (reais); ` Valor Total Pago (*) (**)  `: R$ (reais); `Valor  da Multa Aplicada`: R$ (reais); `Valor Total Pago (*) (**) `: R$ (reais); `Valor da Multa`: R$ (reais); `Valor Total Pago`: R$ (reais); ` Valor da Multa `: R$ (reais); ` Valor Total Pago `: R$ (reais) |
| Dados pessoais | `CNPJ/CPF` (CNPJ de pessoa jurídica e CPF de pessoa física (11 dígitos) do autuado); `Razão Social` (razão social de empresa e nome de pessoa física autuada) |
| Eras | 2016: 10 colunas, com `Auto de Infração`, `Data Transito Julgado` e valores sem `R$` (`33000,00`); o arquivo 2016-2019 reúne quatro anos de vencimento; 2020: valores com `R$` e pontos de milhar (`R$ 5.000,00`); os nomes das colunas de valor ganham espaços no início e no fim; 2022: `Número do DUF` substitui `Auto de Infração`; `Valor da Multa Aplicada` passa a `Valor da Multa` e `Valor Total Pago (*) (**)` a `Valor Total Pago`; 2023: 9 colunas: sai `Data Transito Julgado`; `Vencimento` passa a `Vencimento da Multa`; valores `R$ -` para pagamento zero; 2024: volta o nome `Vencimento`; os valores perdem o `R$` (`369000,00`); entra uma coluna sem nome com `SIM` em parte das linhas; 2025: `Vencimento` passa a `Vencimento GRM`; a coluna sem nome desaparece |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Centro de Gestão de Créditos (CGC); contato cobranca@anp.gov.br (metadados da ANP); os arquivos citam o Sistema de Controle de Multas (SICOM) como fonte. A extração é anual, e o status do processo representa a situação no momento dela.
- **Catálogo do fetcher:** 7 arquivos: `multas-2016-2019`, `multas-2020`, `multas-2021`, `multas-2022`, `multas-2023`, `multas-2024` e `multas-2025` (conferido em 2026-11-15). O arquivo de 2021 é publicado como `multas-2021-junho22.xlsx` mas é um CSV em texto, e o fetcher o grava como `.csv`; a página oficial também publica as versões em Excel de 2024 e 2025.
- **Cobertura:** os metadados dão início em 01/01/2016 e cobertura federal; o arquivo de 2025 é o último da página (conferido em 2026-11-15).
- **Preâmbulo e codificação:** cada arquivo começa com linhas de título (órgão, «RELAÇÃO DE MULTAS APLICADAS EM AAAA», data de extração e a fonte, «Sistema de Controle de Multas - SICOM») antes do cabeçalho. Os arquivos de 2016-2019 a 2022 e 2024 são UTF-8 com BOM; os de 2023 e 2025 estão em CP850 (DOS), e o conversor acha o cabeçalho e lê o texto sem corrupção (conferido na amostra: `PETRÓLEO` e demais acentos corretos).
- **Datas de extração do relatório** (do preâmbulo): 2016-2019, 06/02/2020; 2020, fevereiro/2021; 2021, junho/2022; 2022, abril/2022; 2023, junho/2024; 2024, março/2025; 2025, janeiro/2026. O arquivo de 2022 foi extraído em abril de 2022, antes do fim do ano de vencimento, e portanto não reflete a situação do exercício completo.

## Conteúdo

Os sete arquivos do catálogo, todos no lake:

| Arquivo | Linhas | Colunas | Vencimentos | Observação |
|---|---|---|---|---|
| `multas-2016-2019` | 16.440 | 10 | 2016 a 2019 | formato de valor `33000,00`; a coluna de vencimento tem espaço no fim do nome |
| `multas-2020` | 2.026 | 10 | 2020 | valores como `R$ 5.000,00`; nomes de coluna de valor com espaços no início e no fim |
| `multas-2021` | 4.976 | 10 | 2021 | a URL termina em `.xlsx`, mas o arquivo é um CSV em texto (gravado como `.csv`) |
| `multas-2022` | 2.996 | 10 | 2022 | `Número do DUF` no lugar de `Auto de Infração`; `Valor da Multa` e `Valor Total Pago` |
| `multas-2023` | 3.074 | 9 | 2023 | sem `Data Transito Julgado`; `Vencimento da Multa`; valores `R$ -` quando nada foi pago |
| `multas-2024` | 3.004 | 10 | 2024 | sem `Data Transito Julgado`; coluna sem nome (`coluna_10`); valores sem `R$` |
| `multas-2025` | 3.395 | 9 | 2025 | sem `Data Transito Julgado`; `Vencimento GRM`; valores sem `R$` |

- **O que é uma linha:** uma multa. `Número do Processo` quase não repete (16.390 distintos em 16.440 linhas em 2016-2019; 3.386 em 3.395 em 2025), porque um processo pode ter mais de uma multa; por isso não há chave.
- **Status:** em 2025, 1.583 processos pagos, 827 encaminhados à dívida ativa ou execução fiscal, 469 aguardando análise de recurso e 351 aguardando pagamento (os quatro maiores status).
- **Pessoas físicas:** o campo `CNPJ/CPF` traz CPF (11 dígitos) em 150 linhas de 2016-2019 e 20 de 2025.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | 7 arquivos, de 9 a 10 colunas |

## Variáveis

Os metadados da ANP para este conjunto não trazem dicionário de colunas (só a ficha geral: título, descrição, licença, periodicidade). As descrições abaixo são deduzidas do nome das colunas e dos valores observados, e dizem isso quando a dedução é incerta. Os nomes mudam entre os arquivos (ver as eras): o lake mantém uma coluna para cada grafia, e a coluna *Arquivos* diz em quais arquivos ela aparece. O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Status Processo` | `Status Processo` | texto | Situação do processo da multa no momento da extração anual (por exemplo, `Processo Pago`, `Aguardando Pagamento`, `Aguardando análise de recurso`, `Encaminhado para Dívida Ativa/Execução Fiscal`, `Parcelamento em andamento`); a grafia varia entre arquivos | — | — | `multas-2016-2019`, `multas-2020`, `multas-2021` e mais 4 |
| `Superintendência` | `Superintendência` | texto | Sigla da unidade da ANP responsável pelo processo, com a unidade e a UF (por exemplo, `SFI-BA`, `SSO-RJ`, `PRG-DF`); `SFI - RJ` e `SFI-RJ` aparecem como grafias diferentes | — | — | `multas-2016-2019`, `multas-2020`, `multas-2021` e mais 4 |
| `Número do Processo` | `Número do Processo` | texto | Número do processo administrativo, sem pontuação (15 dígitos) | — | — | `multas-2016-2019`, `multas-2020`, `multas-2021` e mais 4 |
| `Auto de Infração` | `Auto de Infração` | texto | Número do auto de infração (arquivos de 2016 a 2021); pode trazer dois números (`513570/485308`); descrição deduzida do nome e dos valores observados | — | — | `multas-2016-2019`, `multas-2020`, `multas-2021` |
| `CNPJ/CPF` | `CNPJ/CPF` | texto | CNPJ (14 dígitos) ou CPF (11 dígitos) do autuado, só dígitos; o CPF identifica pessoa física | — | — | `multas-2016-2019`, `multas-2020`, `multas-2021` e mais 4 |
| `Razão Social` | `Razão Social` | texto | Razão social do autuado, ou nome da pessoa física quando o documento é CPF | — | — | `multas-2016-2019`, `multas-2020`, `multas-2021` e mais 4 |
| `Data Transito Julgado` | `Data Transito Julgado` | texto | Data do trânsito em julgado da decisão administrativa (dd/mm/aaaa); vazia enquanto não houve; presente só nos arquivos de 2016 a 2022; descrição deduzida do nome | — | — | `multas-2016-2019`, `multas-2020`, `multas-2021` e mais 1 |
| `Vencimento ` | `Vencimento ` | texto | Data de vencimento da multa (dd/mm/aaaa); no arquivo de 2016-2019 abrange vencimentos de 2016 a 2019, e nos demais, o ano do arquivo (o nome da coluna tem espaços no início ou no fim) | — | — | `multas-2016-2019` |
| `Valor da Multa Aplicada` | `Valor da Multa Aplicada` | texto | Valor da multa aplicada, em reais (arquivos de 2016 a 2021); o formato varia: `33000,00` (2016-2019) e `R$ 5.000,00` (2020 e 2021) | — | — | `multas-2016-2019` |
| `Valor Total Pago (*) (**)` | `Valor Total Pago (*) (**)` | texto | Valor total pago da multa, em reais; as marcas (*) e (**) remetem a notas que o CSV não traz; pode ser maior que a multa (juros e correção) ou `R$ -` quando nada foi pago (arquivo de 2023) | — | — | `multas-2016-2019` |
| `Vencimento` | `Vencimento` | texto | Data de vencimento da multa (dd/mm/aaaa); no arquivo de 2016-2019 abrange vencimentos de 2016 a 2019, e nos demais, o ano do arquivo | — | — | `multas-2020`, `multas-2021`, `multas-2022` e mais 1 |
| ` Valor  da Multa Aplicada ` | ` Valor  da Multa Aplicada ` | texto | Valor da multa aplicada, em reais (arquivos de 2016 a 2021); o formato varia: `33000,00` (2016-2019) e `R$ 5.000,00` (2020 e 2021) (o nome da coluna tem espaços no início ou no fim) | — | — | `multas-2020` |
| ` Valor Total Pago (*) (**)  ` | ` Valor Total Pago (*) (**)  ` | texto | Valor total pago da multa, em reais; as marcas (*) e (**) remetem a notas que o CSV não traz; pode ser maior que a multa (juros e correção) ou `R$ -` quando nada foi pago (arquivo de 2023) (o nome da coluna tem espaços no início ou no fim) | — | — | `multas-2020` |
| `Valor  da Multa Aplicada` | `Valor  da Multa Aplicada` | texto | Valor da multa aplicada, em reais (arquivos de 2016 a 2021); o formato varia: `33000,00` (2016-2019) e `R$ 5.000,00` (2020 e 2021) | — | — | `multas-2021` |
| `Valor Total Pago (*) (**) ` | `Valor Total Pago (*) (**) ` | texto | Valor total pago da multa, em reais; as marcas (*) e (**) remetem a notas que o CSV não traz; pode ser maior que a multa (juros e correção) ou `R$ -` quando nada foi pago (arquivo de 2023) (o nome da coluna tem espaços no início ou no fim) | — | — | `multas-2021` |
| `Número do DUF` | `Número do DUF` | texto | Número do DUF (sigla não expandida na fonte), que substitui `Auto de Infração` a partir do arquivo de 2022; pode trazer mais de um número (`578900 e 587648`, `608863/608661`) ou código de outro formato (`CA.1027/2022`); descrição deduzida do nome e dos valores observados | — | — | `multas-2022`, `multas-2023`, `multas-2024` e mais 1 |
| `Valor da Multa` | `Valor da Multa` | texto | Valor da multa aplicada, em reais (arquivos de 2022 em diante); o formato varia: `R$ 5.000,00` (2022 e 2023) e `369000,00` (2024 e 2025) | — | — | `multas-2022`, `multas-2024`, `multas-2025` |
| `Valor Total Pago` | `Valor Total Pago` | texto | Valor total pago da multa, em reais, nos arquivos de 2022 em diante; pode ser maior que a multa aplicada (juros e correção); o formato segue o da coluna de valor da multa | — | — | `multas-2022`, `multas-2024`, `multas-2025` |
| `Vencimento da Multa` | `Vencimento da Multa` | texto | Data de vencimento da multa (dd/mm/aaaa), nome da coluna no arquivo de 2023 | — | — | `multas-2023` |
| ` Valor da Multa ` | ` Valor da Multa ` | texto | Valor da multa aplicada, em reais (arquivos de 2022 em diante); o formato varia: `R$ 5.000,00` (2022 e 2023) e `369000,00` (2024 e 2025) (o nome da coluna tem espaços no início ou no fim) | — | — | `multas-2023` |
| ` Valor Total Pago ` | ` Valor Total Pago ` | texto | Valor total pago da multa, em reais, nos arquivos de 2022 em diante; pode ser maior que a multa aplicada (juros e correção); o formato segue o da coluna de valor da multa (o nome da coluna tem espaços no início ou no fim) | — | — | `multas-2023` |
| `coluna_10` | `coluna_10` | texto | Coluna sem nome no cabeçalho do arquivo de 2024 (o conversor a chamou `coluna_10`): traz `SIM` em 34 das 3.004 linhas (todas com `Processo Pago` nas duas primeiras conferidas); significado não informado pela fonte | — | — | `multas-2024` |
| `Vencimento GRM` | `Vencimento GRM` | texto | Data de vencimento da multa (dd/mm/aaaa) segundo a GRM (sigla não expandida na fonte), nome da coluna no arquivo de 2025; descrição deduzida do nome | — | — | `multas-2025` |

## No lake

- Dataset `anp/multas`, sem partições; um Parquet por arquivo, `multas-2016-2019.parquet`, `multas-2020.parquet` e assim por diante até `multas-2025.parquet`. Todas as colunas são texto.
- Os cabeçalhos mantêm os espaços do original: `Vencimento ` (2016-2019), ` Valor  da Multa Aplicada ` e ` Valor Total Pago (*) (**)  ` (2020), `Valor  da Multa Aplicada` e `Valor Total Pago (*) (**) ` (2021), ` Valor da Multa ` e ` Valor Total Pago ` (2023).
- A coluna sem nome do arquivo de 2024 é gravada como `coluna_10`.

## Cuidados de uso

- **Cada arquivo é uma fotografia do status na data de extração do relatório.** O mesmo processo pode aparecer em arquivos de anos diferentes quando tem multas em anos diferentes, mas o status de cada arquivo vale na data da sua extração, não é uma série.
- **Colunas diferentes entre anos.** Para empilhar os arquivos, mapeie `Auto de Infração`/`Número do DUF`, `Vencimento`/`Vencimento da Multa`/`Vencimento GRM`, `Valor da Multa Aplicada`/`Valor da Multa` e `Valor Total Pago (*) (**)`/`Valor Total Pago`. A coluna `Data Transito Julgado` existe só de 2016 a 2022.
- **Valores monetários em texto, com três formatos:** `33000,00`, `R$ 5.000,00` e `R$ -` (pagamento zero). Remova `R$` e pontos, troque a vírgula e trate `-` como zero antes de somar.
- **Valor pago pode superar a multa** (juros e correção): não calcule «percentual pago» sem ver a nota (*) (**) do arquivo original, que o CSV não traz.
- **Nomes de coluna com espaços** no início, no fim ou em dobro (` Valor  da Multa Aplicada `); cite exatamente ou renomeie.
- **`CNPJ/CPF` mistura pessoa jurídica e pessoa física** (CPF, 11 dígitos, 150 linhas em 2016-2019). Os CPFs e os nomes das pessoas físicas autuadas são dado pessoal; trate-os conforme a LGPD ao publicar.
- **Status com grafias diferentes** (`Dívida Ativa / Execução Fiscal` e `Encaminhado para Dívida Ativa/Execução Fiscal`; `Parcelamento em andamento` e `em Andamento`); normalize antes de agrupar.
- **A multa aplicada não prova a infração:** a ANP publica as multas, com status, mas o autuado pode recorrer.

## Exemplos

Número de multas, soma aplicada e soma paga em 2025, convertendo os valores (que neste arquivo vêm como `369000,00`):

```python
import duckdb

duckdb.sql("""
    SELECT "Status Processo" AS status, count(*) AS multas,
           round(sum(replace("Valor da Multa", ',', '.')::DOUBLE) / 1e6, 1) AS aplicado_milhoes_rs,
           round(sum(replace("Valor Total Pago", ',', '.')::DOUBLE) / 1e6, 1) AS pago_milhoes_rs
    FROM read_parquet('lake/anp/multas/multas-2025.parquet')
    GROUP BY ALL
    ORDER BY multas DESC
""").show()
```

## Referências

- Dados abertos da ANP, Multas aplicadas com vencimento a partir de 2016: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/multas-aplicadas-com-vencimento-a-partir-de-2016
- Metadados do conjunto: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/mav/metadados-multas-aplicadas-2016a2019.pdf
