# Plano de Expansão: anp-fetcher Fase 3

> Este plano cobre a integração dos conjuntos de dados descobertos na exploração de 2026-06-29.
> Ver [datasets-anp-descobertos.md](datasets-anp-descobertos.md) para o relatório completo.
>
> **Estado atual (Fase 2):** 13 grupos, 385 datasets, suporte a partições estáticas/anuais/semestrais/mensais.

---

## Visão geral

A Fase 3 adiciona **três ondas** de grupos novos, ordenadas por complexidade de implementação:

| Onda | Grupos | Arquivos estimados | Foco |
|---|---|---|---|
| **3a** | 15 grupos estáticos ou anuais simples | ~100 arquivos | Alta prioridade, baixa complexidade |
| **3b** | 4 grupos mensais ou ZIP | ~210 arquivos | Média complexidade, URLs irregulares |
| **3c** | 2 grupos de grande volume | ~670 arquivos | Alto valor, requer mapeamento prévio |

A arquitetura não precisa mudar — os novos grupos usam exatamente os mesmos mecanismos já existentes (`_static`, `_annual`, `_sem_entry`, `_mon_entry`, `DatasetEntry`, `storage.py`).

---

## Onda 3a — Grupos estáticos e anuais (implementação imediata)

Todos os grupos desta onda são compostos por arquivos estáticos ou séries anuais com padrão de URL regular. A implementação segue exatamente o mesmo padrão do `catalog_dados_abertos.py` atual.

### Novos grupos

| ID | Nome | Arquivos | Padrão |
|---|---|---|---|
| `producao-el` | Produção de Petróleo e Gás por Estado e Localização | 7 CSVs | Estático |
| `pb-abertos` | Produção de Biocombustíveis (dados abertos) | 3 CSVs | Estático |
| `ie-abertos` | Importações e Exportações (dados abertos) | 4 CSVs | Estático |
| `comercializacao-gn` | Comercialização de Gás Natural | 3 CSVs | Estático |
| `movimentacao-terminais` | Movimentação dos Terminais Aquaviários | 1 CSV | Estático |
| `armazenagem-terminais` | Capacidade de Armazenagem de Terminais | 1 CSV | Estático |
| `incidentes` | Incidentes de Segurança Operacional | 5 CSVs | Estático |
| `rodadas` | Rodadas de Licitações | 3 CSVs | Estático |
| `concessionarios` | Relação de Concessionários | 2 CSVs | Estático |
| `revendedores` | Cadastro Revendedores Varejistas | 1 CSV | Estático |
| `revendas-glp` | Cadastro Revendas de GLP | 1 CSV | Estático |
| `registro-lubrificantes` | Registro de Óleos e Graxas Lubrificantes | 1 CSV | Estático |
| `pml` | PML — Monitoramento de Lubrificantes | 1 CSV | Estático |
| `fiscalizacao` | Ações de Fiscalização do Abastecimento | 2 XLSXs | Estático |
| `royalties` | Participações Governamentais | 62 CSVs | Anual (2009–2025) + 4 estáticos |

**Total Onda 3a:** ~90 arquivos adicionais.

### Implementação

**Passo 1: Confirmar URLs exatos antes de codificar**

Para cada grupo, acessar a página listada em `datasets-anp-descobertos.md` e confirmar:
- URL base dos arquivos (pode mudar)
- Nome exato dos arquivos estáticos
- Para `royalties`: confirmar padrão `royalties-uniao-YYYY.csv` para todos os anos

**Passo 2: Criar `catalog_dados_abertos_3a.py`**

Novo sub-catálogo no mesmo padrão de `catalog_dados_abertos.py`:

```python
# src/anp_fetcher/catalog_dados_abertos_3a.py
from ._catalog_base import DatasetEntry, GroupInfo, _static, _annual

_SOURCE = "dados-abertos"
_BASE = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos"

# ... entradas para cada grupo ...

GROUPS_DA_3A: dict[str, GroupInfo] = {
    "producao-el":            GroupInfo(name="...", entries=_producao_el_entries),
    "pb-abertos":             GroupInfo(name="...", entries=_pb_abertos_entries),
    "ie-abertos":             GroupInfo(name="...", entries=_ie_abertos_entries),
    "comercializacao-gn":     GroupInfo(name="...", entries=_com_gn_entries),
    "movimentacao-terminais": GroupInfo(name="...", entries=_mov_term_entries),
    "armazenagem-terminais":  GroupInfo(name="...", entries=_arm_term_entries),
    "incidentes":             GroupInfo(name="...", entries=_incidentes_entries),
    "rodadas":                GroupInfo(name="...", entries=_rodadas_entries),
    "concessionarios":        GroupInfo(name="...", entries=_concession_entries),
    "revendedores":           GroupInfo(name="...", entries=_revendedores_entries),
    "revendas-glp":           GroupInfo(name="...", entries=_revendas_glp_entries),
    "registro-lubrificantes": GroupInfo(name="...", entries=_reg_lub_entries),
    "pml":                    GroupInfo(name="...", entries=_pml_entries),
    "fiscalizacao":           GroupInfo(name="...", entries=_fiscalizacao_entries),
    "royalties":              GroupInfo(name="...", entries=_royalties_entries),
}

GROUP_ALIASES_DA_3A: dict[str, str] = {
    "producao-estado":          "producao-el",
    "participacoes-gov":        "royalties",
    "importacoes-exportacoes-csv": "ie-abertos",
}
```

