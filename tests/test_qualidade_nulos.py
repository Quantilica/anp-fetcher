"""Valores inválidos: sentinela vira nulo e conta; lixo falha, salvo tolerância."""

from __future__ import annotations

import datetime as dt
import json
import logging
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")
import polars as pl  # noqa: E402
import pyarrow.parquet as pq  # noqa: E402
from quantilica.analytics.lake import check_dataset  # noqa: E402

from anp_fetcher.lake import SOURCE_ID, converter  # noqa: E402
from anp_fetcher.reader import (  # noqa: E402
    DEFAULT_NULL_VALUES,
    META_CAST_NULLS,
    META_QUALITY,
    QualityReport,
    _read_na_values,
    normalize_dtypes,
    read_csv,
)
from anp_fetcher.storage import _GROUP_DIRS  # noqa: E402
from anp_fetcher.wrangling import DEFAULT_SPEC, convert_one, spec_for  # noqa: E402

NUM = {"numeric_columns": ["VENDAS"]}


def _norm(valores, spec=NUM):
    report = QualityReport()
    out = normalize_dtypes(pl.DataFrame({"VENDAS": valores}), spec, report=report)
    return out, report


# ---------------------------------------------------------------------------
# sentinelas (null_values)
# ---------------------------------------------------------------------------


def test_sentinela_vira_nulo_e_conta():
    out, rep = _norm(["10,5", "-", " N/D ", "n/d", "--", "...", "*", "ND", "2"])
    assert out["VENDAS"].to_list() == [
        10.5,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        2.0,
    ]
    col = rep.columns["VENDAS"]
    assert col.sentinels == {
        "-": 1,
        "N/D": 1,
        "n/d": 1,
        "--": 1,
        "...": 1,
        "*": 1,
        "ND": 1,
    }
    assert col.invalid == 0 and col.invalid_examples == []
    assert rep.rows == 9
    assert rep.has_loss


def test_celula_vazia_conta_mas_nao_e_perda():
    out, rep = _norm(["1", "", "  ", "3"])
    assert out["VENDAS"].to_list() == [1.0, None, None, 3.0]
    assert rep.columns["VENDAS"].sentinels == {"": 2}
    assert not rep.has_loss
    assert rep.summary().endswith("— ")  # nada a avisar


def test_valor_sem_nada_a_registrar_deixa_o_relatorio_vazio():
    out, rep = _norm(["1", "2,5"])
    assert out["VENDAS"].to_list() == [1.0, 2.5]
    assert rep.columns == {}
    assert rep.to_metadata() == {}
    assert not rep.has_loss


def test_null_values_do_grupo_substitui_a_lista_mas_vazio_vale_sempre():
    spec = {**NUM, "null_values": ["X"]}
    out, rep = _norm(["1", "x", ""], spec)
    assert out["VENDAS"].to_list() == [1.0, None, None]
    assert rep.columns["VENDAS"].sentinels == {"": 1, "x": 1}
    # "-" deixou de ser ausência declarada neste grupo: é lixo e derruba o arquivo.
    with pytest.raises(ValueError, match="VENDAS.*'-'"):
        _norm(["1", "-"], spec)


def test_sentinela_em_coluna_de_texto_e_conteudo_nao_perda():
    df = pl.DataFrame({"VENDAS": ["1", "2"], "Produto": ["-", "N/D"]})
    rep = QualityReport()
    out = normalize_dtypes(df, NUM, report=rep)
    assert out["Produto"].to_list() == ["-", "N/D"]
    assert rep.columns == {}


def test_sentinela_em_data():
    df = pl.DataFrame({"Data": ["03/01/2019", "-", "", "N/D"]})
    rep = QualityReport()
    out = normalize_dtypes(df, {"date_columns": {"Data": "%d/%m/%Y"}}, report=rep)
    assert out["Data"].to_list() == [dt.date(2019, 1, 3), None, None, None]
    assert rep.columns["Data"].sentinels == {"-": 1, "": 1, "N/D": 1}


def test_normalize_dtypes_sem_report_continua_funcionando():
    out = normalize_dtypes(pl.DataFrame({"VENDAS": ["1", "-"]}), NUM)
    assert out["VENDAS"].to_list() == [1.0, None]


