---
dataset:
  id: plataformas-operacao
  fonte: anp
  titulo: Lista de plataformas em operação
  resumo: Cadastro das 78 plataformas de produção em operação no Brasil, com campos atendidos, operador, tipo, lâmina d'água, início de operação, coordenadas e capacidades.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo o metadado da ANP; cada arquivo é um retrato do cadastro, sem histórico
  cobertura:
    inicio: '1966'
    fim: em-curso
  unidade: uma plataforma (instalação) de produção em operação
  granularidade:
    espacial: plataforma, com bacia, campos atendidos e coordenadas (graus decimais, SIRGAS2000)
    temporal: 'sem série temporal: `ANO DE INÍCIO DE OPERAÇÃO` (de 1966 a 2026)'
  formato_bruto: CSV em UTF-8 com BOM, separado por vírgula; os nomes das colunas vêm entre colchetes
  lake:
    estado: convertido
    particoes: []
    chave:
    - '[SIGLA DA INSTALAÇÃO]'
    colunas: 13
  unidades_de_medida:
    '[LÂMINA D''ÁGUA (m)]': m
    '[ANO DE INÍCIO DE OPERAÇÃO]': ano (AAAA)
    '[LATITUDE]': graus decimais (SIRGAS2000)
    '[LONGITUDE]': graus decimais (SIRGAS2000)
    '[CAPACIDADE DE PRODUÇÃO DE PETRÓLEO (bbl/d)]': bbl/dia
    '[CAPACIDADE DE PRODUÇÃO DE GÁS NATURAL (Mil m³/d)]': mil m³/dia
  dados_pessoais:
  - coluna: '[OPERADOR]'
    categoria: razão social de empresa operadora (pessoa jurídica)
  eras:
  - desde: '2026'
    mudanca: layout da coleta de 2026-11-15 (13 colunas, com cabeçalho entre colchetes); só a versão corrente é guardada
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Lista de plataformas em operação

## Resumo

