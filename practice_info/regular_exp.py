import re
t = "abc anil"
p = "anil"
p1 = re.search(p,t)
d = p1.group()
print d
"""
import re
patterns = ["this","that"]
text = "does this text match the pattern?"

for pattern in patterns:
    print 'looking for "%s" in "%s"->' %(pattern,text),
    if re.search(pattern,text):
        print "found a match!"
    else :
        print "no match"
"""