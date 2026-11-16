---
dataset:
  id: comercializacao-gn
  fonte: anp
  titulo: 'Comercialização de gás natural: preços e volumes por agregação (distribuidoras, produtores e comercializadores)'
  resumo: 'Preço médio ponderado e volume diário de venda de gás natural, por mês, em três tabelas: vendas às distribuidoras e consumidores livres, entre produtores e comercializadores de gás rico e entre comercializadores de gás processado.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/comercializacao-de-gas-natural
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; as três tabelas foram atualizadas em 19/10/2026, segundo a página oficial, e os metadados são de 22/04/2026
  cobertura:
    inicio: 2019-09
    fim: 2026-08
  unidade: o preço médio e o volume diário de venda de gás natural num mês, para uma agregação (região e tipo de mercado, bacia ou total)
  granularidade:
    espacial: região agregada (distribuidoras), bacia agregada (produtores) ou nacional (comercializadores)
    temporal: mês (colunas `Ano` e `Mês`)
  formato_bruto: 3 CSV em UTF-16 little-endian com BOM, separador `;`, CRLF e cabeçalho entre aspas; decimais com vírgula
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 7
  unidades_de_medida:
    Preço em Reais por MMBtu: R$ por MMBtu (com impostos)
    Volume em mil metros cúbicos/dia: mil m³ por dia (média diária do mês)
  dados_pessoais: nenhum
  eras:
  - desde: '2019'
    mudanca: '`cgn-distribuidoras` e `cgn-produtores` começam em setembro de 2019 (84 meses até agosto de 2026)'
  - desde: '2021'
    mudanca: '`cgn-comercializadores` começa em dezembro de 2021 (57 meses até agosto de 2026)'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Comercialização de gás natural: preços e volumes por agregação (distribuidoras, produtores e comercializadores)

## Resumo

Dados abertos de comercialização de gás natural divulgados mensalmente pela ANP a partir de informações declaradas pelas empresas (art. 12 da Resolução ANP nº 52/2011), em três tabelas: (1) vendas de gás natural às distribuidoras e consumidores livres autorizados pelos estados, agregadas por região e tipo de mercado (térmico ou não térmico); (2) vendas entre produtores e comercializadores de gás rico (não processado), agregadas por bacia sedimentar; e (3) vendas de gás processado entre comercializadores, na saída das unidades de processamento, terminais de GNL ou pontos de entrada e saída do sistema de transporte. As agregações existem para preservar o sigilo comercial dos agentes; cada linha traz o preço médio ponderado pelo volume e o volume médio diário do mês.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/comercializacao-gn` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/comercializacao-de-gas-natural |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; as três tabelas foram atualizadas em 19/10/2026, segundo a página oficial, e os metadados são de 22/04/2026 |
| Cobertura | 2019-09 a 2026-08 |
| Unidade (uma linha) | o preço médio e o volume diário de venda de gás natural num mês, para uma agregação (região e tipo de mercado, bacia ou total) |
| Granularidade | espacial: região agregada (distribuidoras), bacia agregada (produtores) ou nacional (comercializadores); temporal: mês (colunas `Ano` e `Mês`) |
| Formato bruto | 3 CSV em UTF-16 little-endian com BOM, separador `;`, CRLF e cabeçalho entre aspas; decimais com vírgula |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 7 |
| Unidades de medida | `Preço em Reais por MMBtu`: R$ por MMBtu (com impostos); `Volume em mil metros cúbicos/dia`: mil m³ por dia (média diária do mês) |
| Dados pessoais | nenhum |
| Eras | 2019: `cgn-distribuidoras` e `cgn-produtores` começam em setembro de 2019 (84 meses até agosto de 2026); 2021: `cgn-comercializadores` começa em dezembro de 2021 (57 meses até agosto de 2026) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa três arquivos de `https://www.gov.br/anp/pt-br/assuntos/movimentacao-estocagem-e-comercializacao-de-gas-natural/acompanhamento-do-mercado-de-gas-natural/ppg/`: `distribuidoras-consumidores-livres.csv` (vendas às distribuidoras e consumidores livres), `vendas-aos-comercializadores.csv` (vendas entre comercializadores de gás processado) e `vendas-entre-produtores.csv` (vendas entre produtores e comercializadores de gás rico); todos atualizados em 19/10/2026 segundo a página oficial.
- No bruto os arquivos se chamam `cgn-distribuidoras@AAAAMMDD.csv` (40.908 bytes, 420 linhas de dados), `cgn-comercializadores@AAAAMMDD.csv` (2.284 bytes, 57 linhas) e `cgn-produtores@AAAAMMDD.csv` (14.906 bytes, 252 linhas), em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download. Os arquivos estão em UTF-16, o que o conversor lê corretamente.
- Metadados em PDF (22/04/2026, Superintendência de Infraestrutura e Movimentação, SIM/ANP): `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-comercializacao-de-gas-natural/metadados-vendas-distribuidoras-ou-consumidores-livres.pdf`, `.../metadados-vendas-entre-produtores.pdf` e `.../metadados-vendas-aos-comercializadores.pdf`. Fonte do dado: SIM/ANP, dado declaratório das empresas (art. 12 da Resolução ANP nº 52/2011).
- A página oficial remete ao Boletim Mensal de Comercialização de Gás Natural para mais informações.

