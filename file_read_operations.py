fd = open("123.txt","r+")
#print fd.read(6)
#print "position",fd.tell()
p = fd.readlines()
i = 0
print "fd.readlines():",p

for line in p :

    fd.write(line)
    print "line ::::",i,line.upper()
    i += 1
    a = line

fd.close()