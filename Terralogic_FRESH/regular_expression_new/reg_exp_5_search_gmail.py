import re
str1 = 'purple anil_p@google.com monkey dishwasher'
match = re.search('([\w\.\-\_]+)@([\w\.]+)',str1)

if match:
    print (match.group())
    print(match.group(0))
    print (match.group(1))
    print (match.group(2))
