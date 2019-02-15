# generally we have three types of methods
# 1.regular method
# 2.class methods
# 3.static methods
"""
relgular methods are one which will take instance or object of class as first argument
i.e self
class methods are the one which will take class name as first argument (cls)
static methods are the one which will not take any instance or class name
and we will use these methods when we dont want use any instance or class name in the method
"""
# class Employee:
#
#     def __init__(self,fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#         self.email = fname + "." + lname +"@terralogic.com"
#
#     def fullname(self):
#         return "{} {}".format(self.fname, self.lname)
#
#
# emp1 = Employee("anil","pathapati",40000)
# print(emp1.fullname())


# class Employee:
#
#     raise_amount = 1.05
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@gmail.com"
#
#     def fullname(self):
#         return "{} {}".format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#
#     @staticmethod
#     def is_workday(day):
#         import datetime
#         if day.weekday() == 5 or day.weekday == 6:
#             return "it is holiday"
#         return "it is working day@@!!"
#
#
# emp1 = Employee("Anil", "pathapati",60000)
# Employee.set_raise_amount(1.05)
# # print(emp1.fullname())
# # print(emp1.pay)
# # emp1.apply_raise()
# # print(emp1.pay)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# import datetime
# my_day =datetime.date(2019,2,9)
# print(emp1.is_workday(my_day))


# class Employee():
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = self.first + "." + self.last + "@terralogic.com"
#         self.pay = pay
#
#     def full_name(self):
#         return self.first + self.last
#
#
# class Developer(Employee):
#     pass
#
#
# emp1 = Developer("anil","pathapati",41000)
# emp2 = Developer("pooja","chatiri", 50000)
# print(help(Developer))
# # print(emp1.email)
# # print(emp2.email)

# class A():
#     def m1(self):
#         print("I am class A ")
# class B(A):
#     def m11(self):
#         print("I am class B ")
# class C(A):
#     def m1(self):
#         print("I am class C ")
# class D(B,C):
#     def m11(self):
#         print("I am class D ")
#
# d = D()
# d.m1()

# class Test:
#
#     def __init__(self, limit):
#         self.limit = limit
#         print("limit in init", self.limit)
#
#     def __iter__(self):
#         self.x = 10
#         print("__iter__")
#         return self
#
#     def next(self):
#         x = self.x
#         if x > self.limit:
#             raise StopIteration
#         self.x = x + 1;
#         #print(self.x)
#         return x
#
# import pdb
# pdb.set_trace()
# for i in Test(15):
#     print(i)


# class Test:
#
#     def __init__(self, limit):
#         self.limit = limit
#         print(self.limit)
#
#     def __iter__(self):
#         self.x = 10
#         return self
#     def next(self):
#         x = self.x
#         if x > self.limit:
#             raise StopIteration
#         self.x = x + 1
#         return x
# for i in Test(15):
#     print(i)

# t = ("apple", "banana", "clock")
# my_iter = iter(t)
# print(my_iter.next())
#
# st = "apathapa"
# import pdb
# #pdb.set_trace()
# for i in st:
#
#     print(i)
#
# class sample:
#
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def next(self):
#         x = self.a
#         if self.a > 20 :
#             raise StopIteration
#         self.a = +1
#         return x
# s = sample()
# my_iters = iter(s)
# for x  in my_iters:
#     print(x)


def my_gen():
    n = 1
    print("the value of n is 1")
    yield n

    n += 2
    print("the value of nn is 2")
    yield n

# a = my_gen()
# print(a)
# print(next(a))
# print(next(a))

# for item in my_gen():
#     print(item)

# my_list = [1,3,7,10]
# a = (x**2 for x in my_list)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



#This is code to validate expression

user_input = "[a+b]-{c/d}+a(*c)^2"
user_input = "[a+b-({c/d)+a}*c^2]"

sample_dict = {"{": "}", "[": "]", "(": ")"}
sample_list = [["[", "]"], ["(", ")"], ["{", "}"]]
Flag = 0
dd = []
count = 0
for letter in user_input:
    if letter in sample_dict.keys() or letter in sample_dict.values():
        dd.append(letter)
        if len(dd) == 2:
            if dd in sample_list:
                count = count + 1
                dd = []
            else:
                break

for letter in user_input:
    if letter in sample_dict:
        for num in range(0, len(user_input)):
            if user_input[len(user_input)-num-1] in sample_dict.values():
                if sample_dict[letter] == user_input[len(user_input)-num-1] :
                    user_input = user_input.replace(sample_dict[letter], " ")
                    Flag += 1
                    break
                else:
                    break
if Flag == 3 or count == 3:
    print "valid"
else:
    print "invalid"


class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class Single_linked_list:

    def __init__(self):
        self.headval = None

    def listprint(self):
        print_value = self.headval
        import pdb
        #pdb.set_trace()

        while print_value is not None:
            print(print_value.dataval)
            print_value = print_value.nextval



list1 = Single_linked_list()
list1.headval = Node("Mon")
print(list1.headval)
e2 = Node("Tue")
e3 = Node("Wed")

# linking second element to the first element
list1.headval.nextval = e2
e2.nextval = e3
list1.listprint()

