
import re
str1 = 'purple alice-b@google.com monkey dishwasher'

match = re.search(r'([\w.-_]+)@([\w.]+)',str1)
if match:
    print (type(match.group()))
    print (match.group(1))
    print (match.group(2))

    print(match.group())
    print(match.groups())
"""

t ='abc abc abc abd'
p = '[\w\s]+'
p1=re.search(p,t)
print p1.group()

import re
t = 'hi THIS is anil'
p = '[A-Z]'
p1 =re.search(p,t)
"""
"""
import re
m = re.search('(?<=abc)def', 'abcdef')
ma = m.group(0)
print ma
pattern = r'(?<=@)\w+\.\w+'
match = re.search(r'(?<=-)\w+',"anil-pathapati")
text = 'anilkumar.0466@gmail.com'
match = re.search(pattern,text)
print match.group(0)
text = 'hi this is anil pathapati anil'
pattern = 'anil'
match = re.finditer(pattern,text)
for line in match:
    s = line.start()
    e = line.end()
    print "found %s == %s at %d : %d"%(line.re.pattern,text[s:e],s,e)
"""