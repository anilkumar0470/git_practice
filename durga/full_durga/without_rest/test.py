import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijsoncbv/'
response = requests.post("{}{}".format(BASE_URL, END_POINT))
if response:
    data = response.json()
    print(data)
    # print("employee name:: {}".format(data["ename"]))
    # print("employee eno :: {}".format(data["eno"]))
    # print("employee add :: {}".format(data["eadd"]))
