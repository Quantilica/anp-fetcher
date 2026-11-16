---
dataset:
  id: reservas-nacionais
  fonte: anp
  titulo: Reservas nacionais de petróleo e gás natural — tabela de dados do BAR por campo
  resumo: 'Tabela anual de dados do Boletim Anual de Reservas (BAR) da ANP, de 2020 a 2025: volumes in place, produção acumulada e fração recuperada por campo e área de desenvolvimento, com bacia, estado e situação (maduro ou não).'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/reservas-nacionais-de-petroleo-e-gas-natural
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: anual (BAR; posição em 31 de dezembro, publicada entre março e maio do ano seguinte)
  cobertura:
    inicio: '2020'
    fim: '2025'
  unidade: um campo ou área de desenvolvimento, em um ano de referência do BAR
  granularidade:
    espacial: campo ou área de desenvolvimento, com bacia sedimentar e estado (nome em 2020, sigla desde 2021)
    temporal: ano de referência do BAR, 31 de dezembro (um arquivo por ano, de 2020 a 2025), na partição `ano`
  formato_bruto: seis planilhas XLSX, uma por ano, com uma aba de dados cada
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 11
  unidades_de_medida:
    ANO_REFERENCIA_BAR - Ano: ano civil (AAAA)
    VOIP (bbl): barris (bbl)
    VGIP (m³): m³
    Petróleo Acumulado (bbl): barris (bbl)
    Gás Natural Acumulado (m³): m³
    Fração Recuperada de Petróleo: fração de 0 a 1 (adimensional)
  dados_pessoais: nenhum
  eras:
  - desde: '2020'
    mudanca: 10 colunas, com `Classificação` (`Marginal`) e `Estado` por extenso; aba `Tabela de dados`
  - desde: '2021'
    mudanca: volta a 10 colunas, sem `Classificação`, com a coluna de ano `ANO_REFERENCIA_BAR - Ano` e `Estado` em sigla; aba `Export`
  - desde: '2022'
    mudanca: 10 colunas com `Ano` (que o lake não guarda); sem `Classificação`; abas `BAR_excel_2022_campo` (2022) e `Export` (2023 a 2025)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Reservas nacionais de petróleo e gás natural — tabela de dados do BAR por campo

## Resumo

A ANP controla as reservas brasileiras por meio do Boletim Anual de Recursos e Reservas (BAR), que os contratados enviam até 31 de março de cada ano com as estimativas de cada campo, conforme a Resolução ANP nº 47/2014. Para cada ano, a ANP publica o boletim em PDF e, desde a edição de 2020, uma planilha "Tabela de dados BAR". Este dataset reúne as seis planilhas (posição em 31 de dezembro de 2020 a 2025): uma linha por campo ou área de desenvolvimento, com o volume de óleo e de gás in place (VOIP e VGIP), a produção acumulada de petróleo e de gás, a fração recuperada de petróleo e a situação do campo (maduro ou não maduro). A tabela não traz os volumes de reservas 1P, 2P e 3P, que a ANP apresenta no Painel Dinâmico de Recursos e Reservas de Hidrocarbonetos e no boletim em PDF.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/reservas-nacionais` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/reservas-nacionais-de-petroleo-e-gas-natural |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual (BAR; posição em 31 de dezembro, publicada entre março e maio do ano seguinte) |
| Cobertura | 2020 a 2025 |
| Unidade (uma linha) | um campo ou área de desenvolvimento, em um ano de referência do BAR |
| Granularidade | espacial: campo ou área de desenvolvimento, com bacia sedimentar e estado (nome em 2020, sigla desde 2021); temporal: ano de referência do BAR, 31 de dezembro (um arquivo por ano, de 2020 a 2025), na partição `ano` |
| Formato bruto | seis planilhas XLSX, uma por ano, com uma aba de dados cada |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 11 |
| Unidades de medida | `ANO_REFERENCIA_BAR - Ano`: ano civil (AAAA); `VOIP (bbl)`: barris (bbl); `VGIP (m³)`: m³; `Petróleo Acumulado (bbl)`: barris (bbl); `Gás Natural Acumulado (m³)`: m³; `Fração Recuperada de Petróleo`: fração de 0 a 1 (adimensional) |
| Dados pessoais | nenhum |
| Eras | 2020: 10 colunas, com `Classificação` (`Marginal`) e `Estado` por extenso; aba `Tabela de dados`; 2021: volta a 10 colunas, sem `Classificação`, com a coluna de ano `ANO_REFERENCIA_BAR - Ano` e `Estado` em sigla; aba `Export`; 2022: 10 colunas com `Ano` (que o lake não guarda); sem `Classificação`; abas `BAR_excel_2022_campo` (2022) e `Export` (2023 a 2025) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Seis planilhas XLSX na página de reservas nacionais de petróleo e gás natural da ANP (dados estatísticos), em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/arquivos-reservas-nacionais-de-petroleo-e-gas-natural/`: `tabela-de-dados-bar-2020.xlsx` (44.582 bytes) e `tabela-dados-bar-2021.xlsx` a `tabela-dados-bar-2025.xlsx` (27.623 a 64.446 bytes). Tamanhos conferidos na coleta de 2026-11-15.
- Fonte do dado: Boletim Anual de Recursos e Reservas (BAR) enviado pelos contratados à ANP (Resolução ANP nº 47/2014, que institui o Regulamento Técnico de Estimativa de Recursos e Reservas). A página oficial lista os boletins em PDF de 2001 a 2025 e as planilhas de dados de 2020 a 2025; o fetcher só coleta as planilhas.
- Datas de publicação segundo a página (atualizada em 10/04/2026): 2025, 10/04/2026; 2024, 02/04/2025; 2023, 01/04/2024; 2022, 02/05/2023; 2021, 31/03/2022; 2020, 31/03/2021.
- Não há metadado nem dicionário de dados para as planilhas; as descrições das colunas são deduzidas dos nomes, dos valores e da definição de reserva da página da ANP.
- O servidor não informa a data de modificação dos arquivos; o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15).

