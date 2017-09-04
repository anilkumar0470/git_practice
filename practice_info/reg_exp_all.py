import re
str1 = 'purple alice-b@google.com monkey dishwasher'

match = re.match(r'\w+\s*([\w.-]+)@([\w.]+)',str1)
if match:
    print match.group()
    print match.group(1)
    print match.group(2)

t ='abc abc abc abd'
p = '[\w\s]+'
p1=re.search(p,t)
print p1.group()

import re
t = 'hi THIS is anil'
p = '[(A.Z)]'
p1 =re.search(p,t)
