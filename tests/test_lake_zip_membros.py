"""ZIP com vários membros no lake: nenhuma linha perdida, um layout por dataset."""

from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")
import polars as pl  # noqa: E402
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
    assert set(calha["ano"].to_list()) == {2024}  # do nome do ZIP
    assert _files(base / "amostras-rochas-fluidos-calha") == [
        "arf-consolidacao-2024__consolidacao_daa_2024_calha"
    ]


def test_depositarias_iguais_viram_um_dataset_por_ano_com_a_coluna_membro(
    tmp_path: Path,
) -> None:
    group = "amostras-rochas-fluidos"
    tabela = "SERVIÇOS;UNIDADE;VALOR (R$)\nAmostra;un;10,5\n"
    _zip(
        _group_dir(tmp_path, group) / "arf-depositarias-2017@20261105.zip",
        {
            "valores-depositarias-SAAs-2017/SHELL_2017.csv": tabela,
            "valores-depositarias-SAAs-2017/TOTAL_2017.csv": tabela,
            # mesmo slug de TOTAL_2017.csv: o sufixo entra no nome, antes da extensão
            "valores-depositarias-SAAs-2017/TOTAL_2017..csv": tabela,
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 3
    dataset = tmp_path / "lake" / SOURCE_ID / "amostras-rochas-fluidos-depositarias"
    assert _files(dataset) == [
        "arf-depositarias-2017__shell_2017",
        "arf-depositarias-2017__total_2017",
        "arf-depositarias-2017__total_2017_2",
    ]
    assert (dataset / "ano=2017").is_dir()
    df = scan_dataset(dataset).collect()
    assert df.height == 3
    assert set(df["ano"].to_list()) == {2017}
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
        (
            "amostras-rochas-fluidos",
            "arf-depositarias-2020",
            "SHELL.csv",
            "amostras-rochas-fluidos-depositarias",
        ),
        (
            "movimentacao-derivados",
            "mdpg-logistica",
            "DADOS ABERTOS - LOGISTICA 01 - ABASTECIMENTO NACIONAL DE COMBUSTÍVEIS.csv",
            "movimentacao-derivados-logistica-abastecimento-nacional",
        ),
        (
            "movimentacao-derivados",
            "mdpg-liquidos",
            "Liquidos_Vendas_Historico_2018_a_2023.csv",
            "movimentacao-derivados-liquidos-vendas-historico",
        ),
        (
            "movimentacao-derivados",
            "mdpg-liquidos",
            "LÍQUIDOS vendas historico 2007 a 2017.CSV",
            "movimentacao-derivados-liquidos-vendas-historico",
        ),
        (
            "movimentacao-derivados",
            "mdpg-lubrificante",
            "Lubrificante_Anexo_C.csv",
            "movimentacao-derivados-lubrificante-anexo-c",
        ),
        ("movimentacao-derivados", "mdpg-lubrificante", "INDICE_ANEXOS.xlsx", None),
        ("movimentacao-derivados", "mdpg-novo", "Novo_Atual.csv", None),
    ],
)
def test_table_dataset_for_member(
    group: str, base_id: str, member: str, expected: str | None
) -> None:
    assert table_dataset_for_member(group, base_id, member) == expected