**Passo 3: Adicionar novos `_GROUP_DIRS` em `storage.py`**

```python
# Onda 3a
"producao-el":            "producao-estado-localizacao",
"pb-abertos":             "producao-biocombustiveis-abertos",
"ie-abertos":             "importacoes-exportacoes-abertos",
"comercializacao-gn":     "comercializacao-gas-natural",
"movimentacao-terminais": "movimentacao-terminais",
"armazenagem-terminais":  "armazenagem-terminais",
"incidentes":             "incidentes-operacionais",
"rodadas":                "rodadas-licitacoes",
"concessionarios":        "concessionarios",
"revendedores":           "revendedores-varejistas",
"revendas-glp":           "revendas-glp",
"registro-lubrificantes": "registro-lubrificantes",
"pml":                    "pml",
"fiscalizacao":           "fiscalizacao-abastecimento",
"royalties":              "participacoes-governamentais",
```

**Passo 4: Atualizar `catalog.py`**

```python
from .catalog_dados_abertos_3a import GROUP_ALIASES_DA_3A, GROUPS_DA_3A

GROUPS: dict[str, GroupInfo] = {**GROUPS_DE, **GROUPS_DA, **GROUPS_DA_3A}
GROUP_ALIASES: dict[str, str] = {**GROUP_ALIASES_DE, **GROUP_ALIASES_DA, **GROUP_ALIASES_DA_3A}
```

**Passo 5: Atualizar `plugin.py` e `cli.py`**

Adicionar macro-alias `royalties` no help (é o único grupo 3a com múltiplos arquivos que pode confundir).

**Passo 6: Testes**

Para cada grupo novo, adicionar em `test_catalog.py`:
- `test_{group}_count()` — verifica quantidade de entradas
- `test_{group}_all_csv()` / `test_{group}_all_xlsx()` — verifica extensão
- Para `royalties`: `test_royalties_anual_pattern()` — verifica anos cobertos

Para `test_storage.py`:
- `test_path_for_{group}()` — verifica subdiretório correto para pelo menos 1 grupo novo

Para `test_download.py`:
- `test_download_all_{group}_dry_run()` — verifica contagem em dry-run para grupos principais

---

## Onda 3b — Grupos mensais e ZIPs (complexidade média)

### Movimentação de Gás Natural em Gasodutos (`movimentacao-gn`)

**Arquivos:** ~63 CSVs mensais (jan/2021–mar/2026)  
**Base URL:** `.../arquivos/arquivos-movimentacao-de-gas-natural-em-gasodutos-de-transporte/YYYY/`  
**Padrão de arquivo:** `gn_MM_YYYY.csv`

**Implementação:**

```python
_MOVGN_BASE = f"{_BASE}/arquivos-movimentacao-de-gas-natural-em-gasodutos-de-transporte"
_MOVGN_DATES = (
    [(y, m) for y in (2021, 2022, 2023, 2024, 2025) for m in range(1, 13)]
    + [(2026, m) for m in range(1, 4)]  # atualizar quando novos meses surgirem
)

for _y, _m in _MOVGN_DATES:
    url = f"{_MOVGN_BASE}/{_y}/gn_{_m:02d}_{_y}.csv"
    # _mon_entry("movimentacao-gn", "movimentacao-gn", "Mov. gás natural em gasodutos", _y, _m, url, "csv")
```

**Nota:** verificar se jan/2021 é o primeiro mês disponível ou se a série começa antes.

---

### Tancagem do Abastecimento Nacional (`tancagem`)

**Arquivos:** ~40 CSVs mensais (jun/2022–abr/2026)  
**Base URL:** `.../arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/YYYY/`  
**Complicação:** nomes de arquivo em português por extenso e alguns meses com arquivo bimestral/trimestral.

**Implementação:** enumeração explícita de todas as entradas (como SHPC), sem template. Confirmar URLs exatos via WebFetch antes de codificar — verificar se há meses faltantes, quais são bimestrais, e se os nomes de arquivo variam por ano.

