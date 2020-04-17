"""
import re
t = "123 this is anil kumar 123"
p = r'.\d'
p1 = re.search(p,t)
print p1
d = p1.group()
print d


"""
"""
import re
t = "name : anil age : 20"
p = 'name :\s* (\w+)\s*age :\s*(\w+)'
p1 = re.search(p,t)
print p1
c = p1.groups();
print c

"""
"""
import re
str = "anil btm tcs 12/12/1996"
#str = 'purple alice-12/12/2012 money dishwasher'
match = re.search(r'(\w+) (\w+) (\w+) (\d+\/\d+\/\d+)',str)
if match :
    print match.group(1),match.group(4)
"""

import re
fd = open("abcde.txt","r")
line = fd.readlines()
for eachline in line :
#str = 'purple alice-12/12/2012 money dishwasher'
    match = re.search('^\s*(\w+)\s*(\w+)\s*(\w+)\s*(\d{1,2}/\d{1,2}/\d{4})$',eachline)
    if match :
        print match.group(1),match.group(4)
fd.close()


import re
p = '.*?'
t = '<H1>title</H1>'
m = re.search(p,t)
print m
print m.groups(1)


import re
p = '[A-Z]'
t = 'hi THIS his is anilkumar'
m = re.search(p,t)
print m
print m.group()
