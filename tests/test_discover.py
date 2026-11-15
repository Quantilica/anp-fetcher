"""Descoberta dos links mensais do SHPC (sem rede: página salva em fixture)."""

from __future__ import annotations

import datetime as dt
import json
import logging
from pathlib import Path

import pytest
from typer.testing import CliRunner

from anp_fetcher import discover as d
from anp_fetcher import plugin
from anp_fetcher.catalog import GROUPS, list_datasets

# A função real, guardada antes de o conftest trocá-la por uma que não usa a rede.
_DOWNLOAD_REAL = d._download_page
FIXTURE = Path(__file__).parent / "fixtures" / "shpc_pagina.html"
BASE = (
    "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan"
)
MENSAIS = ("shpc-diesel-gnv", "shpc-gasolina-etanol", "shpc-glp-mensal")

# Nomes de abril a setembro de 2026 que a ANP publicou fora do padrão; antes ficavam
# fixos no catálogo, hoje são só o gabarito da regra de classificação.
NOMES_2026 = {
    4: "04-dados-abertos-precos-{product}",
    5: "05-dados-abertos-precos-{product}.csv",
    6: "06-dados-abertos-precos-2026-06-{product}.csv",
    7: "07-dados-abertos-precos-{product}.csv",
    8: "08-dados-abertos-precos-2026-08-{product}.csv",
    9: "09-dados-abertos-precos-2026-09-{product}.csv",
}
PRODUTOS = {
    "diesel-gnv": "shpc-diesel-gnv",
    "gasolina-etanol": "shpc-gasolina-etanol",
    "glp": "shpc-glp-mensal",
}


@pytest.fixture
def html() -> str:
    return FIXTURE.read_text(encoding="utf-8")


@pytest.fixture(autouse=True)
def _cache_limpo():
    d.reset_cache()
    yield
    d.reset_cache()


def _sem_outubro(entries):
    return [e for e in entries if not (e["year"] == 2026 and e["month"] >= 10)]


# ---------------------------------------------------------------------------
# classificação
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("nome", "mes", "produto", "ext"),
    [
        ("04-dados-abertos-precos-diesel-gnv", 4, "diesel-gnv", "csv"),
        ("05-dados-abertos-precos-glp.csv", 5, "glp", "csv"),
        (
            "06-dados-abertos-precos-2026-06-gasolina-etanol.csv",
            6,
            "gasolina-etanol",
            "csv",
        ),
        ("02-cados-abertos-preco-gasolina-etanol.csv", 2, "gasolina-etanol", "csv"),
        ("10-glp.csv", 10, "glp", "csv"),
        ("11-qualquer_coisa_2026_11-diesel-gnv.xlsx", 11, "diesel-gnv", "xlsx"),
        ("12.dados.GLP.CSV", 12, "glp", "csv"),
        ("precos-glp-03.csv", 3, "glp", "csv"),
        ("precos-diesel-gnv-11.csv", 11, "diesel-gnv", "csv"),
    ],
)
def test_classifica_nomes(nome, mes, produto, ext):
    link = d.classify_href(f"{BASE}/2026/{nome}")
    assert link is not None
    assert (link.year, link.month, link.product, link.ext) == (2026, mes, produto, ext)
    assert link.url == f"{BASE}/2026/{nome}"


@pytest.mark.parametrize(
    "href",
    [
        f"{BASE}/2026/13-dados-abertos-precos-glp.csv",  # mês inválido
        f"{BASE}/2026/00-glp.csv",
        f"{BASE}/2026/metadados-glp.pdf",  # sem mês no início
        f"{BASE}/2026/04-dados-abertos-precos-etanol.csv",  # produto desconhecido
        f"{BASE}/2026/04-dados-abertos-precos-glp-extra.csv",  # produto não está no fim
        f"{BASE.replace('dsan', 'dsas')}/ca/ca-2025-02.zip",  # outra série
        "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos",
        "#topo",
        "",
    ],
)
def test_ignora_o_que_nao_e_mensal(href):
    assert d.classify_href(href) is None


def test_href_relativo_e_com_ancora():
    link = d.classify_href(
        "/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan/2027/01-glp.csv#x"
    )
    assert link is not None
    assert link.url == (
        "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/"
        "shpc/dsan/2027/01-glp.csv"
    )


