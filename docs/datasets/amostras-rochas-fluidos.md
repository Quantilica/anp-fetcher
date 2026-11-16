---
dataset:
  id: amostras-rochas-fluidos
  fonte: anp
  titulo: 'Amostras de rochas e fluidos: acervo e valores das depositárias'
  resumo: Consolidação anual das amostras de rochas e fluidos declaradas pelas depositárias (calha, testemunhos, plugues, laterais, lâminas e fluidos) e os valores que elas cobram pelo acesso.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/amostras-de-rochas-e-fluidos
  licenca: Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: 'anual (metadados da ANP): a consolidação do acervo e os valores das depositárias'
  cobertura:
    inicio: '2015'
    fim: '2026'
  unidade: uma caixa, um intervalo ou uma amostra declarada por uma depositária (conforme o tipo), ou uma linha de serviço com valor numa tabela de depositária
  granularidade:
    espacial: poço e bacia sedimentar; município e estado do depósito (não do poço)
    temporal: ano da consolidação (`ano`) e, nas DAAs de 2015 e 2016, o ano da declaração; data de conclusão do poço dentro da tabela
  formato_bruto: ZIPs anuais com um CSV por tipo de amostra (consolidação) e um CSV por depositária (valores); CSV soltos para as DAAs de 2015 e 2016; separador ponto e vírgula
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 70
  unidades_de_medida:
    Profundidade topo (m): m (metros)
    Profundidade base (m): m (metros)
    Profundidade da lâmina (m): m (metros)
    Profundidadedalâmina(m): m (metros)
    Profundidade (m): m (metros)
    Profundidade do plugue (m): m (metros)
    Profundidade bas (m): m (metros)
    Volume (L): L (litros)
    VALOR (R$): R$ (reais; em dólares na coluna `VALOR (USD)`)
    VALOR 2018 (R$): R$ (reais; em dólares na coluna `VALOR (USD)`)
    VALOR (R$)_2: R$ (reais; em dólares na coluna `VALOR (USD)`)
    VALOR 2020 (R$): R$ (reais; em dólares na coluna `VALOR (USD)`)
    VALOR: R$ (reais; em dólares na coluna `VALOR (USD)`)
    Valores unitários (R$): R$ (reais; em dólares na coluna `VALOR (USD)`)
    VALOR (USD): R$ (reais; em dólares na coluna `VALOR (USD)`)
    Valor unitário (R$): R$ (reais; em dólares na coluna `VALOR (USD)`)
    Valor unitário (R$) incl. impostos: R$ (reais; em dólares na coluna `VALOR (USD)`)
  dados_pessoais: nenhum
  eras:
  - desde: '2017'
    mudanca: 'consolidação 2017: cabeçalhos de calha, lâminas, laterais e testemunhos sem espaços (`Nomedopoço(ANP)`, `Baciasedimentar`); sem `Identificador da caixa` (calha, laterais e plugues) e sem `Tipo de container` (fluidos)'
  - desde: '2018'
    mudanca: entram `Identificador da caixa` e `Tipo de container`; cabeçalhos com espaços
  - desde: '2021'
    mudanca: '`Município/Estado` passa a vir antes de `Depositária`; `Tipo de fluido` e `Quantidade de amostra` (singular) substituem `Tipo fluido` e `Quantidade de amostras`; o pacote de 2021 tem a tabela de células no lugar da de lâminas'
  - desde: '2024'
    mudanca: plugues com `Município` em vez de `Município/Estado`; testemunhos com `Profundidade bas (m)`; lâminas com duas colunas sem nome (`coluna_11` e `coluna_12`); em 2025 a coluna `Município` dos plugues permanece, e as lâminas voltam a 10 colunas
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Amostras de rochas e fluidos: acervo e valores das depositárias

## Resumo

