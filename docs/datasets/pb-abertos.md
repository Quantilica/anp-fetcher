---
dataset:
  id: pb-abertos
  fonte: anp
  titulo: 'Produção de biocombustíveis (dados abertos): biodiesel e etanol'
  resumo: Produção mensal de biodiesel B100 por UF e produtor (2005 a 2023), por grande região (2024 em diante) e de etanol anidro e hidratado por UF (2012 a 2026), em m³.
  orgao: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
  pagina_oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis
  licenca: Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15).
  periodicidade: mensal; a página informa atualização até o último dia do mês seguinte (arquivos atualizados em 15/10/2026 e 28/10/2026, com dados até setembro de 2026)
  cobertura:
    inicio: 2005-01
    fim: 2026-09
  unidade: um produtor de biodiesel numa UF num mês (2005 a 2023); uma grande região num mês (biodiesel de 2024 em diante); ou um tipo de etanol numa UF num mês
  granularidade:
    espacial: UF (e produtor) ou grande região, conforme o arquivo
    temporal: mês (`ANO` e `MÊS`)
  formato_bruto: CSV com separador `;`, vírgula decimal e UTF-8 com BOM; três arquivos
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 7
  unidades_de_medida:
    PRODUÇÃO: m³
  dados_pessoais:
  - coluna: PRODUTOR
    categoria: nome de produtor de biodiesel (pessoa jurídica)
  eras:
  - desde: '2005'
    mudanca: biodiesel por UF e produtor de janeiro de 2005 a dezembro de 2023 (arquivo `producao-biodiesel-m3-2005-2023.csv`)
  - desde: '2012'
    mudanca: etanol anidro e hidratado por UF desde janeiro de 2012
  - desde: '2024'
    mudanca: biodiesel só por grande região (sem UF nem produtor), de janeiro de 2024 em diante, no arquivo `producao-biodiesel-m3-2024-2026.csv`; nele o mês vem por extenso (`Janeiro`) e não abreviado (`JAN`)
  revisado_em: '2026-11-15'
  versao_fetcher: 2.10.0
---

# Produção de biocombustíveis (dados abertos): biodiesel e etanol

## Resumo

Três arquivos CSV da ANP com a produção de biocombustíveis em m³: biodiesel B100 por UF e produtor de 2005 a 2023, biodiesel B100 por grande região de 2024 a 2026 e etanol anidro e hidratado por UF de 2012 a 2026. A mudança do recorte do biodiesel em 2024 acompanha a decisão da ANP de deixar de divulgar a produção por produtor depois do fim dos leilões de comercialização. Os totais, em planilha com meses nas linhas, estão no grupo `pb`.

## Ficha técnica

<!-- gerado:ficha -->

| Campo | Valor |
|---|---|
| Dataset | `anp/pb-abertos` |
| Órgão | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Página oficial | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis |
| Licença | Não informada especificamente para este conjunto; o rodapé do portal gov.br/anp declara que todo o conteúdo do site está publicado sob a licença Creative Commons Atribuição-SemDerivações 3.0 Não Adaptada (conferido em 2026-11-15). |
| Periodicidade | mensal; a página informa atualização até o último dia do mês seguinte (arquivos atualizados em 15/10/2026 e 28/10/2026, com dados até setembro de 2026) |
| Cobertura | 2005-01 a 2026-09 |
| Unidade (uma linha) | um produtor de biodiesel numa UF num mês (2005 a 2023); uma grande região num mês (biodiesel de 2024 em diante); ou um tipo de etanol numa UF num mês |
| Granularidade | espacial: UF (e produtor) ou grande região, conforme o arquivo; temporal: mês (`ANO` e `MÊS`) |
| Formato bruto | CSV com separador `;`, vírgula decimal e UTF-8 com BOM; três arquivos |
| Estado no lake | convertido |
| Partições | — |
| Chave | — |
| Colunas | 7 |
| Unidades de medida | `PRODUÇÃO`: m³ |
| Dados pessoais | `PRODUTOR` (nome de produtor de biodiesel (pessoa jurídica)) |
| Eras | 2005: biodiesel por UF e produtor de janeiro de 2005 a dezembro de 2023 (arquivo `producao-biodiesel-m3-2005-2023.csv`); 2012: etanol anidro e hidratado por UF desde janeiro de 2012; 2024: biodiesel só por grande região (sem UF nem produtor), de janeiro de 2024 em diante, no arquivo `producao-biodiesel-m3-2024-2026.csv`; nele o mês vem por extenso (`Janeiro`) e não abreviado (`JAN`) |
| Revisado em | 2026-11-15 |
| Versão do fetcher | 2.10.0 |

