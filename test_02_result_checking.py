from app import *


def test_names_is_dict():
    html = get_wiki_html(WIKI_URL)
    animals = get_animal_names(html)
    assert animals["Zebra"] == ["zebrine", "hippotigrine"]
