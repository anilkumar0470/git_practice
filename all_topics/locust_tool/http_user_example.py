from locust import HttpUser, task, constant

class MyReqRes(HttpUser):
    host = "https://reqres.in"


    @task
    def get_users(self):
        res = self.client.get(url="/api/users?page=2")
        if res.status_code == 200 :
            print("api call is successful")
        else:
            print("api call is failed")