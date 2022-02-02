from app import *


def test_get_names():
    html = get_wiki_html(WIKI_URL)
    animals, http_paths  = get_animal_names(html)
    assert animals["Zebra"] == ["zebrine", "hippotigrine"]
    assert len(http_paths) == len(animals)
