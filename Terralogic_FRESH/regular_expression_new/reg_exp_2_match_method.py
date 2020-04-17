#This is an example for match method
#searching in starting of the line only

import re
text = "welcome to all"
pattern = "to"
match = re.match(pattern,text)
print match

#output is :None

import re
text = "welcome to all"
pattern = "wel"
result = re.match(pattern,text)
print result
print result.group()
