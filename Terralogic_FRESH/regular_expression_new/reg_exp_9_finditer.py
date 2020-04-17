import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
print ">>",re.finditer(pattern,text)
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print "found %s==%s at %d:%d" %(match.re.pattern,text[s:e],s,e)
#finditer() is a method available in re and it is used to find pattern till it matches all the patterns
# and it will create iterative object by using for loop we can get the pattern
#and it will display the all the occurance of patterns