```python
# Exemplo de entrada manual:
_tancagem_entries = [
    _mon_entry("tancagem", "tancagem", "Tancagem do abastecimento", 2026, 4,
               f"{_TANC_BASE}/2026/abril.csv", "csv"),
    _mon_entry("tancagem", "tancagem", "Tancagem do abastecimento", 2026, 3,
               f"{_TANC_BASE}/2026/marco.csv", "csv"),
    # ... continuar para todos os meses disponíveis ...
]
```

**Ação prévia necessária:** acessar `.../YYYY/` para os anos 2022–2026 e listar todos os arquivos disponíveis antes de implementar.

---

### PMQC — Qualidade de Combustíveis (`pmqc`)

**Arquivos:** ~96 arquivos mensais (jan/2016–abr/2026), CSV e JSON  
**Complicação:** padrão de URL não completamente mapeado na exploração inicial.

**Ação prévia necessária:** acessar a página do PMQC e explorar a estrutura de arquivos para confirmar:
- Padrão de URL por ano/mês
- Se há um produto único por arquivo ou arquivos separados por produto (gasolina, diesel, etanol)
- Se JSON e CSV têm o mesmo conteúdo ou complementar

Após mapeamento, implementar como série mensal com possível filtro por produto.

---

### Movimentação de Derivados de Petróleo (`movimentacao-derivados`)

**Arquivos:** 8–9 ZIPs  
**Base URL:** `.../arquivos/mdpg/`  
**Complicação:** cada ZIP contém um ou mais CSVs internos. O storage atual lida com ZIPs como arquivo único (não extrai). Decisão de design necessária:

**Opção A:** tratar cada ZIP como um arquivo único (comportamento atual). Simples, mas o usuário precisa extrair manualmente.  
**Opção B:** adicionar extração automática de ZIP no `download.py` para este grupo. Requer lógica adicional.

**Recomendação:** Opção A por ora — manter consistência com os ZIPs existentes (ex.: `producao-poco`). Se houver demanda, adicionar extração em versão posterior.

```python
_MDPG_BASE = f"{_BASE}/mdpg"
_movimentacao_derivados_entries = [
    _static("movimentacao-derivados", _SOURCE, "mdpg-asfalto",
            "Movimentação de asfalto", f"{_MDPG_BASE}/asfalto.zip", "zip"),
    _static("movimentacao-derivados", _SOURCE, "mdpg-aviacao",
            "Movimentação de combustível de aviação", f"{_MDPG_BASE}/aviacao.zip", "zip"),
    # ... confirmar nomes exatos dos ZIPs via WebFetch ...
]
```

**Ação prévia necessária:** acessar a página e confirmar nomes exatos dos arquivos ZIP.

---

### Produção por Poço — histórico 2005–2023 (`producao-poco-abertos`)

**Arquivos:** ~50 ZIPs  
**Complicação:** três padrões de URL por período — enumeração explícita necessária.

```python
# 2005–2020: anual
_poco_anuais = [
    _annual_entry("producao-poco-abertos", "producao-poco-da", "Produção por poço",
                  f"{_POCOS_BASE}/producao-por-poco-{year}.zip", year, "zip")
    for year in range(2005, 2021)
]

# 2022: mensais com padrão diferente
_poco_2022 = [
    _mon_entry("producao-poco-abertos", "producao-poco-da", "Produção por poço",
               2022, m, f"{_POCOS_BASE}/producao-2022-{m:02d}.zip", "zip")
    for m in range(1, 13)
]

# 2023: mensais com padrão ainda diferente
_poco_2023 = [
    _mon_entry("producao-poco-abertos", "producao-poco-da", "Produção por poço",
               2023, m, f"{_POCOS_BASE}/producao-{m:02d}.zip", "zip")
    for m in range(1, 13)
]

# 2021: confirmar padrão via WebFetch antes de implementar
```

**Ação prévia necessária:** confirmar o padrão de URL de 2021 (12 arquivos mensais com formato a determinar).

---

## Onda 3c — Projetos maiores (requerem análise prévia)

### Fase de Desenvolvimento e Produção (`producao-fdp`)

**Volume:** ~170 CSVs  
**Complexidade:** Alta — duas séries independentes (mar e terra), cada uma com particionamento histórico + anual/trimestral.

**Antes de implementar:**
1. Acessar a página e mapear todos os arquivos disponíveis para mar e terra
2. Identificar os padrões de URL por período (histórico consolidado vs. anuais vs. trimestrais)
3. Verificar se os dados de mar/terra se sobrepõem com `producao-el` (produção por estado/localização)

**Estrutura esperada de grupos:**

```
"producao-fdp-mar"   — histórico consolidado + anuais/trimestrais mar
"producao-fdp-terra" — histórico consolidado + anuais/trimestrais terra
```

Ou um grupo único `producao-fdp` com subclassificação por `base_id`.

