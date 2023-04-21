# question 1

# str1 = input("enter string1: ")
# str2 = input("enter string2: ")
# op1 = ""
# op2 = ""
# for ele in str1:
#     if ele not in str2:
#         op1 = op1 + ele
# for char in str2:
#     if char not in str1:
#         op2 = op2 + char
# print(op1)
# print(op2)
#
# # question 2
#
# list1 = [["u1","u2"], ["u3","u4"], ["u1","u5"], ["u2","u1"], ["u3","u4"]]
# list2 = []
# for element in list1:
#     if [element[1], element[0]] not in list2 and element not in list2:
#         list2.append(element)
# print(list2)



# l = [10,20,30,40,40,50]
# mm = l[0]
# for i in l:
#     if mm < i:
#       mm = i
#
# print("max value", mm)
#
# for i in l:
#     if mm > i:
#         mm = i
# print("min value", mm)

# -------------------------------------------
# string = "ashok how are you"
# estr = ""
# for i in string.split():
#     estr += " "+i[::-1]
# print(estr)










# lists:
# list = [1,2,3,4,5,6,7]
# i = 4
# if i in list:
#     print("4")


# STRINGS
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))



# for x in range(1, 11):
#     print(11-x)
#
# x = 10
# while x >= 0:
#     print(x)
#     x -= 1


l = [10,20,30,40,40,50]
# print(l.count(10))
#
# count = 0
# for i in range(0, len(l)):
#      count += 1
# print(count)

total = 0
for i in range(0, len(l)):
    total = total + l[i]
print(total)

# new = []
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

# num = 40
# count = 0
# for ele in l:
#     if(ele==num):
#         count = count+ 1
# print(count)

# string = "Operation=DescribeApplicationVersions&ApplicationName=PKnewwebapp&Name=myresource"

# new_string = "ApplicationName=PKnewwebapp&Name=myresource&Operation=DescribeApplicationVersions"
#
# string, new_string = new_string, string
#
# print(string)








# data = custumers.objects.get(sal > 1000000 )


# ----------------------------------------------------
# Multiple inheritance example:

# # inheritance:
#
# class Parent():
#     def m(self):
#         print("class is parent")
# class child(Parent):
#     def m(self):
#         print(" class is child ")
# class child1(Parent):
#     def m(self):
#         print("class is child1")
#
# class child2(child, child1):
#     def m(self):
#         print("class is multiple inhertiance")
# n = child2()
#
#
# n.m()


# -------------------------------------------

# finding even numbers using lambda

# list1 = [10, 20, 30, 40, 3, 11, 45, 95]
#
# even_nos = list(filter(lambda x: (x % 2 == 0), list1))
# print("even numbers in the list : ", even_nos)
# # print(list)




# ---------------------------------------------------------------------

#
# l = [1,2,3,4,5]
# #
# # str = str(l)
# # print(str)
#
# listtostr = ''.join([str(elements) for elements in l])
# print(listtostr)

# ['1','2','3','4','5']

# -----------------------------------------------
# Printing input 5 times

# str1 = ("Ashok")
# print(str1 * 5)
#
# for i in range(5):
#  print(str1)




# static method
# class Ashok:
#     def _init_(self):
#         pass
#     @staticmethod
#     def hello():
#         print("hey ")
#     def hello1(self):
#         print("hiiiii")
#
# d1 = Ashok()
# d1.hello()
# d1.hello1()
# d2 = Ashok()
#
# ---------------------------------------
# example docker file

# from ubuntu
# run apt_get update
# run apt-get install -y nginx
# cmd ["echo", "image create"]
#
#
# from python:3
# add script.py/
# run pip install re.txt
# cmd ["python ", " /script.py"]
#
#
#
# docker build -t pythonf







import json
#
# emp name
# emp id(pk)
# emp salary
# emp depat
#
# class Emp(models.Model):
#
#     data = json.dump()
#
#
#     {"name" : "ashok",
#      "id": 204,
#      "salry": 2000
#      "depat" : "it"
#
#
#      }

# -----------------------------------------------------------

# most freaquently asked question Decarator and example program

# def divide(a,b):
#     print(a/b)
# def sub_divide(func):
#     def inner(a,b):
#         if(a<b):
#             a,b = b,a
#             return func(a,b)
#     return inner
# d1 = sub_divide(divide)
# d1(2,4)


# ------------------------------------------------

# A= "IndaianArmyAaa"
# o/p:6,a

# if "A" and "a" in A:
#     print(A.count("A"))

# for i in range(0, len(A)):
#     count = 1
#     for t in range(i+1, len(A):
#        if(A[s] == A[t] and A[s]) != "")
#     count = count + 1
#     A = A[::t] + "0" + A[t+1:])











