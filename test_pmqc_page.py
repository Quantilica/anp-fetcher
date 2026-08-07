import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
}
url = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pmqc"
r = httpx.get(url, headers=headers, follow_redirects=True)
import re

links = re.findall(r'href="([^"]+pmqc[^"]+)"', r.text)
for link in set(links):
    if "2024" in link:
        print(link)
