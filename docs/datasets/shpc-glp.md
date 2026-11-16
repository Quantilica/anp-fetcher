---
dataset:
  id: shpc-glp
  fonte: anp
  titulo: SHPC — Preços do GLP P13 (botijão de 13 kg), série semestral (2004 em diante)
  resumo: Preços de revenda do gás de cozinha em botijão de 13 kg coletados semanalmente pela ANP, em arquivos semestrais desde o 1º semestre de 2004.
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
  formato_bruto: CSV (44 arquivos), um por semestre, em `.../shpc/dsas/glp/`; separador `;`, UTF-8 com BOM, CRLF
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
    mudanca: 'arquivo do 1º semestre de 2004 (amostra: preços de 10/05/2004 a 30/06/2004), com `Valor de Compra` preenchido em parte das linhas e `Bandeira` com um único valor distinto'
  - desde: '2020'
    mudanca: 'amostra do 1º semestre de 2020: `Bandeira` passa a ter 16 valores distintos e `Valor de Compra` ainda traz preço em parte das linhas, até 30/06/2020'
  - desde: '2025'
    mudanca: 'amostra de 2025: `Valor de Compra` vem vazio em todas as linhas; no 2º semestre de 2025 o CNPJ passa a vir só com os 14 dígitos, sem pontuação'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# SHPC — Preços do GLP P13 (botijão de 13 kg), série semestral (2004 em diante)

## Resumo

Série histórica dos preços de revenda do gás liquefeito de petróleo envasilhado em botijão de 13 quilos (GLP P13), o gás de cozinha, levantados pela ANP numa pesquisa semanal em revendas, publicada em um arquivo por semestre desde 2004. Cada linha é o preço cobrado ao consumidor numa revenda identificada (CNPJ e endereço) em uma data de coleta, em reais por botijão de 13 kg. Os mesmos preços, de 2023 em diante, também aparecem nos arquivos mensais (`shpc-glp-mensal`).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/shpc-glp` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semestral (arquivos por semestre, com preços coletados semanalmente); o catálogo do fetcher vai do 1º semestre de 2004 ao 2º de 2025, e a página oficial já lista o 1º semestre de 2026 |
| Cobertura | 2004 a 2025 |
| Unidade (uma linha) | um preço de venda de um produto, coletado em uma revenda em uma data (uma linha por revenda, produto e data de coleta) |
| Granularidade | espacial: revenda (CNPJ e endereço completo), com município, UF e região; temporal: data da coleta (dia) |
| Formato bruto | CSV (44 arquivos), um por semestre, em `.../shpc/dsas/glp/`; separador `;`, UTF-8 com BOM, CRLF |
| Estado no lake | convertido |
| Partições | `ano`, `semestre` |
| Chave | `CNPJ da Revenda`, `Produto`, `Data da Coleta` |
| Colunas | 16 |
| Unidades de medida | `Valor de Venda`: R$ por litro (gasolina, etanol, diesel), R$ por m³ (GNV) ou R$ por botijão de 13 kg (GLP), conforme `Unidade de Medida`; `Valor de Compra`: R$ por litro, R$ por m³ ou R$ por botijão de 13 kg, conforme `Unidade de Medida` |
| Dados pessoais | `Revenda` (razão social de pessoa jurídica (revenda)); `CNPJ da Revenda` (CNPJ de pessoa jurídica); `Nome da Rua` (endereço do estabelecimento da revenda); `Numero Rua` (endereço do estabelecimento da revenda); `Complemento` (endereço do estabelecimento da revenda); `Bairro` (endereço do estabelecimento da revenda); `Cep` (endereço do estabelecimento da revenda) |
| Eras | 2004: arquivo do 1º semestre de 2004 (amostra: preços de 10/05/2004 a 30/06/2004), com `Valor de Compra` preenchido em parte das linhas e `Bandeira` com um único valor distinto; 2020: amostra do 1º semestre de 2020: `Bandeira` passa a ter 16 valores distintos e `Valor de Compra` ainda traz preço em parte das linhas, até 30/06/2020; 2025: amostra de 2025: `Valor de Compra` vem vazio em todas as linhas; no 2º semestre de 2025 o CNPJ passa a vir só com os 14 dígitos, sem pontuação |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/glp/glp-<AAAA>-<SS>.csv` (`<SS>` = 01 ou 02), 44 arquivos de 2004-01 a 2025-02; o 1º semestre de 2022 se chama `precos-semestrais-glp-2022-01.csv` e há outra variação de nome (`precos-semestrais-glp<AAAA>-01.csv`).
- Tamanhos conferidos na amostra (2026-11-15): 2004-S1 7.158.338 bytes; 2009-S1 31.632.444; 2014-S2 33.979.109; 2020-S1 18.844.490; 2025-S1 12.008.451; 2025-S2 8.692.179.
- Cada arquivo traz a pesquisa de preços de revenda (Levantamento de Preços de Combustíveis, LPC) da Superintendência de Defesa da Concorrência (SDC), feita semanalmente por empresa contratada; a pesquisa abrange gasolina C, etanol hidratado, óleo diesel B, GNV e GLP P13 (metadados da ANP, conferidos em 2026-11-15).
- A página oficial foi atualizada em 13/11/2026 e a ANP indica periodicidade "semanal, mensal e semestral" para a série, conforme o tipo de arquivo.
- Os arquivos da ANP (CSV com separador `;`, UTF-8 com BOM e CRLF) têm uma linha de cabeçalho com 16 colunas; os decimais usam vírgula e as datas, `dd/mm/aaaa`. No bruto do fetcher o nome é `<base>_<período>@AAAAMMDD.<ext>`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- A página oficial lista também o 1º semestre de 2026 (`glp-2026-01.csv`), que o catálogo do fetcher ainda não inclui; de 2023 em diante os mesmos preços estão nos arquivos mensais (`shpc-glp-mensal`).

