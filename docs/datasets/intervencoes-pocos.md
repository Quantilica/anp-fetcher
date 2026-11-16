---
dataset:
  id: intervencoes-pocos
  fonte: anp
  titulo: Intervenções em poços
  resumo: Intervenções (perfuração, completação, restauração, avaliação e abandono) em poços no Brasil, de 2013 a setembro de 2026, com sonda, objetivo, datas e duração.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo o metadado da ANP; o fetcher lê 7 arquivos de janelas bienais (2013-2014 a 2025-2026), e o último é reescrito a cada atualização
  cobertura:
    inicio: 2013-01
    fim: 2026-09
  unidade: uma intervenção em um poço, com sonda, objetivo e período
  granularidade:
    espacial: poço (nome ANP e nome do operador), com campo, bacia e ambiente
    temporal: data de início e de término da intervenção; cada arquivo cobre os inícios de uma janela de dois anos
  formato_bruto: CSV em UTF-8 com BOM, separado por vírgula, de 12 colunas
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 12
  unidades_de_medida:
    Dias_em_intervenção: dias
  dados_pessoais:
  - coluna: Operador_atual
    categoria: nome de empresa operadora ou nome de sonda (pessoa jurídica ou equipamento)
  - coluna: Operador_epoca
    categoria: nome de empresa operadora ou nome de sonda (pessoa jurídica ou equipamento)
  - coluna: Sonda
    categoria: nome de empresa operadora ou nome de sonda (pessoa jurídica ou equipamento)
  eras:
  - desde: '2013'
    mudanca: sete arquivos bienais com as mesmas 12 colunas (2013-2014 a 2025-2026); o último vai até o início de 30/09/2026 na amostra
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Intervenções em poços

## Resumo

Relação das intervenções sofridas pelos poços, desde as perfurações até as restaurações e os abandonos, com o poço, o campo, a bacia, o operador atual e o da época, a sonda empregada, o objetivo, as datas de início e término e os dias em intervenção. Os arquivos são organizados em janelas de dois anos de início da intervenção (2013-2014, 2015-2016, ... 2025-2026).

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/intervencoes-pocos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo o metadado da ANP; o fetcher lê 7 arquivos de janelas bienais (2013-2014 a 2025-2026), e o último é reescrito a cada atualização |
| Cobertura | 2013-01 a 2026-09 |
| Unidade (uma linha) | uma intervenção em um poço, com sonda, objetivo e período |
| Granularidade | espacial: poço (nome ANP e nome do operador), com campo, bacia e ambiente; temporal: data de início e de término da intervenção; cada arquivo cobre os inícios de uma janela de dois anos |
| Formato bruto | CSV em UTF-8 com BOM, separado por vírgula, de 12 colunas |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 12 |
| Unidades de medida | `Dias_em_intervenção`: dias |
| Dados pessoais | `Operador_atual` (nome de empresa operadora ou nome de sonda (pessoa jurídica ou equipamento)); `Operador_epoca` (nome de empresa operadora ou nome de sonda (pessoa jurídica ou equipamento)); `Sonda` (nome de empresa operadora ou nome de sonda (pessoa jurídica ou equipamento)) |
| Eras | 2013: sete arquivos bienais com as mesmas 12 colunas (2013-2014 a 2025-2026); o último vai até o início de 30/09/2026 na amostra |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Sete CSV em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-pocos/`: `intervencao_em_pocos_2013-2014.csv`, `2015-2016`, `2017-2018`, `2019-2020`, `2021-2022`, `2023-2024` e `2025-2026`. Tamanhos na amostra: de 0,85 MB (2019-2020) a 1,45 MB (2013-2014). Os de 2017-2018 e 2021-2022 estão no catálogo, mas não na amostra.
- Fonte do dado, segundo o metadado "Intervenção em Poços" (DOCX, criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; atualização mensal; contato demandas_sdp@anp.gov.br.
- No bruto: `intervencoes-pocos/intervencoes-pocos-<janela>@AAAAMMDD.csv`, com o sufixo da data da coleta.

## Conteúdo

- **Uma linha por intervenção.** Linhas na amostra: 10.654 (2013-2014), 10.675 (2015-2016), 6.157 (2019-2020), 9.752 (2023-2024) e 8.383 (2025-2026). Em cada arquivo, os inícios vão do primeiro dia do primeiro ano da janela até o último dia do segundo (o arquivo de 2025-2026 vai até 30/09/2026); os términos podem ser posteriores (até 20/10/2026).
- **Objetivos.** Na amostra: `Restauração` (33.143), `Completação` (6.989), `Perfuração` (3.102), `Abandono` (1.413), `Avaliação` (612) e `TLD` (46); 316 linhas não têm objetivo.
- **Duração.** `Dias_em_intervenção` vai de 1 a 479 dias na amostra, e nenhuma linha tem término anterior ao início.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `intervencoes-pocos` (12); `intervencoes-pocos` (12); `intervencoes-pocos` (12); `intervencoes-pocos` (12); `intervencoes-pocos` (12) |

## Variáveis

As descrições vêm do metadado "Intervenção em Poços" (DOCX da ANP, criado em junho de 2026), que descreve as 12 colunas; a sigla `TLD` do objetivo não é explicada pelo metadado (provavelmente teste de longa duração).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Nome_poço_anp` | `Nome_poço_anp` | texto | Nome do poço atribuído conforme a Resolução ANP nº 699/2017 (nulo em uma linha do arquivo de 2025-2026). | — | — |
| `Nome_poço_operador` | `Nome_poço_operador` | texto | Nome do poço atribuído pelo operador. | — | — |
| `Campo` | `Campo` | texto | Nome do campo do qual o poço faz parte. | — | — |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar onde o poço foi perfurado (maiúsculas). | — | — |
| `Operador_atual` | `Operador_atual` | texto | Empresa operadora do poço atualmente. | — | — |
| `Operador_epoca` | `Operador_epoca` | texto | Empresa operadora do poço na época da intervenção; vazia em parte das linhas (1.107 das 8.383 do arquivo de 2025-2026). | — | — |
| `Ambiente` | `Ambiente` | texto | Ambiente geográfico onde o poço se localiza: `TERRA` ou `MAR`. | — | — |
| `Sonda` | `Sonda` | texto | Nome da sonda operando no poço durante a intervenção; `POÇO SEM SONDA` e `SONDA DE PRODUÇÃO TERRESTRE ...` aparecem como valores. | — | — |
| `Objetivo` | `Objetivo` | texto | Objetivo da intervenção: `Restauração`, `Completação`, `Perfuração`, `Abandono`, `Avaliação` ou `TLD` (seis valores, mais 316 linhas sem objetivo na amostra). | — | — |
| `Data_início` | `Data_início` | texto | Data de início da intervenção (DD/MM/AAAA, texto). | — | — |
| `Data_término` | `Data_término` | texto | Data de término da intervenção (DD/MM/AAAA, texto). | — | — |
| `Dias_em_intervenção` | `Dias_em_intervenção` | texto | Quantidade de dias em intervenção, inteiro (de 1 a 479 na amostra). | — | — |

