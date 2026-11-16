---
dataset:
  id: vdpb-abertos
  fonte: anp
  titulo: Vendas de derivados de petróleo e biocombustíveis (dados abertos)
  resumo: Vendas de combustíveis pelas distribuidoras, por mês e UF (1990 em diante), por segmento, tipo, produtor, município (anual) e por estado (1947 a 1989).
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal nos arquivos de vendas por UF, segmento, tipo, produtor e biodiesel (a página informa atualização até o último dia do mês seguinte); anual nos arquivos por município; sem atualização nos arquivos históricos por estado (periodicidade «Não aplicável» nos metadados)
  cobertura:
    inicio: '1947'
    fim: 2026-09
  unidade: 'depende do arquivo: um produto numa UF num mês; uma combinação UF-produto-segmento, tipo ou vasilhame num mês; um município num ano; um estado num ano (1947 a 1989); ou um par região de origem-região de destino num mês (biodiesel)'
  granularidade:
    espacial: Brasil, grande região, UF ou município, conforme o arquivo
    temporal: mês (`ANO` e `MÊS`, ou `Mês/Ano` no biodiesel) ou ano (arquivos por município e por estado)
  formato_bruto: CSV; os de vendas mensais por UF usam `;` e vírgula decimal, UTF-8 com BOM e CRLF; o de biodiesel usa `,` como separador e vírgula decimal entre aspas; 23 arquivos
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 20
  unidades_de_medida:
    VENDAS: m³, litro, kg ou t, conforme o arquivo (veja a tabela em Conteúdo)
    Vendas de Biodiesel: m³
    P13: kg
    OUTROS: kg
  dados_pessoais: nenhum
  eras:
  - desde: '1947'
    mudanca: arquivos históricos por estado (1947 a 1989; etanol de 1980 a 1989; GLP de 1953; querosene de aviação de 1959)
  - desde: '1990'
    mudanca: vendas mensais por UF e produto, e vendas anuais por município, a partir de 1990 (asfalto e GLP municipais a partir de 1992)
  - desde: '2007'
    mudanca: até 2006 a fonte dos dados era o Demonstrativo de Controle de Produtos (DCP) e as vendas incluem o consumo próprio das distribuidoras; a partir de 2007 a fonte é o Sistema de Informações de Movimentação de Produtos (SIMP) e só entram as vendas
  - desde: '2012'
    mudanca: arquivo de vendas por segmento (posto revendedor, TRR e consumidor final) a partir de janeiro de 2012; o de GLP por vasilhame começa em 2007 e o de diesel por tipo em 2013
  - desde: '2017'
    mudanca: arquivo de vendas de biodiesel B100 entre regiões, a partir de janeiro de 2017
  - desde: '2025'
    mudanca: arquivo de vendas de óleo diesel pelos produtores, a partir de janeiro de 2025
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Vendas de derivados de petróleo e biocombustíveis (dados abertos)

## Resumo

