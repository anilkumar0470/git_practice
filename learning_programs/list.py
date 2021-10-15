import re
a = "anilabapathapatiababathirupal"
# for i in range(len(a)):
#     patt = r'({}).*?\1.*?\1'.format(a[i])
#     #print(patt)
#     c = a[i:]
#     #print(c)
#     m = re.search(patt, c)
#     if m :
#         #print(m.group())
#         b = m.group()
#         if b == b[::-1]:
#             print("palin drome and length is {}".format(len(b)))
#         else:
#             pass


reverse = a[::-1]
c = 0
for i,j in zip(a, reverse):
    if i == j:
        c = c + 1
print(c)


# class Singletone():
#     __single = None
#
#     def __init__(self):
#         if Singletone.__single:
#             raise Singletone.__single
#         Singletone.__single = self
#
#
# class Child(Singletone):
#
#     def __init__(self, name):
#         Singletone.__init__(self)
#         self.__name = name
#
#     def name(self):
#         return self.__name
#
#
# class Junior(Singletone):
#     pass
#
# def Handle(x = Singletone):
#     try:
#         single = x()
#     except Singletone, s:
#         single = s
#     return single


temp =""";RTRV-ULSDCC-L3:mlvlnjmikae::C;
IP C
<

   MLVLNJMIKAE 20-03-06 09:57:04
M  C COMPLD
   ":L3IDP=39840F"
   ":L3DFI=80"
   ":L3ORG=000000"
   ":L3RES=0000"
   ":L3RD=0000"
   ":L3AREA=0000"
   ":L3SYS=00601D2FEAEF"
   ":L3SEL=00"
   ":L3LV2IS=disable"
   ":NSAPTHLEV=0"
   ":NSAPCOUNT=12"
;'"""
import re
res = re.findall('\w+=\w+' , temp)
d = dict([map(str.strip, i.split('=')) for i in res])
print(d)
if re.search('L3IDP', temp):
    NSAP = (d['L3IDP'],d['L3DFI'],d['L3ORG'],d['L3RES'],d['L3RD'],d['L3AREA'],d['L3SYS'])
    print("sss", NSAP)
else:
    NSAP = (d['L3AFI'],d['L3IDI'],d['L3DFI'],d['L3ORG'],d['L3RES'],d['L3RD'],d['L3AREA'],d['L3SYS'])
NSAP_ID = ''.join(NSAP)+'1D'
print(NSAP_ID)

















# l = [1,5,6,1,2,4,2]
# # d =  {1:2, 5:1,....}
# d = {}
# for i in l:
#     if i not in d:
#         d[i] = l.count(i)
# # print(d)




# l1 =[1,0,0,1,1,0,1,0,1]
# # 1 1 1 1 1 = 5
# count = 0
# initial_value = l1[0]
# for i in range(1, len(l1)):
#     if l1[i] != initial_value:
#         count = count + 1
#         initial_value = l1[i]
#     else:
#         initial_value = l1[i]
#
# print(count)


# fd1 = open("sample.txt", "r")
# fd2 = open("hello.txt", "w")
# lines = fd1.readlines()
# for line in lines:
#     if len(line) > 1 and line != "\n":
#         fd2.write(line)
#         fd2.write("\n")
# fd1.close()
# fd2.close()

list = [x if i%2 == 0 else None  for x in range(10, 50) for i in range(2,x)]
print(list)
# l2  = []
# for i in range(10):
#     if :
#         l2.append()



















def sample(a,b,c):
    trick = a | b & c
    print((trick))

sample(24,30,34)







l = ["a", "b", "c", "d"]
print(",".join(l))

class A:
    def __init__(self, a, b, c):
        self.x = a + b + c

a = A(1,2,3)
b = getattr(a, 'x')
setattr(a, 'x', b + 1)
print(a.x)


def hello():
    pass
print(type(hello()))

# n = "come,bye,almond,zipper"

n = 5
for i in range(5):
new_list = n.split(",")
print(sorted(new_list))

print(",".join(sorted(new_list)))


class Website:
    URL = "junk, "

    @classmethod
    def getMostVisitedPages(cls):

