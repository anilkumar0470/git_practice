# global l
# l = [0,1]
#
#
# def fib(x):
#     return l.append(l[x-1]+l[x-2])
# f = filter(fib,(x for x in range (2,20)))
# print l


# exception handling

a = 10
b = 0
l = [1,2,3]
# try block which may generate the exception
try:
    c = a/b
    print(c)

except :
   pass
else:
    print(c + 10)
    print("i am in else block ")
finally:

    print("this will be executed for sure")







# better information
# l = [1,2,3]
# l[5]
# print("good morning")