"""``multas-2021``: o servidor entrega o ``.xlsx`` como CSV em texto."""

import http.server
import threading
from collections.abc import Iterator
from pathlib import Path

import pytest

from anp_fetcher.catalog import list_datasets
from anp_fetcher.plugin import fetcher

# BOM + título + cabeçalho, como o arquivo real (cp850 não importa para a assinatura).
_CSV = (
    b"\xef\xbb\xbfANP - Ag\xc3\xaancia Nacional do Petr\xc3\xb3leo;;;\r\n"
    b"Multas aplicadas;;;\r\n"
    b"Auto de Infra\xc3\xa7\xc3\xa3o;Status Processo;Valor;UF\r\n"
    b"1;Processo Pago;100,00;RJ\r\n"
)


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        self.send_response(200)
        self.send_header("Content-Type", "application/vnd.ms-excel")
        self.send_header("Content-Length", str(len(_CSV)))
        self.end_headers()
        self.wfile.write(_CSV)

    do_HEAD = do_GET  # noqa: N815

    def log_message(self, *args: object) -> None:
        pass


@pytest.fixture
def url_csv_como_xlsx() -> Iterator[str]:
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/multas-2021-junho22.xlsx"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def _entry_multas_2021() -> dict:
    return dict(next(e for e in list_datasets("multas") if e["id"] == "multas-2021"))


def test_catalogo_grava_o_csv_como_csv():
    entry = _entry_multas_2021()
    assert entry["url"].endswith("multas-2021-junho22.xlsx")
    assert entry["ext"] == "csv"


def test_download_aceita_csv_servido_com_url_xlsx(
    tmp_path: Path, url_csv_como_xlsx: str
):
    entry = _entry_multas_2021()
    entry["url"] = url_csv_como_xlsx
    saved = fetcher.download_entry(entry, tmp_path)
    assert saved.suffix == ".csv"
    assert saved.read_bytes() == _CSV


def test_download_com_nome_xlsx_recusa_o_csv(tmp_path: Path, url_csv_como_xlsx: str):
    """Regressão: com ext xlsx o ZIP inválido derrubava a coleta todo dia."""
    entry = _entry_multas_2021()
    entry["url"] = url_csv_como_xlsx
    entry["ext"] = "xlsx"
    with pytest.raises(Exception, match="(?i)zip"):
        fetcher.download_entry(entry, tmp_path)


def test_leitor_le_o_download_como_csv(tmp_path: Path, url_csv_como_xlsx: str):
    from anp_fetcher.reader import read_file

    entry = _entry_multas_2021()
    entry["url"] = url_csv_como_xlsx
    saved = fetcher.download_entry(entry, tmp_path)
    df = read_file(saved, {})
    assert df.height >= 1
