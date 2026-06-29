import datetime as dt
import re
import unicodedata
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup
from tqdm import tqdm


SHLP_BASE_URL = (
    "https://www.gov.br"
    "/anp"
    "/pt-br"
    "/assuntos"
    "/precos-e-defesa-da-concorrencia"
    "/precos"
    "/precos-revenda-e-de-distribuicao-combustiveis"
    "/shlp"
)

shlp = [
    {
        "url": SHLP_BASE_URL + "/2001-2012/semanal-brasil-2004-a-2012.xlsx",
        "name": "semanal-brasil-2004-a-2012.xlsx",
        "frequency": "weekly",
        "territorial_level": "brasil",
    },
    {
        "url": SHLP_BASE_URL + "/2001-2012/semanal-regioes-2004-a-2012.xlsx",
        "name": "semanal-regioes-2004-a-2012.xlsx",
        "frequency": "weekly",
        "territorial_level": "grande-regiao",
    },
    {
        "url": SHLP_BASE_URL + "/2001-2012/semanal-estados-2004-a-2012.xlsx",
        "name": "semanal-estados-2004-a-2012.xlsx",
        "frequency": "weekly",
        "territorial_level": "uf",
    },
    {
        "url": SHLP_BASE_URL + "/2001-2012/semanal-municipios-2004-a-2012.xlsb",
        "name": "semanal-municipios-2004-a-2012.xlsb",
        "frequency": "weekly",
        "territorial_level": "brasil",
    },
    {
        "url": SHLP_BASE_URL + "/semanal/semanal-brasil-desde-2013-2.xlsx",
        "name": "semanal-brasil-desde-2013-2.xlsx",
        "frequency": "weekly",
        "territorial_level": "brasil",
    },
    {
        "url": SHLP_BASE_URL + "/semanal/semanal-regioes-desde-2013.xlsx",
        "name": "semanal-regioes-desde-2013.xlsx",
        "frequency": "weekly",
        "territorial_level": "grande-regiao",
    },
    {
        "url": SHLP_BASE_URL + "/semanal/semanal-estados-desde-2013-2.xlsx",
        "name": "semanal-estados-desde-2013-2.xlsx",
        "territorial_level": "uf",
    },
    {
        "url": SHLP_BASE_URL + "/semanal/semanal-municipios-2013-a-2017.xlsb",
        "name": "semanal-municipios-2013-a-2017.xlsb",
        "frequency": "weekly",
        "territorial_level": "municipio",
    },
    {
        "url": SHLP_BASE_URL + "/semanal/semanal-municipios-2018-a-2021.xlsb",
        "name": "semanal-municipios-2018-a-2021.xlsb",
        "frequency": "weekly",
        "territorial_level": "municipio",
    },
    {
        "url": SHLP_BASE_URL + "/semanal/semanal-municipios-2022.xlsx",
        "name": "semanal-municipios-2022.xlsx",
        "frequency": "weekly",
        "territorial_level": "municipio",
    },
    {
        "url": SHLP_BASE_URL + "/2001-2012/mensal-brasil-2001-a-2012.xlsx",
        "name": "mensal-brasil-2001-a-2012.xlsx",
        "frequency": "monthly",
        "territorial_level": "brasil",
    },
    {
        "url": SHLP_BASE_URL + "/2001-2012/mensal-regioes-2001-a-2012.xlsx",
        "name": "mensal-regioes-2001-a-2012.xlsx",
        "frequency": "monthly",
        "territorial_level": "grande-regiao",
    },
    {
        "url": SHLP_BASE_URL + "/2001-2012/mensal-estados-2001-a-2012.xlsx",
        "name": "mensal-estados-2001-a-2012.xlsx",
        "frequency": "monthly",
        "territorial_level": "uf",
    },
    {
        "url": SHLP_BASE_URL + "/2001-2012/mensal-municipios-2001-a-2012.xlsb",
        "name": "mensal-municipios-2001-a-2012.xlsb",
        "frequency": "monthly",
        "territorial_level": "municipio",
    },
    {
        "url": SHLP_BASE_URL + "/mensal/mensal-brasil-desde-jan2013.xlsx",
        "name": "mensal-brasil-desde-jan2013.xlsx",
        "frequency": "monthly",
        "territorial_level": "brasil",
    },
    {
        "url": SHLP_BASE_URL + "/mensal/mensal-regioes-desde-jan2013.xlsx",
        "name": "mensal-regioes-desde-jan2013.xlsx",
        "frequency": "monthly",
        "territorial_level": "grande-regiao",
    },
    {
        "url": SHLP_BASE_URL + "/mensal/mensal-estados-desde-jan2013.xlsx",
        "name": "mensal-estados-desde-jan2013.xlsx",
        "frequency": "monthly",
        "territorial_level": "uf",
    },
    {
        "url": SHLP_BASE_URL + "/mensal/mensal-municipios-2013-a-2015.xlsx",
        "name": "mensal-municipios-2013-a-2015.xlsx",
        "frequency": "monthly",
        "territorial_level": "municipio",
    },
    {
        "url": SHLP_BASE_URL + "/mensal/mensal-municipios-2016-a-2018.xlsx",
        "name": "mensal-municipios-2016-a-2018.xlsx",
        "frequency": "monthly",
        "territorial_level": "municipio",
    },
    {
        "url": SHLP_BASE_URL + "/mensal/mensal-municipios-2019-a-2021.xlsx",
        "name": "mensal-municipios-2019-a-2021.xlsx",
        "frequency": "monthly",
        "territorial_level": "municipio",
    },
    {
        "url": SHLP_BASE_URL + "/mensal/mensal-municipios-desde-jan2022.xlsx",
        "name": "mensal-municipios-desde-jan2022.xlsx",
        "frequency": "monthly",
        "territorial_level": "municipio",
    },
]

