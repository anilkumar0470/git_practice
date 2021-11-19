#This is an example for search method
# https://blog.finxter.com/python-regex-greedy-vs-non-greedy-quantifiers/
import re
#
# fd = open("aaa.txt", "r")
# lines = fd.readlines()
# for line in lines:
#     pattern = "(\d+)\.(\d+)\.(\d+)\.(\d+)"
#     match_obj = re.search(pattern, line)
#     if match_obj:
#         # print(match_obj.group(1))
#         # print(match_obj.group(2))
#         # print(match_obj.group(3))
#         # print(match_obj.group(4))
#         # print(type(match_obj.group(1)))
#         a = int(match_obj.group(1))
#         b = int(match_obj.group(2))
#         c = int(match_obj.group(3))
#         d = int(match_obj.group(4))
#         # print(type(a))
#         if a > 1 and a < 255 and b > 1 and b < 255 and c > 1 and c < 255 and d > 1 and d < 255:
#             print("it is valid", line)
#         else:
#             print("it is invalid", line)
#




# import re
# string = "anilkumar 123 this is  anu anil kumar 123 fancy"
# pattern = "anil"
# match1 = re.match(pattern,string)
# print(match1)
# if match1:
#     print(dir(match1))
#     print(match1.group())
# else:
#
#     print("match not found")
  # zero or non-zer
# if match1:
#     print(match1.group())
# else:
#     print("pattern is not matching")





import re
text = "ANJ23456776656567 this is anil kumar 123 is"
pattern = 'is'
p1 = re.search(pattern,text)
print (p1)
d = p1.group()
print (d)
#
#
#
import re
t = "name          : test jinjjs age : 209"
p = 'name\s*:\s*(\w+\s*\w+)\s*age\s*:\s*(\d+)'
p1 = re.search(p,t)
print (p1)
print ("this is for group ",p1.group())
print ("this is for group 0",p1.group(0))
print ("this is for group(1)",p1.group(1))
print ("this is for group(2)",p1.group(2))
# #
c = p1.groups();
print ("this is for groups",c)