As amostras de rocha, sedimento e fluido extraídas de poços e da superfície ficam sob a guarda de empresas e instituições (fiéis depositárias), já que a ANP não tem estrutura definitiva para recebê-las. Cada depositária informa anualmente o volume do seu acervo na Declaração Anual de Acervo (DAA), e a ANP publica a consolidação dos dados públicos, segmentada por tipo de amostra (Resolução ANP nº 71/2014, art. 10, § 7º). O acesso é pedido por Solicitação de Acesso a Amostras (SAA), com recuperação de custos pelas depositárias, e os valores cobrados por elas são publicados todo ano (art. 64). O grupo reúne a consolidação de 2017 a 2025 em tabelas por tipo de amostra (calha, fluidos, lâminas, laterais, plugues e testemunhos), as DAAs de 2015 e 2016 e as tabelas de valores das depositárias de 2016 a 2026.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/amostras-rochas-fluidos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/amostras-de-rochas-e-fluidos |
| Licença | Não informada especificamente para este conjunto nos metadados; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | anual (metadados da ANP): a consolidação do acervo e os valores das depositárias |
| Cobertura | 2015 a 2026 |
| Unidade (uma linha) | uma caixa, um intervalo ou uma amostra declarada por uma depositária (conforme o tipo), ou uma linha de serviço com valor numa tabela de depositária |
| Granularidade | espacial: poço e bacia sedimentar; município e estado do depósito (não do poço); temporal: ano da consolidação (`ano`) e, nas DAAs de 2015 e 2016, o ano da declaração; data de conclusão do poço dentro da tabela |
| Formato bruto | ZIPs anuais com um CSV por tipo de amostra (consolidação) e um CSV por depositária (valores); CSV soltos para as DAAs de 2015 e 2016; separador ponto e vírgula |
| Estado no lake | convertido |
| Partições | `ano` |
| Chave | — |
| Colunas | 70 |
| Unidades de medida | `Profundidade topo (m)`: m (metros); `Profundidade base (m)`: m (metros); `Profundidade da lâmina (m)`: m (metros); `Profundidadedalâmina(m)`: m (metros); `Profundidade (m)`: m (metros); `Profundidade do plugue (m)`: m (metros); `Profundidade bas (m)`: m (metros); `Volume (L)`: L (litros); `VALOR (R$)`: R$ (reais; em dólares na coluna `VALOR (USD)`); `VALOR 2018 (R$)`: R$ (reais; em dólares na coluna `VALOR (USD)`); `VALOR (R$)_2`: R$ (reais; em dólares na coluna `VALOR (USD)`); `VALOR 2020 (R$)`: R$ (reais; em dólares na coluna `VALOR (USD)`); `VALOR`: R$ (reais; em dólares na coluna `VALOR (USD)`); `Valores unitários (R$)`: R$ (reais; em dólares na coluna `VALOR (USD)`); `VALOR (USD)`: R$ (reais; em dólares na coluna `VALOR (USD)`); `Valor unitário (R$)`: R$ (reais; em dólares na coluna `VALOR (USD)`); `Valor unitário (R$) incl. impostos`: R$ (reais; em dólares na coluna `VALOR (USD)`) |
| Dados pessoais | nenhum |
| Eras | 2017: consolidação 2017: cabeçalhos de calha, lâminas, laterais e testemunhos sem espaços (`Nomedopoço(ANP)`, `Baciasedimentar`); sem `Identificador da caixa` (calha, laterais e plugues) e sem `Tipo de container` (fluidos); 2018: entram `Identificador da caixa` e `Tipo de container`; cabeçalhos com espaços; 2021: `Município/Estado` passa a vir antes de `Depositária`; `Tipo de fluido` e `Quantidade de amostra` (singular) substituem `Tipo fluido` e `Quantidade de amostras`; o pacote de 2021 tem a tabela de células no lugar da de lâminas; 2024: plugues com `Município` em vez de `Município/Estado`; testemunhos com `Profundidade bas (m)`; lâminas com duas colunas sem nome (`coluna_11` e `coluna_12`); em 2025 a coluna `Município` dos plugues permanece, e as lâminas voltam a 10 colunas |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- **Fonte:** ANP, Superintendência de Dados Técnicos (SDT): consolidação das Declarações Anuais de Acervo (DAAs) das depositárias, e valores publicados pelas depositárias (metadados da ANP). Publicação conforme a Resolução ANP nº 71/2014, art. 10, § 7º (consolidação) e art. 64 (valores).
- **Catálogo do fetcher:** 24 arquivos: consolidação em ZIP de 2017 a 2025 (9), DAAs avulsas `arf-consolidacao-daa-2015`, `arf-consolidacao-daa-petrobras-2015`, `arf-consolidacao-daa-2016` e `arf-consolidacao-daa-laminas-2016` (4) e valores das depositárias em ZIP de 2016 a 2026 (11) (conferido em 2026-11-15).
- **O que entrou no lake desta documentação:** as 6 amostras originais mais 15 arquivos baixados à parte: consolidação 2017, 2018, 2021 e 2023, DAA 2015 e 2016 e valores das depositárias de 2017 a 2020 e de 2022 a 2026. **Não conferidos:** a consolidação de 2020 e de 2022 (seguem o padrão dos vizinhos) e o arquivo de lâminas da DAA 2016 (`arf-consolidacao-daa-laminas-2016`, 34 MB), que não foram baixados.
- **Metadados:** cada tipo de amostra tem um PDF próprio (calha, células, fluidos, lâminas, laterais, plugues e testemunhos; versões de 2017 para calha, fluidos, lâminas, laterais, plugues e testemunhos), mais os das DAAs de 2015 e 2016 e o dos valores das depositárias. O PDF das células repete o das lâminas, com a coluna de lâminas delgadas ausente. A página oficial indica atualização em 11/03/2026.

