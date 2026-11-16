---
dataset:
  id: distribuidores
  fonte: anp
  titulo: 'Distribuidores de combustíveis líquidos: autorizações, contratos de cessão de espaço e inutilizadores de GLP'
  resumo: 'Três tabelas da ANP sobre a distribuição de combustíveis líquidos: distribuidores autorizados (e suas situações), contratos de cessão de espaço ou carregamento homologados e agentes inutilizadores de botijões de GLP.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-distribuidores-de-combustiveis-liquidos
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'varia por tabela, segundo os metadados da ANP: distribuidores mensal (arquivo gerado em 08/05/2026), cessão de espaço semanal (atualizado em 13/11/2026) e inutilizadores semestral (gerado em 09/04/2026)'
  cobertura:
    inicio: '1996'
    fim: em-curso
  unidade: 'depende da tabela: um estabelecimento (CNPJ) de distribuidor em `distribuidores-filiais`, um contrato homologado em `distribuidores-cessao-espaco` e um agente inutilizador em `distribuidores-inutilizadores-glp`'
  granularidade:
    espacial: estabelecimento (município e UF; endereço da matriz) e, nos contratos, município e UF da cedente
    temporal: data do ato de autorização ou situação (`dd/mm/aaaa`) e, nos contratos, data do ofício de homologação e término do contrato
  formato_bruto: 3 CSV com separador `;` e CRLF, em codificação Windows/ISO-8859 (não UTF-8); `distribuidores-filiais` e `distribuidores-inutilizadores-glp` têm 4 linhas de cabeçalho institucional antes da linha de colunas
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 47
  unidades_de_medida:
    VOLUME (m³): m³
    Gasolina A: m³
    Gasolina A - Premium: m³
    Gasolina C: m³
    B100: m³
    EAC: m³
    EHC: m³
    Óleo Diesel A S500: m³
    Óleo Diesel A S10: m³
    Óleo Diesel B S500: m³
    Óleo Diesel B S10: m³
    Diesel C S10: m³
    Óleo Diesel Mar: m³
    OC - 1A: m³
    OC - 1B: m³
    GAV: m³
    QAV: m³
    Querosene Iluminante: m³
  dados_pessoais:
  - coluna: RAZÃO SOCIAL DA CEDENTE
    categoria: razão social de pessoa jurídica
  - coluna: RAZÃO SOCIAL DA CESSIONÁRIA
    categoria: razão social de pessoa jurídica
  - coluna: Nome Reduzido
    categoria: razão social de pessoa jurídica
  - coluna: Razão Social
    categoria: razão social de pessoa jurídica
  - coluna: CNPJ DA CEDENTE
    categoria: CNPJ de pessoa jurídica
  - coluna: CNPJ DA CESSIONÁRIA
    categoria: CNPJ de pessoa jurídica
  - coluna: CNPJ
    categoria: CNPJ de pessoa jurídica
  - coluna: Endereço da Matriz
    categoria: endereço da empresa
  - coluna: Bairro
    categoria: endereço da empresa
  - coluna: CEP
    categoria: endereço da empresa
  eras:
  - desde: '2026'
    mudanca: formato único observado nos arquivos de 15/11/2026; os metadados em PDF (de 2021) descrevem colunas diferentes das dos arquivos atuais, sobretudo nos inutilizadores (veja Cuidados de uso)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Distribuidores de combustíveis líquidos: autorizações, contratos de cessão de espaço e inutilizadores de GLP

## Resumo

