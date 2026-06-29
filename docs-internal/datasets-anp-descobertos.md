# Conjuntos de dados da ANP — Relatório de Descoberta

> Exploração realizada em 2026-06-29. O site da ANP é fragmentado e não possui página central
> de dados. Este relatório cobre as seções `/dados-abertos`, `/dados-estatisticos`,
> publicações e outras áreas com arquivos para download direto.

**Já implementado no `anp-fetcher`:** `ie`, `pp`, `pb`, `ppg`, `vdpb` (dados estatísticos XLS)
e `shpc-ca`, `shpc-glp`, `shpc-diesel-gnv`, `shpc-gasolina-etanol`, `shpc-glp-mensal`,
`shpc-4s`, `vdpb-abertos`, `pp-abertos` (dados abertos CSV).

---

## Alta prioridade — implementação direta

### Produção por Estado e Localização
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-estado-e-localizacao  
**Base URL dos arquivos:** `.../arquivos/ppgn-el/`  
**Arquivos:** 7 CSVs estáticos, atualização mensal  
**Cobertura:** 1997–2026

| Arquivo | Descrição |
|---|---|
| `producao-petroleo-m3.csv` | Produção de petróleo (m³) |
| `producao-lgn-m3.csv` | Produção de LGN (m³) |
| `producao-gas-natural-1000m3.csv` | Produção de gás natural (mil m³) |
| `reinjecao-gn-1000m3.csv` | Reinjeção de gás natural (mil m³) |
| `queima-e-perda-gn-1000m3.csv` | Queima e perda de gás natural (mil m³) |
| `consumo-proprio-gn1000m3.csv` | Consumo próprio de gás natural (mil m³) |
| `gn-disponivel-1000m3.csv` | Gás natural disponível (mil m³) |

**Recomendação: ✅ Implementar.** Cobertura completa da cadeia de produção e balanço de gás natural desde 1997. Alta relevância analítica. Implementação trivial — idêntica ao `pp-abertos`.  
**Grupo proposto:** `producao-el`

---

### Participações Governamentais (Royalties)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/participacoes-governamentais  
**Base URL dos arquivos:** `.../arquivos/pg/`  
**Arquivos:** 62 CSVs, atualização anual

| Série | Padrão | Anos |
|---|---|---|
| Royalties — União | `royalties-uniao-YYYY.csv` | 2009–2025 (17 arquivos) |
| Royalties — Estados | `royalties-estado-YYYY.csv` | 2009–2025 (17 arquivos) |
| Royalties — Municípios | `royalties-municipio-YYYY.csv` | 2009–2025 (17 arquivos) |
| Participação Especial (4 dimensões) | `pe_*.csv` | 4 arquivos estáticos |
| Preço de Referência Gás Natural | `preco-referencia-gn-YYYY.csv` | 2010–2025 (16 arquivos) |
| Preço de Referência Petróleo | `preco-referencia-petroleo-YYYY.csv` | 2018–2025 (9 arquivos) |
| Preço Mínimo Petróleo (descontinuado) | `preco-minimo-YYYY.csv` | 2009–2017 (9 arquivos) |

**Recomendação: ✅ Implementar.** Dados fiscais de alta relevância para análise econômica do setor. Padrão de URL anual regular. Os preços de referência são insumo direto para cálculo de royalties.  
**Grupo proposto:** `royalties`

---

### Importações e Exportações (dados abertos CSV)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes  
**Arquivos:** 4 CSVs estáticos, atualização mensal, cobertura 2000–2025

| Arquivo | Base URL | Descrição |
|---|---|---|
| `importacoes-exportacoes-petroleo-2000-2025.csv` | `.../arquivos/ie/petroleo/` | Importações e exportações de petróleo |
| `importacao-gas-natural-2000-2025.csv` | `.../arquivos/ie/gn/` | Importação de gás natural |
| `importacoes-exportacoes-derivados-2000-2025.csv` | `.../arquivos/ie/derivados/` | Importações e exportações de derivados |
| `importacoes-exportacoes-etanol-2012-2025.csv` | `.../arquivos/ie/etanol/` | Importações e exportações de etanol |

**Recomendação: ✅ Implementar.** Versão muito mais granular que o grupo `ie` existente (XLS consolidado em apenas 2 arquivos). Distingue petróleo, gás, derivados e etanol.  
**Grupo proposto:** `ie-abertos`

