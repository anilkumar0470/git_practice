import re
t = "abc anil"
p = "anil"
p = re.search(p,t)
text = 'anil pathapati'
p1 = re.match("kumar",text)
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