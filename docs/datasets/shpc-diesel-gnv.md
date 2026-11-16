---
dataset:
  id: shpc-diesel-gnv
  fonte: anp
  titulo: SHPC — Preços de óleo diesel (S-500 e S-10) e GNV, arquivos mensais (2023 em diante)
  resumo: Preços de revenda de diesel e GNV coletados semanalmente pela ANP, em arquivos mensais desde janeiro de 2023.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal (um arquivo por mês, com preços coletados semanalmente); o catálogo vai de janeiro de 2023 a outubro de 2026
  cobertura:
    inicio: 2023-01
    fim: 2026-10
  unidade: um preço de venda de um produto, coletado em uma revenda em uma data (uma linha por revenda, produto e data de coleta)
  granularidade:
    espacial: revenda (CNPJ e endereço completo), com município, UF e região
    temporal: data da coleta (dia)
  formato_bruto: CSV (46 arquivos), um por mês, em `.../shpc/dsan/<AAAA>/`; separador `;`, UTF-8 com BOM, CRLF
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
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
  - desde: '2023'
    mudanca: primeiro mês do catálogo (janeiro de 2023); desde então a ANP publica a série também em arquivos mensais, que repetem períodos já cobertos pelos arquivos semestrais
  - desde: '2026'
    mudanca: os nomes dos arquivos mudam para `<MM>-dados-abertos-precos-diesel-gnv.csv` (o catálogo guarda URLs alternativas para o mesmo mês); as colunas da amostra (janeiro de 2023 e outubro de 2026) são as mesmas 16
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# SHPC — Preços de óleo diesel (S-500 e S-10) e GNV, arquivos mensais (2023 em diante)

## Resumo

