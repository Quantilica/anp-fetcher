---
dataset:
  id: movimentacao-derivados
  fonte: anp
  titulo: 'Movimentação de derivados de petróleo e biocombustíveis (dados abertos): vendas, entregas e logística'
  resumo: Vendas, entregas e movimentação logística de combustíveis líquidos, GLP, asfalto, combustíveis de aviação, solventes, lubrificantes, TRR e etanol (venda direta), mensais, de 2007 a 2026, em 47 tabelas.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-movimentacao-de-derivados-de-petroleo
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; a página informa as atualizações dos pacotes em 03/11/2026 e 13/11/2026 (combustíveis líquidos), com dados até setembro de 2026
  cobertura:
    inicio: 2007-01
    fim: 2026-09
  unidade: 'depende da tabela: um agente (distribuidor, TRR, produtor, fornecedor ou coletor), um produto e um par origem-destino (região, UF ou localidade) num mês; ou, nas tabelas por UF, um produto e um par de UF num mês; ou, nos anexos de lubrificantes, um recorte próprio (veja a tabela em Conteúdo)'
  granularidade:
    espacial: agente regulado, região, UF ou município, conforme a tabela
    temporal: mês (`Ano` e `Mês`, ou `Período`)
  formato_bruto: ZIP com CSV (`;` e vírgula decimal, codificação ISO-8859, não UTF-8); sete ZIP de tabelas, um de fornecedores de etanol e um de logística; o ZIP de lubrificantes inclui `INDICE_ANEXOS.xlsx`
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 60
  unidades_de_medida:
    Quantidade de Produto (mil m³): mil m³
    Quantidade de produto (mil m³): mil m³
    Quantidade de Produto(mil ton): mil t
    Quantidade de Produto (mil ton): mil t
    Qtd  Produto Líquido: litro
    Volume(L): litro
    Volume Coletado(L): litro
    Volume coletado(L): litro
    Volume(mil m³): mil m³
  dados_pessoais:
  - coluna: Agente Regulado
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Distribuidor
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Fornecedor
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Fornecedor Destino
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Distribuidor Origem
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Vendedor
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Comprador
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Coletor
    categoria: razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular
  - coluna: Código Agente Regulado
    categoria: código ANP de agente regulado (pessoa jurídica)
  - coluna: Código do Regulado - ANP
    categoria: código ANP de agente regulado (pessoa jurídica)
  eras:
  - desde: '2007'
    mudanca: tabelas históricas de vendas e entregas de líquidos, GLP, asfalto e solventes a partir de janeiro de 2007 (aviação, em outubro de 2007; importação por distribuidores, em fevereiro de 2009; vendas de TRR, em abril de 2009; solventes de produtores, em abril de 2010; lubrificantes, em outubro de 2015, com o anexo I desde julho de 2007 e o C desde janeiro de 2015; fornecedores de etanol, em novembro de 2021)
  - desde: '2018'
    mudanca: no arquivo histórico de vendas de combustíveis líquidos, o recorte de 2018 a 2023 passa a ter `Descrição do Produto`, que não existe no de 2007 a 2017
  - desde: '2022'
    mudanca: tabelas de logística do abastecimento nacional, «a partir de novembro de 2022» segundo o metadado (no lake os períodos vão de 2022-01 a 2026-09)
  - desde: '2024'
    mudanca: tabelas `atual`, de janeiro de 2024 em diante, sucedem as `historico` (até dezembro de 2023); as `atual` não têm UF por agente e vêm também em versões só por UF, sem agente
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Movimentação de derivados de petróleo e biocombustíveis (dados abertos): vendas, entregas e logística

## Resumo

