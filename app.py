import requests
from bs4 import BeautifulSoup

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_animal_names"


def get_wiki_html(url=WIKI_URL):
    client = requests.Session()
    response = client.get(WIKI_URL)
    response.encoding = 'utf-8'
    html = response.text
    return html


def get_animal_names(html):
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table")
    print(len(tables))
    cntr = 0
    animals = {}
    for table in tables[1:]:
        for raw in table.find_all("tr"):
            cntr += 1
            cells = raw.find_all("td")
            if len(cells) != 0:
                animal_name, collateral_adjective = cells[0].text, cells[5].text
                animals[animal_name] = collateral_adjective.split(" ")
    return animals


def print_names(animals):
    for animal in sorted([*animals]):
        print("{}  >>> {}".format(animal, ", ".join(animals[animal])))


if __name__ == "__main__":
    html = get_wiki_html(WIKI_URL)
    animals = get_animal_names(html)
    print_names(animals)