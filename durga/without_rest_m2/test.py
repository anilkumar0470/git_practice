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

    response = requests.get("{}{}".format(BASE_URL, END_POINT), data=json.dumps(data))
    print(response)
    print(response.json())


get_resource(3)