Conjunto da ANP sobre distribuidores de combustíveis líquidos, reunindo três tabelas pequenas: a relação de distribuidores com autorização de exercício de atividade (e o histórico de situações), os contratos de cessão de espaço de tancagem ou de carregamento rodoviário homologados pela ANP entre cedentes (bases, refinarias, terminais, produtoras) e cessionárias (distribuidores), e os agentes cadastrados para inutilizar botijões de GLP. O lake mantém as três tabelas num mesmo dataset, sem partições; a coluna *Arquivos* do dicionário mostra a que tabela cada coluna pertence.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/distribuidores` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-distribuidores-de-combustiveis-liquidos |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | varia por tabela, segundo os metadados da ANP: distribuidores mensal (arquivo gerado em 08/05/2026), cessão de espaço semanal (atualizado em 13/11/2026) e inutilizadores semestral (gerado em 09/04/2026) |
| Cobertura | 1996 a em-curso |
| Unidade (uma linha) | depende da tabela: um estabelecimento (CNPJ) de distribuidor em `distribuidores-filiais`, um contrato homologado em `distribuidores-cessao-espaco` e um agente inutilizador em `distribuidores-inutilizadores-glp` |
| Granularidade | espacial: estabelecimento (município e UF; endereço da matriz) e, nos contratos, município e UF da cedente; temporal: data do ato de autorização ou situação (`dd/mm/aaaa`) e, nos contratos, data do ofício de homologação e término do contrato |
| Formato bruto | 3 CSV com separador `;` e CRLF, em codificação Windows/ISO-8859 (não UTF-8); `distribuidores-filiais` e `distribuidores-inutilizadores-glp` têm 4 linhas de cabeçalho institucional antes da linha de colunas |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 47 |
| Unidades de medida | `VOLUME (m³)`: m³; `Gasolina A`: m³; `Gasolina A - Premium`: m³; `Gasolina C`: m³; `B100`: m³; `EAC`: m³; `EHC`: m³; `Óleo Diesel A S500`: m³; `Óleo Diesel A S10`: m³; `Óleo Diesel B S500`: m³; `Óleo Diesel B S10`: m³; `Diesel C S10`: m³; `Óleo Diesel Mar`: m³; `OC - 1A`: m³; `OC - 1B`: m³; `GAV`: m³; `QAV`: m³; `Querosene Iluminante`: m³ |
| Dados pessoais | `RAZÃO SOCIAL DA CEDENTE` (razão social de pessoa jurídica); `RAZÃO SOCIAL DA CESSIONÁRIA` (razão social de pessoa jurídica); `Nome Reduzido` (razão social de pessoa jurídica); `Razão Social` (razão social de pessoa jurídica); `CNPJ DA CEDENTE` (CNPJ de pessoa jurídica); `CNPJ DA CESSIONÁRIA` (CNPJ de pessoa jurídica); `CNPJ` (CNPJ de pessoa jurídica); `Endereço da Matriz` (endereço da empresa); `Bairro` (endereço da empresa); `CEP` (endereço da empresa) |
| Eras | 2026: formato único observado nos arquivos de 15/11/2026; os metadados em PDF (de 2021) descrevem colunas diferentes das dos arquivos atuais, sobretudo nos inutilizadores (veja Cuidados de uso) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa três arquivos de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/dcl/`: `planilha-aea-filiais.csv` (distribuidores autorizados, "atualizado em 8/5/2026"), `ce-cr.csv` (contratos de cessão de espaço e carregamento homologados, atualizado em 13/11/2026) e `inutilizadores.csv` (agentes inutilizadores de botijões de GLP, atualizado em 9/4/2026), conforme a página oficial.
- No bruto os arquivos se chamam `distribuidores-filiais@AAAAMMDD.csv`, `distribuidores-cessao-espaco@AAAAMMDD.csv` e `distribuidores-inutilizadores-glp@AAAAMMDD.csv`, em que o sufixo é a data de modificação informada pela fonte ou, se o servidor não informa, a data do download.
- Os arquivos de distribuidores e de inutilizadores começam com um cabeçalho institucional de quatro linhas (`Agência Nacional do Petroleo - ANP`, a data de geração, `SIMP` e o nome do cadastro), que o conversor descarta; a primeira linha dos dados fica na quinta linha.
- Metadados em PDF (2021): `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/dcl/metadados-aea-distliq-27out21.pdf` (distribuidores; fonte SIMP; órgão SDL/CRAT), `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/dcl/metadados-ce-cr-26ago21.pdf` (cessão; fonte processos concluídos do SEI) e `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/dcl/metadados-inutilizadora-26ago21.pdf` (inutilizadores; fonte SIMP e SEI).

## Conteúdo

- **Três tabelas num dataset.** O lake guarda um Parquet por tabela, e a coluna *Arquivos* do dicionário indica de qual tabela vem cada coluna; 13 colunas (de `Código Agente` a `Data Publicação`) são comuns a `distribuidores-filiais` e `distribuidores-inutilizadores-glp`.