Vinte e três arquivos CSV da ANP sobre as vendas de derivados de petróleo e etanol hidratado pelas distribuidoras: o total mensal por UF e produto desde 1990; recortes por segmento comprador, por tipo de diesel e de vasilhame de GLP e por produtor; as vendas de biodiesel B100 entre regiões; as vendas anuais por município de nove produtos; e as vendas anuais por estado de 1947 a 1989. Todos usam as mesmas colunas de ano, mês, região, UF e produto, mas cada arquivo tem a sua unidade de medida e o seu período, listados na tabela de Conteúdo. Os totais mensais em m³ também estão, em planilha, no grupo `vdpb`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/vdpb-abertos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal nos arquivos de vendas por UF, segmento, tipo, produtor e biodiesel (a página informa atualização até o último dia do mês seguinte); anual nos arquivos por município; sem atualização nos arquivos históricos por estado (periodicidade «Não aplicável» nos metadados) |
| Cobertura | 1947 a 2026-09 |
| Unidade (uma linha) | depende do arquivo: um produto numa UF num mês; uma combinação UF-produto-segmento, tipo ou vasilhame num mês; um município num ano; um estado num ano (1947 a 1989); ou um par região de origem-região de destino num mês (biodiesel) |
| Granularidade | espacial: Brasil, grande região, UF ou município, conforme o arquivo; temporal: mês (`ANO` e `MÊS`, ou `Mês/Ano` no biodiesel) ou ano (arquivos por município e por estado) |
| Formato bruto | CSV; os de vendas mensais por UF usam `;` e vírgula decimal, UTF-8 com BOM e CRLF; o de biodiesel usa `,` como separador e vírgula decimal entre aspas; 23 arquivos |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 20 |
| Unidades de medida | `VENDAS`: m³, litro, kg ou t, conforme o arquivo (veja a tabela em Conteúdo); `Vendas de Biodiesel`: m³; `P13`: kg; `OUTROS`: kg |
| Dados pessoais | nenhum |
| Eras | 1947: arquivos históricos por estado (1947 a 1989; etanol de 1980 a 1989; GLP de 1953; querosene de aviação de 1959); 1990: vendas mensais por UF e produto, e vendas anuais por município, a partir de 1990 (asfalto e GLP municipais a partir de 1992); 2007: até 2006 a fonte dos dados era o Demonstrativo de Controle de Produtos (DCP) e as vendas incluem o consumo próprio das distribuidoras; a partir de 2007 a fonte é o Sistema de Informações de Movimentação de Produtos (SIMP) e só entram as vendas; 2012: arquivo de vendas por segmento (posto revendedor, TRR e consumidor final) a partir de janeiro de 2012; o de GLP por vasilhame começa em 2007 e o de diesel por tipo em 2013; 2017: arquivo de vendas de biodiesel B100 entre regiões, a partir de janeiro de 2017; 2025: arquivo de vendas de óleo diesel pelos produtores, a partir de janeiro de 2025 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa 23 CSV: seis mensais em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/` (`vendas-derivados-petroleo-e-etanol`, `vcs`, `vct` com dois arquivos, `vendas-por-produtor` e `vendas-de-biodiesel`), nove municipais anuais (`https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vaehdpm/<produto>/vendas-anuais-de-<produto>-por-municipio.csv`) e oito históricos por estado em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-vendas-anuais-de-etanol-hidratado-e-derivados-de-petroleo-por-estado/`. O nome do arquivo mensal principal (`vendas-combustiveis-m3-1990-2025.csv`) está defasado: o conteúdo vai até setembro de 2026.
- Metadados em PDF para quase todos: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vendas-derivados-petroleo-e-etanol/metadados-vendas-derivados-petroleo-etanol.pdf`, `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vcs/metadados-vendas-combustiveis-por-segmento.pdf`, `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vct/metadados-vendas-glp-por-tipo-vasilhame.pdf`, `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vct/metadados-vendas-oleo-diesel-por-tipo.pdf`, `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vendas-por-produtor/metadados-vendas-oleo-diesel-produtores.pdf`, `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vendas-de-biodiesel/metadados-vendas-biodiesel-b100.pdf`, nove `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vaehdpm/<produto>/metadados-vendas-anuais-de-<produto>-por-municipio.pdf` e oito `metadados-vendas-<produto>-<anos>.pdf` dos históricos por estado.
- Fonte dos dados, segundo os metadados: ANP, conforme as Resoluções ANP nº 17/2014 (vendas mensais por UF) e nº 729/2018 (demais); órgão responsável: Superintendência de Defesa da Concorrência (ANP/SDC), e Superintendência de Produção de Combustíveis (ANP/SPC) para o biodiesel (origem I-SIMP; criado em 18/09/2019, atualizado em 05/03/2026). Os históricos por estado citam a Portaria CNP nº 221, de 25/06/1981, e trazem «vendas ao consumidor mais o consumo próprio das companhias distribuidoras».
- Para converter m³ em barris, os metadados mandam multiplicar por 6,28981. As notas listam também a evolução da mistura obrigatória de biodiesel ao óleo diesel e a de etanol anidro à gasolina C ao longo da série, o que explica parte das variações de volume de cada produto.
- No metadado de GLP por tipo de vasilhame, a ANP avisa que «essas informações são ainda preliminares e poderão sofrer ajustes».

## Conteúdo

- **O que é uma linha.** Depende do arquivo. A coluna `VENDAS` mede o volume vendido, mas muda de unidade (m³, litro, kg, t) de um arquivo para outro, e as colunas que descrevem o recorte (`SEGMENTO`, `VASILHAME`, `ESTADO`, `UF`, `MUNICÍPIO`) existem só em alguns. A tabela abaixo reúne os 23 arquivos do lake (conferidos na amostra de 2026-11-15).

| Arquivo no lake (`vdpb-a-…`) | Conteúdo | Período | Unidade de `VENDAS` | Linhas |
|---|---|---|---|---|
| `combustiveis-m3` | derivados e etanol hidratado por UF e produto (8 produtos) | 1990-01 a 2026-09 | m³ | 95.256 |
| `segmento` | etanol hidratado, gasolina C e óleo diesel por UF e segmento | 2012-01 a 2026-09 | m³ | 43.011 |
| `glp-tipo` | GLP por UF e vasilhame | 2007-01 a 2026-09 | m³ | 12.798 |
| `diesel-tipo` | óleo diesel por UF e tipo (S-10, S-500, S-1800, marítimo, outros) | 2013-01 a 2026-09 | m³ | 22.275 |
| `diesel-produtor` | óleo diesel vendido pelos produtores, por UF | 2025-01 a 2026-09 | m³ | 567 |
| `biodiesel` | biodiesel B100 por região de origem e de destino (colunas próprias) | 2017-01 a 2026-09 | m³ | 1.949 |
| `muni-asfalto` | asfalto, anual, por município | 1992 a 2024 | kg | 57.595 |
| `muni-etanol-hidratado` | etanol hidratado, anual, por município | 1990 a 2024 | litro | 160.692 |
| `muni-gasolina-c` | gasolina C, anual, por município | 1990 a 2024 | litro | 180.839 |
| `muni-gasolina-aviacao` | gasolina de aviação, anual, por município | 1990 a 2024 | litro | 13.904 |
| `muni-glp` | GLP, anual, por município, em `P13` e `OUTROS` (sem `VENDAS`) | 1992 a 2024 | kg | 142.290 |
| `muni-oleo-combustivel` | óleo combustível, anual, por município | 1990 a 2024 | kg | 25.829 |
| `muni-oleo-diesel` | óleo diesel, anual, por município | 1990 a 2024 | litro | 182.878 |
| `muni-querosene-aviacao` | querosene de aviação, anual, por município | 1990 a 2024 | litro | 9.515 |
| `muni-querosene-iluminante` | querosene iluminante, anual, por município | 1990 a 2024 | litro | 15.133 |
| `hist-etanol` | etanol hidratado, anual, por estado | 1980 a 1989 | m³ | 270 |
| `hist-gasolina-c` | gasolina C, anual, por estado | 1947 a 1989 | m³ | 1.161 |
| `hist-gasolina-aviacao` | gasolina de aviação, anual, por estado | 1947 a 1989 | m³ | 1.156 |
| `hist-glp` | GLP, anual, por estado | 1953 a 1989 | t | 999 |
| `hist-oleo-combustivel` | óleo combustível, anual, por estado | 1947 a 1989 | t | 1.203 |
| `hist-oleo-diesel` | óleo diesel, anual, por estado | 1947 a 1989 | m³ | 1.161 |
| `hist-querosene-aviacao` | querosene de aviação, anual, por estado | 1959 a 1989 | m³ | 836 |
| `hist-querosene-iluminante` | querosene iluminante, anual, por estado | 1947 a 1989 | m³ | 1.161 |

- **Mesma venda, três recortes.** Os totais municipais batem com os mensais: a soma de `VENDAS` da gasolina C municipal em 2023 e 2024 (46.029.714.283 e 44.405.318.037 litros) é igual à soma de `GASOLINA C` em m³ do arquivo mensal por UF (46.029.714 e 44.405.318 m³). Não some um arquivo com o outro.
- **Chave.** Os arquivos mensais por UF têm chave própria (`ANO`, `MÊS`, UF e produto, segmento, tipo ou vasilhame; ou `Mês/Ano` e as duas regiões no biodiesel), conferida sem repetição na amostra; como as colunas diferem de arquivo para arquivo, a chave do conjunto não é declarada.
- **Cobertura mensal completa.** `vdpb-a-combustiveis-m3` tem 27 UFs em todos os meses de 1990-01 a 2026-09; em 2026, os nove meses de janeiro a setembro têm 216 linhas cada.

## Variáveis

As descrições vêm dos metadados da ANP. O mesmo nome de coluna pode ter unidade ou formato diferente entre arquivos (veja a coluna Arquivos): `VENDAS` sobretudo, e `GRANDE REGIÃO` (`REGIÃO NORTE` nos mensais e municipais; `Região Norte` nos históricos).
`ANO`, `MÊS`, `CÓDIGO IBGE` e os nomes são texto; os volumes são decimais. Os metadados do GLP municipal citam uma coluna `TOTAL` que não existe no arquivo.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Mês/Ano` | `Mês/Ano` | texto | Mês de referência das vendas de biodiesel B100, no formato `MM/AAAA` | — | — | `vdpb-a-biodiesel` |
| `Região Origem` | `Região Origem` | texto | Região dos produtores responsáveis pela venda do biodiesel B100 | CENTRO OESTE = Centro-Oeste; NORDESTE = Nordeste; NORTE = Norte; SUDESTE = Sudeste; SUL = Sul | — | `vdpb-a-biodiesel` |
| `Região Destino` | `Região Destino` | texto | Região das empresas que compraram o biodiesel B100 | CENTRO OESTE = Centro-Oeste; NORDESTE = Nordeste; NORTE = Norte; SUDESTE = Sudeste; SUL = Sul; NÃO INFORMADA = região não informada | — | `vdpb-a-biodiesel` |
| `Vendas de Biodiesel` | `Vendas de Biodiesel` | decimal | Volume de biodiesel B100 comercializado no mês entre a região de origem e a de destino, em m³ | — | — | `vdpb-a-biodiesel` |
| `ANO` | `ANO` | texto | Ano de referência, com quatro dígitos | — | — | `vdpb-a-combustiveis-m3`, `vdpb-a-diesel-produtor`, `vdpb-a-diesel-tipo` e mais 19 |
| `MÊS` | `MÊS` | texto | Mês de referência, abreviado em três letras maiúsculas | JAN = janeiro; FEV = fevereiro; MAR = março; ABR = abril; MAI = maio; JUN = junho; JUL = julho; AGO = agosto; SET = setembro; OUT = outubro; NOV = novembro; DEZ = dezembro | — | `vdpb-a-combustiveis-m3`, `vdpb-a-diesel-produtor`, `vdpb-a-diesel-tipo` e mais 2 |
| `GRANDE REGIÃO` | `GRANDE REGIÃO` | texto | Grande região do Brasil; nos arquivos históricos por estado a grafia é `Região Norte`, `Região Sul` etc., e nos demais é `REGIÃO NORTE`, `REGIÃO SUL` etc. | REGIÃO CENTRO-OESTE = Centro-Oeste; REGIÃO NORDESTE = Nordeste; REGIÃO NORTE = Norte; REGIÃO SUDESTE = Sudeste; REGIÃO SUL = Sul | — | `vdpb-a-combustiveis-m3`, `vdpb-a-diesel-tipo`, `vdpb-a-glp-tipo` e mais 17 |
| `UNIDADE DA FEDERAÇÃO` | `UNIDADE DA FEDERAÇÃO` | texto | Nome da unidade da federação (por exemplo `ACRE`, `SÃO PAULO`), em maiúsculas | — | — | `vdpb-a-combustiveis-m3`, `vdpb-a-diesel-tipo`, `vdpb-a-glp-tipo` e mais 1 |
| `PRODUTO` | `PRODUTO` | texto | Nome do produto vendido: nos arquivos mensais por UF, `ETANOL HIDRATADO`, `GASOLINA C`, `GASOLINA DE AVIAÇÃO`, `GLP`, `ÓLEO COMBUSTÍVEL`, `ÓLEO DIESEL`, `QUEROSENE DE AVIAÇÃO` e `QUEROSENE ILUMINANTE`; no de diesel por tipo, `ÓLEO DIESEL S-10`, `S-500`, `S-1800`, `MARÍTIMO` e `(OUTROS )`; nos demais, o único produto do arquivo (`ASFALTO` ou `ETANOL`, por exemplo) | — | — | `vdpb-a-combustiveis-m3`, `vdpb-a-diesel-tipo`, `vdpb-a-hist-etanol` e mais 17 |
| `VENDAS` | `VENDAS` | decimal | Volume vendido pelas distribuidoras no período da linha; a unidade depende do arquivo (m³ nos arquivos mensais e nos históricos de etanol, gasolina, óleo diesel e querosene; litros nos municipais de etanol, gasolina, diesel e querosene; kg nos municipais de asfalto e óleo combustível; toneladas nos históricos de GLP e óleo combustível; veja a tabela em Conteúdo) | — | — | `vdpb-a-combustiveis-m3`, `vdpb-a-diesel-produtor`, `vdpb-a-diesel-tipo` e mais 18 |
| `COMBUSTÍVEL` | `COMBUSTÍVEL` | texto | Nome do combustível (nesse arquivo, só `ÓLEO DIESEL`) | — | — | `vdpb-a-diesel-produtor` |
| `REGIÃO` | `REGIÃO` | texto | Grande região da unidade da federação (arquivo de diesel por produtor) | REGIÃO CENTRO-OESTE = Centro-Oeste; REGIÃO NORDESTE = Nordeste; REGIÃO NORTE = Norte; REGIÃO SUDESTE = Sudeste; REGIÃO SUL = Sul | — | `vdpb-a-diesel-produtor` |
| `ESTADO` | `ESTADO` | texto | Nome do estado: em maiúsculas no arquivo de diesel por produtor (`ACRE`) e com inicial maiúscula nos históricos (`Rio de Janeiro`, e `Guanabara` no de óleo combustível) | — | — | `vdpb-a-diesel-produtor`, `vdpb-a-hist-etanol`, `vdpb-a-hist-gasolina-aviacao` e mais 6 |
| `VASILHAME` | `VASILHAME` | texto | Tipo de vasilhame de GLP | GLP - Até P13 = inclui P2, P5, P7, P8 e P13; GLP - Outros = inclui P20, P45, P90 e granel | — | `vdpb-a-glp-tipo` |
| `UF` | `UF` | texto | Sigla da unidade da federação do município; vazia em algumas linhas (veja Cuidados de uso) | — | — | `vdpb-a-muni-asfalto`, `vdpb-a-muni-etanol-hidratado`, `vdpb-a-muni-gasolina-aviacao` e mais 6 |
| `CÓDIGO IBGE` | `CÓDIGO IBGE` | texto | Código IBGE do município, com 7 dígitos; algumas linhas trazem outros códigos (veja Cuidados de uso) | — | — | `vdpb-a-muni-asfalto`, `vdpb-a-muni-etanol-hidratado`, `vdpb-a-muni-gasolina-aviacao` e mais 6 |
| `MUNICÍPIO` | `MUNICÍPIO` | texto | Nome do município, em maiúsculas e em geral sem acentos; `*` marca vendas não atribuídas a um município da UF | — | — | `vdpb-a-muni-asfalto`, `vdpb-a-muni-etanol-hidratado`, `vdpb-a-muni-gasolina-aviacao` e mais 6 |
| `P13` | `P13` | decimal | Total vendido em vasilhames até P13, em kg (arquivo municipal de GLP) | — | — | `vdpb-a-muni-glp` |
| `OUTROS` | `OUTROS` | decimal | Total vendido em outros vasilhames (acima de P13 e granel), em kg (arquivo municipal de GLP) | — | — | `vdpb-a-muni-glp` |
| `SEGMENTO` | `SEGMENTO` | texto | Segmento comprador | POSTO REVENDEDOR = posto revendedor; TRR = transportador-revendedor-retalhista; CONSUMIDOR FINAL = consumidor final | — | `vdpb-a-segmento` |

