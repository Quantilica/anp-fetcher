import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}

for ext in ["csv", "xlsx"]:
    url = f"https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan/2026/04-dados-abertos-precos-diesel-gnv.{ext}"
    with httpx.stream("GET", url, headers=headers, follow_redirects=True) as r:
        print(url, r.status_code)

for ext in ["csv", "xlsx"]:
    url = f"https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsan/2026/04-dados-abertos-precos-gasolina-etanol.{ext}"
    with httpx.stream("GET", url, headers=headers, follow_redirects=True) as r:
        print(url, r.status_code)
