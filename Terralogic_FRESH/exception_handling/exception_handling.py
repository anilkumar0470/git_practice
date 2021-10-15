# exception handling


# try:
#     # a code which may generate error
#
# except:
#     # after exception if you want to something u can write here
#
# l = [1,2,3,]
# print(l[4])
# a = 10
# b = 0
# c = a/b
# print("good morning ")
#
try:
    fd = open("aaa.txt")
except FileNotFoundError:
    print(" please give a valid file name or given file not found ")
else:
    print(" i am in else block ")
    print(fd.readlines())
finally:
    print("this block will be executed for sure")
    # fd.readlines()