| Tabela (Parquet) | O que é uma linha | Linhas | Colunas | Atualização na fonte |
|---|---|---|---|---|
| `distribuidores-filiais` | um estabelecimento (CNPJ) de distribuidor de combustíveis líquidos, com a situação de sua autorização | 713 | 16 | mensal (metadados); arquivo de 08/05/2026 |
| `distribuidores-cessao-espaco` | um contrato de cessão de espaço ou de carregamento rodoviário homologado, com volume por produto | 1.960 | 30 | semanal (metadados); atualizado em 13/11/2026 |
| `distribuidores-inutilizadores-glp` | um agente cadastrado para inutilizar botijões de GLP | 36 | 14 | semestral (metadados); arquivo de 09/04/2026 |

- **Distribuidores (`distribuidores-filiais`).** Apesar do título "autorizados ao exercício da atividade", o arquivo traz o histórico: 346 linhas CANCELADA, 181 AUTORIZADA, 147 AUTORIZAÇÃO REVOGADA, 23 HABILITAÇÃO REVOGADA, 7 HABILITADA, 5 AUTORIZADA POR DECISÃO JUDICIAL e 1 INOPERANTE (3 sem situação). Os 713 CNPJs são únicos e estão em 25 UFs, com SP (268), PR (100) e RJ (62) à frente.
- **Contratos (`distribuidores-cessao-espaco`).** 1.338 contratos de CESSÃO DE ESPAÇO e 622 de CARREGAMENTO, com 137 cedentes (244 CNPJs) e 173 cessionárias (864 CNPJs); a maior cedente é a Transpetro (426 contratos). Cada contrato traz o volume total e o volume por produto (17 colunas de produto, de `Gasolina A` a `Querosene Iluminante`). `PROCESSO` tem 1.948 valores distintos em 1.960 linhas, isto é, alguns processos aparecem em mais de uma linha (possivelmente aditivos, o que não foi verificado). As datas dos ofícios de homologação vão de 20/06/2004 a 29/10/2026.
- **Inutilizadores (`distribuidores-inutilizadores-glp`).** 36 agentes (30 CADASTRADA e 6 OPERAÇÃO) em 11 UFs, com SP (8), CE (5) e PA (4) à frente; `Data Fim` e `Data Publicação` vêm vazias em todas as linhas.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `distribuidores-cessao-espaco` (30); `distribuidores-filiais` (16); `distribuidores-inutilizadores-glp` (14) |

## Variáveis

