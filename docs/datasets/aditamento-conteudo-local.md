---
dataset:
  id: aditamento-conteudo-local
  fonte: anp
  titulo: Aditamento de conteúdo local — solicitações da Resolução ANP 726/2018
  resumo: 'Planilha com o resultado da análise da ANP dos pedidos de aditamento da cláusula de conteúdo local de contratos de exploração e produção (Resolução ANP 726/2018): 518 solicitações, por contrato, bloco ou campo, operador, rodada e situação.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/aditamento-conteudo-local
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'dados estáticos (metadado da ANP: prazo para pedir o aditamento encerrado; "atualizado até mar/21"); a página oficial foi atualizada em 06/03/2026'
  cobertura:
    inicio: 2018-04
    fim: 2021-03
  unidade: uma solicitação de aditamento sobre um bloco exploratório ou campo de um contrato
  granularidade:
    espacial: bloco exploratório ou campo (nome), com bacia sedimentar e ambiente (terra ou mar); sem coordenadas
    temporal: data de protocolo da solicitação (abril a agosto de 2018) e data de publicação do extrato no Diário Oficial da União, dentro do texto de `Status` (até 2021)
  formato_bruto: um CSV em ISO-8859-1, separador ponto e vírgula
  lake:
    estado: convertido
    particoes: []
    chave:
    - Ordem
    colunas: 11
  dados_pessoais:
  - coluna: Operador do Contrato
    categoria: razão social de empresa operadora (pessoa jurídica)
  eras:
  - desde: '2018'
    mudanca: arquivo único e estático, sem mudança de layout; os metadados mais recentes são de 06/03/2026 e o fetcher guarda só a versão corrente
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Aditamento de conteúdo local — solicitações da Resolução ANP 726/2018

## Resumo

A Resolução ANP nº 726/2018 permitiu que as empresas que atuam em exploração e produção de petróleo e gás natural aditassem a cláusula de conteúdo local dos contratos vigentes, com efeitos para as fases não encerradas, conforme autorizado pela Resolução CNPE nº 1/2018. A ANP publica a planilha com o resultado da análise dos pedidos: cada linha é uma solicitação sobre um bloco exploratório ou campo de um contrato, com o operador, a bacia, o ambiente, a rodada de origem, a situação (assinado e publicado no Diário Oficial da União, indeferido e outros) e o alcance do aditamento. Segundo a ANP, os compromissos de conteúdo local foram atualizados em 266 contratos, que alcançam 258 blocos exploratórios (e eventuais campos decorrentes) e 85 campos de produção. Os dados são estáticos: o prazo para pedir o aditamento se encerrou em agosto de 2018.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/aditamento-conteudo-local` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/aditamento-conteudo-local |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | dados estáticos (metadado da ANP: prazo para pedir o aditamento encerrado; "atualizado até mar/21"); a página oficial foi atualizada em 06/03/2026 |
| Cobertura | 2018-04 a 2021-03 |
| Unidade (uma linha) | uma solicitação de aditamento sobre um bloco exploratório ou campo de um contrato |
| Granularidade | espacial: bloco exploratório ou campo (nome), com bacia sedimentar e ambiente (terra ou mar); sem coordenadas; temporal: data de protocolo da solicitação (abril a agosto de 2018) e data de publicação do extrato no Diário Oficial da União, dentro do texto de `Status` (até 2021) |
| Formato bruto | um CSV em ISO-8859-1, separador ponto e vírgula |
| Estado no lake | convertido |
| Partições | — |
| Chave | `Ordem` |
| Colunas | 11 |
| Unidades de medida | — |
| Dados pessoais | `Operador do Contrato` (razão social de empresa operadora (pessoa jurídica)) |
| Eras | 2018: arquivo único e estático, sem mudança de layout; os metadados mais recentes são de 06/03/2026 e o fetcher guarda só a versão corrente |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Um arquivo CSV na página de dados abertos de aditamento de conteúdo local da ANP: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-aditamento-conteudo-local/planilha-aditamento-conteudo-local.csv` (164.731 bytes, conferido na coleta de 2026-11-15). A ANP também publica o PDF de metadados, `metadados-aditamento.pdf`, na mesma pasta.
- Fonte do dado, segundo os metadados: ANP/SCL (Superintendência de Conteúdo Local), com informações consolidadas do SEI (Sistema Eletrônico de Informações); contato scl@anp.gov.br. Criado em 12/04/2018, última atualização 08/03/2021 e "atualizado até mar/21" no PDF de metadados; a página oficial e o link de metadados informam atualização em 06/03/2026.
- A página oficial indica o fim do prazo de pedido em 10 de agosto de 2018; o PDF de metadados diz 12/08/2018. O painel dinâmico de aditamento de conteúdo local da ANP é o recurso associado ao conjunto.
- O servidor não informa a data de modificação do arquivo; o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15).

