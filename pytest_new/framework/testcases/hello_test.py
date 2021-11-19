import requests
#
#
# data ={
#     "name": "morpheus1",
#     "job": "leader",
# }
# res1 = requests.get(url="https://reqres.in/api/users?page=2")
# print(res1.json())
#
# response = requests.post(url="https://reqres.in/api/users", data=data )
# print(response)
#
# res1 = requests.get(url="https://reqres.in/api/users?page=2")
# print(res1.json())

import pytest
# pytest.set_trace()
from framework.lib.get_calls import GetClient

get_client_obj = GetClient()


def test_get_all_available_resources():
    res = get_client_obj.get_all_records()

    if res:
        print("status code is {}".format(res.status_code))
        print("content is {}".format(res.json()))
    else:
        print("status code is {}".format(res.status_code))


def test_get_one_resource():
    res = get_client_obj.get_all_records()



