---
dataset:
  id: shpc-4s
  fonte: anp
  titulo: SHPC — Preços das últimas quatro semanas (diesel, gasolina, etanol, GNV e GLP)
  resumo: Preços de revenda das quatro últimas semanas de pesquisa da ANP para todos os combustíveis automotivos e o GLP, em três arquivos que a ANP reescreve a cada atualização.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semanal (a ANP reescreve os três arquivos, que cobrem sempre as últimas quatro semanas; atualizado em 13/11/2026 segundo a página oficial); a cobertura registrada (2026-10) é a da amostra convertida, e a data inicial anda a cada atualização
  cobertura:
    inicio: 2026-10
    fim: em-curso
  unidade: um preço de venda de um produto, coletado em uma revenda em uma data (uma linha por revenda, produto e data de coleta)
  granularidade:
    espacial: revenda (CNPJ e endereço completo), com município, UF e região
    temporal: data da coleta (dia)
  formato_bruto: 3 CSV (`ultimas-4-semanas-diesel-gnv.csv`, `ultimas-4-semanas-gasolina-etanol.csv` e `ultimas-4-semanas-glp.csv`, em `.../shpc/qus/`); separador `;`, UTF-8 com BOM, CRLF
  lake:
    estado: convertido
    particoes: []
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
  - desde: '2026'
    mudanca: 'janela de coleta da amostra do lake: de 19/10/2026 a 13/11/2026, as quatro semanas anteriores à atualização de 13/11/2026'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# SHPC — Preços das últimas quatro semanas (diesel, gasolina, etanol, GNV e GLP)

## Resumo

