---
dataset:
  id: fiscalizacao
  fonte: anp
  titulo: Ações de fiscalização do abastecimento
  resumo: 'Documentos de fiscalização da ANP no abastecimento nacional de combustíveis desde 1998: local, agente fiscalizado, segmento, tipo de documento e resultado.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acoes-de-fiscalizacao
  licenca: Os metadados do conjunto listam, no campo de licença, as opções «Creative Commons Atribuição ou Creative Commons CCZero ou Licença Aberta para Bases de Dados (ODbL) ou Licença e Dedicação ao Domínio Público (PDDL) do Open Data Commons» sem indicar uma; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (metadados da ANP), com prazo de dois meses entre o mês da fiscalização e o da publicação, segundo a página oficial
  cobertura:
    inicio: 1998-01
    fim: em-curso
  unidade: um resultado de um documento de fiscalização (o mesmo número de documento repete quando há mais de um resultado)
  granularidade:
    espacial: 'local fiscalizado: UF, município, bairro e endereço (sem coordenadas)'
    temporal: data do documento de fiscalização (`DATA DO DF`), dia a dia, de 1998-01-27 a 2026-10-04 na amostra
  formato_bruto: duas planilhas XLSX (1998 a 2018 e 2019 em diante), uma aba de dados cada
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 11
  unidades_de_medida:
    Número do Documento: identificador (sem unidade)
  dados_pessoais:
  - coluna: CNPJ/CPF
    categoria: CNPJ de pessoa jurídica e CPF de pessoa física (11 dígitos) do agente fiscalizado
  - coluna: Agente Econômico
    categoria: razão social de empresa fiscalizada
  - coluna: Bairro
    categoria: endereço do estabelecimento fiscalizado (que pode ser residência de pessoa física em casos de CPF; nesses o endereço vem vazio)
  - coluna: ENDEREÇO
    categoria: endereço do estabelecimento fiscalizado (que pode ser residência de pessoa física em casos de CPF; nesses o endereço vem vazio)
  eras:
  - desde: '1998'
    mudanca: 'arquivo de 1998 a 2018 (`fisc-1998-2018`): sem o procedimento `Boletim de Fiscalização`; `Segmento Fiscalizado` vazio em 32.777 linhas (8%)'
  - desde: '2019'
    mudanca: 'arquivo de 2019 em diante (`fisc-2019`): entra o procedimento `Boletim de Fiscalização` (59.989 linhas) e o segmento `Agente Não Regulado` (3.720 linhas); os segmentos distintos passam de 21 para 36; `Segmento Fiscalizado` quase sempre preenchido (243.905 de 244.247)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Ações de fiscalização do abastecimento

## Resumo