## Conteúdo

- **Uma linha é o preço do botijão P13 numa revenda em uma data de coleta.** O único produto é `GLP`, sempre em `R$ / 13 kg`.
- **Dimensão da amostra do lake.** Os 6 arquivos amostrados (2004-S1, 2009-S1, 2014-S2, 2020-S1, 2025-S1 e 2025-S2) somam 698.761 linhas, de 45.925 a 213.453 por semestre, com 33.999 CNPJs distintos; a série completa tem 44 semestres.
- **Chave.** Na amostra, a combinação `CNPJ da Revenda`, `Produto` e `Data da Coleta` não se repete (698.761 linhas e 698.761 combinações).
- **Faixa de preços na amostra.** O preço mediano passa de R$ 30 em 2004 para R$ 35 em 2009, R$ 44 em 2014, R$ 70 em 2020 e R$ 110 em 2025; o máximo de 2025 é R$ 170.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2004 | `shpc-glp-S1` (16) |
| 2009 | `shpc-glp-S1` (16) |
| 2014 | `shpc-glp-S2` (16) |
| 2020 | `shpc-glp-S1` (16) |
| 2025 | `shpc-glp-S1` (16); `shpc-glp-S2` (16) |

## Variáveis

As descrições vêm do dicionário de campos do documento de metadados da ANP (`metadados-serie-historica-precos-combustiveis-1.pdf`, atualizado em 06/03/2026), comum a todos os arquivos da série; os nomes das colunas do lake são iguais aos do cabeçalho da fonte (com espaços e maiúsculas).
A fonte não traz tabela de códigos; as listas de `Produto`, `Unidade de Medida` e `Regiao - Sigla` abaixo são os valores conferidos na amostra do lake.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Regiao - Sigla` | `Regiao - Sigla` | texto | Sigla da região do país em que fica a revenda pesquisada | CO = Centro-Oeste; N = Norte; NE = Nordeste; S = Sul; SE = Sudeste | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Estado - Sigla` | `Estado - Sigla` | texto | Sigla da unidade da federação (UF) da revenda pesquisada | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Municipio` | `Municipio` | texto | Nome do município da revenda pesquisada, em maiúsculas e em geral sem acentos | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Revenda` | `Revenda` | texto | Nome (razão social) da revenda pesquisada | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `CNPJ da Revenda` | `CNPJ da Revenda` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) da revenda pesquisada, com 14 dígitos; a pontuação varia entre arquivos (veja Cuidados de uso) | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Nome da Rua` | `Nome da Rua` | texto | Nome do logradouro da revenda pesquisada | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Numero Rua` | `Numero Rua` | texto | Número do logradouro da revenda pesquisada, em texto (traz `S/N` e `SN` para sem número) | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Complemento` | `Complemento` | texto | Complemento do logradouro da revenda pesquisada; vazio quando não há | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Bairro` | `Bairro` | texto | Nome do bairro da revenda pesquisada | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Cep` | `Cep` | texto | Código de Endereçamento Postal (CEP) do logradouro da revenda pesquisada, no formato `99999-999` | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Produto` | `Produto` | texto | Nome do combustível pesquisado | GLP = gás liquefeito de petróleo em botijão de 13 kg (P13) | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Data da Coleta` | `Data da Coleta` | date32[day] | Data em que o preço foi coletado na revenda (a pesquisa é semanal, mas as datas caem em vários dias da semana) | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Valor de Venda` | `Valor de Venda` | decimal | Preço de venda ao consumidor final praticado pela revenda na data da coleta | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Valor de Compra` | `Valor de Compra` | decimal | Preço de distribuição, isto é, o preço de venda da distribuidora ao posto revendedor. Segundo o dicionário da fonte, a série existe até agosto de 2020; nos arquivos mais recentes a coluna vem vazia | — | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Unidade de Medida` | `Unidade de Medida` | texto | Unidade em que os preços da linha estão expressos | R$ / 13 kg = preço do botijão de 13 kg | todo | `shpc-glp-S1`, `shpc-glp-S2` |
| `Bandeira` | `Bandeira` | texto | Nome da bandeira da revenda: o posto bandeirado exibe a marca comercial de uma distribuidora e só pode vender combustíveis dela; o posto de bandeira branca não exibe marca e pode comprar de qualquer distribuidora | BRANCA = revenda sem marca de distribuidora | todo | `shpc-glp-S1`, `shpc-glp-S2` |