Os preços de revenda coletados pela ANP nas quatro semanas mais recentes de pesquisa, em três arquivos (diesel e GNV, gasolina e etanol, GLP P13) que a ANP substitui a cada atualização. Cada linha é o preço cobrado ao consumidor numa revenda identificada (CNPJ e endereço), para um produto, em uma data de coleta. É o recorte mais recente da Série Histórica de Preços de Combustíveis e de GLP; as semanas que saem da janela passam a existir só nos arquivos mensais e semestrais.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/shpc-4s` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semanal (a ANP reescreve os três arquivos, que cobrem sempre as últimas quatro semanas; atualizado em 13/11/2026 segundo a página oficial); a cobertura registrada (2026-10) é a da amostra convertida, e a data inicial anda a cada atualização |
| Cobertura | 2026-10 a em-curso |
| Unidade (uma linha) | um preço de venda de um produto, coletado em uma revenda em uma data (uma linha por revenda, produto e data de coleta) |
| Granularidade | espacial: revenda (CNPJ e endereço completo), com município, UF e região; temporal: data da coleta (dia) |
| Formato bruto | 3 CSV (`ultimas-4-semanas-diesel-gnv.csv`, `ultimas-4-semanas-gasolina-etanol.csv` e `ultimas-4-semanas-glp.csv`, em `.../shpc/qus/`); separador `;`, UTF-8 com BOM, CRLF |
| Estado no lake | convertido |
| Partições | — |
| Chave | `CNPJ da Revenda`, `Produto`, `Data da Coleta` |
| Colunas | 16 |
| Unidades de medida | `Valor de Venda`: R$ por litro (gasolina, etanol, diesel), R$ por m³ (GNV) ou R$ por botijão de 13 kg (GLP), conforme `Unidade de Medida`; `Valor de Compra`: R$ por litro, R$ por m³ ou R$ por botijão de 13 kg, conforme `Unidade de Medida` |
| Dados pessoais | `Revenda` (razão social de pessoa jurídica (revenda)); `CNPJ da Revenda` (CNPJ de pessoa jurídica); `Nome da Rua` (endereço do estabelecimento da revenda); `Numero Rua` (endereço do estabelecimento da revenda); `Complemento` (endereço do estabelecimento da revenda); `Bairro` (endereço do estabelecimento da revenda); `Cep` (endereço do estabelecimento da revenda) |
| Eras | 2026: janela de coleta da amostra do lake: de 19/10/2026 a 13/11/2026, as quatro semanas anteriores à atualização de 13/11/2026 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa os três arquivos de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/`: `ultimas-4-semanas-diesel-gnv.csv`, `ultimas-4-semanas-gasolina-etanol.csv` e `ultimas-4-semanas-glp.csv`. Na amostra de 2026-11-15 têm 21.757, 47.804 e 13.330 linhas de dados (contagem de linhas do CSV menos o cabeçalho).
- Cada download gera um novo arquivo bruto com a data de modificação (ou do download) no nome: `shpc-4s-<tema>@AAAAMMDD.csv`; a janela de quatro semanas se desloca a cada atualização.
- Cada arquivo traz a pesquisa de preços de revenda (Levantamento de Preços de Combustíveis, LPC) da Superintendência de Defesa da Concorrência (SDC), feita semanalmente por empresa contratada; a pesquisa abrange gasolina C, etanol hidratado, óleo diesel B, GNV e GLP P13 (metadados da ANP, conferidos em 2026-11-15).
- A página oficial foi atualizada em 13/11/2026 e a ANP indica periodicidade "semanal, mensal e semestral" para a série, conforme o tipo de arquivo.
- Os arquivos da ANP (CSV com separador `;`, UTF-8 com BOM e CRLF) têm uma linha de cabeçalho com 16 colunas; os decimais usam vírgula e as datas, `dd/mm/aaaa`. No bruto do fetcher o nome é `<base>_<período>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.

## Conteúdo

- **Uma linha é o preço de um produto numa revenda em uma data de coleta**, como nas demais séries SHPC, mas só para as últimas quatro semanas.
- **Três arquivos, três recortes de produto:** `shpc-4s-diesel-gnv` (DIESEL, DIESEL S10 e GNV), `shpc-4s-gasolina-etanol` (GASOLINA, GASOLINA ADITIVADA e ETANOL) e `shpc-4s-glp` (GLP).
- **Dimensão da amostra do lake.** Os três arquivos somam 82.891 linhas, de 9.279 CNPJs distintos, com datas de coleta de 19/10/2026 a 13/11/2026.
- **Chave.** Na amostra, a combinação `CNPJ da Revenda`, `Produto` e `Data da Coleta` não se repete (82.891 linhas e 82.891 combinações).
- **Sem linhas vazias.** Ao contrário de alguns arquivos mensais e semestrais, os três arquivos da amostra não têm linhas só de separadores.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `shpc-4s-diesel-gnv` (16); `shpc-4s-gasolina-etanol` (16); `shpc-4s-glp` (16) |

## Variáveis

As descrições vêm do dicionário de campos do documento de metadados da ANP (`metadados-serie-historica-precos-combustiveis-1.pdf`, atualizado em 06/03/2026), comum a todos os arquivos da série; os nomes das colunas do lake são iguais aos do cabeçalho da fonte (com espaços e maiúsculas).
A fonte não traz tabela de códigos; as listas de `Produto`, `Unidade de Medida` e `Regiao - Sigla` abaixo são os valores conferidos na amostra do lake.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Regiao - Sigla` | `Regiao - Sigla` | texto | Sigla da região do país em que fica a revenda pesquisada | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Estado - Sigla` | `Estado - Sigla` | texto | Sigla da unidade da federação (UF) da revenda pesquisada | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Municipio` | `Municipio` | texto | Nome do município da revenda pesquisada, em maiúsculas e em geral sem acentos | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Revenda` | `Revenda` | texto | Nome (razão social) da revenda pesquisada | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `CNPJ da Revenda` | `CNPJ da Revenda` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) da revenda pesquisada, com 14 dígitos; a pontuação varia entre arquivos (veja Cuidados de uso) | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Nome da Rua` | `Nome da Rua` | texto | Nome do logradouro da revenda pesquisada | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Numero Rua` | `Numero Rua` | texto | Número do logradouro da revenda pesquisada, em texto (traz `S/N` e `SN` para sem número) | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Complemento` | `Complemento` | texto | Complemento do logradouro da revenda pesquisada; vazio quando não há | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Bairro` | `Bairro` | texto | Nome do bairro da revenda pesquisada | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Cep` | `Cep` | texto | Código de Endereçamento Postal (CEP) do logradouro da revenda pesquisada, no formato `99999-999` | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Produto` | `Produto` | texto | Nome do combustível pesquisado | GASOLINA = gasolina comum (gasolina C); GASOLINA ADITIVADA = gasolina C aditivada; ETANOL = etanol hidratado; DIESEL = óleo diesel B comum (S-500); DIESEL S10 = óleo diesel B S-10; GNV = gás natural veicular; … (lista completa no dicionário da fonte) | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Data da Coleta` | `Data da Coleta` | date32[day] | Data em que o preço foi coletado na revenda (a pesquisa é semanal, mas as datas caem em vários dias da semana) | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Valor de Venda` | `Valor de Venda` | decimal | Preço de venda ao consumidor final praticado pela revenda na data da coleta | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Valor de Compra` | `Valor de Compra` | decimal | Preço de distribuição, isto é, o preço de venda da distribuidora ao posto revendedor. Segundo o dicionário da fonte, a série existe até agosto de 2020; nos arquivos mais recentes a coluna vem vazia | — | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Unidade de Medida` | `Unidade de Medida` | texto | Unidade em que os preços da linha estão expressos | R$ / litro = gasolina, etanol e diesel; R$ / m³ = GNV; R$ / 13 kg = GLP | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |
| `Bandeira` | `Bandeira` | texto | Nome da bandeira da revenda: o posto bandeirado exibe a marca comercial de uma distribuidora e só pode vender combustíveis dela; o posto de bandeira branca não exibe marca e pode comprar de qualquer distribuidora | BRANCA = revenda sem marca de distribuidora | — | `shpc-4s-diesel-gnv`, `shpc-4s-gasolina-etanol`, `shpc-4s-glp` |

## No lake

- Dataset `anp/shpc-4s`, sem partições (o recorte de quatro semanas não tem ano nem mês): três Parquet, `shpc-4s-diesel-gnv.parquet`, `shpc-4s-gasolina-etanol.parquet` e `shpc-4s-glp.parquet`.
- Todas as 16 colunas da fonte são mantidas, com os mesmos nomes (inclusive espaços e maiúsculas); `Data da Coleta` vira data, `Valor de Venda` e `Valor de Compra` viram decimal (ponto decimal) e as demais ficam como texto. Os espaços sobrando antes do CNPJ na fonte (` 49.051.667/0001-02`) são removidos.

## Cuidados de uso

- **A janela se desloca.** Reconverter o lake depois de uma nova atualização troca as datas; não use este dataset como histórico. Para períodos fechados use `shpc-ca`/`shpc-glp` (semestrais) ou os mensais.
- **`Valor de Compra` vazio** em todas as linhas.
- **Unidades diferentes por produto.** O preço do GLP é por botijão de 13 kg (`R$ / 13 kg`), o do GNV por m³ e os demais por litro; não some nem compare preços de produtos com unidades diferentes.
- **É uma pesquisa por amostra, não um censo de preços.** A ANP contrata uma empresa que coleta semanalmente os preços numa amostra de revendas; a mesma revenda não aparece em todas as semanas e o número de linhas por data varia muito (cai na sexta e no fim de semana, quando há pouca coleta). Não leia a contagem de linhas como número de postos.
- **Dados pessoais.** As colunas `Revenda`, `CNPJ da Revenda` e as de endereço identificam o estabelecimento (pessoa jurídica) em que o preço foi coletado; em revendas individuais, a razão social pode conter o nome do titular. São dados públicos da ANP, mas evite divulgá-los de forma que exponha uma pessoa física.

## Exemplos

Número de revendas pesquisadas e preço médio por produto na janela das últimas quatro semanas:

```python
import duckdb

duckdb.sql("""
    SELECT "Produto",
           "Unidade de Medida" AS unidade,
           count(DISTINCT "CNPJ da Revenda") AS revendas,
           round(avg("Valor de Venda"), 2) AS preco_medio
    FROM read_parquet('lake/anp/shpc-4s/*.parquet')
    GROUP BY ALL
    ORDER BY "Produto"
""").show()
```

## Referências

- Página oficial da série: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis
- Metadados (dicionário de campos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/metadados-serie-historica-precos-combustiveis-1.pdf
- Lei do Petróleo (Lei nº 9.478/1997), art. 8º, que fundamenta o acompanhamento de preços pela ANP, conforme a página oficial.
