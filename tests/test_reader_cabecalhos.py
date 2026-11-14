"""Cabeçalhos de CSV da ANP que viravam nomes de coluna inválidos no lake."""

from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("fastexcel")

from anp_fetcher.reader import MAX_COLUMN_NAME, read_csv, read_file  # noqa: E402


def _valid(names: list[str]) -> bool:
    return all(
        n.strip()
        and len(n) <= MAX_COLUMN_NAME
        and not any(ord(c) < 32 or 127 <= ord(c) <= 159 for c in n)
        for n in names
    ) and len(names) == len(set(names))


def test_delimitador_sobrando_no_cabecalho_descarta_coluna_vazia(
    tmp_path: Path,
) -> None:
    # amostras-rochas-fluidos, multas, acervo-dados-tecnicos: "a;b;" + "1;2;"
    src = tmp_path / "multas.csv"
    src.write_text("a;b;\n1;2;\n3;4;\n", encoding="latin-1")
    df = read_csv(src, {})
    assert df.columns == ["a", "b"]
    assert df.height == 2


def test_coluna_de_nome_vazio_com_dados_ganha_nome_estavel(tmp_path: Path) -> None:
    # producao-poco-abertos: "Nome Poço;;Campo" (célula mesclada com valores)
    src = tmp_path / "producao-poco.csv"
    src.write_text("Nome Poço;;Campo\nP1;ANP;C1\nP2;ANP;C2\n", encoding="latin-1")
    df = read_csv(src, {})
    assert df.columns == ["Nome Poço", "coluna_2", "Campo"]
    assert df["coluna_2"].to_list() == ["ANP", "ANP"]


def test_varias_colunas_vazias(tmp_path: Path) -> None:
    src = tmp_path / "x.csv"
    src.write_text("a;;;d;;\n1;x;;4;;\n2;y;;5;;\n", encoding="latin-1")
    df = read_csv(src, {})
    # só a coluna 2 tem valores; as outras vazias somem
    assert df.columns == ["a", "coluna_2", "d"]
    assert _valid(df.columns)


def test_csv_com_virgula_nao_vira_uma_coluna_so(tmp_path: Path) -> None:
    # producao-mar, armazenagem-terminais...: cabeçalho "Ano,Mês/Ano,Estado"
    src = tmp_path / "producao-mar.csv"
    src.write_text("Ano,Mês/Ano,Estado\n2020,01/2020,RJ\n2021,02/2021,SP\n", "latin-1")
    df = read_csv(src, {})
    assert df.columns == ["Ano", "Mês/Ano", "Estado"]
    assert df.height == 2


def test_virgula_vence_ponto_e_virgula_solto_em_nome(tmp_path: Path) -> None:
    src = tmp_path / "x.csv"
    src.write_text("Ano,Valor (R$; mil),UF\n2020,1,RJ\n", encoding="utf-8")
    assert read_csv(src, {}).columns == ["Ano", "Valor (R$; mil)", "UF"]


def test_ponto_e_virgula_continua_o_padrao(tmp_path: Path) -> None:
    src = tmp_path / "x.csv"
    src.write_text("Nome;Descricao, longa;UF\nA;b, c;RJ\n", encoding="utf-8")
    assert read_csv(src, {}).columns == ["Nome", "Descricao, longa", "UF"]


@pytest.mark.parametrize("codec", ["utf-16", "utf-16-le", "utf-16-be"])
def test_utf16_com_e_sem_bom(tmp_path: Path, codec: str) -> None:
    # comercializacao-gn: UTF-16 LE com BOM, nomes entre aspas
    src = tmp_path / "cgn-produtores.csv"
    text = (
        '"Ano";"Mês";"Preço em Reais por MMBtu"\r\n'
        '"2020";"1";"3,5"\r\n"2021";"2";"4,0"\r\n'
    )
    src.write_bytes(text.encode(codec))
    df = read_csv(src, {})
    assert df.columns == ["Ano", "Mês", "Preço em Reais por MMBtu"]
    assert df.height == 2
    assert df["Mês"].to_list() == ["1", "2"]
    assert df["Preço em Reais por MMBtu"].to_list() == ["3,5", "4,0"]


def test_nome_com_quebra_de_linha_entre_aspas(tmp_path: Path) -> None:
    # producao-poco-abertos, amostras-rochas-fluidos: "PCS GP\n(kJ/m³)"
    src = tmp_path / "x.csv"
    src.write_text('a;"PCS GP\n(kJ/m³)";b\n1;2;3\n', encoding="utf-8")
    df = read_csv(src, {})
    assert df.columns == ["a", "PCS GP (kJ/m³)", "b"]


def test_nomes_validos_nao_sao_alterados(tmp_path: Path) -> None:
    # só nome inválido é corrigido: espaços das pontas e repetidos ficam como estão
    src = tmp_path / "x.csv"
    src.write_text("Valor  de Venda; Data da Coleta \n1;2\n", encoding="utf-8")
    assert read_csv(src, {}).columns == ["Valor  de Venda", " Data da Coleta "]


