import requests


def get_call(url):
    response = requests.get(url)
    print("url is {}".format(url))
    if response.status_code:
        print(response.status_code)
        return response.json()
    else:
        return response.status_code


def post_call(url, data, ):
    response = requests.post(url, data)
    print("url is {}".format(url))

    if response.status_code:
        print(response.status_code)
        return response.json()
    else:
        return response.status_code