## Conteúdo

- **Três tabelas num dataset.** O lake guarda um Parquet por tabela, e a coluna *Arquivos* do dicionário mostra a que tabela cada coluna pertence; `Ano`, `Mês`, o preço e o volume existem nas três.

| Tabela (Parquet) | O que é uma linha | Linhas | Período | Colunas próprias |
|---|---|---|---|---|
| `cgn-distribuidoras` | vendas a distribuidoras e consumidores livres, num mês, por tipo de mercado e região agregada | 420 | 2019-09 a 2026-08 | `TipoMercado`, `RegiãoAgregada` |
| `cgn-produtores` | vendas entre produtores e comercializadores de gás rico, num mês, por bacia agregada | 252 | 2019-09 a 2026-08 | `BaciaAgregada` |
| `cgn-comercializadores` | vendas de gás processado entre comercializadores, num mês (total nacional) | 57 | 2021-12 a 2026-08 | nenhuma |

- **Agregações.** Em `cgn-distribuidoras` há cinco grupos por mês: mercado Não Térmico em Norte-Nordeste, Sudeste e Sul-Centro-Oeste e mercado Térmico em Norte-Nordeste e Sudeste-Sul-Centro-Oeste (84 meses vezes 5 grupos = 420 linhas). Em `cgn-produtores` há três por mês: Santos, Campos e Demais Bacias (84 vezes 3 = 252).
- **Chaves.** Em cada tabela, `Ano`, `Mês` e as colunas de agregação identificam a linha (420, 252 e 57 combinações distintas em 420, 252 e 57 linhas).
- **Preço ausente.** `Preço em Reais por MMBtu` vem vazio em 94 das 420 linhas de `cgn-distribuidoras` e em 13 das 252 de `cgn-produtores`; as 57 linhas de `cgn-comercializadores` têm preço.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `cgn-comercializadores` (4); `cgn-distribuidoras` (6); `cgn-produtores` (5) |

## Variáveis

