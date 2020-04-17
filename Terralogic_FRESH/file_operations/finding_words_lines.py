def count_line_word(filename):
    wc = 0
    ac = 0
    dc = 0
    fd = open(filename,"r")
    f = fd.readlines()
    line = len(f)
    for l in f:
        templine = l.split()
        wc = wc + len(templine)
        for e in templine :
            if e.isdigit():
                dc += 1
            if e.isalpha():
                ac += 1
    fd.close()
    print "total lines:",line
    print "alpha count:",ac
    print "digit count:",dc
    print "word count:",wc
count_line_word("abcde.txt")