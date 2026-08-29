"""ANP Fase de Exploração catalog.

Dados mensais (CSV) da fase de exploração de contratos de E&P: blocos sob
contrato, declarações de comercialidade, PADs (concluídos/em andamento),
poços exploratórios, prorrogações de prazos e processos sancionadores.

Publicados em ``gov.br/anp/.../gcep/arquivos-fase-de-exploracao`` desde
2023-02. O mapeamento de URLs abaixo foi extraído do HTML real do portal
(2026-08-29) — a nomenclatura muda por grupo/mês (2023 usa nomes de mês,
2026 usa separadores e sufixos irregulares, há typos e links duplicados),
por isso é literal e não gerado por fórmula. Arquivos que apontam para o
dado errado (ex.: blocos-2023-03 aponta para poços) ficam de fora.
"""

from ._catalog_base import DatasetEntry, GroupInfo

_SOURCE = "dados-abertos"
_BASE = (
    "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/"
    "arquivos/gcep/arquivos-fase-de-exploracao"
)

# Mapeamento (group, year, month) -> caminho relativo sob _BASE.
_URLS: dict[tuple[str, int, int], str] = {
    (
        "blocos-contrato",
        2023,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/abril.csv",
    (
        "blocos-contrato",
        2023,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/maio.csv",
    (
        "blocos-contrato",
        2023,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/junho.csv",
    (
        "blocos-contrato",
        2023,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/julho.csv",
    (
        "blocos-contrato",
        2023,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/agosto.csv",
    (
        "blocos-contrato",
        2023,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/setembro.csv",
    (
        "blocos-contrato",
        2023,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/outubro.csv",
    (
        "blocos-contrato",
        2023,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/novembro.csv",
    (
        "blocos-contrato",
        2023,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2023/dezembro.csv",
    (
        "blocos-contrato",
        2024,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-jan.csv",
    (
        "blocos-contrato",
        2024,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-fev.csv",
    (
        "blocos-contrato",
        2024,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-mar.csv",
    (
        "blocos-contrato",
        2024,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-abr.csv",
    (
        "blocos-contrato",
        2024,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocossobcontratomai.csv",
    (
        "blocos-contrato",
        2024,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-jun.csv",
    (
        "blocos-contrato",
        2024,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-jul.csv",
    (
        "blocos-contrato",
        2024,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-ago.csv",
    (
        "blocos-contrato",
        2024,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-set.csv",
    (
        "blocos-contrato",
        2024,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-out.csv",
    (
        "blocos-contrato",
        2024,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-nov.csv",
    (
        "blocos-contrato",
        2024,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2024/blocos-sob-contrato-dez.csv",
    (
        "blocos-contrato",
        2025,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-jan.csv",
    (
        "blocos-contrato",
        2025,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-fev.csv",
    (
        "blocos-contrato",
        2025,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-mar.csv",
    (
        "blocos-contrato",
        2025,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-abr.csv",
    (
        "blocos-contrato",
        2025,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-mai.csv",
    (
        "blocos-contrato",
        2025,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-jun.csv",
    (
        "blocos-contrato",
        2025,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-jul.csv",
    (
        "blocos-contrato",
        2025,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-ago.csv",
    (
        "blocos-contrato",
        2025,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-set.csv",
    (
        "blocos-contrato",
        2025,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-out.csv",
    (
        "blocos-contrato",
        2025,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-nov-2025.csv",
    (
        "blocos-contrato",
        2025,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2025/blocos-sob-contrato-dez-2025.csv",
    (
        "blocos-contrato",
        2026,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2026/blocos-sob-contrato-jan.csv",
    (
        "blocos-contrato",
        2026,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2026/blocos-sob-contrato-fev.csv",
    (
        "blocos-contrato",
        2026,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2026/blocos-sob-contrato-mar.csv",
    (
        "blocos-contrato",
        2026,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2026/blocos-sob-contrato_abr_2026.csv",
    (
        "blocos-contrato",
        2026,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2026/blocos-sob-contrato-mai.csv",
    (
        "blocos-contrato",
        2026,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2026/blocos-sob-contrato-jun.csv",
    (
        "blocos-contrato",
        2026,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/bsc/2026/blocos-sob-contrato-jul.csv",
    (
        "declaracoes-comercialidade",
        2023,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/fevereiro.csv",
    (
        "declaracoes-comercialidade",
        2023,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/marco.csv",
    (
        "declaracoes-comercialidade",
        2023,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/abril.csv",
    (
        "declaracoes-comercialidade",
        2023,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/maio.csv",
    (
        "declaracoes-comercialidade",
        2023,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/junho.csv",
    (
        "declaracoes-comercialidade",
        2023,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/julho.csv",
    (
        "declaracoes-comercialidade",
        2023,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/agosto.csv",
    (
        "declaracoes-comercialidade",
        2023,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/setembro.csv",
    (
        "declaracoes-comercialidade",
        2023,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/outubro.csv",
    (
        "declaracoes-comercialidade",
        2023,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/novembro.csv",
    (
        "declaracoes-comercialidade",
        2023,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2023/dezembro.csv",
    (
        "declaracoes-comercialidade",
        2024,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-jan.csv",
    (
        "declaracoes-comercialidade",
        2024,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-fev.csv",
    (
        "declaracoes-comercialidade",
        2024,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-mar.csv",
    (
        "declaracoes-comercialidade",
        2024,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-abr.csv",
    (
        "declaracoes-comercialidade",
        2024,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-mai-csv.csv",
    (
        "declaracoes-comercialidade",
        2024,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-jun.csv",
    (
        "declaracoes-comercialidade",
        2024,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-jul.csv",
    (
        "declaracoes-comercialidade",
        2024,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-ago.csv",
    (
        "declaracoes-comercialidade",
        2024,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-set.csv",
    (
        "declaracoes-comercialidade",
        2024,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-out.csv",
    (
        "declaracoes-comercialidade",
        2024,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-nov.csv",
    (
        "declaracoes-comercialidade",
        2024,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2024/declaracoes-comercialidade-fase-exploracao-dez.csv",
    (
        "declaracoes-comercialidade",
        2025,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-jan.csv",
    (
        "declaracoes-comercialidade",
        2025,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-fev.csv",
    (
        "declaracoes-comercialidade",
        2025,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-mar.csv",
    (
        "declaracoes-comercialidade",
        2025,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-abr.csv",
    (
        "declaracoes-comercialidade",
        2025,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-mai.csv",
    (
        "declaracoes-comercialidade",
        2025,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-jun.csv",
    (
        "declaracoes-comercialidade",
        2025,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-jul.csv",
    (
        "declaracoes-comercialidade",
        2025,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoees-comercialidade-fase-exploracao-ago.csv",
    (
        "declaracoes-comercialidade",
        2025,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-set.csv",
    (
        "declaracoes-comercialidade",
        2025,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-out.csv",
    (
        "declaracoes-comercialidade",
        2025,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-nov.csv",
    (
        "declaracoes-comercialidade",
        2025,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2025/declaracoes-comercialidade-fase-exploracao-dez.csv",
    (
        "declaracoes-comercialidade",
        2026,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2026/declaracoes-comercialidade-fase-exploracao-jan.csv",
    (
        "declaracoes-comercialidade",
        2026,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2026/declaracoes-comercialidade-fase-exploracao-fev-26.csv",
    (
        "declaracoes-comercialidade",
        2026,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2026/declaracoes-comercialidade-fase-exploracao_mar_26.csv",
    (
        "declaracoes-comercialidade",
        2026,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2026/declaracoes-comercialidade-fase-exploracao_abr_2026.csv",
    (
        "declaracoes-comercialidade",
        2026,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2026/declaracoes-comercialidade-fase-exploracao-mai.csv",
    (
        "declaracoes-comercialidade",
        2026,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2026/declaracoes-comercialidade-fase-exploracao-jun.csv",
    (
        "declaracoes-comercialidade",
        2026,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/dcfe/2026/declaracoes-comercialidade-fase-exploracao-jul.csv",
    (
        "pads-andamento",
        2023,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/fevereiro.csv",
    (
        "pads-andamento",
        2023,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/marco.csv",
    (
        "pads-andamento",
        2023,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/abril.csv",
    (
        "pads-andamento",
        2023,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/maio.csv",
    (
        "pads-andamento",
        2023,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/julho.csv",
    (
        "pads-andamento",
        2023,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/agosto.csv",
    (
        "pads-andamento",
        2023,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/setembro.csv",
    (
        "pads-andamento",
        2023,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/outubro.csv",
    (
        "pads-andamento",
        2023,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/novembro.csv",
    (
        "pads-andamento",
        2023,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2023/dezembro.csv",
    (
        "pads-andamento",
        2024,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-jan.csv",
    (
        "pads-andamento",
        2024,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-fev.csv",
    (
        "pads-andamento",
        2024,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-mar.csv",
    (
        "pads-andamento",
        2024,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-abr.csv",
    (
        "pads-andamento",
        2024,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-mai-csv.csv",
    (
        "pads-andamento",
        2024,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-jun.csv",
    (
        "pads-andamento",
        2024,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-jul.csv",
    (
        "pads-andamento",
        2024,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-ago.csv",
    (
        "pads-andamento",
        2024,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-set.csv",
    (
        "pads-andamento",
        2024,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-out.csv",
    (
        "pads-andamento",
        2024,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-nov.csv",
    (
        "pads-andamento",
        2024,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2024/pads-andamento-dez.csv",
    (
        "pads-andamento",
        2025,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-jan.csv",
    (
        "pads-andamento",
        2025,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-fev.csv",
    (
        "pads-andamento",
        2025,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-mar.csv",
    (
        "pads-andamento",
        2025,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-abr.csv",
    (
        "pads-andamento",
        2025,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-mai.csv",
    (
        "pads-andamento",
        2025,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-jun.csv",
    (
        "pads-andamento",
        2025,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-jul.csv",
    (
        "pads-andamento",
        2025,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-ago.csv",
    (
        "pads-andamento",
        2025,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-set.csv",
    (
        "pads-andamento",
        2025,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-out.csv",
    (
        "pads-andamento",
        2025,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-nov.csv",
    (
        "pads-andamento",
        2025,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2025/pads-andamento-dez.csv",
    (
        "pads-andamento",
        2026,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2026/pads-andamento-jan.csv",
    (
        "pads-andamento",
        2026,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2026/pads-andamento_fev_2026.csv",
    (
        "pads-andamento",
        2026,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2026/pads-andamento_mar_2026.csv",
    (
        "pads-andamento",
        2026,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2026/pads-andamento_abr_2026.csv",
    (
        "pads-andamento",
        2026,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2026/pads-andamento-mai.csv",
    (
        "pads-andamento",
        2026,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2026/pads-andamento-jun.csv",
    (
        "pads-andamento",
        2026,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-andamento/2026/pads-andamento-jul.csv",
    (
        "pads-concluidos",
        2023,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/fevereiro.csv",
    (
        "pads-concluidos",
        2023,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/marco.csv",
    (
        "pads-concluidos",
        2023,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/abril.csv",
    (
        "pads-concluidos",
        2023,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/maio.csv",
    (
        "pads-concluidos",
        2023,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/junho.csv",
    (
        "pads-concluidos",
        2023,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/julho.csv",
    (
        "pads-concluidos",
        2023,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/agosto.csv",
    (
        "pads-concluidos",
        2023,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/setembro.csv",
    (
        "pads-concluidos",
        2023,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/outubro.csv",
    (
        "pads-concluidos",
        2023,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/novembro.csv",
    (
        "pads-concluidos",
        2023,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2023/dezembro.csv",
    (
        "pads-concluidos",
        2024,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-jan.csv",
    (
        "pads-concluidos",
        2024,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-fev.csv",
    (
        "pads-concluidos",
        2024,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-mar.csv",
    (
        "pads-concluidos",
        2024,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-abr.csv",
    (
        "pads-concluidos",
        2024,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-mai-csv.csv",
    (
        "pads-concluidos",
        2024,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-jun.csv",
    (
        "pads-concluidos",
        2024,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-jul.csv",
    (
        "pads-concluidos",
        2024,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-ago.csv",
    (
        "pads-concluidos",
        2024,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-set.csv",
    (
        "pads-concluidos",
        2024,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-out.csv",
    (
        "pads-concluidos",
        2024,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-nov.csv",
    (
        "pads-concluidos",
        2024,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2024/pads-concluidos-dez.csv",
    (
        "pads-concluidos",
        2025,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-jan.csv",
    (
        "pads-concluidos",
        2025,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-fev.csv",
    (
        "pads-concluidos",
        2025,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-mar.csv",
    (
        "pads-concluidos",
        2025,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-abr.csv",
    (
        "pads-concluidos",
        2025,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-mai.csv",
    (
        "pads-concluidos",
        2025,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-jun.csv",
    (
        "pads-concluidos",
        2025,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-jul.csv",
    (
        "pads-concluidos",
        2025,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-ago.csv",
    (
        "pads-concluidos",
        2025,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-out.csv",
    (
        "pads-concluidos",
        2025,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-nov.csv",
    (
        "pads-concluidos",
        2025,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2025/pads-concluidos-dez.csv",
    (
        "pads-concluidos",
        2026,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2026/pads-concluidos-jan.csv",
    (
        "pads-concluidos",
        2026,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2026/pads-concluidos_fev_2026.csv",
    (
        "pads-concluidos",
        2026,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2026/pads-concluidos_mar_2026.csv",
    (
        "pads-concluidos",
        2026,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2026/pads-concluidos_abr_2026.csv",
    (
        "pads-concluidos",
        2026,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2026/pads-concluidos-mai.csv",
    (
        "pads-concluidos",
        2026,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2026/pads-concluidos-jun.csv",
    (
        "pads-concluidos",
        2026,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pads-concluidos/2026/pads-concluidos-jul.csv",
    (
        "pocos-exploratorios",
        2023,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/marco.csv",
    (
        "pocos-exploratorios",
        2023,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/abril.csv",
    (
        "pocos-exploratorios",
        2023,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/maio.csv",
    (
        "pocos-exploratorios",
        2023,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/junho.csv",
    (
        "pocos-exploratorios",
        2023,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/julho.csv",
    (
        "pocos-exploratorios",
        2023,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/agosto.csv",
    (
        "pocos-exploratorios",
        2023,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/setembro.csv",
    (
        "pocos-exploratorios",
        2023,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/outubro.csv",
    (
        "pocos-exploratorios",
        2023,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/novembro.csv",
    (
        "pocos-exploratorios",
        2023,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2023/dezembro.csv",
    (
        "pocos-exploratorios",
        2024,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-jan.csv",
    (
        "pocos-exploratorios",
        2024,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-fev.csv",
    (
        "pocos-exploratorios",
        2024,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-mar.csv",
    (
        "pocos-exploratorios",
        2024,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-abr.csv",
    (
        "pocos-exploratorios",
        2024,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-mai-csv.csv",
    (
        "pocos-exploratorios",
        2024,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-jun.csv",
    (
        "pocos-exploratorios",
        2024,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-jul.csv",
    (
        "pocos-exploratorios",
        2024,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-ago.csv",
    (
        "pocos-exploratorios",
        2024,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-set.csv",
    (
        "pocos-exploratorios",
        2024,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-out.csv",
    (
        "pocos-exploratorios",
        2024,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-nov.csv",
    (
        "pocos-exploratorios",
        2024,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2024/pocos-exploratorios-dez.csv",
    (
        "pocos-exploratorios",
        2025,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-jan.csv",
    (
        "pocos-exploratorios",
        2025,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-fev.csv",
    (
        "pocos-exploratorios",
        2025,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-mar.csv",
    (
        "pocos-exploratorios",
        2025,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-abr.csv",
    (
        "pocos-exploratorios",
        2025,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-mai.csv",
    (
        "pocos-exploratorios",
        2025,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-jun.csv",
    (
        "pocos-exploratorios",
        2025,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-jul.csv",
    (
        "pocos-exploratorios",
        2025,
        8,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-ago.csv",
    (
        "pocos-exploratorios",
        2025,
        9,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-set.csv",
    (
        "pocos-exploratorios",
        2025,
        10,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-out.csv",
    (
        "pocos-exploratorios",
        2025,
        11,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-nov.csv",
    (
        "pocos-exploratorios",
        2025,
        12,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2025/pocos-exploratorios-dez.csv",
    (
        "pocos-exploratorios",
        2026,
        1,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2026/pocos-exploratorios-jan.csv",
    (
        "pocos-exploratorios",
        2026,
        2,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2026/pocos-exploratorios_fev_2026.csv",
    (
        "pocos-exploratorios",
        2026,
        3,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2026/pocos-exploratorios_mar_2026.csv",
    (
        "pocos-exploratorios",
        2026,
        4,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2026/pocos-exploratorios_abr_2026.csv",
    (
        "pocos-exploratorios",
        2026,
        5,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2026/pocos-exploratorios-mai.csv",
    (
        "pocos-exploratorios",
        2026,
        6,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2026/pocos-exploratorios-jun.csv",
    (
        "pocos-exploratorios",
        2026,
        7,
    ): "painel-dinamico-da-fase-de-exploracao/pocos-exploratorios/2026/pocos-exploratorios-jul.csv",
    ("processos-sancionadores", 2023, 2): "processos-sancionadores/2023/feveiro.csv",
    ("processos-sancionadores", 2023, 3): "processos-sancionadores/2023/marco.csv",
    ("processos-sancionadores", 2023, 4): "processos-sancionadores/2023/abril.csv",
    ("processos-sancionadores", 2023, 5): "processos-sancionadores/2023/maio.csv",
    ("processos-sancionadores", 2023, 6): "processos-sancionadores/2023/junho.csv",
    ("processos-sancionadores", 2023, 7): "processos-sancionadores/2023/julho.csv",
    ("processos-sancionadores", 2023, 8): "processos-sancionadores/2023/agosto.csv",
    ("processos-sancionadores", 2023, 9): "processos-sancionadores/2023/setembro.csv",
    ("processos-sancionadores", 2023, 10): "processos-sancionadores/2023/outubro.csv",
    ("processos-sancionadores", 2023, 11): "processos-sancionadores/2023/novembro.csv",
    ("processos-sancionadores", 2023, 12): "processos-sancionadores/2023/dezembro.csv",
    (
        "processos-sancionadores",
        2024,
        1,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-jan.csv",
    (
        "processos-sancionadores",
        2024,
        2,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-fev.csv",
    (
        "processos-sancionadores",
        2024,
        3,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-mar.csv",
    (
        "processos-sancionadores",
        2024,
        4,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-abr.csv",
    (
        "processos-sancionadores",
        2024,
        5,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-mai-csv.csv",
    (
        "processos-sancionadores",
        2024,
        6,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-jun.csv",
    (
        "processos-sancionadores",
        2024,
        7,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-jul.csv",
    (
        "processos-sancionadores",
        2024,
        8,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-ago.csv",
    (
        "processos-sancionadores",
        2024,
        9,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-set.csv",
    (
        "processos-sancionadores",
        2024,
        10,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-out.csv",
    (
        "processos-sancionadores",
        2024,
        11,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-nov-1.csv",
    (
        "processos-sancionadores",
        2024,
        12,
    ): "processos-sancionadores/2024/processos-sancionadores-sep-dez.csv",
    (
        "processos-sancionadores",
        2025,
        1,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-jan.csv",
    (
        "processos-sancionadores",
        2025,
        2,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-fev.csv",
    (
        "processos-sancionadores",
        2025,
        3,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-mar.csv",
    (
        "processos-sancionadores",
        2025,
        4,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-abr.csv",
    (
        "processos-sancionadores",
        2025,
        5,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-mai.csv",
    (
        "processos-sancionadores",
        2025,
        6,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-jun.csv",
    (
        "processos-sancionadores",
        2025,
        7,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-jul.csv",
    (
        "processos-sancionadores",
        2025,
        8,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-ago.csv",
    (
        "processos-sancionadores",
        2025,
        9,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-set.csv",
    (
        "processos-sancionadores",
        2025,
        10,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-out.csv",
    (
        "processos-sancionadores",
        2025,
        11,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-nov.csv",
    (
        "processos-sancionadores",
        2025,
        12,
    ): "processos-sancionadores/2025/processos-sancionadores-sep-dez.csv",
    (
        "processos-sancionadores",
        2026,
        1,
    ): "processos-sancionadores/2026/processos-sancionadores-sep-jan.csv",
    (
        "processos-sancionadores",
        2026,
        2,
    ): "processos-sancionadores/2026/processos-sancionadores-sep_fev_2026.csv",
    (
        "processos-sancionadores",
        2026,
        3,
    ): "processos-sancionadores/2026/processos-sancionadores-sep_mar_2026.csv",
    (
        "processos-sancionadores",
        2026,
        4,
    ): "processos-sancionadores/2026/processos-sancionadores-sep_abr_2026.csv",
    (
        "processos-sancionadores",
        2026,
        5,
    ): "processos-sancionadores/2026/processos-sancionadores-sep-mai.csv",
    (
        "processos-sancionadores",
        2026,
        6,
    ): "processos-sancionadores/2026/processos-sancionadores-jun.csv",
    (
        "processos-sancionadores",
        2026,
        7,
    ): "processos-sancionadores/2026/processos-sancionadores-jul.csv",
    (
        "prorrogacoes-708",
        2023,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/fevereiro.csv",
    (
        "prorrogacoes-708",
        2023,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/marco.csv",
    (
        "prorrogacoes-708",
        2023,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/abril.csv",
    (
        "prorrogacoes-708",
        2023,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/maio.csv",
    (
        "prorrogacoes-708",
        2023,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/junho.csv",
    (
        "prorrogacoes-708",
        2023,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/julho.csv",
    (
        "prorrogacoes-708",
        2023,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/agosto.csv",
    (
        "prorrogacoes-708",
        2023,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/setembro.csv",
    (
        "prorrogacoes-708",
        2023,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/outubro.csv",
    (
        "prorrogacoes-708",
        2023,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/novembro.csv",
    (
        "prorrogacoes-708",
        2023,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2023/dezembro.csv",
    (
        "prorrogacoes-708",
        2024,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-jan.csv",
    (
        "prorrogacoes-708",
        2024,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-fev.csv",
    (
        "prorrogacoes-708",
        2024,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-mar.csv",
    (
        "prorrogacoes-708",
        2024,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-abr.csv",
    (
        "prorrogacoes-708",
        2024,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-mai-csv.csv",
    (
        "prorrogacoes-708",
        2024,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-jun.csv",
    (
        "prorrogacoes-708",
        2024,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-jul.csv",
    (
        "prorrogacoes-708",
        2024,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-ago.csv",
    (
        "prorrogacoes-708",
        2024,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-set.csv",
    (
        "prorrogacoes-708",
        2024,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-out.csv",
    (
        "prorrogacoes-708",
        2024,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-nov.csv",
    (
        "prorrogacoes-708",
        2024,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2024/ranp-708-2017-dez.csv",
    (
        "prorrogacoes-708",
        2025,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-jan.csv",
    (
        "prorrogacoes-708",
        2025,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-fev.csv",
    (
        "prorrogacoes-708",
        2025,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-mar.csv",
    (
        "prorrogacoes-708",
        2025,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-abr.csv",
    (
        "prorrogacoes-708",
        2025,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-mai.csv",
    (
        "prorrogacoes-708",
        2025,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-jun.csv",
    (
        "prorrogacoes-708",
        2025,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-jul.csv",
    (
        "prorrogacoes-708",
        2025,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-ago.csv",
    (
        "prorrogacoes-708",
        2025,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-set.csv",
    (
        "prorrogacoes-708",
        2025,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-out.csv",
    (
        "prorrogacoes-708",
        2025,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-nov.csv",
    (
        "prorrogacoes-708",
        2025,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2025/ranp-708-2017-dez.csv",
    (
        "prorrogacoes-708",
        2026,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2026/ranp-708-2017-jan.csv",
    (
        "prorrogacoes-708",
        2026,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2026/ranp-708-2017_fev_2026.csv",
    (
        "prorrogacoes-708",
        2026,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2026/ranp-708_2017_mar_2026.csv",
    (
        "prorrogacoes-708",
        2026,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2026/ranp_708_2017_abr_2026.csv",
    (
        "prorrogacoes-708",
        2026,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2026/ranp-708-2017-mai.csv",
    (
        "prorrogacoes-708",
        2026,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2026/ranp7082017jun.csv",
    (
        "prorrogacoes-708",
        2026,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-708-2017/2026/ranp-708-2017-jul.csv",
    (
        "prorrogacoes-815",
        2023,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/fevereiro.csv",
    (
        "prorrogacoes-815",
        2023,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/marco.csv",
    (
        "prorrogacoes-815",
        2023,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/abril.csv",
    (
        "prorrogacoes-815",
        2023,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/maio.csv",
    (
        "prorrogacoes-815",
        2023,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/junho.csv",
    (
        "prorrogacoes-815",
        2023,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/julho.csv",
    (
        "prorrogacoes-815",
        2023,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/agosto.csv",
    (
        "prorrogacoes-815",
        2023,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/setembro.csv",
    (
        "prorrogacoes-815",
        2023,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/outubro.csv",
    (
        "prorrogacoes-815",
        2023,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/novembro.csv",
    (
        "prorrogacoes-815",
        2023,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2023/dezembro.csv",
    (
        "prorrogacoes-815",
        2024,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-jan.csv",
    (
        "prorrogacoes-815",
        2024,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-fev.csv",
    (
        "prorrogacoes-815",
        2024,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-mar.csv",
    (
        "prorrogacoes-815",
        2024,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-abr.csv",
    (
        "prorrogacoes-815",
        2024,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-mai-csv.csv",
    (
        "prorrogacoes-815",
        2024,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-jun.csv",
    (
        "prorrogacoes-815",
        2024,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-jul.csv",
    (
        "prorrogacoes-815",
        2024,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-ago.csv",
    (
        "prorrogacoes-815",
        2024,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-set.csv",
    (
        "prorrogacoes-815",
        2024,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-out.csv",
    (
        "prorrogacoes-815",
        2024,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-nov.csv",
    (
        "prorrogacoes-815",
        2024,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2024/ranp-815-2020-dez.csv",
    (
        "prorrogacoes-815",
        2025,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-jan.csv",
    (
        "prorrogacoes-815",
        2025,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-fev.csv",
    (
        "prorrogacoes-815",
        2025,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-mar.csv",
    (
        "prorrogacoes-815",
        2025,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-abr.csv",
    (
        "prorrogacoes-815",
        2025,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-mai.csv",
    (
        "prorrogacoes-815",
        2025,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-jun.csv",
    (
        "prorrogacoes-815",
        2025,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-jul.csv",
    (
        "prorrogacoes-815",
        2025,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-ago.csv",
    (
        "prorrogacoes-815",
        2025,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-set.csv",
    (
        "prorrogacoes-815",
        2025,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-out.csv",
    (
        "prorrogacoes-815",
        2025,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-nov.csv",
    (
        "prorrogacoes-815",
        2025,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2025/ranp-815-2020-dez.csv",
    (
        "prorrogacoes-815",
        2026,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2026/ranp-815-2020-jan.csv",
    (
        "prorrogacoes-815",
        2026,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2026/ranp-815_2020_fev_2026.csv",
    (
        "prorrogacoes-815",
        2026,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2026/ranp-815_2020_mar_2026.csv",
    (
        "prorrogacoes-815",
        2026,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2026/ranp_815_2020_abr_2026.csv",
    (
        "prorrogacoes-815",
        2026,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2026/ranp-815-2020-mai.csv",
    (
        "prorrogacoes-815",
        2026,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2026/ranp-815-2020-jun.csv",
    (
        "prorrogacoes-815",
        2026,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-815-2020/2026/ranp-815-2020-jul.csv",
    (
        "prorrogacoes-878",
        2023,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/fevereiro.csv",
    (
        "prorrogacoes-878",
        2023,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/marco.csv",
    (
        "prorrogacoes-878",
        2023,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/abril.csv",
    (
        "prorrogacoes-878",
        2023,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/maio.csv",
    (
        "prorrogacoes-878",
        2023,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/junho.csv",
    (
        "prorrogacoes-878",
        2023,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/julho.csv",
    (
        "prorrogacoes-878",
        2023,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/agosto.csv",
    (
        "prorrogacoes-878",
        2023,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/setembro.csv",
    (
        "prorrogacoes-878",
        2023,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/outubro.csv",
    (
        "prorrogacoes-878",
        2023,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/novembro.csv",
    (
        "prorrogacoes-878",
        2023,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2023/dezembro.csv",
    (
        "prorrogacoes-878",
        2024,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-jan.csv",
    (
        "prorrogacoes-878",
        2024,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-fev.csv",
    (
        "prorrogacoes-878",
        2024,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-mar.csv",
    (
        "prorrogacoes-878",
        2024,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-abr.csv",
    (
        "prorrogacoes-878",
        2024,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-mai-csv.csv",
    (
        "prorrogacoes-878",
        2024,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-jun.csv",
    (
        "prorrogacoes-878",
        2024,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-jul.csv",
    (
        "prorrogacoes-878",
        2024,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-ago.csv",
    (
        "prorrogacoes-878",
        2024,
        9,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-set.csv",
    (
        "prorrogacoes-878",
        2024,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-out.csv",
    (
        "prorrogacoes-878",
        2024,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-nov.csv",
    (
        "prorrogacoes-878",
        2024,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2024/ranp-878-2022-dez.csv",
    (
        "prorrogacoes-878",
        2025,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-jan.csv",
    (
        "prorrogacoes-878",
        2025,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-fev.csv",
    (
        "prorrogacoes-878",
        2025,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-mar.csv",
    (
        "prorrogacoes-878",
        2025,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-abr.csv",
    (
        "prorrogacoes-878",
        2025,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-mai.csv",
    (
        "prorrogacoes-878",
        2025,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-jun.csv",
    (
        "prorrogacoes-878",
        2025,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-jul.csv",
    (
        "prorrogacoes-878",
        2025,
        8,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-ago.csv",
    (
        "prorrogacoes-878",
        2025,
        10,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-out.csv",
    (
        "prorrogacoes-878",
        2025,
        11,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-nov.csv",
    (
        "prorrogacoes-878",
        2025,
        12,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2025/ranp-878-2022-dez.csv",
    (
        "prorrogacoes-878",
        2026,
        1,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2026/ranp-878-2022-jan-csv.csv",
    (
        "prorrogacoes-878",
        2026,
        2,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2026/ranp-878_2022_fev_2026.csv",
    (
        "prorrogacoes-878",
        2026,
        3,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2026/ranp-878_2022_mar_2026.csv",
    (
        "prorrogacoes-878",
        2026,
        4,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2026/ranp_878_2022_abr_2026.csv",
    (
        "prorrogacoes-878",
        2026,
        5,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2026/ranp-878-2022-mai.csv",
    (
        "prorrogacoes-878",
        2026,
        6,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2026/ranp-878-2022-jun.csv",
    (
        "prorrogacoes-878",
        2026,
        7,
    ): "prorrogacao-prazos-fase-exploracao/ranp-878-2022/2026/ranp-878-2022-jul.csv",
}

_GROUP_NAMES: dict[str, str] = {
    "blocos-contrato": "Blocos sob Contrato",
    "declaracoes-comercialidade": "Declarações de Comercialidade",
    "pads-concluidos": "PADs Concluídos",
    "pads-andamento": "PADs em Andamento",
    "pocos-exploratorios": "Poços Exploratórios",
    "prorrogacoes-708": "Prorrogação de Prazos — RANP 708/2017",
    "prorrogacoes-815": "Prorrogação de Prazos — RANP 815/2020",
    "prorrogacoes-878": "Prorrogação de Prazos — RANP 878/2022",
    "processos-sancionadores": "Processos Sancionadores",
}


def _build_groups() -> dict[str, list[DatasetEntry]]:
    groups: dict[str, list[DatasetEntry]] = {}
    for (group, year, month), tail in sorted(_URLS.items()):
        entries = groups.setdefault(group, [])
        entries.append(
            DatasetEntry(
                id=f"{group}-{year}-{month:02d}",
                base_id=group,
                name=f"{_GROUP_NAMES[group]} — {year}-{month:02d}",
                url=f"{_BASE}/{tail}",
                ext="csv",
                group=group,
                source=_SOURCE,
                year=year,
                semester=None,
                month=month,
            )
        )
    return groups


_GROUPS: dict[str, list[DatasetEntry]] = _build_groups()

GROUPS_FASE_EXPLORACAO: dict[str, GroupInfo] = {
    key: {"name": _GROUP_NAMES[key], "entries": entries}
    for key, entries in _GROUPS.items()
}

GROUP_ALIASES_FASE_EXPLORACAO: dict[str, str] = {
    "blocos": "blocos-contrato",
    "comercialidade": "declaracoes-comercialidade",
    "pads": "pads-concluidos",
    "pocos": "pocos-exploratorios",
    "sancionadores": "processos-sancionadores",
    "prorrogacoes": "prorrogacoes-708",
}
