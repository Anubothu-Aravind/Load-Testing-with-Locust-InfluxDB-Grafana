from locust import HttpUser, task, constant_pacing

class RPSUser(HttpUser):
    wait_time = constant_pacing(0.5)

    @task
    def home(self):
        self.client.get("/")
