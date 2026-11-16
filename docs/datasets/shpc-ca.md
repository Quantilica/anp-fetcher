---
dataset:
  id: shpc-ca
  fonte: anp
  titulo: SHPC — Preços de combustíveis automotivos, série semestral (2004 em diante)
  resumo: Preços de revenda de gasolina, gasolina aditivada, etanol, diesel e GNV coletados semanalmente pela ANP, em arquivos semestrais desde o 1º semestre de 2004.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semestral (arquivos por semestre, com preços coletados semanalmente); o catálogo do fetcher vai do 1º semestre de 2004 ao 2º de 2025, e a página oficial já lista o 1º semestre de 2026
  cobertura:
    inicio: '2004'
    fim: '2025'
  unidade: um preço de venda de um produto, coletado em uma revenda em uma data (uma linha por revenda, produto e data de coleta)
  granularidade:
    espacial: revenda (CNPJ e endereço completo), com município, UF e região
    temporal: data da coleta (dia)
  formato_bruto: CSV (36 arquivos) ou ZIP com um CSV (8 arquivos, de 2022 a 2025), um por semestre, em `.../shpc/dsas/ca/`; separador `;`, UTF-8 com BOM, CRLF
  lake:
    estado: convertido
    particoes:
    - ano
    - semestre
    chave:
    - CNPJ da Revenda
    - Produto
    - Data da Coleta
    colunas: 16
  unidades_de_medida:
    Valor de Venda: R$ por litro (gasolina, etanol, diesel), R$ por m³ (GNV) ou R$ por botijão de 13 kg (GLP), conforme `Unidade de Medida`
    Valor de Compra: R$ por litro, R$ por m³ ou R$ por botijão de 13 kg, conforme `Unidade de Medida`
  dados_pessoais:
  - coluna: Revenda
    categoria: razão social de pessoa jurídica (revenda)
  - coluna: CNPJ da Revenda
    categoria: CNPJ de pessoa jurídica
  - coluna: Nome da Rua
    categoria: endereço do estabelecimento da revenda
  - coluna: Numero Rua
    categoria: endereço do estabelecimento da revenda
  - coluna: Complemento
    categoria: endereço do estabelecimento da revenda
  - coluna: Bairro
    categoria: endereço do estabelecimento da revenda
  - coluna: Cep
    categoria: endereço do estabelecimento da revenda
  eras:
  - desde: '2004'
    mudanca: 'arquivo do 1º semestre de 2004 (amostra: preços de 10/05/2004 a 30/06/2004), com `Valor de Compra` preenchido em parte das linhas e só os produtos GASOLINA, ETANOL, DIESEL e GNV'
  - desde: '2020'
    mudanca: 'amostra do 1º semestre de 2020: aparece o produto DIESEL S10 e `Valor de Compra` ainda traz preço em parte das linhas, até 30/06/2020; o dicionário da ANP diz que a série de preço de distribuição vai até agosto de 2020'
  - desde: '2025'
    mudanca: 'amostra de 2025: surge o produto GASOLINA ADITIVADA e `Valor de Compra` vem vazio em todas as linhas; no 2º semestre de 2025 o CNPJ passa a vir só com os 14 dígitos, sem pontuação, e a unidade do GNV é grafada `R$ / m3`'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# SHPC — Preços de combustíveis automotivos, série semestral (2004 em diante)

## Resumo