def test_padrao_do_grupo_traz_a_lista_e_tolerancia_zero():
    plano = {"", "-", "--", "N/D", "ND", "...", "*"}
    # além dos sete da ANP, os que o leitor comum de CSV já anulava sem registro
    legado = {"NA", "n.a.", "n.d.", "não disp", "-9999"}
    assert set(DEFAULT_NULL_VALUES) == plano | legado
    assert DEFAULT_SPEC["null_values"] == list(DEFAULT_NULL_VALUES)
    assert DEFAULT_SPEC["max_invalid_frac"] == 0.0
    assert spec_for("vdpb-abertos")["null_values"] == list(DEFAULT_NULL_VALUES)


def test_marcador_legado_do_leitor_agora_e_contado():
    out, rep = _norm(["1", "NA", "n.a.", "-9999", "não disp", "n.d."])
    assert out["VENDAS"].to_list() == [1.0, None, None, None, None, None]
    assert rep.columns["VENDAS"].sentinels == {
        "NA": 1,
        "n.a.": 1,
        "-9999": 1,
        "não disp": 1,
        "n.d.": 1,
    }


def test_leitura_so_anula_o_vazio_em_grupo_tipado():
    # grupo sem colunas tipadas: leitura como era (o leitor comum anula "-" e "N/D")
    assert _read_na_values({"separator": ";"}) is None
    # com colunas tipadas, só o campo vazio é nulo na leitura, qualquer que seja o
    # ``null_values`` do grupo: o resto chega à conversão, que conta ou rejeita
    assert _read_na_values(spec_for("vdpb-abertos")) == [""]
    assert _read_na_values({"numeric_columns": ["V"], "null_values": ["-"]}) == [""]


def test_null_values_reduzido_nao_deixa_marcador_sumir_na_leitura(tmp_path):
    # "N/D" e "-9999" não estão no ``null_values`` deste grupo: antes o leitor os
    # anulava na coluna tipada sem contar nem falhar.
    src = tmp_path / "a.csv"
    src.write_text(
        "PRODUTO;VENDAS\nGLP;-\nGLP;N/D\nGLP;-9999\nGLP;5\n", encoding="utf-8"
    )
    spec = {**DEFAULT_SPEC, "numeric_columns": ["VENDAS"], "null_values": ["-"]}
    df = read_csv(src, spec)
    assert df["VENDAS"].to_list() == ["-", "N/D", "-9999", "5"]
    with pytest.raises(ValueError, match="VENDAS.*'N/D'"):
        normalize_dtypes(df, spec)
    # dentro da tolerância, vira nulo e conta
    rep = QualityReport()
    out = normalize_dtypes(df, {**spec, "max_invalid_frac": 0.5}, report=rep)
    assert out["VENDAS"].to_list() == [None, None, -9999.0, 5.0]
    assert rep.columns["VENDAS"].sentinels == {"-": 1}
    assert rep.columns["VENDAS"].invalid_examples == ["N/D"]


def test_ie_abertos_e_pb_abertos_tratam_9999_como_valor():
    for grupo in ("ie-abertos", "pb-abertos"):
        assert "-9999" not in spec_for(grupo)["null_values"]
        out, rep = _norm(
            ["-9999", "-"], spec_for(grupo) | {"numeric_columns": ["VENDAS"]}
        )
        assert out["VENDAS"].to_list() == [-9999.0, None]
    assert "-9999" in spec_for("vdpb-abertos")["null_values"]


def test_coluna_sem_nome_so_com_marcador_continua_descartada(tmp_path):
    # ";" a mais no fim do cabeçalho e "-" numa linha: a coluna sem nome só tem
    # ausência e some, como no leitor antigo (não vira ``coluna_5`` toda nula).
    src = tmp_path / "a.csv"
    src.write_text("ANO;PRODUTO;VENDAS;\n2020;GLP;5;\n2021;GLP;6;-\n", encoding="utf-8")
    spec = {**DEFAULT_SPEC, "numeric_columns": ["VENDAS"]}
    assert read_csv(src, spec).columns == ["ANO", "PRODUTO", "VENDAS"]
    # com valor de verdade, a coluna fica
    src.write_text(
        "ANO;PRODUTO;VENDAS;\n2020;GLP;5;x\n2021;GLP;6;-\n", encoding="utf-8"
    )
    df = read_csv(src, spec)
    assert df.columns == ["ANO", "PRODUTO", "VENDAS", "coluna_4"]
    assert df["coluna_4"].to_list() == ["x", None]


