



class Sample:

    def sample(cls, name):
        print("sample")

s = Sample()
s.sample("anil")


d = {u'Content-Length': u'85', u'Content-Type': u'application/json', u'key': u'$ENV.NAME'}
for key, value in d.items():
    if "$ENV" in value:
        print(key)

a = "anil"
b = a[::-1]
print(a == b)
even = []
odd = []
elements = []


for i in a:
    if a.count(i) % 2 == 0:
        even.append(i)
        if i not in elements:
            elements.append(i)
    else:

        if i not in elements:
            elements.append(i)
            odd.append(i)
if len(odd)>1:
    print("it is not palindrome")
else:
    print("Palin drome")


# if a.count(a[0]) == len(a):
#     print("it can be a palindrome")
# elif len(a)%2 == 0:
#     print('Not palin drome')
d = {}
l = []
st = "abafgabadfgcbcbcedrfrfrfrasdededed"
for k in range(len(st)) :
    for j in range(k,len(st)+1):
        m = st[k:j]
        r = m[::-1]
        if m == r:
            if len(m) not in l :
                l.append(len(m))
            d.update({m: len(m)})

print(l)
print(d)
for key, value in d.items():
    if value == max(l):
        print("largest palindrome  {} and length {}".format(key, value))


# N = input()
#
# # Get the input
# numArray = map(int, raw_input().split())
#
# sum_integer = 0
# # Write the logic to add these numbers here
#
# for num in numArray:
#     # Print the sum
#     val = num * num
#     print(val)
#     sum_integer = sum_integer + val
# print sum_integer

#
# # Get L and R from the input
# L, R = map(int, raw_input().split())
#
# # Write here the logic to print all integers between L and R
#
# for i in range(L, R+1):
#     print(i),
#
# open_list = ["[", "{", "("]
# close_list = ["]", "}", ")"]
# # Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                     (open_list[pos] == stack[len(stack) - 1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
# # Driver code
# string = "{()}[]"
# print(string, "-", check(string))
#
# string = "[{}{})(]"
# print(string, "-", check(string))


str1 = "anil"
str2 = "kumarpatha"
if len(str1) < len(str2):
    count = len(str1)
    res = str2[len(str1): ]
else:
    count = len(str2)
    res = str1[len(str2):]


for j in range(count):
    print(str1[j], end ="")
    print(str2[j], end='')
print(res)


# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
    print("9999\n")
    print(num % 2, end='')

dec_val = 5
# Calling function
DecimalToBinary(dec_val)


 