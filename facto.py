# Python program to find the factorial of a number provided by the user.

# take input from the user
# num = int(input("Enter a number: "))
num = 10
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)


for i in range(10):
    print(i)
else:
    print("apathapa")


list1 = [1,2,3,4,5,6]
list2 = list1
list2.append(7)
print(list1)
print(list2)


import re
str = "apathapa 123 hello"
match = re.search("\w+\s*\d+", str)
print(match.group())
print(match.groups())