def test_preambulo_com_marcador_ainda_acha_o_cabecalho(tmp_path):
    # a linha de "-" é preâmbulo (para o leitor antigo era vazia), não o cabeçalho
    src = tmp_path / "a.csv"
    src.write_text(
        "TITULO;;;\n-;-;-;-\nANO;PRODUTO;VENDAS;OBS\n2020;GLP;5;a\n",
        encoding="utf-8",
    )
    spec = {**DEFAULT_SPEC, "numeric_columns": ["VENDAS"]}
    assert read_csv(src, spec).columns == ["ANO", "PRODUTO", "VENDAS", "OBS"]


def test_tolerancia_pelos_valores_nao_nulos_e_nao_pelas_linhas():
    # coluna esparsa: 2 valores, 1 inválido = 50% dos valores (não 1% das linhas)
    valores = [None] * 98 + ["1", "abc"]
    df = pl.DataFrame({"VENDAS": valores}, schema={"VENDAS": pl.String})
    with pytest.raises(ValueError, match="50.00% dos valores não nulos"):
        normalize_dtypes(df, {**NUM, "max_invalid_frac": 0.05})
    out = normalize_dtypes(df, {**NUM, "max_invalid_frac": 0.5})
    assert out["VENDAS"].null_count() == 99


def test_texto_de_grupo_tipado_segue_anulado_como_antes(tmp_path):
    # A leitura deixa o marcador chegar à coluna tipada para contá-lo, mas o texto
    # continua saindo como saía: "-" e "N/D" em coluna de texto viram nulo.
    raw_dir = _raw(tmp_path, "2020;1;-;5\n2020;2;N/D;-\n2020;3;ND;7\n")
    res = converter.convert(raw_dir, tmp_path / "lake")
    assert not res.errors, res.errors
    df = pl.read_parquet(next((tmp_path / "lake" / SOURCE_ID).rglob("*.parquet")))
    assert df["PRODUTO"].to_list() == [
        None,
        None,
        "ND",
    ]  # "ND" nunca foi marcador do leitor
    assert df["VENDAS"].to_list() == [5.0, None, 7.0]
    # só a coluna tipada entra no relatório
    assert json.loads(_footer(tmp_path / "lake")["anp.quality"])["null_sentinels"] == {
        "VENDAS": {"-": 1}
    }


# ---------------------------------------------------------------------------
# lixo: erro, salvo tolerância (max_invalid_frac)
# ---------------------------------------------------------------------------


def test_lixo_com_tolerancia_zero_continua_falhando():
    with pytest.raises(ValueError, match="VENDAS") as exc:
        _norm(["10,5", "abc"])
    assert "'abc'" in str(exc.value) and "1 valor(es)" in str(exc.value)


def test_lixo_abaixo_da_tolerancia_vira_nulo_e_conta():
    valores = ["1"] * 97 + ["abc", "x" * 60, "abc"]
    out, rep = _norm(valores, {**NUM, "max_invalid_frac": 0.05})
    assert out["VENDAS"].null_count() == 3
    col = rep.columns["VENDAS"]
    assert col.invalid == 3
    assert col.invalid_examples == ["abc", "x" * 39 + "…"]  # distintos, truncados
    assert col.sentinels == {}
    assert rep.has_loss


def test_tolerancia_na_fronteira_e_inclusiva():
    valores = ["1"] * 9 + ["abc"]
    out, rep = _norm(valores, {**NUM, "max_invalid_frac": 0.1})
    assert out["VENDAS"].null_count() == 1
    assert rep.columns["VENDAS"].invalid == 1


def test_lixo_acima_da_tolerancia_levanta_com_coluna_e_exemplos():
    valores = ["1"] * 8 + ["abc", "def"]
    with pytest.raises(ValueError) as exc:
        _norm(valores, {**NUM, "max_invalid_frac": 0.1})
    msg = str(exc.value)
    assert "'VENDAS'" in msg and "2 valor(es)" in msg
    assert "['abc', 'def']" in msg
    assert "20.00% dos valores não nulos" in msg and "tolerância 10.00%" in msg


def test_exemplos_sao_no_maximo_cinco():
    valores = ["1"] * 90 + [f"lixo{i}" for i in range(8)] + ["2", "3"]
    _, rep = _norm(valores, {**NUM, "max_invalid_frac": 0.1})
    col = rep.columns["VENDAS"]
    assert col.invalid == 8
    assert col.invalid_examples == [f"lixo{i}" for i in range(5)]


