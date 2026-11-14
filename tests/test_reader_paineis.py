"""Painéis estatísticos da ANP (várias tabelas empilhadas) e planilhas municipais."""

from __future__ import annotations

from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("fastexcel")
xlsxwriter = pytest.importorskip("xlsxwriter")

from anp_fetcher.reader import read_file  # noqa: E402
from anp_fetcher.wrangling import spec_for  # noqa: E402

MESES = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]
BAD = ("__UNNAMED__", "column_", "coluna_")


def _planilha(path: Path, rows: list[list[object]]) -> Path:
    book = xlsxwriter.Workbook(str(path))
    sheet = book.add_worksheet()
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            if value is not None:
                sheet.write(i, j, value)
    book.close()
    return path


def _tabela(
    titulo: str, anos: list[int], *, mes: str = "MÊS", recuo: int = 0
) -> list[list[object]]:
    """Uma tabela do painel: título, filtros, faixa, cabeçalho em dois níveis, notas."""
    pad = [None] * recuo
    n = len(anos)
    topo = [
        [*pad, titulo],
        [*pad, "Selecione, clicando nas setas abaixo, a UF desejada."],
        [*pad, "BRASIL"],
        [*pad, "UN. DA FEDERAÇÃO", "(Tudo)"],
        [*pad, *["xxxxxxxx"] * (n + 2)],
        [*pad, None, "ANO", *[None] * (n - 1), "VARIAÇÃO DO ACUMULADO"],
        [*pad, mes, *anos, f"NO ANO {anos[-1]} / {anos[-2]} (%) ¹"],
    ]
    dados: list[list[object]] = [
        [*pad, m, *[i + a for a in range(n)], 5.5] for i, m in enumerate(MESES)
    ]
    dados.append([*pad, "Total do Ano", *[100.0] * n, 7.5])
    notas = [
        [*pad, "BRASIL"],
        [*pad, "Produção Mensal"],
        [*pad, "Fonte: ANP, conforme o Decreto n.º 2.705/98."],
        [*pad, "Notas: (b) = barril."],
        [*pad, "Dados atualizados em 29 de outubro de 2026."],
        [*pad, "Voltar ao índice"],
    ]
    return topo + dados + notas


def _painel(path: Path, *, recuo: int = 0) -> Path:
    capa = [
        ["Agência Nacional do Petróleo, Gás Natural e Biocombustíveis"],
        ["Produção Nacional"],
        ["Índice:"],
        ["Produção por Unidade da Federação - 2000-2011 (b)"],
        ["Dados atualizados em 29 de outubro de 2026."],
    ]
    rows = [
        *capa,
        *_tabela(
            "Produção por Unidade da Federação - 2000-2011 (b)",
            list(range(2000, 2012)),
            recuo=recuo,
        ),
        # segunda tabela: começa em outro ano e o cabeçalho diz "Meses"
        *_tabela(
            "Produção por Grande Região - 2010-2011 (b)",
            [2010, 2011],
            mes="Meses",
            recuo=recuo,
        ),
    ]
    return _planilha(path, rows)


def test_painel_empilha_as_tabelas_com_nomes_legiveis_e_so_o_dado(
    tmp_path: Path,
) -> None:
    df = read_file(_painel(tmp_path / "ppg.xlsx"), spec_for("ppg"))
    assert df.columns == [
        "tabela",
        "Mês",
        *[f"ANO {ano}" for ano in range(2000, 2012)],
        "VARIAÇÃO DO ACUMULADO NO ANO (%)",
    ]
    assert not any(c.startswith(BAD) for c in df.columns)
    assert df.height == 2 * 13  # 12 meses e "Total do Ano" por tabela; resto fora
    assert df.group_by("tabela", maintain_order=True).len().to_dicts() == [
        {"tabela": "Produção por Unidade da Federação - 2000-2011 (b)", "len": 13},
        {"tabela": "Produção por Grande Região - 2010-2011 (b)", "len": 13},
    ]
    assert df["Mês"].to_list()[:2] == ["Janeiro", "Fevereiro"]
    assert df["Mês"].to_list()[12] == "Total do Ano"
    assert df["Mês"].to_list()[13] == "Janeiro"  # "Meses" também é a linha de dados
    assert not set(df["Mês"]) - {*MESES, "Total do Ano"}  # sem título, nota nem faixa


def test_painel_junta_as_colunas_pelo_nome_e_nao_pela_posicao(tmp_path: Path) -> None:
    df = read_file(_painel(tmp_path / "ppg.xlsx"), spec_for("ppg"))
    segunda = df.filter(pl.col("tabela").str.contains("Região"))
    # a segunda tabela, de cabeçalho curto (4 células), só tem 2010 e 2011: os
    # outros anos ficam vazios, não deslocados
    assert segunda["ANO 2000"].null_count() == 13
    assert segunda["ANO 2009"].null_count() == 13
    # janeiro de cada tabela vale 0, 1, 2... na ordem das colunas da própria tabela
    assert segunda["ANO 2010"].to_list()[0] == 0.0
    assert segunda["ANO 2011"].to_list()[0] == 1.0
    primeira = df.filter(pl.col("tabela").str.contains("Unidade"))
    assert primeira["ANO 2002"].to_list()[0] == 2.0
    assert primeira["ANO 2000"].to_list()[0] == 0.0


