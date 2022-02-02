from app import *


def test_html_is_str():
    assert get_wiki_html(WIKI_URL) is not None


def test_names_is_dict():
    html = get_wiki_html(WIKI_URL)
    animals = get_animal_names(html)
    assert len(animals) != 0
