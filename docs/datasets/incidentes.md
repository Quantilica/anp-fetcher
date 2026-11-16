---
dataset:
  id: incidentes
  fonte: anp
  titulo: Incidentes de segurança operacional em exploração e produção de petróleo e gás (SISO-Incidentes)
  resumo: 'Incidentes de segurança operacional comunicados à ANP nas atividades de exploração e produção de petróleo e gás natural, de 2013 a 2026: tabela principal (30.744 incidentes) e tabelas de classificação, feridos, substâncias e tipo.'
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/incidentes-seguranca-operacional
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: semestral, segundo o metadado da ANP (dados abertos atualizados em 20/05/2026; metadados em 11/06/2026)
  cobertura:
    inicio: 2013-07
    fim: 2026-05
  unidade: 'depende do arquivo: um incidente (`issm-incidentes`); uma classificação, um ferimento, uma substância ou um tipo de um incidente (`issm-classificacao`, `issm-feridos`, `issm-substancias` e `issm-tipo`)'
  granularidade:
    espacial: instalação (nome e código), com latitude e longitude em graus decimais e endereço em texto livre; sem município ou UF em coluna própria
    temporal: data de registro do incidente (de 2013-07 a 2026-05, no número do incidente e em `Data_de_criacao`) e data e hora estimadas da ocorrência
  formato_bruto: cinco CSV em ISO-8859-1 (Latin-1), separados por ponto e vírgula
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 26
  unidades_de_medida:
    Latitude: graus decimais (texto, ponto decimal)
    Longitude: graus decimais (texto, ponto decimal)
    Volume: unidade não informada pela fonte (texto, vírgula decimal)
    Numero_de_feridos_graves: pessoas (inteiro em texto)
    Numero_Fatalidades: pessoas (inteiro em texto)
  dados_pessoais:
  - coluna: Empresa
    categoria: razão social e CNPJ de empresa (pessoa jurídica) que comunicou o incidente
  - coluna: CNPJ
    categoria: razão social e CNPJ de empresa (pessoa jurídica) que comunicou o incidente
  - coluna: Breve_Descricao_Incidente
    categoria: texto livre que às vezes cita o nome de pessoa física (por exemplo, empregado ou comandante, precedido de `Sr.`), apesar de a ANP dizer que divulga os dados sem informações pessoais
  eras:
  - desde: '2013'
    mudanca: série contínua de 2013-07 a 2026-05 na coleta de 2026-11-15, em um único layout de cinco arquivos
  - desde: '2025'
    mudanca: em novembro de 2025 a ANP passou a divulgar a operadora e a instalação logo após a notificação (Decisão de Diretoria nº 319/2025), e não só após a investigação; o fetcher guarda apenas a versão corrente, e a diferença não é visível nas colunas
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Incidentes de segurança operacional em exploração e produção de petróleo e gás (SISO-Incidentes)

## Resumo

