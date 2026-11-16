---
dataset:
  id: movimentacao-terminais
  fonte: anp
  titulo: Movimentação dos terminais aquaviários de derivados de petróleo
  resumo: Volumes mensais de petróleo, derivados e biocombustíveis recebidos e entregues pelos terminais aquaviários, por terminal, produto, tipo de operação e modo de transporte, em um arquivo único atualizado mensalmente.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/movimentacao-dos-terminais-aquaviarios
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo os metadados da ANP (versão de 12/06/2026); um único arquivo reescrito a cada atualização (atualizado em 04/11/2026)
  cobertura:
    inicio: 2013-01
    fim: 2026-09
  unidade: o volume de um produto recebido ou entregue por um terminal aquaviário, num mês, em um tipo de operação e modo de transporte
  granularidade:
    espacial: terminal aquaviário (município e UF)
    temporal: mês de referência
  formato_bruto: planilha Excel (.xlsx, aba `Planilha1`) servida com a extensão `.csv`; 13 colunas e uma linha de cabeçalho
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 13
  unidades_de_medida:
    volume_m3: m³ a 20 ºC
    codigo_anp_do_terminal: código (adimensional)
    sentido_da_operacao: código (adimensional)
    tipo_da_operacao: código (adimensional)
    modo_de_transporte: código (adimensional)
    codigo_anp_do_produto: código (adimensional)
  dados_pessoais:
  - coluna: nome_do_terminal
    categoria: nome de terminal ou empresa operadora (pessoa jurídica)
  - coluna: nome_da_instalacao
    categoria: nome de terminal ou empresa operadora (pessoa jurídica)
  eras:
  - desde: '2013'
    mudanca: 'primeiros meses do arquivo: 8.137 linhas em 2013 (22 terminais), 7.300 a 9.100 linhas por ano até 2020; os metadados não explicam esses meses, anteriores à obrigação de publicidade'
  - desde: '2022'
    mudanca: 'a partir de setembro de 2022, primeiro mês de referência com obrigação de publicidade no formato padronizado pela ANP (Resolução ANP nº 881/2022): o arquivo passa a ter 22.000 a 26.700 linhas por ano e 65 a 70 terminais'
  - desde: '2026'
    mudanca: 2026 (até setembro) tem 125 terminais distintos na amostra, contra 65 a 70 por ano em 2022 a 2025
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Movimentação dos terminais aquaviários de derivados de petróleo

## Resumo

Movimentação mensal dos terminais aquaviários autorizados pela ANP, compilada a partir dos dados que os operadores devem publicar em seus sites, mensalmente, conforme a Resolução ANP nº 881/2022 (critérios de uso dos terminais aquaviários). Cada linha traz o volume (m³ a 20 ºC) de um produto recebido ou entregue por um terminal em um mês, com o tipo da operação (com ou sem armazenagem, transbordo, abastecimento) e o modo de transporte (rodoviário, ferroviário, aquaviário, dutoviário). Segundo a ANP, a série padronizada começa em setembro de 2022, mas o arquivo traz também meses de 2013 a agosto de 2022.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/movimentacao-terminais` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/movimentacao-dos-terminais-aquaviarios |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo os metadados da ANP (versão de 12/06/2026); um único arquivo reescrito a cada atualização (atualizado em 04/11/2026) |
| Cobertura | 2013-01 a 2026-09 |
| Unidade (uma linha) | o volume de um produto recebido ou entregue por um terminal aquaviário, num mês, em um tipo de operação e modo de transporte |
| Granularidade | espacial: terminal aquaviário (município e UF); temporal: mês de referência |
| Formato bruto | planilha Excel (.xlsx, aba `Planilha1`) servida com a extensão `.csv`; 13 colunas e uma linha de cabeçalho |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 13 |
| Unidades de medida | `volume_m3`: m³ a 20 ºC; `codigo_anp_do_terminal`: código (adimensional); `sentido_da_operacao`: código (adimensional); `tipo_da_operacao`: código (adimensional); `modo_de_transporte`: código (adimensional); `codigo_anp_do_produto`: código (adimensional) |
| Dados pessoais | `nome_do_terminal` (nome de terminal ou empresa operadora (pessoa jurídica)); `nome_da_instalacao` (nome de terminal ou empresa operadora (pessoa jurídica)) |
| Eras | 2013: primeiros meses do arquivo: 8.137 linhas em 2013 (22 terminais), 7.300 a 9.100 linhas por ano até 2020; os metadados não explicam esses meses, anteriores à obrigação de publicidade; 2022: a partir de setembro de 2022, primeiro mês de referência com obrigação de publicidade no formato padronizado pela ANP (Resolução ANP nº 881/2022): o arquivo passa a ter 22.000 a 26.700 linhas por ano e 65 a 70 terminais; 2026: 2026 (até setembro) tem 125 terminais distintos na amostra, contra 65 a 70 por ano em 2022 a 2025 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-movimentacao-dos-terminais-aquaviarios/dados-abertos-movimentacao-terminais-aquaviarios.csv`, o único arquivo do catálogo; a página oficial indica "atualizado em 4/11/2026".
- O arquivo lido em 2026-11-15 tem 10.978.111 bytes e, apesar da extensão `.csv`, é uma planilha Excel (`file` a identifica como "Microsoft Excel 2007+") com uma aba, `Planilha1`, de 190.944 linhas de dados. No bruto, o nome é `movterm@AAAAMMDD.csv`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Metadados em PDF (versão 12/06/2026): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-movimentacao-dos-terminais-aquaviarios/metadados-movimentacao-terminais-aquaviarios.pdf. Fonte: dados de movimentação obtidos dos sites dos operadores de terminais aquaviários e dados cadastrais do SIMP; órgão responsável: Superintendência de Infraestrutura e Movimentação (SIM/ANP); mensal.
- A página liga os dados ao Painel Dinâmico da tancagem do abastecimento nacional de combustíveis e informa que a série histórica começa em 2022-09; o painel dos metadados é o Painel Dinâmico de Aplicação da Resolução ANP nº 881/2022.

