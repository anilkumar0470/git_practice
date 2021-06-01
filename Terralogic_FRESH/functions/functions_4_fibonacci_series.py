# #Example for generating fibonacci series
# def fibonacci_series(num):
#     a = 0
#     print a
#     b = 1
#     for i in range(num):
#         c = a + b
#         print c
#         b = a
#         a = c
#
# num = input("enter a number:")
# fibonacci_series(num)
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

a = 0
print(a)
b = 1

for i in range(20):
    c = a + b
    print(c) # c value
    b = a  #
    a = c

a,b = 0,1
print(a)
for i in range(10):
    c = a + b
    print(c)
    b = a
    a =c