A ANP recebe a Comunicação Inicial dos incidentes das atividades de exploração e produção pelo Sistema Integrado de Segurança Operacional (SISO-Incidentes), nos termos da Resolução ANP nº 882/2022, e divulga os dados em cinco tabelas CSV ligadas pela coluna `Numero`: a principal (`INCIDENTES`: empresa, instalação, datas, localização, feridos graves, fatalidades e descrição) e quatro secundárias (classificação, feridos, substâncias e tipos do incidente). Cada incidente tem um registro na principal e zero ou mais nas secundárias. Segundo a página, os dados são divulgados nos termos da Lei de Acesso à Informação, sem informações pessoais; a ANP também publica os relatórios de investigação dos incidentes, fora deste dataset.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/incidentes` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/incidentes-seguranca-operacional |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | semestral, segundo o metadado da ANP (dados abertos atualizados em 20/05/2026; metadados em 11/06/2026) |
| Cobertura | 2013-07 a 2026-05 |
| Unidade (uma linha) | depende do arquivo: um incidente (`issm-incidentes`); uma classificação, um ferimento, uma substância ou um tipo de um incidente (`issm-classificacao`, `issm-feridos`, `issm-substancias` e `issm-tipo`) |
| Granularidade | espacial: instalação (nome e código), com latitude e longitude em graus decimais e endereço em texto livre; sem município ou UF em coluna própria; temporal: data de registro do incidente (de 2013-07 a 2026-05, no número do incidente e em `Data_de_criacao`) e data e hora estimadas da ocorrência |
| Formato bruto | cinco CSV em ISO-8859-1 (Latin-1), separados por ponto e vírgula |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 26 |
| Unidades de medida | `Latitude`: graus decimais (texto, ponto decimal); `Longitude`: graus decimais (texto, ponto decimal); `Volume`: unidade não informada pela fonte (texto, vírgula decimal); `Numero_de_feridos_graves`: pessoas (inteiro em texto); `Numero_Fatalidades`: pessoas (inteiro em texto) |
| Dados pessoais | `Empresa` (razão social e CNPJ de empresa (pessoa jurídica) que comunicou o incidente); `CNPJ` (razão social e CNPJ de empresa (pessoa jurídica) que comunicou o incidente); `Breve_Descricao_Incidente` (texto livre que às vezes cita o nome de pessoa física (por exemplo, empregado ou comandante, precedido de `Sr.`), apesar de a ANP dizer que divulga os dados sem informações pessoais) |
| Eras | 2013: série contínua de 2013-07 a 2026-05 na coleta de 2026-11-15, em um único layout de cinco arquivos; 2025: em novembro de 2025 a ANP passou a divulgar a operadora e a instalação logo após a notificação (Decisão de Diretoria nº 319/2025), e não só após a investigação; o fetcher guarda apenas a versão corrente, e a diferença não é visível nas colunas |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Cinco arquivos CSV na página de dados abertos de incidentes de segurança operacional da ANP, em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/issm/`: `incidentes.csv` (16.539.231 bytes), `incidentes-classificacao.csv` (1.949.472), `incidentes-feridos.csv` (418.999), `incidentes-substancias.csv` (572.112) e `incidentes-tipo.csv` (2.667.913). Tamanhos conferidos na coleta de 2026-11-15.
- Fonte do dado, segundo o metadado (`metadados-incidentes.pdf`, atualizado em 11/06/2026): ANP/Superintendência de Segurança Operacional, a partir do SISO-Incidentes (https://siso.anp.gov.br/); periodicidade de extração semestral; contato cdados_sso@anp.gov.br. A página informa que cada arquivo foi atualizado em 20/05/2026.
- A página explica que, em novembro de 2025, a ANP mudou a forma de apresentação: operadora e instalação passam a ser divulgadas logo após a notificação, e não só nos relatórios de investigação (Decisão de Diretoria nº 319/2025).
- O servidor não informa a data de modificação dos arquivos; o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15).

## Conteúdo

- **`issm-incidentes` (tabela principal, 30.744 linhas):** um incidente por linha, com 19 colunas. `Numero` é único. Incidentes por ano de registro: 1.646 (2013, a partir de julho), 1.811 (2014), 2.197 (2015), 2.881 (2016), 2.090 (2017), 1.984 (2018), 2.325 (2019), 1.846 (2020), 2.697 (2021), 2.415 (2022), 2.414 (2023), 2.686 (2024), 2.715 (2025) e 1.037 (2026, até maio).
- **`issm-classificacao` (45.240 linhas, 30.741 incidentes):** classificação do incidente; os valores mais frequentes são `Risco de dano à saúde humana` (19.200), `Risco de dano ao meio ambiente` (15.780) e `Dano ao meio ambiente` (5.440).
- **`issm-feridos` (30.821 linhas):** tipo de ferimento ou fatalidade; 579 linhas têm tipo (`Fratura (excluíndo de dedos)` em 237 e `Fatalidade` em 36) e 30.242 são linhas vazias de incidentes sem ferido.
- **`issm-substancias` (31.534 linhas):** substância e volume derramados ou vazados; só 6.281 linhas têm substância, e o resto são linhas vazias (por exemplo, `Óleo` em 1.543 e `Fluido hidráulico` em 1.342).
- **`issm-tipo` (35.597 linhas, 30.744 incidentes):** tipo, gravidade e ocorrência (acidente ou quase acidente). Por linha: `LEVE` em 28.721, `MODERADO` em 3.953, `GRAVE` em 588 e vazio em 2.335 (`Reclassificação`); `Quase acidente` em 22.849 e `Acidente` em 10.413.
- **Gravidade humana:** 752 incidentes registram feridos graves (801 pessoas) e 34 registram fatalidades (45 mortes).

## Variáveis

