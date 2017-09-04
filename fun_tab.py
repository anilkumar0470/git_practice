for a in range (1,11):
    #print a
    for i in range(1,11):
        #print a, "*", i,"=",(a * i)
        print (a * i),"\t",
    print "\n"
"""


def mul_table(x, y):
    for line in xrange(1, y+1):
        for table in xrange(1, x+1):
            print line * table, "\t",
        print "\n"
mul_table(10,10)
"""