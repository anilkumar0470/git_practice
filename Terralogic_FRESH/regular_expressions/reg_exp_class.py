"""
import re
t ='abc abc abc abd'
p ='(\w+)\s*(\w+)\s*(\w+)\s*(\w+)'
p1 = re.search(p,t)
if p1:
    print p1.group()
"""

#p= re.search('(\d+/\d+/\d+)',t)
#print p
#A..Za..z0..9 it used when if contain any uppercase or lowercase or

import re
str1 = 'purple alice-b@google.com monkey dishwasher'
match = re.match(r'\w+\s*([\w.-]+)@([\w.]+)',str1)
#match = re.match('\w+\s([\w.-]+)@([\w.-]+)',str1)

if match :
    print match.group()
    print match.group(1)
    print match.group(2)


import re
t = 'hi THIS is anil'
p = '[[A-Z]+]'
p1 =re.search(p,t)
