---
dataset:
  id: registro-lubrificantes
  fonte: anp
  titulo: Registro de óleos e graxas lubrificantes autorizados pela ANP
  resumo: Relação dos registros ativos de óleos e graxas lubrificantes na ANP, com marca, detentor, produtor, finalidade, viscosidade e embalagens, em um arquivo atualizado semanalmente.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/registro-de-oleos-e-graxas-lubrificantes
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semanal, segundo a página oficial (atualizada em 23/10/2026 e metadados de 15/06/2026); um único arquivo reescrito a cada atualização
  cobertura:
    inicio: '2008'
    fim: em-curso
  unidade: uma marca comercial de lubrificante com seu registro e uma variante de classificação de viscosidade (SAE, ISO ou NLGI)
  granularidade:
    espacial: nacional (sem localização; só o país do produto em `ORIGEM`)
    temporal: ano de publicação do registro (`ANO`, de 2008 a 2026) sobre um retrato dos registros ativos
  formato_bruto: CSV com separador `;`, UTF-8 com BOM e CRLF, com campos de texto entre aspas quando contêm `;`
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 20
  dados_pessoais:
  - coluna: DETENTOR
    categoria: razão social de pessoa jurídica
  - coluna: PRODUTOR
    categoria: razão social de pessoa jurídica
  - coluna: CNPJ_DETENTOR
    categoria: CNPJ de pessoa jurídica
  eras:
  - desde: '2008'
    mudanca: primeiro `ANO` de registro da amostra; o arquivo é um retrato dos registros ativos em 2026, não um histórico (todas as linhas têm `SITUACAO` `ATIVO`)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Registro de óleos e graxas lubrificantes autorizados pela ANP

## Resumo

Relação dos registros de óleos e graxas lubrificantes concedidos pela ANP segundo a Resolução ANP nº 804/2019, que fixa os critérios do registro e as obrigações de produtores e importadores. Por meio do registro a ANP obtém as especificações dos produtos, que usa para avaliar a qualidade no mercado comparando os testes de seu laboratório com os valores registrados. Cada linha descreve uma marca comercial registrada com seu detentor, produtor, finalidade, classificação de viscosidade (SAE, ISO ou NLGI), nível de desempenho, composição e embalagens; um mesmo número de registro se repete quando há mais de um grau de viscosidade.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/registro-lubrificantes` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/registro-de-oleos-e-graxas-lubrificantes |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semanal, segundo a página oficial (atualizada em 23/10/2026 e metadados de 15/06/2026); um único arquivo reescrito a cada atualização |
| Cobertura | 2008 a em-curso |
| Unidade (uma linha) | uma marca comercial de lubrificante com seu registro e uma variante de classificação de viscosidade (SAE, ISO ou NLGI) |
| Granularidade | espacial: nacional (sem localização; só o país do produto em `ORIGEM`); temporal: ano de publicação do registro (`ANO`, de 2008 a 2026) sobre um retrato dos registros ativos |
| Formato bruto | CSV com separador `;`, UTF-8 com BOM e CRLF, com campos de texto entre aspas quando contêm `;` |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 20 |
| Unidades de medida | — |
| Dados pessoais | `DETENTOR` (razão social de pessoa jurídica); `PRODUTOR` (razão social de pessoa jurídica); `CNPJ_DETENTOR` (CNPJ de pessoa jurídica) |
| Eras | 2008: primeiro `ANO` de registro da amostra; o arquivo é um retrato dos registros ativos em 2026, não um histórico (todas as linhas têm `SITUACAO` `ATIVO`) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-registro/dados-abertos-registro-produtos.csv`, o único arquivo do catálogo; a página oficial indica "atualizado em 23/10/2026" e atualização semanal.
- O arquivo lido em 2026-11-15 tem 7.492.582 bytes. No bruto, o nome é `registro-lubrificantes@AAAAMMDD.csv`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Metadados: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-registro/metadados-registro-produtos.pdf (apesar da extensão, é um documento Word), que descreve 20 colunas; origem dos dados: Consulta de Lubrificantes e Microsoft Power BI. A página remete também à consulta pública de lubrificantes (cdp.anp.gov.br) e ao Painel Dinâmico de Registro de Óleos e Graxas Lubrificantes.

