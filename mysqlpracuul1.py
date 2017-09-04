def student_register():
    import MySQLdb
    db = MySQLdb.connect("127.0.0.1","root","aneel","student")
    cursor = db.cursor();
    sqla = """create table if not exists employee17(
         first_name char(20) not null,
         last_name char(20),
         rollnumber int,
         standard int,
         dob char(10),
         mobile int,
         address char(20))"""
    cursor.execute(sqla)
    f = True
    while f:
        first_name = raw_input("enter first name ")
        last_name = raw_input("enter last name")
        rollnumber = input("enter roll number")
        standard = input("enter the standard of the student")
        dob = raw_input("enter date of birth")
        mobile = input("enter mobile number")
        address = raw_input("enter address")
        sql= "insert into employee16(first_name,last_name,rollnumber,standard,dob,mobile,address)\
        values( '%s','%s','%d','%d','%s','%d','%s')"\
        %(first_name,last_name,rollnumber,standard,dob,mobile,address)
        cursor.execute(sql)
        db.commit()
        ent=raw_input("Press y/yes for to enter another student details n/no for main menu:")
        if ent in ['yes','y','YES','Y']:
            f=True
        else:
            f=False
    db.close()


def student_marks():
    g = True
    sql = """create table if not exists std_marks100(
    rollnumber int,
    telugu int,
    hindi int,
    english int,
    maths int,
    science int,
    social int,
    total int,
    percentage float,
    status char(10))"""
    import MySQLdb
    db = MySQLdb.connect("localhost","root","aneel","student")
    cursor =db.cursor()
    cursor.execute(sql)
    rollnumber = input("enter the roll number of the student ")
    telugu = input("enter the marks of telugu:")
    hindi = input("enter the marks of hindhi:")
    english = input("enter the marks of english:")
    maths = input("enter the marks of maths:")
    science = input("enter the marks of science:")
    social = input("enter the marks of social:")
    list1 =[telugu,english,hindi,maths,science,social]
    for i in list1:
        if i >= 35:
            pass
        else:
            g = False
    total = telugu+english+maths+hindi+science+social

    """if sub1<35:
        g = False
    elif sub2<35:
         g = False
    elif sub3<35:
        g = False
    elif sub4<35:
        g = False
    elif sub5<35:
        g = False
    elif sub6<35:
        g = False
        """

    if g:
        print "........!!!!!!Congratulations!!!!!!!......"
        status = "pass"
        print status

    else :
        status = "fail"
        print "result:",status
        print "@@@Better luck next time@@@"
    print "total marks :",total
    percentage = total/6
    print "hai",percentage
    print "status",status

    #sql= "insert into employee16(first_name,last_name,rollnumber,standard,dob,mobile,address)\
     #   values( '%s','%s','%d','%d','%s','%d','%s')"\
      #  %(first_name,last_name,rollnumber,standard,dob,mobile,address)
    sql2 = "insert into std_marks100(rollnumber,telugu,hindi,english,maths,science,social,total,percentage,status)\
    values('%d','%d','%d','%d','%d','%d','%d','%d','%f','%s')"\
    % (rollnumber,telugu,hindi,english,maths,science,social,total,percentage,status)
    print "hello"
    #std_marks.append({"name":name,"total marks":total,"sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4,"sub5":sub5,"sub6":sub6,"Result":result})
    cursor.execute(sql2)
    db.commit()
    ent=raw_input("enter if you want to continue  yes otherwise no:")
    if ent in ['yes','y','Y','YES']:
        student_marks()


def menu():

    global std_list
    std_list=[]
    global std_marks
    std_marks=[]
    global std_Fee
    std_Fee =[]
    global db
    global cursor


    p = """
    1.student register
    2.student marks details
    3.search for student
    4.student report
    5.all student report
    6.fee collection
    7.exit
    """
    f = True
    while f:
        print p
        opt = input("choose option which ever you want from above menu:")
        if opt == 1:
            print "===student register==="
            student_register()
        elif opt == 2:
            print "****student marks details****"
            student_marks()
        elif opt == 3:
            print "!!!!search for student!!!!"
            student_register()
        elif opt == 4:
            print "@@@@student report@@@@"
            student_register()
        elif opt == 5:
            print "!@#$ALL Students Report%^&*"
            student_register()
        elif opt == 6:
            print "$$$$Fee Details$$$$"
            student_register()
        elif opt == 7:
            print "Have a Nice Day"
            f = False
        else :
            print "enter proper output"
        #ent = raw_input("if you want Main Menu press yes/y or no/n:")
        #if ent in ("yes","y","YES","Y"):
            f = True
        #else :
            f = False
menu ()
