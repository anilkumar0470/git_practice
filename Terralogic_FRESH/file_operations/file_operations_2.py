fd = open("zzz.txt","r")
f= fd.read(10)
print f
for line in fd.readlines():
    print "line",line
fd.close()