def test_mdpg_ids_estaveis_historicos_juntos_indice_fora_e_membro_novo_avisa(
    tmp_path: Path,
) -> None:
    group = "movimentacao-derivados"
    cabecalho = "Ano;Mês;Agente Regulado;Quantidade\n"
    _zip(
        _group_dir(tmp_path, group) / "mdpg-liquidos@20261114.zip",
        {
            "Liquidos_Vendas_Atual.csv": cabecalho + "2024;1;A;1,5\n",
            "Liquidos_Vendas_Historico_2007_a_2017.csv": cabecalho + "2010;1;A;7,5\n",
            "Liquidos_Vendas_Historico_2018_a_2023.csv": cabecalho + "2020;1;B;8,5\n",
            "Liquidos_Tabela_Nova.csv": cabecalho + "2024;1;A;1,5\n",
        },
    )
    _zip(
        _group_dir(tmp_path, group) / "mdpg-lubrificante@20261104.zip",
        {
            "INDICE_ANEXOS.xlsx": b"nao e lido",
            "Lubrificante_Anexo_A.csv": cabecalho + "2024;1;A;1,5\n",
            "Lubrificante_Anexo_B.csv": cabecalho + "2024;1;A;2,5\n",
        },
    )
    lake = tmp_path / "lake"
    res = converter.convert(tmp_path / "raw", lake)
    assert res.errors == []  # membro desconhecido não derruba os demais
    assert len(res.warnings) == 1
    assert "Liquidos_Tabela_Nova.csv" in res.warnings[0]
    assert "sem tabela declarada" in res.warnings[0]
    base = lake / SOURCE_ID
    assert sorted(p.name for p in base.iterdir()) == [
        "movimentacao-derivados-liquidos-vendas-atual",
        "movimentacao-derivados-liquidos-vendas-historico",
        "movimentacao-derivados-lubrificante-anexo-a",
        "movimentacao-derivados-lubrificante-anexo-b",
    ]  # nada de dataset novo para o membro desconhecido, nem para o índice
    historico = base / "movimentacao-derivados-liquidos-vendas-historico"
    assert _files(historico) == [
        "mdpg-liquidos__liquidos_vendas_historico_2007_a_2017",
        "mdpg-liquidos__liquidos_vendas_historico_2018_a_2023",
    ]
    assert scan_dataset(historico).collect().height == 2


def test_upgrade_do_lake_apaga_o_layout_antigo_e_nao_duplica(tmp_path: Path) -> None:
    import polars as pl
    from quantilica.analytics.lake import LakeWriter
    from quantilica.core.lake import DatasetDescriptor, partition_types_for

    group = "producao-poco-abertos"
    zpath = _zip(
        _group_dir(tmp_path, group) / "producao-poco-da_2005@20261105.zip",
        {
            "2005/2005_producao_mar.csv": _poco_csv("M", 3),
            "2005/2005_producao_terra.csv": _poco_csv("T", 5),
        },
    )
    lake = tmp_path / "lake"
    # o que o layout antigo gravava: o ZIP inteiro como um Parquet só (o 1º membro)
    old_dataset = lake / SOURCE_ID / "producao-poco-abertos"
    writer = LakeWriter(
        old_dataset,
        DatasetDescriptor(
            source_id=SOURCE_ID,
            dataset_id="producao-poco-abertos",
            alias="producao-poco-abertos",
            partition_keys=["ano"],
            partition_types=partition_types_for(["ano"]),
        ),
    )
    writer.write_polars(
        pl.DataFrame({"x": [1, 2, 3]}), zpath, partitions={"ano": "2005"}
    )
    old = list(old_dataset.rglob("producao-poco-da_2005.parquet"))
    assert len(old) == 1
    # outro Parquet do mesmo dataset, de outro ZIP, que não pode sair
    other = old_dataset / "ano=2006" / "producao-poco-da_2006.parquet"
    other.parent.mkdir(parents=True)
    other.write_bytes(old[0].read_bytes())

    res = converter.convert(tmp_path / "raw", lake, force=True)
    assert not res.errors, res.errors
    assert not old[0].exists()
    assert other.exists()
    names = sorted(p.stem for p in old_dataset.rglob("*.parquet"))
    assert names == [
        "producao-poco-da_2005__2005_producao_mar",
        "producao-poco-da_2005__2005_producao_terra",
        "producao-poco-da_2006",
    ]
    assert scan_dataset(old_dataset / "ano=2005").collect().height == 8  # sem dobrar

    # sem force também (o skip dos membros não impede a limpeza)
    old[0].parent.mkdir(exist_ok=True)
    writer.write_polars(pl.DataFrame({"x": [1]}), zpath, partitions={"ano": "2005"})
    res2 = converter.convert(tmp_path / "raw", lake)
    assert res2.converted == 0 and res2.skipped == 2
    assert not old[0].exists()


