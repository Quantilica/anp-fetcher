"""Aviso de grupo inteiro em HTTP 404 (alerts + plugin)."""

import json
from types import SimpleNamespace

import pytest
from quantilica.core.http import HttpStatusError
from typer.testing import CliRunner

from anp_fetcher import alerts, plugin


def _item(group, action, reason):
    return SimpleNamespace(dataset=group, action=action, reason=reason)


def test_dead_groups_from_plan_so_grupo_inteiro_em_404():
    items = [
        _item("pmqc", "skip-unavailable", "remote-404"),
        _item("pmqc", "skip-unavailable", "remote-404"),
        _item("tancagem", "skip-unavailable", "remote-404"),
        _item("tancagem", "download", "new"),
        _item("ie", "skip-up-to-date", "fresh"),
    ]
    assert alerts.dead_groups_from_plan(items) == ["pmqc"]


def test_dead_groups_from_errors():
    entries = [
        {"id": "a1", "group": "g1"},
        {"id": "a2", "group": "g1"},
        {"id": "b1", "group": "g2"},
        {"id": "b2", "group": "g2"},
    ]
    errors = [
        ("a1", "HTTP 404 while fetching x"),
        ("a2", "HTTP 404 while fetching y"),
        ("b1", "HTTP 404 while fetching z"),
        ("b2", "HTTP 500 while fetching w"),
    ]
    assert alerts.dead_groups_from_errors(entries, errors) == ["g1"]


def test_exit_code_env(monkeypatch):
    monkeypatch.delenv("ANP_DEAD_GROUP_EXIT", raising=False)
    assert alerts.exit_code() == 3
    monkeypatch.setenv("ANP_DEAD_GROUP_EXIT", "0")
    assert alerts.exit_code() == 0
    monkeypatch.setenv("ANP_DEAD_GROUP_EXIT", "lixo")
    assert alerts.exit_code() == 3


def _plan(tmp_path, items):
    payload = {
        "fetcher": "anp-fetcher",
        "output_dir": str(tmp_path),
        "generated_at": "2026-11-05T00:00:00+00:00",
        "items": [
            {
                "dataset": g,
                "id": i,
                "url": "https://example.test/" + i,
                "action": a,
                "reason": r,
                "entry": {"id": i, "group": g, "url": "https://example.test/" + i},
            }
            for g, i, a, r in items
        ],
    }
    path = tmp_path / "plano.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_sync_from_plan_sai_com_codigo_quando_grupo_morto(tmp_path, monkeypatch):
    monkeypatch.delenv("ANP_DEAD_GROUP_EXIT", raising=False)
    path = _plan(
        tmp_path,
        [
            ("pmqc", "pmqc-csv-2026-01", "skip-unavailable", "remote-404"),
            ("pmqc", "pmqc-csv-2026-02", "skip-unavailable", "remote-404"),
            ("ie", "ie-1", "skip-up-to-date", "fresh"),
        ],
    )
    result = CliRunner().invoke(
        plugin.app, ["sync", "--from-plan", str(path), "-o", str(tmp_path)]
    )
    assert result.exit_code == 3
    assert "pmqc" in result.output


def test_sync_from_plan_sem_grupo_morto_sai_com_zero(tmp_path, monkeypatch):
    monkeypatch.delenv("ANP_DEAD_GROUP_EXIT", raising=False)
    path = _plan(
        tmp_path,
        [
            ("pmqc", "pmqc-csv-2026-01", "skip-unavailable", "remote-404"),
            ("pmqc", "pmqc-csv-2026-02", "skip-up-to-date", "fresh"),
        ],
    )
    result = CliRunner().invoke(
        plugin.app, ["sync", "--from-plan", str(path), "-o", str(tmp_path)]
    )
    assert result.exit_code == 0


def test_sync_grupo_morto_pode_ficar_so_no_aviso(tmp_path, monkeypatch):
    monkeypatch.setenv("ANP_DEAD_GROUP_EXIT", "0")
    path = _plan(
        tmp_path, [("pmqc", "pmqc-csv-2026-01", "skip-unavailable", "remote-404")]
    )
    result = CliRunner().invoke(
        plugin.app, ["sync", "--from-plan", str(path), "-o", str(tmp_path)]
    )
    assert result.exit_code == 0


def test_sync_completo_detecta_grupo_inteiro_em_404(tmp_path, monkeypatch):
    monkeypatch.delenv("ANP_DEAD_GROUP_EXIT", raising=False)

    def fake_download(self, entry, output_dir, **kwargs):
        raise HttpStatusError(entry["url"], 404)

    monkeypatch.setattr(plugin.AnpFetcherApp, "download_entry", fake_download)
    result = CliRunner().invoke(plugin.app, ["sync", "reservas", "-o", str(tmp_path)])
    assert result.exit_code == 3
    assert "reservas-nacionais" in result.output


def test_check_nao_muda_o_codigo_de_saida(tmp_path, monkeypatch):
    """No modo de plano, check != 0 faria o cron cair num sync completo."""
    from quantilica.cli.sdk import CheckPlan, CheckPlanItem

    plan = CheckPlan(
        fetcher="anp-fetcher",
        output_dir=str(tmp_path),
        generated_at="x",
        items=[
            CheckPlanItem(
                dataset="pmqc",
                id="pmqc-csv-2026-01",
                url="u",
                partition=None,
                local_path="p",
                remote_etag=None,
                remote_last_modified=None,
                remote_size=None,
                local_exists=False,
                action="skip-unavailable",
                reason="remote-404",
                entry={"id": "pmqc-csv-2026-01", "group": "pmqc", "url": "u"},
            )
        ],
    )
    monkeypatch.setattr(plugin.FetcherApp, "check_datasets", lambda self, *a, **k: plan)
    out = tmp_path / "plano.json"
    result = CliRunner().invoke(
        plugin.app, ["check", "pmqc", "-o", str(tmp_path), "--out", str(out)]
    )
    assert result.exit_code == 0
    assert out.exists()


@pytest.mark.parametrize("group", ["pmqc"])
def test_check_registra_aviso(group, caplog):
    caplog.set_level("WARNING")
    alerts.report([group])
    assert any(group in r.getMessage() for r in caplog.records)
