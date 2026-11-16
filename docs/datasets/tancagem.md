---
dataset:
  id: tancagem
  fonte: anp
  titulo: Tancagem do abastecimento nacional de combustíveis (unidade a unidade)
  resumo: Capacidade operacional de cada unidade de armazenagem (tanque, vaso ou esfera) das instalações autorizadas pela ANP, em retratos mensais de 2022 em diante.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/tancagem-do-abastecimento-nacional-de-combustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo os metadados da ANP (versão de 12/06/2026); alguns arquivos cobrem vários meses (por exemplo, `marco-julho` de 2024) e o catálogo vai de junho de 2022 a setembro de 2026
  cobertura:
    inicio: 2022-06
    fim: 2026-09
  unidade: uma unidade de armazenagem (tanque, vaso de pressão ou esfera) de uma instalação autorizada, num retrato da data de disponibilização
  granularidade:
    espacial: instalação (CNPJ, código i-SIMP, município e UF)
    temporal: data de disponibilização do retrato (`Data`); um retrato por arquivo
  formato_bruto: CSV com separador `,` e UTF-8 (a maior parte com BOM), um por mês ou por intervalo de meses
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave:
    - Data
    - CodInstalacao
    - Tag
    - TipoDaUnidade
    - GrupoDeProdutos
    colunas: 12
  unidades_de_medida:
    TancagemM3: m³ (capacidade operacional)
  dados_pessoais:
  - coluna: NomeEmpresarial
    categoria: razão social de pessoa jurídica
  - coluna: Cnpj
    categoria: CNPJ de pessoa jurídica
  eras:
  - desde: '2022'
    mudanca: primeiros arquivos (junho de 2022 em diante) com nomes como `tancagem_terminais_dados_abertos_<mês>_2022.csv`; o de outubro de 2022 é um `.xlsx`; as colunas da amostra de dezembro de 2022 são as mesmas 12 dos arquivos de 2026
  - desde: '2024'
    mudanca: arquivos que cobrem vários meses passam a ser publicados (`marco-julho` e `setembro-outubro` de 2024, `maio-junho`, `julho-agosto` e `setembro-a-novembro` de 2025, `maio-a-setembro` de 2026); em cada caso o catálogo marca o último mês do intervalo
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Tancagem do abastecimento nacional de combustíveis (unidade a unidade)

## Resumo

Dados abertos que alimentam o painel de tancagem autorizada a operar da ANP: a capacidade de armazenagem da indústria do petróleo, do gás natural e dos biocombustíveis, por tipo de instalação (distribuidor, TRR, produtor e terminais), por empresa, por grupo de produto (derivados e biocombustíveis, GLP, petróleo e outros) e por localidade. Cada linha é uma unidade de armazenagem de uma instalação, com sua capacidade operacional em m³. Cada arquivo é um retrato completo da tancagem autorizada na data em que foi disponibilizado, e não uma variação do período.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/tancagem` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/tancagem-do-abastecimento-nacional-de-combustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo os metadados da ANP (versão de 12/06/2026); alguns arquivos cobrem vários meses (por exemplo, `marco-julho` de 2024) e o catálogo vai de junho de 2022 a setembro de 2026 |
| Cobertura | 2022-06 a 2026-09 |
| Unidade (uma linha) | uma unidade de armazenagem (tanque, vaso de pressão ou esfera) de uma instalação autorizada, num retrato da data de disponibilização |
| Granularidade | espacial: instalação (CNPJ, código i-SIMP, município e UF); temporal: data de disponibilização do retrato (`Data`); um retrato por arquivo |
| Formato bruto | CSV com separador `,` e UTF-8 (a maior parte com BOM), um por mês ou por intervalo de meses |
| Estado no lake | convertido |
| Partições | `ano`, `mes` |
| Chave | `Data`, `CodInstalacao`, `Tag`, `TipoDaUnidade`, `GrupoDeProdutos` |
| Colunas | 12 |
| Unidades de medida | `TancagemM3`: m³ (capacidade operacional) |
| Dados pessoais | `NomeEmpresarial` (razão social de pessoa jurídica); `Cnpj` (CNPJ de pessoa jurídica) |
| Eras | 2022: primeiros arquivos (junho de 2022 em diante) com nomes como `tancagem_terminais_dados_abertos_<mês>_2022.csv`; o de outubro de 2022 é um `.xlsx`; as colunas da amostra de dezembro de 2022 são as mesmas 12 dos arquivos de 2026; 2024: arquivos que cobrem vários meses passam a ser publicados (`marco-julho` e `setembro-outubro` de 2024, `maio-junho`, `julho-agosto` e `setembro-a-novembro` de 2025, `maio-a-setembro` de 2026); em cada caso o catálogo marca o último mês do intervalo |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa os arquivos de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/<AAAA>/<mês>.csv` (2023 a 2026, com nomes como `janeiro.csv`, `maio-junho.csv`) e `.../dados-abertos/2022/tancagem_terminais_dados_abertos_*.csv`: 37 entradas, de 2022-06 a 2026-09, sendo a de 2022-10 um `.xlsx`.
- Tamanhos conferidos na amostra (2026-11-15): 2022-12, 1.702.456 bytes (10.302 linhas de dados); 2023-10, 2.242.175 (13.705); 2024-12, 2.297.584 (14.060); 2025-08, 2.352.426 (14.393); 2026-01, 2.370.491 (14.517); 2026-02, 2.375.100 (14.545).
- Cinco dos seis arquivos da amostra (todos menos o de janeiro de 2026) terminam com uma linha em branco, que o lake guarda como linha nula.
- Metadados em PDF (versão 12/06/2026): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/metadados-tancagem.pdf, que descreve 12 colunas. Fonte do dado: Sistema de Informações de Movimentação de Produtos (SIMP) da ANP; contato da área de movimentação.
- A página oficial liga os dados ao Painel Dinâmico da tancagem do abastecimento nacional de combustíveis e informa atualização em 06/11/2026.

