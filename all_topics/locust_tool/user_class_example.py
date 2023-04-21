from locust import User, task, constant


class MyScript(User):

    @task
    def launch_url(self):
        print("launching")

    @task
    def testing_something(self):
        print("hhhhh")