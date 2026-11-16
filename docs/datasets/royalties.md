---
dataset:
  id: royalties
  fonte: anp
  titulo: Participações governamentais — royalties, participação especial e preços de referência do petróleo e do gás natural
  resumo: Valores mensais dos royalties repassados à União, aos estados e aos municípios (de 2009), da participação especial por beneficiário e campo (trimestral, de 2006) e os preços de referência mensais do gás natural (de 2010) e do petróleo (de 2018) por campo.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/participacoes-governamentais
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'anual (metadado da ANP: cada arquivo de royalties e de preços cobre um ano; a participação especial é um arquivo por recorte, sem ano, com valores trimestrais; o metadado dá `Anual` para todas as tabelas)'
  cobertura:
    inicio: 2006-09
    fim: 2025-12
  unidade: 'depende da tabela: um mês de repasse de royalties (`royalties_uniao`, `royalties_estado`); um município em um mês (`royalties_municipio`); um beneficiário ou campo em um trimestre (`participacoes_especiais`); um campo em um mês (`preco_referencia_gn`, `preco_referencia_petroleo`)'
  granularidade:
    espacial: federal (União), estado (UF, em coluna por estado), município (nome e sigla da UF) e campo produtor; os preços de referência têm um preço por campo, e o petróleo, por corrente
    temporal: mês de competência (produção) e mês de caixa (repasse), em número de série de data do Excel, nos royalties e na participação especial (trimestral); mês de referência (`data`) nos preços; o ano do arquivo (`ano`) é o ano do caixa
  formato_bruto: 79 CSV em ASCII ou ISO-8859-1, separados por ponto e vírgula, com decimais em vírgula e datas como número de série do Excel; os arquivos de royalties têm linhas em branco no fim
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 53
  unidades_de_medida:
    competencia: data (número de série do Excel, primeiro dia do mês; texto)
    caixa: data (número de série do Excel, primeiro dia do mês; texto)
    data: data (número de série do Excel, primeiro dia do mês; texto)
    preco: R$/m³ (texto, vírgula decimal)
    preço: R$/m³ (texto, vírgula decimal)
    valor: R$ (reais; unidade deduzida; texto, vírgula decimal)
    acre: R$ (reais; texto, vírgula decimal)
    alagoas: R$ (reais; texto, vírgula decimal)
    amazonas: R$ (reais; texto, vírgula decimal)
    amapa: R$ (reais; texto, vírgula decimal)
    bahia: R$ (reais; texto, vírgula decimal)
    ceara: R$ (reais; texto, vírgula decimal)
    espirito santo: R$ (reais; texto, vírgula decimal)
    goias: R$ (reais; texto, vírgula decimal)
    maranhao: R$ (reais; texto, vírgula decimal)
    minas gerais: R$ (reais; texto, vírgula decimal)
    mato grosso do sul: R$ (reais; texto, vírgula decimal)
    mato grosso: R$ (reais; texto, vírgula decimal)
    para: R$ (reais; texto, vírgula decimal)
    paraiba: R$ (reais; texto, vírgula decimal)
    pernambuco: R$ (reais; texto, vírgula decimal)
    piaui: R$ (reais; texto, vírgula decimal)
    parana: R$ (reais; texto, vírgula decimal)
    rio de janeiro: R$ (reais; texto, vírgula decimal)
    rio grande do norte: R$ (reais; texto, vírgula decimal)
    rondonia: R$ (reais; texto, vírgula decimal)
    roraima: R$ (reais; texto, vírgula decimal)
    rio grande do sul: R$ (reais; texto, vírgula decimal)
    santa catarina: R$ (reais; texto, vírgula decimal)
    sergipe: R$ (reais; texto, vírgula decimal)
    sao paulo: R$ (reais; texto, vírgula decimal)
    tocantins: R$ (reais; texto, vírgula decimal)
    distrito federal: R$ (reais; texto, vírgula decimal)
    estados: R$ (reais; texto, vírgula decimal)
    municipios: R$ (reais; texto, vírgula decimal)
    fundo especial: R$ (reais; texto, vírgula decimal)
    comando da marinha: R$ (reais; texto, vírgula decimal)
    mct: R$ (reais; texto, vírgula decimal)
    fundo social: R$ (reais; texto, vírgula decimal)
    educacao e saude: R$ (reais; texto, vírgula decimal)
    royalties minimos: R$ (reais; texto, vírgula decimal)
    royalties excedentes: R$ (reais; texto, vírgula decimal)
  dados_pessoais: nenhum
  eras:
  - desde: '2009'
    mudanca: royalties por ente, por estado e por município de 2009 em diante (competência de 2008-11 em diante); preços de referência do gás natural de 2010 e do petróleo de 2018; participação especial desde a competência de 2006-09
  - desde: '2012'
    mudanca: '`royalties_uniao` passa de 12 a 15 linhas por ano (3 em branco no fim) e o repasse ao Fundo Social começa em 2012-01 (`educacao e saude` só em 2013-10)'
  - desde: '2016'
    mudanca: o arquivo de estados de 2016 inclui a coluna `distrito federal` e ordem diferente de colunas; o arquivo de preços de gás de 2016 traz um mês com data errada (2018-09 no lugar de 2016-09)
  - desde: '2019'
    mudanca: o arquivo de municípios de 2019 tem duas colunas a mais (`coluna_8` e `coluna_9`, com uma linha de verificação e `#REF!`) e 742 valores `-`; o de estados tem 24 linhas em branco no fim
  - desde: '2021'
    mudanca: o preço do petróleo troca a coluna `preco` por `preço` (acentuada) e os nomes de campo passam a vir com iniciais maiúsculas e acento em todas as linhas (em parte das de 2019 e 2020); o arquivo de 2020 tem espaços no fim do nome de `campo`
  - desde: '2022'
    mudanca: 'os nomes de município passam a vir com o sufixo da UF (`anadia-al`): 10 linhas em 2022, 12 em 2023 e 2024 e todas as de 2025'
  - desde: '2024'
    mudanca: os preços de referência (gás e petróleo) trocam `contrato` por `código do campo`; o do petróleo ganha `coluna_7` com notas de rodapé
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Participações governamentais — royalties, participação especial e preços de referência do petróleo e do gás natural

