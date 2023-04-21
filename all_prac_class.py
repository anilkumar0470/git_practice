"""
t = (1,2,3,4,2,5,2)
print type(t)
print t.count(2)
print "hai",t.index(2)
l = ['anil','kumar','sita','shanti',1,2,3,4]
print "length:",len(l)
print l[6]
l.append([1,2,3,4])
print l
print l[8][2]
l.extend((85,96,85))
print l
l.insert(0,4)
print l
l[0]='pathapati'
print l
l[10]=78
print l
print l.pop()
print l
print l.remove(78)
print l
print l.count(2)
print "this is output is belonging to strings only"
str = 'anilkumar pathapati naidu'
print str.count('a')
print str.count('p')
print str.find('p')
print str.index('n')
print str.find('w')
print str.index('u')
a = str.lower()
print a
b = str.upper()
print b
c = str.title()
print c
d = c.istitle()
print d
e = 'anilkumar'

print e.islower()
print e.isalpha()
print e.isalnum()
f = 'PATHAPATI'
print f.isupper()
print f.isalpha()
print f.isalnum()
print str
print str[1:7]
print range(10)
print str.startswith('anil')
print str.startswith('anilkumar p')
print str.startswith('nil')
print str.endswith('idu')
print str.endswith('naidu')
print str
#a = input("enter the string ")
#if 'a' in str :
   # print "searching word is found"
print str.capitalize()
print str.replace('anilkumar','aneelkumar')
print str
q = 'anilkumar is pathapati '
print q.lstrip()
print q.rstrip()
print q.strip()
print q.split('is')
print l
for i in l:
    for j in range(len(l)):
        print j,"==",i
print l[2]
print l.index('sita')
print "="*50
print "DICTIONARY"
d ={1:2,2:3,3:4,4:5,5:6,2:9}
print d
print d.items()
print d.keys()
print d.values()
print len(d)
for k,v in d.items():
    print k,"==",v
print d.has_key(2)
print d
d.update({2:20})
print d
d1 =d.copy()
print d1
d.pop(2)
print d
d.popitem()
print d
st = 'hello'
for i in st :

    if i == 'l':
        continue
        print "hai welcome to bvsrec"
    else:
        print i

print "generating prime numbers"
for num in range(2,20):
    for i in range (2,num):
        if num%i ==0:
            break
    else:
        print "num",num
print "welcome to india"
a=1
b=1
n=200
z = input('enter input upto where you want end:')

while a<n:
    c=2
    while c<a-1:
        if a%c==0:
            break
        c=c+1
    else:
        print "prime number:",a
    if b==z:
        print "b value is :",b
        break;
    else:
        a+=1
        b+=1
"""
# print "now we are in  functions "
# print "do practice well"

"""
def total(a,b):
    c = a+b
    return c
a = input('enter a value:')
b = input('enter b value:')
p=total(a,b)
print "total:",p
"""
# def sum(a,b):
#     c =a+b
#     print c
# sum(12,15)
#
# def details(name,age):
#     print "name:",name
#     print "age:",age
# details(age=30,name='pavan')
# def detail(name,age):
#     print "name",name
#     print "age",age
# detail('anil','23')









# str1 = input("enter string1: ")
# str2 = input("enter string2: ")
str1 = "ABC"
str2 = "BC"
str1 = "BC"
str2 = "BANGALORE"
op1 = ""
op2 = ""


# def chec

# op1 should contain all the characters which are present in str1 but NOT present in str2.
for ele in str1:
    if ele not in str2:
        op1 = op1 + ele
for char in str2:
    if char not in str1:
        op2 = op2 + char
print(op1)
print(op2)


list1 = [["u1","u2"], ["u3","u4"], ["u1","u5"], ["u2","u1"], ["u3","u4"]]
list2 = []
for element in list1:
    if [element[1], element[0]] not in list2 and element not in list2:
        list2.append(element)
print(list2)
import os
import itertools as it
def substrCount(n, s):
    if n == 1:
        return 1
    s = [list(g) for k, g in it.groupby(s)]
    res = sum([int(len(i)*(len(i)+1)/2) for i in s])

    for i in range(len(s)):
        if i == 0 or i == len(s)-1 or len(s[i]) > 1 :
            continue
        if s[i-1][0] == s[i+1][0]:
            res+= min(len(s[i-1]), len(s[i+1]))
    return res
print(substrCount(7, "abcbaba"))

#abcbaba
#a a

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = ["eat","tea","tan","ate","nat","bat"]
res = []
res1 = []
for i in range(len(strs)):
    if strs[i] in res1:
        continue
    temp = []
    for j in range(i, len(strs)):
        print("j is {}".format(j))
        print("values are {}:{}".format(strs[i], strs[j]))
        if sorted(strs[i]) == sorted(strs[j]):
            if strs[i] not in temp:
                temp.append(strs[i])
            if strs[j] not in temp:
                temp.append(strs[j])
    else:
        import pdb
        # pdb.set_trace()
        if not temp:
            temp.append(strs[i])
    res.append(temp)
    # res1.extend(temp)
res.sort()
print(res)