dados_abertos_url_base = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos"
months = {
    "janeiro": 1,
    "fevereiro": 2,
    "marco": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12,
}


def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )


def clean_resource_name(resource_name: str) -> str:
    return (
        strip_accents(resource_name)
        .strip()
        .lower()
    )


def decode_monthyear(monthyear: str) -> dt.date:
    month, year = clean_resource_name(monthyear).split("/")
    return dt.date(int(year), months[month], 1)


def decode_semesteryear(semesteryear: str) -> dt.date:
    semesteryear = clean_resource_name(semesteryear).replace(".", "")
    m = re.match(r"([12])o sem (\d{4})", semesteryear)
    semester, year = m.groups()
    if semester == "1":
        return dt.date(int(year), 1, 1)
    elif semester == "2":
        return dt.date(int(year), 6, 1)
    else:
        raise ValueError(f"Invalid {semesteryear}")
def get_shpc_filepath(data_dir: Path, dataset_info: dict) -> Path:
    dataset = dataset_info["dataset"]
    if subset := dataset_info["subset"]:
        dataset += "-" + subset
    if dataset_info["grouping"] == "weekly":
        date_partition = f"@{dt.datetime.utcnow():%Y%mW%U}"
    else:
        year, subyear = dataset_info["date"]
        date_partition = f"{year:04}{subyear:02}"
    extension = dataset_info["file_extension"]
    dest_filename = f"{dataset}_{date_partition}.{extension}"
    dest_filepath = data_dir / "shpc" / dataset / dest_filename
    return dest_filepath


def get_shlp_filepath(dest_data_dir: Path, info: dict) -> Path:
    frequency = info["frequency"]
    region = info["region"]
    period = info["period"]
    extension = info["extension"]
    dest_filename = f"{region}-{frequency}-{period}.{extension}"
    dest_filepath = dest_data_dir / "shlp" / f"{region}-{frequency}" / dest_filename
    return dest_filepath


def write_data(data: bytes, filepath: Path):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with filepath.open("wb") as f:
        f.write(data)

def parse_date_semester(txt: str) -> tuple[int]:
    m = re.match(r"(1|2)º semestre de (\d{4})", txt)
    semester, year = m.groups()
    return int(year), int(semester)


