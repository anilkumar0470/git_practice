#Example for generating fibonacci series
def fibonacci_series(num):
    a = 0
    print a
    b = 1
    for i in range(num):
        c = a + b
        print c
        b = a
        a = c

num = input("enter a number:")
fibonacci_series(num)