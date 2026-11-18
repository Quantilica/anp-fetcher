"""O build sem mudança não abre ZIP nem lê o bruto: só stat, sidecar e rodapé."""

from __future__ import annotations

import builtins
import hashlib
import io
import json
import zipfile
from pathlib import Path

import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")
import quantilica.core.manifests as manifests  # noqa: E402

import anp_fetcher.lake as lake_mod  # noqa: E402
from anp_fetcher.lake import converter  # noqa: E402
from anp_fetcher.storage import _GROUP_DIRS  # noqa: E402

GLP = "shpc-glp"
POCO = "producao-poco-abertos"
CSV = (
    "Regiao;Estado;Municipio;Produto;Valor de Venda;Valor de Compra\n"
    "SE;SP;SAO PAULO;GLP;{valor};80,00\n"
)
POCO_CSV = (
    "Estado;Bacia;Nome Poço;Período;Óleo (bbl/dia)\nBA;Recôncavo;{p}-1-BA;2005/01;1,5\n"
)


def _sidecar(arquivo: Path) -> None:
    dados = arquivo.read_bytes()
    arquivo.with_name(arquivo.name + ".manifest.json").write_text(
        json.dumps(
            {"sha256": hashlib.sha256(dados).hexdigest(), "size_bytes": len(dados)}
        ),
        encoding="utf-8",
    )