def test_upgrade_nao_apaga_o_antigo_se_um_membro_falhar(tmp_path: Path) -> None:
    import polars as pl
    from quantilica.analytics.lake import LakeWriter
    from quantilica.core.lake import DatasetDescriptor

    group = "movimentacao-derivados"
    zpath = _zip(
        _group_dir(tmp_path, group) / "mdpg-trr@20261104.zip",
        {
            "TRR_Vendas_Dist_Atual.csv": "Ano;Q\n2024;1\n",
            "TRR_Vendas_TRR_Atual.xlsx": b"nao e uma planilha",
        },
    )
    old_dataset = tmp_path / "lake" / SOURCE_ID / "movimentacao-derivados"
    LakeWriter(
        old_dataset,
        DatasetDescriptor(
            source_id=SOURCE_ID,
            dataset_id="movimentacao-derivados",
            alias="movimentacao-derivados",
        ),
    ).write_polars(pl.DataFrame({"x": [1]}), zpath)
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert len(res.errors) == 1
    assert (old_dataset / "mdpg-trr.parquet").exists()


def test_id_de_tabela_inexistente_e_dataset_desconhecido(tmp_path: Path) -> None:
    group = "movimentacao-derivados"
    _zip(
        _group_dir(tmp_path, group) / "mdpg-asfalto@20261104.zip",
        {
            "Asfalto_Vendas_Distribuidor_Atual.csv": "Ano;Q\n2024;1\n",
            "Asfalto_Vendas_Distribuidor_UF_Atual.csv": "Ano;Q\n2024;1\n",
        },
    )
    res = converter.convert(
        tmp_path / "raw",
        tmp_path / "lake",
        datasets=["movimentacao-derivados-nao-existe"],
    )
    assert res.errors == ["dataset desconhecido: movimentacao-derivados-nao-existe"]
    assert not (tmp_path / "lake").exists()


def test_convert_de_ppg_presal_grava_so_o_presal(tmp_path: Path) -> None:
    _zip(
        _group_dir(tmp_path, "ppg") / "producao-poco_2018@20261105.zip",
        {
            "2018/2018_producao_mar.csv": _poco_csv("M", 3),
            "2018/2018_producao_presal.csv": _poco_csv("P", 2),
            "2018/2018_producao_terra.csv": _poco_csv("T", 4),
        },
    )
    res = converter.convert(
        tmp_path / "raw", tmp_path / "lake", datasets=["ppg-presal"]
    )
    assert not res.errors, res.errors
    assert res.converted == 1
    assert [p.name for p in (tmp_path / "lake" / SOURCE_ID).iterdir()] == ["ppg-presal"]
    df = scan_dataset(tmp_path / "lake" / SOURCE_ID / "ppg-presal").collect()
    assert df.height == 2 and set(df["ambiente"].to_list()) == {"presal"}


def test_membro_com_nome_cp437_e_em_subpasta(tmp_path: Path) -> None:
    # o nome do membro fica em cp437 (sem a marca UTF-8): "produc╞o_terra"
    path = _zip(
        _group_dir(tmp_path, "producao-poco-abertos")
        / "producao-poco-da_2015@20261105.zip",
        {
            "2015/sub/2015_producao_mar.csv": _poco_csv("M", 2),
            "2015/sub/2015_producao_produc_o_terra.csv": _poco_csv("T", 3),
        },
    )
    path.write_bytes(path.read_bytes().replace(b"produc_o_terra", b"produc\xc6o_terra"))
    with zipfile.ZipFile(path) as zf:
        assert any("produc╞o" in n for n in zf.namelist())
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    df = scan_dataset(tmp_path / "lake" / SOURCE_ID / "producao-poco-abertos").collect()
    assert df.group_by("ambiente").len().sort("ambiente").rows() == [
        ("mar", 2),
        ("terra", 3),
    ]
    assert _files(tmp_path / "lake" / SOURCE_ID / "producao-poco-abertos") == [
        "producao-poco-da_2015__2015_producao_mar",
        "producao-poco-da_2015__2015_producao_produco_terra",
    ]


