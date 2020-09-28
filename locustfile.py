import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/api")
        self.client.get("/")
        self.client.get("/short/?url=google.com")

    @task(3)
    def view_item(self):
        urls = ['google.com', 'yandex.ru', 'https://vk.com',
                't.me', 'youtube.com', 'meduza.io', 'avito.ru', 'hh.ru', 'nplus1.ru', 'oioioi']
        for url in urls:
            print(self.client.get(f"/api/?url={url}", name="url"))
            time.sleep(1)