As descrições vêm dos três documentos de metadados da ANP (2021) e, quando o arquivo atual difere do metadado, dos valores observados na amostra. Os nomes das colunas do lake são os do cabeçalho de cada arquivo (`distribuidores-cessao-espaco` em maiúsculas e com grau `N°`; as demais com acento e espaços).
Todas as colunas são texto. As siglas dos produtos do contrato (EAC, EHC, GAV, QAV) não são expandidas nos metadados; a expansão registrada é a dedução a partir da sigla.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `TIPO DE CONTRATO` | `TIPO DE CONTRATO` | texto | Tipo de contrato homologado | CESSÃO DE ESPAÇO = 1.338 contratos; CARREGAMENTO = 622 contratos | — | `distribuidores-cessao-espaco` |
| `RAZÃO SOCIAL DA CEDENTE` | `RAZÃO SOCIAL DA CEDENTE` | texto | Nome da empresa cedente (base, refinaria, terminal ou produtora que cede o espaço ou o ponto de carregamento) | — | — | `distribuidores-cessao-espaco` |
| `CNPJ DA CEDENTE` | `CNPJ DA CEDENTE` | texto | Número de inscrição da empresa cedente no CNPJ, com pontuação | — | — | `distribuidores-cessao-espaco` |
| `N° AO DA CEDENTE` | `N° AO DA CEDENTE` | texto | Número e ano da Autorização de Operação (AO) da instalação cedente, publicada no DOU (por exemplo, `432/2023`) | — | — | `distribuidores-cessao-espaco` |
| `MUNICÍPIO DA CEDENTE` | `MUNICÍPIO DA CEDENTE` | texto | Município onde se localiza a empresa cedente | — | — | `distribuidores-cessao-espaco` |
| `UF DA CEDENTE` | `UF DA CEDENTE` | texto | Unidade Federativa onde se localiza a empresa cedente | — | — | `distribuidores-cessao-espaco` |
| `RAZÃO SOCIAL DA CESSIONÁRIA` | `RAZÃO SOCIAL DA CESSIONÁRIA` | texto | Nome da empresa cessionária (distribuidor de combustíveis líquidos, de aviação, de GLP ou TRR) | — | — | `distribuidores-cessao-espaco` |
| `CNPJ DA CESSIONÁRIA` | `CNPJ DA CESSIONÁRIA` | texto | Número de inscrição da empresa cessionária no CNPJ, com pontuação | — | — | `distribuidores-cessao-espaco` |
| `N° DA AEA CESSIONÁRIA` | `N° DA AEA CESSIONÁRIA` | texto | Número e ano da Autorização de Exercício de Atividade (AEA) da cessionária, publicada no DOU; traz o texto `Aviação` em alguns contratos e erros de digitação (`823/22024`) | — | — | `distribuidores-cessao-espaco` |
| `INÍCIO CONTRATO (ATO DE HOMOLOGAÇÃO)` | `INÍCIO CONTRATO (ATO DE HOMOLOGAÇÃO)` | texto | Ato de homologação do contrato: número/ano do Ofício SDL (`Ofício SDL 427 de 30/01/2026`) ou do despacho, com a data. É texto, não uma data; em duas linhas a palavra vem grafada `Oficío` | — | — | `distribuidores-cessao-espaco` |
| `PROCESSO` | `PROCESSO` | texto | Número do processo SEI do contrato homologado | — | — | `distribuidores-cessao-espaco` |
| `TÉRMINO CONTRATO` | `TÉRMINO CONTRATO` | texto | Data de término do contrato. Os metadados dizem `DD/MM/AAAA`, mas 1.956 das 1.960 linhas vêm como número de série de data do Excel (`46387` é 31/12/2026) e quatro têm valores inválidos (`31/11/2026`, `31/09/2027`, `413194`, `413256`) | — | — | `distribuidores-cessao-espaco` |
| `VOLUME (m³)` | `VOLUME (m³)` | texto | Volume total do contrato, somatório dos volumes de todos os produtos, em m³ (texto; vírgula decimal em 37 linhas, como `754,5`) | — | — | `distribuidores-cessao-espaco` |
| `Gasolina A` | `Gasolina A` | texto | Volume de gasolina A em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Gasolina A - Premium` | `Gasolina A - Premium` | texto | Volume de gasolina A Premium em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Gasolina C` | `Gasolina C` | texto | Volume de gasolina C em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `B100` | `B100` | texto | Volume de biodiesel B100 em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `EAC` | `EAC` | texto | Volume de EAC (sigla da fonte; etanol anidro combustível, deduzido da sigla) em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `EHC` | `EHC` | texto | Volume de EHC (sigla da fonte; etanol hidratado combustível, deduzido da sigla) em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Óleo Diesel A S500` | `Óleo Diesel A S500` | texto | Volume de óleo diesel A S500 em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Óleo Diesel A S10` | `Óleo Diesel A S10` | texto | Volume de óleo diesel A S10 em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Óleo Diesel B S500` | `Óleo Diesel B S500` | texto | Volume de óleo diesel B S500 em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Óleo Diesel B S10` | `Óleo Diesel B S10` | texto | Volume de óleo diesel B S10 em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Diesel C S10` | `Diesel C S10` | texto | Volume de diesel C S10 (coluna que existe no arquivo mas não nos metadados) em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Óleo Diesel Mar` | `Óleo Diesel Mar` | texto | Volume de óleo diesel Mar em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `OC - 1A` | `OC - 1A` | texto | Volume de óleo combustível 1A em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `OC - 1B` | `OC - 1B` | texto | Volume de óleo combustível 1B em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `GAV` | `GAV` | texto | Volume de GAV (sigla da fonte; gasolina de aviação, deduzida da sigla) em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `QAV` | `QAV` | texto | Volume de QAV (sigla da fonte; querosene de aviação, deduzida da sigla) em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Querosene Iluminante` | `Querosene Iluminante` | texto | Volume de querosene iluminante em contrato, em m³ (texto; vírgula decimal quando há fração) | — | — | `distribuidores-cessao-espaco` |
| `Código Agente` | `Código Agente` | texto | Código do agente (número). Não é único: no arquivo `distribuidores-filiais` o código 1288 aparece em dois CNPJs (matriz e filial) | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Código Agente i-SIMP` | `Código Agente i-SIMP` | texto | Código do agente no i-SIMP (número); vazio em 36 linhas de `distribuidores-filiais` | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `CNPJ` | `CNPJ` | texto | Número de inscrição da empresa no Cadastro Nacional da Pessoa Jurídica, com pontuação (`00.000.000/0000-00`); um por estabelecimento (matriz ou filial) | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Nome Reduzido` | `Nome Reduzido` | texto | Nome reduzido da empresa | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Razão Social` | `Razão Social` | texto | Nome (razão social) da empresa | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Endereço da Matriz` | `Endereço da Matriz` | texto | Endereço onde a matriz está localizada (logradouro e número, texto livre) | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Bairro` | `Bairro` | texto | Bairro onde a empresa está localizada | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Municipio` | `Municipio` | texto | Município onde a empresa está localizada, em maiúsculas e em geral sem acentos | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `UF` | `UF` | texto | Unidade Federativa onde a empresa está localizada | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `CEP` | `CEP` | texto | Número do Código de Endereço Postal de onde a empresa se localiza, no formato `99999-999` | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Situação` | `Situação` | texto | Situação do agente. Os metadados de `distribuidores-filiais` citam "Autorizada" e "Autorizada por Decisão Judicial", mas o arquivo traz também situações encerradas; em `distribuidores-inutilizadores-glp` os valores são CADASTRADA e OPERAÇÃO | CANCELADA = 346 linhas em `distribuidores-filiais`; AUTORIZADA = 181 linhas; AUTORIZAÇÃO REVOGADA = 147; HABILITAÇÃO REVOGADA = 23; HABILITADA = 7; AUTORIZADA POR DECISÃO JUDICIAL = 5; INOPERANTE = 1; … (lista completa no dicionário da fonte) | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Início da Situação` | `Início da Situação` | texto | Data de início da situação atual (`dd/mm/aaaa`); `01/01/1900` é valor-padrão (placeholder) em 171 linhas de `distribuidores-filiais`, quase todas CANCELADA | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Data Publicação` | `Data Publicação` | texto | Data de publicação do ato (`dd/mm/aaaa`); vazia em 305 das 713 linhas de `distribuidores-filiais` e em todas as de `distribuidores-inutilizadores-glp` | — | — | `distribuidores-filiais`, `distribuidores-inutilizadores-glp` |
| `Tipo de Ato` | `Tipo de Ato` | texto | Tipo do ato que originou a situação (`distribuidores-filiais`) | DESPACHO = 221 linhas; AUTORIZAÇÃO = 187 linhas | — | `distribuidores-filiais` |
| `Tipo de Autorização` | `Tipo de Autorização` | texto | Tipo de autorização, `AUTORIZAÇÃO DE EXERCÍCIO DE ATIVIDADE` quando preenchido (`distribuidores-filiais`; vazio em 511 linhas) | — | — | `distribuidores-filiais` |
| `Número da Autorização` | `Número da Autorização` | texto | Número da autorização da empresa (`distribuidores-filiais`); os metadados chamam o campo de "Número do Ato". Pode vir como `00` ou como referência de ofício (`Ofício 117 (5016708)`) | — | — | `distribuidores-filiais` |
| `Data Fim` | `Data Fim` | texto | Data de fim da atividade (`dd/mm/aaaa`); coluna do arquivo `distribuidores-inutilizadores-glp`, vazia em todas as linhas da amostra | — | — | `distribuidores-inutilizadores-glp` |

