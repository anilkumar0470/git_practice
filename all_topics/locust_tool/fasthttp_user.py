from locust import FastHttpUser, constant, task

class MyFastHttpUser(FastHttpUser):
    host = "https://reqres.in"

    @task
    def get_users(self):
        # res = self.client.get("/api/users?page=2")
        # print("all users")
        res = self.client.request("GET", "/api/users?page=2")
