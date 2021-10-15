# 1233
# wewewe
# de3de
def count_line_word(filename):
    wc = 0
    ac = 0
    dc = 0
    fd = open(filename,"r")
    lines = fd.readlines() # [line1, line2, line3]
    line = len(lines)
    for l in lines:
        templine = l.split() # [word1, word2, word3]
        wc = wc + len(templine)
        for e in templine : # word1
            if e.isdigit():
                dc += 1
            if e.isalpha():
                ac += 1
    fd.close()
    print ("total lines:",line)
    print ("alpha count:",ac)
    print ("digit count:",dc)
    print ("word count:",wc)
count_line_word("abcde.txt")


def sample():
    # print("z value is ", z)
    z = 50
    print("z value is ", z)
# sample()
# print("z value is ",z)