## Conteúdo

- **15.369 linhas, 8.395 registros (`REG`) e 311 CNPJ de detentores.** Um registro tem em média quase duas linhas, porque as variantes de viscosidade (`SAE`, `ISO`, `NLGI`) geram linhas separadas (por exemplo, `REG` 6808, `DEITON EXTRA GEAR`, aparece com os graus 85W140 e 140, entre outros); não há chave simples.
- **Produtos.** 14.989 óleos lubrificantes e 380 graxas; por `FINALIDADE`, predominam o inciso I (cárter de motor, 8.272 linhas) e o inciso II (transmissões automotivas, 4.182).
- **Detentores.** `TIPO_EMPRESA`: 9.377 linhas de PRODUTOR, 3.301 de TERCEIRIZADOR e 2.691 de IMPORTADOR; `ORIGEM`: 12.578 NACIONAL e 2.791 IMPORTADO; `COMPOSICAO`: 7.222 MINERAL, 5.705 SINTÉTICO e 2.442 SEMISSINTÉTICO.
- **Ano do registro.** `ANO` vai de 2008 a 2026; os anos com mais linhas são 2025 (1.960), 2024 (1.513) e 2026 (1.196, parcial).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `registro-lubrificantes` (20) |

## Variáveis

As descrições vêm do documento de metadados da ANP (documento Word com 20 colunas). Os nomes das colunas do lake são os do cabeçalho do arquivo; o metadado chama `ACONDICIONAMENTO` de `ACOND.`, enquanto o arquivo traz o nome por extenso.
Todas as colunas são texto. As colunas `ISO` e `NLGI` ficam vazias nas linhas de outro tipo de produto (`ISO` só tem valor em 1.399 linhas e `NLGI` em 390).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `REG` | `REG` | texto | Número de registro do produto na ANP. Cada marca comercial está vinculada a um único número de registro, mas um registro pode aparecer em várias linhas (uma por grau de viscosidade ou outra variante) | — | — |
| `SITUACAO` | `SITUACAO` | texto | Situação do registro; na amostra só tem o valor `ATIVO` | — | — |
| `PROCESSO` | `PROCESSO` | texto | Processo ANP que aprovou e publicou o registro | — | — |
| `ANO` | `ANO` | texto | Ano de publicação do registro (2008 a 2026 na amostra) | — | — |
| `MARCA_COMERCIAL` | `MARCA_COMERCIAL` | texto | Identificação do produto, indicada no Anexo II e no rótulo | — | — |
| `DETENTOR` | `DETENTOR` | texto | Pessoa jurídica vinculada ao registro, responsável legal por todas as atualizações e alterações cadastrais da empresa e do registro perante a ANP | — | — |
| `CNPJ_DETENTOR` | `CNPJ_DETENTOR` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) do detentor, no formato `00.000.000/0000-00` | — | — |
| `TIPO_EMPRESA` | `TIPO_EMPRESA` | texto | Natureza do detentor | PRODUTOR = produtor; IMPORTADOR = importador; TERCEIRIZADOR = terceirizador | — |
| `TIPO_PRODUTO` | `TIPO_PRODUTO` | texto | Descrição do tipo de produto | ÓLEO LUBRIFICANTE = óleo lubrificante; GRAXA LUBRIFICANTE = graxa lubrificante | — |
| `FINALIDADE` | `FINALIDADE` | texto | Campo de aplicação conforme os incisos do art. 2º da Resolução ANP nº 804/2019 (I cárter de motor, II transmissões automotivas, III multifuncionais, IV aeronaves, V náuticos e marítimos, VI motores 2T, VII direção hidráulica, VIII biodegradáveis, IX contato alimentar incidental) | — | — |
| `APLICACAO` | `APLICACAO` | texto | Campo de aplicação, conforme a descrição apresentada pelo detentor no Anexo II (28 valores na amostra, como `CICLO OTTO`, `MOTOCICLETAS 4T` e `CICLO DIESEL`) | — | — |
| `PRODUTOR` | `PRODUTOR` | texto | Pessoa jurídica autorizada pela ANP para produção do lubrificante; em alguns registros lista dois produtores numerados (`[1] ... OU [2] ...`) | — | — |
| `ORIGEM` | `ORIGEM` | texto | Local de produção | NACIONAL = produzido no país; IMPORTADO = importado | — |
| `SAE` | `SAE` | texto | Classificação de viscosidade de óleos lubrificantes (SAE), conforme definições adotadas globalmente; `N.A.` quando não se aplica | — | — |
| `ISO` | `ISO` | texto | Classificação de viscosidade ISO de óleos lubrificantes; vazio ou `N.A.` quando não se aplica | — | — |
| `NLGI` | `NLGI` | texto | Classificação de penetração de graxas lubrificantes (grau NLGI); vazio ou `N.A.` quando não se aplica | — | — |
| `ND` | `ND` | texto | Nível de desempenho do produto; a Resolução ANP nº 804/2019 fixa como mínimos API SL e ACEA vigente (ciclo Otto) e API CH-4 e ACEA vigente (ciclo Diesel); aceita várias especificações separadas por ponto e vírgula | — | — |
| `COMPOSICAO` | `COMPOSICAO` | texto | Tipo de óleos básicos usados na formulação | MINERAL = mineral; SINTÉTICO = sintético; SEMISSINTÉTICO = semissintético | — |
| `ACONDICIONAMENTO` | `ACONDICIONAMENTO` | texto | Volumes em que os produtos são comercializados (lista separada por ponto e vírgula, com unidade, como `1 L; 20 L; 200 L`) | — | — |
| `OBS.` | `OBS.` | texto | Informações gerais não apresentadas em outros campos, como histórico de alterações do registro; `SEM OBSERVAÇÕES` quando não há | — | — |