## Conteúdo

- **190.944 linhas de 165 meses (2013-01 a 2026-09), 130 códigos de terminal e 70 nomes de terminal.** Antes de setembro de 2022 há 75.767 linhas (22 a 33 terminais por ano); de setembro de 2022 em diante, 115.177.
- **Operações.** Por `sentido_modal`: Recepção - Aquaviário (43.686 linhas), Entrega - Rodoviário (43.379), Entrega - Aquaviário (27.860), Entrega - Dutoviário (27.047), Recepção - Dutoviário (23.417) e Recepção - Rodoviário (17.936), mais ferroviário e outros; `tipo_da_operacao` 1 (com armazenagem) responde por 142.564 linhas.
- **Produtos.** 233 códigos ANP de produto e 476 descrições distintas (74 códigos têm mais de uma descrição); os mais frequentes são óleo diesel A S10, gasolina A comum, óleo diesel A S500, etanol anidro e biodiesel B100.
- **Terminais mais frequentes.** `ULTRACARGO ITAQUI` (24.538 linhas), `VOPAK BRASIL S/A - ALEMOA` (11.251), `TA ILHA DAGUA` (10.957) e `TA S.SEBASTIAO` (10.897).
- **Volume.** `volume_m3` vai de 0 a 4.297.656,614 m³ por linha; 2.079 linhas valem zero e uma linha é nula (um recebimento de querosene de aviação em maio de 2025 no terminal PANDENOR IPOJUCA).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `movterm` (13) |

## Variáveis

As descrições e os códigos vêm do documento de metadados da ANP (versão de 12/06/2026). Os nomes das colunas do lake são os do arquivo, em minúsculas com sublinhado (o metadado `MesReferencia` é `mes_de_referencia`); `sentido_modal` e `nome_da_instalacao` não constam nos metadados.
Os códigos de `sentido_da_operacao`, `tipo_da_operacao` e `modo_de_transporte` são os da tabela do metadado; os códigos de terminal e de produto vêm das tabelas de apoio T008 e T012 do SIMP, que não estão na fonte do arquivo.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `mes_de_referencia` | `MesReferencia` | date32[day] | Mês de referência, como data do primeiro dia do mês. Os metadados dizem formato `AAAA-MM`, mas o arquivo traz data completa | — | — |
| `codigo_anp_do_terminal` | `codigo_anp_do_terminal` | inteiro | Sequência numérica de sete algarismos que identifica cada estabelecimento junto à ANP (código de instalação i-SIMP), conforme a tabela de apoio T008 do SIMP | — | — |
| `nome_do_terminal` | `nome_do_terminal` | texto | Nome reduzido atribuído pela ANP ao terminal (por exemplo, `ABI SANTARÉM`) | — | — |
| `municipio_do_terminal` | `municipio_do_terminal` | texto | Nome do município onde está estabelecida a instalação autorizada a operar; a grafia varia (`SANTOS`, `Rio de Janeiro`, `Vila Velha`) | — | — |
| `uf` | `uf` | texto | Sigla da unidade da federação onde está estabelecida a instalação; uma linha traz o texto `SP+E460:F500`, resíduo de fórmula da planilha | — | — |
| `sentido_da_operacao` | `sentido_da_operacao` | inteiro | Indica se o produto está entrando (1) ou saindo (2) do terminal | 1 = Recepção; 2 = Entrega | — |
| `tipo_da_operacao` | `tipo_da_operacao` | inteiro | Detalha a operação realizada pelo terminal | 1 = com armazenagem: produto bombeado a partir de, ou para, tanque do próprio terminal; 2 = sem armazenagem: produto bombeado a partir de, ou para, tanque de outra instalação; 3 = transbordo: transferência direta de produtos de uma embarcação para outra; … (lista completa no dicionário da fonte) | — |
| `modo_de_transporte` | `modo_de_transporte` | inteiro | Modo de transporte usado na movimentação do produto | 1 = rodoviário; 2 = ferroviário; 4 = aquaviário; 5 = dutoviário; 9 = outros | — |
| `codigo_anp_do_produto` | `codigo_anp_do_produto` | inteiro | Código ANP do produto movimentado, conforme a tabela de apoio T012 do SIMP (códigos de produtos), com 9 dígitos | — | — |
| `descricao_do_produto` | `descricao_do_produto` | texto | Nome do produto conforme a tabela T012 do SIMP, ou a denominação própria do produto quando ele não consta na tabela; em parte das linhas o texto vem com acentos corrompidos (`Ã“LEO DIESEL A S10`) | — | — |
| `sentido_modal` | `sentido_modal` | texto | Combinação de sentido e modo de transporte em texto (`Recepção - Aquaviário`, `Entrega - Rodoviário` etc.); coluna do arquivo que não consta nos metadados | — | — |
| `volume_m3` | `volume_m3` | decimal | Quantidade de produto movimentada convertida para metros cúbicos (m³) a 20 ºC, com três casas decimais | — | — |
| `nome_da_instalacao` | `nome_da_instalacao` | texto | Nome da instalação (terminal) com o nome da empresa e do local (por exemplo, `TRANSPETRO SÃO SEBASTIÃO`); coluna do arquivo que não consta nos metadados e fica vazia em 12.109 linhas | — | — |

