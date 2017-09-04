def number(num):
    for i in range(2, num):
        print i
        if num % i == 0:
            print "given number is not a prime number"
            break
    else:
        print"given number is prime number", num
a = input("enter a number to check it is a prime number or not: ")

number(a)

