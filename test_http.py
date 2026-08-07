import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}
r1 = httpx.get("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan/2026/04-dados-abertos-precos-diesel-gnv.csv", headers=headers, follow_redirects=True)
print("CSV:", r1.status_code)
r2 = httpx.get("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan/2026/04-dados-abertos-precos-diesel-gnv.xlsx", headers=headers, follow_redirects=True)
print("XLSX:", r2.status_code)
