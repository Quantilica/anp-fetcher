---
dataset:
  id: armazenagem-terminais
  fonte: anp
  titulo: Capacidade de armazenagem de terminais (petróleo, combustíveis líquidos e GLP)
  resumo: Capacidade nominal de armazenamento dos terminais de petróleo, derivados, biocombustíveis e GLP autorizados pela ANP, por tipo, operador, município e UF, em um arquivo atualizado semestralmente.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semestral, segundo os metadados da ANP (versão de 12/06/2026); a página oficial indica o arquivo atualizado em 20/10/2026
  cobertura:
    inicio: 2026-10
    fim: em-curso
  unidade: um terminal autorizado a operação, com a capacidade nominal de seus tanques por grupo de produto
  granularidade:
    espacial: terminal (município e UF; sem endereço nem coordenadas)
    temporal: retrato da data da atualização (sem coluna de data)
  formato_bruto: CSV com separador `,` e UTF-8, com cabeçalho; a ANP publica também uma versão `.xlsx` do mesmo conteúdo
  lake:
    estado: convertido
    particoes: []
    chave:
    - Tipo
    - Municipio
    - UF
    - Operador
    colunas: 8
  unidades_de_medida:
    Numero_de_tanques: tanques (unidades)
    Capacidade_nominal_petroleo: m³
    Capacidade_nominal_derivados_biocombustiveis: m³
    Capacidade_nominal_GLP: m³
  dados_pessoais:
  - coluna: Operador
    categoria: nome de pessoa jurídica (empresa operadora do terminal)
  eras:
  - desde: '2026'
    mudanca: formato único observado no arquivo de 15/11/2026, com 8 colunas e 141 terminais (não foi possível conferir versões antigas do arquivo); a página indica a versão dos metadados de 12/06/2026
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Capacidade de armazenagem de terminais (petróleo, combustíveis líquidos e GLP)

## Resumo

Relação dos terminais autorizados a operar pela ANP (exceto terminais de GNL), com o número de tanques e a capacidade nominal de armazenagem de petróleo, de derivados e biocombustíveis e de GLP. Terminais são instalações de movimentação e armazenamento de petróleo, derivados e biocombustíveis; a operação e a construção dependem de autorização da ANP (Resolução ANP nº 52/2015). Cada linha é um terminal, com tipo (fluvial, lacustre, marítimo ou terrestre), operador, município e UF.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/armazenagem-terminais` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semestral, segundo os metadados da ANP (versão de 12/06/2026); a página oficial indica o arquivo atualizado em 20/10/2026 |
| Cobertura | 2026-10 a em-curso |
| Unidade (uma linha) | um terminal autorizado a operação, com a capacidade nominal de seus tanques por grupo de produto |
| Granularidade | espacial: terminal (município e UF; sem endereço nem coordenadas); temporal: retrato da data da atualização (sem coluna de data) |
| Formato bruto | CSV com separador `,` e UTF-8, com cabeçalho; a ANP publica também uma versão `.xlsx` do mesmo conteúdo |
| Estado no lake | convertido |
| Partições | — |
| Chave | `Tipo`, `Municipio`, `UF`, `Operador` |
| Colunas | 8 |
| Unidades de medida | `Numero_de_tanques`: tanques (unidades); `Capacidade_nominal_petroleo`: m³; `Capacidade_nominal_derivados_biocombustiveis`: m³; `Capacidade_nominal_GLP`: m³ |
| Dados pessoais | `Operador` (nome de pessoa jurídica (empresa operadora do terminal)) |
| Eras | 2026: formato único observado no arquivo de 15/11/2026, com 8 colunas e 141 terminais (não foi possível conferir versões antigas do arquivo); a página indica a versão dos metadados de 12/06/2026 |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/cat/capacidade-armazenagem-terminais.csv`, o único arquivo do catálogo; a página oficial indica "atualizado em 20/10/2026" para o CSV e para o XLSX.
- O arquivo lido em 2026-11-15 tem 9.689 bytes e 141 linhas de dados. No bruto, o nome é `armazterm@AAAAMMDD.csv`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Metadados em PDF (versão 12/06/2026): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/cat/metadados-capacidade-armazenagem-terminais-novo.pdf. Fonte: Superintendência de Infraestrutura e Movimentação (SIM/ANP); escopo nacional; frequência de atualização semestral; codificação UTF-8.

## Conteúdo