def test_data_invalida_dentro_da_tolerancia():
    df = pl.DataFrame({"Data": ["03/01/2019"] * 9 + ["2019-01-03"]})
    spec = {"date_columns": {"Data": "%d/%m/%Y"}, "max_invalid_frac": 0.1}
    rep = QualityReport()
    out = normalize_dtypes(df, spec, report=rep)
    assert out["Data"].null_count() == 1
    assert rep.columns["Data"].invalid == 1
    assert rep.columns["Data"].invalid_examples == ["2019-01-03"]
    with pytest.raises(ValueError, match="Data"):
        normalize_dtypes(df, {**spec, "max_invalid_frac": 0.0})


def test_sentinela_e_lixo_na_mesma_coluna():
    valores = ["1"] * 18 + ["-", "abc"]
    out, rep = _norm(valores, {**NUM, "max_invalid_frac": 0.1})
    assert out["VENDAS"].null_count() == 2
    col = rep.columns["VENDAS"]
    assert col.sentinels == {"-": 1}
    assert col.invalid == 1  # a sentinela não conta contra a tolerância
    assert col.lost == 2


# ---------------------------------------------------------------------------
# formato dos metadados
# ---------------------------------------------------------------------------


def test_to_metadata_formato():
    _, rep = _norm(["1"] * 18 + ["-", "abc"], {**NUM, "max_invalid_frac": 0.1})
    meta = rep.to_metadata()
    assert set(meta) == {META_QUALITY, META_CAST_NULLS}
    assert META_QUALITY == "anp.quality" and META_CAST_NULLS == "quantilica.cast_nulls"
    assert json.loads(meta[META_QUALITY]) == {
        "rows": 20,
        "null_sentinels": {"VENDAS": {"-": 1}},
        "invalid_to_null": {"VENDAS": {"count": 1, "examples": ["abc"]}},
    }
    assert json.loads(meta[META_CAST_NULLS]) == {"VENDAS": 1}


def test_to_metadata_so_sentinela_nao_escreve_cast_nulls():
    _, rep = _norm(["1", "-"])
    assert set(rep.to_metadata()) == {META_QUALITY}


def test_resumo_para_o_log():
    _, rep = _norm(["1"] * 18 + ["-", "abc"], {**NUM, "max_invalid_frac": 0.1})
    resumo = rep.summary()
    assert "20 linhas" in resumo and "'VENDAS'" in resumo
    assert "'-' x1" in resumo and "1 inválido(s)" in resumo and "['abc']" in resumo


# ---------------------------------------------------------------------------
# conversão para o lake
# ---------------------------------------------------------------------------

CABECALHO = "ANO;MES;PRODUTO;VENDAS\n"


def _raw(tmp_path: Path, linhas: str, group: str = "vdpb-abertos") -> Path:
    raw_dir = tmp_path / "raw"
    group_dir = raw_dir / _GROUP_DIRS[group]
    group_dir.mkdir(parents=True)
    (group_dir / "vdpb-a-segmento.csv").write_text(CABECALHO + linhas, encoding="utf-8")
    return raw_dir


def _footer(lake_dir: Path) -> dict[str, str]:
    parquets = sorted((lake_dir / SOURCE_ID).rglob("*.parquet"))
    assert len(parquets) == 1
    meta = pq.ParquetFile(parquets[0]).metadata.metadata
    return {k.decode(): v.decode() for k, v in meta.items()}


def test_lake_arquivo_com_traco_em_vendas_converte_com_contagem(tmp_path, caplog):
    raw_dir = _raw(
        tmp_path, "2020;1;GLP;100,5\n2020;2;GLP;-\n2020;3;GLP;N/D\n2020;4;GLP;  \n"
    )
    lake_dir = tmp_path / "lake"
    with caplog.at_level(logging.WARNING, logger="anp_fetcher"):
        res = converter.convert(raw_dir, lake_dir)
    assert not res.errors, res.errors
    assert res.converted == 1
    footer = _footer(lake_dir)
    quality = json.loads(footer["anp.quality"])
    assert quality == {
        "rows": 4,
        "null_sentinels": {"VENDAS": {"": 1, "-": 1, "N/D": 1}},
    }
    assert "quantilica.cast_nulls" not in footer
    # os metadados do core seguem lá
    assert footer["quantilica.dataset_id"] and footer["quantilica.file_key"]
    assert check_dataset(next((lake_dir / SOURCE_ID).iterdir())) == []
    df = pl.read_parquet(next((lake_dir / SOURCE_ID).rglob("*.parquet")))
    assert df["VENDAS"].to_list() == [100.5, None, None, None]
    # aviso no log e no resultado, com o arquivo
    assert any(
        "vdpb-a-segmento.csv" in r.getMessage() and "'-' x1" in r.getMessage()
        for r in caplog.records
    )
    assert len(res.warnings) == 1 and "vdpb-a-segmento.csv" in res.warnings[0]