def test_skip_nao_extrai_nem_hasheia_cada_membro(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from anp_fetcher import lake

    _zip(
        _group_dir(tmp_path, "producao-poco-abertos")
        / "producao-poco-da_2005@20261105.zip",
        {
            "a_producao_mar.csv": _poco_csv("M", 2),
            "a_producao_terra.csv": _poco_csv("T", 2),
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res.converted == 2

    extracted: list[str] = []
    real = lake.extract_zip_member
    monkeypatch.setattr(
        lake,
        "extract_zip_member",
        lambda *a, **k: extracted.append(a[1]) or real(*a, **k),
    )
    hashed: list[object] = []
    import quantilica.analytics.lake as analytics_lake

    real_sha = analytics_lake.sha256_file
    for module in (analytics_lake, lake):
        monkeypatch.setattr(
            module,
            "sha256_file",
            lambda p, *a, **k: hashed.append(p) or real_sha(p, *a, **k),
        )
    lake._DIGESTS.clear()
    res2 = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res2.converted == 0 and res2.skipped == 2
    assert extracted == []
    assert len(hashed) == 1  # o ZIP é lido uma vez, não uma por membro


def test_cabecalho_real_no_csv_com_titulo_subcabecalho_e_linha_repetida(
    tmp_path: Path,
) -> None:
    sub = ";;ANP;Operador;;;;;;;;Associado;Não Associado;Gás Total"
    cabecalho = (
        "Estado;Bacia;Nome Poço;;Campo;Operador;Contrato;Período;Óleo;Cond;Petr;"
        "Gás Natural (Mm³/dia);;"
    )
    topo = [
        "ANP - Agência Nacional do Petróleo;;;;Data: 15/03/2019;;;;;;;;;",
        "SIGEP Produção;;;;;;;;;;;;;",
        cabecalho,
        sub,
        "BA;Recôncavo;1-A-1-BA;1A 0001 BA;CAMPO;Petro;480000;2005/01;1,5;0;1,5;1;2;3",
        cabecalho,
        sub,
        "SE;Sergipe;1-B-1-SE;1B 0001 SE;OUTRO;Petro;480001;2005/01;2,5;0;2,5;1;2;3",
    ]
    _zip(
        _group_dir(tmp_path, "producao-poco-abertos")
        / "producao-poco-da_2005@20261105.zip",
        {
            "a_producao_mar.csv": "\n".join(topo) + "\n",
            "a_producao_terra.csv": "\n".join(topo) + "\n",
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    df = scan_dataset(tmp_path / "lake" / SOURCE_ID / "producao-poco-abertos").collect()
    assert (
        df.height == 4
    )  # só as linhas de dado; título, subcabeçalho e repetições fora
    assert df.columns[:4] == ["Estado", "Bacia", "Nome Poço ANP", "Nome Poço Operador"]
    assert "Gás Natural (Mm³/dia) Gás Total" in df.columns
    assert "Gás Natural (Mm³/dia) Não Associado" in df.columns
    assert not any(c.startswith(("__UNNAMED__", "Data:", "ANP -")) for c in df.columns)
    assert df["Estado"].to_list().count("Estado") == 0


def test_upgrade_remove_o_dataset_que_ficou_sem_dados(tmp_path: Path) -> None:
    import polars as pl
    from quantilica.analytics.lake import LakeWriter
    from quantilica.core.lake import DatasetDescriptor

    group = "amostras-rochas-fluidos"
    zpath = _zip(
        _group_dir(tmp_path, group) / "arf-consolidacao-2017@20261105.zip",
        {
            "c/consolidacao-calha-2017.csv": "Bacia sedimentar;Total de caixas\nA;1\n",
            "c/consolidacao-fluidos-2017.csv": "Bacia sedimentar;Volume (L)\nA;1,5\n",
        },
    )
    old_dataset = tmp_path / "lake" / SOURCE_ID / group
    LakeWriter(
        old_dataset,
        DatasetDescriptor(source_id=SOURCE_ID, dataset_id=group, alias=group),
    ).write_polars(pl.DataFrame({"x": [1]}), zpath)
    assert (old_dataset / "arf-consolidacao-2017.parquet").exists()
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert not res.errors, res.errors
    assert not old_dataset.exists()
    assert sorted(p.name for p in (tmp_path / "lake" / SOURCE_ID).iterdir()) == [
        "amostras-rochas-fluidos-calha",
        "amostras-rochas-fluidos-fluidos",
    ]


@pytest.mark.parametrize(
    ("member", "expected"),
    [
        ("2015/2015_01_produc╞o_terra.csv", "terra"),
        ("2022_08_producao_Terra.xlsx", "terra"),
        ("2023_12_producao_PreSal.csv", "presal"),
        ("2021_10_producao_Mar (2).xlsx", "mar"),
        ("2021_10_producao_presal (1).xlsx", "presal"),
        ("2021_10_producao_terra_1.xlsx", "terra"),
        ("2020/2020_producao_marte.csv", None),
        ("leia-me.csv", None),
    ],
)
def test_ambiente_do_nome_do_membro(member: str, expected: str | None) -> None:
    from anp_fetcher.lake import _ambiente

    assert _ambiente(member) == expected


def _seed(dataset: Path, key: str, partitions: dict[str, str] | None = None) -> Path:
    """Grava um Parquet de uma conversão anterior: ``file_key`` = ``key``."""
    import polars as pl
    from quantilica.analytics.lake import LakeWriter
    from quantilica.core.lake import DatasetDescriptor, partition_types_for

    keys = list(partitions or {})
    LakeWriter(
        dataset,
        DatasetDescriptor(
            source_id=SOURCE_ID,
            dataset_id=dataset.name,
            alias=dataset.name,
            partition_keys=keys,
            partition_types=partition_types_for(keys),
        ),
    ).write_polars(
        pl.DataFrame({"x": [1]}), None, partitions=partitions, file_key_name=key
    )
    (path,) = dataset.rglob(f"{key}.parquet")
    return path


def test_logistica_edicao_antiga_no_zip_avisa_e_nada_antigo_sobra(
    tmp_path: Path,
) -> None:
    group = "movimentacao-derivados"
    cab = "Ano;Q\n2024;1\n"
    nova = [
        "DADOS ABERTOS - LOGISTICA 01 - ABASTECIMENTO NACIONAL DE COMBUSTÍVEIS.csv",
        "DADOS ABERTOS - LOGISTICA 02 - VENDAS NO MERCADO BRASILEIRO.csv",
        "DADOS ABERTOS - LOGISTICA 03 - VENDAS CONGÊNERES DE DISTRIBUIDORES.csv",
    ]
    antiga = [
        "DADOS ABERTOS - LOGISTICA DO ABASTECIMENTO NACIONAL DE COMBUSTÍVEIS.csv",
        "DADOS ABERTOS - VENDAS CONGÊNERES DE DISTRIBUIDORES.csv",
    ]
    zpath = _zip(
        _group_dir(tmp_path, group) / "mdpg-logistica@20261104.zip",
        {name: cab for name in [*nova, *antiga]},
    )
    base = tmp_path / "lake" / SOURCE_ID
    from quantilica.core.lake import composite_file_key

    # o que a conversão anterior deixou: os cinco membros (a edição antiga também)
    # nos datasets em que cada um caía, e o Parquet do layout mais antigo ainda
    stale = [
        _seed(
            base / "movimentacao-derivados-logistica-abastecimento-nacional",
            composite_file_key(zpath, antiga[0]),
        ),
        _seed(
            base / "movimentacao-derivados-logistica-vendas-congeneres",
            composite_file_key(zpath, antiga[1]),
        ),
        _seed(base / "movimentacao-derivados", composite_file_key(zpath)),
    ]
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res.errors == []
    assert len(res.warnings) == 2  # a edição antiga fica fora, com aviso
    assert not any(p.exists() for p in stale)
    assert not (base / "movimentacao-derivados").exists()
    assert sorted(p.name for p in base.iterdir()) == [
        "movimentacao-derivados-logistica-abastecimento-nacional",
        "movimentacao-derivados-logistica-vendas-congeneres",
        "movimentacao-derivados-logistica-vendas-mercado",
    ]
    assert _files(base / "movimentacao-derivados-logistica-vendas-congeneres") == [
        "mdpg-logistica__dados_abertos_logistica_03_vendas_congeneres_de_distribuidores"
    ]
    assert (
        scan_dataset(base / "movimentacao-derivados-logistica-abastecimento-nacional")
        .collect()
        .height
        == 1
    )


def test_zip_que_passa_de_varios_membros_para_um_so_nao_deixa_os_antigos(
    tmp_path: Path,
) -> None:
    group_dir = _group_dir(tmp_path, "producao-poco-abertos")
    zname = "producao-poco-da_2005@20261105.zip"
    _zip(
        group_dir / zname,
        {
            "a_producao_mar.csv": _poco_csv("M", 3),
            "a_producao_terra.csv": _poco_csv("T", 2),
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res.converted == 2
    dataset = tmp_path / "lake" / SOURCE_ID / "producao-poco-abertos"
    assert len(_files(dataset)) == 2

    # edição nova do ZIP, só com o mar: o terra de antes não pode ficar
    _zip(group_dir / zname, {"a_producao_mar.csv": _poco_csv("M", 4)})
    res2 = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res2.errors == []
    assert _files(dataset) == ["producao-poco-da_2005"]
    assert scan_dataset(dataset).collect().height == 4


def test_limpeza_fica_nos_datasets_do_grupo_e_nao_alcanca_outro_grupo(
    tmp_path: Path,
) -> None:
    group = "pp"
    zpath = _zip(
        _group_dir(tmp_path, group) / "pp-x_2020@20261105.zip",
        {"a.csv": "Ano;Q\n2020;1\n", "b.csv": "Ano;Q\n2020;2\n"},
    )
    from quantilica.core.lake import file_key

    key = file_key(zpath)  # chave antiga do ZIP
    base = tmp_path / "lake" / SOURCE_ID
    mine = _seed(base / "pp", key, {"ano": "2020"})
    other = _seed(base / "pp-abertos", key, {"ano": "2020"})  # outro grupo, mesma chave
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res.errors == []
    assert not mine.exists()
    assert other.exists()


def test_sha_cached_serializa_threads_e_restaura_o_original() -> None:
    import threading

    import quantilica.analytics.lake as analytics_lake

    from anp_fetcher import lake

    original = analytics_lake.sha256_file
    seen: list[tuple[str, str]] = []
    barrier = threading.Barrier(2)

    def run(name: str) -> None:
        barrier.wait()
        with lake._sha_cached(Path(f"/x/{name}"), f"digest-{name}"):
            seen.append((name, analytics_lake.sha256_file(Path(f"/x/{name}"))))

    threads = [threading.Thread(target=run, args=(n,)) for n in ("a", "b")]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sorted(seen) == [("a", "digest-a"), ("b", "digest-b")]
    assert analytics_lake.sha256_file is original


_COM_DESCRICAO = (
    "Ano;Mês;Agente Regulado;Código do Produto;Nome do Produto;Descrição do Produto;"
    "UF Origem;Quantidade de Produto (mil m³)\n"
)


def _historico_zip(tmp_path: Path, antigo: str) -> None:
    _zip(
        _group_dir(tmp_path, "movimentacao-derivados") / "mdpg-liquidos@20261104.zip",
        {
            "Liquidos_Vendas_Historico_2018_a_2023.csv": _COM_DESCRICAO
            + "2018;1;A;320102001;Gasolina C;GASOLINA C COMUM;RJ;1,5\n"
            + "2018;2;B;810101001;Etanol Hidratado;ETANOL HIDRATADO;SP;2,5\n",
            "Liquidos_Vendas_Historico_2007_a_2017.csv": antigo,
        },
    )


def test_membro_sem_cabecalho_ganha_os_nomes_do_irmao_sem_perder_linha(
    tmp_path: Path,
) -> None:
    # a 1ª linha do membro de 2007-2017 é dado; falta a coluna "Descrição do Produto"
    _historico_zip(
        tmp_path,
        "2007;1;ABENGOA;810101001;Etanol Hidratado;SP;1,98\n"
        "2007;2;ABENGOA;810101001;Etanol Hidratado;SP;0,02\n"
        "2008;1;USINA;320102001;Gasolina C;RJ;3,10\n",
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res.errors == []
    historico = (
        tmp_path
        / "lake"
        / SOURCE_ID
        / "movimentacao-derivados-liquidos-vendas-historico"
    )
    todos = scan_dataset(historico).collect()
    antigo = todos.filter(pl.col("Ano").is_in(["2007", "2008"]))
    assert antigo.height == 3  # nenhuma linha virou nome de coluna
    assert todos.height == 5
    assert "Código do Produto" in todos.columns
    # o irmão tem "Descrição do Produto" a mais: vazia no membro antigo
    assert antigo["Descrição do Produto"].null_count() == 3
    assert sorted(antigo["Nome do Produto"].to_list()) == [
        "Etanol Hidratado",
        "Etanol Hidratado",
        "Gasolina C",
    ]  # "Descrição do Produto" saiu, não "Nome do Produto"
    assert not any(c.isdigit() for c in antigo.columns)


def test_membro_sem_cabecalho_com_largura_diferente_e_erro_claro(
    tmp_path: Path,
) -> None:
    _historico_zip(tmp_path, "2007;1;ABENGOA\n2007;2;ABENGOA\n")
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert len(res.errors) == 1
    assert "Liquidos_Vendas_Historico_2007_a_2017.csv" in res.errors[0]
    assert "sem cabeçalho" in res.errors[0]
    assert "nomes não inferíveis" in res.errors[0]


def test_membro_com_cabecalho_nao_muda(tmp_path: Path) -> None:
    _historico_zip(
        tmp_path,
        _COM_DESCRICAO + "2007;1;ABENGOA;810101001;Etanol Hidratado;ETANOL;SP;1,98\n",
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res.errors == []
    historico = (
        tmp_path
        / "lake"
        / SOURCE_ID
        / "movimentacao-derivados-liquidos-vendas-historico"
    )
    assert scan_dataset(historico).collect().height == 3


def test_membro_sem_cabecalho_de_mesma_largura_usa_os_nomes_do_irmao(
    tmp_path: Path,
) -> None:
    cabecalho = "Ano;Mês;Agente Regulado;Quantidade\n"
    _zip(
        _group_dir(tmp_path, "movimentacao-derivados") / "mdpg-liquidos@20261104.zip",
        {
            "Liquidos_Vendas_Historico_2018_a_2023.csv": cabecalho
            + "2018;1;A;1,5\n2018;2;B;2,5\n",
            "Liquidos_Vendas_Historico_2007_a_2017.csv": "2007;1;ABENGOA;1,98\n",
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert res.errors == []
    historico = (
        tmp_path
        / "lake"
        / SOURCE_ID
        / "movimentacao-derivados-liquidos-vendas-historico"
    )
    todos = scan_dataset(historico).collect()
    assert todos.height == 3
    assert todos.filter(pl.col("Ano") == "2007")["Agente Regulado"].to_list() == [
        "ABENGOA"
    ]


def test_membro_sem_cabecalho_de_mesma_largura_com_ordem_trocada_e_erro(
    tmp_path: Path,
) -> None:
    cabecalho = "Ano;Mês;Agente Regulado;Quantidade\n"
    _zip(
        _group_dir(tmp_path, "movimentacao-derivados") / "mdpg-liquidos@20261104.zip",
        {
            "Liquidos_Vendas_Historico_2018_a_2023.csv": cabecalho
            + "2018;1;A;1,5\n2018;2;B;2,5\n",
            # quantidade antes do agente: o tipo de cada posição não bate
            "Liquidos_Vendas_Historico_2007_a_2017.csv": "2007;1;1,98;ABENGOA\n",
        },
    )
    res = converter.convert(tmp_path / "raw", tmp_path / "lake")
    assert len(res.errors) == 1
    assert "2007_a_2017" in res.errors[0]
    assert "a ordem das colunas não bate" in res.errors[0]