## No lake

- Dataset `anp/intervencoes-pocos`, sem partição: um Parquet por janela bienal, `intervencoes-pocos-<anoi>-<anof>.parquet`.
- Todas as colunas são texto, inclusive as datas (DD/MM/AAAA) e os dias.

## Cuidados de uso

- **Janela pelo início, não pelo término.** Cada arquivo traz as intervenções que começaram na janela; uma intervenção que começou em dezembro de 2014 e terminou em 2015 está em 2013-2014, com o término no ano seguinte (o maior término do arquivo de 2013-2014 é 14/06/2015).
- **Arquivos recentes são reescritos.** O de 2025-2026 muda a cada atualização mensal; os mais antigos são estáveis.
- **Sem chave.** `(Nome_poço_anp, Data_início, Sonda, Objetivo)` repete em 2 linhas do arquivo de 2013-2014 (10.652 combinações em 10.654 linhas), e há uma linha sem nome de poço em 2025-2026.
- **Operador da época em branco.** `Operador_epoca` está vazio em 51 linhas de 2013-2014 e em 1.107 de 2025-2026; use `Operador_atual` como alternativa, sabendo que pode ser outro operador.
- **Objetivo ausente e sondas fictícias.** 316 linhas sem objetivo, e `Sonda` traz `POÇO SEM SONDA` (intervenção sem sonda) e `SONDA DE PRODUÇÃO TERRESTRE ...`, que não são equipamentos únicos; não conte sondas distintas sem filtrar esses valores.
- **Dados pessoais.** Não há: poços, campos, sondas e operadoras.

## Exemplos

Número de intervenções, dias médios em intervenção e total por objetivo e ambiente, em 2025 e 2026:

```python
import duckdb

duckdb.sql("""
    SELECT Objetivo, Ambiente, count(*) AS intervencoes,
           round(avg(Dias_em_intervenção::INTEGER), 1) AS dias_medios
    FROM read_parquet('lake/anp/intervencoes-pocos/intervencoes-pocos-2025-2026.parquet')
    GROUP BY ALL
    ORDER BY intervencoes DESC
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos), informações sobre poços: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadado "Intervenção em Poços" (DOCX): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-pocos/metadado-intervencao-em-pocos.docx
