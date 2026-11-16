---
dataset:
  id: pocos-exploratorios
  fonte: anp
  titulo: Poços exploratórios em blocos
  resumo: Retrato mensal dos poços exploratórios perfurados em blocos sob contrato desde 1998, com bloco, bacia, operador, datas, profundidade e notificação de descoberta.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; o fetcher lê um CSV por mês, de 2023-03 a 2026-07 (41 arquivos), cada um com todos os poços exploratórios desde 1998
  cobertura:
    inicio: 2023-03
    fim: 2026-07
  unidade: um poço exploratório em blocos sob contrato, na posição do mês do arquivo (a partição `ano`/`mes` é o mês do retrato)
  granularidade:
    espacial: poço exploratório, com bloco, bacia (e grupo de bacias a partir de 2024), estado (sigla) e ambiente
    temporal: mês do retrato (partições `ano` e `mes`); datas de perfuração, conclusão e descoberta no poço
  formato_bruto: CSV em UTF-8 com BOM, separado por vírgula
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 16
  unidades_de_medida:
    PROFUNDIDADE FINAL (m): m
  dados_pessoais:
  - coluna: OPERADOR
    categoria: nome fantasia de empresa operadora (pessoa jurídica)
  eras:
  - desde: 2023-03
    mudanca: '10 colunas: sem `BACIAS AGRUPADAS`, sem profundidade final e sem a marca de pré-sal; `DATA DA NOTIFICAÇÃO DE DESCOBERTA`'
  - desde: 2024-01
    mudanca: '12 colunas: entram `BACIAS AGRUPADAS` e `PROFUNDIDADE FINAL (m)`'
  - desde: 2024-11
    mudanca: '13 colunas: `DATA DA 1ª NOTIFICAÇÃO DE DESCOBERTA` e `FLUIDO NOTIFICAÇÃO DESCOBERTA`; o arquivo da amostra tem só 129 linhas'
  - desde: 2025-09
    mudanca: '14 colunas: entra `ATINGIU PRÉ-SAL?` e a coluna de data passa a se chamar `DATA 1ª DESCOBERTA`'
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Poços exploratórios em blocos

## Resumo

Dados gerais dos poços exploratórios que tiveram a perfuração iniciada a partir de 1998, a cada mês, com o bloco sob contrato, a bacia, o estado, o ambiente, o operador, as datas de início e conclusão, a profundidade final, a indicação de que atingiu o pré-sal e a notificação de descoberta de hidrocarbonetos (data e fluido). Cada arquivo mensal é um retrato completo do painel dinâmico da fase de exploração (todos os poços desde 1998), não só os do mês: as linhas se repetem de um mês para o seguinte.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pocos-exploratorios` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; o fetcher lê um CSV por mês, de 2023-03 a 2026-07 (41 arquivos), cada um com todos os poços exploratórios desde 1998 |
| Cobertura | 2023-03 a 2026-07 |
| Unidade (uma linha) | um poço exploratório em blocos sob contrato, na posição do mês do arquivo (a partição `ano`/`mes` é o mês do retrato) |
| Granularidade | espacial: poço exploratório, com bloco, bacia (e grupo de bacias a partir de 2024), estado (sigla) e ambiente; temporal: mês do retrato (partições `ano` e `mes`); datas de perfuração, conclusão e descoberta no poço |
| Formato bruto | CSV em UTF-8 com BOM, separado por vírgula |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | — |
| Colunas | 16 |
| Unidades de medida | `PROFUNDIDADE FINAL (m)`: m |
| Dados pessoais | `OPERADOR` (nome fantasia de empresa operadora (pessoa jurídica)) |
| Eras | 2023-03: 10 colunas: sem `BACIAS AGRUPADAS`, sem profundidade final e sem a marca de pré-sal; `DATA DA NOTIFICAÇÃO DE DESCOBERTA`; 2024-01: 12 colunas: entram `BACIAS AGRUPADAS` e `PROFUNDIDADE FINAL (m)`; 2024-11: 13 colunas: `DATA DA 1ª NOTIFICAÇÃO DE DESCOBERTA` e `FLUIDO NOTIFICAÇÃO DESCOBERTA`; o arquivo da amostra tem só 129 linhas; 2025-09: 14 colunas: entra `ATINGIU PRÉ-SAL?` e a coluna de data passa a se chamar `DATA 1ª DESCOBERTA` |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- 41 CSV mensais de 2023-03 a 2026-07 em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/<ano>/` (nomes por mês, como `marco.csv` em 2023 e `pocos-exploratorios-jul.csv` em 2026). Os arquivos da amostra têm de 13 KB (2024-11) a 198 KB (2026-07).
- Fonte do dado, segundo o metadado "Poços Exploratórios em Blocos" (DOCX, de dados abertos da Fase de Exploração): ANP/SEP (Superintendência de Exploração), a partir do SIGEP; atualização mensal; contato sigep_sep@anp.gov.br. A página oficial lista os arquivos de 2023-02 a 2026-10; o fetcher tem até 2026-07.
- No bruto: `fase-exploracao-pocos-exploratorios/pocos-exploratorios_<AAAA>-<MM>@AAAAMMDD.csv`, com o sufixo da data da coleta.

