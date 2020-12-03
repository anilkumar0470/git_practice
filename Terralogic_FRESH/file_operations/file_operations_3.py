fd = open("C:\Users\apathapa\test\test-automation\GUI-Automation\abc.txt","r")
print "name of file :",fd.name
print "file closed or not",fd.closed
print "access mode of file ",fd.mode
if fd.closed:
    print "something"
    fd.close()