def test_extract_links_da_fixture(html):
    links = d.extract_links(html)
    assert len(links) == 66  # 12 meses de 2025 e 10 de 2026, em 3 produtos
    assert {(link.year, link.month) for link in links} == {
        (2025, m) for m in range(1, 13)
    } | {(2026, m) for m in range(1, 11)}
    assert links == sorted(links)
    # ``a`` sem href, links repetidos e outras séries não entram.
    assert d.extract_links('<a name="x">y</a>' + '<a href="">z</a>') == []
    dup = (
        f'<a href="{BASE}/2026/10-glp.csv">a</a><a href="{BASE}/2026/10-glp.csv">b</a>'
    )
    assert len(d.extract_links(dup)) == 1


def test_regressao_nomes_irregulares_de_2026_geram_as_mesmas_18_urls(html):
    esperadas = {
        (PRODUTOS[produto], mes): f"{BASE}/2026/{nome.format(product=produto)}"
        for mes, nome in NOMES_2026.items()
        for produto in PRODUTOS
    }
    assert len(esperadas) == 18
    descobertas = {
        (link.group, link.month): link.url
        for link in d.extract_links(html)
        if link.year == 2026 and 4 <= link.month <= 9
    }
    assert descobertas == esperadas


def test_fevereiro_com_erro_de_digitacao(html):
    links = [
        link
        for link in d.extract_links(html)
        if (link.year, link.month, link.product) == (2026, 2, "gasolina-etanol")
    ]
    assert [link.url for link in links] == [
        f"{BASE}/2026/02-cados-abertos-preco-gasolina-etanol.csv"
    ]


# ---------------------------------------------------------------------------
# apply_links
# ---------------------------------------------------------------------------


def test_apply_links_troca_urls_de_2026_e_preserva_o_resto(html):
    links = d.extract_links(html)
    antes = list_datasets("shpc-glp-mensal")
    depois = d.apply_links(antes, links, group="shpc-glp-mensal")
    assert [e["id"] for e in depois] == [e["id"] for e in antes]
    por_mes = {e["month"]: e for e in depois if e["year"] == 2026}
    assert por_mes[4]["url"] == f"{BASE}/2026/04-dados-abertos-precos-glp"
    assert por_mes[4]["ext"] == "csv"
    assert por_mes[6]["url"].endswith("/06-dados-abertos-precos-2026-06-glp.csv")
    assert por_mes[10]["url"] == f"{BASE}/2026/10-glp.csv"
    assert all("fallback_urls" not in e for e in por_mes.values())
    # 2023-2025 seguem o catálogo estático, mesmo com links de 2025 na página.
    assert [e for e in depois if e["year"] < 2026] == [
        e for e in antes if e["year"] < 2026
    ]
    # O catálogo original não é alterado.
    assert "fallback_urls" in next(
        e for e in list_datasets("shpc-glp-mensal") if e["year"] == 2026
    )


def test_apply_links_nao_toca_nos_outros_produtos(html):
    links = d.extract_links(html)
    entries = list_datasets("shpc-diesel-gnv")
    out = d.apply_links(entries, links, group="shpc-diesel-gnv")
    assert all("glp" not in e["url"].split("/")[-1] for e in out if e["year"] == 2026)


def _html_sem_outubro(html: str) -> str:
    return "\n".join(
        linha for linha in html.splitlines() if "/dsan/2026/10-" not in linha
    )


def test_mes_novo_com_nome_irregular_entra_sem_editar_codigo(html):
    # Catálogo "de antes": sem outubro. A página perde o outubro real e ganha um com
    # nome inventado, que nenhuma regra anterior conhecia.
    extra = "".join(
        f'<a href="{BASE}/2026/10-preco_medio-2026_10-{p}.xlsx">Outubro</a>'
        for p in PRODUTOS
    )
    pagina = _html_sem_outubro(html).replace("</ul>", extra + "</ul>")
    links = d.extract_links(pagina)
    assert sum(1 for link in links if (link.year, link.month) == (2026, 10)) == 3
    for produto, grupo in PRODUTOS.items():
        entries = _sem_outubro(list_datasets(grupo))
        out = d.apply_links(entries, links, group=grupo)
        outubro = next(e for e in out if (e["year"], e["month"]) == (2026, 10))
        assert outubro["id"] == f"{grupo}-2026-10"
        assert outubro["url"] == f"{BASE}/2026/10-preco_medio-2026_10-{produto}.xlsx"
        assert outubro["ext"] == "xlsx"
        assert len(out) == len(entries) + 1
        assert [(e["year"], e["month"]) for e in out] == sorted(
            (e["year"], e["month"]) for e in out
        )


