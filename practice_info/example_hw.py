str1 = 'abc'
str2 = 'bcd'
for i in str1:
    if i.isupper():
        print i
        k = i.lower()
        print k
    if i in str2:
        pass
    else:
        p = str1.count(i)
        if p > 1:
            pass
        else:
            print i
for j in str2:
    if j in str1:
        pass
    else:
        p = str1.count(j)
        if p > 1:
            pass
        else:
            print j

"""
str1 = 'anil kumar  pathapati '
l=len(str1)
str =""
for i in str1:
    st=""
    while (l>0):
        st = st + str1[l-1]
        l = l-1
    str = str + st
print str

"""

"""
str1 = 'ab'
str2 = 'abbab'
for i in str1:
    if i.isupper():
        print i
        k = i.lower()
        print k
    if k in str2:
        pass
    else:
        p = str1.count(k)
        if p > 1:
            pass
        else:
            print k
for j in str2:
    if j in str1:
        pass
    else:
        p = str1.count(j)
        if p > 1:
            pass
        else:
            print j
"""