def test_painel_tipa_os_valores_como_numero(tmp_path: Path) -> None:
    df = read_file(_painel(tmp_path / "ppg.xlsx"), spec_for("ppg"))
    assert df.schema["ANO 2000"] == pl.Float64
    assert df.schema["VARIAÇÃO DO ACUMULADO NO ANO (%)"] == pl.Float64
    assert df.schema["Mês"] == pl.String


def test_painel_com_a_tabela_na_segunda_coluna(tmp_path: Path) -> None:
    # ``vendas``: a primeira coluna da planilha fica vazia
    df = read_file(_painel(tmp_path / "v.xlsx", recuo=1), spec_for("vdpb"))
    assert df.columns[:3] == ["tabela", "Mês", "ANO 2000"]
    assert df.height == 26
    assert df["Mês"][0] == "Janeiro"


@pytest.mark.parametrize("group", ["ie", "pp", "pb", "ppg", "vdpb"])
def test_painel_vale_para_todos_os_grupos_de_painel(tmp_path: Path, group: str) -> None:
    df = read_file(_painel(tmp_path / "x.xlsx"), spec_for(group))
    assert df.height == 26
    assert not any(c.startswith(BAD) for c in df.columns)
    assert len(set(df.columns)) == len(df.columns)


def test_planilha_municipal_acha_o_cabecalho_e_deixa_titulo_e_vazio_de_fora(
    tmp_path: Path,
) -> None:
    path = _planilha(
        tmp_path / "vendas-municipais-asfalto_2000.xlsx",
        [
            ["AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCOMBUSTÍVEIS"],
            ["VENDAS DE ASFALTO POR ESTADO E MUNICÍPIO"],
            ["UNIDADE DE MEDIDA: QUILO"],
            ["ANO 2000"],
            ["CÓDIGO IBGE", "Município", "TOTAL GERAL"],
            ["IBGE"],
            [],
            [None, "RONDÔNIA"],  # estado só com o nome: não é nível do cabeçalho
            ["1100023", "ARIQUEMES", 1569005],
            [None, "ACRE", 79000],
            ["1100049", "CACOAL", 698440],
            [None, None, None],
            [None, "TOTAL BRASIL", 1853584348],
        ],
    )
    df = read_file(path, spec_for("vdpb"))
    assert df.columns == [
        "CÓDIGO IBGE",
        "Município",
        "TOTAL GERAL",
        "produto",
        "unidade",
    ]
    assert set(df["produto"]) == {"ASFALTO"}
    assert set(df["unidade"]) == {"QUILO"}
    assert df.height == 5  # estado, municípios e total; título, unidade e vazio fora
    assert df["Município"].to_list() == [
        "RONDÔNIA",
        "ARIQUEMES",
        "ACRE",
        "CACOAL",
        "TOTAL BRASIL",
    ]


def test_painel_sem_tabela_reconhecida_passa_como_veio(tmp_path: Path) -> None:
    path = _planilha(tmp_path / "x.xlsx", [["a", "b"], [1, 2]])
    assert read_file(path, spec_for("ie")).width == 2


def _municipal(path: Path, preambulo: list[list[object]]) -> Path:
    return _planilha(
        path,
        [
            *preambulo,
            ["CÓDIGO IBGE", "Município", "Vendas"],
            ["IBGE"],
            ["1100023", "ARIQUEMES", 10],
            [None, "TOTAL BRASIL", 10],
        ],
    )


def test_planilha_municipal_leva_produto_e_unidade_do_preambulo(tmp_path: Path) -> None:
    path = _municipal(
        tmp_path / "vendas-municipais-etanol-hidratado_2005.xlsx",
        [
            ["AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCOMBUSTÍVEIS"],
            ["VENDAS DE ALCOOL HIDRATADO POR ESTADO E MUNICÍPIO"],
            ["UNIDADE DE MEDIDA: LITRO"],
            ["ANO: 2005"],
        ],
    )
    df = read_file(path, spec_for("vdpb"))
    assert df.columns == ["CÓDIGO IBGE", "Município", "Vendas", "produto", "unidade"]
    assert set(df["produto"]) == {"ALCOOL HIDRATADO"}  # como vem, sem o "VENDAS DE"
    assert set(df["unidade"]) == {"LITRO"}  # sem o rótulo
    assert df.height == 2


def test_planilha_municipal_produto_sem_por_no_titulo(tmp_path: Path) -> None:
    path = _municipal(
        tmp_path / "vendas-municipais-gasolina-c_2001.xlsx",
        [
            ["AGÊNCIA NACIONAL DO PETRÓLEO"],
            ["VENDAS DE GASOLINA C"],
            ["UNIDADE DE MEDIDA: LITRO"],
        ],
    )
    assert read_file(path, spec_for("vdpb"))["produto"][0] == "GASOLINA C"


def test_planilha_municipal_sem_preambulo_usa_o_nome_do_arquivo_e_avisa(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    path = _municipal(
        tmp_path / "vendas-municipais-asfalto_2001.xlsx",
        [["AGÊNCIA NACIONAL DO PETRÓLEO"], ["ANO 2001"]],
    )
    with caplog.at_level("WARNING"):
        df = read_file(path, spec_for("vdpb"))
    assert set(df["produto"]) == {"ASFALTO"}
    assert df["unidade"].null_count() == df.height
    assert "produto não consta do preâmbulo" in caplog.text
    assert "unidade não consta do preâmbulo" in caplog.text


def test_painel_do_vdpb_nao_ganha_produto_nem_unidade(tmp_path: Path) -> None:
    df = read_file(_painel(tmp_path / "v.xlsx"), spec_for("vdpb"))
    assert "produto" not in df.columns