def test_nome_longo_e_cortado_e_repetidos_ganham_sufixo(tmp_path: Path) -> None:
    longo = "x" * 300
    src = tmp_path / "x.csv"
    src.write_text(f"{longo};{longo}a;b\n1;2;3\n", encoding="utf-8")
    cols = read_csv(src, {}).columns
    assert _valid(cols)
    assert all(len(c) <= MAX_COLUMN_NAME for c in cols)
    assert cols[2] == "b"


def test_preambulo_de_titulo_antes_do_cabecalho(tmp_path: Path) -> None:
    # multas: título, linhas em branco, "RELAÇÃO DE MULTAS...", e só então o cabeçalho
    src = tmp_path / "multas-2022.csv"
    src.write_text(
        "ANP - Agência Nacional do Petroleo;;;\n"
        ";;;\n"
        "RELAÇÃO DE MULTAS APLICADAS EM 2022;;;\n"
        ";;;\n"
        "Status Processo;Superintendência;Número do Processo;Valor\n"
        "Pago;SFI-BA;486110;33000,00\n"
        "Aberto;SFI-DF;486111;10,00\n",
        encoding="utf-8",
    )
    df = read_csv(src, {})
    assert df.columns == [
        "Status Processo",
        "Superintendência",
        "Número do Processo",
        "Valor",
    ]
    assert df.height == 2
    assert df["Status Processo"].to_list() == ["Pago", "Aberto"]


def test_linha_de_grupos_mesclados_antes_do_cabecalho(tmp_path: Path) -> None:
    # acervo-dados-tecnicos: "INFORMAÇÕES GERAIS;;;OUTRAS" e o cabeçalho na 2ª linha
    src = tmp_path / "adt.csv"
    src.write_text(
        "INFORMAÇÕES GERAIS;;;;;OUTRAS\nPoço;Extensão;Fonte;Topo;Base;Nota\n"
        "P1;pdf;ANP;1;2;x\n",
        encoding="utf-8",
    )
    df = read_csv(src, {})
    assert df.columns == ["Poço", "Extensão", "Fonte", "Topo", "Base", "Nota"]
    assert df.height == 1


def test_cabecalho_normal_nao_e_promovido(tmp_path: Path) -> None:
    # a 2ª linha tem a mesma densidade e não vira cabeçalho
    src = tmp_path / "x.csv"
    src.write_text("a;b;c\nx;y;z\n1;2;3\n", encoding="utf-8")
    df = read_csv(src, {})
    assert df.columns == ["a", "b", "c"]
    assert df.height == 2


def test_cp850_nao_deixa_controle_no_nome(tmp_path: Path) -> None:
    # multas-2024/2025: bytes DOS; em latin-1, "ê" (0x88) é caractere de controle
    src = tmp_path / "multas-2025.csv"
    src.write_bytes(
        "Status Processo;Superintendência;Número do Processo;Razão Social\n"
        "Pago;SFI-BA;486110;PETRÓLEO LTDA\n".encode("cp850")
    )
    df = read_csv(src, {})
    assert df.columns == [
        "Status Processo",
        "Superintendência",
        "Número do Processo",
        "Razão Social",
    ]
    assert df["Razão Social"].to_list() == ["PETRÓLEO LTDA"]


def test_latin1_comum_nao_vira_cp850(tmp_path: Path) -> None:
    src = tmp_path / "x.csv"
    src.write_bytes("Estado;Município\nSP;São Paulo\n".encode("latin-1"))
    df = read_csv(src, {})
    assert df.columns == ["Estado", "Município"]
    assert df["Município"].to_list() == ["São Paulo"]


def test_read_file_aplica_a_limpeza_aos_csv(tmp_path: Path) -> None:
    src = tmp_path / "producao-fdp-mar.csv"
    src.write_text("Ano,Estado,\n2020,RJ,\n", encoding="latin-1")
    assert read_file(src, {}).columns == ["Ano", "Estado"]


def test_json_com_chave_de_controle(tmp_path: Path) -> None:
    src = tmp_path / "x.json"
    src.write_text('[{"a\\nb": 1, "": 2}]', encoding="utf-8")
    assert _valid(read_file(src, {}).columns)


def test_separador_pela_consistencia_das_colunas(tmp_path: Path) -> None:
    # vírgulas dentro dos nomes não fazem do "," o separador
    src = tmp_path / "x.csv"
    src.write_text(
        "Produto;Preço (R$/l, média, mínimo);Unidade (m³, kg)\n"
        "GASOLINA;5,49;m³\nETANOL;3,99;m³\n",
        encoding="utf-8",
    )
    df = read_csv(src, {})
    assert df.columns == ["Produto", "Preço (R$/l, média, mínimo)", "Unidade (m³, kg)"]
    assert df.height == 2


def test_cabecalho_real_com_poucos_nomes_nao_e_promovido(tmp_path: Path) -> None:
    # "A;;;" + "1;x;y;z": a 2ª linha é dado (tem número), não cabeçalho
    src = tmp_path / "x.csv"
    src.write_text("A;;;\n1;x;y;z\n2;x;y;z\n", encoding="utf-8")
    df = read_csv(src, {})
    assert df.columns[0] == "A"
    assert df.height == 2
    assert df["A"].to_list() == ["1", "2"]


