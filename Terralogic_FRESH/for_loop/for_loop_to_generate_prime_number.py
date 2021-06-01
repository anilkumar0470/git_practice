# a = int(input("enter a value:"))
# b = int(input("enter b value:"))
# for num in range(a,b):#10,11,12,13,14....19
#     for i in range(2,num):#2,3,4,5,6,7,8,9
#         if num % i == 0:
#             break
#     else:
#         print "prime number is:",num

# for num in range(a,b):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print("prime number {}".format(num))

# for num in range(10, 20):
#     for i in range(2, ):
#         if num % i == 0:
#             break
#     else:
#         print("prime number {}".format(num))

# num = 7
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            print("given number is not  prime number")

            break
    else:
        print("given number {} is primenumber".format(num))