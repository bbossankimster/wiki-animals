import sys,os
sys.path.append(os.getcwd())
from app import *



def test_image_not_found():
    for file in os.listdir(os.path.join(BASE_DIR, "tmp")):
        print(file)
        os.remove(os.path.join(BASE_DIR, "tmp", file))
    loader = classes.ImageLoader(123, "https://en.wikipedia.org/wiki/Suidae")
    loader.run()
    assert loader.task_id == 123
    assert loader.result != {}
    assert loader.result == {'status': 'Image not found', 'path': 'none'}
    

def test_image_dowload_ok():
    for file in os.listdir(os.path.join(BASE_DIR, "tmp")):
        print(file)
        os.remove(os.path.join(BASE_DIR, "tmp", file))
    loader = classes.ImageLoader(123, "https://en.wikipedia.org/wiki/Bird")
    loader.run()
    assert loader.task_id == 123
    assert loader.result != {}
    assert loader.result == {'status': 'https://en.wikipedia.org/wiki/File:Bird_Diversity_2013.png', 'path': os.path.join(BASE_DIR, "tmp", "Bird_Diversity_2013.png")}