- **Um terminal por linha.** Na amostra, as 141 linhas têm 141 valores distintos de `Operador`, 77 municípios e 23 UFs; por tipo: 65 terrestres, 62 marítimos, 10 fluviais e 4 lacustres.
- **Capacidades por grupo de produto.** 125 dos 141 terminais têm capacidade de petróleo igual a zero, 119 têm capacidade de GLP igual a zero e 13 têm capacidade de derivados e biocombustíveis igual a zero; 5 terminais têm todas as capacidades e o número de tanques iguais a zero.
- **Escopo.** A página oficial descreve a relação dos terminais autorizados a operação pela ANP, exceto os terminais de GNL.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `armazterm` (8) |

## Variáveis

As descrições vêm do documento de metadados da ANP (versão de 12/06/2026). Os nomes das colunas do lake são os do cabeçalho do arquivo, com sublinhado (`Numero_de_tanques`, `Capacidade_nominal_*`).
Todas as colunas ficam como texto, inclusive as numéricas, que a fonte escreve com ponto decimal e uma casa (`16.0`, `23377.0`).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Tipo` | `Tipo` | texto | Tipo de terminal (a fonte admite quatro tipos) | FLUVIAL = fluvial; LACUSTRE = lacustre; MARÍTIMO = marítimo; TERRESTRE = terrestre | — |
| `Municipio` | `Municipio` | texto | Nome do município onde o terminal está localizado | — | — |
| `UF` | `UF` | texto | Sigla da unidade da federação onde o terminal está localizado | — | — |
| `Operador` | `Operador` | texto | Identificação da empresa que opera o terminal (nome da empresa seguido do local, como `TRANSPETRO ITABUNA`) | — | — |
| `Numero_de_tanques` | `Numero_de_tanques` | texto | Número de tanques autorizados a operação, inclusive tanques de resíduos; texto com uma casa decimal (`16.0`) | — | — |
| `Capacidade_nominal_petroleo` | `Capacidade_nominal_petroleo` | texto | Capacidade de armazenagem nominal dos tanques de petróleo autorizados a operação, em metros cúbicos (m³), inclusive tanques de resíduos; texto com uma casa decimal | — | — |
| `Capacidade_nominal_derivados_biocombustiveis` | `Capacidade_nominal_derivados_biocombustiveis` | texto | Capacidade de armazenagem nominal dos tanques de derivados de petróleo (exceto GLP) e biocombustíveis autorizados a operação, em metros cúbicos (m³); texto com uma casa decimal | — | — |
| `Capacidade_nominal_GLP` | `Capacidade_nominal_GLP` | texto | Capacidade de armazenagem nominal dos tanques de gás liquefeito de petróleo (GLP) autorizados a operação, em metros cúbicos (m³); texto com uma casa decimal | — | — |

## No lake

- Dataset `anp/armazenagem-terminais`, sem partições: um Parquet, `armazterm.parquet`, com as 8 colunas do CSV, todas como texto.
- Um novo download substitui o retrato anterior no bruto; o lake não guarda histórico de capacidades.

## Cuidados de uso

- **Colunas numéricas guardadas como texto.** Converta com `try_cast(... AS DOUBLE)` antes de somar; os valores têm formato `16.0`. Capacidades estão em m³ e `Numero_de_tanques` em unidades.
- **A capacidade de petróleo inclui tanques de resíduos** e o número de tanques também (metadados da ANP); a capacidade de derivados exclui o GLP, que tem coluna própria.
- **Zero não é sempre "sem tancagem".** Em 5 terminais o número de tanques e as três capacidades são zero (por exemplo `NAVEMAZÔNIA MANAUS`); a fonte não diz se isso indica terminal sem tancagem autorizada ou dado ainda não informado. Trate como ausência de informação ao calcular médias por terminal.
- **Retrato sem data na linha.** O arquivo não tem coluna de data; a data do retrato é a da atualização na página (20/10/2026) ou a do sufixo do arquivo bruto.
- **Sobreposição parcial com `tancagem`.** A tancagem por instalação (dataset `tancagem`) cobre terminais e outros segmentos com tanque a tanque; as capacidades aqui são os totais por terminal, com definições próprias (nominal, e não operacional).
- **Dados pessoais.** Só há nomes de empresas operadoras (pessoas jurídicas).

## Exemplos

Capacidade nominal total de derivados e biocombustíveis por UF e tipo de terminal (m³):

```python
import duckdb

duckdb.sql("""
    SELECT UF, Tipo, count(*) AS terminais,
           sum(try_cast(Capacidade_nominal_derivados_biocombustiveis AS DOUBLE)) AS capacidade_m3
    FROM read_parquet('lake/anp/armazenagem-terminais/*.parquet')
    GROUP BY ALL
    ORDER BY capacidade_m3 DESC
    LIMIT 10
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/cat/metadados-capacidade-armazenagem-terminais-novo.pdf
- Resolução ANP nº 52/2015, que trata da autorização de operação e construção de terminais, citada na página oficial.