Série histórica dos preços de revenda dos combustíveis automotivos (gasolina C, gasolina aditivada, etanol hidratado, óleo diesel B comum e S-10 e GNV) levantados pela ANP numa pesquisa semanal de preços em postos revendedores, publicada em um arquivo por semestre desde 2004. Cada linha é o preço cobrado ao consumidor numa revenda identificada (CNPJ e endereço), para um produto, em uma data de coleta; em arquivos antigos há também o preço de distribuição pago pela revenda. É a série mais longa e a base da maioria das análises de preço de combustível no Brasil.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/shpc-ca` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semestral (arquivos por semestre, com preços coletados semanalmente); o catálogo do fetcher vai do 1º semestre de 2004 ao 2º de 2025, e a página oficial já lista o 1º semestre de 2026 |
| Cobertura | 2004 a 2025 |
| Unidade (uma linha) | um preço de venda de um produto, coletado em uma revenda em uma data (uma linha por revenda, produto e data de coleta) |
| Granularidade | espacial: revenda (CNPJ e endereço completo), com município, UF e região; temporal: data da coleta (dia) |
| Formato bruto | CSV (36 arquivos) ou ZIP com um CSV (8 arquivos, de 2022 a 2025), um por semestre, em `.../shpc/dsas/ca/`; separador `;`, UTF-8 com BOM, CRLF |
| Estado no lake | convertido |
| Partições | `ano`, `semestre` |
| Chave | `CNPJ da Revenda`, `Produto`, `Data da Coleta` |
| Colunas | 16 |
| Unidades de medida | `Valor de Venda`: R$ por litro (gasolina, etanol, diesel), R$ por m³ (GNV) ou R$ por botijão de 13 kg (GLP), conforme `Unidade de Medida`; `Valor de Compra`: R$ por litro, R$ por m³ ou R$ por botijão de 13 kg, conforme `Unidade de Medida` |
| Dados pessoais | `Revenda` (razão social de pessoa jurídica (revenda)); `CNPJ da Revenda` (CNPJ de pessoa jurídica); `Nome da Rua` (endereço do estabelecimento da revenda); `Numero Rua` (endereço do estabelecimento da revenda); `Complemento` (endereço do estabelecimento da revenda); `Bairro` (endereço do estabelecimento da revenda); `Cep` (endereço do estabelecimento da revenda) |
| Eras | 2004: arquivo do 1º semestre de 2004 (amostra: preços de 10/05/2004 a 30/06/2004), com `Valor de Compra` preenchido em parte das linhas e só os produtos GASOLINA, ETANOL, DIESEL e GNV; 2020: amostra do 1º semestre de 2020: aparece o produto DIESEL S10 e `Valor de Compra` ainda traz preço em parte das linhas, até 30/06/2020; o dicionário da ANP diz que a série de preço de distribuição vai até agosto de 2020; 2025: amostra de 2025: surge o produto GASOLINA ADITIVADA e `Valor de Compra` vem vazio em todas as linhas; no 2º semestre de 2025 o CNPJ passa a vir só com os 14 dígitos, sem pontuação, e a unidade do GNV é grafada `R$ / m3` |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-<AAAA>-<SS>.csv` ou `.zip` (`<SS>` = 01 ou 02), 44 arquivos de 2004-01 a 2025-02; o de 2022-01 se chama `precos-semestrais-ca.zip`. De 2022 em diante os arquivos são ZIP com um único CSV.
- Tamanhos conferidos na amostra (2026-11-15): 2004-S1 48.637.859 bytes (CSV); 2020-S1 86.655.383 bytes (CSV); 2025-S1 8.176.445 bytes (ZIP, com um CSV de 71.902.526 bytes); 2025-S2 17.314.933 bytes (ZIP).
- Cada arquivo traz a pesquisa de preços de revenda (Levantamento de Preços de Combustíveis, LPC) da Superintendência de Defesa da Concorrência (SDC), feita semanalmente por empresa contratada; a pesquisa abrange gasolina C, etanol hidratado, óleo diesel B, GNV e GLP P13 (metadados da ANP, conferidos em 2026-11-15).
- A página oficial foi atualizada em 13/11/2026 e a ANP indica periodicidade "semanal, mensal e semestral" para a série, conforme o tipo de arquivo.
- Os arquivos da ANP (CSV com separador `;`, UTF-8 com BOM e CRLF) têm uma linha de cabeçalho com 16 colunas; os decimais usam vírgula e as datas, `dd/mm/aaaa`. No bruto do fetcher o nome é `<base>_<período>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- A página oficial lista também o 1º semestre de 2026 (`ca-2026-01.zip`), que o catálogo do fetcher ainda não inclui; para 2023 em diante há ainda os arquivos mensais (datasets `shpc-gasolina-etanol` e `shpc-diesel-gnv`) que cobrem os mesmos períodos.

## Conteúdo

- **Uma linha é o preço de um produto numa revenda em uma data de coleta.** A pesquisa semanal gera datas de coleta de segunda a sábado, com mais coletas no início da semana (na amostra de 2025, 319.256 das 804.617 linhas com preço são de segundas-feiras e só 942 de sábados).
- **Produtos.** GASOLINA, ETANOL, DIESEL e GNV desde a amostra de 2004; DIESEL S10 aparece na amostra de 2020 e GASOLINA ADITIVADA na de 2025 (os semestres intermediários não foram amostrados).
- **Dimensão da amostra do lake.** Os 4 arquivos amostrados somam 1.591.925 linhas (de 281.531 a 496.663 por semestre), com 33.618 CNPJs distintos; a série completa tem 44 semestres.
- **Chave.** Na amostra, a combinação `CNPJ da Revenda`, `Produto` e `Data da Coleta` não se repete (1.582.811 linhas com preço e 1.582.811 combinações), exceto pelas 9.114 linhas totalmente vazias do 1º semestre de 2025.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2004 | `shpc-ca-S1` (16) |
| 2020 | `shpc-ca-S1` (16) |
| 2025 | `shpc-ca-S1` (16); `shpc-ca-S2` (16) |

## Variáveis

As descrições vêm do dicionário de campos do documento de metadados da ANP (`metadados-serie-historica-precos-combustiveis-1.pdf`, atualizado em 06/03/2026), comum a todos os arquivos da série; os nomes das colunas do lake são iguais aos do cabeçalho da fonte (com espaços e maiúsculas).
A fonte não traz tabela de códigos; as listas de `Produto`, `Unidade de Medida` e `Regiao - Sigla` abaixo são os valores conferidos na amostra do lake.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Regiao - Sigla` | `Regiao - Sigla` | texto | Sigla da região do país em que fica a revenda pesquisada | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Estado - Sigla` | `Estado - Sigla` | texto | Sigla da unidade da federação (UF) da revenda pesquisada | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Municipio` | `Municipio` | texto | Nome do município da revenda pesquisada, em maiúsculas e em geral sem acentos | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Revenda` | `Revenda` | texto | Nome (razão social) da revenda pesquisada | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `CNPJ da Revenda` | `CNPJ da Revenda` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) da revenda pesquisada, com 14 dígitos; a pontuação varia entre arquivos (veja Cuidados de uso) | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Nome da Rua` | `Nome da Rua` | texto | Nome do logradouro da revenda pesquisada | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Numero Rua` | `Numero Rua` | texto | Número do logradouro da revenda pesquisada, em texto (traz `S/N` e `SN` para sem número) | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Complemento` | `Complemento` | texto | Complemento do logradouro da revenda pesquisada; vazio quando não há | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Bairro` | `Bairro` | texto | Nome do bairro da revenda pesquisada | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Cep` | `Cep` | texto | Código de Endereçamento Postal (CEP) do logradouro da revenda pesquisada, no formato `99999-999` | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Produto` | `Produto` | texto | Nome do combustível pesquisado | GASOLINA = gasolina comum (gasolina C); GASOLINA ADITIVADA = gasolina C aditivada; ETANOL = etanol hidratado; DIESEL = óleo diesel B comum (S-500); DIESEL S10 = óleo diesel B S-10; GNV = gás natural veicular | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Data da Coleta` | `Data da Coleta` | date32[day] | Data em que o preço foi coletado na revenda (a pesquisa é semanal, mas as datas caem em vários dias da semana) | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Valor de Venda` | `Valor de Venda` | decimal | Preço de venda ao consumidor final praticado pela revenda na data da coleta | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Valor de Compra` | `Valor de Compra` | decimal | Preço de distribuição, isto é, o preço de venda da distribuidora ao posto revendedor. Segundo o dicionário da fonte, a série existe até agosto de 2020; nos arquivos mais recentes a coluna vem vazia | — | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Unidade de Medida` | `Unidade de Medida` | texto | Unidade em que os preços da linha estão expressos | R$ / litro = gasolina, etanol e diesel; R$ / m³ = GNV (grafado `R$ / m3` no 2º semestre de 2025) | todo | `shpc-ca-S1`, `shpc-ca-S2` |
| `Bandeira` | `Bandeira` | texto | Nome da bandeira da revenda: o posto bandeirado exibe a marca comercial de uma distribuidora e só pode vender combustíveis dela; o posto de bandeira branca não exibe marca e pode comprar de qualquer distribuidora | BRANCA = revenda sem marca de distribuidora | todo | `shpc-ca-S1`, `shpc-ca-S2` |

## No lake

- Dataset `anp/shpc-ca`, particionado por `ano` e `semestre` (`S1`, `S2`); um Parquet por arquivo da fonte, no padrão `ano=<AAAA>/semestre=<S1|S2>/shpc-ca_<AAAA>-<S1|S2>.parquet`.
- Todas as 16 colunas da fonte são mantidas, com os mesmos nomes (inclusive espaços e maiúsculas); `Data da Coleta` vira data, `Valor de Venda` e `Valor de Compra` viram decimal (ponto decimal) e as demais ficam como texto. Os espaços sobrando antes do CNPJ na fonte (` 49.051.667/0001-02`) são removidos.

## Cuidados de uso

- **Linhas vazias no 1º semestre de 2025.** O CSV da fonte termina com 9.114 linhas só de separadores (`;;;;;;;;;;;;;;;`); o lake as guarda como linhas com todas as colunas nulas (inclusive `Valor de Venda`). Filtre `"Valor de Venda" IS NOT NULL` antes de contar ou agregar.
- **A pontuação do CNPJ muda no 2º semestre de 2025.** Até o 1º semestre de 2025 o CNPJ vem no formato `49.051.667/0001-02`; no 2º semestre de 2025, só com os dígitos (`04431113000100`). Normalize (remova `.`, `/` e `-`) antes de juntar semestres ou de juntar com os arquivos mensais, que seguem o formato com pontuação.
- **Mesma unidade, duas grafias no GNV.** `Unidade de Medida` é `R$ / m³` até o 1º semestre de 2025 e `R$ / m3` no 2º semestre de 2025. Compare produtos por `Produto`, não por texto de unidade; o preço do GLP (`R$ / 13 kg`) não é comparável ao dos demais.
- **`Valor de Compra`.** Só aparece em arquivos antigos, de forma parcial (na amostra, 60.043 das 84.686 linhas de DIESEL de 2004 e 20.060 das 79.121 de 2020 têm o valor) e termina em 2020; em 2025 toda a coluna é vazia. Não use como série contínua.
- **Sobreposição com os arquivos mensais.** De 2023 em diante, os mesmos preços também estão nos datasets mensais `shpc-gasolina-etanol` e `shpc-diesel-gnv`: em novembro de 2025 o semestral tem 16.435 linhas de GASOLINA e o mensal 16.423, números próximos mas não idênticos, e o CNPJ vem com pontuação diferente. Escolha uma série por período para não contar duas vezes.
- **É uma pesquisa por amostra, não um censo de preços.** A ANP contrata uma empresa que coleta semanalmente os preços numa amostra de revendas; a mesma revenda não aparece em todas as semanas e o número de linhas por data varia muito (cai na sexta e no fim de semana, quando há pouca coleta). Não leia a contagem de linhas como número de postos.
- **Datas e semestres.** O arquivo de 2020-S1 tem coletas de 01/01/2020 a 30/06/2020 e o de 2025-S2, de 01/07/2025 a 31/12/2025; a coluna `semestre` é a do arquivo (`S1` ou `S2`), não a calculada da data.
- **Dados pessoais.** As colunas `Revenda`, `CNPJ da Revenda` e as de endereço identificam o estabelecimento (pessoa jurídica) em que o preço foi coletado; em revendas individuais, a razão social pode conter o nome do titular. São dados públicos da ANP, mas evite divulgá-los de forma que exponha uma pessoa física.

## Exemplos

Preço médio de venda da gasolina comum por UF no 2º semestre de 2025 (amostra do lake: `ano=2025`, `semestre=S2`):

```python
import duckdb

duckdb.sql("""
    SELECT "Estado - Sigla" AS uf,
           count(*) AS coletas,
           round(avg("Valor de Venda"), 2) AS preco_medio
    FROM read_parquet('lake/anp/shpc-ca/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2025 AND semestre = 'S2'
      AND "Produto" = 'GASOLINA'
      AND "Valor de Venda" IS NOT NULL
    GROUP BY uf
    ORDER BY preco_medio DESC
    LIMIT 10
""").show()
```

## Referências

- Página oficial da série: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis
- Metadados (dicionário de campos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/metadados-serie-historica-precos-combustiveis-1.pdf
- Lei do Petróleo (Lei nº 9.478/1997), art. 8º, que fundamenta o acompanhamento de preços pela ANP, conforme a página oficial.