## Resumo

As participações governamentais são compensações financeiras devidas pelas empresas outorgadas do direito de exploração e produção de petróleo e gás natural no território brasileiro. A ANP calcula os valores a distribuir a estados e municípios beneficiários, conforme as Leis nº 9.478/1997 e nº 7.990/1989, regulamentadas pelos Decretos nº 2.705/1998 e nº 1/1991. Este grupo reúne seis tabelas de dados abertos: a distribuição dos royalties por tipo de ente (`royalties_uniao`), por estado (`royalties_estado`) e por município (`royalties_municipio`), em um arquivo por ano; a participação especial por União, estado, município e campo (`participacoes_especiais`, quatro arquivos sem ano); e os preços de referência mensais do gás natural (`preco_referencia_gn`) e do petróleo (`preco_referencia_petroleo`) por campo, que servem de base ao cálculo. A página da ANP também publica o preço mínimo do petróleo (até 2017), que o fetcher não coleta.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/royalties` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/participacoes-governamentais |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual (metadado da ANP: cada arquivo de royalties e de preços cobre um ano; a participação especial é um arquivo por recorte, sem ano, com valores trimestrais; o metadado dá `Anual` para todas as tabelas) |
| Cobertura | 2006-09 a 2025-12 |
| Unidade (uma linha) | depende da tabela: um mês de repasse de royalties (`royalties_uniao`, `royalties_estado`); um município em um mês (`royalties_municipio`); um beneficiário ou campo em um trimestre (`participacoes_especiais`); um campo em um mês (`preco_referencia_gn`, `preco_referencia_petroleo`) |
| Granularidade | espacial: federal (União), estado (UF, em coluna por estado), município (nome e sigla da UF) e campo produtor; os preços de referência têm um preço por campo, e o petróleo, por corrente; temporal: mês de competência (produção) e mês de caixa (repasse), em número de série de data do Excel, nos royalties e na participação especial (trimestral); mês de referência (`data`) nos preços; o ano do arquivo (`ano`) é o ano do caixa |
| Formato bruto | 79 CSV em ASCII ou ISO-8859-1, separados por ponto e vírgula, com decimais em vírgula e datas como número de série do Excel; os arquivos de royalties têm linhas em branco no fim |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 53 |
| Unidades de medida | `competencia`: data (número de série do Excel, primeiro dia do mês; texto); `caixa`: data (número de série do Excel, primeiro dia do mês; texto); `data`: data (número de série do Excel, primeiro dia do mês; texto); `preco`: R$/m³ (texto, vírgula decimal); `preço`: R$/m³ (texto, vírgula decimal); `valor`: R$ (reais; unidade deduzida; texto, vírgula decimal); `acre`: R$ (reais; texto, vírgula decimal); `alagoas`: R$ (reais; texto, vírgula decimal); `amazonas`: R$ (reais; texto, vírgula decimal); `amapa`: R$ (reais; texto, vírgula decimal); `bahia`: R$ (reais; texto, vírgula decimal); `ceara`: R$ (reais; texto, vírgula decimal); `espirito santo`: R$ (reais; texto, vírgula decimal); `goias`: R$ (reais; texto, vírgula decimal); `maranhao`: R$ (reais; texto, vírgula decimal); `minas gerais`: R$ (reais; texto, vírgula decimal); `mato grosso do sul`: R$ (reais; texto, vírgula decimal); `mato grosso`: R$ (reais; texto, vírgula decimal); `para`: R$ (reais; texto, vírgula decimal); `paraiba`: R$ (reais; texto, vírgula decimal); `pernambuco`: R$ (reais; texto, vírgula decimal); `piaui`: R$ (reais; texto, vírgula decimal); `parana`: R$ (reais; texto, vírgula decimal); `rio de janeiro`: R$ (reais; texto, vírgula decimal); `rio grande do norte`: R$ (reais; texto, vírgula decimal); `rondonia`: R$ (reais; texto, vírgula decimal); `roraima`: R$ (reais; texto, vírgula decimal); `rio grande do sul`: R$ (reais; texto, vírgula decimal); `santa catarina`: R$ (reais; texto, vírgula decimal); `sergipe`: R$ (reais; texto, vírgula decimal); `sao paulo`: R$ (reais; texto, vírgula decimal); `tocantins`: R$ (reais; texto, vírgula decimal); `distrito federal`: R$ (reais; texto, vírgula decimal); `estados`: R$ (reais; texto, vírgula decimal); `municipios`: R$ (reais; texto, vírgula decimal); `fundo especial`: R$ (reais; texto, vírgula decimal); `comando da marinha`: R$ (reais; texto, vírgula decimal); `mct`: R$ (reais; texto, vírgula decimal); `fundo social`: R$ (reais; texto, vírgula decimal); `educacao e saude`: R$ (reais; texto, vírgula decimal); `royalties minimos`: R$ (reais; texto, vírgula decimal); `royalties excedentes`: R$ (reais; texto, vírgula decimal) |
| Dados pessoais | nenhum |
| Eras | 2009: royalties por ente, por estado e por município de 2009 em diante (competência de 2008-11 em diante); preços de referência do gás natural de 2010 e do petróleo de 2018; participação especial desde a competência de 2006-09; 2012: `royalties_uniao` passa de 12 a 15 linhas por ano (3 em branco no fim) e o repasse ao Fundo Social começa em 2012-01 (`educacao e saude` só em 2013-10); 2016: o arquivo de estados de 2016 inclui a coluna `distrito federal` e ordem diferente de colunas; o arquivo de preços de gás de 2016 traz um mês com data errada (2018-09 no lugar de 2016-09); 2019: o arquivo de municípios de 2019 tem duas colunas a mais (`coluna_8` e `coluna_9`, com uma linha de verificação e `#REF!`) e 742 valores `-`; o de estados tem 24 linhas em branco no fim; 2021: o preço do petróleo troca a coluna `preco` por `preço` (acentuada) e os nomes de campo passam a vir com iniciais maiúsculas e acento em todas as linhas (em parte das de 2019 e 2020); o arquivo de 2020 tem espaços no fim do nome de `campo`; 2022: os nomes de município passam a vir com o sufixo da UF (`anadia-al`): 10 linhas em 2022, 12 em 2023 e 2024 e todas as de 2025; 2024: os preços de referência (gás e petróleo) trocam `contrato` por `código do campo`; o do petróleo ganha `coluna_7` com notas de rodapé |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- 79 arquivos CSV na página de participações governamentais da ANP (dados abertos), em `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pg/`: royalties da União (`royalties-uniao/`), dos estados (`royalties-estados/`) e dos municípios (`royalties-municipios/`), um por ano de 2009 a 2025 (17 por tabela); participação especial (`participacao-especial/pe_uniao.csv`, `pe_estado.csv`, `pe_municipio.csv` e `pe_campo.csv`); preço de referência do gás natural de 2010 a 2025 (16) e do petróleo de 2018 a 2025 (8). Tamanhos conferidos na coleta de 2026-11-15: de 1.011 bytes (royalties da União, 2009) a 509.310 (royalties dos municípios, 2019).
- Fonte do dado, segundo o metadado `metadados.docx` da página (e a mesma pasta): ANP/SPG (Superintendência de Participações Governamentais), a partir das tabelas de royalties e participações especiais publicadas na página de assuntos de royalties; contato secretaria_spg@anp.gov.br. Os royalties são recolhidos mensalmente, até o último dia do mês seguinte à produção (página oficial); a participação especial é apurada trimestralmente por campo.
- A página oficial (atualizada em 22/05/2026) lista os arquivos de royalties e de preços até 2025 e a participação especial em quatro arquivos únicos; as páginas de assuntos de royalties (royalties, participação especial, preço de referência do petróleo e do gás natural), atualizadas em outubro e novembro de 2026, trazem os meses de 2026, que o catálogo do fetcher ainda não tem.
- A página oficial também lista o preço mínimo do petróleo (de 2009 a 2017), descontinuado pela Resolução ANP nº 703/2017; o catálogo do fetcher não o inclui.
- O servidor não informa a data de modificação dos arquivos; o sufixo `@AAAAMMDD` do bruto é a data da coleta (2026-11-15). A participação especial é um arquivo por recorte, substituído a cada atualização.

