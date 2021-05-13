import requests
BASE_URL = "http://localhost:8000/"
END_POINT = "apijsonnewcbv"
print(END_POINT)
response = requests.put("{}{}".format(BASE_URL, END_POINT))
print(response)
print(response.json())