As descrições vêm dos três documentos de metadados da ANP (22/04/2026), que descrevem as mesmas variáveis. Os nomes das colunas do lake são os do cabeçalho de cada arquivo (por exemplo, o metadado "Tipo Mercado" é a coluna `TipoMercado`).
Todas as colunas são texto, inclusive o preço (com vírgula decimal) e o volume.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Ano` | `Ano` | texto | Ano de comercialização do gás (texto) | — | — | `cgn-comercializadores`, `cgn-distribuidoras`, `cgn-produtores` |
| `Mês` | `Mês` | texto | Mês de comercialização do gás, de 1 a 12 e sem zero à esquerda (texto) | — | — | `cgn-comercializadores`, `cgn-distribuidoras`, `cgn-produtores` |
| `Preço em Reais por MMBtu` | `Preço em Reais por MMBtu` | texto | Preço médio de venda do gás natural, ponderado pelo volume comercializado na agregação da linha (região agregada, bacia agregada ou total, conforme a tabela), com impostos, em reais por milhão de BTU (MMBtu); texto com vírgula decimal, vazio em parte das linhas | — | — | `cgn-comercializadores`, `cgn-distribuidoras`, `cgn-produtores` |
| `Volume em mil metros cúbicos/dia` | `Volume em mil metros cúbicos/dia` | texto | Média diária de venda do gás natural, em mil metros cúbicos (1.000 m³) por dia; texto com número inteiro | — | — | `cgn-comercializadores`, `cgn-distribuidoras`, `cgn-produtores` |
| `TipoMercado` | `TipoMercado` | texto | Tipo do mercado atendido pela venda do gás: termelétrico ou não termelétrico (`cgn-distribuidoras`). Os metadados chamam o campo de "Tipo Mercado" | Térmico = mercado termelétrico; Não Térmico = mercado não termelétrico | — | `cgn-distribuidoras` |
| `RegiãoAgregada` | `RegiãoAgregada` | texto | Agregação das regiões geográficas brasileiras (`cgn-distribuidoras`); depende do tipo de mercado | Norte-Nordeste = Norte e Nordeste (os dois mercados); Sudeste = só no mercado não térmico; Sul-Centro-Oeste = só no mercado não térmico; Sudeste-Sul-Centro-Oeste = só no mercado térmico | — | `cgn-distribuidoras` |
| `BaciaAgregada` | `BaciaAgregada` | texto | Agregação das bacias sedimentares brasileiras (`cgn-produtores`); `Demais Bacias` reúne todas as bacias que não sejam Santos e Campos | Santos = Bacia de Santos; Campos = Bacia de Campos; Demais Bacias = todas as outras bacias sedimentares | — | `cgn-produtores` |

## No lake

- Dataset `anp/comercializacao-gn`, sem partições: três Parquet, `cgn-distribuidoras.parquet`, `cgn-comercializadores.parquet` e `cgn-produtores.parquet`, cada um com as colunas do respectivo CSV, todas como texto.
- O conversor lê o UTF-16 e remove as aspas do cabeçalho; os números não são convertidos (o preço mantém a vírgula decimal).

## Cuidados de uso

- **Números são texto com vírgula.** Troque a vírgula por ponto e converta (`try_cast(replace("Preço em Reais por MMBtu", ',', '.') AS DOUBLE)`); `Mês` não tem zero à esquerda, então ordene por `try_cast("Mês" AS INT)`.
- **O preço é médio ponderado de uma agregação, não um preço de contrato.** Os dados são declaratórios, agregados para preservar o sigilo comercial; o preço inclui impostos e o volume é uma média diária do mês.
- **Preço vazio.** 94 linhas de `cgn-distribuidoras` e 13 de `cgn-produtores` não têm preço; não use zero no lugar.
- **Agregações diferentes em cada mercado.** `Sudeste` e `Sul-Centro-Oeste` só existem no mercado Não Térmico, e `Sudeste-Sul-Centro-Oeste` só no Térmico; compare regiões dentro do mesmo tipo de mercado.
- **Valor atípico em `cgn-comercializadores`.** O preço de dezembro de 2021 (206,6 R$/MMBtu) é mais que o dobro do de janeiro de 2022 (99,2); a fonte não comenta, e o valor não foi verificado.
- **Defasagem.** As tabelas vão até agosto de 2026 e foram atualizadas em 19/10/2026; o último mês pode ser revisado.
- **Dados pessoais.** Não há identificação de empresas (os dados são agregados por região, bacia ou total).

## Exemplos

Preço médio ponderado simples do gás vendido às distribuidoras no mercado não térmico por região agregada, em 2025:

```python
import duckdb

duckdb.sql("""
    SELECT "RegiãoAgregada" AS regiao,
           count(*) AS meses,
           round(avg(try_cast(replace("Preço em Reais por MMBtu", ',', '.') AS DOUBLE)), 2) AS preco_medio_rs_mmbtu,
           round(avg(try_cast("Volume em mil metros cúbicos/dia" AS DOUBLE))) AS volume_medio_mil_m3_dia
    FROM read_parquet('lake/anp/comercializacao-gn/cgn-distribuidoras.parquet')
    WHERE "Ano" = '2025' AND "TipoMercado" = 'Não Térmico'
    GROUP BY regiao
    ORDER BY regiao
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/comercializacao-de-gas-natural
- Metadados das vendas às distribuidoras ou consumidores livres: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-comercializacao-de-gas-natural/metadados-vendas-distribuidoras-ou-consumidores-livres.pdf
- Metadados das vendas entre produtores: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-comercializacao-de-gas-natural/metadados-vendas-entre-produtores.pdf
- Metadados das vendas aos comercializadores: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-comercializacao-de-gas-natural/metadados-vendas-aos-comercializadores.pdf
- Resolução ANP nº 52/2011 (art. 12), citada nos metadados como base da natureza declaratória dos dados.