## Conteúdo

| Tabela (dataset fino) | Arquivos | Linhas na amostra | Colunas | Observação |
|---|---|---|---|---|
| `royalties_uniao` | 17 (2009 a 2025) | 246 (204 com dados) | 9 | um mês de caixa por linha, em colunas por tipo de ente (estados, municípios, fundo especial, Comando da Marinha, MCT, Fundo Social, educação e saúde) |
| `royalties_estado` | 17 | 241 (204 com dados) | 28 (29 em 2016) | um mês por linha, com uma coluna por UF; só 11 UFs têm valores diferentes de zero |
| `royalties_municipio` | 17 | 186.501 | 6 (8 em 2019) | um município em um mês; 10.406 a 11.844 linhas por ano |
| `participacoes_especiais` | 4 (sem ano) | 3.912 (197 União, 417 estados, 2.002 municípios, 1.296 campos) | 8 no conjunto (5 a 6 por recorte) | coluna `recorte` (criada pelo conversor) identifica a tabela de origem; 73 trimestres, de 2006-09 a 2024-09 (caixa 2006-11 a 2024-11) |
| `preco_referencia_gn` | 16 (2010 a 2025) | 72.803 | 4 (5 no conjunto) | um campo em um mês, em R$/m³; 3.712 a 5.119 linhas por ano |
| `preco_referencia_petroleo` | 8 (2018 a 2025) | 38.694 | 5 a 6 | um campo e uma corrente em um mês, em R$/m³; 4.550 a 5.117 linhas por ano |

