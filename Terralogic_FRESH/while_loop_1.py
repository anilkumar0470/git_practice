# # class and objects
# # class is a collection of methods(functions) and attributes(varibles) and it user defined datatype
#
# # functions
#
#
# # syntax
#
# # definition
# # self is instance of class and which is used to carry the data between the methods
#
#
# # instance variables
# # class variables
#
# class Student:
#     c = "lalli"
#     def __init__(self, name, loc):
#         self.name = name
#         self.loc = loc
#
#     def display(self):
#         print(self.name + self.loc)
#         print(self.c)
#
#     def set_class_variable(self, new_name):
#         self.c = new_name
#
#
# # s1 = Student("Lalli", "bang")
# # s1.set_class_variable("Love")
# # s1.display()
# #
# # s2 = Student("Anil", "bnfdfd")
# #
# # s2.display()
#
#
#
#
#
# # functions :
# # functions are used to write once and use many times
# #  two parts
# # function defintion
# # calling function
#
# # syntax
#
# # addition of two numbers
#
# # def sample(a,b , c,d ):
# #     print(a,b,c,d)
# # sample(10, "madhavre","rtrtrtr","aaaaattrtrtr")
#
# # default arguments
#
# def sample(name, age, loc=None):
#
#     print("name :", name)
#     print("age:", age)
#     if loc:
#         print("loc", loc)
#
# # sample("ssss", 23, "bang")
# # sample("ssss", 23)
#
# # def addition(a = 10, b = 20):
# #     print(a + b)
# #
# # addition(20, 90)
#
# # postion arguments is not matter in matter
#
# def sample(a, b, c):
#     print(a,b,c)
#
#
# # * args **kwargs
# *args -- tuple
# **
#
#
# def addition(**kwargs):
#     print(type(kwargs))
#     for i in kwargs:
#         print(i)
# addition(name="anil", loc="fff")
#
#
#
# # write a function to check prime number
# # 10,20
# # fibanoacci series
#

a = "madhav"
l =[]
letter = input("enter a character to find the index")
for i in a :
    l.append(i)
flag = False
for k in a :
    if k == letter:
        print(l.index(letter))
        l.remove(letter)
        flag = True
if not flag:
    print("invalid")




