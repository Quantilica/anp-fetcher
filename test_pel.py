import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}
base = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ppgn-el"
for name in ["reinjecao-gn-1000m3.csv", "reinjecao-gn1000m3.csv", "reinjecao-gas-natural-1000m3.csv", "reinjecao-gas-natural-m3.csv", "reinjecao-gas-natural.csv", "reinjecao-gn.csv"]:
    url = f"{base}/{name}"
    with httpx.stream("GET", url, headers=headers, follow_redirects=True) as r:
        print(url, r.status_code)