---

### Produção de Biocombustíveis (dados abertos CSV)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis  
**Base URL:** `.../arquivos/arquivos-producao-de-biocombustiveis/`  
**Arquivos:** 3 CSVs estáticos, atualização mensal

| Arquivo | Cobertura |
|---|---|
| `producao-biodiesel-m3-2005-2023.csv` | Biodiesel 2005–2023 |
| `producao-biodiesel-m3-2024-2026.csv` | Biodiesel 2024–2026 |
| `producao-etanol-anidro-hidratado-m3-2012-2026.csv` | Etanol anidro + hidratado 2012–2026 |

**Recomendação: ✅ Implementar.** Complementa o grupo `pb` (XLS) com versão CSV de dados abertos de atualização mensal e cobertura histórica maior.  
**Grupo proposto:** `pb-abertos`

---

### Rodadas de Licitações de Petróleo e Gás Natural
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/rodadas-de-licitacoes-de-petroleo-e-gas-natural  
**Arquivos:** 3 CSVs estáticos (9ª–17ª rodadas)

| Arquivo | Descrição |
|---|---|
| `blocos-ofertados-rodadas.csv` | Todos os blocos ofertados nas rodadas |
| `ofertas-vencedoras-rodadas.csv` | Consórcios vencedores e condicionantes |
| `processos-cessao-contratos.csv` | Cesões de contratos entre empresas |

**Recomendação: ✅ Implementar.** Dado histórico único sobre os leilões de blocos exploratórios no Brasil — relevante para análise regulatória e estrutura de mercado E&P.  
**Grupo proposto:** `rodadas`

---

### Relação de Concessionários
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/relacao-de-concessionarios  
**Arquivos:** 2 CSVs estáticos, atualização irregular

| Arquivo | Descrição |
|---|---|
| `relacao-concessionarios.csv` | Contratos ativos com percentuais por empresa |
| `relacao-pais-origem-concessionarios.csv` | País de origem dos concessionários |

**Recomendação: ✅ Implementar.** Dado estrutural sobre quem opera os contratos de E&P. Dois arquivos estáticos, implementação trivial.  
**Grupo proposto:** `concessionarios`

---

### Incidentes de Segurança Operacional
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/incidentes-seguranca-operacional  
**Base URL:** `.../arquivos/issm/`  
**Arquivos:** 5 CSVs estáticos em modelo relacional, atualização irregular (última: mai/2026)

| Arquivo | Descrição |
|---|---|
| `incidentes.csv` | Tabela principal de incidentes |
| `incidentes-classificacao.csv` | Classificação dos incidentes (dimensão) |
| `incidentes-feridos.csv` | Feridos por incidente (dimensão) |
| `incidentes-substancias.csv` | Substâncias envolvidas (dimensão) |
| `incidentes-tipo.csv` | Tipos de incidente (dimensão) |

**Recomendação: ✅ Implementar.** Único dataset público sobre acidentes em operações de E&P. Modelo relacional (tabela fato + 4 dimensões).  
**Grupo proposto:** `incidentes`

---

### Ações de Fiscalização do Abastecimento
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acoes-de-fiscalizacao  
**Arquivos:** 2 XLSXs, atualização anual

| Arquivo | Cobertura |
|---|---|
| `dados-fisc-1998-2018.xlsx` | Histórico de autuações 1998–2018 |
| `dados-fisc-a-partir-2019.xlsx` | Autuações a partir de 2019 (atualizado jun/2026) |

**Recomendação: ✅ Implementar.** Autos de infração e autuações do abastecimento nacional, série histórica desde 1998. Apenas 2 arquivos XLSX.  
**Grupo proposto:** `fiscalizacao`

---

### Cadastro de Revendedores Varejistas de Combustíveis Automotivos
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos  
**Arquivos:** 1 CSV estático, atualização semanal  
`dados-cadastrais-revendedores-varejistas-combustiveis-automoveis.csv`

**Recomendação: ✅ Implementar.** Cadastro de todos os postos autorizados no Brasil — útil para análise espacial e de mercado varejista. Arquivo único.  
**Grupo proposto:** `revendedores`

---

### Cadastro de Revendas de GLP
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo  
**Arquivos:** 1 CSV estático, atualização mensal  
`cadastro-revendas-glp.csv`