def test_mes_novo_inventado_vira_entrada_completa():
    link = f"{BASE}/2026/11-ref_2026-11_preco-gasolina-etanol.xlsx"
    links = d.extract_links(f'<a href="{link}">Novembro de 2026</a>')
    entries = _sem_outubro(list_datasets("shpc-gasolina-etanol"))
    out = d.apply_links(entries, links, group="shpc-gasolina-etanol")
    novo = out[-1]
    assert novo["id"] == "shpc-gasolina-etanol-2026-11"
    assert (novo["url"], novo["ext"]) == (link, "xlsx")
    assert (novo["year"], novo["month"], novo["semester"]) == (2026, 11, None)
    assert novo["base_id"] == "shpc-gasolina-etanol"
    assert "Novembro 2026" in novo["name"]
    assert "fallback_urls" not in novo


def test_anos_anteriores_a_2026_nunca_mudam_nem_entram():
    links = d.extract_links(f'<a href="{BASE}/2022/01-glp.csv">x</a>')
    entries = list_datasets("shpc-glp-mensal")
    assert d.apply_links(entries, links, group="shpc-glp-mensal") == entries


# ---------------------------------------------------------------------------
# uso pelo sync (entries_for_group / list_datasets_descoberto)
# ---------------------------------------------------------------------------


def test_sync_usa_links_descobertos_e_consulta_a_pagina_uma_vez(monkeypatch, html):
    chamadas = []
    monkeypatch.setattr(
        d, "_download_page", lambda client, url: chamadas.append(url) or html
    )
    for grupo in MENSAIS:
        entries = plugin.list_datasets_descoberto(grupo)
        por_mes = {e["month"]: e for e in entries if e["year"] == 2026}
        assert por_mes[10]["url"].endswith(
            "/2026/10-" + grupo.removeprefix("shpc-").removesuffix("-mensal") + ".csv"
        )
    assert chamadas == [d.SHPC_PAGE_URL]


def test_pagina_fora_do_ar_cai_para_a_url_presumida(monkeypatch, caplog):
    chamadas = []

    def falha(client, url):
        chamadas.append(url)
        raise OSError("sem rede")

    monkeypatch.setattr(d, "_download_page", falha)
    with caplog.at_level(logging.WARNING, logger="anp_fetcher.discover"):
        for grupo in MENSAIS:
            assert plugin.list_datasets_descoberto(grupo) == list_datasets(grupo)
    assert len(chamadas) == 1  # não insiste a cada grupo
    avisos = [r.getMessage() for r in caplog.records]
    assert len(avisos) == 1
    assert "sem rede" in avisos[0] and "URLs presumidas" in avisos[0]


def test_pagina_sem_links_mensais_tambem_cai_para_a_reserva(monkeypatch, caplog):
    monkeypatch.setattr(
        d, "_download_page", lambda client, url: "<html>Request Rejected</html>"
    )
    with caplog.at_level(logging.WARNING, logger="anp_fetcher.discover"):
        assert plugin.list_datasets_descoberto("shpc-glp-mensal") == list_datasets(
            "shpc-glp-mensal"
        )
    assert "nenhum link mensal" in caplog.text


def test_outros_grupos_e_alias_nao_consultam_a_pagina(monkeypatch):
    def nao_deve_chamar(client, url):
        raise AssertionError("não devia consultar a página")

    monkeypatch.setattr(d, "_download_page", nao_deve_chamar)
    assert plugin.list_datasets_descoberto("shpc-ca") == list_datasets("shpc-ca")
    assert plugin.list_datasets_descoberto("shpc-4s") == list_datasets("shpc-4s")
    assert plugin.list_datasets_descoberto("vdpb-abertos") == list_datasets(
        "vdpb-abertos"
    )
    assert plugin.list_datasets_descoberto() == list_datasets()


