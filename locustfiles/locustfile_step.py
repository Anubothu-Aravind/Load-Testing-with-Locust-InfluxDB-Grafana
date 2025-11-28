from locust import HttpUser, task, between, LoadTestShape

class OpptymUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def home(self):
        self.client.get("/")

class StepLoadShape(LoadTestShape):
    step_time = 30
    step_users = 25
    max_steps = 12

    def tick(self):
        run_time = self.get_run_time()
        step = int(run_time / self.step_time)
        if step >= self.max_steps:
            return None
        user_count = (step + 1) * self.step_users
        spawn_rate = self.step_users
        return (user_count, spawn_rate)