## No lake

- Dataset `anp/vdpb-abertos`, sem partições; um Parquet por arquivo da fonte (`vdpb-a-combustiveis-m3.parquet`, `vdpb-a-muni-gasolina-c.parquet`, `vdpb-a-hist-glp.parquet` e assim por diante).
- O lake guarda o conteúdo como está na fonte: as colunas dos 23 arquivos aparecem na união (as que um arquivo não tem ficam vazias ao ler vários juntos com `union_by_name`).

## Cuidados de uso

- **Unidades diferentes na mesma coluna.** `VENDAS` está em m³, litro, kg ou t, conforme o arquivo; converta antes de comparar (1 m³ = 1.000 litros). Os arquivos municipais de asfalto, GLP e óleo combustível estão em kg, não em litros.
- **Defasagem no nome e atraso nos dados.** Os mensais vão até setembro de 2026, mas o nome do principal diz `1990-2025`; os municipais acabam em 2024 (atualizados em 05/01/2026).
- **Quebra de série em 2007.** Até 2006 os volumes incluem o consumo próprio das distribuidoras; de 2007 em diante, só vendas, de outra fonte (SIMP em vez de DCP).
- **Municípios: linhas que não são município.** Nos arquivos municipais há linhas com `MUNICÍPIO` = `*` (vendas não atribuídas a município, com códigos que parecem de UF, como `3500004`, ou de 5 a 6 dígitos, como `96520`), duas linhas de gasolina de aviação com o código `53000108` (Brasília com 8 dígitos) e 17 linhas sem `UF` nos nove arquivos (7 no asfalto, 4 no óleo combustível, 3 na gasolina C, 2 no óleo diesel e 1 no querosene de aviação). Para somar por município, filtre `length("CÓDIGO IBGE") = 7` e `MUNICÍPIO <> '*'`. A combinação `ANO`, `PRODUTO` e `CÓDIGO IBGE` repete-se (788.675 linhas e 760.702 combinações distintas nos nove arquivos).
- **Valores negativos.** Há poucos volumes negativos (3 em `combustiveis-m3`, 8 em `segmento`, 1 em `diesel-tipo`, 8 no asfalto municipal e 3 no querosene de aviação municipal), correções da fonte.
- **GLP municipal sem total.** O arquivo traz `P13` e `OUTROS`, sem `VENDAS`; o total é a soma das duas colunas.
- **Históricos por estado.** Os nomes de estado são os da época (`Guanabara`, `Tocantins` com zeros antes de 1988); Roraima falta em um ano no óleo combustível (42 linhas contra 43).
- **Dados pessoais.** Nenhum: são totais por UF, município ou estado.

