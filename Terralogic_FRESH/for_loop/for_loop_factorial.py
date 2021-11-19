# Python program to find the factorial of a given number .

# take input from the user
# num = 10
# factorial = 1

# # check if the number is negative, positive or zero
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial*i
#     print"The factorial of",num,"is",factorial
# num = int(input("enter a number:"))
# print(type(num))

# 5 * 4 * 3 * 2 * 1
num = 5
factorial = 1
if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial is 1 for zero")
else:
    for i in range(1,num + 1): # 1,2,3,4,5 i =5
        factorial = factorial * i # 2 * 3 = 6  =24 * 5 = 120
    print("factorial is ",factorial)


a = 0
print(a)
b = 1
for i in range(20): # [0,1,2,3...9]
    c = a + b # 1 1 2 3 5 8  b = a , a = c
    print (c)
    b = a # 0 1 1 2 3
    a = c # 1 1 2 3 5

# 0 1 1 2 3 5  8