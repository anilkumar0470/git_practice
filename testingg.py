#
#
#
#
# # # class A:
# # #
# # #     def method1(self):
# # #         print("i am in method1 class A")
# # #
# # #
# # # class B:
# # #
# # #     def method1(self):
# # #         print("i am in method1 class B")
# # #
# # #
# # # class C(A, B):
# # #     def method2(self):
# # #         print(" i am in method2 class C")
# # #
# # #
# # #
# # # c  = C()
# # # c.method1()
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # class Sample
# # # #     COUNT = 0
# # # #     @classmethod
# # # #     def sample_class_method(cls):
# # # #         print("i am in class method")
# # # #         print(cls.COUNT)
# # # #
# # # #
# # # #     @staticmethod
# # # #     def sample_static_method(cls):
# # # #        pass
# # # #
# # # #
# # # # Sample.sample_class_method()
# # # # # Sample.sample_static_method(Sample)
# # # #
# # # #
# # # # list1 = [10,20, 3434, 45,100,1,3,4,5,34,67,88,8,9,9,3,3,3]
# # # #
# # # #
# # # # def sample_function(element):
# # # #     return element*2
# # # #
# # # #
# # # #
# # # # out =  list(map(sample_function, list1))
# # # # print(out)
# # # #
# # # # #
# # # # # l = [1,"name", "loc"]
# # # # # new_list = []
# # # # # for element in list1:
# # # # #     if element not in new_list:
# # # # #         new_list.append(element)
# # # # # print(sorted(new_list))
# # # #
# # # #
# # # #
# # # # # new_dict = {}
# # # # # for value in list1:
# # # # #     if value not in new_dict:
# # # # #         new_dict.update({value:list1.count(value)})
# # # # # print(new_dict)
# # # #
# # # #
# # # #
# # # #
# # # # # obj = iter(list1)
# # # # #
# # # # # while True:
# # # # #     try:
# # # # #         print(next(obj))
# # # # #     except StopIteration:
# # # # #         break
# # #
# # # # serialization and deserialization
# # # # for loop to print the values
# # # # difference between dict and map
# # # # pytest features
# # #
# # # string = "good@eving*f"
# # # result = ""
# # # d ={}
# # # for element in string:
# # #     if element.isalpha():
# # #         print(element, ord(element))
# # #         result = element + result
# # #     else:
# # #     #     import pdb
# # #     #     pdb.set_trace()
# # #     #     print(element)
# # #     #     result = result + element
# # #           d.update({string.index(element):element})
# # #     # print(result)
# # # print(result,d )
# # # st  = ""
# # # for var in range(len(result)):
# # #     print(var)
# # #
# # #     if var in d :
# # #         st = st + d[var]
# # #     else:
# # #         st = st + result[var]
# # #
# # # print(st)
# # #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # names = ['Chris', 'Jack', 'John', 'Daman']
# # # print(names[-1][-3])
# #
# # # print(" ".join(names))
# # #
# # # s='Online Python compiler'
# # #
# # # vowels = ['a','e', 'i', 'o', 'u']
# # # out = [x for x in s if x in vowels]
# # # print(out)
# # #
# # # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # #
# # # list_out = [fruit for fruit in fruits if "e" in fruit]
# # # print(list_out)
# #
# # # random even number by using lambda expression
# #
# # # import random
# # # # a  = lambda x : x * 2
# # # num = random.randint(10, 100)
# # # print(num)
# # #
# # # list_outt = [num if num%2==0 else "not even number"]
# # #
# # # print(list_outt)
# #
# #
# # class Parent:
# #
# #     def __init__(self):
# #         print(" I m parent")
# #
# #     def method1(self, name):
# #         print(" I am in method 1 parent class")
# #
# #
# # class Child(Parent):
# #
# #     def method1(self, name):
# #         print(" I am in method1 child class")
# #         self.name = name
# #
# #
# # # c = Child()
# # # c.method1("good")
# # # [4:42 PM] Praveen Kumar Mishra
# # #     names = ['Chris', 'Jack', 'John', 'Daman']
# # # print(names[-1][-3])
# # # ​[4:44 PM] Praveen Kumar Mishra
# # #     s='Online Python compiler'
# # # ​[4:46 PM] Praveen Kumar Mishra
# # #     fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
# # k=5
# # for i in range(k):
# #   if i == int(k/2):
# #     print("~"*int(k/2)+"*"+"~"*int(k/2))
# #   else:
# #     print("~"*k)
#
#
# #
# # num = 12
# # b = 2
# # r = 3
# # y = 1
# #
# # c = int(num * 3)/2
# # # print(int(c))
# #
# # ind_val = num/3
# #
# # list1 = list(range(0, num, int(ind_val)))
# # # print(list1)
# # last1 , last2, last3 = list1
# # # print(last1, last2, last3)
# #
# # for j in range(int(num)):
# #     for i in range(int(c)):
# #         # print(j)
# #         if j >= last1 and j < last2:
# #             print(b, end=' ')
# #         if j >= last2 and j < last3:
# #             print(r, end=' ')
# #         if j>=last3 :
# #             print(y, end=' ')
# #     print()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import socket
# # hostname=socket.gethostname()
# # IPAddr=socket.gethostbyname(hostname)
# # print("Your Computer Name is:"+hostname)
# # print("Your Computer IP Address is:"+IPAddr)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # for i in range(5):
# #     for j in range(i+1):
# #         print("*", end=" ")
# #     print()
#
#
# # right handed triangle
# #                     *
# #                 *   *
# #             *   *   *
# #         *   *   *   *
# #     *   *   *   *   *
#
#
# for i in range(5):
#     for j in range(5-i):
#         print("  ", end="")
#     for k in range(i+1):
#         print("*", end=" ")
#     print("")
#
# for i in range(5):
#     for j in range(5-i):
#         print("  ", end="")
#     for k in range(i+1):
#         print("*", end=" ")
#     print("")
#
#
#
#
#
#
# import itertools
#
#
# squares =  map(pow, range(10), itertools.repeat(3))
#
# print(list(squares))
#
# #  for port in dnac_handle.dnaconfig.ixiaedgeports:
# #             logger.info("configuring traffic on port:{}".format(port))
# #             ixia_client.config_traffic_ipv4(dnac_handle.dnaconfig.ixia_fusion_interface, port)
# #             # ixia_client.config_traffic_ipv6(dnac_handle.dnaconfig.ixia_fusion_interface, port)
# #             i = i + 1
# # list1 = []
# # list2 = []
# # for ind in range(len(dnac_handle.dnaconfig.ixiaedgeports)):
# #     if ind %2 ==  0:
# #         list1.append(dnac_handle.dnaconfig.ixiaedgeports[ind])
# #     else:
# #         list1.append(dnac_handle.dnaconfig.ixiaedgeports[ind])
# #
# # for value1, value2 in zip(list1, list2):
# #     ixia_client.config_traffic_ipv4(value1, value2)
#
#


list1  = ['1', '2', '3', '4', '5', '6']
list2 = []

for i in range(len(list1)):
    if i < len(list1)-1:
        list2.append(list1[i])
        for j in range(i+1, len(list1)):
            list2.append(list1[j])

print(list2)


















