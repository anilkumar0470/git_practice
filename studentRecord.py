"""def marks(name,*marks):
    print "name",name
    print "type",type(marks)
    total = 0
    for i in marks :

        total = total + i
        if i >= 35:
            print "marks of the subject :",i

        else:
            print "you failed in one of subject :",i
            print "status:fail"
    print "total marks of anil is ",total

marks ("anil",98,35,75,76)
"""


def std_dict(name, *marks):
    print "="*20
    print"student details"
    print "="*20
    print "Name :", name
    f = True
    total = 0
    p=len(marks)
    for i in marks:
            total += i

            if i < 35:
                f = False
    if f :
        print "........!!!!!!Congratulations!!!!!!!......"
        result = "pass"
        print "Result:",result

    else :

        result = "fail"
        print "result:",result
        print "@@@Better luck next time@@@"
    print "marks you get :",total
    print "total marks conducted :",p * 100

std_dict("kumar.p",95,99,99,95)