**Recomendação: ✅ Implementar.** Análogo ao anterior para distribuidoras e revendas de GLP. Arquivo único.  
**Grupo proposto:** `revendas-glp`

---

### Registro de Óleos e Graxas Lubrificantes
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/registro-de-oleos-e-graxas-lubrificantes  
**Arquivos:** 1 CSV estático, atualização semanal  
`dados-abertos-registro-produtos.csv`

**Recomendação: ✅ Implementar.** Catálogo de todos os lubrificantes registrados no Brasil com especificações técnicas. Alta frequência de atualização.  
**Grupo proposto:** `registro-lubrificantes`

---

### PML — Programa de Monitoramento dos Lubrificantes
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/o-programa-de-monitoramento-dos-lubrificantes-pml  
**Arquivos:** 1 CSV estático, atualização semestral  
`dados-abertos-pml.csv`

**Recomendação: ✅ Implementar.** Resultados de qualidade de lubrificantes no mercado. Arquivo único, trivial.  
**Grupo proposto:** `pml`

---

### Capacidade de Armazenagem de Terminais
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais  
**Arquivos:** 2 arquivos (CSV + XLSX do mesmo dado), atualização anual

**Recomendação: ✅ Implementar.** Dado de infraestrutura de armazenagem — complementa a tancagem (estoques efetivos em uso). Apenas o CSV é necessário.  
**Grupo proposto:** `armazenagem-terminais`

---

### Movimentação dos Terminais Aquaviários
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/movimentacao-dos-terminais-aquaviarios  
**Arquivos:** 1 CSV estático, atualização mensal (desde set/2022)  
`dados-abertos-movimentacao-terminais-aquaviarios.csv`

**Recomendação: ✅ Implementar.** Fluxo de entrada e saída de derivados em terminais marítimos. Dado de supply chain sem equivalente em outras seções.  
**Grupo proposto:** `movimentacao-terminais`

---

### Comercialização de Gás Natural
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/comercializacao-de-gas-natural  
**Base URL:** `.../assuntos/gas-natural/comercializacao-de-gas/dados-abertos/`  
**Arquivos:** 3 CSVs estáticos, atualização mensal (última: jan/2026)

| Arquivo | Descrição |
|---|---|
| `distribuidoras-consumidores-livres.csv` | Vendas a distribuidoras e consumidores livres |
| `vendas-entre-produtores.csv` | Transações entre produtores |
| `vendas-aos-comercializadores.csv` | Vendas aos comercializadores |

**Recomendação: ✅ Implementar.** Preços médios ponderados por volume e segmento — dado exclusivo sobre o mercado de gás natural, sem equivalente em outras seções.  
**Grupo proposto:** `comercializacao-gn`

---

## Média prioridade — útil mas com complicações de implementação

### Movimentação de Gás Natural em Gasodutos de Transporte
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-consolidados-movimentacao-de-gas-natural-em-gasodutos-de-transporte  
**Base URL:** `.../arquivos/arquivos-movimentacao-de-gas-natural-em-gasodutos-de-transporte/YYYY/`  
**Arquivos:** ~63 CSVs mensais (jan/2021–mar/2026), padrão `gn_MM_YYYY.csv`  
**Complicação:** partição mensal por ano — padrão suportado pelo storage mas requer enumeração ou geração de datas.

**Recomendação: ✅ Implementar (próxima iteração).** Dado físico de fluxo em gasodutos — não disponível em nenhuma outra seção. Partição mensal já suportada pela infraestrutura.  
**Grupo proposto:** `movimentacao-gn` (mensal)

---

### Tancagem do Abastecimento Nacional de Combustíveis
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/tancagem-do-abastecimento-nacional-de-combustiveis  
**Base URL:** `.../arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/YYYY/`  
**Arquivos:** ~40 CSVs mensais (jun/2022–abr/2026)  
**Complicação:** nomes de arquivo em português por extenso (`janeiro.csv`, `fevereiro.csv`, `marco.csv`, etc.) e alguns meses com arquivo bimestral/trimestral em vez de mensal — exige enumeração explícita de URLs, similar ao SHPC.

**Recomendação: ✅ Implementar (próxima iteração).** Estoques físicos de combustíveis em armazenagem ativa — dado de segurança energética. Complicação de URL gerenciável com enumeração explícita.  
**Grupo proposto:** `tancagem` (mensal)

---