## Conteúdo

O grupo reúne nove tabelas finas, e cada uma tem estrutura própria:

| Dataset fino | Conteúdo | Anos no lake |
|---|---|---|
| `amostras-rochas-fluidos-calha` | consolidação das amostras de calha: poço, bacia, caixas, intervalo de profundidade e depositária | 2017, 2018, 2019, 2021, 2023, 2024, 2025 |
| `amostras-rochas-fluidos-fluidos` | amostras de fluidos: tipo de fluido, quantidade, recipiente e volume | 2017, 2018, 2019, 2021, 2023, 2024, 2025 |
| `amostras-rochas-fluidos-laminas` | lâminas delgadas e bioestratigráficas por profundidade | 2017, 2018, 2019, 2023, 2024, 2025 |
| `amostras-rochas-fluidos-celulas` | «células» (lâminas bioestratigráficas) do pacote de 2021, que no lugar de lâminas traz esta tabela | 2021 |
| `amostras-rochas-fluidos-laterais` | amostras laterais: profundidade e caixas | 2017, 2018, 2019, 2021, 2023, 2024, 2025 |
| `amostras-rochas-fluidos-plugues` | plugues: testemunho de origem, profundidade, orientação e caixas | 2017, 2018, 2019, 2021, 2023, 2024, 2025 |
| `amostras-rochas-fluidos-testemunhos` | testemunhos: número, caixas e intervalo de profundidade | 2017, 2018, 2019, 2021, 2023, 2024, 2025 |
| `amostras-rochas-fluidos` | DAA de 2015 (`daa-2015`, `daa-petrobras-2015`) e de 2016 (`daa-2016`): poços e número de caixas por depositária | sem partição (2015, 2016) |
| `amostras-rochas-fluidos-depositarias` | tabelas de valores que as fiéis depositárias cobram para atender às SAAs, uma por depositária e ano | 2016 a 2026 (274 tabelas) |

Linhas por ano da consolidação, nas tabelas lidas:

| Ano | calha | fluidos | lâminas (células em 2021) | laterais | plugues | testemunhos |
|---|---|---|---|---|---|---|
| 2017 | 165.533 | 1.818 | 175.800 | 61.759 | 157.245 | 34.550 |
| 2018 | 242.034 | 2.617 | 392.496 | 66.175 | 175.228 | 34.630 |
| 2019 | 180.904 | 3.262 | 324.257 | 68.931 | 179.570 | 36.167 |
| 2021 | 194.908 | 3.376 | 155.599 (células) | 73.635 | 181.024 | 45.173 |
| 2023 | 193.949 | 3.697 | 401.955 | 75.284 | 182.167 | 59.425 |
| 2024 | 259.833 | 9.887 | 561.622 | 75.607 | 203.062 | 90.905 |
| 2025 | 281.052 | 8.514 | 653.824 | 77.058 | 192.642 | 152.186 |

- **Cada ano é uma fotografia do acervo declarado,** não um incremento: os mesmos poços reaparecem a cada ano, e o total só cresce ou muda com novas declarações e correções. Não some anos.
- **DAAs de 2015 e 2016:** `daa-2015` tem 2.462 linhas, `daa-petrobras-2015`, 24.102 (poço, caixas e depósito) e `daa-2016`, 22.532 (calha, testemunhos e laterais por poço); as lâminas de 2016 estão em arquivo à parte, não lido.
- **Valores das depositárias:** 274 tabelas (uma por depositária e ano) com 13.585 linhas no total, de 2016 a 2026; o número de tabelas por ano vai de 10 (2018 e 2021) a 42 (2026).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2016 | 25 arquivos, de 4 a 4 colunas |
| 2017 | 32 arquivos, de 4 a 11 colunas |
| 2018 | 16 arquivos, de 4 a 12 colunas |
| 2019 | 22 arquivos, de 4 a 12 colunas |
| 2020 | 19 arquivos, de 4 a 6 colunas |
| 2021 | 16 arquivos, de 4 a 12 colunas |
| 2022 | 24 arquivos, de 4 a 7 colunas |
| 2023 | 30 arquivos, de 4 a 12 colunas |
| 2024 | 45 arquivos, de 4 a 12 colunas |
| 2025 | 45 arquivos, de 4 a 12 colunas |
| 2026 | 42 arquivos, de 4 a 6 colunas |

