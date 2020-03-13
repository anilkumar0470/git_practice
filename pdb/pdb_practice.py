# import pdb
# import os
# file_name = __file__
# # print(f'filename is {file_name}')
# # print("file name is {}".format(file_name))
#
# # p is used to print the value variable
# # pp is used to display the dictionary in proper format
# # l is used to display the few lines of source code
# # ll(longlist) is used to display the all the lines
# # b (break) some times you have to execute unnecessary statements, to avoid
# # we will use break b filename : line_nummber : condition
# # b  will display the breakpoints available in current execution if no
# # break points  set it will display None
# # cl is used to delete the break points cl b 1
#
#
# # def get_path(file_path):
# #
# #     head, tail = os.path.split(file_path)
# #     pdb.set_trace()
# #     return head
# #
# #
# # print(f'{get_path(file_name)}')
#
#
# # import utils
# # pdb.set_trace()
# # file_path = utils.get_path(file_name)
# # print(f'filename is {file_path}')
#
#
# class sample():
#     def __init__(self, num_loops):
#         self.count = num_loops
#
#     def go(self):
#         for i in range(self.count):
#             pdb.set_trace()
#             print(i)
#             print(i+1)
#         return
# s = sample(5)
# #s.go()
#
# def f(n):
#     import pdb
#     pdb.set_trace()
#     result = []
#     j = 0
#     for i in range(n):
#         j = i * n + j
#         j += n
#         result.append(j)
#     return result
#
# if __name__ == '__main__':
#     print (f(5))
#
#
#
#
#
#
#
#
#
import re
str = "name is anil kumar"
pat = "(\w+)\s*(\w+)\s*(\w+)\s*(\w+)"
match = re.search(pat, str)
if match:
    print(match.group(1))
    print(match.group(2))
    print(match.group())
    print(match.groups())

#
# import requests
# import pdb
# pdb.set_trace()
# bbb = requests.post("https://intranet.terralogic.com", data={"u_username":"anilkumar.pathapati@terralogic.com", "j_username":"anilkumar.pathapati@terralogic.com","j_password":"8374851518@As"})
#
# print (bbb)
# print(r)
# body = {"keyword": "1263"}
# a = r.post("https://intranet.terralogic.com/ajax/search/employee", body=body)
# print(a)






#
# def a (name="anil"):
#     pass
# a(p="junk")