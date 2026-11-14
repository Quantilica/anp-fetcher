"""ZIP com vários membros no lake: nenhuma linha perdida, um layout por dataset."""

from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")
from quantilica.analytics.lake import check_dataset, scan_dataset  # noqa: E402

from anp_fetcher.lake import (  # noqa: E402
    SOURCE_ID,
    converter,
    table_dataset_for_member,
)
from anp_fetcher.reader import zip_data_members  # noqa: E402
from anp_fetcher.storage import _GROUP_DIRS  # noqa: E402

POCO_HEADER = "Estado;Bacia;Nome Poço;Período;Óleo (bbl/dia)"


def _poco_csv(prefix: str, rows: int) -> str:
    lines = [POCO_HEADER]
    lines += [f"BA;Recôncavo;{prefix}-{i}-BA;2005/01;{i},5" for i in range(rows)]
    return "\n".join(lines) + "\n"


def _zip(path: Path, members: dict[str, str | bytes]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as zf:
        for name, content in members.items():
            zf.writestr(name, content)
    return path


def _group_dir(tmp_path: Path, group: str) -> Path:
    return tmp_path / "raw" / _GROUP_DIRS[group]


def _files(dataset_dir: Path) -> list[str]:
    return sorted(p.stem for p in dataset_dir.rglob("*.parquet"))


def test_zip_mar_e_terra_viram_dois_parquets_com_ambiente(tmp_path: Path) -> None:
    group = "producao-poco-abertos"
    _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2005@20261105.zip",
        {
            "2005/2005_producao_mar.csv": _poco_csv("M", 3),
            "2005/2005_producao_terra.csv": _poco_csv("T", 5),
        },
    )
    lake = tmp_path / "lake"
    res = converter.convert(tmp_path / "raw", lake)
    assert not res.errors, res.errors
    assert res.converted == 2

    dataset = lake / SOURCE_ID / "producao-poco-abertos"
    assert check_dataset(dataset) == []
    assert _files(dataset) == [
        "producao-poco-da_2005__2005_producao_mar",
        "producao-poco-da_2005__2005_producao_terra",
    ]
    df = scan_dataset(dataset).collect()
    assert df.height == 8  # 3 + 5: nenhuma linha perdida
    assert df.group_by("ambiente").len().sort("ambiente").rows() == [
        ("mar", 3),
        ("terra", 5),
    ]
    assert set(df["ano"].to_list()) == {2005}

    res2 = converter.convert(tmp_path / "raw", lake)
    assert res2.converted == 0 and res2.skipped == 2


def test_presal_vai_para_dataset_proprio_e_nao_duplica_a_soma(tmp_path: Path) -> None:
    group = "producao-poco-abertos"
    _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2023-12@20261105.zip",
        {
            "2023_12_producao_PreSal.csv": _poco_csv("P", 2),
            "2023_12_producao_Terra.csv": _poco_csv("T", 4),
            "2023_12_producao_Mar.csv": _poco_csv("M", 3),
        },
    )
    _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2015@20261105.zip",
        {
            "2015/2015_producao_mar.csv": _poco_csv("M", 3),
            "2015/2015_producao_presal.csv": _poco_csv("P", 1),
            "2015/2015_producao_terra.csv": _poco_csv("T", 2),
        },
    )
    lake = tmp_path / "lake"
    res = converter.convert(tmp_path / "raw", lake)
    assert not res.errors, res.errors
    base = lake / SOURCE_ID
    assert sorted(p.name for p in base.iterdir()) == [
        "producao-poco-abertos",
        "producao-poco-abertos-anual",
        "producao-poco-abertos-anual-presal",
        "producao-poco-abertos-presal",
    ]
    mensal = scan_dataset(base / "producao-poco-abertos").collect()
    assert mensal.group_by("ambiente").len().sort("ambiente").rows() == [
        ("mar", 3),
        ("terra", 4),
    ]
    assert set(mensal["mes"].to_list()) == {"12"}
    presal = scan_dataset(base / "producao-poco-abertos-presal").collect()
    assert presal.height == 2 and set(presal["ambiente"].to_list()) == {"presal"}
    assert set(presal["mes"].to_list()) == {"12"}
    anual = scan_dataset(base / "producao-poco-abertos-anual").collect()
    assert sorted(anual["ambiente"].to_list()) == ["mar"] * 3 + ["terra"] * 2
    anual_presal = scan_dataset(base / "producao-poco-abertos-anual-presal").collect()
    assert anual_presal.height == 1 and set(anual_presal["ano"].to_list()) == {2015}
    for dataset in base.iterdir():
        assert check_dataset(dataset) == []

    # o id do dataset de pré-sal seleciona o grupo, mas só grava o recorte
    only = converter.convert(
        tmp_path / "raw", tmp_path / "lake2", datasets=["producao-poco-abertos-presal"]
    )
    assert not only.errors, only.errors
    assert only.converted == 1
    assert [p.name for p in (tmp_path / "lake2" / SOURCE_ID).iterdir()] == [
        "producao-poco-abertos-presal"
    ]