## Conteúdo

- **O que é uma linha:** um campo (ou área de desenvolvimento) no BAR de um ano. Linhas por ano: 440 (2020), 430 (2021), 425 (2022), 419 (2023), 426 (2024) e 430 (2025). O nome do campo não é único em todos os anos (`Brejinho` e `Fazenda Belém` em 2020 e 2021; `Camaçari`, `Fazenda Sori`, `Mosquito`, `Saíra` e `Rio Joanes` em 2023 a 2025), e a combinação com bacia e estado também repete em 2023 a 2025.
- **Totais por ano (soma das linhas):** o VOIP vai de 209,3 bilhões de barris (2020) a 217,8 bilhões (2025), e a produção acumulada de petróleo, de 20,8 para 26,9 bilhões de barris; a produção acumulada de gás vai de 701 bilhões para 983 bilhões de m³.
- **Maiores campos em produção acumulada em 2025:** Tupi (3,25 bilhões de barris), Marlim (2,68), Roncador (1,62), Marlim Sul (1,49) e Jubarte (1,27).
- **Situação:** de 279 a 347 campos `Maduro` por ano e 93 a 145 `Não Maduro`; os maduros caem de 347 (2020) para 299 (2021), 290 (2022), 279 (2023), 281 (2024) e 294 (2025).
- **Colunas por ano:** 10 em cada arquivo; `Classificação` só existe em 2020 (29 linhas `Marginal`), `ANO_REFERENCIA_BAR - Ano` só em 2021.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2020 | `reservas-nacionais` (10) |
| 2021 | `reservas-nacionais` (10) |
| 2022 | `reservas-nacionais` (9) |
| 2023 | `reservas-nacionais` (9) |
| 2024 | `reservas-nacionais` (9) |
| 2025 | `reservas-nacionais` (9) |

## Variáveis