## No lake

- Dataset `anp/registro-lubrificantes`, sem partições: um Parquet, `registro-lubrificantes.parquet`, com as 20 colunas do CSV, todas como texto.
- Um novo download substitui o retrato anterior no bruto; o arquivo só traz registros ativos, então um registro que deixa de ser ativo some do retrato seguinte.

## Cuidados de uso

- **Retrato dos registros ativos.** `SITUACAO` é `ATIVO` em todas as linhas; o arquivo só traz registros ativos, de modo que não serve para estudar o histórico de registros nem a saída de produtos do mercado.
- **`REG` repete.** Conte registros com `count(DISTINCT REG)` (8.395) e marcas com `count(DISTINCT MARCA_COMERCIAL)` (8.339); contar linhas superestima os produtos.
- **Valores `N.A.` e vazios.** `SAE` é `N.A.` em 2.343 linhas (graxas e outros produtos sem classificação SAE), `ISO` é `N.A.` em 641 e vazio em 13.970, `NLGI` é `N.A.` em 74 e vazio em 14.979. Trate `N.A.` e vazio como ausência.
- **Campos compostos.** `ND`, `ACONDICIONAMENTO` e `PRODUTOR` podem listar vários valores no mesmo campo (`;` ou `OU`); 347 linhas têm em `PRODUTOR` a forma `[1] ... OU [2] ...`. Divida antes de agrupar.
- **Texto de rótulo livre.** `MARCA_COMERCIAL`, `APLICACAO` e `OBS.` são digitados pelos detentores e mudam de grafia entre registros.
- **Dados pessoais.** O arquivo trata de pessoas jurídicas (detentores e produtores, com CNPJ); em empresas individuais a razão social pode trazer o nome do titular.

## Exemplos

Número de registros distintos por tipo de produto e tipo de empresa detentora:

```python
import duckdb

duckdb.sql("""
    SELECT TIPO_PRODUTO, TIPO_EMPRESA,
           count(DISTINCT REG) AS registros,
           count(*) AS linhas
    FROM read_parquet('lake/anp/registro-lubrificantes/*.parquet')
    GROUP BY ALL
    ORDER BY registros DESC
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/registro-de-oleos-e-graxas-lubrificantes
- Metadados (documento Word com extensão .pdf): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-registro/metadados-registro-produtos.pdf
- Resolução ANP nº 804/2019, que estabelece os critérios para o registro de graxas e óleos lubrificantes, citada pela página oficial.
