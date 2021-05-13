# import requests
#
# BASE_URL = "http://localhost:8000/"
# END_POINT = "api"
# id = "10"
# # response = requests.get("{}{}/{}".format(BASE_URL, END_POINT, id))
# # print(response)
# # print(response.json())
#
# import json
#
#



# create_source()
#
#
# def update_source(id):
#
#     new_emp_data = {
#
#         "esal":20
#     }
#     import pdb
#     # pdb.set_trace()
#     response = requests.put("{}{}/{}/".format(BASE_URL, END_POINT, id), data=json.dumps(new_emp_data))
#     # print(response.json())
#     print(response.status_code)
#     print(response.json())
#
#
# # update_source(11)
#
# def delete_resource(id):
#
#     response = requests.delete("{}{}/{}/".format(BASE_URL, END_POINT, id))
#     # print(response.json())
#     print(response.status_code)
#     print(response.json())
#
#
# delete_resource(9)


import requests
BASE_URL = "http://localhost:8000/"
END_POINT = "api/"
import json


def get_resource(id=None):

    data = {}
    if id:
        data = {
            "id": id
        }
    # import pdb
    # pdb.set_trace()
    updated_data = data
    response = requests.get("{}{}".format(BASE_URL, END_POINT), data=json.dumps(updated_data))
    print(response)
    print(response.json())
# get_resource()

def create_source():

    new_emp_data = {

        "eno": 13,
        "ename": "user13",
        "esal": 30000,
        "eadd": "Mumbai"
    }
    response = requests.post("{}{}".format(BASE_URL, END_POINT), data=json.dumps(new_emp_data))
    # print(response.json())
    print(response.status_code)
    print(response.json())
create_source()


# def update_source(id):
#     new_emp_data = {
#         "id": id,
#         "esal": 20000,
#         "eadd": "Bang"
#     }
#     import pdb
#     # pdb.set_trace()
#     response = requests.put("{}{}".format(BASE_URL, END_POINT), data=json.dumps(new_emp_data))
#     # print(response.json())
#     print(response.status_code)
#     print(response.json())
#
#
# update_source(12)

def delete_resource(id):

    data = {}
    if id:
        data = {
            "id": None
        }
    response = requests.delete("{}{}".format(BASE_URL, END_POINT), data=json.dumps(data))
    print(response)
    print(response.json())


# delete_resource("12")