### PMQC — Programa de Monitoramento da Qualidade dos Combustíveis
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pmqc-programa-de-monitoramento-da-qualidade-dos-combustiveis  
**Arquivos:** ~96 arquivos mensais (jan/2016–abr/2026), formato CSV e JSON  
**Complicação:** padrão de URL não completamente documentado — requer exploração adicional para confirmar a estrutura exata por ano/mês/produto.

**Recomendação: ✅ Implementar (após mapeamento de URLs).** Único dataset com resultados laboratoriais de qualidade de gasolina, etanol e diesel em postos. Relevante para análise de conformidade técnica.  
**Grupo proposto:** `pmqc` (mensal)

---

### Movimentação de Derivados de Petróleo (distribuição física)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-movimentacao-de-derivados-de-petroleo  
**Base URL:** `.../arquivos/mdpg/`  
**Arquivos:** 8–9 ZIPs (cada ZIP contém um ou mais CSVs por produto)  
**Produtos:** asfalto, aviação, líquidos, GLP, lubrificantes, solventes, TRR, vendas diretas de etanol, logística  
**Complicação:** estrutura interna dos ZIPs precisa ser verificada (um ou vários CSVs por arquivo).

**Recomendação: ✅ Implementar (próxima iteração).** Dados de distribuição física por produto e distribuidor — complementam `vdpb` (totais de vendas) com o canal de distribuição.  
**Grupo proposto:** `movimentacao-derivados`

---

### Produção de Petróleo e Gás Natural por Poço (dados abertos, 2005–2023)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-poco  
**Arquivos:** ~50 ZIPs  
**Complicação:** três padrões de URL diferentes por período:
- 2005–2020: `producao-por-poco-YYYY.zip` (16 arquivos anuais)
- 2021: ZIPs mensais com padrão próprio a confirmar
- 2022: `producao-2022-MM.zip` (12 arquivos mensais)
- 2023: `producao-MM.zip` (12 arquivos mensais)
- 2024+: apenas via portal CDP interativo (sem download direto)

**Recomendação: ✅ Implementar série histórica disponível.** Dados microeconômicos por poço — extremamente valiosos mas requerem mapeamento manual de URLs por período. A lacuna de 2024+ é uma limitação da ANP.  
**Grupo proposto:** `producao-poco-abertos` (misto anual/mensal)

---

### Fase de Desenvolvimento e Produção (histórico 1941–2026)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao  
**Arquivos:** ~170 CSVs com duas séries separadas (mar e terra)  
**Complicação:** cada série tem particionamento diferente por período (histórico consolidado + anuais + trimestrais); dois padrões de URL distintos (mar/terra).

**Recomendação: ✅ Implementar (projeto maior).** Série mais longa disponível sobre produção no Brasil (desde 1941). Requer mapeamento detalhado de URLs antes de implementar.  
**Grupo proposto:** `producao-fdp` (misto anual/trimestral)

---

### Anuário Estatístico Brasileiro do Petróleo, Gás e Biocombustíveis (CSV)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/anuario-estatistico-brasileiro-do-petroleo-gas-natural-e-biocombustiveis  
**Arquivos:** ~500 CSVs (8 anuários, 2018–2025, ~62 tabelas por edição)  
**Base URL:** `.../arquivos/anuario-estatistico-YYYY/secao-N/`  
**Complicação:** maior volume de arquivos do site. Muitas tabelas se sobrepõem a dados disponíveis em outras seções (produção, importações, royalties), mas algumas são exclusivas: panorama internacional, reservas provadas comparadas, cotações Brent/WTI.

**Recomendação: ✅ Implementar seleção de tabelas (projeto maior).** Implementar apenas as tabelas com dados não disponíveis em outras seções (cotações internacionais, reservas mundiais). Requer mapeamento das ~62 tabelas × 8 anos para identificar sobreposições.  
**Grupo proposto:** `anuario` (anual, com sub-tabelas)

---

### Boletim Mensal da Produção de Petróleo e Gás Natural (XLS)
**URL:** https://www.gov.br/anp/pt-br/centrais-de-conteudo/publicacoes/boletins-anp/boletim-mensal-da-producao-de-petroleo-e-gas-natural  
**Arquivos:** ~100 XLS/XLSX mensais (2017–2026)  
**Complicação:** provável sobreposição de conteúdo com os dados abertos CSV já mapeados (produção por estado, por poço). Verificar antes de implementar se os XLS têm colunas adicionais não disponíveis em CSV.

