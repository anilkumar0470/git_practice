"""fd = open("abc.txt","w")
fd.write("python is great language. \nsay yes or no guys")
fd.close()

fd = open("abc.txt","r")
a = fd.read(10)
print "read string is: ",a
print "current position",fd.tell()
fd.seek(0,0)
print "current position",fd.tell()
fd.read(10)
print "read string is: ",a
fd.seek(0,1)
print "current position",fd.tell()
fd.read(10)
print "read string is: ",a

fd.close()
import os
os.rename("abc.txt","abcd.txt")

"""
with open("abcd.txt")as f:
    print f.closed
    for line in f:
        print line
print f.closed