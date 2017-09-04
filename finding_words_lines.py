"""
fd = open("abc.txt","r")
f = fd.readlines()
print f
for line in f :
    c = 0
    print line.split()
    c =len(line.split())
    d = c +c
    print d
"""
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
count_line_word("abc.txt")