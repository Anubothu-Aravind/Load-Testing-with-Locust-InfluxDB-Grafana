from locust import HttpUser, task, between

class DBUser(HttpUser):
    wait_time = between(0.2, 1)

    @task(6)
    def query_list(self):
        self.client.get("/api/reports?limit=50")

    @task(2)
    def generate_report(self):
        payload = {"range":"last_30_days","filters":{}}
        self.client.post("/api/reports/generate", json=payload)