## No lake

- Dataset `anp/shpc-glp`, particionado por `ano` e `semestre` (`S1`, `S2`); um Parquet por arquivo da fonte, no padrão `ano=<AAAA>/semestre=<S1|S2>/shpc-glp_<AAAA>-<S1|S2>.parquet`.
- Todas as 16 colunas da fonte são mantidas, com os mesmos nomes (inclusive espaços e maiúsculas); `Data da Coleta` vira data, `Valor de Venda` e `Valor de Compra` viram decimal (ponto decimal) e as demais ficam como texto. Os espaços sobrando antes do CNPJ na fonte (` 49.051.667/0001-02`) são removidos.

## Cuidados de uso

- **A pontuação do CNPJ muda no 2º semestre de 2025.** Até o 1º semestre de 2025 o CNPJ vem como `61.602.199/0240-54`; no 2º semestre de 2025, só com os dígitos. Normalize (remova `.`, `/` e `-`) antes de juntar semestres ou com os arquivos mensais.
- **`Valor de Compra`.** Só aparece em arquivos antigos, de forma parcial (na amostra, 14.836 das 45.925 linhas de 2004, 84.821 das 199.939 de 2009, 53.198 das 213.453 de 2014 e 29.325 das 114.241 de 2020), e termina em 2020; em 2025 a coluna é vazia.
- **`Bandeira` de uma só marca em 2004.** Na amostra de 2004 a coluna tem um único valor distinto; nas de 2020 e 2025, de 13 a 16 valores. Não compare participação por bandeira entre épocas sem checar a codificação.
- **Sobreposição com `shpc-glp-mensal`.** De 2023 em diante os mesmos preços também estão nos arquivos mensais (em novembro de 2025 a amostra tem 9.872 linhas nos dois). Escolha uma série por período para não contar duas vezes.
- **É uma pesquisa por amostra, não um censo de preços.** A ANP contrata uma empresa que coleta semanalmente os preços numa amostra de revendas; a mesma revenda não aparece em todas as semanas e o número de linhas por data varia muito (cai na sexta e no fim de semana, quando há pouca coleta). Não leia a contagem de linhas como número de postos.
- **O preço é de botijão, não de quilo.** Divida por 13 para obter o preço por quilo.
- **Dados pessoais.** As colunas `Revenda`, `CNPJ da Revenda` e as de endereço identificam o estabelecimento (pessoa jurídica) em que o preço foi coletado; em revendas individuais, a razão social pode conter o nome do titular. São dados públicos da ANP, mas evite divulgá-los de forma que exponha uma pessoa física.

## Exemplos

Preço mediano do botijão de 13 kg por UF no 2º semestre de 2025 (amostra do lake: `ano=2025`, `semestre=S2`):

```python
import duckdb

duckdb.sql("""
    SELECT "Estado - Sigla" AS uf,
           count(*) AS coletas,
           median("Valor de Venda") AS preco_mediano
    FROM read_parquet('lake/anp/shpc-glp/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE ano = 2025 AND semestre = 'S2'
    GROUP BY uf
    ORDER BY preco_mediano DESC
    LIMIT 10
""").show()
```

## Referências

- Página oficial da série: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis
- Metadados (dicionário de campos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/metadados-serie-historica-precos-combustiveis-1.pdf
- Lei do Petróleo (Lei nº 9.478/1997), art. 8º, que fundamenta o acompanhamento de preços pela ANP, conforme a página oficial.