def test_download_page_usa_o_client_recebido_e_fecha_o_proprio(monkeypatch):
    class Falso:
        fechado = False

        def get_text(self, url):
            return f"<html>{url}</html>"

        def close(self):
            Falso.fechado = True

    recebido = Falso()
    assert _DOWNLOAD_REAL(recebido, "u") == "<html>u</html>"
    assert Falso.fechado is False  # quem passa o client é quem fecha

    import quantilica.core.http as http

    monkeypatch.setattr(http, "HttpClient", lambda **kw: Falso())
    assert _DOWNLOAD_REAL(None, "v") == "<html>v</html>"
    assert Falso.fechado is True


def test_fetch_links_levanta_sem_links(monkeypatch):
    monkeypatch.setattr(d, "_download_page", _DOWNLOAD_REAL)

    class Falso:
        def get_text(self, url):
            return "<html></html>"

    with pytest.raises(RuntimeError, match="nenhum link mensal"):
        d.fetch_links(Falso())


# ---------------------------------------------------------------------------
# discover() e o comando
# ---------------------------------------------------------------------------


def test_discover_lista_mes_fora_do_catalogo_e_nomes_diferentes(html):
    links = d.extract_links(html)
    catalogo = _sem_outubro([e for g in MENSAIS for e in list_datasets(g)])
    rel = d.discover(links, catalog=catalogo, today=dt.date(2026, 11, 3))
    assert {(i["group"], i["year"], i["month"]) for i in rel.new_months} == {
        (g, 2026, 10) for g in MENSAIS
    }
    assert rel.late == []
    assert rel.has_changes
    # abril, junho, agosto, setembro e o erro de fevereiro diferem do padrão presumido.
    meses = {(i["year"], i["month"]) for i in rel.url_differs}
    assert {(2026, 2), (2026, 4), (2026, 6), (2026, 8), (2026, 9)} <= meses
    assert rel.known == len(links)
    assert json.loads(json.dumps(rel.to_dict()))["has_changes"] is True


def test_discover_sem_novidade_com_o_catalogo_do_pacote(html):
    links = [
        link for link in d.extract_links(html) if link.year == 2026 and link.month < 10
    ]
    rel = d.discover(links, today=dt.date(2026, 11, 3))
    assert rel.new_months == []
    assert not rel.has_changes


def test_discover_aviso_de_atraso_depois_do_dia_15(html):
    links = d.extract_links(html)  # vai até outubro de 2026
    # Em 20/11 o mês anterior é outubro: está na página, sem atraso.
    assert d.discover(links, today=dt.date(2026, 11, 20)).late == []
    # Em 20/12 o mês anterior é novembro, que a página não tem.
    rel = d.discover(links, today=dt.date(2026, 12, 20))
    assert {(i["group"], i["year"], i["month"]) for i in rel.late} == {
        (g, 2026, 11) for g in MENSAIS
    }
    assert rel.has_changes
    # Até o dia 15 ainda é cedo.
    assert d.discover(links, today=dt.date(2026, 12, 15)).late == []
    # Janeiro olha dezembro do ano anterior.
    rel = d.discover(links, today=dt.date(2027, 1, 16))
    assert {(i["year"], i["month"]) for i in rel.late} == {(2026, 12)}


def test_discover_atraso_so_do_produto_que_falta(html):
    links = [
        link
        for link in d.extract_links(html)
        if not (link.product == "glp" and link.month == 10)
    ]
    rel = d.discover(links, today=dt.date(2026, 11, 20))
    assert [(i["group"], i["month"]) for i in rel.late] == [("shpc-glp-mensal", 10)]


def test_discover_baixa_a_pagina_quando_nao_recebe_links(monkeypatch, html):
    monkeypatch.setattr(d, "_download_page", lambda client, url: html)
    rel = d.discover(today=dt.date(2026, 11, 3))
    assert rel.known == 66
    assert rel.late == []


def test_discover_ano_anterior_a_2026_nao_gera_atraso(html):
    # Mesmo com a página vazia de 2025, não há "atraso" antes da era da descoberta.
    links = d.extract_links(html)
    assert d.discover(links, today=dt.date(2026, 1, 20)).late == []