## Conteúdo

- **Um retrato por arquivo.** Cada arquivo traz todas as unidades de armazenagem autorizadas na data de `Data`, de modo que as linhas de arquivos diferentes repetem as mesmas unidades; o volume somado cresce de 32,1 milhões de m³ no retrato de 01/12/2022 para 59,98 milhões de m³ em 27/02/2026 (soma de `TancagemM3` na amostra).
- **Instalações e segmentos.** Na amostra de seis retratos, 1.865 códigos de instalação e 1.178 razões sociais; os segmentos mais frequentes são BASES DO RAMO DE COMBUSTÍVEIS, TERMINAL, BASES DO RAMO DE TRR, INSTALAÇÃO PRODUTORA DE ETANOL, INSTALAÇÃO PRODUTORA DE BIODIESEL e REFINARIA (11 segmentos distintos no total); por tipo de unidade, 73.311 tanques, 7.680 vasos de pressão e 479 esferas.
- **Grupos de produto.** DERIVADOS E BIOCOMBUSTÍVEIS (62.404 linhas), GLP (9.456), OUTROS (8.376) e PETRÓLEO (1.234).
- **Chave.** Na amostra, `Data`, `CodInstalacao`, `Tag`, `TipoDaUnidade` e `GrupoDeProdutos` juntas não se repetem entre as 81.470 linhas completas (sem as 52 quebradas nem as 5 nulas), que dão 81.470 combinações; `Data`, `CodInstalacao` e `Tag` sozinhas repetem em 104 linhas, porque o mesmo rótulo aparece em unidades de grupos de produto diferentes.

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| 2022 | `tancagem-12` (12) |
| 2023 | `tancagem-10` (12) |
| 2024 | `tancagem-12` (12) |
| 2025 | `tancagem-08` (12) |
| 2026 | `tancagem-01` (12); `tancagem-02` (12) |

## Variáveis

As descrições vêm do documento de metadados da ANP (versão de 12/06/2026, 12 colunas). O nome do campo de volume nos metadados é `Tancagem (m³)`; no arquivo e no lake é `TancagemM3`.
Todas as colunas são texto, inclusive `Data` (formato `AAAA-MM-DD`), `CodInstalacao` e `TancagemM3`.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `Data` | `Data` | texto | Data de disponibilização dos dados abertos na página da ANP, no formato `AAAA-MM-DD`; todas as linhas de um arquivo têm a mesma data (veja Cuidados de uso) | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `NomeEmpresarial` | `NomeEmpresarial` | texto | Nome empresarial (razão social) da pessoa jurídica autorizada pela ANP a operar a instalação com tancagem | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `Uf` | `Uf` | texto | Sigla da unidade da federação onde está estabelecida a instalação autorizada a operar | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `Municipio` | `Municipio` | texto | Nome do município onde está estabelecida a instalação autorizada a operar | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `Cnpj` | `Cnpj` | texto | Número do Cadastro Nacional da Pessoa Jurídica (CNPJ) da empresa autorizada a operar a instalação, com 14 dígitos e sem pontuação | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `CodInstalacao` | `CodInstalacao` | texto | Código de instalação i-SIMP: sequência numérica de sete algarismos que identifica cada estabelecimento junto à ANP | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `Segmento` | `Segmento` | texto | Atividade econômica da indústria do petróleo, do gás natural e dos biocombustíveis (por exemplo, BASES DO RAMO DE TRR, TERMINAL, REFINARIA, INSTALAÇÃO PRODUTORA DE ETANOL) | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `DetalheInstalacao` | `DetalheInstalacao` | texto | Detalhe relevante sobre o segmento em que a instalação atua (por exemplo, EXCLUSIVA, COMPARTILHADA, MARÍTIMO, TERRESTRE) | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `Tag` | `Tag` | texto | Rótulo, numérico ou alfanumérico, que identifica cada unidade dentro da instalação e é cadastrado no SIMP; a grafia varia (`TQ 01`, `01`, `TQ01`) | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `TipoDaUnidade` | `TipoDaUnidade` | texto | Tipo da unidade de armazenagem: recipiente com capacidade líquida superior a 230 L, projetado conforme normas técnicas, de instalação fixa e não usado em processamento industrial | TANQUE = tanque; VASO DE PRESSÃO = vaso de pressão; ESFERA = esfera | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `GrupoDeProdutos` | `GrupoDeProdutos` | texto | Grupo de produtos armazenados na unidade: petróleo, seus derivados e biocombustíveis e outros líquidos regulados pela ANP compatíveis no transporte dutoviário | DERIVADOS E BIOCOMBUSTÍVEIS = derivados e biocombustíveis; GLP = gás liquefeito de petróleo; PETRÓLEO = petróleo; OUTROS = outros | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |
| `TancagemM3` | `Tancagem (m³)` | texto | Volume total que pode ser armazenado na unidade, cadastrado como capacidade operacional na ANP, em metros cúbicos (m³), arredondado para o inteiro mais próximo, sem separador de milhares. Nos metadados da ANP a coluna se chama `Tancagem (m³)` | — | todo | `tancagem-01`, `tancagem-02`, `tancagem-08` e mais 2 |

