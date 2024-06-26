# to find the occurrence of characters and display max occurrence character
#
# str = "hi all good morning how are you "
# d = {}
# for i in str:
#    if i not in d and not i.isspace():#
#        d.update({i: str.count(i)})
# max_value = max(d.values())#5
# for k, v in d.items():
#    if v == max_value:
#        print(k, v)


# to rotate the given list left with three positions

l = [1,2,3,4,5,6,7] # 4567123
# 2345671
# 3456712
# 4567123
# n = 3
# for i in : # 0 1 2 3  i = 0
#    l.append(i)
#    l.remove(i)
# print(l)

# list1 = [10, 30, 90, 60, 50, 65]
# for i in range(len(list1)): #0 ,1,2,3,4,5
#    for j in range(i+1, len(list1)): ## 1,2,3
#        import pdb
#        pdb.set_trace()
#        if list1[i] > list1[j]: # 10 > 30
#            list1[i], list1[j] = list1[j], list1[i]
#
# print(list1)

#reverse a string

str1 = "good evening"
# print(str1[::-1])

result = ""

for i in str1: # g , o, od
    result = i + result # g , g+o=go,o+og=oog,d+oog = doog,
# print(result)


# start
# end
# step

# to display the even number of dictionary keys

# dict1={1:'a',2:'b',3:'c',4:'d',7:'e',8:'f',"name":"har"}
# for key in dict1.keys():
#     if type(key)  == int:
#        if key %2 == 0 : # modulus operator
#            print(key, dict1[key])


# fibonacci series
# a = 0
# print(a)
# b = 1
# for i in range(5): # [0,1,2,3...9]
#    c = a + b # 1 1 2 3 5 8  b = a , a = c
#    print (c)
#    b = a # 0 1 1 2 3
#    a = c # 1 1 2 3 5

#
# # factorial of given number
# num = 5 # 5 *4 3 2 1
# factorial = 1
# if num < 0:
#    print("factorial does not exist for negative numbers")
# elif num == 0:
#    print("the factorial is 1 for zero")
# else:
#    for i in range(1, num + 1): # 1,2,3,4,5 i =5
#        factorial = factorial * i #1*1,2*1=2, 2 * 3 = 6,4*6  =24,24 * 5 = 120
#    print("factorial is ",factorial)
#
# num = 72
# # 2,3,--
# #
# # #prime number to check
# # for i in range(2,num): # 2,3,4,5,6
# #    if num%i == 0: # 7%2 = 1
# #        print("given number is not prime number")
# #        break
# # else:
# #    print ("given number is prime number ")
# #
# # #generate prime numbers in the given range
# # for num in range(10, 20):
# #    for i in range(2, num):
# #        if num % i == 0:
# #            break
# #    else:
# #        print("prime number {}".format(num))

# for i in range(10):
#     print(i, end=" ")
# for i in range(5):# i = 3
#     for j in range(i):# 0,1,2
#         print("*", end= " ")
#     print("")


# *
# * *
#  * * *

# class Bye:
#     def sample(self):
#         print("good")
#
# b1 = Bye()
# b1.sample()


class TestSample:
    def test_sample1(self):
        print("good evening")
        print("good byyyy")

    def test_sample2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys

        import time

        driver = webdriver.Chrome(executable_path=r"C:\Users\SBI BC POINT\Desktop\testtt\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.co.in/")
        time.sleep(3)
        assert driver.title == "Google", "title is not matching"


