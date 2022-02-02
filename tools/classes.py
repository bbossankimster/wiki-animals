from threading import Thread
from tools.web_parsing import get_pic_urls
import os
import wget


class ImageLoader(Thread):
    def __init__(self, task_id, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.task_id = task_id
        self.result = {}

    def run(self):  
        print(self.url)
        img_url, img_os_path = get_pic_urls(self.url)
        print("img_url, img_os_path", img_url, img_os_path)
        if img_url:
            if not os.path.exists(img_os_path):
                try:
                    wget.download(img_url, img_os_path)
                    self.result = {"status": img_url, "path": img_os_path}
                except Exception as e:
                    self.result = {"status": e, "path": "none"}
            else:
                self.result = {"status": "file_exists", "path": img_os_path}
        else:
            self.result = {"status": "Image not found", "path": "none"}
