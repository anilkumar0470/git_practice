# import requests
#
# response = requests.get("https://reqres.in/api/users?page=2")
#
# print(type(response))
# if response.status_code:
#     for key in response.json()['data']:
#         print(key['first_name'])
#
# abc = "hello"
# if abc:
#    pass



class Sample:

    initial_value = 100

    def __init__(self, name, age):
        print("i am in")
        self.name = name
        self.age = age

    def display_instance(self):
        print("name:  {}  age: {} ".format(self.name, self.age))

    @classmethod
    def samp_class_menthod(cls):
        print(Sample.initial_value)

    @staticmethod
    def hello_static():

        print("Hello static method")


# s = Sample("Kumar", 28)
#
# s.display_instance()
# s.samp_class_menthod()
# s.hello_static()


# "Mapping Lists in 2D/dict
list_1 = ['a','b','c','d','e','f','g','h','i','j']
list_2 =['1','2','3']
#
# Output
# [['a','1'], ['b','2'], ['c','3'], ['d','1'],['e','2'],['f','3'],['g','1'],['h','2'],['i','3'],['j','1']]"

list3 = []
count = 1
for i in range(len(list_1)):
    list4 = []
    print(list_1[i])
    print(count)
    if count < len(list_2):
        list4.append(list_1[i])
        list4.append(list_2[count])
        list3.append(list4)
        count = count + 1
    elif count == len(list_2):
        count = 0
        continue

print(list3)