As descrições vêm do metadado `metadados-incidentes.pdf` da ANP; os contadores e as irregularidades vêm da amostra do lake (2026-11-15), que cobre os cinco arquivos inteiros. O metadado dá `Data_de_criacao` e datas como "Data", horas como "Hora" e contagens como número inteiro, mas o lake guarda tudo como texto.
O metadado grafa `Numero_de_fatalidades` e `Hora_ da_primeira_observacao`; o CSV traz `Numero_Fatalidades` e `Hora_da_primeira_observacao`. A coluna *Arquivos* diz em quais tabelas cada coluna aparece (`Numero` está em todas).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Numero` | `Numero` | texto | Número de registro e identificação do incidente, no formato `AAMM/NNNNNN` (os quatro primeiros dígitos são o ano e o mês do registro, conferido com `Data_de_criacao`); liga a tabela principal às quatro secundárias. Está nos cinco arquivos. | — | — | `issm-classificacao`, `issm-feridos`, `issm-incidentes` e mais 2 |
| `Classificacao_do_incidente` | `Classificacao_do_incidente` | texto | Classificação do incidente (7 valores, como `Risco de dano à saúde humana`, `Risco de dano ao meio ambiente`, `Dano ao meio ambiente`, `Dano à saúde humana` e `Prejuízos materiais ao patrimônio próprio ou de terceiros`); um incidente pode ter várias classificações; só em `issm-classificacao`. | — | — | `issm-classificacao` |
| `Tipo_de_Ferimento_barra_Fatalidade` | `Tipo_de_Ferimento_barra_Fatalidade` | texto | Tipo de ferimento ou fatalidade sofrido (8 valores, como `Fratura (excluíndo de dedos)`, `Amputação`, `Fatalidade`); vazio em 30.242 das 30.821 linhas de `issm-feridos` (incidente sem ferido); só em `issm-feridos`. A grafia `excluíndo` é a da fonte. | — | — | `issm-feridos` |
| `Empresa` | `Empresa` | texto | Empresa que identificou e cadastrou o incidente, como `RAZÃO SOCIAL (CNPJ de 14 dígitos)`; só na tabela principal. A mesma empresa pode aparecer com razões sociais diferentes (`PETRÓLEO BRASILEIRO S.A.` e `PETRÓLEO BRASILEIRO S.A. - PETROBRAS`). | — | — | `issm-incidentes` |
| `CNPJ` | `CNPJ` | texto | CNPJ da empresa, só dígitos (14); só na tabela principal. | — | — | `issm-incidentes` |
| `Data_de_criacao` | `Data_de_criacao` | texto | Data do registro do incidente nos sistemas da ANP (DD-MM-AAAA, texto), de 09-07-2013 a 19-05-2026. | — | — | `issm-incidentes` |
| `Autoridades_comunicadas` | `Autoridades_comunicadas` | texto | Autoridades que foram comunicadas a respeito do incidente, em texto livre (`Marinha DL/CP - Macaé/RJ`, `Órgão ambiental estadual, INEMA-BA.`, `N/A`); preenchida em 3.280 dos 30.744 incidentes. | — | — | `issm-incidentes` |
| `Instalacao` | `Instalacao` | texto | Nome da instalação onde ocorreu o incidente (plataformas, sondas, embarcações, poços e unidades em terra, como `PETROBRAS 75 (P-75)`); 5.231 nomes distintos, sem padronização. | — | — | `issm-incidentes` |
| `Data_da_primeira_observacao` | `Data_da_primeira_observacao` | texto | Data em que o incidente foi observado pela primeira vez (DD-MM-AAAA, texto); a mais antiga é 31-12-2011, de incidente registrado depois. | — | — | `issm-incidentes` |
| `Hora_da_primeira_observacao` | `Hora_da_primeira_observacao` | texto | Hora em que o incidente foi observado pela primeira vez (HH:MM, texto). | — | — | `issm-incidentes` |
| `Latitude` | `Latitude` | texto | Latitude da instalação onde ocorreu o incidente, em graus decimais com ponto (texto, como `-24.150622222222218`); vale 0 em 1.027 incidentes (valor ausente na prática) e passa de 10 em 18, o que é incompatível com o Brasil. | — | — | `issm-incidentes` |
| `Longitude` | `Longitude` | texto | Longitude da instalação onde ocorreu o incidente, em graus decimais com ponto (texto); em 31 incidentes o valor é positivo (de até 44,8), provavelmente com o sinal perdido, e vale 0 em 1.027. | — | — | `issm-incidentes` |
| `Endereco` | `Endereco` | texto | Endereço da instalação onde ocorreu o incidente, em texto livre (bacia, campo, município ou descrição da área); vazio em 280 incidentes. | — | — | `issm-incidentes` |
| `Situacao_atual_descarga` | `Situacao_atual_descarga` | texto | Tipo de situação da descarga (nome do metadado); os valores observados indicam o andamento do registro no sistema, interpretação deduzida: `Fechada` (22.448), `Aprovada` (7.165), `Retificada aguardando aprovação` (1.061), `Aguardando ação` (41), `Ações concluídas aguardando aprovação` (26) e `Cadastrada aguardando aprovação` (3). | — | — | `issm-incidentes` |
| `Data_estimada_do_incidente` | `Data_estimada_do_incidente` | texto | Data estimada em que o incidente ocorreu (DD-MM-AAAA, texto); `01-01-1900` em 2.723 incidentes é valor de preenchimento (data desconhecida). | — | — | `issm-incidentes` |
| `Hora_do_incidente` | `Hora_do_incidente` | texto | Hora estimada em que o incidente ocorreu (HH:MM, texto); vazia em 2.724 incidentes. | — | — | `issm-incidentes` |
| `Numero_de_feridos_graves` | `Numero_de_feridos_graves` | texto | Quantidade de pessoas feridas de forma grave (inteiro em texto, de 0 a 7); 752 incidentes têm pelo menos um. | — | — | `issm-incidentes` |
| `Numero_Fatalidades` | `Numero_Fatalidades` | texto | Quantidade de fatalidades (inteiro em texto, de 0 a 9); 34 incidentes têm pelo menos uma (45 mortes no total). | — | — | `issm-incidentes` |
| `Breve_Descricao_Incidente` | `Breve_Descricao_Incidente` | texto | Breve descrição do que aconteceu no incidente, em texto livre, às vezes com quebras de linha e com notas como `NOTA: Este incidente já foi comunicado via e-mail`. | — | — | `issm-incidentes` |
| `Codigo` | `Codigo` | texto | Código referente à instalação, número inteiro em texto (2.518 valores distintos); vale 0 em 4.072 incidentes; só na tabela principal. | — | — | `issm-incidentes` |
| `Numero_IMO` | `Numero_IMO` | texto | Número IMO (Organização Marítima Internacional) referente à instalação, inteiro em texto; vazio em 11.629 incidentes e 0 em 5.231; só na tabela principal. | — | — | `issm-incidentes` |
| `Substancias` | `Substancias` | texto | Substância derramada ou vazada (36 valores, como `Óleo`, `Fluido hidráulico`, `Água Produzida fora de especificação`, `Gás natural`, `Óleo Diesel`); vazia em 25.253 das 31.534 linhas de `issm-substancias`; só nesse arquivo. | — | — | `issm-substancias` |
| `Volume` | `Volume` | texto | Volume da substância derramada ou vazada, texto com vírgula decimal (`0,0003`, `1428,`); o metadado não informa a unidade, e os valores vão de 0,0003 a 858.000; 30 valores têm formato irregular (`,045`, `1428,`, `1e-005`); só em `issm-substancias`. | — | — | `issm-substancias` |
| `Tipo_de_incidente` | `Tipo_de_incidente` | texto | Tipo do incidente (170 valores, a maioria com o prefixo `SSO - `, como `SSO - Parada emergencial de nível menor`, `SSO - Ferimento grave`, `SSO - Queda de objetos`); um incidente pode ter vários tipos; `Reclassificação` aparece em 2.280 linhas; só em `issm-tipo`. | — | — | `issm-tipo` |
| `DSC_GRAVIDADE_TIPO` | `DSC_GRAVIDADE_TIPO` | texto | Tipo de gravidade: `LEVE`, `MODERADO` ou `GRAVE` (vazio nas linhas de reclassificação, 2.335); só em `issm-tipo`. | — | — | `issm-tipo` |
| `DSC_QUASE_ACIDENTE_ACIDENTE` | `DSC_QUASE_ACIDENTE_ACIDENTE` | texto | Tipo de ocorrência: `Acidente` ou `Quase acidente` (vazio em 2.335 linhas); só em `issm-tipo`. | — | — | `issm-tipo` |

## No lake

- Dataset `anp/incidentes`, sem partição: um Parquet por arquivo, `issm-incidentes.parquet`, `issm-classificacao.parquet`, `issm-feridos.parquet`, `issm-substancias.parquet` e `issm-tipo.parquet`.
- Todas as colunas são texto. O conversor lê o texto em ISO-8859-1 sem corrupção (conferido: acentos corretos em `Classificacao_do_incidente` e `Tipo_de_incidente`) e mantém os nomes do cabeçalho (`Tipo_de_Ferimento_barra_Fatalidade`, `DSC_GRAVIDADE_TIPO`).

## Cuidados de uso

- **Cinco tabelas, não uma.** Empilhar os cinco Parquet com `union_by_name` mistura granularidades e deixa muitos nulos; leia cada arquivo e ligue por `Numero`. Ligar a tabela principal a `issm-classificacao` ou `issm-tipo` multiplica as linhas do incidente; agregue antes de juntar.
- **Linhas vazias nas tabelas secundárias.** `issm-feridos` tem uma linha por incidente mesmo sem ferido (30.242 vazias) e `issm-substancias` também (25.253 vazias); filtre `Tipo_de_Ferimento_barra_Fatalidade IS NOT NULL` e `Substancias IS NOT NULL` para contar eventos.
- **Datas e horas em texto e valores de preenchimento.** As datas são `DD-MM-AAAA`; `Data_estimada_do_incidente` vale `01-01-1900` em 2.723 incidentes e deve ser tratada como ausente; `Hora_do_incidente` está vazia em 2.724.
- **Coordenadas com defeitos.** `Latitude`/`Longitude` valem 0 em 1.027 incidentes, 31 longitudes são positivas (o Brasil tem longitude negativa) e 18 latitudes passam de 10 graus; valide a caixa geográfica antes de mapear.
- **`Volume` sem unidade.** O metadado não diz a unidade, e os valores vão de 0,0003 a 858.000; 30 valores têm formato irregular (`,045`, `1428,`, `1e-005`) e não convertem direto com `::DOUBLE` depois de trocar a vírgula. Não some volumes de substâncias diferentes sem saber a unidade.
- **Nomes não padronizados.** `Empresa` varia na razão social (`PETRÓLEO BRASILEIRO S.A.` e `... - PETROBRAS`; use `CNPJ` para agrupar); `Instalacao` tem 5.231 grafias; `Tipo_de_incidente` mistura `SSO - Reclassificação` e `Reclassificação`.
- **Mudança de divulgação em novembro de 2025.** Operadora e instalação são divulgadas logo após a notificação; incidentes recentes podem ter descrições e classificações ainda sem a investigação concluída e ser revistos nas atualizações semestrais.
- **Dados pessoais.** `Empresa` e `CNPJ` são de pessoas jurídicas, públicos; `Breve_Descricao_Incidente` é texto livre e, em ao menos cinco registros da amostra, cita nome de pessoa física (precedido de `Sr.`); trate o texto como potencialmente identificável. Números de inscrição de embarcações aparecem na descrição, mas não foram encontrados CPFs.
- **Chave.** `Numero` é único só na tabela principal; nas demais, repete por incidente. Por serem cinco tabelas, a chave do dataset fica vazia.

## Exemplos

Incidentes, feridos graves e fatalidades por ano de registro (o ano vem dos dois primeiros dígitos de `Numero`; 2013 começa em julho e 2026 vai até maio):

```python
import duckdb

duckdb.sql("""
    SELECT '20' || substr(Numero, 1, 2) AS ano,
           count(*) AS incidentes,
           sum(Numero_de_feridos_graves::INTEGER) AS feridos_graves,
           sum(Numero_Fatalidades::INTEGER) AS fatalidades
    FROM read_parquet('lake/anp/incidentes/issm-incidentes.parquet')
    GROUP BY 1
    ORDER BY 1
""").show()
```

## Referências

- Dados de incidentes de exploração e produção (ANP): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/incidentes-seguranca-operacional
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/issm/metadados-incidentes.pdf
- Sistema Integrado de Segurança Operacional (SISO): https://siso.anp.gov.br/; Manual de Comunicação de Incidentes e Resolução ANP nº 882/2022, citados na página da ANP.