def parse_date_monthly(txt: str) -> tuple[int]:
    months = {
        "janeiro": 1,
        "fevereiro": 2,
        "março": 3,
        "abril": 4,
        "maio": 5,
        "junho": 6,
        "julho": 7,
        "agosto": 8,
        "setembro": 9,
        "outubro": 10,
        "novembro": 11,
        "dezembro": 12,
    }
    pattern = f"({'|'.join(months.keys())})" + r" de (\d{4})"
    m = re.match(pattern, txt.lower())
    month, year = m.groups()
    return int(year), months[month]


def parse_url(url: str) -> dict:
    filename = url.rsplit("/", maxsplit=1)[1]
    stem, extension = filename.split(".")
    return {
        "filename": filename,
        "file_stem": stem,
        "file_extension": extension,
    }


def gather_shpc_resources_metadata() -> dict[str, str | list[dict[str, Any]]]:
    """Gathers metadata links of SHPC datasets. Returns a list of dictionaries
    with informations of each data file link.

    Example dataset:

    {
        'dataset': 'glp-p13',
        'date': (None, None),
        'extension': 'csv',
        'filename': 'ultimas-4-semanas-glp.csv',
        'grouping': 'weekly',
        'link_text': 'GLP P13',
        'stem': 'ultimas-4-semanas-glp',
        'subset': None,
        'url': 'https://www.gov.br/anp/pt-br/.../ultimas-4-semanas-glp.csv',
    }
    """
    url = (
        "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos"
        "/serie-historica-de-precos-de-combustiveis"
    )
    r = httpx.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    content_core = soup.select_one("#content-core")
    link_lists = content_core.select("ul")
    doc_link = link_lists[0].select_one("a")
    doc = {
        "link_text": doc_link.text.strip(),
        "url": doc_link["href"],
        **parse_url(doc_link["href"]),
    }

    # Dados semanais agrupados por semestre
    combustiveis_automotivos_list = link_lists[1].select("a")
    combustiveis_automotivos = [
        {
            "dataset": "combustiveis-automotivos",
            "subset": None,
            "grouping": "semester",
            "dynamic": False,
            "url": a["href"],
            "link_text": a.text.strip(),
            "date": parse_date_semester(a.text.strip()),
            **parse_url(a["href"]),
        }
        for a in combustiveis_automotivos_list
    ]

    glp_p13_list = link_lists[2].select("a")
    glp_p13 = [
        {
            "dataset": "glp-p13",
            "subset": None,
            "grouping": "semester",
            "dynamic": False,
            "url": a["href"],
            "link_text": a.text.strip(),
            "date": parse_date_semester(a.text.strip()),
            **parse_url(a["href"]),
        }
        for a in glp_p13_list
    ]

    # Dados semanais agrupados mensalmente
    diesel_gnv_list = link_lists[3].select("a")
    diesel_gnv = [
        {
            "dataset": "combustiveis-automotivos",
            "subset": "diesel-gnv",
            "grouping": "monthly",
            "dynamic": False,
            "url": a["href"],
            "link_text": a.text.strip(),
            "date": parse_date_monthly(a.text.strip()),
            **parse_url(a["href"]),
        }
        for a in diesel_gnv_list
    ]

    gasolina_etanol_list = link_lists[4].select("a")
    gasolina_etanol = [
        {
            "dataset": "combustiveis-automotivos",
            "subset": "gasolina-etanol",
            "grouping": "monthly",
            "dynamic": False,
            "url": a["href"],
            "link_text": a.text.strip(),
            "date": parse_date_monthly(a.text.strip()),
            **parse_url(a["href"]),
        }
        for a in gasolina_etanol_list
    ]

    glp_list = link_lists[5].select("a")
    glp = [
        {
            "dataset": "glp-p13",
            "subset": None,
            "grouping": "monthly",
            "dynamic": False,
            "url": a["href"],
            "link_text": a.text.strip(),
            "date": parse_date_monthly(a.text.strip()),
            **parse_url(a["href"]),
        }
        for a in glp_list
    ]

    names = {
        "Óleo Diesel (S-500 e S-10) + GNV": (
            "combustiveis-automotivos",
            "diesel-gnv",
        ),
        "Etanol Hidratado + Gasolina C": (
            "combustiveis-automotivos",
            "gasolina-etanol",
        ),
        "GLP P13": ("glp-p13", None),
    }
    ultimas_4_semanas_list = link_lists[6].select("a")
    ultimas_4_semanas = [
        {
            "dataset": names[a.text.strip()][0],
            "subset": names[a.text.strip()][1],
            "grouping": "weekly",
            "dynamic": True,
            "url": a["href"],
            "link_text": a.text.strip(),
            "date": (None, None),
            **parse_url(a["href"]),
        }
        for a in ultimas_4_semanas_list
    ]
    return {
        "doc": doc,
        "datasets": (
            combustiveis_automotivos
            + glp_p13
            + diesel_gnv
            + gasolina_etanol
            + glp
            + ultimas_4_semanas
        ),
    }