## Conteúdo

- **Retrato cumulativo.** Cada mês traz todos os poços exploratórios iniciados desde 25/01/1998: 1.570 (2023-03), 1.732 (2023-04), 1.605 (2024-01), 1.792 (2025-09) e 1.798 (2026-07), com o mais recente iniciado em 23/09/2025 e 14/07/2026 nos dois últimos. A contagem não cresce monotonicamente (2023-04 tem mais que 2024-01).
- **Notificação de descoberta.** Em 2026-07, 882 dos 1.798 poços têm data de primeira descoberta e 1.058 têm fluido notificado (as duas colunas não coincidem em número de linhas preenchidas).
- **Estados e bacias.** O estado vem em sigla (19 valores em 2026-07), e as bacias são 25 em 2026-07 (como `Campos`, `Santos` e `Potiguar`), agrupadas em quatro grupos.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2023 | `pocos-exploratorios-03` (10); `pocos-exploratorios-04` (10) |
| 2024 | `pocos-exploratorios-01` (12); `pocos-exploratorios-11` (13) |
| 2025 | `pocos-exploratorios-09` (14) |
| 2026 | `pocos-exploratorios-07` (14) |

## Variáveis

As descrições vêm do metadado "Poços Exploratórios em Blocos" (DOCX da ANP), que descreve a era mais nova (14 colunas, sem os três nomes de coluna antigos); as colunas anteriores têm a descrição da homônima. A coluna *Período* mostra em que meses cada coluna existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `POÇO ANP` | `POÇO ANP` | texto | Identificador padronizado do poço, conforme as regras da ANP (Resolução ANP nº 699/2017); vazio em uma linha de cada arquivo da amostra, exceto o de 2026-07. | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `BLOCO` | `BLOCO` | texto | Nome do bloco exploratório em que o poço foi perfurado. | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `BACIA` | `BACIA` | texto | Nome da bacia sedimentar. | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `ESTADO` | `ESTADO` | texto | Unidade da Federação, em sigla (`RJ`, `ES`, `RN`...). | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `AMBIENTE` | `AMBIENTE` | texto | Localização por ambiente dos blocos exploratórios sob contrato: `MAR` ou `TERRA`. | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `OPERADOR` | `OPERADOR` | texto | Empresa que opera o contrato de E&P (nome fantasia; vazio em 2 linhas de 2026-07). | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `INÍCIO DA PERFURAÇÃO` | `INÍCIO DA PERFURAÇÃO` | texto | Data em que a perfuração do poço exploratório teve início (DD/MM/AAAA, texto). | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `CONCLUSÃO DO POÇO` | `CONCLUSÃO DO POÇO` | texto | Data em que foi concluída a perfuração do poço exploratório (DD/MM/AAAA, texto); o metadado chama a coluna `CONCLUSÃO DA PERFURAÇÃO`. | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `NOTIFICAÇÃO DE DESCOBERTA ?` | `NOTIFICAÇÃO DE DESCOBERTA ?` | texto | Indica se houve indícios de hidrocarbonetos notificados à ANP durante a perfuração do poço exploratório (`Sim` ou `Não`). | — | todo | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` e mais 3 |
| `DATA DA NOTIFICAÇÃO DE DESCOBERTA` | `DATA DA NOTIFICAÇÃO DE DESCOBERTA` | texto | Data da notificação da descoberta à ANP (DD/MM/AAAA); coluna dos arquivos de 2023 a 2024-01 (nome antigo de `DATA 1ª DESCOBERTA`). | — | 2023-03 a 2024-01 | `pocos-exploratorios-01`, `pocos-exploratorios-03`, `pocos-exploratorios-04` |
| `BACIAS AGRUPADAS` | `BACIAS AGRUPADAS` | texto | Agrupamento das bacias: `Margem Equatorial` e `Margem Leste` (mar), `Maduras` e `Nova Fronteira` (terra); não existe nos arquivos anteriores a 2024. | — | 2024-01 a 2026-07 | `pocos-exploratorios-01`, `pocos-exploratorios-07`, `pocos-exploratorios-09` e mais 1 |
| `PROFUNDIDADE FINAL (m)` | `PROFUNDIDADE FINAL (m)` | texto | Profundidade final alcançada pelo poço, em metros (texto; não existe nos arquivos de 2023). | — | 2024-01 a 2026-07 | `pocos-exploratorios-01`, `pocos-exploratorios-07`, `pocos-exploratorios-09` e mais 1 |
| `DATA DA 1ª NOTIFICAÇÃO DE DESCOBERTA` | `DATA DA 1ª NOTIFICAÇÃO DE DESCOBERTA` | texto | Data em que foi notificada à ANP a primeira descoberta de hidrocarbonetos pelo poço exploratório; nome intermediário da coluna `DATA 1ª DESCOBERTA` (arquivo de 2024-11). | — | 2024-11 | `pocos-exploratorios-11` |
| `FLUIDO NOTIFICAÇÃO DESCOBERTA` | `FLUIDO NOTIFICAÇÃO DESCOBERTA` | texto | Hidrocarboneto cuja descoberta foi notificada à ANP: `Petróleo`, `Gás`, `Gás e Petróleo` ou outro (4 valores na amostra); vazio nos poços sem notificação. | — | 2024-11 a 2026-07 | `pocos-exploratorios-07`, `pocos-exploratorios-09`, `pocos-exploratorios-11` |
| `ATINGIU PRÉ-SAL?` | `ATINGIU PRÉ-SAL?` | texto | Indica se o poço atingiu o pré-sal (`Sim` ou `Não`); só nos arquivos recentes. | — | 2025-09 a 2026-07 | `pocos-exploratorios-07`, `pocos-exploratorios-09` |
| `DATA 1ª DESCOBERTA` | `DATA 1ª DESCOBERTA` | texto | Data em que foi notificada à ANP a primeira descoberta de hidrocarbonetos pelo poço exploratório (DD/MM/AAAA); vazia nos poços sem notificação. | — | 2025-09 a 2026-07 | `pocos-exploratorios-07`, `pocos-exploratorios-09` |

## No lake

- Dataset `anp/pocos-exploratorios`, particionado por `ano` e `mes`: um Parquet por CSV, `ano=<AAAA>/mes=<MM>/pocos-exploratorios_<AAAA>-<MM>.parquet`.
- Todas as colunas são texto, com os nomes da fonte (maiúsculas, acentos, `?`).

## Cuidados de uso

- **Todos os poços em cada arquivo.** Não some os arquivos mensais: cada um repete os poços do anterior. Para uma série de poços perfurados por ano, use um único arquivo (o mais recente) e agrupe por ano de `INÍCIO DA PERFURAÇÃO`.
- **Arquivo incompleto em 2024-11.** O da amostra tem só 129 linhas (13 KB), com início de perfuração de 27/01/1998 a 15/11/2017, enquanto os outros meses têm 1.570 a 1.798; não é um retrato completo, e a causa não é explicada pela fonte. Não use 2024-11 para contagens.
- **Colunas mudam com o tempo.** Os arquivos de 2023 têm 10 colunas; o de 2026-07, 14. A coluna da data de descoberta tem três nomes (`DATA DA NOTIFICAÇÃO DE DESCOBERTA`, `DATA DA 1ª NOTIFICAÇÃO DE DESCOBERTA`, `DATA 1ª DESCOBERTA`); ao empilhar, una por nome e normalize os três. Use `union_by_name` e `coalesce`.
- **Linha sem nome de poço.** Cada um dos arquivos de 2023-03 a 2025-09 da amostra tem uma linha com `POÇO ANP` vazio (1.569 nomes distintos em 1.570 linhas, em 2023-03); o de 2026-07 não tem. Fora essa linha, `POÇO ANP` é único dentro do arquivo; a chave do dataset fica vazia.
- **Poços que tiveram descoberta, mas não fluido.** Em 2026-07, 882 poços têm data de descoberta e 1.058 têm fluido preenchido; a diferença não é explicada pela fonte.
- **Estado em sigla, ambiente em maiúsculas.** Em outros datasets da ANP, o estado vem por extenso; use uma tabela de siglas.
- **Dados pessoais.** Não há: poços, blocos e empresas operadoras.

## Exemplos

Poços exploratórios por ano de início da perfuração, com a proporção de poços com notificação de descoberta, no retrato de 2026-07 (as datas vêm em texto, como DD/MM/AAAA):

```python
import duckdb

duckdb.sql("""
    SELECT year(strptime("INÍCIO DA PERFURAÇÃO", '%d/%m/%Y')) AS ano_perfuracao,
           count(*) AS pocos,
           count(*) FILTER (WHERE "NOTIFICAÇÃO DE DESCOBERTA ?" = 'Sim') AS com_descoberta
    FROM read_parquet('lake/anp/pocos-exploratorios/ano=2026/mes=07/*.parquet')
    GROUP BY 1
    ORDER BY 1 DESC
    LIMIT 10
""").show()
```

## Referências

- Fase de exploração (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao
- Metadado "Poços Exploratórios em Blocos": https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/gcep/arquivos-fase-de-exploracao/painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/metadado-pocos-exploratorios.pdf (o arquivo é um DOCX apesar da extensão)
