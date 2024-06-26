# # class Parent:
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def display(self):
# #         print("name {} age {}".format(self.name, self.age))
# #
#
# #
# # p = Parent("sam", 27)
# # p.display()
# #
# # class Child(Parent):
# #     pass
# # c = Child("nag", 32)
# # c.display()
#
#
# # restricting
#
# # class Sample:
# #
# #     a = 10
# #     __b =  10
#
#
# # class Sample():
# #
# #     def add(self, a, b):
# #         print(a + b)
# #
# # class Test(Sample):
# #
# #     def add(self, a, b):
# #         print(a - b)
# #
# #
# # t = Test()
# # t.add(1
#
#
#
#
#
# # "message":"2022-03-16T19:13:25.853819-04:00 ASM-AMS-SBC01A SBC - - - ACT 1 0 Info CAM ,88,0,0,7,01,0,7,P:1:,0,0,P:1:,0,FOTIVE_AC_SBC_Zone,PURE_IP_Zone,555,123,,,,,0x00000000,,,,,,,,,,,,,,,,4,01,0,0,0,0,2,01,No DSP inserted,No DSP inserted"
# #
# # "message":"2022-03-16T19:29:07.434215-04:00 ASM-AMS-SBC01A SBC - - - ACT 1 0 Info CAM 55616,185.109.45.199:40784,0:0:0:0,124,,,,,01,audio,1,1785,1355,285600,216800,0,0,1355,1785,216800,285600,0,0,0,,,,,,,,,,,,,,0,,,0,,0,89,117,0,0,0,117,89,0,0,7,01,0,0,P:1:,0,0,P:1:,0,FOTIVE_AC_SBC_Zone,PURE_IP_Zone,555,123,,,,,0x00000000,,,,,,,,,,,,,,,,4,01,0,0,0,0,2,01,Transcoding,No DSP inserted"
# #
#
#
#
# fd = open("sample.json", )
# lines = fd.readlines()
# import re
# pattern = "\"message\"\:\"(.*)\""
# for line in lines:
#     if line.strip():
#         match_obj = re.search(pattern, line)
#         if match_obj:
#             print(match_obj.group(1))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

class Sample:
    def function1(self,a,b,c):
        print(a,b,c)

    def function1(self,*args):
        print(args)

s = Sample()
s.function1(10,3,4,5,5)