def gather_dados_estatisticos_metadata() -> list[dict[str, Any]]:
    html_page_url = (
        "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos"
    )
    r = httpx.get(html_page_url)
    soup = BeautifulSoup(r.text, "html.parser")

    def is_file(href: str) -> bool:
        m = re.match(r".*\.(pdf|xls|xlsx|zip)$", href)
        return bool(m)

    links = [
        {
            "href": a["href"],
            "text": a.text.strip(),
            "filename": a["href"].rsplit("/", 1)[1],
        }
        for a in soup.select("a") if is_file(a["href"])
    ]

    return links


def gather_shlp_metadata():
    """Gathers metadata links of SHLP datasets. Returns a list of dictionaries"""
    BASE_URL = (
        "https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia"
        "/precos/precos-revenda-e-de-distribuicao-combustiveis/shlp"
    )
    BASE_URL + "/semanal"
    BASE_URL + "/mensal"
    BASE_URL + "/2001-2012"


def fetch_file(url: str, dest_filepath: Path) -> bytes:
    print(url, "->", dest_filepath)
    args = {
        "method": "GET",
        "url": url,
        "timeout": 30,
        "follow_redirects": True,
    }
    dest_filepath.parent.mkdir(parents=True, exist_ok=True)
    while True:
        try:
            with httpx.stream(**args) as r:
                if "Content-Length" not in r.headers:
                    raise Exception("No Content-Length")
                total = int(r.headers["Content-Length"])
                progress = tqdm(
                    total=total,
                    unit="B",
                    unit_scale=True,
                    desc=dest_filepath.name,
                )
                with dest_filepath.open("wb") as f:
                    for chunk in r.iter_bytes():
                        f.write(chunk)
                        progress.update(len(chunk))
                progress.close()
                break
        except httpx.ProtocolError as e:
            print("\nProtocol error", e)
        except (httpx.ConnectTimeout, httpx.ConnectError) as e:
            print("\nConnection timeout", e)
            dest_filepath.unlink(missing_ok=True)
            break


def fetch_shlp(resource: dict[str, Any], dest_dir: Path):
    url = resource["url"]
    dest_filepath = dest_dir / "shlp" / resource["name"]
    if dest_filepath.exists():
        return {"filepath": dest_filepath}
    fetch_file(url, dest_filepath)
    return {
        "filepath": dest_filepath,
    }


def fetch_shpc(resource: dict[str, Any], data_dir: Path) -> dict:
    url = resource["url"]
    dest_filepath = get_shpc_filepath(data_dir, resource)
    if dest_filepath.exists():
        return resource | {"dest_filepath": dest_filepath}
    fetch_file(url, dest_filepath)
    return resource | {"dest_filepath": dest_filepath}


def fetch_shpc_doc(data_dir: Path):
    shpc_resources = gather_shpc_resources_metadata()
    url = shpc_resources["doc"]["url"]
    filename = shpc_resources["doc"]["filename"]
    dest_filepath = data_dir / "shpc" / "[doc]" / filename
    fetch_file(url, dest_filepath)


def dados_estatisticos(dest_dir: Path):
    links = gather_dados_estatisticos_metadata()
    for link in links:
        url = link["href"]
        dest_filepath = dest_dir / "dados-estatisticos" / link["filename"]
        if dest_filepath.exists():
            continue
        print(link)
        fetch_file(url, dest_filepath)