## Variáveis

As descrições vêm dos metadados da ANP de cada tipo de amostra (e das DAAs de 2015 e 2016), com os nomes variantes de cada ano mapeados para a mesma descrição. As colunas sem nome do cabeçalho das tabelas de depositárias (`coluna_2` a `coluna_6`, `z`) não constam dos metadados, e suas descrições são deduzidas dos valores. A coluna *Arquivos* diz em quais tabelas finas a coluna aparece. O lake guarda tudo como texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Poço` | `Poço` | texto | Nome do poço na ANP (DAA 2015 e DAA da Petrobras 2015) | — | — | `amostras-rochas-fluidos` |
| `Caixas` | `Caixas` | texto | Número de caixas com as amostras desse poço | — | — | `amostras-rochas-fluidos` |
| `Depositária` | `Depositária` | texto | Nome fantasia da empresa ou instituição que guarda a amostra (fiel depositária) | — | 2017 a 2025 | `amostras-rochas-fluidos`, `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-celulas` e mais 5 |
| `Depósito` | `Depósito` | texto | Empresa contratada pela depositária para guardar a amostra; às vezes, a própria depositária | — | — | `amostras-rochas-fluidos` |
| `Cidade` | `Cidade` | texto | Cidade onde fica o depósito | — | — | `amostras-rochas-fluidos` |
| `UF` | `UF` | texto | Sigla do estado onde fica o depósito | — | — | `amostras-rochas-fluidos` |
| `Município/Estado do Depósito` | `Município/Estado do Depósito` | texto | Município e estado onde fica o depósito (DAA 2016) | — | — | `amostras-rochas-fluidos` |
| `Poços e Levantamentos ↓` | `Poços e Levantamentos ↓` | texto | Nome do poço na ANP (DAA 2016), sem os hifens em parte das linhas (por exemplo, `1ALV3DBA`) | — | — | `amostras-rochas-fluidos` |
| `Código API do poço` | `Código API do poço` | texto | Cadastro do poço na ANP (DAA 2016) | — | — | `amostras-rochas-fluidos` |
| `Nº de caixas de amostras de calha` | `Nº de caixas de amostras de calha` | texto | Número de caixas com amostras de calha desse poço (DAA 2016) | — | — | `amostras-rochas-fluidos` |
| `Nº de caixas de testemunhos` | `Nº de caixas de testemunhos` | texto | Número de caixas com testemunhos desse poço (DAA 2016) | — | — | `amostras-rochas-fluidos` |
| `Nº de caixas de amostras laterais` | `Nº de caixas de amostras laterais` | texto | Número de caixas com amostras laterais desse poço (DAA 2016) | — | — | `amostras-rochas-fluidos` |
| `Observações ↓` | `Observações ↓` | texto | Observações de preenchimento opcional (DAA 2016) | — | — | `amostras-rochas-fluidos` |
| `Bacia sedimentar` | `Bacia sedimentar` | texto | Bacia de onde a amostra foi coletada (em maiúsculas, por exemplo `ALAGOAS MAR`, `POTIGUAR`) | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-celulas`, `amostras-rochas-fluidos-fluidos` e mais 4 |
| `Código do poço (API)` | `Código do poço (API)` | texto | Cadastro do poço na ANP, conforme a Resolução ANP nº 699/2017 (texto de 9 a 13 dígitos, na maioria 11 ou 12) | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-celulas`, `amostras-rochas-fluidos-fluidos` e mais 4 |
| `Nomedopoço(ANP)` | `Nomedopoço(ANP)` | texto | Nome do poço na ANP, conforme a Resolução ANP nº 699/2017 (por exemplo, `1-ALS-10`) | — | 2017 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-laminas`, `amostras-rochas-fluidos-laterais` e mais 1 |
| `Total de caixas` | `Total de caixas` | texto | Número total de caixas onde essas amostras estão armazenadas no depósito | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-laterais`, `amostras-rochas-fluidos-plugues` e mais 1 |
| `Profundidade topo (m)` | `Profundidade topo (m)` | texto | Profundidade medida de origem do topo da amostra (a mais rasa), em metros, em texto com vírgula decimal e, nos arquivos antigos, ponto de milhar (`2.445,00`) | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-fluidos`, `amostras-rochas-fluidos-testemunhos` |
| `Profundidade base (m)` | `Profundidade base (m)` | texto | Profundidade medida de origem da base da amostra (a mais funda), em metros, em texto | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-fluidos`, `amostras-rochas-fluidos-testemunhos` |
| `Data de conclusão do poço` | `Data de conclusão do poço` | texto | Data em que terminaram as atividades diretamente ligadas à perfuração do poço (dd/mm/aaaa); vazia em parte das linhas | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-celulas`, `amostras-rochas-fluidos-fluidos` e mais 4 |
| `Município/Estado` | `Município/Estado` | texto | Município e estado do depósito onde a amostra está guardada (não é o local do poço; por exemplo, `Aracaju/SE`, `DUQUE DE CAXIAS/RJ`) | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-celulas`, `amostras-rochas-fluidos-fluidos` e mais 4 |
| `Nome do poço (ANP)` | `Nome do poço (ANP)` | texto | Nome do poço na ANP, conforme a Resolução ANP nº 699/2017 (por exemplo, `1-ALS-10`) | — | 2017 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-celulas`, `amostras-rochas-fluidos-fluidos` e mais 4 |
| `Identificador da caixa` | `Identificador da caixa` | texto | Número sequencial da caixa onde está a amostra no depósito (em alguns arquivos recentes, código com letra, como `1-1R`) | — | 2018 a 2025 | `amostras-rochas-fluidos-calha`, `amostras-rochas-fluidos-laterais`, `amostras-rochas-fluidos-plugues` |
| `Profundidade da lâmina (m)` | `Profundidade da lâmina (m)` | texto | Profundidade medida de origem da lâmina, em metros, em texto; pode ser um intervalo (`90,00 - 120,00`) | — | 2018 a 2025 | `amostras-rochas-fluidos-celulas`, `amostras-rochas-fluidos-laminas` |
| `Tipo de amostra de origem` | `Tipo de amostra de origem` | texto | Tipo de origem das amostras: CALH (calha), CLHC, LATE (lateral), PLUG (plugue), TEST (testemunho), e variações de grafia nos arquivos mais recentes (`Plugue`, `AC`) | — | 2018 a 2025 | `amostras-rochas-fluidos-celulas`, `amostras-rochas-fluidos-laminas` |
| `Quantidade de células bioestratigráficas` | `Quantidade de células bioestratigráficas` | texto | Número de lâminas (células) bioestratigráficas geradas para a profundidade indicada; coluna do arquivo de 2021, que substitui as colunas de lâminas | — | 2021 | `amostras-rochas-fluidos-celulas` |
| `SERVIÇOS` | `SERVIÇOS` | texto | Especificação de cada serviço oferecido pela depositária para atender às solicitações de acesso a amostras; as linhas de título de seção (`1. Amostra de Calha`) têm só este campo | — | todo | `amostras-rochas-fluidos-depositarias` |
| `UNIDADE` | `UNIDADE` | texto | Forma de contabilização do serviço (caixa, unidade, por metro, SAA etc.) | — | todo | `amostras-rochas-fluidos-depositarias` |
| `VALOR (R$)` | `VALOR (R$)` | texto | Valor, em reais, praticado por unidade do serviço, escrito como `R$ 901,00` | — | todo | `amostras-rochas-fluidos-depositarias` |
| `membro` | `membro` | texto | Nome do arquivo de cada depositária dentro do ZIP anual (por exemplo, `ALVOPETRO_2019`), acrescentado pelo conversor; identifica a depositária da tabela | — | todo | `amostras-rochas-fluidos-depositarias` |
| `VALOR 2018 (R$)` | `VALOR 2018 (R$)` | texto | Valor, em reais, praticado por unidade do serviço, na tabela de 2018 | — | 2018 | `amostras-rochas-fluidos-depositarias` |
| `VALOR (R$)_2` | `VALOR (R$)_2` | texto | Segunda coluna de valor em reais da tabela de 2020 (o conversor repetiu o nome e acrescentou `_2`); significado não informado | — | 2020 | `amostras-rochas-fluidos-depositarias` |
| `VALOR 2020 (R$)` | `VALOR 2020 (R$)` | texto | Valor, em reais, praticado por unidade do serviço, na tabela de 2020 | — | 2020 | `amostras-rochas-fluidos-depositarias` |
| `VALOR` | `VALOR` | texto | Valor praticado por unidade do serviço, em reais, escrito sem o rótulo de moeda no cabeçalho (tabelas de 2021, 2024, 2025 e 2026) | — | 2021 a 2026 | `amostras-rochas-fluidos-depositarias` |
| `SERVIÇO` | `SERVIÇO` | texto | Especificação do serviço oferecido pela depositária (nome da coluna nas tabelas de 2022 em diante) | — | 2022 a 2026 | `amostras-rochas-fluidos-depositarias` |
| `coluna_2` | `coluna_2` | texto | Coluna sem nome no cabeçalho da tabela (o conversor a chamou `coluna_2`); nas tabelas de 2022 em diante traz o item do serviço ou o detalhe, conforme a depositária | — | 2022 a 2026 | `amostras-rochas-fluidos-depositarias` |
| `Detalhes` | `Detalhes` | texto | Detalhamento do serviço (tabelas de 2022 em diante) | — | 2022 a 2026 | `amostras-rochas-fluidos-depositarias` |
| `Valores unitários (R$)` | `Valores unitários (R$)` | texto | Valor unitário do serviço, em reais (tabelas de 2022 e 2023) | — | 2022 a 2023 | `amostras-rochas-fluidos-depositarias` |
| `coluna_6` | `coluna_6` | texto | Coluna sem nome no cabeçalho da tabela (o conversor a chamou `coluna_6`); significado não informado | — | 2022 a 2023 | `amostras-rochas-fluidos-depositarias` |
| `VALOR (USD)` | `VALOR (USD)` | texto | Valor, em dólares, praticado por unidade do serviço (tabelas de 2022 e 2023 de uma depositária) | — | 2022 a 2023 | `amostras-rochas-fluidos-depositarias` |
| `SERVIÇO [Detalhes]` | `SERVIÇO [Detalhes]` | texto | Especificação e detalhe do serviço, em uma só coluna (tabelas de 2022 e 2023 com esse formato) | — | 2022 a 2023 | `amostras-rochas-fluidos-depositarias` |
| `coluna_3` | `coluna_3` | texto | Coluna sem nome no cabeçalho da tabela (o conversor a chamou `coluna_3`); traz os valores unitários nas tabelas com cabeçalho `SERVIÇO [Detalhes]` | — | 2022 a 2023 | `amostras-rochas-fluidos-depositarias` |
| `Valor unitário (R$)` | `Valor unitário (R$)` | texto | Valor unitário do serviço, em reais (tabelas de 2024 a 2026) | — | 2024 a 2026 | `amostras-rochas-fluidos-depositarias` |
| `z` | `z` | texto | Coluna com o cabeçalho `z` numa tabela de 2024 e 2025; significado não informado | — | 2024 a 2025 | `amostras-rochas-fluidos-depositarias` |
| `Valor unitário (R$) incl. impostos` | `Valor unitário (R$) incl. impostos` | texto | Valor unitário do serviço, em reais, com impostos incluídos (tabelas de 2024 e 2025 de uma depositária) | — | 2024 a 2025 | `amostras-rochas-fluidos-depositarias` |
| `coluna_5` | `coluna_5` | texto | Coluna sem nome no cabeçalho da tabela (o conversor a chamou `coluna_5`); significado não informado | — | 2024 a 2025 | `amostras-rochas-fluidos-depositarias` |
| `coluna_4` | `coluna_4` | texto | Coluna sem nome no cabeçalho da tabela (o conversor a chamou `coluna_4`); significado não informado | — | 2024 a 2025 | `amostras-rochas-fluidos-depositarias` |
| `Tipo fluido` | `Tipo fluido` | texto | Fase dominante da amostra de fluido (por exemplo, água, óleo, fluido de perfuração); nome da coluna nos arquivos de 2017 a 2019 | — | 2017 a 2019 | `amostras-rochas-fluidos-fluidos` |
| `Quantidade de amostras` | `Quantidade de amostras` | texto | Número de amostras de fluido; nome da coluna nos arquivos de 2017 a 2019 | — | 2017 a 2019 | `amostras-rochas-fluidos-fluidos` |
| `Volume (L)` | `Volume (L)` | texto | Volume da amostra de fluido, em litros, em texto (na amostra de 2025 aparecem valores como `Menos de 5L`) | — | 2017 a 2025 | `amostras-rochas-fluidos-fluidos` |
| `Tipo de container` | `Tipo de container` | texto | Tipo de material do recipiente da amostra de fluido (em geral garrafa de vidro âmbar); ausente no arquivo de 2017 | — | 2018 a 2025 | `amostras-rochas-fluidos-fluidos` |
| `Tipo de fluido` | `Tipo de fluido` | texto | Fase dominante da amostra de fluido (por exemplo, água, óleo, lama de perfuração); a coluna fica vazia em parte das linhas de 2025 | — | 2021 a 2025 | `amostras-rochas-fluidos-fluidos` |
| `Quantidade de amostra` | `Quantidade de amostra` | texto | Número de amostras de fluido; nome da coluna nos arquivos de 2021 em diante | — | 2021 a 2025 | `amostras-rochas-fluidos-fluidos` |
| `Baciasedimentar` | `Baciasedimentar` | texto | Bacia de onde a amostra foi coletada (em maiúsculas, por exemplo `ALAGOAS MAR`, `POTIGUAR`) | — | 2017 | `amostras-rochas-fluidos-laminas` |
| `Códigodopoço(API)` | `Códigodopoço(API)` | texto | Cadastro do poço na ANP, conforme a Resolução ANP nº 699/2017 (texto de 9 a 13 dígitos, na maioria 11 ou 12) | — | 2017 | `amostras-rochas-fluidos-laminas` |
| `Profundidadedalâmina(m)` | `Profundidadedalâmina(m)` | texto | Profundidade medida de origem da lâmina, em metros, em texto; pode ser um intervalo (`90,00 - 120,00`) | — | 2017 | `amostras-rochas-fluidos-laminas` |
| `Tipodeamostradeorigem` | `Tipodeamostradeorigem` | texto | Tipo de origem das amostras: CALH (calha), CLHC, LATE (lateral), PLUG (plugue), TEST (testemunho), e variações de grafia nos arquivos mais recentes (`Plugue`, `AC`) | — | 2017 | `amostras-rochas-fluidos-laminas` |
| `Quantidadedelâminasdelgadas` | `Quantidadedelâminasdelgadas` | texto | Número de lâminas delgadas geradas para a profundidade indicada | — | 2017 | `amostras-rochas-fluidos-laminas` |
| `Quantidadedelâminasbioestratigráficas` | `Quantidadedelâminasbioestratigráficas` | texto | Número de lâminas bioestratigráficas geradas para a profundidade indicada (`-` ou vazio quando não há) | — | 2017 | `amostras-rochas-fluidos-laminas` |
| `Datadeconclusãodopoço` | `Datadeconclusãodopoço` | texto | Data em que terminaram as atividades diretamente ligadas à perfuração do poço (dd/mm/aaaa); vazia em parte das linhas | — | 2017 | `amostras-rochas-fluidos-laminas` |
| `Quantidade de lâminas delgadas` | `Quantidade de lâminas delgadas` | texto | Número de lâminas delgadas geradas para a profundidade indicada | — | 2018 a 2025 | `amostras-rochas-fluidos-laminas` |
| `Quantidade de lâminas bioestratigráficas` | `Quantidade de lâminas bioestratigráficas` | texto | Número de lâminas bioestratigráficas geradas para a profundidade indicada (`-` ou vazio quando não há) | — | 2018 a 2025 | `amostras-rochas-fluidos-laminas` |
| `coluna_11` | `coluna_11` | texto | Coluna sem nome no arquivo de lâminas de 2024 (o conversor a chamou `coluna_11`), vazia na amostra; sem significado informado | — | 2024 | `amostras-rochas-fluidos-laminas` |
| `coluna_12` | `coluna_12` | texto | Coluna sem nome no arquivo de lâminas de 2024 (o conversor a chamou `coluna_12`), vazia na amostra; sem significado informado | — | 2024 | `amostras-rochas-fluidos-laminas` |
| `Profundidade (m)` | `Profundidade (m)` | texto | Profundidade medida de origem da amostra lateral, em metros, em texto | — | 2017 a 2025 | `amostras-rochas-fluidos-laterais` |
| `Número do testemunho` | `Número do testemunho` | texto | Número sequencial de identificação do testemunho (às vezes com texto, como `1-1H` ou `Testemunho 1`) | — | 2017 a 2025 | `amostras-rochas-fluidos-plugues`, `amostras-rochas-fluidos-testemunhos` |
| `Profundidade do plugue (m)` | `Profundidade do plugue (m)` | texto | Profundidade medida de onde foi coletado o plugue, em metros, em texto | — | 2017 a 2025 | `amostras-rochas-fluidos-plugues` |
| `Orientação do plugue (H ou V)` | `Orientação do plugue (H ou V)` | texto | Orientação da coleta do plugue: H horizontal, V vertical | — | 2017 a 2025 | `amostras-rochas-fluidos-plugues` |
| `Município` | `Município` | texto | Município e estado do depósito onde a amostra está guardada (nome da coluna nos arquivos de plugues de 2024 e 2025) | — | 2024 a 2025 | `amostras-rochas-fluidos-plugues` |
| `Profundidade bas (m)` | `Profundidade bas (m)` | texto | Profundidade medida de origem da base da amostra, em metros; o nome da coluna tem erro de grafia («bas») nos arquivos de testemunhos de 2024 e 2025 | — | 2024 a 2025 | `amostras-rochas-fluidos-testemunhos` |

