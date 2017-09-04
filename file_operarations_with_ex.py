fd = open("abc.txt","r")
try:
    for i in range(100):
        l = fd.next()
        print "line is",i,":",l.upper()
except :
    pass

fd.close()
