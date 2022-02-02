import requests
from bs4 import BeautifulSoup
from settings import WIKI_BASE, BASE_DIR
import os


def get_wiki_html(url):
    client = requests.Session()
    response = client.get(url)
    response.encoding = 'utf-8'
    html = response.text
    return html


def get_animal_names(html):
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")
    print(len(tables))
    cntr = 0
    animals = {}
    http_paths = []
    for table in tables[1:]:
        for raw in table.find_all("tr"):
            cntr += 1
            cells = raw.find_all("td")
            if len(cells) != 0:
                animal_name, url, collateral_adjective = cells[0].text, cells[0].next_element.get("href"), cells[5].text
                animals[animal_name] = collateral_adjective.split(" ")
                http_paths.append("{}{}".format(WIKI_BASE, url))
    return animals, http_paths


def get_pic_urls(url):
    html = get_wiki_html(url)
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all("a")
    for data in tags:
        if data.get("title"):
            if "About this image" in data.get("title"):
                img_url = "{}{}".format(WIKI_BASE, data.get("href"))
                return img_url, os.path.join(BASE_DIR, "tmp", img_url.rsplit(":", 1)[1])
    return None, None