def test_anual_consolidado_vale_mais_que_os_meses(tmp_path: Path) -> None:
    group = "producao-poco-abertos"
    _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2013@20261105.zip",
        {
            "2013/2013_01_producao_mar.csv": _poco_csv("M", 1),
            "2013/2013_02_producao_mar.csv": _poco_csv("M", 1),
            "2013/2013_producao_mar.csv": _poco_csv("M", 2),
            # sem anual de terra: os meses de terra entram
            "2013/2013_01_producao_terra.csv": _poco_csv("T", 1),
            "2013/2013_02_producao_terra.csv": _poco_csv("T", 1),
            "2013/prod_por_poco_2013_01_mar.pdf": b"%PDF-",
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    dataset = tmp_path / "lake" / SOURCE_ID / "producao-poco-abertos"
    assert _files(dataset) == [
        "producao-poco-da_2013__2013_01_producao_terra",
        "producao-poco-da_2013__2013_02_producao_terra",
        "producao-poco-da_2013__2013_producao_mar",
    ]


def test_gemeos_csv_e_json_do_zip_convertem_so_o_csv(tmp_path: Path) -> None:
    group = "producao-poco-abertos"
    _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2005@20261105.zip",
        {
            "a_producao_mar.csv": _poco_csv("M", 2),
            "a_producao_mar.json": '[{"Estado": "BA"}]',
            "a_producao_terra.csv": _poco_csv("T", 2),
            "a_producao_terra.json": '[{"Estado": "BA"}]',
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 2
    dataset = tmp_path / "lake" / SOURCE_ID / "producao-poco-abertos"
    assert scan_dataset(dataset).collect().height == 4


def test_zip_de_um_membro_fica_como_antes(tmp_path: Path) -> None:
    group = "movimentacao-derivados"
    _zip(
        _group_dir(tmp_path, group) / "mdpg-fornecedores@20261104.zip",
        {
            "venda_direta.csv": "Ano;Valor\n2024;1,5\n",
            "Thumbs.db": b"lixo",
            "leia-me.pdf": b"%PDF-",
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 1
    dataset = tmp_path / "lake" / SOURCE_ID / "movimentacao-derivados"
    assert _files(dataset) == ["mdpg-fornecedores"]


def test_tabelas_diferentes_vao_para_datasets_proprios(tmp_path: Path) -> None:
    group = "movimentacao-derivados"
    _zip(
        _group_dir(tmp_path, group) / "mdpg-asfalto@20261104.zip",
        {
            "Asfalto_Vendas_Distribuidor_Atual.csv": (
                "Ano;Mês;Agente Regulado;Quantidade\n2024;1;ACME;1,5\n2024;2;ACME;2,5\n"
            ),
            "Asfalto_Vendas_Distribuidor_UF_Atual.csv": (
                "Ano;Mês;UF de Origem;UF de Destino;Quantidade\n2024;1;SP;RJ;3,5\n"
            ),
            "Asfalto_Vendas_Distribuidor_Historico.csv": (
                "Ano;Mês;Agente Regulado;UF Origem;Quantidade\n2010;1;X;SP;7,5\n"
            ),
        },
    )
    lake = tmp_path / "lake"
    res = converter.convert(tmp_path / "raw", lake)
    assert not res.errors, res.errors
    assert res.converted == 3

    base = lake / SOURCE_ID
    assert not (base / "movimentacao-derivados").exists()
    expected = {
        "movimentacao-derivados-asfalto-vendas-distribuidor-atual": (
            2,
            ["Ano", "Mês", "Agente Regulado", "Quantidade"],
        ),
        "movimentacao-derivados-asfalto-vendas-distribuidor-uf-atual": (
            1,
            ["Ano", "Mês", "UF de Origem", "UF de Destino", "Quantidade"],
        ),
        "movimentacao-derivados-asfalto-vendas-distribuidor-historico": (
            1,
            ["Ano", "Mês", "Agente Regulado", "UF Origem", "Quantidade"],
        ),
    }
    for dataset_id, (rows, columns) in expected.items():
        assert check_dataset(base / dataset_id) == []
        df = scan_dataset(base / dataset_id).collect()
        assert df.height == rows
        assert df.columns == columns

    # o grupo e o id de uma tabela selecionam os mesmos arquivos
    only = converter.convert(
        tmp_path / "raw",
        tmp_path / "lake2",
        datasets=["movimentacao-derivados-asfalto-vendas-distribuidor-uf-atual"],
    )
    assert not only.errors, only.errors
    assert only.converted == 1


def test_arf_consolidacao_uma_tabela_por_dataset(tmp_path: Path) -> None:
    group = "amostras-rochas-fluidos"
    _zip(
        _group_dir(tmp_path, group) / "arf-consolidacao-2024@20261105.zip",
        {
            "consolidacao-2024/consolidacao-daa-2024-calha.csv": (
                "Bacia sedimentar;Total de caixas\nCampos;3\nSantos;4\n"
            ),
            "consolidacao-2024/consolidacao-daa-2024-fluido.csv": (
                "Bacia sedimentar;Tipo fluido;Volume (L)\nCampos;óleo;1,5\n"
            ),
            "consolidacao-2024/consolidacao-daa-2024-lamina.csv": (
                "Bacia sedimentar;Profundidade da lâmina (m)\nCampos;10,5\n"
            ),
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    base = tmp_path / "lake" / SOURCE_ID
    assert sorted(p.name for p in base.iterdir()) == [
        "amostras-rochas-fluidos-calha",
        "amostras-rochas-fluidos-fluidos",
        "amostras-rochas-fluidos-laminas",
    ]
    calha = scan_dataset(base / "amostras-rochas-fluidos-calha").collect()
    assert calha.height == 2
    assert _files(base / "amostras-rochas-fluidos-calha") == [
        "arf-consolidacao-2024__consolidacao_daa_2024_calha"
    ]


def test_depositarias_iguais_ficam_no_grupo_com_a_coluna_membro(
    tmp_path: Path,
) -> None:
    group = "amostras-rochas-fluidos"
    tabela = "SERVIÇOS;UNIDADE;VALOR (R$)\nAmostra;un;10,5\n"
    _zip(
        _group_dir(tmp_path, group) / "arf-depositarias-2017@20261105.zip",
        {
            "valores-depositarias-SAAs-2017/SHELL_2017.csv": tabela,
            "valores-depositarias-SAAs-2017/TOTAL_2017.csv": tabela,
            # mesmo slug de TOTAL_2017.csv: ganha sufixo, não sobrescreve
            "valores-depositarias-SAAs-2017/TOTAL_2017..csv": tabela,
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 3
    dataset = tmp_path / "lake" / SOURCE_ID / "amostras-rochas-fluidos"
    assert len(_files(dataset)) == 3
    df = scan_dataset(dataset).collect()
    assert df.height == 3
    assert sorted(df["membro"].to_list()) == ["SHELL_2017", "TOTAL_2017", "TOTAL_2017."]


def test_json_com_extensao_zip_nao_derruba_nem_mascara_o_mes(
    tmp_path: Path,
) -> None:
    group_dir = _group_dir(tmp_path, "pmqc")
    group_dir.mkdir(parents=True)
    _zip(
        group_dir / "pmqc-csv_2024@20261106.zip",
        {
            f"2024/PMQC_2024_{m:02d}.csv": f"Produto;Resultado\nG;{m}\n"
            for m in (1, 2, 3)
        },
    )
    # a ANP já publicou JSON com extensão .zip (um mês solto, antes do ZIP anual)
    (group_dir / "pmqc-json_2024-02.zip").write_text('{"UF": {"GO": {}}}')
    (group_dir / "pmqc-csv_2024-04@20261106.zip").write_bytes(b"PK\x03\x04quebrado")

    res = converter.convert(tmp_path / "raw", tmp_path / "lake", datasets=["pmqc"])
    assert len(res.errors) == 1 and "pmqc-csv_2024-04" in res.errors[0], res.errors
    assert "ZIP" in res.errors[0] or "zip" in res.errors[0]
    df = scan_dataset(tmp_path / "lake" / SOURCE_ID / "pmqc").collect()
    assert sorted(df["mes"].to_list()) == ["01", "02", "03"]  # fevereiro vem do ZIP

    planned = {p.path.name: p for p in converter.inventory(tmp_path / "raw")}
    assert planned["pmqc-json_2024-02.zip"].skip_reason == "gemeo"
    assert planned["pmqc-csv_2024@20261106.zip"].dataset == "pmqc"


def test_conversao_nao_deixa_temporarios(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    scratch = tmp_path / "scratch"
    scratch.mkdir()
    monkeypatch.setenv("QUANTILICA_LAKE_SCRATCH", str(scratch))
    group = "producao-poco-abertos"
    _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2005@20261105.zip",
        {
            "a_producao_mar.csv": _poco_csv("M", 2),
            "a_producao_terra.csv": _poco_csv("T", 2),
        },
    )
    _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2006@20261105.zip",
        {"2006_producao_mar.csv": _poco_csv("M", 2)},
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 3
    assert list(scratch.iterdir()) == []


def test_zip_data_members_ignora_ruido_pdf_e_json(tmp_path: Path) -> None:
    path = _zip(
        tmp_path / "x.zip",
        {
            "2015/b.csv": "a\n1\n",
            "2015/a.xlsx": b"x",
            "2015/b.json": "{}",
            "2015/leia.pdf": b"%PDF-",
            "2015/Thumbs.db": b"x",
            "__MACOSX/2015/._b.csv": b"x",
            "~$a.xlsx": b"x",
        },
    )
    assert zip_data_members(path) == ["2015/a.xlsx", "2015/b.csv"]


def test_zip_data_members_de_planilha_e_vazio(tmp_path: Path) -> None:
    path = _zip(tmp_path / "x.zip", {"[Content_Types].xml": "<x/>", "xl/a.csv": "1"})
    assert zip_data_members(path) == []


def test_zip_data_members_recusa_arquivo_que_nao_e_zip(tmp_path: Path) -> None:
    fake = tmp_path / "falso.zip"
    fake.write_text('{"UF": {}}')
    with pytest.raises(zipfile.BadZipFile):
        zip_data_members(fake)


@pytest.mark.parametrize(
    ("group", "base_id", "member", "expected"),
    [
        (
            "amostras-rochas-fluidos",
            "arf-consolidacao-2022",
            "Consolidaç╞o DAA 2022 Lâminas.csv",
            "amostras-rochas-fluidos-laminas",
        ),
        (
            "amostras-rochas-fluidos",
            "arf-consolidacao-2020",
            "consolidacao-celulas-2020.csv",
            "amostras-rochas-fluidos-celulas",
        ),
        (
            "amostras-rochas-fluidos",
            "arf-consolidacao-2017",
            "consolidacao-2017/consolidacao-laterais-2017.csv",
            "amostras-rochas-fluidos-laterais",
        ),
        (
            "amostras-rochas-fluidos",
            "arf-consolidacao-2024",
            "consolidacao-daa-2024-testemunho.csv",
            "amostras-rochas-fluidos-testemunhos",
        ),
        ("amostras-rochas-fluidos", "arf-depositarias-2020", "SHELL.csv", None),
        (
            "movimentacao-derivados",
            "mdpg-logistica",
            "DADOS ABERTOS - LOGISTICA 01 - ABASTECIMENTO NACIONAL DE COMBUSTÍVEIS.csv",
            "movimentacao-derivados-logistica-01-abastecimento-nacional-de-combustiveis",
        ),
    ],
)
def test_table_dataset_for_member(
    group: str, base_id: str, member: str, expected: str | None
) -> None:
    assert table_dataset_for_member(group, base_id, member) == expected