# ----------------------------------------------------------------------------------------
# finding the sum of values in a file by giving input means Manam 1-9 values inputga isthe return lo motham sum aiye ravali
# total = 0
# with open("file.txt", "r") as inp, open("output.txt") as outp:
#     for line in inp:
#         try:
#             num = float(line)
#             total = total + num
#             outp.write(line)
#         except ValueError:
#             print("{} is not a number ".format(line))
#
# print("total of all numbers: {} ".format(total))
#
#
#--------------------------------------------------------------------
# def countnumberofzeros(arr, n):
#     flag = 0
#     pos = 0
#     count = 0
#     for i in range(n):
#         if arr[i] is 0:
#             flag = 1
#             pos = i
#             break
#
#     if flag is 1:
#         count = n-pos
#     return count
# arr = [1,2,3,0,0,0,0,0,1,3,3,3,0,0,0,0]
# n = len(arr)
# print("number of zeros founded are: ", countnumberofzeros(arr, n))
# --------------------------------------------------------------------

















# nodes = [{
# "name" : "A",
# "id" : 27,
# "pid": 3
# },
# {
# "name" : "B",
# "id" : 3,
# "pid" : 1
# },
# {
# "name" : "C",
# "id" : 42,
# "pid" : 1
# },
# {
# "name" : "D",
#
#
#
# "id" : 11,
# "pid" : 2
# },
# {
# "name" : "E",
# "id" : 23,
# "pid" : 5
# }]


# list1 = len(nodes)
# for i in range(list1-1):
#     for j in range(i+1, list1):
#         if nodes[i][1] > nodes[j][1]:
#             total = nodes[i]
#             nodes[i] = nodes[j]
#             nodes[j] = total
# sortdict = dict(nodes)
# print(sortdict)

# -------------------------------------------------------
# lista = [1, 2, 3, 4, 5, 3, 3, 2]


# print unique elements from the above list [1,4,5]

# new_list = []
# for i in lista:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

#
# --------------------------------------------
# find out unique values from list
# lista = [1,2,3,4,5,3,3,2]
# def unique_list():
#     list_uniquues = []
#     unique_numbers = set(list)
#     for lista in unique_numbers:
#         list_uniquues.append(lista)
#     return list_uniquues
# print(unique_list())

# --------------------------------------------------
# adding 2 list into matrix form
# lista = [1, 2, 3, 4, 5]
# listb = [6, 7, 8, 9, 10]
#
# # op: [(1, 6,), (2, 7), (3, 8), (4, 9), (5, 10)]
#
# join = dict(zip(lista, listb))
# print(list(join))
#
# join_list = [(lista[i], listb[i]) for i in range(0, len(lista))]
# print(join_list)
#----------------------------------------------------------------------------
# count repeated stings
# string1= "helllowlw"
# string2 = {}
#
# for i in string1:
#     if i in string2:
#         string2[i] += 1
#     else:
#         string2[i] = 1
# print("count od values: \n"+ str(string2))


# d={'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
# for i in d.values():
#     if
# value = dict.pop('a')
# print(value)
# print()
# print(""+)
# for i in range(len(d)):
#     if d[i]['a'] == 2:
#         del d[i]
# print("list of dict"+str(d))

#
#
# class a:
#     @api_view=['GET', 'POST']]
#     def _init_(self, fname, lname):
#         self.firstname = fname
#         self.lastnamew = lname
#     def print_something(self):
#         print(self.firstname, self.lastnamew)
# class Student(a):
#     def _init_(self, fname, lname, year):
#         super()._init_(fname, lname)
#         self.gradyear = year
#     def welcome(self):
#

# a=[1,2,3,4]
# b=[3,4,5,6]
#
# op c = [4, 6, 8, 10]


# print("originsl list: "+str(a))
# print("orinal list: " +str(b))
# res_list = []
# for i in range(0, len(a)):
#     res_list.append(a[i] + b[i])
# print(str(res_list))

# # c = a + b
# # print(c)
#
#
# c = zip(a,b)
# print(c)


# 2. Write a function to checl whether a list is unique or not.
# Function should take list as an input parameter and return True or False.
# for eg list [1,2,3,4] returns True and list [3,4,4,5,6] should return False


# def unique():
Alist = [3, 4, 4, 5, 6]
#
# print("given list: ", Alist)
# if len(set(Alist) == len(Alist)):
#     print("elements unique")
# else:
#     print("mot unique")

# def check(x):
#     for elem in x:
#         if x.count(elem)>1:
#             return
#

num = int(input("enter the number"))
flag = False
if num>1:
    for i in range(2, num):
        if (num%i) == 0:
            flag = True
            break
    if flag:
        print("its a not a prime:", num)
    else:
        print("its a prime:", num)

list1 = [2,3,4,5]
# for i in range(0, len(list1)):
square_list = list(map(lambda x: x**2, list1))
print(square_list)


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

def finding(nums, len, tot):
    print("total sum is: ", tot)
# def finding(i, j, nums):
#     for i, j in range(len, tot):
    for i in range(len):
        for j in range(i, len):
            if nums[i]+nums[j] == tot:
                print(nums[i], nums[j])
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tot = 9
finding(nums, len(nums), tot)