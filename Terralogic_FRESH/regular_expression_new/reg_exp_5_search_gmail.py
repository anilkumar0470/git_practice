import re
str1 = 'purple alice-b@google.com monkey dishwasher'

match = re.search(r'([\w\.\-\_]+)@([\w\.]+)',str1)
if match:
    print match.group()
    print match.group(1)
    print match.group(2)