## No lake

- Dataset `anp/distribuidores`, sem partições: três Parquet, `distribuidores-filiais.parquet`, `distribuidores-cessao-espaco.parquet` e `distribuidores-inutilizadores-glp.parquet`, cada um com as colunas do respectivo CSV, todas como texto.
- O conversor pula as quatro linhas de cabeçalho institucional dos arquivos de distribuidores e de inutilizadores e lê os acentos corretamente (os CSV não estão em UTF-8).

## Cuidados de uso

- **Não é só "autorizados".** `distribuidores-filiais` tem mais linhas canceladas (346) do que autorizadas (181); para a lista de distribuidores ativos filtre `Situação` em `AUTORIZADA` e `AUTORIZADA POR DECISÃO JUDICIAL`.
- **`Início da Situação` = `01/01/1900`** em 171 linhas de `distribuidores-filiais` (169 CANCELADA) é um valor-padrão, não uma data real.
- **Chaves não são únicas.** `Código Agente` se repete em dois CNPJs (por exemplo, o código 1288 da TIC TRANSPORTES LTDA., matriz e filial) e `Código Agente i-SIMP` falta em 36 linhas; em `distribuidores-cessao-espaco`, `PROCESSO` tem 12 repetições. Use `CNPJ` em `distribuidores-filiais`.
- **`TÉRMINO CONTRATO` não é data legível.** Quase todas as linhas trazem o número de série de data do Excel (data = 30/12/1899 mais o número de dias; em DuckDB, `date '1899-12-30' + n`); `31/11/2026` e `31/09/2027` são datas inexistentes e `413194` e `413256` equivalem ao ano 3031, provável erro de digitação.
- **`INÍCIO CONTRATO (ATO DE HOMOLOGAÇÃO)` é texto livre**, no formato `Ofício SDL <número> de <data>`; extraia a data com expressão regular (duas linhas trazem `Oficío`).
- **Volumes são texto, com vírgula decimal em 37 linhas.** Troque a vírgula por ponto antes de converter (`replace(..., ',', '.')`); a coluna `VOLUME (m³)` é o total declarado e pode diferir da soma dos produtos em contratos com fração. Os produtos EAC, EHC, GAV e QAV usam siglas não expandidas nos metadados.
- **Metadados desatualizados.** Os metadados de 2021 listam colunas que o arquivo atual não tem (`Processo Relacionado` e `Óleo Diesel Não Rodoviário`, nos contratos; `Código Instalação i-SIMP`, `Nome da Instalação` e `Número` nos inutilizadores) e o arquivo de contratos traz `Diesel C S10`, que não consta nos metadados.
- **Dados pessoais.** Só há razões sociais e CNPJ de empresas (distribuidores, cedentes, cessionárias, requalificadoras) e o endereço da matriz; em empresas individuais a razão social pode trazer o nome do titular.

