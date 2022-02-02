from app import *


def test_object_loader():
    loader = classes.ImageLoader(123, "https://en.wikipedia.org/wiki/Suidae")
    loader.run()
    assert loader.task_id == 123
    assert loader.result != {}
    assert loader.result == {'status': 'Image not found', 'path': 'none'}
    