## Conteúdo

- **O que é uma linha:** uma solicitação de aditamento sobre um bloco ou campo de um contrato. A planilha tem 518 linhas e 518 valores distintos de `Ordem`; os 287 contratos distintos aparecem em mais de uma linha quando o contrato tem vários blocos ou campos.
- **Situação das solicitações:** 333 assinadas e publicadas no Diário Oficial da União (as datas de publicação vão de 26/07/2018 a 27/01/2021, dentro de `Status`), 161 indeferidas, 17 de contratos aditados fora do escopo da Resolução 726/2018, 5 anexadas a um campo e 2 outras (rodada não alcançada pela resolução; contrato original sem obrigação de conteúdo local).
- **Ambiente e operadores:** 354 linhas em terra e 164 em mar; 46 operadores, dos quais a Petrobras responde por 232 linhas, a Petra Energia por 38, a Imetame por 25 e a Eneva por 24.
- **Rodadas:** 19 códigos; as maiores são `BID07` (96 linhas), `BID11` (94), `BID06` (69), `BID09` (59) e `BID12` (50).
- O arquivo é único, sem partição por ano; todas as colunas vêm do CSV como texto.

## Variáveis

As descrições das 11 colunas vêm do metadado da ANP (`metadados-aditamento.pdf`); os números de linhas e valores vêm da amostra do lake (2026-11-15), que cobre o arquivo inteiro. O metadado dá `Ordem` como número, mas o lake a guarda como texto.
Os valores de `Status` e `Link Extrato DOU` são textos livres: as datas e os links ficam dentro do texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Ordem` | `Ordem` | texto | Ordem de recebimento, pela ANP, da solicitação de aditamento contratual (1 a 518, sem repetição na amostra). | — | — |
| `Solicitação` | `Solicitação` | texto | Identificação do documento que contém a solicitação de aditamento: número de carta, de ofício ou de processo do operador (por exemplo `GIA-E&P/GCP 0046/2018`); um mesmo documento cobre várias linhas (78 valores distintos em 518 linhas). | — | — |
| `Data do Protocolo` | `Data do Protocolo` | texto | Data de protocolização da solicitação na ANP (DD/MM/AAAA, texto), de 16/04/2018 a 14/08/2018; em 4 linhas o valor vem como número de série do Excel (`43313`, `43321`). | — | — |
| `Contrato` | `Contrato` | texto | Número do contrato de exploração e produção de petróleo e gás natural, no formato do número de processo (como `48610.001413/2008-15`); 287 contratos distintos. | — | — |
| `Operador do Contrato` | `Operador do Contrato` | texto | Operador do contrato no momento da solicitação de aditamento, pela razão social (como `Petróleo Brasileiro S.A.`); 46 empresas distintas. | — | — |
| `Nome do Bloco / Campo` | `Nome do Bloco / Campo` | texto | Nome do bloco exploratório ou do campo em desenvolvimento cujo contrato foi aditado (por exemplo `PN-T-102` ou `Tupi_Sul`). | — | — |
| `Bacia` | `Bacia` | texto | Bacia sedimentar onde estão o bloco ou o campo; a grafia varia (`Potiguar` e `POTIGUAR`). | — | — |
| `Localização` | `Localização` | texto | Ambiente em que se localiza o bloco ou o campo: `Terra` (354 linhas) ou `Mar` (164). | — | — |
| `Rodada` | `Rodada` | texto | Rodada de licitação de origem do contrato, em código (`BID07`, `BID11`, `AM1`, `CO_2010`, `PP1`, `BID13AM` e outros; 19 valores). | — | — |
| `Status` | `Status` | texto | Situação da solicitação: `Assinado, publicado no D.O.U. em DD/MM/AAAA.` (333 linhas), `Analisado, indeferida a solicitação de adesão ao Termo Aditivo.` (161), `Contrato aditado fora do escopo da Resolução 726/2018...` (17), `Anexado ao Campo ...` (5) e dois textos isolados; a data de publicação fica dentro do texto. | — | — |
| `Link Extrato DOU` | `Link Extrato DOU` | texto | Alcance do aditamento e link de publicação do extrato no Diário Oficial da União. Texto livre, em geral `Bloco alcançado pelo Termo Aditivo assinado em DD/MM/AAAA.` ou `Campo ...`, seguido de quebra de linha e `Link: <URL>` (335 linhas trazem URL); vazio em 25. | — | — |

## No lake

- Dataset `anp/aditamento-conteudo-local`, sem partição: um Parquet, `aditamento-conteudo-local.parquet`, com as 518 linhas.
- Todas as colunas são texto e mantêm o cabeçalho da fonte (com acentos, espaços e `/`, como `Nome do Bloco / Campo`).

## Cuidados de uso

- **Planilha estática.** Os pedidos se encerraram em agosto de 2018 e as situações vão até janeiro de 2021; não é série temporal e não reflete contratos assinados depois.
- **Data do protocolo em dois formatos.** 514 linhas trazem `DD/MM/AAAA`; 4 trazem o número de série de data do Excel (`43313` é 01/08/2018 e `43321` é 09/08/2018). Converta os dois formatos antes de ordenar.
- **`Status` mistura estado e data.** A data de publicação no D.O.U. está dentro do texto (`Assinado, publicado no D.O.U. em 27/12/2018.`), com variações de caixa e espaços (`Assinado, Publicado ...`, `em  10/05/2019`); extraia com expressão regular e normalize antes de agrupar.
- **`Link Extrato DOU` é texto livre**, com quebra de linha dentro do campo e, às vezes, sem link (25 vazias; `Anexado ao Campo Gavião Branco.` e `Bloco NÃO alcançado pelo Termo Aditivo...` não têm URL).
- **Grafias.** `Bacia` aparece como `Potiguar` (60) e `POTIGUAR` (5); `Rodada` usa códigos de formato variado (`BID07`, `CO_2010`, `AM1`).
- **Contratos de 266 versus 287.** A página da ANP fala em 266 contratos com compromissos atualizados; o arquivo traz 287 contratos distintos porque inclui solicitações indeferidas e fora do escopo, e não só as aditadas.
- **Chave (conferida na amostra).** `Ordem` é única nas 518 linhas e é a ordem de recebimento descrita pelo metadado; não repete entre linhas.
- **Dados pessoais.** Só há nomes de empresas operadoras (pessoas jurídicas); não há pessoa física nem CNPJ.

## Exemplos

Situação das solicitações por rodada de licitação (as assinadas são as que têm `Assinado` no início do `Status`):

```python
import duckdb

duckdb.sql("""
    SELECT "Rodada",
           count(*) AS solicitacoes,
           count(*) FILTER (WHERE "Status" ILIKE 'Assinado%') AS assinadas,
           count(*) FILTER (WHERE "Status" ILIKE 'Analisado, indeferida%') AS indeferidas
    FROM read_parquet('lake/anp/aditamento-conteudo-local/aditamento-conteudo-local.parquet')
    GROUP BY 1
    ORDER BY solicitacoes DESC
    LIMIT 8
""").show()
```

## Referências

- Aditamento de conteúdo local (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/aditamento-conteudo-local
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-aditamento-conteudo-local/metadados-aditamento.pdf
- Resolução ANP nº 726/2018 e Resolução CNPE nº 1/2018, citadas na página da ANP.
