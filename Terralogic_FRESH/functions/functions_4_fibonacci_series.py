# #Example for generating fibonacci series
def fibonacci_series(num):
    a = 0
    print (a)
    b = 1
    for i in range(num):
        c = a + b # 1 1 2
        print (c)
        b = a # 0  1  1
        a = c # 1  1  2   2


# num = input("enter a number:")
fibonacci_series(10)
# print("*"*50)
# fibonacci_series(20)
#
#
# a = 0
# print(a)
# b = 1
#
# for i in range(20):
#     c = a + b
#     print(c)
#     b = a
#     a = c
#
#
# a = 0
# print(a)
# b = 1

# for i in range(20):
#     c = a + b
#     print(c) # c value
#     b = a  #
#     a = c
#
#
# a = 0
# b = 1
#
# print(a)  # 0
# for i in range(10): #
#     c = a + b # 1 1 2
#     print(c)
#     b = a # 0 1  1
#     a =c  # 1 1
#
# print(a)  # 0
# for i in range(20): #
#     c = a + b # 1 1 2
#     print(c)
#     b = a # 0 1  1
#     a =c  # 1 1