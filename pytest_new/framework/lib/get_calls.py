
import requests
class GetClient:

    def get_all_records(self, **params):
        # if params:
        #     response = requests.get("https://reqres.in/api/users")
        # print(response.json())
        # response = requests.get("https://reqres.in/api/users?page=2")
        # print(response.json())
        # return response
        response = requests.get("https://httpbin.org/get?page=2&count=25")
        print(response.json())

g = GetClient()
g.get_all_records()