- **Ordens de grandeza (soma dos arquivos de royalties de cada ano de caixa):** a distribuição total por ente passa de R$ 7,96 bilhões em 2009 para R$ 62,16 bilhões em 2025; os estados recebem R$ 2,4 bilhões em 2009 e R$ 16,6 bilhões em 2025 (a soma das 27 colunas de `royalties_estado` coincide com `estados` de `royalties_uniao`), e os municípios, R$ 2,7 bilhões e R$ 20,9 bilhões (a soma por município fica de 98% a 100% da coluna `municipios`).
- **Participação especial (soma de todos os trimestres):** recortes `campo` R$ 390,8 bilhões (maior: Tupi, R$ 151,5 bilhões), `uniao` R$ 193,0 bilhões (fundo social, R$ 128,3 bilhões; Ministério de Minas e Energia, R$ 52,1 bilhões; Ministério do Meio Ambiente, R$ 12,6 bilhões), `estado` R$ 156,3 bilhões e `municipio` R$ 38,9 bilhões; a soma da União, dos estados e dos municípios (R$ 388,3 bilhões) é próxima à dos campos. A unidade (reais) é deduzida.
- **Preços:** o preço de referência do gás vai de R$ 0,45 a R$ 3,85 por m³ em 2025 (R$ 0 a 5,31 em todo o lake); o do petróleo vai de centenas de R$/m³ (2018) a milhares (2025), por campo e corrente.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2009 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6) |
| 2010 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2011 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2012 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2013 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2014 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2015 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2016 | `royalties_uniao` (9); `royalties_estado` (29); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2017 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4) |
| 2018 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4); `preco_referencia_petroleo` (5) |
| 2019 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (8); `preco_referencia_gn` (4); `preco_referencia_petroleo` (5) |
| 2020 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4); `preco_referencia_petroleo` (5) |
| 2021 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4); `preco_referencia_petroleo` (5) |
| 2022 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4); `preco_referencia_petroleo` (5) |
| 2023 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4); `preco_referencia_petroleo` (5) |
| 2024 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4); `preco_referencia_petroleo` (6) |
| 2025 | `royalties_uniao` (9); `royalties_estado` (28); `royalties_municipio` (6); `preco_referencia_gn` (4); `preco_referencia_petroleo` (6) |

## Variáveis

