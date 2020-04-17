"""import re
patterns = ["this","does"]
text = "this does text match the pattern?"

for pattern in patterns:
    print 'looking for "%s" in "%s"->' %(pattern,text),
    if re.match(pattern,text):
        print "found a match!"
    else :
        print "no match"
"""

"""
import re
t = "name: shiva age: 20"
p = 'name:\s*(\w+)\s*age:\s*(\w+)'
p1 = re.search(p,t)
print p1
p1.groups()
"""
import re
str = 'purple alice-b@google.com money dishwasher'
match = re.search(r'\w+\s*\w+-\w+@\w+',str)
if match :
    print match.group()##'b@google'