## No lake

- Dataset `anp/movimentacao-terminais`, sem partições: um Parquet, `movterm.parquet`, com as 13 colunas da planilha; `mes_de_referencia` fica como data, os códigos como inteiros e `volume_m3` como decimal.
- O conversor lê a planilha mesmo com a extensão `.csv`; o texto corrompido e o resíduo de fórmula da planilha de origem vêm intactos para o lake.

## Cuidados de uso

- **Série de 2013 a 2022 não é a série padronizada.** A ANP diz que a série histórica inicia em 2022-09; o arquivo traz 75.767 linhas de 2013-01 a 2022-08 (22 a 33 terminais), com cobertura bem menor (cerca de 7.300 a 9.100 linhas por ano contra 22.000 a 26.700 depois). Não compare totais entre os dois períodos sem checar os terminais incluídos.
- **Texto corrompido em `descricao_do_produto`.** 27.760 linhas (15 descrições distintas, de setembro de 2022 em diante) trazem acentos mal codificados na própria planilha (`Ã“LEO DIESEL A S10` em vez de `ÓLEO DIESEL A S10`), de modo que o mesmo produto aparece com duas grafias. Agrupe pelo `codigo_anp_do_produto` e não pela descrição.
- **Resíduo de fórmula em `uf`.** Uma linha tem `uf` igual a `SP+E460:F500` (terminal ADONAI QUIMICA, dezembro de 2024); trate como `SP`.
- **Grafia do município.** Dois municípios aparecem com capitalização diferente das demais linhas (`Rio de Janeiro`, 14.121 linhas, e `Vila Velha`, 3.385); use `upper()` ao agrupar.
- **Códigos e descrições de produto não são 1 para 1.** 74 códigos de produto têm mais de uma descrição (grafias e formas corrompidas); o inverso (um nome para vários códigos) não foi verificado.
- **Linhas repetidas sem chave.** Com mês, terminal, sentido, tipo, modo e produto, só 128.024 combinações aparecem em 190.944 linhas, porque a mesma combinação se repete em várias linhas (a causa não foi verificada); agregue (`sum(volume_m3)`) antes de comparar.
- **Volume é movimentação, não estoque.** `volume_m3` é a quantidade movimentada no mês, em m³ a 20 ºC; somar recepção e entrega mistura os dois sentidos e pode contar duas vezes o mesmo volume (recebido e depois entregue).
- **Dados pessoais.** Só há nomes de terminais e operadores (pessoas jurídicas).

## Exemplos

Volume entregue (sentido 2) por terminal e modo de transporte em 2025, em m³:

```python
import duckdb

duckdb.sql("""
    SELECT nome_do_terminal, sentido_modal,
           round(sum(volume_m3)) AS volume_m3
    FROM read_parquet('lake/anp/movimentacao-terminais/*.parquet')
    WHERE year(mes_de_referencia) = 2025 AND sentido_da_operacao = 2
    GROUP BY ALL
    ORDER BY volume_m3 DESC
    LIMIT 8
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/movimentacao-dos-terminais-aquaviarios
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-movimentacao-dos-terminais-aquaviarios/metadados-movimentacao-terminais-aquaviarios.pdf
- Resolução ANP nº 881/2022, que estabelece os critérios de uso dos terminais aquaviários e a publicação mensal da movimentação, citada na página oficial e nos metadados.