As descrições vêm do metadado da ANP (`metadados.docx`, uma ficha por tabela); as unidades dos preços (R$/m³) vêm da página oficial do preço de referência do petróleo e do gás natural, e as dos royalties (R$), da página de royalties da ANP. Os contadores vêm do lake de todos os 79 arquivos convertidos (2026-11-15), mais amplo que a amostra padrão deste lote. O metadado dá datas e valores como `Data em formato 'Geral'` e `Número em formato 'Geral'`, mas o lake os guarda como texto.
Os nomes de coluna seguem os arquivos da fonte (minúsculas, sem acento nos royalties; com acento em parte dos preços). A coluna *Arquivos* diz em quais tabelas cada coluna aparece (`ano` é partição, exceto em `participacoes_especiais`); *Período* mostra o intervalo de anos em que a coluna existe.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `competencia` | `competencia` | texto | Mês da produção de óleo e gás que gerou os valores repassados, como número de série de data do Excel (primeiro dia do mês; `39753` é 2008-11-01), em texto; vazia nas linhas em branco do fim de alguns arquivos. Em `participacoes_especiais`, os valores são de setembro, dezembro, março e junho, o que indica o último mês do trimestre apurado (dedução). | — | todo | `participacoes_especiais`, `royalties_estado`, `royalties_municipio` e mais 1 |
| `caixa` | `caixa` | texto | Mês do efetivo repasse (royalties) ou do recolhimento (participação especial), como número de série de data do Excel (primeiro dia do mês); é dois meses depois da `competencia` e dá o ano do arquivo (`ano`) nos royalties. | — | todo | `participacoes_especiais`, `royalties_estado`, `royalties_municipio` e mais 1 |
| `estados` | `estados` | texto | Valor dos royalties repassado aos Estados brasileiros, em reais; só em `royalties_uniao`. | — | todo | `royalties_uniao` |
| `municipios` | `municipios` | texto | Valor dos royalties repassado aos Municípios brasileiros, em reais; só em `royalties_uniao`; a soma por município (`royalties_municipio`) é de 98% a 100% desse valor. | — | todo | `royalties_uniao` |
| `fundo especial` | `fundo especial` | texto | Valor dos royalties repassado ao Fundo Especial, em reais; só em `royalties_uniao`. | — | todo | `royalties_uniao` |
| `comando da marinha` | `comando da marinha` | texto | Valor dos royalties repassado ao Comando da Marinha, em reais; só em `royalties_uniao`. | — | todo | `royalties_uniao` |
| `mct` | `mct` | texto | Valor dos royalties repassado ao Ministério da Ciência, Tecnologia e Inovações (MCT), em reais; só em `royalties_uniao`. | — | todo | `royalties_uniao` |
| `fundo social` | `fundo social` | texto | Valor dos royalties repassado ao Fundo Social, em reais; vale 0 até a competência de 2011-12 (primeiro valor positivo em 2012-01); só em `royalties_uniao`. | — | todo | `royalties_uniao` |
| `educacao e saude` | `educacao e saude` | texto | Valor repassado à União com destinação à Educação e Saúde, em reais; vale 0 até a competência de 2013-09 (primeiro valor positivo em 2013-10); só em `royalties_uniao`. | — | todo | `royalties_uniao` |
| `acre` | `acre` | texto | Valor dos royalties repassado ao Estado do Acre, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `alagoas` | `alagoas` | texto | Valor dos royalties repassado ao Estado de Alagoas, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `amazonas` | `amazonas` | texto | Valor dos royalties repassado ao Estado do Amazonas, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `amapa` | `amapa` | texto | Valor dos royalties repassado ao Estado do Amapá, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `bahia` | `bahia` | texto | Valor dos royalties repassado ao Estado da Bahia, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `ceara` | `ceara` | texto | Valor dos royalties repassado ao Estado do Ceará, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `espirito santo` | `espirito santo` | texto | Valor dos royalties repassado ao Estado do Espírito Santo, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `goias` | `goias` | texto | Valor dos royalties repassado ao Estado de Goiás, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `maranhao` | `maranhao` | texto | Valor dos royalties repassado ao Estado do Maranhão, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `minas gerais` | `minas gerais` | texto | Valor dos royalties repassado ao Estado de Minas Gerais, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `mato grosso do sul` | `mato grosso do sul` | texto | Valor dos royalties repassado ao Estado de Mato Grosso do Sul, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `mato grosso` | `mato grosso` | texto | Valor dos royalties repassado ao Estado de Mato Grosso, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `para` | `para` | texto | Valor dos royalties repassado ao Estado do Pará, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `paraiba` | `paraiba` | texto | Valor dos royalties repassado ao Estado da Paraíba, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `pernambuco` | `pernambuco` | texto | Valor dos royalties repassado ao Estado de Pernambuco, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `piaui` | `piaui` | texto | Valor dos royalties repassado ao Estado do Piauí, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `parana` | `parana` | texto | Valor dos royalties repassado ao Estado do Paraná, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `rio de janeiro` | `rio de janeiro` | texto | Valor dos royalties repassado ao Estado do Rio de Janeiro, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `rio grande do norte` | `rio grande do norte` | texto | Valor dos royalties repassado ao Estado do Rio Grande do Norte, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `rondonia` | `rondonia` | texto | Valor dos royalties repassado ao Estado de Rondônia, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `roraima` | `roraima` | texto | Valor dos royalties repassado ao Estado de Roraima, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `rio grande do sul` | `rio grande do sul` | texto | Valor dos royalties repassado ao Estado do Rio Grande do Sul, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `santa catarina` | `santa catarina` | texto | Valor dos royalties repassado ao Estado de Santa Catarina, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `sergipe` | `sergipe` | texto | Valor dos royalties repassado ao Estado de Sergipe, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `sao paulo` | `sao paulo` | texto | Valor dos royalties repassado ao Estado de São Paulo, em reais, texto com vírgula decimal; só em `royalties_estado`. Tem valor diferente de zero em algum mês. | — | todo | `royalties_estado` |
| `tocantins` | `tocantins` | texto | Valor dos royalties repassado ao Estado de Tocantins, em reais, texto com vírgula decimal; só em `royalties_estado`. Vale 0 em todos os meses (estado sem produção nem confrontação). | — | todo | `royalties_estado` |
| `distrito federal` | `distrito federal` | texto | Valor dos royalties repassado ao Distrito Federal, em reais; só existe no arquivo de 2016 (12 linhas, todas 0); só em `royalties_estado`. | — | 2016 | `royalties_estado` |
| `municipio` | `municipio` | texto | Município beneficiário do repasse, em minúsculas e sem acentos (`barra de santo antonio`); em `royalties_municipio`, de 2022 a 2025 vem às vezes com o sufixo da UF (`anadia-al`; 10 linhas em 2022, 12 em 2023 e 2024 e todas em 2025); em `participacoes_especiais`, só no recorte `municipio` (62 municípios). | — | todo | `participacoes_especiais`, `royalties_municipio` |
| `estado` | `estado` | texto | Estado do município ou beneficiário: em `royalties_municipio`, a sigla da UF em minúsculas (`al`; 20 UFs); em `participacoes_especiais`, o nome do estado em minúsculas e sem acentos (`alagoas`; 9 estados), nos recortes `estado` e `municipio`. | — | todo | `participacoes_especiais`, `royalties_municipio` |
| `royalties minimos` | `royalties minimos` | texto | Valores repassados referentes à Lei nº 7.990/89 (parcela de 5%), em reais, texto com vírgula decimal; `-` em 54 linhas de 2019 e 1 valor negativo; só em `royalties_municipio`. | — | todo | `royalties_municipio` |
| `royalties excedentes` | `royalties excedentes` | texto | Valores repassados referentes à Lei nº 9.478/97 (parcela acima de 5%), em reais, texto com vírgula decimal; `-` em 688 linhas, todas de 2019, e 1 valor negativo; só em `royalties_municipio`. | — | todo | `royalties_municipio` |
| `coluna_8` | `coluna_8` | texto | Coluna sem nome do arquivo de municípios de 2019, com um único valor (`108.086,76`, a soma de `royalties minimos` e `royalties excedentes` da linha de `abreu e lima`, `pe`); vazia no resto; só em `royalties_municipio`. | — | 2019 | `royalties_municipio` |
| `coluna_9` | `coluna_9` | texto | Coluna sem nome do arquivo de municípios de 2019, com um único valor (`#REF!`, erro de planilha); vazia no resto; só em `royalties_municipio`. | — | 2019 | `royalties_municipio` |
| `campo` | `campo` | texto | Nome do campo produtor. Em `participacoes_especiais` (recorte `campo`), o campo pagador de participação especial (48 campos, como `tupi`, `lula`, `roncador`); em `preco_referencia_gn` e `preco_referencia_petroleo`, o nome do campo produtor, com grafia que muda entre os anos: minúsculas sem acento até 2018 (`abalone`), com acento em parte das linhas de 2019, e com iniciais maiúsculas e acento em parte das linhas de 2020 e em todas as de 2021 em diante (`Abalone`). No arquivo de 2020 do preço do petróleo o nome desta coluna tem espaços no fim, que o lake mantém e esta documentação remove. | — | 2010 a 2025 | `participacoes_especiais`, `preco_referencia_gn`, `preco_referencia_petroleo` |
| `valor` | `valor` | texto | Valor da participação especial repassado ou recolhido, em reais (unidade deduzida: o metadado não a informa), texto com vírgula decimal; 8 valores negativos no recorte `campo`; só em `participacoes_especiais`. | — | — | `participacoes_especiais` |
| `recorte` | `recorte` | texto | Recorte da tabela de origem, criado pelo conversor (não existe na fonte): `uniao`, `estado`, `municipio` ou `campo`, conforme o arquivo (`pe_uniao.csv`, `pe_estado.csv`, `pe_municipio.csv` e `pe_campo.csv`); só em `participacoes_especiais`. | — | — | `participacoes_especiais` |
| `conta` | `conta` | texto | Órgão ou ente da União beneficiário do repasse da participação especial: `ministerio de minas e energia` (73 linhas), `ministerio do meio ambiente` (72) ou `fundo social` (52); só em `participacoes_especiais` (recorte `uniao`). | — | — | `participacoes_especiais` |
| `data` | `data` | texto | Mês de referência do preço, como número de série de data do Excel (primeiro dia do mês, de 2010-01 a 2025-12 no gás e de 2018-01 a 2025-12 no petróleo); o metadado diz "mês da publicação do preço"; em `preco_referencia_*`. O arquivo de gás de 2016 traz `43344` (2018-09-01) onde se esperaria `42614` (2016-09-01). | — | 2010 a 2025 | `preco_referencia_gn`, `preco_referencia_petroleo` |
| `contrato` | `contrato` | texto | Número do contrato de concessão do campo (texto, em formatos variados: `48000003552/97-11`, `48610.003901/2000`, `Área Não Contratada`, `Autorização ANP 102/2000` e `#N/D` no petróleo); só de 2010 a 2023 (nos arquivos de 2024 e 2025 foi substituído por `código do campo`); em `preco_referencia_*`. | — | 2010 a 2023 | `preco_referencia_gn`, `preco_referencia_petroleo` |
| `preco` | `preco` | texto | Preço de referência, em reais por metro cúbico (R$/m³), texto com vírgula decimal: no gás natural (PRGN, 0 a 5,31 no lake) e no petróleo (PRP) nos arquivos de 2018 a 2020 (o PRP vai de centenas a milhares de R$/m³; `#REF!` em 1 linha de 2018); em `preco_referencia_*`. | — | 2010 a 2025 | `preco_referencia_gn`, `preco_referencia_petroleo` |
| `código do campo` | `código do campo` | texto | Código do campo produtor (número em texto, como `823`; `SIX` em 4 linhas do petróleo), que substitui o número do contrato nos arquivos de 2024 e 2025; em `preco_referencia_*`. | — | 2024 a 2025 | `preco_referencia_gn`, `preco_referencia_petroleo` |
| `corrente` | `corrente` | texto | Nome da corrente de petróleo à qual o preço se refere (`ostra`, `lagoa do paulo norte`, `rgn mistura`, 281 valores); em muitas linhas vem `-1` ou `-2` no lugar do nome (531 de 4.836 linhas em 2018 e 1.630 de 4.550 em 2025), indicador da nota de rodapé sobre a forma de fixação do preço (notas em `coluna_7` de 2024 e 2025: `-1`, preços estabelecidos conforme os arts. 5º e 8º da Resolução ANP nº 874/2022; `-2`, art. 12 da mesma resolução); só em `preco_referencia_petroleo`. | — | 2018 a 2025 | `preco_referencia_petroleo` |
| `preço` | `preço` | texto | Preço de referência do petróleo (PRP), em R$/m³, texto com vírgula decimal; é `preco` com acento nos arquivos de 2021 a 2025 (o de 2021 tem 13 linhas `#N/D`); só em `preco_referencia_petroleo`. | — | 2021 a 2025 | `preco_referencia_petroleo` |
| `coluna_7` | `coluna_7` | texto | Coluna sem nome do arquivo de 2024 e 2025 do preço do petróleo, que traz só as notas de rodapé nas 2 primeiras linhas (`-1: preços estabelecidos nos termos dos arts. 5° e 8° da Resolução ANP n° 874/2022.` e `-2: preço estabelecido nos termos do art. 12 da Resolução ANP n° 874/2022.`); só em `preco_referencia_petroleo`. | — | 2024 a 2025 | `preco_referencia_petroleo` |