## No lake

- Dataset `anp/amostras-rochas-fluidos` e oito datasets finos irmãos (`-calha`, `-celulas`, `-depositarias`, `-fluidos`, `-laminas`, `-laterais`, `-plugues` e `-testemunhos`); os de consolidação são particionados por `ano`, e as DAAs de 2015 e 2016 não têm partição.
- Um Parquet por CSV: o nome é `<arquivo do ZIP>__<csv>.parquet` (por exemplo, `arf-consolidacao-2019__consolidacao_calha_2019.parquet`); nas depositárias, um por depositária e ano (274), com a coluna `membro`.
- Todas as colunas são texto, com os números em vírgula decimal e, nos arquivos antigos, ponto de milhar (`2.445,00`).
- Os cabeçalhos das depositárias mudam muito entre anos e entre empresas (cabeçalho em duas linhas, colunas sem nome, `z`); o conversor gravou as colunas sem nome como `coluna_N`.

## Cuidados de uso

- **Cada ano repete o acervo.** Cada consolidação é um retrato completo das declarações do ano; para o estado atual use o ano mais recente, e compare anos só para ver mudanças de declaração.
- **`Município/Estado` é do depósito, não do poço.** A coluna diz onde as amostras estão guardadas; não use como localização geográfica do poço (use a bacia e o código do poço).
- **Cabeçalhos variam entre anos.** Para empilhar anos, use `union_by_name` e junte as variantes (`Tipo fluido`/`Tipo de fluido`, `Quantidade de amostras`/`Quantidade de amostra`, `Município`/`Município/Estado`, `Profundidade base (m)`/`Profundidade bas (m)`; em 2017 sem espaços nos nomes).
- **Números em texto, com formatos diferentes.** `2.445,00` (2019), `407,00` (2017), `2956` (2024) e `516,00` (2025); remova o ponto de milhar só quando ele existir e troque a vírgula por ponto. `Volume (L)` tem valores como `Menos de 5L`.
- **Dados faltantes.** `Data de conclusão do poço` está vazia em parte das linhas (por exemplo, na amostra de 2019); `Tipo de fluido` vazia em parte de 2025.
- **O código do poço não tem tamanho fixo.** `Código do poço (API)` tem de 9 a 13 dígitos (a maioria, 11 ou 12; `81160159500` e `081160406100` aparecem nos exemplos de 2019 como códigos de poços da mesma bacia, um sem e outro com zero à esquerda); normalize antes de ligar a outras tabelas.
- **Colunas sem nome** nas tabelas de lâminas de 2024 (`coluna_11` e `coluna_12`) e nas de depositárias (`coluna_2` a `coluna_6`, `z`) são artefatos do cabeçalho do CSV da fonte.
- **As tabelas das depositárias não têm estrutura uniforme.** Cada empresa e ano tem o seu layout (seções numeradas, colunas de detalhe e valor); só a coluna `membro` identifica a empresa. Para comparar preços é preciso tratar cada layout.
- **Valores monetários em texto** (`R$ 901,00`, `R$ 72,21`), às vezes vazios para o serviço sem preço, e em dólares (`VALOR (USD)`) em uma tabela.
- **Anos que faltam na tabela acima.** A consolidação de 2020 e a de 2022 existem no catálogo, mas não foram lidas; o lake desta documentação não as tem.
- **Dados identificáveis.** Depositárias, empresas e poços; não há dados de pessoas físicas.

## Exemplos

Número de linhas e de poços distintos de calha por ano da consolidação, usando as colunas comuns:

```python
import duckdb

duckdb.sql("""
    SELECT ano, count(*) AS caixas, count(DISTINCT "Código do poço (API)") AS pocos
    FROM read_parquet('lake/anp/amostras-rochas-fluidos-calha/**/*.parquet', hive_partitioning = true, union_by_name = true)
    GROUP BY ALL
    ORDER BY ano
""").show()
```

## Referências

- Dados abertos da ANP, Amostras de Rochas e Fluidos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/amostras-de-rochas-e-fluidos
- Metadados: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-amostras-de-rochas-e-fluidos/acervo-de-amostras/ (por exemplo, `metadados-consolidacao-calha.pdf`) e .../valores-praticados-pelas-fieis-depositarias-para-atendimento-das-saas/metadados-valores-depositarias-saas.pdf
- Resolução ANP nº 71/2014 (procedimentos para coleta e manejo das amostras).
