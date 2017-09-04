"""fd = open("abc.txt","w")
c = True
while c == True :
    str1 = raw_input("enter the string to write into file")
    fd.write(str1)
    fd.write("\n")
    c = raw_input("Do you want continue press yes otherwise no")
    if c in ("yes","y","YES","Y"):
        c = True
    else :
        break
fd.close()
print "Write Done"
"""
"""
fd = open("abc.txt","r")
f= fd.read(10)
print f
for line in fd.readlines():
    print "line",line
fd.close()
"""
fd = open("abc.txt","r")
print "name of file :",fd.name
print "file closed or not",fd.closed
print "access mode of file ",fd.mode