## Origem e coleta

- O fetcher baixa três CSV de `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-biocombustiveis/`: `producao-biodiesel-m3-2005-2023.csv` (atualizado em 15/10/2026), `producao-biodiesel-m3-2024-2026.csv` (28/10/2026) e `producao-etanol-anidro-hidratado-m3-2012-2026.csv` (28/10/2026).
- Metadados em PDF: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-biocombustiveis/metadados-biodiesel.pdf` (por UF e produtor), `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-biocombustiveis/metadados-prod-biodiesel-grande-regiao.pdf` (por região) e `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-biocombustiveis/metadados-producao-etanol.pdf`.
- Fonte do dado, segundo os metadados: ANP, conforme a Resolução ANP nº 729/2018; biodiesel B100 conforme a Resolução ANP nº 45/2014; produtores são unidades produtoras autorizadas pela ANP. Órgão responsável: Superintendência de Defesa da Concorrência (ANP/SDC).
- Nota dos metadados sobre a mudança de recorte: até dezembro de 2021, a produção de biodiesel era divulgada por instalação produtora, quando a comercialização ocorria em leilões da ANP; desde 2022 a venda é direta entre produtores e distribuidores (Resolução CNPE nº 14/2020 e Resolução ANP nº 857/2021), e a produção passou a ser divulgada, em regra, só por região, porque em quase todas as regiões há estados com menos de três produtores no mês. O CSV de 2005 a 2023 traz produtor e UF até dezembro de 2023; o de 2024 em diante, só região.
- Os metadados de biodiesel avisam que as informações são preliminares e podem ser ajustadas.

## Conteúdo

- **`pba-biodiesel-2005-2023`**: 23.864 linhas, de 2005-01 a 2023-12, uma por mês, UF e produtor (105 produtores em 17 UFs); 16.376 linhas têm produção zero. A soma de 2023 (7.532.436 m³) é a mesma da planilha de totais do grupo `pb`.
- **`pba-biodiesel-2024-2026`**: 165 linhas, de 2024-01 a 2026-09, uma por mês e grande região (33 meses × 5 regiões); produção de 9,05 milhões de m³ em 2024, 9,84 milhões em 2025 e 7,75 milhões de janeiro a setembro de 2026.
- **`pba-etanol`**: 9.558 linhas, de 2012-01 a 2026-09 (177 meses × 27 UFs × 2 tipos de etanol), grade completa; 4.404 linhas têm produção zero (UF sem produção do tipo no mês). A soma de 2024 (36.961.311 m³) é a mesma da planilha de totais do grupo `pb`.
- **Chave.** Em cada arquivo as combinações (`ANO`, `MÊS`, UF e produtor; `ANO`, `MÊS` e região; `ANO`, `MÊS`, UF e produto) não se repetem na amostra; como as colunas diferem, a chave do conjunto não é declarada.

## Variáveis

As descrições vêm dos metadados da ANP (um PDF por arquivo). `ANO` e `MÊS` são texto; `PRODUÇÃO` é decimal (a vírgula decimal é convertida).
As colunas `UNIDADE DA FEDERAÇÃO`, `PRODUTOR` e `PRODUTO` não existem no arquivo de biodiesel de 2024 em diante (veja a coluna Arquivos).

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período | Arquivos |
|---|---|---|---|---|---|---|
| `ANO` | `ANO` | texto | Ano de referência, com quatro dígitos | — | — | `pba-biodiesel`, `pba-etanol` |
| `MÊS` | `MÊS` | texto | Mês de referência: abreviado em três letras maiúsculas (`JAN` a `DEZ`) nos arquivos de biodiesel de 2005 a 2023 e de etanol; por extenso (`Janeiro` a `Dezembro`) no de biodiesel de 2024 a 2026 | JAN = janeiro; FEV = fevereiro; MAR = março; ABR = abril; MAI = maio; JUN = junho; JUL = julho; AGO = agosto; SET = setembro; OUT = outubro; NOV = novembro; DEZ = dezembro | — | `pba-biodiesel`, `pba-etanol` |
| `GRANDE REGIÃO` | `GRANDE REGIÃO` | texto | Grande região do Brasil; no arquivo de etanol a grafia é `REGIÃO CENTRO OESTE` (sem hífen) | REGIÃO CENTRO-OESTE = Centro-Oeste; REGIÃO NORDESTE = Nordeste; REGIÃO NORTE = Norte; REGIÃO SUDESTE = Sudeste; REGIÃO SUL = Sul | — | `pba-biodiesel`, `pba-etanol` |
| `UNIDADE DA FEDERAÇÃO` | `UNIDADE DA FEDERAÇÃO` | texto | Nome da unidade da federação do produtor (por exemplo `BAHIA`, `SÃO PAULO`), em maiúsculas; no arquivo de biodiesel de 2005 a 2023 só aparecem as 17 UFs com produção | — | — | `pba-biodiesel`, `pba-etanol` |
| `PRODUTOR` | `PRODUTOR` | texto | Nome do produtor de biodiesel (B100): unidade produtora autorizada pela ANP, em maiúsculas, em geral com a marca ou a planta e, às vezes, o nome anterior entre parênteses (por exemplo `JBS (EX-BRACOL EX-BERTIN)`) | — | — | `pba-biodiesel` |
| `PRODUTO` | `PRODUTO` | texto | Produto: `BIODIESEL` (arquivo de biodiesel) ou o tipo de etanol (arquivo de etanol) | BIODIESEL = biodiesel B100; ANIDRO = etanol anidro; HIDRATADO = etanol hidratado | — | `pba-biodiesel`, `pba-etanol` |
| `PRODUÇÃO` | `PRODUÇÃO` | decimal | Volume produzido no mês, em m³ | — | — | `pba-biodiesel`, `pba-etanol` |

## No lake

- Dataset `anp/pb-abertos`, sem partições; um Parquet por arquivo da fonte (`pba-biodiesel-2005-2023.parquet`, `pba-biodiesel-2024-2026.parquet`, `pba-etanol.parquet`).
- O lake guarda o conteúdo como está na fonte, sem juntar os dois arquivos de biodiesel.

## Cuidados de uso

- **Dois recortes de biodiesel.** Para uma série contínua de biodiesel por região de 2005 a 2026, agregue o arquivo antigo por `GRANDE REGIÃO` e junte com o novo; o antigo tem UF e produtor, o novo não.
- **Grafias diferentes.** `MÊS` abreviado (`JAN`) nos arquivos de 2005 a 2023 e de etanol, por extenso (`Janeiro`) no biodiesel de 2024 em diante; `GRANDE REGIÃO` é `REGIÃO CENTRO-OESTE` no biodiesel e `REGIÃO CENTRO OESTE` no etanol.
- **Zeros não são lacunas.** As grades são completas: um produtor ou UF sem produção no mês aparece com `PRODUÇÃO` zero (dois terços das linhas de biodiesel de 2005 a 2023).
- **Nomes de produtores mudam.** O texto de `PRODUTOR` carrega marcas e nomes anteriores entre parênteses (`OLEOPLAN NORDESTE (EX-V-BIODIESEL)`); não foi conferido se o mesmo produtor tem uma só grafia ao longo dos anos.
- **Dados preliminares.** A ANP avisa que os valores podem ser ajustados.
- **Dados pessoais.** `PRODUTOR` é nome de produtor de biodiesel (pessoa jurídica), dado público; não há dados de pessoas físicas.

## Exemplos

Produção anual de biodiesel (m³) por grande região, juntando os dois arquivos de biodiesel:

```python
import duckdb

duckdb.sql("""
    SELECT ANO, "GRANDE REGIÃO" AS regiao, sum("PRODUÇÃO") AS m3
    FROM (
        SELECT ANO, "GRANDE REGIÃO", "PRODUÇÃO" FROM read_parquet('lake/anp/pb-abertos/pba-biodiesel-2005-2023.parquet')
        UNION ALL
        SELECT ANO, "GRANDE REGIÃO", "PRODUÇÃO" FROM read_parquet('lake/anp/pb-abertos/pba-biodiesel-2024-2026.parquet')
    )
    WHERE ANO IN ('2022', '2023', '2024', '2025')
    GROUP BY ALL
    ORDER BY ANO, m3 DESC
""").show()
```

## Referências

- Página oficial: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis
- Metadados (PDF): https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-biocombustiveis/metadados-biodiesel.pdf, https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-biocombustiveis/metadados-prod-biodiesel-grande-regiao.pdf e https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-biocombustiveis/metadados-producao-etanol.pdf
- Grupo `pb`: totais mensais em planilha (dados estatísticos).