def _zip(path: Path, membros: dict[str, str]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as zf:
        for nome, conteudo in membros.items():
            zf.writestr(nome, conteudo)
    _sidecar(path)
    return path


def _bruto(tmp_path: Path) -> Path:
    raw = tmp_path / "raw"
    glp = raw / _GROUP_DIRS[GLP]
    glp.mkdir(parents=True)
    # ZIP de um membro só (vai inteiro) e um CSV avulso
    _zip(glp / f"{GLP}_2024-05@20240601.zip", {"a.csv": CSV.format(valor="105,50")})
    csv = glp / f"{GLP}_2024-06@20240701.csv"
    csv.write_text(CSV.format(valor="99,90"), encoding="utf-8")
    _sidecar(csv)
    # ZIP com vários membros de dados (um item por membro)
    _zip(
        raw / _GROUP_DIRS[POCO] / "producao-poco-da_2005@20261105.zip",
        {
            "2005/2005_producao_mar.csv": POCO_CSV.format(p="M"),
            "2005/2005_producao_terra.csv": POCO_CSV.format(p="T"),
        },
    )
    return raw


@pytest.fixture
def aberturas(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """ZIPs abertos (``ZipFile``/``is_zipfile``) e membros/arquivos lidos."""
    abertos: list[str] = []
    original_zip, original_is = zipfile.ZipFile, zipfile.is_zipfile

    def espia_zip(file, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003
        abertos.append(f"ZipFile:{Path(file).name}")
        return original_zip(file, *args, **kwargs)

    def espia_is(file, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003
        abertos.append(f"is_zipfile:{Path(file).name}")
        return original_is(file, *args, **kwargs)

    monkeypatch.setattr(zipfile, "ZipFile", espia_zip)
    monkeypatch.setattr(zipfile, "is_zipfile", espia_is)
    for modulo, nome in (
        (lake_mod, "read_file"),
        (lake_mod, "extract_zip_member"),
        (lake_mod, "decompress"),
    ):
        original = getattr(modulo, nome)

        def espia(*args, _o=original, _n=nome, **kwargs):  # noqa: ANN002, ANN003
            abertos.append(f"{_n}:{Path(args[0]).name}")
            return _o(*args, **kwargs)

        monkeypatch.setattr(modulo, nome, espia)
    return abertos


@pytest.fixture
def sem_hash_por_leitura(monkeypatch: pytest.MonkeyPatch) -> None:
    def falha(path):  # noqa: ANN001, ANN202
        raise AssertionError(f"bruto lido para o sha256: {path}")

    monkeypatch.setattr(manifests, "sha256_file", falha)


def test_segunda_rodada_de_zip_inteiro_nao_abre_o_zip(
    tmp_path: Path, aberturas: list[str], sem_hash_por_leitura: None
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake, datasets=[GLP])
    assert not res.errors, res.errors
    assert res.converted == 2 and res.skipped == 0
    assert any(a.startswith("ZipFile:") for a in aberturas)

    aberturas.clear()
    res2 = converter.convert(raw, lake, datasets=[GLP])
    assert not res2.errors, res2.errors
    assert res2.converted == 0 and res2.skipped == 2
    assert aberturas == []


def test_zip_de_varios_membros_so_abre_o_indice_e_nao_le_membro(
    tmp_path: Path, aberturas: list[str], sem_hash_por_leitura: None
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake, datasets=[POCO])
    assert not res.errors, res.errors
    assert res.converted == 2

    aberturas.clear()
    res2 = converter.convert(raw, lake, datasets=[POCO])
    assert not res2.errors, res2.errors
    assert res2.converted == 0 and res2.skipped == 2
    # o índice do ZIP é aberto para rotear os membros (e isso é o que não dá para
    # evitar sem registro por membro no lake); nada é extraído nem lido
    assert aberturas
    assert all(a.startswith(("ZipFile:", "is_zipfile:")) for a in aberturas)


def test_zip_novo_converte(tmp_path: Path, aberturas: list[str]) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[GLP])
    novo = raw / _GROUP_DIRS[GLP] / f"{GLP}_2024-05@20240801.zip"
    _zip(novo, {"a.csv": CSV.format(valor="111,00")})

    aberturas.clear()
    res = converter.convert(raw, lake, datasets=[GLP])
    assert not res.errors, res.errors
    assert res.converted == 1 and res.skipped == 1
    assert any(a.startswith("read_file:") for a in aberturas)


def test_force_reconverte_zip_em_dia(tmp_path: Path) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[GLP])
    res = converter.convert(raw, lake, datasets=[GLP], force=True)
    assert not res.errors, res.errors
    assert res.converted == 2 and res.skipped == 0


def test_sem_datasets_continua_convertendo_tudo(tmp_path: Path) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake)
    assert not res.errors, res.errors
    assert res.converted == 4
    res2 = converter.convert(raw, lake)
    assert res2.converted == 0 and res2.skipped == 4


def test_zip_gravado_inteiro_por_conversor_antigo_ainda_e_reaberto(
    tmp_path: Path,
) -> None:
    """Sem a versão no rodapé não há prova de membro único: o ZIP é roteado."""
    import polars as pl
    from quantilica.analytics.lake import LakeWriter
    from quantilica.core.lake import DatasetDescriptor, partition_types_for

    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    zpath = raw / _GROUP_DIRS[POCO] / "producao-poco-da_2005@20261105.zip"
    LakeWriter(
        lake / "anp" / POCO,
        DatasetDescriptor(
            source_id="anp",
            dataset_id=POCO,
            alias=POCO,
            partition_keys=["ano"],
            partition_types=partition_types_for(["ano"]),
        ),
    ).write_polars(pl.DataFrame({"x": [1]}), zpath, partitions={"ano": "2005"})

    res = converter.convert(raw, lake, datasets=[POCO])

    assert not res.errors, res.errors
    assert res.converted == 2  # um Parquet por membro; o inteiro sai
    nomes = sorted(p.stem for p in (lake / "anp" / POCO).rglob("*.parquet"))
    assert nomes == [
        "producao-poco-da_2005__2005_producao_mar",
        "producao-poco-da_2005__2005_producao_terra",
    ]


ZIP_POCO = "producao-poco-da_2005@20261105.zip"
MEMBROS = [
    "producao-poco-da_2005__2005_producao_mar",
    "producao-poco-da_2005__2005_producao_terra",
]


def _gravar_inteiro(raw: Path, lake: Path, tag: str) -> Path:
    """O ZIP de vários membros gravado inteiro (um Parquet com a chave do ZIP)."""
    import polars as pl
    from quantilica.analytics.lake import LakeWriter
    from quantilica.core.lake import DatasetDescriptor, partition_types_for

    zpath = raw / _GROUP_DIRS[POCO] / ZIP_POCO
    LakeWriter(
        lake / "anp" / POCO,
        DatasetDescriptor(
            source_id="anp",
            dataset_id=POCO,
            alias=POCO,
            partition_keys=["ano"],
            partition_types=partition_types_for(["ano"]),
        ),
    ).write_polars(
        pl.DataFrame({"x": [1]}), zpath, partitions={"ano": "2005"}, converter=tag
    )
    return zpath


def _nomes(lake: Path) -> list[str]:
    return sorted(p.stem for p in (lake / "anp" / POCO).rglob("*.parquet"))


def test_force_reroteia_o_zip_que_o_lake_tem_inteiro(
    tmp_path: Path, aberturas: list[str]
) -> None:
    """O registro de ZIP inteiro dispensa abrir o ZIP, mas não vale com force."""
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    _gravar_inteiro(raw, lake, lake_mod._converter_tag())
    aberturas.clear()

    sem_force = converter.convert(raw, lake, datasets=[POCO])
    assert (sem_force.converted, sem_force.skipped, sem_force.errors) == (0, 1, [])
    assert aberturas == []
    assert _nomes(lake) == ["producao-poco-da_2005"]

    res = converter.convert(raw, lake, datasets=[POCO], force=True)

    assert not res.errors, res.errors
    assert res.converted == 2 and res.skipped == 0
    assert _nomes(lake) == MEMBROS  # um por membro; o inteiro saiu


@pytest.mark.parametrize(
    "tag",
    [
        "anp-fetcher 2.12.0 roteamento=2",  # roteamento de outra revisão
        "anp-fetcher 99.0.0",  # versão futura sem revisão: não se presume
        "anp-fetcher 2.6.2",  # anterior aos membros (lia só o primeiro)
        "quantilica-analytics",
    ],
)
def test_so_a_mesma_revisao_de_roteamento_dispensa_abrir_o_zip(
    tmp_path: Path, tag: str
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    _gravar_inteiro(raw, lake, tag)

    res = converter.convert(raw, lake, datasets=[POCO])

    assert not res.errors, res.errors
    assert res.converted == 2
    assert _nomes(lake) == MEMBROS


@pytest.mark.parametrize(
    "tag",
    [
        "anp-fetcher 2.11.1",
        "anp-fetcher 2.10.0",
        "anp-fetcher 2.9.0",
        "anp-fetcher 2.8.0",  # a versão do lake real
        "anp-fetcher 2.7.0",  # a primeira que separa os membros do ZIP
    ],
)
def test_gravado_antes_da_revisao_no_rodape_vale_como_revisao_1(
    tmp_path: Path, aberturas: list[str], tag: str
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    _gravar_inteiro(raw, lake, tag)
    aberturas.clear()

    res = converter.convert(raw, lake, datasets=[POCO])

    assert (res.converted, res.skipped, res.errors) == (0, 1, [])
    assert aberturas == []


def test_o_rodape_grava_versao_e_revisao_de_roteamento(tmp_path: Path) -> None:
    import pyarrow.parquet as pq

    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[GLP])
    for parquet in (lake / "anp" / GLP).rglob("*.parquet"):
        tag = pq.ParquetFile(parquet).metadata.metadata[b"quantilica.converter"]
        assert tag.decode().endswith(f" roteamento={lake_mod._ROUTING_REVISION}")


def test_sha256_com_erro_de_es_no_roteamento_nao_derruba_o_convert(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[GLP])

    def falha(path):  # noqa: ANN001, ANN202
        raise OSError(5, "Input/output error")

    monkeypatch.setattr(lake_mod, "_digest", falha)

    res = converter.convert(raw, lake, datasets=[GLP])  # não levanta

    assert res.errors  # cada item reporta o erro; o ZIP foi roteado abrindo-o
    assert res.converted == 0


def test_conversao_interrompida_num_membro_de_zip_e_completada(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    original = type(converter)._write_item

    def cai_no_segundo(writer, group, spec, item, source_path, result):  # noqa: ANN001, ANN202
        if item.member and "terra" in item.member:
            raise RuntimeError("sem espaço em disco")
        return original(writer, group, spec, item, source_path, result)

    with monkeypatch.context() as m:
        m.setattr(type(converter), "_write_item", staticmethod(cai_no_segundo))
        r1 = converter.convert(raw, lake, datasets=[POCO])
    assert (r1.converted, len(r1.errors)) == (1, 1)

    r2 = converter.convert(raw, lake, datasets=[POCO])
    assert (r2.converted, r2.skipped, r2.errors) == (1, 1, [])
    r3 = converter.convert(raw, lake, datasets=[POCO])
    assert (r3.converted, r3.skipped, r3.errors) == (0, 2, [])
    assert _nomes(lake) == MEMBROS


@pytest.fixture
def sem_abrir_csv(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):  # noqa: ANN201
    """Devolve ``armar()``: depois dela, nenhum CSV do bruto é aberto (``open``,
    ``io.open`` ou ``Path.open``). ZIPs e sidecars podem."""
    raiz = str((tmp_path / "raw").resolve())

    def vigia(original):  # noqa: ANN001, ANN202
        def aberto(file, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003, ANN202
            nome = str(file) if isinstance(file, str | Path) else ""
            if nome.startswith(raiz) and nome.lower().endswith(".csv"):
                raise AssertionError(f"bruto aberto: {nome}")
            return original(file, *args, **kwargs)

        return aberto

    def armar() -> None:
        monkeypatch.setattr(builtins, "open", vigia(builtins.open))
        monkeypatch.setattr(io, "open", vigia(io.open))
        original_path_open = Path.open

        def path_open(self, *args, **kwargs):  # noqa: ANN001, ANN002, ANN003, ANN202
            return vigia(lambda f, *a, **k: original_path_open(Path(f), *a, **k))(
                self, *args, **kwargs
            )

        monkeypatch.setattr(Path, "open", path_open)

    return armar


def test_segunda_rodada_nao_abre_csv_do_bruto(
    tmp_path: Path, sem_abrir_csv, sem_hash_por_leitura: None
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    assert not converter.convert(raw, lake).errors
    sem_abrir_csv()
    res = converter.convert(raw, lake)
    assert (res.converted, res.skipped, res.errors) == (0, 4, [])
