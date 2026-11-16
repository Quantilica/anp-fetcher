---
dataset:
  id: situacao-pocos
  fonte: anp
  titulo: Situação dos poços
  resumo: Cadastro de todos os poços perfurados no Brasil desde 1939 com a situação atual, datas de perfuração, operação, produção e injeção, método de elevação e localização da base.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
  licenca: Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal, segundo o metadado da ANP; cada arquivo é um retrato do cadastro, sem histórico (o da coleta de 2026-11-15 traz atualizações até 20/10/2026)
  cobertura:
    inicio: '1939'
    fim: em-curso
  unidade: um poço perfurado, com a situação e as datas do ciclo de vida do poço
  granularidade:
    espacial: poço (nome ANP), com campo, bacia, estado, ambiente e coordenadas da base
    temporal: 'sem série temporal: datas de perfuração (a partir de 30/09/1939), de operação e da situação (referência até 14/10/2026)'
  formato_bruto: CSV em UTF-8 com BOM, separado por vírgula; datas em DD/MM/AAAA e MM/AAAA
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 24
  dados_pessoais:
  - coluna: Operador_atual
    categoria: nome fantasia de empresa operadora (pessoa jurídica)
  eras:
  - desde: '2026'
    mudanca: layout da coleta de 2026-11-15 (24 colunas), o mesmo descrito no metadado de junho de 2026; só a versão corrente do arquivo é guardada
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Situação dos poços

## Resumo

