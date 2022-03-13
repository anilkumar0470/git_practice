class Sample:
    count = 0

    # def __new__(cls, *args, **kwargs):
    #     print("I am in new method")

    def __new__(cls, *args, **kwargs):
        print("auueuue")
        return super(Sample, cls).__new__(cls)

    def __init__(self, name, age):
        print("I am init method")
        self.name = name
        self.age = age
        Sample.count += 1

    def display_details(self):
        print("name :{} age : {}".format(self.name, self.age))

    @classmethod
    def sample_class_method(cls):
        print("i am in class method ", Sample.count)

    @staticmethod
    def test_static_method():
        print("I am in static method")


# s = Sample("anil", 27)
# s.display_details()
# Sample.sample_class_method()
# s.test_static_method()


class A:

    def __new__(cls, *args, **kwargs):
        print("i am in new method")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("i am in init method")

A()


class B:

    def __init__(self):
        print("init method")
        return "checking"
# print(B())


class GeeksForGeeks():

    def __str__(self):
        return "GeeksForGeeks"


class Geek():

    def __new__(cls, *args, **kwargs):
        return GeeksForGeeks()

    def __init__(self):
        print("333")

print(Geek())



list1 = [10,20,13,10,20,23,234,2344,10]
# 10, 20, 13, 23, 234, 2344

for element in list1:
    occ = list1.count(element)
    if occ > 1:
        for i in range(occ-1):
            list1.remove(element)

print(list1)


for num in range(2,20):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print(num)

out = [num for num in range(2,20) if all(num%i !=0 for i in range(2,num))]