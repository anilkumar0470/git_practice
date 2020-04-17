#This is an example for search method
import re
text = "123 this is anil kumar 123 "
pattern = "anil"
match = re.search(pattern,text)
print match
d = match.group()
print d



import re
text = "123 this is anil kumar 123"
pattern = r'.\d'
p1 = re.search(pattern,text)
print p1
d = p1.group()
print d



import re
t = "name : anil age : 20"
p = 'name :\s* (\w+)\s*age :\s*(\w+)'
p1 = re.search(p,t)
print p1
c = p1.groups();
print "this is for groups",c
print "this is for group",p1.group()
print "this is for group",p1.group(0)
print "this is for group(1)",p1.group(1)
print "this is for group(2)",p1.group(2)