def test_lake_arquivo_limpo_nao_grava_qualidade_nem_avisa(tmp_path):
    raw_dir = _raw(tmp_path, "2020;1;GLP;100,5\n2020;2;GLP;7\n")
    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert not res.errors and not res.warnings
    footer = _footer(lake_dir)
    assert "anp.quality" not in footer and "quantilica.cast_nulls" not in footer


def test_lake_so_celula_vazia_grava_contagem_sem_avisar(tmp_path, caplog):
    raw_dir = _raw(tmp_path, "2020;1;GLP;100,5\n2020;2;GLP;  \n")
    lake_dir = tmp_path / "lake"
    with caplog.at_level(logging.WARNING, logger="anp_fetcher"):
        res = converter.convert(raw_dir, lake_dir)
    assert not res.errors and not res.warnings
    assert not [r for r in caplog.records if r.levelno >= logging.WARNING]
    assert json.loads(_footer(lake_dir)["anp.quality"])["null_sentinels"] == {
        "VENDAS": {"": 1}
    }


def test_lake_lixo_continua_falhando_com_tolerancia_zero(tmp_path):
    raw_dir = _raw(tmp_path, "2020;1;GLP;100,5\n2020;2;GLP;abc\n")
    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert res.converted == 0
    assert len(res.errors) == 1
    assert "VENDAS" in res.errors[0] and "'abc'" in res.errors[0]
    assert not list((lake_dir / SOURCE_ID).rglob("*.parquet"))


def test_lake_lixo_dentro_da_tolerancia_do_grupo_converte(tmp_path, monkeypatch):
    # ``spec_for`` do topo do módulo: outro teste recarrega ``anp_fetcher.wrangling``,
    # e o conversor importado aqui usa a versão antiga.
    monkeypatch.setitem(
        spec_for.__globals__["PROCESSING_SPECS"],
        "vdpb-abertos",
        {"numeric_columns": ["VENDAS"], "max_invalid_frac": 0.3},
    )
    raw_dir = _raw(
        tmp_path, "2020;1;GLP;1\n2020;2;GLP;2\n2020;3;GLP;3\n2020;4;GLP;abc\n"
    )
    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert not res.errors, res.errors
    footer = _footer(lake_dir)
    assert json.loads(footer["anp.quality"])["invalid_to_null"] == {
        "VENDAS": {"count": 1, "examples": ["abc"]}
    }
    assert json.loads(footer["quantilica.cast_nulls"]) == {"VENDAS": 1}
    assert "1 inválido(s)" in res.warnings[0]


def test_lake_metadado_nao_vaza_para_a_escrita_seguinte(tmp_path):
    raw_dir = _raw(tmp_path, "2020;1;GLP;-\n")
    group_dir = raw_dir / _GROUP_DIRS["vdpb-abertos"]
    (group_dir / "vdpb-a-glp-tipo.csv").write_text(
        CABECALHO + "2020;1;GLP;5\n", encoding="utf-8"
    )
    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert not res.errors and res.converted == 2
    por_arquivo = {}
    for path in (lake_dir / SOURCE_ID).rglob("*.parquet"):
        meta = pq.ParquetFile(path).metadata.metadata
        por_arquivo[path.name] = b"anp.quality" in meta
    assert sorted(por_arquivo.values()) == [False, True]


def test_wrangling_convert_one_avisa_no_log(tmp_path, caplog):
    raw_dir = _raw(tmp_path, "2020;1;GLP;100,5\n2020;2;GLP;-\n")
    raw = raw_dir / _GROUP_DIRS["vdpb-abertos"] / "vdpb-a-segmento.csv"
    with caplog.at_level(logging.WARNING, logger="anp_fetcher.wrangling"):
        written = convert_one("vdpb-abertos", raw, tmp_path / "out")
    assert len(written) == 1
    assert pl.read_parquet(written[0])["VENDAS"].to_list() == [100.5, None]
    assert any("'-' x1" in r.getMessage() for r in caplog.records)