def test_comando_discover_texto_e_json(monkeypatch, html):
    monkeypatch.setattr(d, "_download_page", lambda client, url: html)
    runner = CliRunner()
    monkeypatch.setattr(d, "_today", lambda: dt.date(2026, 11, 20))
    r = runner.invoke(plugin.app, ["discover"])
    assert r.exit_code == 0, r.output
    assert "66 link(s) mensais" in r.output
    assert "arquivo(s) com nome fora do padrão" in r.output
    assert "02-cados-abertos" not in r.output  # o detalhe fica no --json
    assert "ATRASO" not in r.output

    r = runner.invoke(plugin.app, ["discover", "--json", "--fail-on-change"])
    assert r.exit_code == 0, r.output
    dados = json.loads(r.output)
    assert dados["has_changes"] is False
    assert any("02-cados-abertos" in i["pagina"] for i in dados["url_differs"])


def test_comando_discover_fail_on_change_e_atraso(monkeypatch, html):
    monkeypatch.setattr(d, "_download_page", lambda client, url: html)
    monkeypatch.setattr(d, "_today", lambda: dt.date(2026, 12, 20))
    runner = CliRunner()
    r = runner.invoke(plugin.app, ["discover"])
    assert r.exit_code == 0
    assert "ATRASO   shpc-glp-mensal 2026-11" in r.output
    r = runner.invoke(plugin.app, ["discover", "--fail-on-change"])
    assert r.exit_code == 1


def test_comando_discover_mes_novo_no_texto(monkeypatch, html):
    novo = f'<a href="{BASE}/2026/12-surpresa-glp.csv">x</a>'
    monkeypatch.setattr(
        d, "_download_page", lambda client, url: html.replace("</ul>", novo + "</ul>")
    )
    r = CliRunner().invoke(plugin.app, ["discover"])
    assert r.exit_code == 0
    assert (
        f"NOVO     shpc-glp-mensal 2026-12: {BASE}/2026/12-surpresa-glp.csv" in r.output
    )


def test_comando_discover_pagina_fora_do_ar(monkeypatch):
    def falha(client, url):
        raise OSError("fora do ar")

    monkeypatch.setattr(d, "_download_page", falha)
    r = CliRunner().invoke(plugin.app, ["discover"])
    assert r.exit_code == 2
    assert "fora do ar" in r.output


def test_catalogo_estatico_tem_os_tres_grupos_mensais():
    for grupo in MENSAIS:
        assert grupo in GROUPS


# ---------------------------------------------------------------------------
# revisão: layout parcial, não reconhecidos, duplicatas, ano, falha, list
# ---------------------------------------------------------------------------


def _com(html: str, *hrefs: str) -> str:
    extra = "".join(f'<a href="{h}">x</a>' for h in hrefs)
    return html.replace("</ul>", extra + "</ul>")


def _sem_2026(html: str) -> str:
    return "\n".join(linha for linha in html.splitlines() if "/dsan/2026/" not in linha)


def test_pagina_sem_o_bloco_de_2026_e_erro_nao_reserva_silenciosa(monkeypatch, html):
    monkeypatch.setattr(d, "_today", lambda: dt.date(2026, 11, 3))
    monkeypatch.setattr(d, "_download_page", _DOWNLOAD_REAL)
    with pytest.raises(RuntimeError, match="2026 em diante"):
        d.fetch_page(_Cliente(_sem_2026(html)))


class _Cliente:
    def __init__(self, texto):
        self.texto = texto

    def get_text(self, url):
        return self.texto


def test_pagina_sem_2026_so_e_erro_a_partir_de_2026(monkeypatch, html):
    monkeypatch.setattr(d, "_today", lambda: dt.date(2025, 12, 20))
    monkeypatch.setattr(d, "_download_page", _DOWNLOAD_REAL)
    assert d.fetch_page(_Cliente(_sem_2026(html))).links


def test_sync_com_pagina_sem_2026_cai_para_a_reserva_com_aviso(
    monkeypatch, html, caplog
):
    monkeypatch.setattr(d, "_today", lambda: dt.date(2026, 11, 3))
    monkeypatch.setattr(d, "_download_page", lambda c, u: _sem_2026(html))
    with caplog.at_level(logging.WARNING, logger="anp_fetcher.discover"):
        assert plugin.list_datasets_descoberto("shpc-glp-mensal") == list_datasets(
            "shpc-glp-mensal"
        )
    assert "2026 em diante" in caplog.text


NAO_RECONHECIDOS = ["2026/2026-11-glp.csv", "2026/11-glp-p13.csv", "2026/1-glp.csv"]


