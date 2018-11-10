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


# reverse = a[::-1]
# c = 0
# for i,j in zip(a, reverse):
#     if i == j:
#         c = c + 1
# print(c)


class Singletone():
    __single = None
    def __init__(self):
        if Singletone.__single:
            raise Singletone.__single
        Singletone.__single = self

    def Handle(x = Singletone):


