## No lake

- Dataset `anp/royalties`, composto por seis datasets finos no lake: `royalties_uniao`, `royalties_estado`, `royalties_municipio`, `preco_referencia_gn` e `preco_referencia_petroleo`, particionados por `ano` (ano do arquivo, que é o ano do caixa nos royalties e o do `data` nos preços), e `participacoes_especiais`, sem partição, com os quatro recortes no mesmo Parquet.
- Todas as colunas são texto. O conversor mantém os nomes do cabeçalho (minúsculas, com espaços em nomes como `fundo especial` e `código do campo`), descarta colunas vazias em parte dos arquivos e cria `coluna_N` para colunas sem nome com algum valor; as linhas em branco do fim dos CSV de royalties viram linhas todas nulas.
- A coluna `recorte` de `participacoes_especiais` não existe na fonte: o conversor a cria a partir do nome do arquivo.

## Cuidados de uso

- **Datas são números de série do Excel em texto.** `competencia`, `caixa` e `data` valem, por exemplo, `39753`; converta com `DATE '1899-12-30' + coluna::INTEGER`. A `competencia` é o mês da produção, e o `caixa`, dois meses depois (o do repasse); `ano` é o ano do caixa, não o da competência.
- **Linhas em branco viram linhas nulas.** `royalties_uniao` tem 3 linhas nulas por arquivo desde 2012, `royalties_estado` tem 24 em 2019 e 13 em 2025; filtre `competencia IS NOT NULL` antes de contar ou somar.
- **Valores em reais, como texto.** Troque a vírgula decimal por ponto e converta (`replace(col, ',', '.')::DOUBLE`); `royalties_municipio` tem `-` como valor em 742 linhas de 2019 (54 em `royalties minimos` e 688 em `royalties excedentes`), a tratar como 0 ou ausente. Há valores negativos (2 em royalties de municípios, 1 por coluna; 8 em participação especial por campo).
- **Colunas que mudam entre os anos.** Preço do petróleo: `preco` (2018 a 2020) e `preço` (2021 a 2025); `contrato` até 2023 e `código do campo` em 2024 e 2025; `coluna_7` em 2024 e 2025 só traz notas. Estado: o arquivo de 2016 tem `distrito federal` e ordem diferente. Empilhe com `union_by_name` e junte as duas colunas de preço com `coalesce`.
- **Nomes de município e de campo não são padronizados.** Município: o sufixo da UF (`anadia-al`) aparece de 2022 a 2025 (todas as linhas de 2025); remova `-[a-z]{2}$` antes de ligar entre anos. Há 12 pares de linhas duplicadas por mês para `embu`/`sp` em 2018 (possivelmente dois municípios homônimos abreviados). Campo: minúsculas sem acento até 2018, com acento em parte das linhas de 2019, com iniciais maiúsculas em parte das de 2020 e em todas de 2021 em diante; compare nomes com `lower()` e remoção de acentos.
- **`corrente` com `-1` e `-2`.** Em parte das linhas de petróleo, a coluna traz esses códigos no lugar do nome da corrente, e o preço foi fixado por regra (Resolução ANP nº 874/2022, arts. 5º, 8º e 12); não os trate como nomes.
- **Valores de erro de planilha.** `#REF!` (1 linha de petróleo de 2018 e 1 de municípios de 2019), `#N/D` (13 linhas de 2021 no preço do petróleo, mais `contrato` e `corrente` em alguns campos) e `Área Não Contratada` em `contrato`; descarte antes de converter.
- **Mês errado.** O arquivo de gás natural de 2016 tem um mês com `data` `43344` (2018-09) no lugar de `42614` (2016-09); corrija ou descarte.
- **Participação especial não é mensal e é só até 2024.** Os quatro arquivos cobrem 73 trimestres (competência de 2006-09 a 2024-09, caixa de 2006-11 a 2024-11), não há recorte de 2025 na coleta de 2026-11-15.
- **Chave.** Em `royalties_municipio`, (`caixa`, `municipio`, `estado`) repete em 12 casos; por serem seis tabelas, a chave do dataset fica vazia.
- **Dados pessoais.** Não há; só valores por ente federativo, município, campo e corrente.

