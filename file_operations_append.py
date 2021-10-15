def append_file(filename):
    fd = open(filename,"a")
    print "current position :",fd.tell()
    temp = ""
    while True:
        en = raw_input("enter something")
        if "$" in en:
            break
        else:
            temp+= en

    fd.write(temp+"\n")
    print "After write ----",fd.tell()
    fd.close()
append_file("abc11.txt")
# __enter__
# __exit___