def test_href_nao_reconhecido_e_devolvido(html):
    hrefs = [f"{BASE}/{n}" for n in NAO_RECONHECIDOS]
    page = d.extract_page(_com(html, *hrefs))
    assert page.unclassified == sorted(hrefs)
    assert len(page.links) == 66  # os reconhecidos não mudam
    # extensão que não é de dados, e outros anos/pastas, não são "não reconhecidos"
    ruido = _com(html, f"{BASE}/2026/dicionario.pdf", f"{BASE}/2025/xx-yy.csv")
    assert d.extract_page(ruido).unclassified == []


def test_ano_da_pasta_tem_de_bater_com_o_nome():
    ok = d.classify_href(f"{BASE}/2026/06-dados-abertos-precos-2026-06-glp.csv")
    assert ok is not None
    for nome in (
        "2027/12-dados-abertos-precos-2026-12-glp.csv",  # pasta de outro ano
        "2026/06-dados-abertos-precos-2026-07-glp.csv",  # mês do nome diverge
        "2026/06-dados-abertos-precos-2025-06-glp.csv",
    ):
        assert d.classify_href(f"{BASE}/{nome}") is None
    page = d.extract_page(f'<a href="{BASE}/2027/12-x-2026-12-glp.csv">x</a>')
    assert page.links == [] and page.unclassified == [
        f"{BASE}/2027/12-x-2026-12-glp.csv"
    ]
    # separador "_" também vale
    assert d.classify_href(f"{BASE}/2026/10-preco_2026_10-glp.csv") is not None


def test_extensao_que_nao_e_de_dados_e_descartada():
    for ext in ("pdf", "ods", "txt"):
        assert d.classify_href(f"{BASE}/2026/10-glp.{ext}") is None
    assert d.classify_href(f"{BASE}/2026/04-dados-abertos-precos-glp").ext == "csv"
    page = d.extract_page(f'<a href="{BASE}/2026/10-glp.pdf">x</a>')
    assert page.links == [] and page.unclassified == []


def test_duplicata_do_mes_prefere_csv_e_guarda_o_resto_como_reserva():
    hrefs = [
        f"{BASE}/2026/10-glp.pdf",
        f"{BASE}/2026/10-glp.xlsx",
        f"{BASE}/2026/10-glp.csv",
        f"{BASE}/2026/10-glp.zip",
        f"{BASE}/2026/10-glp.csv",
    ]
    page = d.extract_page("".join(f'<a href="{h}">x</a>' for h in hrefs))
    (link,) = page.links
    assert link.url == f"{BASE}/2026/10-glp.csv" and link.ext == "csv"
    assert link.fallbacks == (f"{BASE}/2026/10-glp.xlsx", f"{BASE}/2026/10-glp.zip")
    out = d.apply_links(
        _sem_outubro(list_datasets("shpc-glp-mensal")),
        page.links,
        group="shpc-glp-mensal",
    )
    entrada = out[-1]
    assert entrada["url"].endswith("10-glp.csv")
    assert entrada["fallback_urls"] == list(link.fallbacks)
    # só xlsx na página: ele vence e ext é xlsx
    (so_xlsx,) = d.extract_page(f'<a href="{BASE}/2026/10-glp.xlsx">x</a>').links
    assert (so_xlsx.ext, so_xlsx.fallbacks) == ("xlsx", ())


def test_discover_lista_nao_reconhecido_como_mudanca(html):
    page = d.extract_page(_com(html, f"{BASE}/2026/11-glp-p13.csv"))
    rel = d.discover(
        page.links, unclassified=page.unclassified, today=dt.date(2026, 11, 3)
    )
    assert rel.unclassified == [f"{BASE}/2026/11-glp-p13.csv"]
    assert rel.has_changes
    assert rel.to_dict()["unclassified"] == rel.unclassified


def test_comando_discover_mostra_nao_reconhecido_e_falha_com_fail_on_change(
    monkeypatch, html
):
    monkeypatch.setattr(d, "_today", lambda: dt.date(2026, 11, 20))
    pagina = _com(html, f"{BASE}/2026/11-glp-p13.csv")
    monkeypatch.setattr(d, "_download_page", lambda c, u: pagina)
    runner = CliRunner()
    r = runner.invoke(plugin.app, ["discover"])
    assert r.exit_code == 0
    assert f"NAO RECONHECIDO {BASE}/2026/11-glp-p13.csv" in r.output
    assert runner.invoke(plugin.app, ["discover", "--fail-on-change"]).exit_code == 1


