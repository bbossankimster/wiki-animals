import tools.classes as classes
from settings import BASE_DIR, WIKI_URL
from tools.web_parsing import get_animal_names, get_wiki_html, get_pic_urls
import os



def print_names(animals):
    for animal in sorted([*animals]):
        print("{}  >>> {}".format(animal, ", ".join(animals[animal])))


def run_threads(download_pool, job_result):
    for loader in download_pool:
        loader.start()
    for loader in download_pool:
        loader.join()
        job_result[loader.task_id] = loader.result


def download_images(urls):
    cntr = 0
    download_pool = []
    job_result = {}
    for url in urls:
        cntr += 1
        download_pool.append(classes.ImageLoader(cntr, url))
    run_threads(download_pool, job_result)
    return job_result


if __name__ == "__main__":
    html = get_wiki_html(WIKI_URL)
    animals, http_paths = get_animal_names(html)
    print_names(animals)
    job_result = download_images(http_paths[0:22])
    for job in sorted([*job_result]):
        print(job_result[job])