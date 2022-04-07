import json
from common_lib import get_call, post_call

class Test_methods:

    def variables(self):
        self.url = "https://reqres.in"
        self.get_endpoint = "api/users?page=2"
        self.post_data = {
            "name": "morpheus",
            "job": "leader"
        }
        self.post_endpoint = "api/users"
     # https://reqres.in/api/users?page=2

    def test_get_data(self):
        self.variables()

        result = get_call("{}/{}".format(self.url,self.get_endpoint))

        if result:
            print(result)
            assert result["total"] ==12
        else:
            print(result)

    def test_post_data(self):
        self.variables()
        result = post_call("{}/{}".format(self.url, self.post_endpoint), data=self.post_data)

        if result:
            print(result)
            assert result["name"] =="morpheus"
        else:
            print(result)


