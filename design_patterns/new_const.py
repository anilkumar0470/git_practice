# class Sample:
#     def __new__(cls, *args, **kwargs):
#         print("first")
#         instance = super(Sample, cls).__new__(cls)
#         return instance
#
#     def __init__(self):
#         print("second")
#
#     def method(self):
#         print("third")
#
# s = Sample()
# s.method()


#
# class Test_class:
#
#     def __new__(cls, *args, **kwargs):
#         print("executing first")
#         if not hasattr(cls, "instance"):
#
#             print("executing first")
#             instance = super(Test_class, cls).__new__(cls)
#             return instance
#
#     def __init__(self):
#         print("executing second ")
#
#     def method1(self):
#         print("executing third")
#
#
# t1 = Test_class()
# t1.method1()
# print(id(t1))
#
# t2 = Test_class()
# t2.method1()
# print(id(t2))




# class Test_sample:
#
#     def __new__(cls, *args, **kwargs):
#         print(" i am in new method")
#         if not hasattr(cls, "instance"):
#             print("creating first time only")
#             cls.instance = super(Test_sample, cls).__new__(cls)
#         return cls.instance
#
#     def __init__(self):
#         print("i am in init method")
#
#     def method1(self):
#         print(" i am in method1")
#
# t1 = Test_sample()
# t1.method1()
# print(id(t1))
#
# t2 = Test_sample()
# t2.method1()
# print(id(t2))


class student_details_1:

    def __init__(self):
        self.details = {"name": "anil",
                        "age": 23,
                        "loc": "bang"}

    def get_details(self, field):
        return self.details.get(field, field)


class student_details_2:

    def __init__(self):
        self.details = {"name": "kumar",
                        "age": 26,
                        "loc": "chen"}

    def get_details(self, field):
        return self.details.get(field, field)

class student_details():

    def get_details(self, field):
        return field


details = ["name", "age", "loc"]

f1 = student_details_1()
f2 = student_details_2()
f3 = student_details()

for field in details:
    print(f1.get_details(field))
    print(f2.get_details(field))
    print(f3.get_details(field))






class student_details_1:

    def __init__(self):
        self.details = {"name": "anil",
                        "age": 23,
                        "loc": "bang"}

    def get_details(self, field):
        return self.details.get(field, field)


class student_details_2:

    def __init__(self):
        self.details = {"name": "kumar",
                        "age": 26,
                        "loc": "chen"}

    def get_details(self, field):
        return self.details.get(field, field)

class student_details_3:

    def get_details(self, field):
        return field


def factory(std = student_details_3):

    details  ={

        "student1": student_details_1,
        "student2": student_details_2,
        "student3": student_details_3
    }
    return details[std]()




class Wash:

    def washing(self):
        print("washing")


class Rinse:

    def Rinse(self):
        print("ri")