Preços de revenda do óleo diesel B comum (S-500), do diesel S-10 e do gás natural veicular (GNV) levantados pela ANP numa pesquisa semanal em revendas, publicados em um arquivo por mês desde janeiro de 2023. Cada linha é o preço cobrado ao consumidor numa revenda identificada (CNPJ e endereço), para um produto, em uma data de coleta. Os mesmos preços também estão nos arquivos semestrais de combustíveis automotivos (`shpc-ca`); este recorte mensal é o que a ANP atualiza mais perto do tempo real.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/shpc-diesel-gnv` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal (um arquivo por mês, com preços coletados semanalmente); o catálogo vai de janeiro de 2023 a outubro de 2026 |
| Cobertura | 2023-01 a 2026-10 |
| Unidade (uma linha) | um preço de venda de um produto, coletado em uma revenda em uma data (uma linha por revenda, produto e data de coleta) |
| Granularidade | espacial: revenda (CNPJ e endereço completo), com município, UF e região; temporal: data da coleta (dia) |
| Formato bruto | CSV (46 arquivos), um por mês, em `.../shpc/dsan/<AAAA>/`; separador `;`, UTF-8 com BOM, CRLF |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `CNPJ da Revenda`, `Produto`, `Data da Coleta` |
| Colunas | 16 |
| Unidades de medida | `Valor de Venda`: R$ por litro (gasolina, etanol, diesel), R$ por m³ (GNV) ou R$ por botijão de 13 kg (GLP), conforme `Unidade de Medida`; `Valor de Compra`: R$ por litro, R$ por m³ ou R$ por botijão de 13 kg, conforme `Unidade de Medida` |
| Dados pessoais | `Revenda` (razão social de pessoa jurídica (revenda)); `CNPJ da Revenda` (CNPJ de pessoa jurídica); `Nome da Rua` (endereço do estabelecimento da revenda); `Numero Rua` (endereço do estabelecimento da revenda); `Complemento` (endereço do estabelecimento da revenda); `Bairro` (endereço do estabelecimento da revenda); `Cep` (endereço do estabelecimento da revenda) |
| Eras | 2023: primeiro mês do catálogo (janeiro de 2023); desde então a ANP publica a série também em arquivos mensais, que repetem períodos já cobertos pelos arquivos semestrais; 2026: os nomes dos arquivos mudam para `<MM>-dados-abertos-precos-diesel-gnv.csv` (o catálogo guarda URLs alternativas para o mesmo mês); as colunas da amostra (janeiro de 2023 e outubro de 2026) são as mesmas 16 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan/<AAAA>/precos-diesel-gnv-<MM>.csv` (2023 a 2025) e `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan/2026/<MM>-dados-abertos-precos-diesel-gnv.csv` (2026), 46 meses de 2023-01 a 2026-10; para 2026 o catálogo guarda também URLs alternativas, com outro nome de arquivo, que o fetcher tenta se a principal falhar.
- Tamanhos conferidos na amostra (2026-11-15): 2023-01 3.780.657 bytes; 2023-02 3.427.392; 2023-12 4.022.603; 2024-12 3.752.292; 2025-11 3.251.568; 2026-10 3.818.119.
- Cada arquivo traz a pesquisa de preços de revenda (Levantamento de Preços de Combustíveis, LPC) da Superintendência de Defesa da Concorrência (SDC), feita semanalmente por empresa contratada; a pesquisa abrange gasolina C, etanol hidratado, óleo diesel B, GNV e GLP P13 (metadados da ANP, conferidos em 2026-11-15).
- A página oficial foi atualizada em 13/11/2026 e a ANP indica periodicidade "semanal, mensal e semestral" para a série, conforme o tipo de arquivo.
- Os arquivos da ANP (CSV com separador `;`, UTF-8 com BOM e CRLF) têm uma linha de cabeçalho com 16 colunas; os decimais usam vírgula e as datas, `dd/mm/aaaa`. No bruto do fetcher o nome é `<base>_<período>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.

## Conteúdo

- **Uma linha é o preço de um produto (DIESEL, DIESEL S10 ou GNV) numa revenda em uma data de coleta.**
- **Dimensão da amostra do lake.** Os 6 arquivos amostrados (2023-01, 2023-02, 2023-12, 2024-12, 2025-11 e 2026-10) somam 130.950 linhas, de 19.158 a 23.734 por mês, com 9.830 CNPJs distintos.
- **Chave.** Na amostra, a combinação `CNPJ da Revenda`, `Produto` e `Data da Coleta` não se repete (129.473 linhas com preço e 129.473 combinações), exceto pelas 1.477 linhas totalmente vazias de janeiro de 2023.
- **Faixa de preços na amostra.** Entre 2023 e 2026, o `Valor de Venda` do DIESEL vai de R$ 4,69 a R$ 8,90, o do DIESEL S10 de R$ 4,73 a R$ 9,99 e o do GNV de R$ 3,19 a R$ 7,15; `Valor de Compra` é vazio em todas as linhas.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `shpc-diesel-gnv-01` (16); `shpc-diesel-gnv-02` (16); `shpc-diesel-gnv-12` (16) |
| 2024 | `shpc-diesel-gnv-12` (16) |
| 2025 | `shpc-diesel-gnv-11` (16) |
| 2026 | `shpc-diesel-gnv-10` (16) |

## Variáveis

As descrições vêm do dicionário de campos do documento de metadados da ANP (`metadados-serie-historica-precos-combustiveis-1.pdf`, atualizado em 06/03/2026), comum a todos os arquivos da série; os nomes das colunas do lake são iguais aos do cabeçalho da fonte (com espaços e maiúsculas).
A fonte não traz tabela de códigos; as listas de `Produto`, `Unidade de Medida` e `Regiao - Sigla` abaixo são os valores conferidos na amostra do lake.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Regiao - Sigla` | `Regiao - Sigla` | texto | Sigla da região do país em que fica a revenda pesquisada | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Estado - Sigla` | `Estado - Sigla` | texto | Sigla da unidade da federação (UF) da revenda pesquisada | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Municipio` | `Municipio` | texto | Nome do município da revenda pesquisada, em maiúsculas e em geral sem acentos | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Revenda` | `Revenda` | texto | Nome (razão social) da revenda pesquisada | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `CNPJ da Revenda` | `CNPJ da Revenda` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) da revenda pesquisada, com 14 dígitos; a pontuação varia entre arquivos (veja Cuidados de uso) | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Nome da Rua` | `Nome da Rua` | texto | Nome do logradouro da revenda pesquisada | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Numero Rua` | `Numero Rua` | texto | Número do logradouro da revenda pesquisada, em texto (traz `S/N` e `SN` para sem número) | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Complemento` | `Complemento` | texto | Complemento do logradouro da revenda pesquisada; vazio quando não há | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Bairro` | `Bairro` | texto | Nome do bairro da revenda pesquisada | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Cep` | `Cep` | texto | Código de Endereçamento Postal (CEP) do logradouro da revenda pesquisada, no formato `99999-999` | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Produto` | `Produto` | texto | Nome do combustível pesquisado | DIESEL = óleo diesel B comum (S-500); DIESEL S10 = óleo diesel B S-10; GNV = gás natural veicular | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Data da Coleta` | `Data da Coleta` | date32[day] | Data em que o preço foi coletado na revenda (a pesquisa é semanal, mas as datas caem em vários dias da semana) | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Valor de Venda` | `Valor de Venda` | decimal | Preço de venda ao consumidor final praticado pela revenda na data da coleta | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Valor de Compra` | `Valor de Compra` | decimal | Preço de distribuição, isto é, o preço de venda da distribuidora ao posto revendedor. Segundo o dicionário da fonte, a série existe até agosto de 2020; nos arquivos mais recentes a coluna vem vazia | — | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Unidade de Medida` | `Unidade de Medida` | texto | Unidade em que os preços da linha estão expressos | R$ / litro = diesel; R$ / m³ = GNV | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |
| `Bandeira` | `Bandeira` | texto | Nome da bandeira da revenda: o posto bandeirado exibe a marca comercial de uma distribuidora e só pode vender combustíveis dela; o posto de bandeira branca não exibe marca e pode comprar de qualquer distribuidora | BRANCA = revenda sem marca de distribuidora | todo | `shpc-diesel-gnv-01`, `shpc-diesel-gnv-02`, `shpc-diesel-gnv-10` e mais 2 |

## No lake

- Dataset `anp/shpc-diesel-gnv`, particionado por `ano` e `mes` (`01` a `12`); um Parquet por arquivo da fonte, no padrão `ano=<AAAA>/mes=<MM>/shpc-diesel-gnv_<AAAA>-<MM>.parquet`.
- Todas as 16 colunas da fonte são mantidas, com os mesmos nomes (inclusive espaços e maiúsculas); `Data da Coleta` vira data, `Valor de Venda` e `Valor de Compra` viram decimal (ponto decimal) e as demais ficam como texto. Os espaços sobrando antes do CNPJ na fonte (` 49.051.667/0001-02`) são removidos.

## Cuidados de uso

- **Linhas vazias em janeiro de 2023.** O CSV da fonte termina com 1.477 linhas só de separadores; o lake as guarda como linhas com todas as colunas nulas. Filtre `"Valor de Venda" IS NOT NULL` antes de contar ou agregar.
- **`Valor de Compra` vazio.** Nenhuma linha dos arquivos mensais traz o preço de distribuição.
- **Sobreposição com `shpc-ca`.** De 2023 a 2025 os mesmos preços também estão nos arquivos semestrais (em novembro de 2025, 6.757 linhas de DIESEL aqui e 6.758 no semestral); o CNPJ vem com pontuação aqui e, no 2º semestre de 2025, sem pontuação no semestral. Escolha uma série por período.
- **GNV em `R$ / m³`.** O preço do GNV é por metro cúbico; o do diesel, por litro. Compare só dentro do mesmo `Produto`.
- **É uma pesquisa por amostra, não um censo de preços.** A ANP contrata uma empresa que coleta semanalmente os preços numa amostra de revendas; a mesma revenda não aparece em todas as semanas e o número de linhas por data varia muito (cai na sexta e no fim de semana, quando há pouca coleta). Não leia a contagem de linhas como número de postos.
- **Dados pessoais.** As colunas `Revenda`, `CNPJ da Revenda` e as de endereço identificam o estabelecimento (pessoa jurídica) em que o preço foi coletado; em revendas individuais, a razão social pode conter o nome do titular. São dados públicos da ANP, mas evite divulgá-los de forma que exponha uma pessoa física.

## Exemplos

Preço médio do diesel S-10 por UF em outubro de 2026 (amostra do lake: `ano=2026`, `mes=10`):

```python
import duckdb

duckdb.sql("""
    SELECT "Estado - Sigla" AS uf,
           count(*) AS coletas,
           round(avg("Valor de Venda"), 2) AS preco_medio
    FROM read_parquet('lake/anp/shpc-diesel-gnv/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2026 AND mes = '10'
      AND "Produto" = 'DIESEL S10'
    GROUP BY uf
    ORDER BY preco_medio DESC
    LIMIT 10
""").show()
```

## Referências

- Página oficial da série: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis
- Metadados (dicionário de campos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/metadados-serie-historica-precos-combustiveis-1.pdf
- Lei do Petróleo (Lei nº 9.478/1997), art. 8º, que fundamenta o acompanhamento de preços pela ANP, conforme a página oficial.
