def number(a, b):
    for num in range(a, b):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print"prime number", num
a = input("enter a starting value for finding prime number ")
b = input("enter a last value")
number(a, b)