Não há dicionário publicado pela ANP para estas planilhas. As descrições são deduzidas do nome das colunas, dos valores observados (2026-11-15) e da página oficial, e as que dependem de interpretação dizem isso. Os tipos são os do XLSX: números (inteiros ou decimais, conforme o ano) e texto.
A coluna *Período* mostra em quais anos cada coluna existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Campo/Área de desenvolvimento` | `Campo/Área de desenvolvimento` | texto | Nome do campo ou da área de desenvolvimento de petróleo e gás natural; em maiúsculas em quase todos os arquivos, mas com nomes em caixa mista em parte das linhas de 2023 a 2025 (`Camaçari`, `Fazenda Sori`). O mesmo nome pode repetir em bacias ou estados diferentes. | — | todo |
| `Bacia` | `Bacia` | texto | Bacia sedimentar do campo (15 a 17 bacias por ano, como Campos, Santos, Potiguar, Recôncavo e Espírito Santo). | — | todo |
| `Estado` | `Estado` | texto | Unidade da Federação do campo: nome por extenso em 2020 (`Bahia`) e sigla de 2021 em diante (`BA`); nos campos no mar é presumivelmente a UF confrontante (`ES` para `ABALONE`, da bacia de Campos), dedução do valor. | — | todo |
| `VOIP (bbl)` | `VOIP (bbl)` | decimal/inteiro | Volume de óleo originalmente in place (VOIP) do campo, em barris (bbl); deduzida do nome e dos valores observados, pois a ANP não publica dicionário para esta tabela. Vazio em 6 a 10 linhas por ano a partir de 2021; 0 em 15 linhas de 2020. | — | todo |
| `VGIP (m³)` | `VGIP (m³)` | decimal/inteiro | Volume de gás originalmente in place (VGIP) do campo, em m³; deduzida do nome e dos valores observados. | — | todo |
| `Petróleo Acumulado (bbl)` | `Petróleo Acumulado (bbl)` | decimal/inteiro | Produção acumulada de petróleo do campo até o fim do ano de referência, em barris (bbl); deduzida do nome e dos valores observados. | — | todo |
| `Gás Natural Acumulado (m³)` | `Gás Natural Acumulado (m³)` | decimal/inteiro | Produção acumulada de gás natural do campo até o fim do ano de referência, em m³; deduzida do nome e dos valores observados. | — | todo |
| `Fração Recuperada de Petróleo` | `Fração Recuperada de Petróleo` | decimal | Fração (de 0 a 1) do óleo in place já produzida: `Petróleo Acumulado (bbl)` dividido por `VOIP (bbl)` (conferido: coincide em todas as linhas com os dois valores, com tolerância de 0,005); vazia quando o VOIP é 0 ou vazio. Há valores acima de 1 (`PARDAL` 2022: 1,66; `CACHOEIRINHA` 2023 e 2024: 10,6). | — | todo |
| `Situação` | `Situação` | texto | Classificação do campo em `Maduro` ou `Não Maduro` (nomenclatura da fonte; o critério não é informado na página da ANP lida); 279 a 347 campos maduros por ano. | — | todo |
| `Classificação` | `Classificação` | texto | `Marginal` em 29 linhas de 2020; vazia nas demais e ausente nos arquivos de 2021 a 2025; descrição deduzida do valor, pois a fonte não a explica. | — | 2020 |
| `ANO_REFERENCIA_BAR - Ano` | `ANO_REFERENCIA_BAR - Ano` | inteiro | Ano de referência do Boletim Anual de Reservas (BAR), igual a 2021 em todas as linhas; só no arquivo de 2021 (nos de 2022 a 2025, a planilha tem a coluna `Ano`, que o lake não guarda: o ano está na partição `ano`). | — | 2021 |

## No lake

- Dataset `anp/reservas-nacionais`, particionado por `ano` (ano de referência do BAR): um Parquet por planilha, `reservas-nacionais_AAAA.parquet`.
- Os números são lidos do XLSX como inteiros ou decimais (o tipo da coluna varia entre os anos: `VOIP (bbl)` é inteiro em 2020 e 2022 e decimal nos demais; `VGIP (m³)` é inteiro só em 2022); os nomes seguem o cabeçalho da fonte (acentos, espaços, `/` e parênteses).
- A coluna `Ano` das planilhas de 2022 a 2025 não está no lake (o valor é o da partição `ano`); a de 2021, `ANO_REFERENCIA_BAR - Ano`, está.

## Cuidados de uso

- **Não são as reservas.** A tabela traz volume in place, produção acumulada e fração recuperada; as reservas 1P/2P/3P, que a ANP publica no boletim e no painel, não estão aqui.
- **`Estado` muda de forma.** `Bahia` em 2020 e `BA` de 2021 em diante; normalize antes de empilhar os anos.
- **Nomes de campo mudam de caixa.** `ABALONE` na maior parte e `Camaçari` nas linhas novas de 2023 a 2025; use `upper()` antes de ligar campos entre anos. Os nomes mudam também por renomeação de campos, não verificada aqui.
- **Valores impossíveis.** `Fração Recuperada de Petróleo` passa de 1 em `PARDAL` (2022, 1,66) e em `CACHOEIRINHA` (2023, 10,59 e 2024, 10,60), onde a produção acumulada supera o volume in place; trate como erro da fonte. O VOIP é 0 em 15 campos de 2020 e vazio em 6 a 10 campos por ano desde 2021.
- **Mudança de tipo.** O tipo dos volumes alterna entre inteiro e decimal conforme o ano (`VOIP (bbl)` é inteiro em 2020 e 2022 e decimal nos demais); ao somar, converta tudo para `DOUBLE`.
- **Colunas que somem.** `Classificação` só em 2020; `ANO_REFERENCIA_BAR - Ano` só em 2021. Empilhe com `union_by_name`.
- **Volumes in place não são aditivos entre anos** nem entre revisões: o BAR revê as estimativas todos os anos, e a produção acumulada de um campo só pode ser comparada com a do mesmo campo no ano anterior.
- **Dados pessoais.** Não há; só nomes de campos, bacias e estados.

## Exemplos

Evolução anual do volume in place e da produção acumulada de petróleo (soma de todos os campos de cada BAR):

```python
import duckdb

duckdb.sql("""
    SELECT ano,
           count(*) AS campos,
           round(sum("VOIP (bbl)") / 1e9, 1) AS voip_bilhoes_bbl,
           round(sum("Petróleo Acumulado (bbl)") / 1e9, 1) AS acumulado_bilhoes_bbl
    FROM read_parquet('lake/anp/reservas-nacionais/**/*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ano
    ORDER BY ano
""").show()
```

## Referências

- Reservas nacionais de petróleo e gás natural (ANP, dados estatísticos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/reservas-nacionais-de-petroleo-e-gas-natural
- Resolução ANP nº 47/2014 (Regulamento Técnico de Estimativa de Recursos e Reservas de Petróleo e Gás Natural), citada na página da ANP.
- Painel Dinâmico de Recursos e Reservas de Hidrocarbonetos (ANP), indicado na página.
