n = 4
l1 = []
for i in range(1,11):
    l = []
    p = i
    for j in range(1,n + 1):
        p=p +i
        l.append(p)
    l1.append(l)

for m in l1:
    print m

def mul_table(x, y):
    for line in xrange(1, y+1):
        for table in xrange(1, x+1):
            print line * table, "\t",
        print
mul_table(10,10)