## Exemplos

Situação dos distribuidores de combustíveis líquidos por UF, mostrando só os autorizados:

```python
import duckdb

duckdb.sql("""
    SELECT UF, count(*) AS distribuidores
    FROM read_parquet('lake/anp/distribuidores/distribuidores-filiais.parquet')
    WHERE "Situação" IN ('AUTORIZADA', 'AUTORIZADA POR DECISÃO JUDICIAL')
    GROUP BY UF
    ORDER BY distribuidores DESC
    LIMIT 10
""").show()
```

Volume contratado de cessão de espaço por cedente (m³), com a vírgula decimal tratada:

```python
import duckdb

duckdb.sql("""
    SELECT "RAZÃO SOCIAL DA CEDENTE" AS cedente, count(*) AS contratos,
           round(sum(try_cast(replace("VOLUME (m³)", ',', '.') AS DOUBLE))) AS volume_m3
    FROM read_parquet('lake/anp/distribuidores/distribuidores-cessao-espaco.parquet')
    GROUP BY ALL
    ORDER BY volume_m3 DESC
    LIMIT 5
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-distribuidores-de-combustiveis-liquidos
- Metadados dos distribuidores autorizados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/dcl/metadados-aea-distliq-27out21.pdf
- Metadados dos contratos de cessão de espaço e carregamento (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/dcl/metadados-ce-cr-26ago21.pdf
- Metadados dos agentes inutilizadores de GLP (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/dcl/metadados-inutilizadora-26ago21.pdf
- Lei nº 9.847/1999, citada pela página como base da regulação do abastecimento nacional de combustíveis pela ANP.
