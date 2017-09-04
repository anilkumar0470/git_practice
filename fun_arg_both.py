def std_details(name,*marks,**details):
    p = "="
    total = 0
    for i in marks :
        total = total + i
    print p * 50
    print "student details"
    print p * 50
    #print "name:%s"%(name)
    #print "totalmarks:%d"%(total)
    print "name : %s total : %d"%(name,total)
    for k,v in details.items():
        print k,":",v
    print p * 50
std_details("shiva",96,51,85,66,age = 20,loc = "btm")