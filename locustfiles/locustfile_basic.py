from locust import HttpUser, task, between

class BasicUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def home(self):
        self.client.get("/")

    @task(1)
    def health(self):
        self.client.get("/health")
