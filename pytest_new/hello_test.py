# import math
# #
# # def test_sqrt():
# #    num = 25
# #    assert math.sqrt(num) == 5
# #
# # def testsquare():
# #    num = 7
# #    assert 7*7 == 40
# #
# # def tesequality():
# #    assert 10 == 11
#
#
# class Testsample():
#    def test_hello(self):
#       print("sss")
#
# class Testsample_1():
#    def test_hello(self):
#       print("sss")
#       assert True

# import logging
# import pytest

# class Test_log_level:
#
#    @pytest_new.fixture
#    def logger_fixture(self):
#        logging.basicConfig(filename="newfile.log",
#                            format='%(asctime)s %(message)s',
#                            filemode='w')
#        log = logging.getLogger(__name__)
#        log.setLevel(logging.DEBUG)
#        return log
#    def test_we(self, logger_fixture):
#       self.log = logger_fixture
#       self.log.debug("this is first test case")
#
# import pytest
# @pytest.mark.sample
# def test_sample1():
#     print("i am in test sample1")
#
#
# def test_sample2():
#     print("i am in test sample2")
#
# def test_sample3():
#     print("i am in test sample3")

# inbuilt discovery mechanism

import pytest
import random
# random number

# @pytest.fixture(scope="module")
# def generate_random_number():
#     print("i am executing from testcase")
#     rand_num = random.randint(1,999999)
#     return rand_num


# class Test_sample1:
#     def test_sample1(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample2(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample3(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample4(self,generate_random_number):
#         print("dsfsdfs",generate_random_number)
#
# class Test_sample2:
#     def test_sample1(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample2(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample3(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample4(self,generate_random_number):
#         print("dsfsdfs",generate_random_number)
#
# class Test_sample3:
#     def test_sample1(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample2(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample3(self,generate_random_number):
#         print(generate_random_number)
#
#     def test_sample4(self,generate_random_number):
#         print("dsfsdfs",generate_random_number)


import requests

# input_body = {
#     "name": "anil",
#     "job": "tester"
# }
# response = requests.post(url="https://reqres.in/api/users", data=input_body)
# print(response.status_code)
# data = response.json()
# print(data)
# for key,value in data.items():
#     print(key,value)
#
# def get_employee_data(params=None):
#     import requests
#     response = requests.get(url="https://reqres.in/api/users", params=params)
#     return response
#
#
# print(get_employee_data())
#
# def update_employee_data(data):
#     import requests
#     response = requests.delete(url="https://reqres.in/api/users", data=data)
#     return response








# print(response.json())
#
# # response = requests.post("https://reqres.in/api/users", data={"name":"anil", "id":34})
# # print(response.json())


# response = requests.get("http://dummy.restapiexample.com/api/v1/employees",headers={"User-Agent": "XY"})
# print(response.content)
#
# response = requests.post("https://dummy.restapiexample.com/create", data=json.dumps([{"name":"anil", "age":34, "salary":45}]),headers={"content-type":"application/json"})
# print(response)

# def test_sample1():
#     print(" i am in sample1")
#
# def test_sample_funct():
#     print("i am in sample func")


import os
import requests

def test_create_directory():

    if not os.path.exists("testing"):
        os.mkdir("testing")
        print("directory created successfully")
    else:
        print("directory already found")


import requests
data ={
    "name": "morpheus1",
    "job": "leader",
}
res1 = requests.get(url="https://reqres.in/api/users?page=2")
print(res1.json())

response = requests.post(url="https://reqres.in/api/users", data=data )
print(response)

res1 = requests.get(url="https://reqres.in/api/users?page=2")
print(res1.json())