def test_preambulo_nao_pula_linha_de_dado(tmp_path: Path) -> None:
    # linha com 60% preenchida entre o título e a candidata: não é preâmbulo
    src = tmp_path / "x.csv"
    src.write_text("Título;;;;\nA;B;C;;\nx;y;z;w;v\n", encoding="utf-8")
    assert read_csv(src, {}).columns[0] == "Título"


def test_apostrofo_cp1252_nao_vira_cp850(tmp_path: Path) -> None:
    # distribuidores-cessao-espaco, pdi-projetos-rt: 0x92 é o apóstrofo do cp1252
    src = tmp_path / "x.csv"
    texto = "Razão Social;Município\nSTARBUCKS D\x92ÁVILA;SANTA BÁRBARA D\x92OESTE\n"
    src.write_bytes(texto.encode("latin-1"))
    df = read_csv(src, {})
    assert df.columns == ["Razão Social", "Município"]
    assert "Á" in df["Razão Social"][0]
    assert df["Município"][0].startswith("SANTA BÁRBARA D")


def test_mac_roman(tmp_path: Path) -> None:
    # prorrogacoes-708: "Prorrogação" e "1º" em mac_roman
    src = tmp_path / "prorrogacoes-708.csv"
    src.write_bytes(
        "Efetivação da Prorrogação;1º e 2º PE\nsim;não\n".encode("mac_roman")
    )
    assert read_csv(src, {}).columns == ["Efetivação da Prorrogação", "1º e 2º PE"]


def test_encoding_fixo_no_spec_nao_e_adivinhado(tmp_path: Path) -> None:
    src = tmp_path / "x.csv"
    src.write_bytes("Município;Ação\nSP;1\n".encode())
    assert read_csv(src, {"encoding": "utf-8"}).columns == ["Município", "Ação"]


def test_transcodificacao_nao_deixa_lixo_ao_lado_do_arquivo(
    tmp_path: Path, monkeypatch
) -> None:
    scratch = tmp_path / "scratch"
    scratch.mkdir()
    monkeypatch.setenv("QUANTILICA_LAKE_SCRATCH", str(scratch))
    bruto = tmp_path / "bruto"
    bruto.mkdir()
    src = bruto / "cgn.csv"
    src.write_bytes("Ano;Mês\n2020;1\n".encode("utf-16"))
    assert read_csv(src, {}).columns == ["Ano", "Mês"]
    assert [p.name for p in bruto.iterdir()] == ["cgn.csv"]
    assert list(scratch.iterdir()) == []


def test_apostrofo_cp1252_em_arquivo_curto_nao_vira_mac_roman(tmp_path: Path) -> None:
    src = tmp_path / "x.csv"
    src.write_bytes(b"NOME;x\nATEM\x92S;1\n")
    df = read_csv(src, {})
    # segue o caminho de sempre (latin-1), como no main; nada de "ATEMíS"
    assert df["NOME"].to_list() == ["ATEM\x92S"]


def _planilha(path: Path, rows: list[list[object]]) -> Path:
    xlsxwriter = pytest.importorskip("xlsxwriter")
    book = xlsxwriter.Workbook(str(path))
    sheet = book.add_worksheet()
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            if value is not None:
                sheet.write(i, j, value)
    book.close()
    return path


def test_planilha_de_producao_acha_o_cabecalho_de_dois_niveis(tmp_path: Path) -> None:
    from anp_fetcher.wrangling import spec_for

    cab = ["Estado", "Bacia", "Nome Poço", None, "Período", "Gás Natural (Mm³/dia)"]
    sub = [None, None, "ANP", "Operador", None, "Associado", "Total"]
    cab += [None]
    path = _planilha(
        tmp_path / "2005_producao_mar.xlsx",
        [
            ["ANP - Agência Nacional do Petróleo"],
            [None, None, None, None, "Data: 29/03/2019"],
            [],
            cab,
            sub,
            ["BA", "Recôncavo", "1-A-1-BA", "1A 0001", "2005/01", 1.5, 2.5],
            cab,  # cabeçalho repetido no meio dos dados
            sub,
            ["SE", "Sergipe", "1-B-1-SE", "1B 0001", "2005/02", 3.5, 4.5],
        ],
    )
    df = read_file(path, spec_for("ppg"))
    assert df.columns == [
        "Estado",
        "Bacia",
        "Nome Poço ANP",
        "Nome Poço Operador",
        "Período",
        "Gás Natural (Mm³/dia) Associado",
        "Gás Natural (Mm³/dia) Total",
    ]
    assert df.height == 2
    assert df["Estado"].to_list() == ["BA", "SE"]
    assert _valid(df.columns)


def test_planilha_sem_cabecalho_de_producao_nao_muda(tmp_path: Path) -> None:
    # grupo sem a opção de cabeçalho: o comportamento anterior fica
    path = _planilha(tmp_path / "x.xlsx", [["a", "b"], [1, 2]])
    assert read_file(path, {}).columns == ["a", "b"]
