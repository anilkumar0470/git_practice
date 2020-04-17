#This is an example for compile method
import re
str1 = "name:anil kumar pathapati age: 22 dob: 12/07/1993"
pattern= re.compile('^name:([\w\s]+)\s*age\s*:\s*(\d+)\s*dob\s*:\s*(\d{1,2}\/\d{1,2}\/\d{2,4})$')
t = pattern.search(str1)
if t:
    print "pattern match"
    print "group :",t.group(0)
    print "name :",t.group(1)
    print "age :",t.group(2)
    print "dob :",t.group(3)
else:
    print "match not found"