Relação dos poços já perfurados em território nacional, com a situação atual de cada um (produzindo, injetando, fechado, abandonado, arrasado, devolvido etc.), as datas de perfuração, conclusão, início e fim de operação, produção e injeção, o método de elevação, a última intervenção e as coordenadas da base. Cada atualização substitui a anterior: o arquivo é um retrato do cadastro do SIGEP, e não uma série temporal.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/situacao-pocos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| Licença | Não informada especificamente para este conjunto nos metadados da ANP; o rodapé do portal da ANP declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal, segundo o metadado da ANP; cada arquivo é um retrato do cadastro, sem histórico (o da coleta de 2026-11-15 traz atualizações até 20/10/2026) |
| Cobertura | 1939 a em-curso |
| Unidade (uma linha) | um poço perfurado, com a situação e as datas do ciclo de vida do poço |
| Granularidade | espacial: poço (nome ANP), com campo, bacia, estado, ambiente e coordenadas da base; temporal: sem série temporal: datas de perfuração (a partir de 30/09/1939), de operação e da situação (referência até 14/10/2026) |
| Formato bruto | CSV em UTF-8 com BOM, separado por vírgula; datas em DD/MM/AAAA e MM/AAAA |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 24 |
| Unidades de medida | — |
| Dados pessoais | `Operador_atual` (nome fantasia de empresa operadora (pessoa jurídica)) |
| Eras | 2026: layout da coleta de 2026-11-15 (24 colunas), o mesmo descrito no metadado de junho de 2026; só a versão corrente do arquivo é guardada |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- Um CSV: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-pocos/situacao-pocos-1939-2026.csv`, com 6.427.093 bytes na coleta de 2026-11-15. O nome do arquivo no catálogo traz o intervalo `1939-2026`, que pode mudar a cada ano.
- Fonte do dado, segundo o metadado "Situação Poços" (DOCX, criado em junho de 2026): ANP/SDP (Superintendência de Desenvolvimento e Produção), a partir do SIGEP e do Do Poço ao Posto, em Power BI; atualização mensal; contato demandas_sdp@anp.gov.br.
- No bruto: `situacao-pocos/situacao-pocos@AAAAMMDD.csv`, com o sufixo da data da coleta (o servidor não informa a data de modificação).

## Conteúdo

- **27.334 linhas na amostra** (todas as linhas do arquivo): 21.557 poços em terra e 5.777 em mar; os estados com mais poços são Rio Grande do Norte (8.038), Bahia (6.597), Sergipe (4.538), Rio de Janeiro (3.637) e Espírito Santo (1.974), em 13 estados.
- **Situação.** 23 valores; os mais frequentes são `FECHADO` (6.250), `PRODUZINDO` (6.131), `ABANDONADO TEMPORARIAMENTE COM MONITORAMENTO` (4.664), `ABANDONADO PERMANENTEMENTE` (4.522), `ARRASADO` (2.565) e `INJETANDO` (1.817); 152 linhas não têm situação.
- **Datas.** A perfuração mais antiga começa em 30/09/1939 e a mais recente em 18/10/2026; a última referência de situação é 14/10/2026 e a última atualização, 20/10/2026. As datas de operação, produção e injeção vêm só como mês e ano (MM/AAAA).

Arquivos do lake por ano (conferido em amostra convertida pelo conversor atual, 2026-11-15):

| Ano | Arquivos (colunas) |
|---|---|
| — | `situacao-pocos` (24) |

## Variáveis

As descrições vêm do metadado "Situação Poços" da ANP (DOCX, criado em junho de 2026); as contagens e os formatos vêm da amostra do lake. O metadado diz que a coluna de latitude e longitude está em "grau, minuto e segundo" e lista as datas como `Data (DD/MM/AAAA)` ou `Data (MM/AAAA)`; no lake tudo é texto.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `Nome_poço_anp` | `Nome_poço_anp` | texto | Nome do poço atribuído conforme a Resolução ANP nº 699/2017; vazio em 109 linhas da amostra, de campos como `CEXIS` e `DOM JOÃO` (sem poço cadastrado). | — | — |
| `Campo` | `Campo` | texto | Nome do campo de que o poço faz parte; poços sem campo trazem `ÁREA DO <sigla>` ou outro nome de área. | — | — |
| `Bacia` | `Bacia` | texto | Nome da bacia sedimentar onde o poço foi perfurado (maiúsculas). | — | — |
| `Operador_atual` | `Operador_atual` | texto | Empresa operadora do poço atualmente (nome fantasia). | — | — |
| `Data_início_perfuração` | `Data_início_perfuração` | texto | Data de início da perfuração (DD/MM/AAAA, texto; vazia em 108 linhas). | — | — |
| `Data_término_perfuração` | `Data_término_perfuração` | texto | Data de término da perfuração, segundo a definição da Resolução ANP nº 699/2017 (DD/MM/AAAA). | — | — |
| `Data_conclusão_poço` | `Data_conclusão_poço` | texto | Data da conclusão do poço, segundo a definição da Resolução ANP nº 699/2017 (DD/MM/AAAA). | — | — |
| `Data_início_operação_(mês/ano)` | `Data_início_operação_(mês/ano)` | texto | Mês e ano do início da operação (produção ou injeção) do poço (MM/AAAA). | — | — |
| `Data_última_operação_(mês/ano)` | `Data_última_operação_(mês/ano)` | texto | Mês e ano da última operação (produção ou injeção) do poço (MM/AAAA). | — | — |
| `Data_início_produção_(mês/ano)` | `Data_início_produção_(mês/ano)` | texto | Mês e ano do início da produção do poço (MM/AAAA). | — | — |
| `Data_última_produçaõ_(mês/ano)` | `Data_última_produçaõ_(mês/ano)` | texto | Mês e ano da última produção do poço (MM/AAAA); o nome da coluna traz o erro de grafia `produçaõ`, do arquivo da ANP (o metadado escreve `produção`). | — | — |
| `Data_início_injeção_(mês/ano)` | `Data_início_injeção_(mês/ano)` | texto | Mês e ano do início da injeção do poço (MM/AAAA). | — | — |
| `Data_última_injeção_(mês/ano)` | `Data_última_injeção_(mês/ano)` | texto | Mês e ano da última injeção do poço (MM/AAAA). | — | — |
| `Em_operação_(produção_ou_injeção)` | `Em_operação_(produção_ou_injeção)` | texto | Indicador de que o poço está em operação (`SIM` ou `NÃO`). | — | — |
| `Ambiente` | `Ambiente` | texto | Ambiente geográfico onde o poço se localiza: `TERRA` ou `MAR`. | — | — |
| `Latitude_da_base` | `Latitude_da_base` | texto | Latitude da base do poço, em graus, minutos e segundos no formato `-GG:MM:SS,SSS` (texto, com sinal `+` ou `-`; vazia em 140 linhas). | — | — |
| `Longitude_da_base` | `Longitude_da_base` | texto | Longitude da base do poço, no mesmo formato da latitude. | — | — |
| `Estado` | `Estado` | texto | Estado da Federação onde o poço se localiza (nome por extenso, em maiúsculas). | — | — |
| `Data_de_referência_situação` | `Data_de_referência_situação` | texto | Data de referência da situação do poço (DD/MM/AAAA). | — | — |
| `Data_atualização_da_situação` | `Data_atualização_da_situação` | texto | Data da atualização da situação do poço (DD/MM/AAAA). | — | — |
| `Situação_do_poço` | `Situação_do_poço` | texto | Situação do poço, segundo o domínio da Resolução ANP nº 699/2017: `FECHADO`, `PRODUZINDO`, `ABANDONADO TEMPORARIAMENTE COM MONITORAMENTO`, `ABANDONADO PERMANENTEMENTE`, `ARRASADO`, `INJETANDO`, `DEVOLVIDO` e outros 15 valores; vazia em 152 linhas. | — | — |
| `Método_de_elevação` | `Método_de_elevação` | texto | Método de elevação atual do poço, como `SEM MÉTODO DE ELEVAÇÃO`, `BOMBEIO MECÂNICO`, `SURGENTE`, `BOMBEIO CENTRÍFUGO SUBMERSO` e `GAS LIFT CONTÍNUO` (15 valores). | — | — |
| `Última_intervenção` | `Última_intervenção` | texto | Natureza da última intervenção no poço: `Restauração`, `Completação`, `Abandono`, `Perfuração` ou `Avaliação`; vazia na maioria das linhas (24.808). | — | — |
| `Data_última_intervenção` | `Data_última_intervenção` | texto | Data de término da última intervenção no poço (DD/MM/AAAA). | — | — |

## No lake

- Dataset `anp/situacao-pocos`, sem partição: um Parquet, `situacao-pocos.parquet`.
- Todas as colunas são texto. Valores faltantes vêm como texto vazio (`''`), não como nulo, exceto em `Nome_poço_anp`, `Operador_atual` e nas coordenadas, que vêm nulos. Os nomes das colunas são os da fonte (acentos, parênteses e `_`).

## Cuidados de uso

- **Vazio como texto.** Datas e situação ausentes são `''` (por exemplo, 108 linhas sem data de início de perfuração e 152 sem situação); converta com `NULLIF(col, '')` antes de aplicar `strptime`.
- **Dois formatos de data.** `DD/MM/AAAA` nas datas de perfuração, conclusão, referência e intervenção, e `MM/AAAA` nas de operação, produção e injeção; o ano mais recente nas colunas `(mês/ano)` ordenadas como texto engana (`09/2026` vem antes de `12/2025`), então converta antes de ordenar.
- **Nome do poço ausente.** 109 linhas não têm `Nome_poço_anp` (nulo); entre as demais, o nome é único (27.225 nomes distintos), mas a chave do dataset fica vazia por causa das linhas sem nome.
- **Coordenadas em texto, nem sempre presentes.** `-18:22:40,186` (graus:minutos:segundos, vírgula decimal nos segundos); 140 linhas sem coordenada e 15 com latitude positiva.
- **`Em_operação` e situação não coincidem sempre.** 738 poços `FECHADO` estão com `Em_operação` igual a `SIM`, e 32 `PRODUZINDO`, com `NÃO`: os dois campos vêm de datas e eventos diferentes.
- **Nome de coluna com erro.** A coluna da última produção se chama `Data_última_produçaõ_(mês/ano)` no arquivo e no lake (o metadado escreve `produção`).
- **Retrato sem histórico.** Cada coleta substitui a anterior; mudanças de situação ao longo do tempo só podem ser reconstruídas guardando coletas sucessivas do bruto.
- **Dados pessoais.** Não há: poços, campos e operadoras.

## Exemplos

Poços por situação e ambiente, restritos aos que estão produzindo ou injetando, com a data mais recente de última produção convertida para data:

```python
import duckdb

duckdb.sql("""
    SELECT "Ambiente", "Situação_do_poço" AS situacao, count(*) AS pocos,
           max(strptime('01/' || NULLIF("Data_última_produçaõ_(mês/ano)", ''), '%d/%m/%Y')) AS ultima_producao
    FROM read_parquet('lake/anp/situacao-pocos/situacao-pocos.parquet')
    WHERE "Situação_do_poço" IN ('PRODUZINDO', 'INJETANDO')
    GROUP BY ALL
    ORDER BY ALL
""").show()
```

## Referências

- Fase de desenvolvimento e produção (dados abertos), informações sobre poços: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao
- Metadado "Situação Poços" (DOCX): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-fase-de-desenvolvimento-e-producao/informacoes-sobre-pocos/metadado-situacao-de-poco.docx
