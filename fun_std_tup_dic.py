def std_dict(name,*marks,**std_dict):
    print "="*20
    print  "student details"
    print "="*20
    print "Name :",name
    f = True
    total = 0
    for i in marks:
        total += i
        if i < 35 :
            f = False
    if f :
        print "........!!!!!!Congratulations!!!!!!!......"
        result = "pass"
        print "result:",result

    else :

        result = "fail"
        print "result:",result
        print "@@@Better luck next time@@@"
    print "total marks :",total
    for k,v in std_dict.items():
        print k,"-",v
std_dict("kumar.p",95,99,99,95,age = 22,loc = "chundi")