**Recomendação: 🟡 Avaliar sobreposição antes de implementar.** Se os XLS contiverem dados exclusivos (ex.: breakdown por operadora não disponível nos CSVs abertos), vale implementar. Caso contrário, os CSVs de dados abertos são preferíveis.

---

## Não recomendados

| Dataset | URL | Razão |
|---|---|---|
| Fase de Exploração (blocos ativos) | `.../fase-exploracao` | ~180 CSVs mensais revisados retroativamente — alta volatilidade e difícil versionamento |
| Fiscalização de Conteúdo Local | `.../fiscalizacao-de-conteudo-local` | Nicho regulatório de E&P, baixa demanda analítica geral |
| Distribuidores de Combustíveis (cadastro) | `.../distribuidores-de-combustiveis-liquidos` | Dado de compliance operacional; menor valor quantitativo |
| Multas aplicadas (2016+) | `.../multas-aplicadas-com-vencimento-a-partir-de-2016` | Dado administrativo; formato misto irregular; valor analítico limitado |
| PD&I — Pesquisa e Desenvolvimento | `.../pesquisa-e-desenvolvimento-e-inovacao-pd-i` | Dado de obrigações contratuais, não analítico |
| Acervo de Dados Técnicos (subsolo) | `.../acervo-de-dados-tecnicos` | Dado geológico de nicho; não é série temporal |
| Pontos de Abastecimento Autorizados | portal SPA | Portal SPA sem download direto desde mai/2024 |
| Bacias Sedimentares (GIS) | `.../bacias-sedimentares` | Shapefiles geográficos — fora do escopo do fetcher |
| Dados de Poços (BDP) | portal BDP | Acesso por portal especializado, sem download direto |
| Amostras de Rochas e Fluidos | portal BDT | Acesso por sistema especializado BDT |
| Dados de Rodadas CDP | portal CDP | Apenas via portal interativo, sem arquivos para download |

---

## Resumo por prioridade

| Prioridade | Grupo | Arquivos | Atualização | Complexidade |
|---|---|---|---|---|
| 🥇 | `producao-el` | 7 CSVs | Mensal | Baixa |
| 🥇 | `royalties` | 62 CSVs | Anual | Baixa |
| 🥇 | `ie-abertos` | 4 CSVs | Mensal | Baixa |
| 🥇 | `pb-abertos` | 3 CSVs | Mensal | Baixa |
| 🥇 | `rodadas` | 3 CSVs | Estático | Baixa |
| 🥇 | `concessionarios` | 2 CSVs | Irregular | Baixa |
| 🥇 | `incidentes` | 5 CSVs | Irregular | Baixa |
| 🥇 | `fiscalizacao` | 2 XLSXs | Anual | Baixa |
| 🥇 | `revendedores` | 1 CSV | Semanal | Baixa |
| 🥇 | `revendas-glp` | 1 CSV | Mensal | Baixa |
| 🥇 | `registro-lubrificantes` | 1 CSV | Semanal | Baixa |
| 🥇 | `pml` | 1 CSV | Semestral | Baixa |
| 🥇 | `armazenagem-terminais` | 1 CSV | Anual | Baixa |
| 🥇 | `movimentacao-terminais` | 1 CSV | Mensal | Baixa |
| 🥇 | `comercializacao-gn` | 3 CSVs | Mensal | Baixa |
| 🥈 | `movimentacao-gn` | 63 CSVs mensais | Mensal | Média |
| 🥈 | `tancagem` | ~40 CSVs mensais | Mensal | Média (URLs irregulares) |
| 🥈 | `pmqc` | ~96 CSVs mensais | Mensal | Média (mapeamento de URLs pendente) |
| 🥈 | `movimentacao-derivados` | 8–9 ZIPs | Irregular | Média (ZIP+CSV interno) |
| 🥈 | `producao-poco-abertos` | ~50 ZIPs | Histórico | Média (3 padrões de URL) |
| 🥉 | `producao-fdp` | ~170 CSVs | Trimestral | Alta |
| 🥉 | `anuario` | ~500 CSVs | Anual | Alta |
| 🟡 | Boletim Mensal Produção | ~100 XLSXs | Mensal | Avaliar sobreposição primeiro |
