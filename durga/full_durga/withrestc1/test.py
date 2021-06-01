import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def get_resource(id=None):
    data = {}
    if id is not None:
        data['id'] = id
    url = "{}{}".format(BASE_URL, END_POINT)
    response = requests.get(url, data=json.dumps(data))


    data1 = response.json()
    print(data1)
    print(response.status_code)
    # print("employee name:: {}".format(data["ename"]))
    # print("employee eno :: {}".format(data["eno"]))
    # print("employee add :: {}".format(data["eadd"]))


# get_resource(900)

def get_all_resource():
    url = "{}{}".format(BASE_URL, END_POINT)
    response = requests.get(url)
    print(response)
    if response:
        data = response.json()
        print(data)
        print(response.status_code)
    # print("employee name:: {}".format(data["ename"]))
    # print("employee eno :: {}".format(data["eno"]))
    # print("employee add :: {}".format(data["eadd"]))


# get_all_resource()
import json


def create_new_resource():
    new_emp= {
        'eno': 4,
        'ename': "lilly",
        'esal': 30000,
        'eadd': "kaligiri"
    }
    response = requests.post("{}{}".format(BASE_URL, END_POINT), data=json.dumps(new_emp))
    print(response)
    print(response.json())
create_new_resource()


def update_new_resource(id):
    new_emp= {
        'id': id,
        'eadd': "pamur",
    }
    response = requests.put("{}{}".format(BASE_URL, END_POINT), data=json.dumps(new_emp))

    print(response)
    print(response.json())
# update_new_resource(7)


def delete_resource(id=None):

    data ={
        "id": id
    }

    response = requests.delete("{}{}".format(BASE_URL, END_POINT), data=data)
    print(response)
    print(response.json())
# delete_resource()