## Exemplos

Municípios que mais receberam royalties em 2024 (soma de `royalties minimos` e `royalties excedentes`; as datas de `caixa` estão em 2024):

```python
import duckdb

duckdb.sql("""
    SELECT municipio, estado,
           round(sum(coalesce(nullif(replace("royalties minimos", ',', '.'), '-')::DOUBLE, 0)
                   + coalesce(nullif(replace("royalties excedentes", ',', '.'), '-')::DOUBLE, 0)) / 1e6, 1) AS milhoes_reais
    FROM read_parquet('lake/anp/royalties_municipio/ano=2024/*.parquet')
    GROUP BY 1, 2
    ORDER BY milhoes_reais DESC
    LIMIT 8
""").show()
```

Preço de referência do petróleo do campo de Tupi nos primeiros meses de 2025 (a data é número de série do Excel, e o nome do campo tem iniciais maiúsculas nos arquivos de 2024 e 2025):

```python
import duckdb

duckdb.sql("""
    SELECT DATE '1899-12-30' + data::INTEGER AS mes, campo, corrente,
           replace("preço", ',', '.')::DOUBLE AS reais_por_m3
    FROM read_parquet('lake/anp/preco_referencia_petroleo/ano=2025/*.parquet')
    WHERE campo = 'Tupi'
    ORDER BY 1
    LIMIT 6
""").show()
```

## Referências

- Participações governamentais (dados abertos): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/participacoes-governamentais
- Metadados (.docx): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/pg/metadados.docx
- Royalties, participação especial e preços de referência (ANP): https://www.gov.br/anp/pt-br/assuntos/royalties-e-outras-participacoes/royalties, https://www.gov.br/anp/pt-br/assuntos/royalties-e-outras-participacoes/participacao-especial, https://www.gov.br/anp/pt-br/assuntos/royalties-e-outras-participacoes/preco-de-referencia-do-petroleo e https://www.gov.br/anp/pt-br/assuntos/royalties-e-outras-participacoes/preco-de-referencia-do-gas-natural