Relação das plataformas em atividade no território nacional, com os campos que cada uma atende, a bacia, o operador, o tipo (FPSO, plataforma fixa, semissubmersível, TLP), a lâmina d'água, o sistema de escoamento do óleo, o ano de início de operação, as coordenadas (SIRGAS2000) e as capacidades de processamento de petróleo e de gás natural. É um retrato do cadastro na coleta, substituído a cada atualização.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/plataformas-operacao` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo o metadado da ANP; cada arquivo é um retrato do cadastro, sem histórico |
| Cobertura | 1966 a em-curso |
| Unidade (uma linha) | uma plataforma (instalação) de produção em operação |
| Granularidade | espacial: plataforma, com bacia, campos atendidos e coordenadas (graus decimais, SIRGAS2000); temporal: sem série temporal: `ANO DE INÍCIO DE OPERAÇÃO` (de 1966 a 2026) |
| Formato bruto | CSV em UTF-8 com BOM, separado por vírgula; os nomes das colunas vêm entre colchetes |
| Estado no lake | convertido |
| Partições | — |
| Chave | `[SIGLA DA INSTALAÇÃO]` |
| Colunas | 13 |
| Unidades de medida | `[LÂMINA D'ÁGUA (m)]`: m; `[ANO DE INÍCIO DE OPERAÇÃO]`: ano (AAAA); `[LATITUDE]`: graus decimais (SIRGAS2000); `[LONGITUDE]`: graus decimais (SIRGAS2000); `[CAPACIDADE DE PRODUÇÃO DE PETRÓLEO (bbl/d)]`: bbl/dia; `[CAPACIDADE DE PRODUÇÃO DE GÁS NATURAL (Mil m³/d)]`: mil m³/dia |
| Dados pessoais | `[OPERADOR]` (razão social de empresa operadora (pessoa jurídica)) |
| Eras | 2026: layout da coleta de 2026-11-15 (13 colunas, com cabeçalho entre colchetes); só a versão corrente é guardada |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Um CSV de 15.195 bytes: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/lpo/dados-abertos-plataformas-operacao.csv`, coletado em 2026-11-15.
- Fonte do dado, segundo o metadado "Plataformas em Operação" (DOCX, criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; atualização mensal; contato demandas_sdp@anp.gov.br.
- No bruto: `plataformas-operacao/plataformas-operacao@AAAAMMDD.csv`, com o sufixo da data da coleta.

## Conteúdo

- **78 plataformas** na amostra (todas as linhas do arquivo), em 5 bacias, com 13 operadores, em 48 combinações distintas de campos. Cinco classificações, entre elas `Floating Production Storage Offloading - FPSO`, `Plataforma Fixa - Jaqueta` e `Semissubmersível - SS`.
- **Capacidades.** 62 plataformas têm capacidade de petróleo (bbl/dia) e 63 têm capacidade de gás natural (mil m³/dia); o restante vem em branco.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `plataformas-operacao` (13) |

## Variáveis

As descrições vêm do metadado "Plataformas em Operação" (DOCX da ANP, criado em junho de 2026). Os nomes das colunas no lake mantêm os colchetes do cabeçalho do CSV; a coluna *Na fonte* repete o nome exato.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `[SIGLA DA INSTALAÇÃO]` | `[SIGLA DA INSTALAÇÃO]` | texto | Sigla da plataforma. | — | — |
| `[NOME DA INSTALAÇÃO]` | `[NOME DA INSTALAÇÃO]` | texto | Nome da plataforma. | — | — |
| `[CAMPOS]` | `[CAMPOS]` | texto | Campos atendidos pela plataforma (texto com `/` entre os nomes quando há mais de um). | — | — |
| `[BACIA]` | `[BACIA]` | texto | Bacia em que está localizada a plataforma. | — | — |
| `[OPERADOR]` | `[OPERADOR]` | texto | Operador do campo integrante da plataforma (razão social). | — | — |
| `[CLASSIFICAÇÃO]` | `[CLASSIFICAÇÃO]` | texto | Tipo da instalação (FPSO, FSO, fixa, semissubmersível, TLP), por extenso, como `Floating Production Storage Offloading - FPSO` e `Plataforma Fixa - Jaqueta`. | — | — |
| `[LÂMINA D'ÁGUA (m)]` | `[LÂMINA D'ÁGUA (m)]` | texto | Lâmina d'água aproximada na locação da plataforma, em metros (texto; `0` em instalações fixas rasas). | — | — |
| `[SISTEMA DE ESCOAMENTO]` | `[SISTEMA DE ESCOAMENTO]` | texto | Forma pela qual a plataforma escoa a produção de óleo: `Duto`, `Navio Aliviador` ou `Navio Aliviador e Duto`. | — | — |
| `[ANO DE INÍCIO DE OPERAÇÃO]` | `[ANO DE INÍCIO DE OPERAÇÃO]` | texto | Ano em que a plataforma iniciou sua operação (AAAA). | — | — |
| `[LATITUDE]` | `[LATITUDE]` | texto | Latitude da plataforma em graus decimais, com vírgula decimal (`-24,59253250`); o metadado diz `-GG:MM:SS,SSS`, mas o arquivo traz graus decimais. Datum SIRGAS2000. | — | — |
| `[LONGITUDE]` | `[LONGITUDE]` | texto | Longitude da plataforma em graus decimais, com vírgula decimal. Datum SIRGAS2000. | — | — |
| `[CAPACIDADE DE PRODUÇÃO DE PETRÓLEO (bbl/d)]` | `[CAPACIDADE DE PRODUÇÃO DE PETRÓLEO (bbl/d)]` | texto | Capacidade de processamento de petróleo da plataforma, em barris por dia (vazia em 16 plataformas). | — | — |
| `[CAPACIDADE DE PRODUÇÃO DE GÁS NATURAL (Mil m³/d)]` | `[CAPACIDADE DE PRODUÇÃO DE GÁS NATURAL (Mil m³/d)]` | texto | Capacidade de processamento de gás natural da plataforma, em mil m³ por dia (vazia em 15 plataformas). | — | — |

## No lake

- Dataset `anp/plataformas-operacao`, sem partição: um Parquet, `plataformas-operacao.parquet`.
- Todas as colunas são texto; o cabeçalho é mantido com os colchetes (`[SIGLA DA INSTALAÇÃO]`).

## Cuidados de uso

- **Colchetes nos nomes.** Todas as 13 colunas têm colchetes (`[BACIA]`, `[LATITUDE]`, ...), e as aspas duplas do SQL são necessárias (`"[BACIA]"`).
- **Coordenadas em graus decimais com vírgula.** O metadado diz `-GG:MM:SS,SSS`, mas o arquivo traz graus decimais com vírgula (`-24,59253250`); troque a vírgula por ponto antes do cast.
- **Capacidade em branco.** 16 plataformas sem capacidade de petróleo e 15 sem capacidade de gás natural: ausente não é zero.
- **Nome longo de campo.** `[CAMPOS]` junta campos com `/` e inclui áreas de campos (`AnC_...`); para ligar a `campos-producao`, separe a lista.
- **Chave.** `[SIGLA DA INSTALAÇÃO]` é única nas 78 linhas da amostra (78 siglas distintas), e `[NOME DA INSTALAÇÃO]` também.
- **Retrato sem histórico.** O arquivo lista só as plataformas em operação na data da coleta; uma plataforma desativada deixa de aparecer.
- **Dados pessoais.** Não há: instalações e razão social de operadoras.

## Exemplos

Número de plataformas e capacidade de petróleo somada por bacia e tipo de instalação (colunas em texto; capacidade vazia fica fora da soma):

```python
import duckdb

duckdb.sql("""
    SELECT "[BACIA]" AS bacia, "[CLASSIFICAÇÃO]" AS tipo, count(*) AS plataformas,
           sum(try_cast("[CAPACIDADE DE PRODUÇÃO DE PETRÓLEO (bbl/d)]" AS DOUBLE)) AS capacidade_bbl_d
    FROM read_parquet('lake/anp/plataformas-operacao/plataformas-operacao.parquet')
    GROUP BY ALL
    ORDER BY capacidade_bbl_d DESC NULLS LAST
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos), lista de plataformas em operação: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadado "Plataformas em Operação" (DOCX): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/lpo/metadadosplataformasoperacao.docx