def test_sync_avisa_dos_nao_reconhecidos(monkeypatch, html, caplog):
    monkeypatch.setattr(
        d, "_download_page", lambda c, u: _com(html, f"{BASE}/2026/1-glp.csv")
    )
    with caplog.at_level(logging.WARNING, logger="anp_fetcher.discover"):
        plugin.list_datasets_descoberto("shpc-glp-mensal")
        plugin.list_datasets_descoberto("shpc-diesel-gnv")
    avisos = [
        r.getMessage() for r in caplog.records if "não reconhece" in r.getMessage()
    ]
    assert len(avisos) == 1 and "1-glp.csv" in avisos[0]


def test_sync_avisa_de_arquivo_de_2026_que_a_pagina_nao_lista(
    monkeypatch, html, caplog
):
    sem_setembro = "\n".join(
        linha for linha in html.splitlines() if "2026/09-" not in linha
    )
    monkeypatch.setattr(d, "_download_page", lambda c, u: sem_setembro)
    monkeypatch.setattr(d, "_today", lambda: dt.date(2026, 11, 3))
    with caplog.at_level(logging.WARNING, logger="anp_fetcher.discover"):
        plugin.list_datasets_descoberto("shpc-glp-mensal")
    avisos = [r.getMessage() for r in caplog.records if "não lista" in r.getMessage()]
    assert len(avisos) == 1 and "2026-09" in avisos[0]
    assert "2026-10" not in avisos[0]  # outubro está na página


def test_mes_ainda_nao_publicado_nao_gera_aviso(html):
    links = d.extract_links(html)  # vai até outubro
    entries = list_datasets("shpc-glp-mensal")
    sem_out = [lk for lk in links if not (lk.year == 2026 and lk.month == 10)]
    # outubro ausente até o dia 15 de novembro: ainda não publicado
    assert (
        d.presumed_months(
            entries, sem_out, group="shpc-glp-mensal", today=dt.date(2026, 11, 10)
        )
        == []
    )
    # depois do dia 15 já é atraso
    assert d.presumed_months(
        entries, sem_out, group="shpc-glp-mensal", today=dt.date(2026, 11, 20)
    ) == [(2026, 10)]


def test_falha_da_pagina_nao_fica_para_sempre(monkeypatch, html, caplog):
    relogio = [1000.0]
    monkeypatch.setattr(d, "_monotonic", lambda: relogio[0])
    estado = {"falha": True, "chamadas": 0}

    def baixar(client, url):
        estado["chamadas"] += 1
        if estado["falha"]:
            raise OSError("sem rede")
        return html

    monkeypatch.setattr(d, "_download_page", baixar)
    with caplog.at_level(logging.WARNING, logger="anp_fetcher.discover"):
        for grupo in MENSAIS:  # três grupos, uma tentativa
            plugin.list_datasets_descoberto(grupo)
        assert estado["chamadas"] == 1
        relogio[0] += d.FAILURE_RETRY_SECONDS - 1
        plugin.list_datasets_descoberto("shpc-glp-mensal")
        assert estado["chamadas"] == 1
        # passado o prazo e a rede de volta, a descoberta funciona sem reiniciar
        relogio[0] += 2
        estado["falha"] = False
        entries = plugin.list_datasets_descoberto("shpc-glp-mensal")
    assert estado["chamadas"] == 2
    assert entries[-1]["url"].endswith("/2026/10-glp.csv")
    # sucesso fica em cache
    plugin.list_datasets_descoberto("shpc-diesel-gnv")
    assert estado["chamadas"] == 2


def test_list_nao_consulta_a_pagina(monkeypatch):
    def nao_deve_chamar(client, url):
        raise AssertionError("list não devia consultar a página")

    monkeypatch.setattr(d, "_download_page", nao_deve_chamar)
    r = CliRunner().invoke(plugin.app, ["list"])
    assert r.exit_code == 0, r.output
    assert "shpc-glp-mensal" in r.output


def test_discovery_disabled_so_vale_dentro_do_bloco(monkeypatch, html):
    monkeypatch.setattr(d, "_download_page", lambda c, u: html)
    entries = list_datasets("shpc-glp-mensal")
    with d.discovery_disabled():
        assert d.entries_for_group("shpc-glp-mensal", entries) == entries
    assert d.entries_for_group("shpc-glp-mensal", entries) != entries