Nove pacotes da ANP, cada um com várias tabelas CSV de movimentação de derivados de petróleo e biocombustíveis feita pelo segmento de distribuição, a partir do SIMP (Sistema de Informações de Movimentação de Produtos). As tabelas cobrem asfalto, combustíveis de aviação, combustíveis líquidos, GLP, lubrificantes, solventes, TRR (transportador-revendedor-retalhista), fornecedores de etanol em venda direta e a «logística do abastecimento nacional». Em cada segmento há tabelas de vendas por agente, de vendas por UF e de entregas, em versão `atual` (de 2024 em diante) e `historico` (de 2007 a 2023). O lake guarda cada tabela como um dataset próprio (`movimentacao-derivados-<segmento>-<tabela>`); esta página cobre as 47.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/movimentacao-derivados` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-movimentacao-de-derivados-de-petroleo |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; a página informa as atualizações dos pacotes em 03/11/2026 e 13/11/2026 (combustíveis líquidos), com dados até setembro de 2026 |
| Cobertura | 2007-01 a 2026-09 |
| Unidade (uma linha) | depende da tabela: um agente (distribuidor, TRR, produtor, fornecedor ou coletor), um produto e um par origem-destino (região, UF ou localidade) num mês; ou, nas tabelas por UF, um produto e um par de UF num mês; ou, nos anexos de lubrificantes, um recorte próprio (veja a tabela em Conteúdo) |
| Granularidade | espacial: agente regulado, região, UF ou município, conforme a tabela; temporal: mês (`Ano` e `Mês`, ou `Período`) |
| Formato bruto | ZIP com CSV (`;` e vírgula decimal, codificação ISO-8859, não UTF-8); sete ZIP de tabelas, um de fornecedores de etanol e um de logística; o ZIP de lubrificantes inclui `INDICE_ANEXOS.xlsx` |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 60 |
| Unidades de medida | `Quantidade de Produto (mil m³)`: mil m³; `Quantidade de produto (mil m³)`: mil m³; `Quantidade de Produto(mil ton)`: mil t; `Quantidade de Produto (mil ton)`: mil t; `Qtd  Produto Líquido`: litro; `Volume(L)`: litro; `Volume Coletado(L)`: litro; `Volume coletado(L)`: litro; `Volume(mil m³)`: mil m³ |
| Dados pessoais | `Agente Regulado` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Distribuidor` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Fornecedor` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Fornecedor Destino` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Distribuidor Origem` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Vendedor` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Comprador` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Coletor` (razão social de pessoa jurídica; em empresas individuais pode trazer o nome do titular); `Código Agente Regulado` (código ANP de agente regulado (pessoa jurídica)); `Código do Regulado - ANP` (código ANP de agente regulado (pessoa jurídica)) |
| Eras | 2007: tabelas históricas de vendas e entregas de líquidos, GLP, asfalto e solventes a partir de janeiro de 2007 (aviação, em outubro de 2007; importação por distribuidores, em fevereiro de 2009; vendas de TRR, em abril de 2009; solventes de produtores, em abril de 2010; lubrificantes, em outubro de 2015, com o anexo I desde julho de 2007 e o C desde janeiro de 2015; fornecedores de etanol, em novembro de 2021); 2018: no arquivo histórico de vendas de combustíveis líquidos, o recorte de 2018 a 2023 passa a ter `Descrição do Produto`, que não existe no de 2007 a 2017; 2022: tabelas de logística do abastecimento nacional, «a partir de novembro de 2022» segundo o metadado (no lake os períodos vão de 2022-01 a 2026-09); 2024: tabelas `atual`, de janeiro de 2024 em diante, sucedem as `historico` (até dezembro de 2023); as `atual` não têm UF por agente e vêm também em versões só por UF, sem agente |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa nove ZIP de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/mdpg/`: `asfalto.zip`, `aviacao.zip`, `liquidos.zip`, `glp.zip`, `lubrificante.zip`, `solvente.zip`, `trr.zip`, `fornecedores-vendas-diretas.zip` e `movimentacaologistica.zip` (a página informa «Dados abertos (.zip)» de cada um, atualizados em 03/11/2026, e 13/11/2026 para líquidos). Cada CSV de dentro do ZIP vira um dataset do lake.
- Metadados: a página oferece um ZIP de metadados para cada segmento, que não pôde ser baixado na conferência (o link interno não resolveu); só o metadado unificado da logística é um PDF acessível (`https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/mdpg/metadado-unificado-logistica.pdf`), e o de lubrificantes tem um índice de anexos dentro do ZIP de dados. Por isso, as descrições das colunas, exceto as da logística e as dos títulos dos anexos de lubrificantes, são deduzidas do nome e dos valores observados.
- Fonte dos dados: SIMP (ANP); a página descreve os pacotes como os dados «referentes às comercializações de derivados de petróleo e de biocombustíveis realizadas pelo segmento de distribuição», em tabelas por segmento com metadados e em CSV. Para a logística, o metadado cita a Superintendência de Logística (ANP/SDL) como órgão responsável.
- A página informa que os dados abertos de graxas, antes publicados à parte, passam a integrar o arquivo de lubrificantes e o Painel Dinâmico do Mercado Brasileiro de Lubrificantes.

## Conteúdo

- **47 tabelas, um dataset por tabela.** O lake tem um dataset por CSV: `anp/movimentacao-derivados-<segmento>-<tabela>` (46) mais `anp/movimentacao-derivados` (a tabela de fornecedores de etanol, que é um CSV isolado). A tabela abaixo lista todas (período e linhas conferidos na amostra de 2026-11-15):

| Tabela (`movimentacao-derivados-…`) | Conteúdo | Período | Unidade da quantidade | Linhas |
|---|---|---|---|---|
| `movimentacao-derivados` (fornecedores) | vendas diretas de etanol hidratado pelos fornecedores (usinas), por operação, produto, agente, regiões de origem e de destino e mercado | 2021-11 a 2026-09 | mil m³ | 2.540 |
| `asfalto-vendas-distribuidor-atual` | vendas de asfalto por distribuidor, produto, regiões de origem e de destino e mercado (sem UF) | 2024-01 a 2026-09 | mil t | 12.348 |
| `asfalto-vendas-distribuidor-historico` | vendas de asfalto por distribuidor e produto, com UF e região de origem e de destino | 2007-01 a 2023-12 | mil t | 133.219 |
| `asfalto-vendas-distribuidor-uf-atual` | vendas de asfalto por produto, UF e região de origem e de destino (sem distribuidor) | 2024-01 a 2026-09 | mil t | 11.673 |
| `aviacao-entregas-distribuidor-atual` | entregas de gasolina e querosene de aviação por distribuidor e região | 2024-01 a 2026-09 | mil m³ | 655 |
| `aviacao-entregas-fornecedor-atual` | entregas de gasolina e querosene de aviação por fornecedor e região | 2024-01 a 2026-09 | mil m³ | 378 |
| `aviacao-entregas-historico` | entregas de combustíveis de aviação por par fornecedor-distribuidor, UF de origem e localidade de destino | 2007-10 a 2023-12 | mil m³ | 6.166 |
| `aviacao-vendas-atual` | vendas de combustíveis de aviação por distribuidor, regiões de origem e de destino e mercado (sem UF) | 2024-01 a 2026-09 | mil m³ | 5.484 |
| `aviacao-vendas-historico` | vendas de combustíveis de aviação por distribuidor, com UF e região de origem e de destino | 2007-10 a 2023-12 | mil m³ | 100.338 |
| `aviacao-vendas-uf-atual` | vendas de combustíveis de aviação por UF e região de origem e de destino (sem distribuidor) | 2024-01 a 2026-09 | mil m³ | 17.888 |
| `glp-entregas-distribuidor-atual` | entregas de GLP por distribuidor, região e código de embalagem | 2024-01 a 2026-09 | mil t | 1.296 |
| `glp-entregas-fornecedor-atual` | entregas de GLP por fornecedor, região e código de embalagem | 2024-01 a 2026-09 | mil t | 702 |
| `glp-entregas-historico` | entregas de GLP por par fornecedor-distribuidor, UF de origem e localidade de destino | 2007-01 a 2023-12 | mil t | 25.402 |
| `glp-vendas-atual` | vendas de GLP por distribuidor, embalagem, UF e região de origem e de destino e mercado | 2024-01 a 2026-09 | mil t | 56.627 |
| `glp-vendas-historico` | vendas de GLP por distribuidor, com UF e região de origem e de destino, mercado e embalagem | 2007-01 a 2023-12 | mil t | 342.522 |
| `glp-vendas-uf-atual` | vendas de GLP por produto, embalagem (código numérico), UF e região de origem e de destino (sem distribuidor) | 2024-01 a 2026-09 | mil t | 25.391 |
| `liquidos-entregas-distribuidor-atual` | entregas de combustíveis líquidos por distribuidor, produto e região | 2024-01 a 2026-09 | mil m³ | 36.832 |
| `liquidos-entregas-fornecedor-atual` | entregas de combustíveis líquidos por fornecedor, produto e região | 2024-01 a 2026-09 | mil m³ | 13.945 |
| `liquidos-entregas-historico` | entregas de combustíveis líquidos por par fornecedor-distribuidor, UF de origem e localidade de destino | 2007-01 a 2023-12 | mil m³ | 564.014 |
| `liquidos-importacao-distribuidores` | importação de combustíveis líquidos pelos distribuidores, por região e UF do distribuidor e região e UF de origem | 2009-02 a 2026-09 | mil m³ | 1.805 |
| `liquidos-vendas-atual` | vendas de combustíveis líquidos por distribuidor, produto (com descrição), UF e região de origem e de destino e mercado | 2024-01 a 2026-09 | mil m³ | 377.701 |
| `liquidos-vendas-historico` | vendas de combustíveis líquidos por distribuidor (dois arquivos: 2007 a 2017, sem descrição do produto, e 2018 a 2023, com ela) | 2007-01 a 2023-12 | mil m³ | 1.390.894 |
| `logistica-abastecimento-nacional` | comercialização de combustíveis líquidos por UF de origem e de destino, produto, classificação, operação e modal | 2022-01 a 2026-09 | litro | 233.946 |
| `logistica-vendas-congeneres` | vendas entre congêneres de distribuidores, por produto, UF de origem e de destino, vendedor e comprador | 2022-01 a 2026-09 | litro | 55.328 |
| `logistica-vendas-mercado` | vendas no mercado brasileiro de combustíveis, por UF de destino, produto e vendedor | 2022-01 a 2026-09 | litro | 234.198 |
| `lubrificante-anexo-a` | Anexo A: vendas por UF de óleos lubrificantes acabados (OLAC) pelos produtores e importadores, por produto, origem e destino | 2015-10 a 2026-09 | litro | 197.527 |
| `lubrificante-anexo-b` | Anexo B: vendas por UF de OLAC dispensadas de coleta, por agente, produto, origem e destino | 2015-10 a 2026-09 | litro | 65.177 |
| `lubrificante-anexo-c` | Anexo C: produção nacional de OLAC, por produto, região e UF do produtor e operação | 2015-01 a 2026-09 | litro | 7.021 |
| `lubrificante-anexo-d` | Anexo D: vendas nacionais de OLAC pelos produtores e importadores, por agente, produto e destino | 2015-10 a 2026-09 | litro | 201.137 |
| `lubrificante-anexo-e` | Anexo E: vendas nacionais de OLAC dispensadas de coleta, por agente, produto e destino | 2015-10 a 2026-09 | litro | 65.177 |
| `lubrificante-anexo-f` | Anexo F: volume de óleo lubrificante usado ou contaminado (OLUC) coletado, por município | 2015-10 a 2026-09 | litro | 359.796 |
| `lubrificante-anexo-g` | Anexo G: volume de OLUC coletado, por coletor e UF de coleta | 2015-10 a 2026-09 | litro | 25.486 |
| `lubrificante-anexo-h` | Anexo H: volume de certificados de recebimento no rerrefino, por coletor | 2015-10 a 2026-09 | litro | 17.381 |
| `lubrificante-anexo-i` | Anexo I: operações por rerrefinador (coleta, produção de básicos e outras), por produto e destino | 2007-07 a 2026-09 | litro | 46.629 |
| `lubrificante-anexo-j` | Anexo J: meta de coleta, volume vendido e dispensado de coleta por região | 2015-10 a 2026-09 | mil m³ | 1.320 |
| `solvente-vendas-distribuidor-atual` | vendas de solventes por distribuidor, produto, regiões de origem e de destino e mercado (sem UF) | 2024-01 a 2026-09 | mil m³ | 14.697 |
| `solvente-vendas-distribuidor-historico` | vendas de solventes por distribuidor, com UF e região de origem e de destino | 2007-01 a 2023-12 | mil m³ | 120.390 |
| `solvente-vendas-distribuidor-uf-atual` | vendas de solventes por produto, UF e região de origem e de destino (sem distribuidor) | 2024-01 a 2026-09 | mil m³ | 10.357 |
| `solvente-vendas-produtor-atual` | vendas de solventes pelos produtores, por produto, regiões e mercado (sem UF) | 2024-01 a 2026-09 | mil m³ | 2.319 |
| `solvente-vendas-produtor-historico` | vendas de solventes pelos produtores, com UF e região de origem e de destino | 2010-04 a 2023-12 | mil m³ | 10.212 |
| `solvente-vendas-produtor-uf-atual` | vendas de solventes pelos produtores, por produto, UF e região de origem e de destino (sem agente) | 2024-01 a 2026-09 | mil m³ | 2.521 |
| `trr-vendas-distribuidor-atual` | vendas dos distribuidores aos TRR, por distribuidor, produto e região de origem e de destino (sem UF) | 2024-01 a 2026-09 | mil m³ | 47.823 |
| `trr-vendas-distribuidor-historico` | vendas dos distribuidores aos TRR, com UF e região de origem e de destino | 2007-01 a 2023-12 | mil m³ | 116.337 |
| `trr-vendas-distribuidor-uf-atual` | vendas dos distribuidores aos TRR por produto, UF e região (sem agente) | 2024-01 a 2026-09 | mil m³ | 9.695 |
| `trr-vendas-trr-atual` | vendas dos TRR a consumidor final, por TRR, produto, UF e região de origem e de destino (rótulos das colunas de UF e região trocados na fonte) | 2024-01 a 2026-09 | mil m³ | 88.889 |
| `trr-vendas-trr-historico` | vendas dos TRR, por TRR, produto, com UF e região de origem e de destino | 2009-04 a 2023-12 | mil m³ | 305.682 |
| `trr-vendas-trr-uf-atual` | vendas dos TRR por produto, UF e região de origem e de destino (sem agente) | 2024-01 a 2026-09 | mil m³ | 24.667 |

- **Padrão das tabelas de vendas.** Vendas por agente `atual` (2024 a 2026-09) têm região de origem e de destino; as `historico` (2007 a 2023) acrescentam UF de origem e de destino; as `uf-atual` têm UF e região, sem o agente. O mesmo vale para TRR, solventes, aviação, GLP e asfalto. As tabelas de **entregas** (aviação, GLP e líquidos) são por distribuidor ou por fornecedor e região (`atual`) ou por par fornecedor-distribuidor e localidade de destino (`historico`).
- **Lubrificantes.** O índice do ZIP de lubrificantes (`INDICE_ANEXOS.xlsx`) dá os títulos dos dez anexos, de A a J; eles alimentam o Painel Dinâmico do Mercado Brasileiro de Lubrificantes. Os anexos B e E têm o mesmo total (3.394.185.931 litros): o B é o E aberto por região e UF de origem.
- **Logística.** Três tabelas que, segundo o metadado, começam em novembro de 2022 (no lake os períodos vão de 2022-01 a 2026-09): abastecimento nacional (UF de origem e de destino, classificação, operação e modal), vendas no mercado brasileiro (vendedor e UF de destino) e vendas entre congêneres de distribuidores (vendedor e comprador); a quantidade está em litros, ao contrário das demais, em mil m³ ou mil toneladas.
- **Valores.** Todas as colunas, inclusive as quantidades, são texto no lake, com vírgula decimal (`0,241581`). Há valores negativos (estornos ou ajustes) em 38 das 47 tabelas, por exemplo 5.406 linhas no histórico de vendas de GLP e 14.632 na tabela de abastecimento nacional da logística.

## Variáveis

Os metadados dos segmentos não puderam ser lidos (veja Origem e coleta); as descrições são deduzidas do nome e dos valores observados, exceto as das colunas da logística (metadado unificado em PDF) e as que citam os títulos do `INDICE_ANEXOS.xlsx` de lubrificantes.
A mesma coluna aparece com nomes parecidos em tabelas diferentes (por exemplo `Região Origem`, `Região de Origem`, `UF Origem`, `UF de Origem`, `Quantidade de Produto (mil m³)`, `Quantidade de Produto(mil ton)`): cada grafia é uma linha do dicionário, com a coluna Arquivos dizendo em quais tabelas ela existe. O nome `Ano` aparece também como ` Ano` (com espaço no início) em quatro tabelas; o esquema acima já traz o nome sem espaços.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | texto | Ano de referência, com quatro dígitos; em quatro tabelas o nome da coluna vem com um espaço no início (` Ano`) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 41 |
| `Mês` | `Mês` | texto | Mês de referência, como número em texto: `1` a `12` na maioria das tabelas e `01` a `12` nas tabelas por UF e na de importação; a tabela histórica de vendas aos TRR mistura as duas grafias (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 41 |
| `Código Operação` | `Código Operação` | texto | Código da operação (7 dígitos), só na tabela de fornecedores de etanol (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados` |
| `Nome Operação` | `Nome Operação` | texto | Nome da operação: venda para agente regulado ou não regulado, venda com remessa por terceiro, entrega de venda contratada a futuro e recebimento de devoluções, só na tabela de fornecedores de etanol (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados` |
| `Código do Produto` | `Código do Produto` | texto | Código ANP do produto, com 9 dígitos (por exemplo `320101001`) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 37 |
| `Nome do Produto` | `Nome do Produto` | texto | Nome do produto: nos líquidos, `Diesel A`, `Diesel B`, `Gasolina A`, `Gasolina C`, `EAC`, `EHC`, `Etanol Hidratado`, `OC` (óleo combustível) e `Querosene Iluminante`; nos de aviação, `GAV` e `QAV`; no GLP, `GLP`, `PROPANO`, `BUTANO` e as versões especiais; no asfalto, quatro grupos; nos TRR, nove grupos de produto; nos solventes, de 13 a 17 solventes (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 31 |
| `Código Agente Regulado` | `Código Agente Regulado` | texto | Código ANP do agente regulado (de 7 a 10 dígitos nos valores observados), só na tabela de fornecedores de etanol (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados` |
| `Agente Regulado` | `Agente Regulado` | texto | Razão social do agente regulado que fez a movimentação: distribuidor, TRR, produtor, fornecedor de etanol, rerrefinador ou coletor, conforme a tabela; em empresas individuais pode ser o nome do titular (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 19 |
| `Região Origem` | `Região Origem` | texto | Grande região de origem da movimentação, em sigla (deduzida do nome e dos valores observados) | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; NI = região não informada | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 19 |
| `Região Destinatário` | `Região Destinatário` | texto | Grande região do destinatário, em sigla (`NI` quando não informada) (deduzida do nome e dos valores observados) | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; NI = região não informada | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 18 |
| `Mercado Destinatário` | `Mercado Destinatário` | texto | Mercado do destinatário: consumidor final, posto de combustíveis (bandeirado ou bandeira branca), TRR, revenda de GLP, consumidor industrial, abastecimento de aeronaves, vendas internas e, nos produtores de solventes, listas de mercados concatenadas entre `:` (por exemplo `:AGENTE DE COMÉRCIO EXTERIOR:,:CONSUMIDOR INDUSTRIAL:`) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados`, `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico` e mais 21 |
| `Quantidade de Produto (mil m³)` | `Quantidade de Produto (mil m³)` | texto | Quantidade de produto movimentada no mês, em mil m³ (milhares de metros cúbicos), em texto com vírgula decimal e seis casas; pode ser negativa (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados`, `movimentacao-derivados-aviacao-entregas-distribuidor-atual`, `movimentacao-derivados-aviacao-entregas-fornecedor-atual` e mais 21 |
| `Quantidade de Produto(mil ton)` | `Quantidade de Produto(mil ton)` | texto | Quantidade de produto movimentada no mês, em mil toneladas, em texto com vírgula decimal e seis casas; pode ser negativa (asfalto e GLP) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-asfalto-vendas-distribuidor-atual`, `movimentacao-derivados-asfalto-vendas-distribuidor-historico`, `movimentacao-derivados-asfalto-vendas-distribuidor-uf-atual` e mais 5 |
| `UF Origem` | `UF Origem` | texto | Sigla da UF de origem (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-asfalto-vendas-distribuidor-historico`, `movimentacao-derivados-aviacao-entregas-historico`, `movimentacao-derivados-aviacao-vendas-historico` e mais 12 |
| `UF Destino` | `UF Destino` | texto | Sigla da UF de destino (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-asfalto-vendas-distribuidor-historico`, `movimentacao-derivados-aviacao-entregas-historico`, `movimentacao-derivados-aviacao-vendas-historico` e mais 12 |
| `UF de Origem` | `UF de Origem` | texto | Sigla da UF de origem (tabelas por UF e anexo A de lubrificantes) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-asfalto-vendas-distribuidor-uf-atual`, `movimentacao-derivados-aviacao-vendas-uf-atual`, `movimentacao-derivados-glp-vendas-atual` e mais 8 |
| `UF de Destino` | `UF de Destino` | texto | Sigla da UF de destino (tabelas por UF e vendas de GLP) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-asfalto-vendas-distribuidor-uf-atual`, `movimentacao-derivados-aviacao-vendas-uf-atual`, `movimentacao-derivados-glp-vendas-atual` e mais 6 |
| `Distribuidor` | `Distribuidor` | texto | Razão social do distribuidor (tabelas de entregas e de importação) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-aviacao-entregas-distribuidor-atual`, `movimentacao-derivados-glp-entregas-distribuidor-atual`, `movimentacao-derivados-liquidos-entregas-distribuidor-atual` e mais 1 |
| `Região` | `Região` | texto | Grande região do Brasil, em sigla (entregas e anexo J e importação) (deduzida do nome e dos valores observados) | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; NI = região não informada | — | `movimentacao-derivados-aviacao-entregas-distribuidor-atual`, `movimentacao-derivados-aviacao-entregas-fornecedor-atual`, `movimentacao-derivados-glp-entregas-distribuidor-atual` e mais 5 |
| `Fornecedor` | `Fornecedor` | texto | Razão social do fornecedor (tabelas de entregas por fornecedor) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-aviacao-entregas-fornecedor-atual`, `movimentacao-derivados-glp-entregas-fornecedor-atual`, `movimentacao-derivados-liquidos-entregas-fornecedor-atual` |
| `Fornecedor Destino` | `Fornecedor Destino` | texto | Razão social do fornecedor de destino da entrega (tabelas históricas de entregas) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-aviacao-entregas-historico`, `movimentacao-derivados-glp-entregas-historico`, `movimentacao-derivados-liquidos-entregas-historico` |
| `Distribuidor Origem` | `Distribuidor Origem` | texto | Razão social do distribuidor de origem da entrega (tabelas históricas de entregas) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-aviacao-entregas-historico`, `movimentacao-derivados-glp-entregas-historico`, `movimentacao-derivados-liquidos-entregas-historico` |
| `Localidade Destino` | `Localidade Destino` | texto | Município e UF de destino da entrega, no formato `MUNICÍPIO, UF` (por exemplo `ARAUCARIA, PR`), nas tabelas históricas de entregas (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-aviacao-entregas-historico`, `movimentacao-derivados-glp-entregas-historico`, `movimentacao-derivados-liquidos-entregas-historico` |
| `Código de Embalagem GLP` | `Código de Embalagem GLP` | texto | Embalagem de GLP, em texto: `A Granel` ou `P <capacidade em kg>` (por exemplo `P 13`, `P 45`) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-glp-entregas-distribuidor-atual`, `movimentacao-derivados-glp-entregas-fornecedor-atual`, `movimentacao-derivados-glp-entregas-historico` e mais 2 |
| `Quantidade de Produto (mil ton)` | `Quantidade de Produto (mil ton)` | texto | Quantidade de produto movimentada no mês, em mil toneladas, em texto com vírgula decimal (`glp-entregas-historico`) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-glp-entregas-historico` |
| `Código da Embalagem` | `Código da Embalagem` | texto | Código numérico da embalagem de GLP, só na tabela de vendas por UF (`1` a `43`, sem tabela de códigos) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-glp-vendas-uf-atual` |
| `UF` | `UF` | texto | Sigla da UF do distribuidor, só na tabela de importação (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-liquidos-importacao-distribuidores` |
| `Descrição do Produto` | `Descrição do Produto` | texto | Descrição detalhada do produto: nos líquidos, o tipo e a especificação (por exemplo `ÓLEO DIESEL A S10`); nos lubrificantes, o grupo ou tipo de óleo (`CICLO OTTO`, `ÓLEOS BÁSICOS - GRUPO I`, `BS 150`) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-liquidos-importacao-distribuidores`, `movimentacao-derivados-liquidos-vendas-atual`, `movimentacao-derivados-liquidos-vendas-historico` e mais 6 |
| `Quantidade de produto (mil m³)` | `Quantidade de produto (mil m³)` | texto | Quantidade de produto importada no mês, em mil m³, em texto com vírgula decimal; só na tabela de importação (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-liquidos-importacao-distribuidores` |
| `Período` | `Período` | texto | Ano e mês de referência, no formato `AAAA/MM` (tabelas de logística) | — | — | `movimentacao-derivados-logistica-abastecimento-nacional`, `movimentacao-derivados-logistica-vendas-congeneres`, `movimentacao-derivados-logistica-vendas-mercado` |
| `Produto` | `Produto` | texto | Nome do produto (tabelas de logística, 24 a 62 valores por tabela) | — | — | `movimentacao-derivados-logistica-abastecimento-nacional`, `movimentacao-derivados-logistica-vendas-congeneres`, `movimentacao-derivados-logistica-vendas-mercado` |
| `Classificação` | `Classificação` | texto | Nome da operação realizada pelo agente, segundo o metadado da logística: `VENDA FINAL`, `PRODUCAO`, `COMPRA DE DISTRIBUIDORES`, `RECEBIMENTO TRANSFERENCIA DISTRIBUIDORES`, `RECEBIMENTO TRANSPORTE PRIMARIO`, `IMPORTACAO`, `COMPRA CONGENERES PRODUTOR` e as variantes de compra entre congêneres de distribuidores | — | — | `movimentacao-derivados-logistica-abastecimento-nacional` |
| `Sub Classificação` | `Sub Classificação` | texto | Detalha a `Classificação` `VENDA FINAL` (venda para consumidor final, para consumidor final regulado, para posto e agente não regulado, para revenda ou para TRR); nas demais classificações repete o valor da `Classificação` | — | — | `movimentacao-derivados-logistica-abastecimento-nacional` |
| `Operação` | `Operação` | texto | Nas tabelas de logística, a operação detalhada registrada no SIMP; no anexo J, `VENDA` ou `DISPENSADO` (de coleta) | — | — | `movimentacao-derivados-logistica-abastecimento-nacional`, `movimentacao-derivados-lubrificante-anexo-j` |
| `Modal` | `Modal` | texto | Modo de transporte da movimentação (rodoviário, aquaviário, dutoviário, ferroviário, multimodal, cabotagem / longo curso, navegação interior, aéreo, sem modal ou não informado), segundo o metadado da logística | — | — | `movimentacao-derivados-logistica-abastecimento-nacional` |
| `Qtd  Produto Líquido` | `Qtd  Produto Líquido` | texto | Quantidade de produto em litros (número inteiro, em texto), segundo o metadado da logística; o nome tem dois espaços entre `Qtd` e `Produto` | — | — | `movimentacao-derivados-logistica-abastecimento-nacional`, `movimentacao-derivados-logistica-vendas-congeneres`, `movimentacao-derivados-logistica-vendas-mercado` |
| `Vendedor` | `Vendedor` | texto | Razão social do vendedor (tabelas de logística) | — | — | `movimentacao-derivados-logistica-vendas-congeneres`, `movimentacao-derivados-logistica-vendas-mercado` |
| `Comprador` | `Comprador` | texto | Razão social do comprador, nas vendas entre congêneres (logística) | — | — | `movimentacao-derivados-logistica-vendas-congeneres` |
| `Região de Origem` | `Região de Origem` | texto | Grande região de origem: em sigla nas tabelas de TRR, por extenso (`CENTRO OESTE`) nos lubrificantes; atenção: em `trr-vendas-trr-atual` os rótulos de UF e região estão trocados (veja Cuidados de uso) (deduzida do nome e dos valores observados) | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; NI = região não informada | — | `movimentacao-derivados-lubrificante-anexo-a`, `movimentacao-derivados-lubrificante-anexo-b`, `movimentacao-derivados-trr-vendas-distribuidor-atual` e mais 5 |
| `Região do Destinatário` | `Região do Destinatário` | texto | Grande região do destinatário, por extenso (`CENTRO OESTE`), nos lubrificantes; `-` em parte do anexo I (deduzida do nome e dos valores observados) | CENTRO OESTE = Centro-Oeste; NORDESTE = Nordeste; NORTE = Norte; SUDESTE = Sudeste; SUL = Sul; NÃO INFORMADA = não informada | — | `movimentacao-derivados-lubrificante-anexo-a`, `movimentacao-derivados-lubrificante-anexo-b`, `movimentacao-derivados-lubrificante-anexo-d` e mais 2 |
| `UF do Destinatário` | `UF do Destinatário` | texto | Sigla da UF do destinatário (lubrificantes) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-a`, `movimentacao-derivados-lubrificante-anexo-b`, `movimentacao-derivados-lubrificante-anexo-d` e mais 2 |
| `Volume(L)` | `Volume(L)` | texto | Volume em litros (número inteiro, em texto) nos anexos A a E, H e I de lubrificantes (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-a`, `movimentacao-derivados-lubrificante-anexo-b`, `movimentacao-derivados-lubrificante-anexo-c` e mais 4 |
| `Código do Regulado - ANP` | `Código do Regulado - ANP` | texto | Código ANP do agente regulado (de 6 a 10 dígitos nos valores observados), nas tabelas de lubrificantes (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-b`, `movimentacao-derivados-lubrificante-anexo-d`, `movimentacao-derivados-lubrificante-anexo-e` e mais 3 |
| `Região do Produtor` | `Região do Produtor` | texto | Grande região do produtor, por extenso (anexo C) (deduzida do nome e dos valores observados) | CENTRO OESTE = Centro-Oeste; NORDESTE = Nordeste; NORTE = Norte; SUDESTE = Sudeste; SUL = Sul; NÃO INFORMADA = não informada | — | `movimentacao-derivados-lubrificante-anexo-c` |
| `UF do Produtor` | `UF do Produtor` | texto | Sigla da UF do produtor (anexo C) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-c` |
| `Código da Operação` | `Código da Operação` | texto | Código da operação (7 dígitos) nos anexos C e I de lubrificantes (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-c`, `movimentacao-derivados-lubrificante-anexo-i` |
| `Descrição da Operação` | `Descrição da Operação` | texto | Descrição da operação (por exemplo `PRODUÇÃO POR MISTURA`, `COLETA DE ÓLEO LUBRIFICANTE`) nos anexos C e I (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-c`, `movimentacao-derivados-lubrificante-anexo-i` |
| `Região da coleta` | `Região da coleta` | texto | Região da coleta de óleo usado ou contaminado, em sigla (anexo F) (deduzida do nome e dos valores observados) | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; NI = região não informada | — | `movimentacao-derivados-lubrificante-anexo-f` |
| `UF da coleta` | `UF da coleta` | texto | Sigla da UF da coleta (anexo F) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-f` |
| `Código do Município - ANP` | `Código do Município - ANP` | texto | Código do município no cadastro da ANP, numérico (de 1 a 999 nos valores observados; anexo F) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-f` |
| `Código do Município - IBGE` | `Código do Município - IBGE` | texto | Código IBGE do município, com 7 dígitos (anexo F) | — | — | `movimentacao-derivados-lubrificante-anexo-f` |
| `Município da coleta` | `Município da coleta` | texto | Nome do município e UF da coleta, no formato `NOME - UF` (anexo F) | — | — | `movimentacao-derivados-lubrificante-anexo-f` |
| `Volume coletado(L)` | `Volume coletado(L)` | texto | Volume de óleo lubrificante usado ou contaminado coletado no município, em litros (anexo F) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-f` |
| `Região da Coleta` | `Região da Coleta` | texto | Região da coleta de óleo usado ou contaminado, em sigla (anexo G) (deduzida do nome e dos valores observados) | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; NI = região não informada | — | `movimentacao-derivados-lubrificante-anexo-g` |
| `UF da Coleta` | `UF da Coleta` | texto | Sigla da UF da coleta (anexo G) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-g` |
| `Volume Coletado(L)` | `Volume Coletado(L)` | texto | Volume de óleo lubrificante usado ou contaminado coletado, em litros (anexo G) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-g` |
| `Coletor` | `Coletor` | texto | Nome do coletor de óleo lubrificante usado ou contaminado que recebeu o certificado (anexo H) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-h` |
| `UF do certificado` | `UF do certificado` | texto | Sigla da UF do certificado de recebimento no rerrefino (anexo H); vazia em 16 linhas (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-h` |
| `Volume(mil m³)` | `Volume(mil m³)` | texto | Volume em mil m³, em texto com vírgula decimal (anexo J) (deduzida do nome e dos valores observados) | — | — | `movimentacao-derivados-lubrificante-anexo-j` |
| `Região de Destino` | `Região de Destino` | texto | Grande região de destino, em sigla (tabelas de TRR); atenção: em `trr-vendas-trr-atual` os rótulos de UF e região estão trocados (deduzida do nome e dos valores observados) | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; NI = região não informada | — | `movimentacao-derivados-trr-vendas-distribuidor-atual`, `movimentacao-derivados-trr-vendas-distribuidor-historico`, `movimentacao-derivados-trr-vendas-distribuidor-uf-atual` e mais 3 |

## No lake

- 47 datasets sem partições, um por CSV da fonte: `anp/movimentacao-derivados-<segmento>-<tabela>/mdpg-<pacote>__<arquivo>.parquet` (por exemplo `mdpg-trr__trr_vendas_dist_historico.parquet`) e `anp/movimentacao-derivados/mdpg-fornecedores.parquet`; o histórico de vendas de líquidos tem dois Parquet (2007 a 2017 e 2018 a 2023) no mesmo dataset.
- Todas as colunas são texto, inclusive ano, mês e quantidades. Os nomes das colunas são os do cabeçalho do CSV, com acentos e espaços; em quatro tabelas (`aviacao-vendas-uf-atual`, `lubrificante-anexo-b`, `solvente-vendas-distribuidor-uf-atual`, `trr-vendas-distribuidor-uf-atual`) o nome da coluna de ano é ` Ano`, com espaço no início.
- O conversor decodifica os CSV de ISO-8859 para UTF-8 e não altera os valores.

## Cuidados de uso

- **Escolha uma tabela por pergunta.** `atual` e `historico` do mesmo segmento são períodos consecutivos (2007 a 2023 e 2024 a 2026), mas com colunas diferentes (o `atual` não tem UF por agente); as tabelas `uf-atual` repetem as vendas do `atual` agregadas por UF. Somar tabelas diferentes conta a mesma venda duas ou três vezes.
- **Três unidades.** Quantidades em mil m³ (líquidos, aviação, solventes, TRR e etanol), em mil toneladas (asfalto e GLP), em litros (lubrificantes e logística) e, no anexo J, em mil m³. Não some colunas de quantidade de tabelas diferentes sem converter.
- **Texto com vírgula decimal.** Converta com `replace(col, ',', '.')::DOUBLE`; na logística e nos lubrificantes os valores são inteiros em texto.
- **Rótulos trocados em `trr-vendas-trr-atual`.** O cabeçalho do CSV traz `UF de Origem`, `Região de Origem`, `UF de Destino`, `Região de Destino`, mas os valores vêm na ordem região, UF, região, UF (`SE`, `SP`, `SE`, `SP`): `UF de Origem` guarda a região e `Região de Origem` guarda a UF, e o mesmo vale para o destino. As tabelas `trr-vendas-trr-uf-atual` e `trr-vendas-trr-historico` não têm o problema.
- **Estouro de planilha.** No histórico de vendas de asfalto, duas linhas (2007 e 2008, de um distribuidor com destino `NI`) trazem `#############` em lugar da quantidade, marca do Excel para número que não coube na coluna.
- **Mês com grafias diferentes.** `1` a `12` na maioria das tabelas e `01` a `12` nas tabelas por UF e na de importação; em `trr-vendas-distribuidor-historico` as duas grafias aparecem na mesma coluna. Converta com `Mês::INT`.
- **Coluna de ano com espaço.** Em quatro tabelas a coluna é ` Ano`; ao juntar tabelas com `union_by_name`, `Ano` e ` Ano` viram duas colunas.
- **Mercado com listas.** Nas tabelas de solventes de produtores, `Mercado Destinatário` traz listas de mercados concatenadas (`:AGENTE DE COMÉRCIO EXTERIOR:,:CONSUMIDOR INDUSTRIAL:`), em 12 combinações distintas na tabela atual e 29 na histórica.
- **Embalagem de GLP com dois códigos.** `Código de Embalagem GLP` (`P 13`, `A Granel`) nas tabelas de vendas e de entregas e `Código da Embalagem` (números de 1 a 43) na de vendas por UF; a fonte não traz a tabela de correspondência.
- **Valores ausentes sem marca.** `Região do Destinatário` é `-` em parte do anexo I e `UF do Destinatário` e `UF do certificado` ficam vazias em 16 linhas; `UF de Origem` do anexo A fica vazia em 83 linhas; `Região Origem` aparece como `NÃO INFORMADA` nos anexos A e B.
- **Nomes de agentes mudam.** Razões sociais variam de grafia entre tabelas e anos (`PETROBAHIA S/A`, `AIR BP PETROBAHIA LTDA.`); não foi verificada a unicidade.
- **Dados pessoais.** Razão social e código ANP de agentes regulados (pessoas jurídicas, dado público); em empresas individuais a razão social pode ser o nome do titular.

## Exemplos

Vendas de GLP em 2025 por UF de destino (mil toneladas), a partir da tabela de vendas por agente:

```python
import duckdb

duckdb.sql("""
    SELECT "UF de Destino" AS uf,
           sum(replace("Quantidade de Produto(mil ton)", ',', '.')::DOUBLE) AS mil_t
    FROM read_parquet('lake/anp/movimentacao-derivados-glp-vendas-atual/*.parquet')
    WHERE Ano = '2025'
    GROUP BY uf
    ORDER BY mil_t DESC
    LIMIT 5
""").show()
```

Volume vendido em setembro de 2026 por produto na tabela de vendas no mercado brasileiro (litros):

```python
import duckdb

duckdb.sql("""
    SELECT Produto, sum("Qtd  Produto Líquido"::BIGINT) AS litros
    FROM read_parquet('lake/anp/movimentacao-derivados-logistica-vendas-mercado/*.parquet')
    WHERE "Período" = '2026/09'
    GROUP BY Produto
    ORDER BY litros DESC
    LIMIT 5
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-movimentacao-de-derivados-de-petroleo
- Metadado unificado da logística (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/mdpg/metadado-unificado-logistica.pdf
- Os metadados dos demais segmentos estão em ZIP na página oficial (links internos que não resolveram na conferência).