---

### Anuário Estatístico Brasileiro do Petróleo, Gás e Biocombustíveis (`anuario`)

**Volume:** ~500 CSVs (8 anuários × ~62 tabelas)  
**Complexidade:** Alta — escala e sobreposição de conteúdo.

**Antes de implementar:**
1. Acessar o anuário de 2025 e listar todas as ~62 tabelas com suas seções e URLs
2. Marcar quais tabelas têm equivalente nos dados abertos já implementados (produção, importações, royalties, SHPC)
3. Identificar as tabelas **exclusivas** do anuário — candidatas principais:
   - Panorama internacional de produção/reservas
   - Cotações históricas Brent/WTI
   - Reservas provadas do Brasil
   - Dados de refino comparados internacionalmente
4. Definir se implementar anuário completo ou apenas subset de tabelas exclusivas

**Modelo de implementação sugerido:**

```python
# Hierarquia: anuario-YYYY/secao-N/tabela-N-NN
_anuario_entries = [
    _static("anuario", _SOURCE, "anuario-2025-1-01",
            "Anuário 2025 — Tabela 1.01: Reservas mundiais de petróleo",
            f"{_ANU_BASE}/anuario-estatistico-2025/secao-1/tabela-1-01.csv", "csv"),
    # ... ~62 × 8 = ~500 entradas ...
]
```

**Alternativa:** um grupo por anuário (`anuario-2025`, `anuario-2024`, ...) para permitir sync por edição.

---

## Checklist de alterações por onda

### Onda 3a

- [ ] Confirmar URLs de todos os 15 grupos via WebFetch
- [ ] Criar `src/anp_fetcher/catalog_dados_abertos_3a.py`
- [ ] Atualizar `src/anp_fetcher/storage.py` — adicionar 15 entradas em `_GROUP_DIRS`
- [ ] Atualizar `src/anp_fetcher/catalog.py` — importar e mesclar `GROUPS_DA_3A`
- [ ] Atualizar `src/anp_fetcher/plugin.py` — help do `sync` atualizado
- [ ] Atualizar `src/anp_fetcher/cli.py` — help do `sync` atualizado
- [ ] Atualizar `tests/test_catalog.py` — testes de contagem e campos para grupos novos
- [ ] Atualizar `tests/test_storage.py` — testes de subdiretório para grupos novos
- [ ] Atualizar `tests/test_download.py` — dry-run para grupos principais novos
- [ ] `uv run pytest anp-fetcher/tests/ -v` — todos os testes passam

### Onda 3b

Para cada grupo (`movimentacao-gn`, `tancagem`, `pmqc`, `movimentacao-derivados`, `producao-poco-abertos`):

- [ ] Explorar URLs exatos com WebFetch antes de codificar
- [ ] Adicionar no `catalog_dados_abertos_3b.py` (novo arquivo ou append no 3a)
- [ ] Adicionar em `_GROUP_DIRS`
- [ ] Testes de contagem e dry-run
- [ ] `tancagem`: verificar e enumerar explicitamente todos os meses disponíveis
- [ ] `pmqc`: confirmar padrão de URL por produto/mês antes de implementar
- [ ] `producao-poco-abertos`: confirmar padrão de 2021 antes de codificar

### Onda 3c

- [ ] `producao-fdp`: mapear os ~170 CSVs com WebFetch e definir estrutura de grupos
- [ ] `anuario`: listar as ~62 tabelas de 2025, identificar exclusivas, definir escopo de implementação
- [ ] Implementar após aprovação do escopo

---

## Estimativa de tamanho final do catálogo

| Fase | Grupos | Datasets | Cumulativo |
|---|---|---|---|
| Fase 2 (atual) | 13 | 385 | 385 |
| + Onda 3a | +15 | +~90 | ~475 |
| + Onda 3b | +5 | +~210 | ~685 |
| + Onda 3c | +3–5 | +~670 | ~1.355 |

---

## Notas de manutenção futura

- **SHPC mensais:** a série vai até mai/2026. Quando novos meses forem publicados (tipicamente ~45 dias após o mês de referência), atualizar `_MONTHLY_DATES` em `catalog_dados_abertos.py` e os grupos `movimentacao-gn` e `tancagem` corresponidentemente.
- **Royalties:** novo arquivo anual por ano (ex.: `royalties-uniao-2026.csv`) — atualizar os ranges em `royalties`.
- **Dados cadastrais** (`revendedores`, `revendas-glp`, `registro-lubrificantes`): arquivos estáticos com conteúdo atualizado regularmente — sem necessidade de alterar o catálogo, apenas re-baixar.
- **`producao-poco-abertos` para 2024+:** a ANP migrou para o portal CDP interativo. Monitorar se reabre download direto; caso contrário, a série fica encerrada em dez/2023.
