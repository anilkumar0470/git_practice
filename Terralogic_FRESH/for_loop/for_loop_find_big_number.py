#
#
# list = [100,23,10,450,85,26,74,1000, 3000,22,334343]
# # print(max(list))
# # print(min(list))
# # list.sort()
# # print(list)
# #
# big = list[0] # 1000
# for i in range(1,len(list)):  # range(1,11), [1,2,3,...10] , 1, 2, 3
#     if big < list[i]: # 100 < 1000
#         big = list[i] #
# print ("Big number is :",big)
#
# # range function
# # for loop
# # prime number
# # big number in the gievn list
# # small number in the given list
# # prime numbers in the given range
# # fibanocci series
# # while loops
#
#
#
#
# # big = list[0]
# # for i in range(1, len(list)):
# #     if big < list[i]:
# #         big = list[i]
# # print(big)
#
# # small = list[0]
# # for i in range(1, len(list)):
# #     if small > list[i]:
# #         small = list[i]
# # print(small)
#
#
# # l = [1,2,3,4,5,6,7]
# #
# # # three positons
# #
# # n = 3
# # for i in range(n+1):
# #    l.append(i)
# #    l.remove(i)
# # print(l)

c1 = ['a','b','c','d']
c2 = c1
c3 = c1[:]

c2[0] = 'c'
c3[1] = 'b'
count = 0
for c in (c1,c2,c3):
    if c[0] == 'c':
        count += 12
    if c[2] == "b":
        count += 20
print (count)

a = [0,1,2,3]

for a[0] in a:
    print (a[0])
else:
    print ("kkk")

x = "abcdef"
i = "a"
while i in x:
    x = x[:-1]
    print (i)

def f(i, v=[]):
    v.append(i)
    return v
f(1)
f(2)
v = f(3)
print(v)

import copy
a = [10,23,56,[78]]
b = copy.deepcopy(a)
a[3][0] = 95
a[1] = 34
print(b)


def b(n):
    s = bin(n)
    s1 = s[2:]
    return s1
print(b(1^2)+b(4-2))




d = {}


# for i in range(2):
#
#     pass_num = d.update({})

string = str(input("enter string"))
#string = "WELcome to online welcome training welcome online welcome to welcome"
new_list = []
for word in string.split():
    new_list.append(word.lower())
fina = []
out = []
for new_word in new_list:
    if new_word not in fina:
        fina.append(new_word)

        out.append((new_word,new_list.count(new_word)))
print(tuple(out))


def findNthTerm(n):
    # If n is even
    if (n % 2 == 0):
        n = n // 2
        n = 2 * (n - 1)
        return  n // 2

    # If n is odd
    else:
        n = (n // 2) + 1
        n = 2 * (n - 1)
        return n


x = int(input("enter a value"))
out =  findNthTerm(x)