Dados brutos do painel dinâmico da fiscalização do abastecimento da Superintendência de Fiscalização do Abastecimento (SFI) da ANP: as ações de fiscalização nos diversos segmentos do abastecimento nacional de combustíveis (revendas de combustíveis e de GLP, distribuidores, TRR e outros). Cada linha traz o local (UF, município, bairro e endereço), o agente econômico fiscalizado (CNPJ ou CPF e nome), o segmento, a data e o número do documento de fiscalização, o procedimento lavrado (auto de infração, notificação, coleta de amostra, boletim de fiscalização e outros) e o resultado. A ANP avisa que os agentes autuados têm direito ao contraditório e à ampla defesa: só após o julgamento definitivo do processo sancionador se confirma a infração.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/fiscalizacao` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acoes-de-fiscalizacao |
| Licença | Os metadados do conjunto listam, no campo de licença, as opções «Creative Commons Atribuição ou Creative Commons CCZero ou Licença Aberta para Bases de Dados (ODbL) ou Licença e Dedicação ao Domínio Público (PDDL) do Open Data Commons» sem indicar uma; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (metadados da ANP), com prazo de dois meses entre o mês da fiscalização e o da publicação, segundo a página oficial |
| Cobertura | 1998-01 a em-curso |
| Unidade (uma linha) | um resultado de um documento de fiscalização (o mesmo número de documento repete quando há mais de um resultado) |
| Granularidade | espacial: local fiscalizado: UF, município, bairro e endereço (sem coordenadas); temporal: data do documento de fiscalização (`DATA DO DF`), dia a dia, de 1998-01-27 a 2026-10-04 na amostra |
| Formato bruto | duas planilhas XLSX (1998 a 2018 e 2019 em diante), uma aba de dados cada |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 11 |
| Unidades de medida | `Número do Documento`: identificador (sem unidade) |
| Dados pessoais | `CNPJ/CPF` (CNPJ de pessoa jurídica e CPF de pessoa física (11 dígitos) do agente fiscalizado); `Agente Econômico` (razão social de empresa fiscalizada); `Bairro` (endereço do estabelecimento fiscalizado (que pode ser residência de pessoa física em casos de CPF; nesses o endereço vem vazio)); `ENDEREÇO` (endereço do estabelecimento fiscalizado (que pode ser residência de pessoa física em casos de CPF; nesses o endereço vem vazio)) |
| Eras | 1998: arquivo de 1998 a 2018 (`fisc-1998-2018`): sem o procedimento `Boletim de Fiscalização`; `Segmento Fiscalizado` vazio em 32.777 linhas (8%); 2019: arquivo de 2019 em diante (`fisc-2019`): entra o procedimento `Boletim de Fiscalização` (59.989 linhas) e o segmento `Agente Não Regulado` (3.720 linhas); os segmentos distintos passam de 21 para 36; `Segmento Fiscalizado` quase sempre preenchido (243.905 de 244.247) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Fiscalização do Abastecimento (SFI); os dados vêm do Sistema de Gestão das Ações de Fiscalização (SIGAF) e são publicados como os dados brutos do painel dinâmico da fiscalização do abastecimento (metadados da ANP). Contato: sfi_cdex@anp.gov.br.
- **Catálogo do fetcher:** 2 arquivos: `fisc-1998-2018` (`dados-fisc-1998-2018.xlsx`) e `fisc-2019` (`dados-fisc-a-partir-2019.xlsx`), ambos em endereços do painel dinâmico (conferido em 2026-11-15). A página oficial rotula o segundo como «2019 a 2025», mas o arquivo da amostra tem datas até 2026-10-04 (atualizado em 20/10/2026 segundo a página).
- **Atualização:** mensal, com prazo de dois meses entre o mês da fiscalização e o da publicação, para cumprir exigências legais e operacionais (página oficial).
- **Metadados:** o documento da ANP descreve o conjunto, mas não traz dicionário de colunas; as descrições abaixo são deduzidas do nome das colunas e dos valores observados.

## Conteúdo

| Arquivo no lake | Período das datas | Linhas |
|---|---|---|
| `fisc-1998-2018` | 1998-01-27 a 2018-12-31 | 403.977 (225.923 números de documento distintos) |
| `fisc-2019` | 2019-01-02 a 2026-10-04 | 244.247 (141.290 números de documento distintos) |

- **Procedimentos mais frequentes em 1998-2018:** auto de infração (147.300), termo de coleta de amostra (94.566), notificação (87.013) e medida reparadora de conduta (25.630). De 2019 em diante: boletim de fiscalização (59.989), notificação (51.646), auto de infração (49.278) e medida reparadora de conduta (36.773).
- **Segmentos:** revenda de combustíveis lidera nos dois arquivos (282.194 e 190.282 linhas), seguida de revenda de GLP (57.918 e 30.073) e distribuidor de combustíveis líquidos (16.850 e 7.743).
- **Pessoas físicas:** o `CNPJ/CPF` tem 11 dígitos (CPF) em 6.366 linhas de 1998-2018 e 1.294 de 2019 em diante; nessas linhas `Agente Econômico` e `ENDEREÇO` vêm vazios.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `fisc-1998-2018` (11); `fisc-2019` (11) |

## Variáveis

Os metadados da ANP para este conjunto não trazem dicionário de colunas; as descrições abaixo são deduzidas do nome e dos valores observados. As duas planilhas têm as mesmas 11 colunas, com os mesmos nomes. `DATA DO DF` vem como data e `Número do Documento` como inteiro; as demais colunas são texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `UF` | `UF` | texto | Sigla da unidade da federação onde a fiscalização foi feita | — | — | `fisc-1998-2018`, `fisc-2019` |
| `Município` | `Município` | texto | Município do local fiscalizado (em maiúsculas; a grafia acentuada varia) | — | — | `fisc-1998-2018`, `fisc-2019` |
| `Bairro` | `Bairro` | texto | Bairro do local fiscalizado; vazio em parte das linhas | — | — | `fisc-1998-2018`, `fisc-2019` |
| `ENDEREÇO` | `ENDEREÇO` | texto | Endereço do local fiscalizado (logradouro e número em texto livre); vazio quando o autuado é pessoa física (CPF) | — | — | `fisc-1998-2018`, `fisc-2019` |
| `CNPJ/CPF` | `CNPJ/CPF` | texto | CNPJ (14 dígitos) ou CPF (11 dígitos) do agente econômico fiscalizado, só dígitos; há valores curtos de 1 dígito, que são marcadores sem documento (309 linhas em 1998-2018 e 5 em 2019 em diante) | — | — | `fisc-1998-2018`, `fisc-2019` |
| `Agente Econômico` | `Agente Econômico` | texto | Nome do agente econômico fiscalizado (razão social); vazio quando o documento é CPF ou o valor é marcador | — | — | `fisc-1998-2018`, `fisc-2019` |
| `Segmento Fiscalizado` | `Segmento Fiscalizado` | texto | Segmento do abastecimento a que pertence o agente: por exemplo, `Revenda de Combustíveis`, `Revenda de GLP`, `Distribuidor de Combustíveis Líquidos`, `Distribuidor de GLP`, `Agente Não Regulado`, `TRR`; vazio em parte das linhas | — | — | `fisc-1998-2018`, `fisc-2019` |
| `DATA DO DF` | `DATA DO DF` | date32[day] | Data do documento de fiscalização (DF), como data | — | — | `fisc-1998-2018`, `fisc-2019` |
| `Número do Documento` | `Número do Documento` | inteiro | Número do documento de fiscalização; repete em várias linhas quando o mesmo documento tem mais de um resultado | — | — | `fisc-1998-2018`, `fisc-2019` |
| `Procedimento de Fiscalização` | `Procedimento de Fiscalização` | texto | Tipo do documento ou procedimento lavrado: `Auto de Infração`, `Termo de Coleta de Amostra`, `Notificação`, `Medida Reparadora de Conduta`, `Auto de Interdição`, `Termo Final de Medida Cautelar`, `Auto de Apreensão`, `Termo Fiel Depositário`, `Boletim de Fiscalização` (só de 2019 em diante), entre outros | — | — | `fisc-1998-2018`, `fisc-2019` |
| `Resultado` | `Resultado` | texto | Resultado ou irregularidade constatada na fiscalização, em texto de uma lista de valores (593 valores distintos em 1998-2018 e 495 de 2019 em diante), por exemplo `Sem Registro de Ocorrência` | — | — | `fisc-1998-2018`, `fisc-2019` |

## No lake

- Dataset `anp/fiscalizacao`, sem partições; um Parquet por planilha, `fisc-1998-2018.parquet` e `fisc-2019.parquet`.
- `DATA DO DF` é gravada como data (a planilha tem células de data) e `Número do Documento`, como inteiro; as demais colunas são texto. O CNPJ/CPF fica como texto de dígitos, sem formatação.

## Cuidados de uso

- **Uma linha não é uma infração confirmada.** A fonte avisa que só o julgamento definitivo do processo sancionador comprova a infração; documentos como o boletim de fiscalização e o termo de coleta de amostra não indicam, por si, irregularidade.
- **Número de documento repete.** 225.923 números distintos em 403.977 linhas (1998-2018) e 141.290 em 244.247 (2019 em diante): um documento pode ter vários resultados. Conte documentos com `count(distinct)`.
- **Duas planilhas com a mesma estrutura:** use `union_all` das duas para a série completa de 1998 até hoje; o rótulo «2019 a 2025» da página não vale para as datas do arquivo.
- **`CNPJ/CPF` com marcadores.** Há valores de 1 dígito (309 e 5 linhas) que não são documento; ao ligar a outras tabelas por CNPJ, descarte valores de menos de 11 dígitos.
- **Pessoa física.** Linhas com CPF de 11 dígitos trazem o documento de pessoa física; nome e endereço vêm vazios nessas linhas, mas o CPF continua no arquivo, e isso é dado pessoal.
- **`Resultado` é texto de uma lista grande** (593 e 495 valores distintos), com variações de grafia; agrupe com cuidado.
- **Dependência de vazios.** `Segmento Fiscalizado` é vazio em 8% das linhas de 1998-2018 e `Procedimento de Fiscalização`, em 487; `Bairro` e `ENDEREÇO` também têm vazios.

## Exemplos

Número de documentos de fiscalização por ano e por procedimento «Auto de Infração», nos anos mais recentes do arquivo de 2019 em diante:

```python
import duckdb

duckdb.sql("""
    SELECT year("DATA DO DF") AS ano, count(DISTINCT "Número do Documento") AS autos_de_infracao
    FROM read_parquet('lake/anp/fiscalizacao/fisc-2019.parquet')
    WHERE "Procedimento de Fiscalização" = 'Auto de Infração'
    GROUP BY ALL
    ORDER BY ano
""").show()
```

## Referências

- Dados abertos da ANP, Ações de Fiscalização do Abastecimento: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acoes-de-fiscalizacao
- Metadados do conjunto: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-acoes-de-fiscalizacao/metadados-acoes-fiscalizacao.docx
- Painel dinâmico da fiscalização do abastecimento: https://www.gov.br/anp/pt-br/centrais-de-conteudo/paineis-dinamicos-da-anp/painel-dinamico-da-fiscalizacao-do-abastecimento
