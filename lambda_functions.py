f = lambda x,y : x+y

p =f(1,2)
print p
print "sum is ",[p]


f = lambda x : "%s length is %d "%(x,len(x))
[f(x) for x in ["rama","sita","raghu"]]
f