from locust import HttpUser, task, between
import random

class ApiUser(HttpUser):
    wait_time = between(0.5, 2)

    def on_start(self):
        # Use a dedicated test account for staging
        r = self.client.post("/api/auth/login", json={"user":"test","pass":"test"})
        if r.status_code == 200:
            self.token = r.json().get("access_token")
        else:
            self.token = None

    @task(5)
    def list_items(self):
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        self.client.get("/api/items", headers=headers)

    @task(2)
    def read_item(self):
        item_id = random.randint(1, 100)
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        self.client.get(f"/api/items/{item_id}", headers=headers)

    @task(1)
    def create_item(self):
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        payload = {"title":"load test","body":"non-sensitive"}
        self.client.post("/api/items", json=payload, headers=headers)