## Exemplos

Vendas anuais de gasolina C (m³) por grande região, a partir do arquivo mensal por UF:

```python
import duckdb

duckdb.sql("""
    SELECT ANO, "GRANDE REGIÃO", sum(VENDAS) AS m3
    FROM read_parquet('lake/anp/vdpb-abertos/vdpb-a-combustiveis-m3.parquet')
    WHERE PRODUTO = 'GASOLINA C' AND ANO IN ('2023', '2024')
    GROUP BY ALL
    ORDER BY ANO, m3 DESC
""").show()
```

Os cinco maiores municípios em vendas de gasolina C (litros) em 2024, sem as linhas `*`:

```python
import duckdb

duckdb.sql("""
    SELECT UF, "MUNICÍPIO", VENDAS AS litros
    FROM read_parquet('lake/anp/vdpb-abertos/vdpb-a-muni-gasolina-c.parquet')
    WHERE ANO = '2024' AND length("CÓDIGO IBGE") = 7 AND "MUNICÍPIO" <> '*'
    ORDER BY VENDAS DESC
    LIMIT 5
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/vdpb/vendas-derivados-petroleo-e-etanol/metadados-vendas-derivados-petroleo-etanol.pdf (os demais estão na página oficial)
- Grupo `vdpb`: totais mensais em planilha (dados estatísticos) e vendas municipais anuais em xls/xlsx (2000 a 2024).
