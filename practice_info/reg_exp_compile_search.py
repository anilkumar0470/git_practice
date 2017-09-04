"""
import re
regexes = [re.compile(p) for p in ['this','that']]
text = 'does this text match the pattern'
print "list object :",regexes
for regex in regexes:
    print ">>",regex
    print "looking for %s in %s ->" % (regex.pattern,text)
    if regex.search(text):
        print "found a match"
    else:
        print "not found"
"""
import re
str1 = "name:anil kumar pathapati age: 22 dob: 12/07/1993"
r= re.compile('^name:([\w\s]+)\s*age\s*:\s*(\d+)\s*dob\s*:\s*(\d{1,2}\/\d{1,2}\/\d{2,4})$')
t = r.search(str1)
if t:
    print "pattern match"
    print "group :",t.group(0)
    print "name :",t.group(1)
    print "age :",t.group(2)
    print "dob :",t.group(3)
else:
    print "match not found"

#\/\ instead of this we can use /\