## No lake

- Dataset `anp/tancagem`, particionado por `ano` e `mes`; um Parquet por arquivo da fonte, no padrão `ano=<AAAA>/mes=<MM>/tancagem_<AAAA>-<MM>.parquet`, em que `mes` é o último mês do arquivo do catálogo (nos arquivos que cobrem vários meses).
- Todas as 12 colunas do CSV ficam como texto; a linha em branco que fecha alguns arquivos vira uma linha com todas as colunas nulas.

## Cuidados de uso

- **Retratos acumulados, não fluxos.** Não some `TancagemM3` entre arquivos: cada arquivo já é o total da tancagem naquela data. Para uma série, some dentro de cada `Data` e compare os totais.
- **`Data` não é o mês do nome do arquivo.** É a data de disponibilização: o arquivo catalogado como 2023-10 tem `Data` 2023-12-04, o de 2024-12 tem 2025-01-06 e o de 2026-01 tem 2026-01-31. Use `Data` (e não a partição `mes`) para datar o retrato.
- **Linhas quebradas em janeiro de 2026.** No arquivo de janeiro de 2026, 52 linhas vêm inteiras entre aspas na fonte (o registro todo, com aspas duplas internas) e o leitor as guarda em uma só coluna: a coluna `Data` contém o registro inteiro (`2026-01-31,"USINA CENTRAL MATA SUL, ...",PE,...`) e as demais colunas ficam nulas. Filtre `length("Data") > 10` para achá-las; elas representam unidades de armazenagem reais que ficam fora de qualquer agregação por empresa, UF ou segmento.
- **Linha nula no fim de alguns arquivos.** Cinco dos seis arquivos da amostra têm uma linha com todas as colunas nulas (a linha em branco final); filtre `NomeEmpresarial IS NOT NULL` e `length("Data") = 10`.
- **`Tag` é texto livre.** A grafia varia entre instalações (`01`, `TQ 01`, `TQ01`, `Nº 07`); não foi verificado se a de uma mesma unidade muda entre retratos, então normalize antes de seguir uma unidade no tempo.
- **Capacidade operacional, não nominal.** `TancagemM3` é a capacidade operacional cadastrada na ANP; o dataset `armazenagem-terminais` traz capacidade nominal por terminal, com definição diferente.
- **Dados pessoais.** Só há razão social e CNPJ de pessoas jurídicas (empresas autorizadas a operar instalações); em empresas individuais a razão social pode trazer o nome do titular.

## Exemplos

Capacidade total (m³) por segmento no retrato mais recente da amostra (`Data` = 2026-02-27):

```python
import duckdb

duckdb.sql("""
    SELECT Segmento, count(*) AS unidades,
           sum(try_cast(TancagemM3 AS BIGINT)) AS capacidade_m3
    FROM read_parquet('lake/anp/tancagem/**/*.parquet', hive_partitioning = true, union_by_name = true)
    WHERE "Data" = '2026-02-27'
    GROUP BY Segmento
    ORDER BY capacidade_m3 DESC
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/tancagem-do-abastecimento-nacional-de-combustiveis
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/metadados-tancagem.pdf
- Painel Dinâmico da tancagem do abastecimento nacional de combustíveis (ANP), citado nos metadados e na página oficial.
