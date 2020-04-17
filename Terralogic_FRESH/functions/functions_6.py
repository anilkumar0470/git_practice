#Tuple(*) as argument

def totalmarks(name,m1,m2,m3):
    total = m1 + m2 + m3
    print "name",name
    print "total marks",total

totalmarks("anil",78,77,70)


def something(name,*marks):
    print "name",name
    total = 0
    print type(marks)
    for i in marks:
        total = total + i
    print "total:",total
something("anil",70,45,65,45)
