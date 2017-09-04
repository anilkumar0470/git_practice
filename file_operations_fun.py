def read_file(filename):
    fd = open("abc.txt","r")
    print fd.read(6)
    print "position",fd.tell()
    p = fd.readlines()
    #print "fd.readlines():",p
    for line in p :
        print "line ::::",line.upper()
    fd.close()


def append_file(filename):
    fd=open("filename","a")
    print fd.tell()
    fd.write("hello anil")
    print fd.tell()
    fd.close()
append_file("abc1.txt")

#read_file("abc.txt")