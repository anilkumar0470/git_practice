"""
sql = "select * from employee where income >= %d " %(2000)
try:
    #excute the sql command
    print "==>",sql
    cursor.execute(sql)
    #fetch all the rows in alist of lists
    results = cursor.fetchall()
    print "===",results
    for row in results:
        print "---",row
        first_name = row[0]
        last_name = row[1]
        age = row[2]
        address = row[3]
        sex = row[4]
        income = row[5]
        # now print fetched result
        print "%s %s %d %s %s %f" % \
              (first_name,last_name,age,address,sex,income)
except :
    print "error : unable to fetch data"
#disconnect from server
db.close()
"""
def student_register():
    f = True
    while f:
        name = raw_input ("enter the name of student:")
        regNo = raw_input ("enter the roll number:")
        address = raw_input ("enter the address:")
        standard = raw_input ("enter the section:")
        mobile = raw_input ("enter the mobile number:")
        dob = raw_input ("enter the date of bitrh :")
        std_list.append({'name':name,'reg':regNo,'address':address,'section':standard,'contact':mobile,'dob':dob})
        ent=raw_input("Press y/yes for to enter another student details n/no for main menu:")
        if ent in ['yes','y','YES','Y']:
            f=True
        else:
            f=False
def student_search_result():
    name = raw_input("enter the student name:")
    for each_student in std_list: #[{name:shiva,reg:2},{name:anil,reg:1},{}]
        if each_student['name'] == name:
            p = "="
            print p*50
            print "       Student search result        "
            print p*50
            print "Name    Reg   Address Section   Contact DOB  "
            print p*50
            print "%s   %s   %s     %s   %s    %s"%(each_student['name'],each_student['reg'],each_student['address'],each_student['section'],each_student['contact'],each_student['dob'])
            print p*50
            print "name     total marks     sub1    sub2    sub3    sub4    sub5    sub6"
            print p*50
            """
            for j in std_marks :
                print "%s    %d     %d  %d  %d  %d   %d   %d"%(j["name"],j["total marks"],j["sub1"],j["sub2"],j["sub3"],j["sub4"],j["sub5"],j["sub6"])
            """
            for student in std_marks:
                if student['name'] == name:
                    print "%s    %d     %d  %d  %d  %d   %d   %d"%(student["name"],student["total marks"],student["sub1"],student["sub2"],student["sub3"],student["sub4"],student["sub5"],student["sub6"])


def student_register():
    f = True
    while f:
        name = raw_input ("enter the name of student:")
        regNo = raw_input ("enter the roll number:")
        address = raw_input ("enter the address:")
        section = raw_input ("enter the section:")
        mobile = raw_input ("enter the mobile number:")
        dob = raw_input ("enter the date of bitrh :")
        std_list.append({'name':name,'reg':regNo,'address':address,'section':section,'contact':mobile,'dob':dob})
        ent=raw_input("Press y/yes for to enter another student details n/no for main menu:")
        if ent in ['yes','y','YES','Y']:
            f=True
        else:
            f=False


def student_marks():
    name = raw_input ("enter the name of the student ")
    sub1 = input("enter the marks of sub1:")
    sub2 = input("enter the marks of sub2:")
    sub3 = input("enter the marks of sub3:")
    sub4 = input("enter the marks of sub4:")
    sub5 = input("enter the marks of sub5:")
    sub6 = input("enter the marks of sub6:")
    total = sub1+sub2+sub3+sub4+sub5+sub6
    if sub1<35:
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

    if g:
        print "........!!!!!!Congratulations!!!!!!!......"
        result = "pass"
        print "Result:",result
    else :
        result = "fail"
        print "result:",result
        print "@@@Better luck next time@@@"
    print "total marks :",total
    std_marks.append({"name":name,"total marks":total,"sub1":sub1,"sub2":sub2,"sub3":sub3,"sub4":sub4,"sub5":sub5,"sub6":sub6,"Result":result})
    ent=raw_input("enter if you want to continue  yes otherwise no:")
    if ent in ['yes','y','Y','YES']:
        student_marks()


def student_report():
    name = raw_input("enter the name of the student for report:")
    for each_student in std_list: #[{name:shiva,reg:2},{name:anil,reg:1},{}]
        if each_student['name'] == name:
            p="="
            print p*50
            print "       Student report         "
            print p*50
            print "Name    Reg   Address Section   Contact DOB  "
            print p*50
            print "%s   %s   %s     %s   %s    %s"%(each_student['name'],each_student['reg'],each_student['address'],each_student['section'],each_student['contact'],each_student['dob'])
            print p*50
            print "name     total marks     sub1    sub2    sub3    sub4    sub5    sub6"
            print p*50
            for student in std_marks:
                if student['name'] == name:
                    print "%s    %d     %d  %d  %d  %d   %d   %d"%(student["name"],student["total marks"],student["sub1"],student["sub2"],student["sub3"],student["sub4"],student["sub5"],student["sub6"])
            """for j in std_marks :
                print "%s    %d     %d  %d  %d  %d   %d   %d"%(j["name"],j["total marks"],j["sub1"],j["sub2"],j["sub3"],j["sub4"],j["sub5"],j["sub6"])
            """
            """for i in std_list:
                print "%s   %s   %s     %s   %s    %s"%(i['name'],i['reg'],i['address'],i['section'],i['contact'],i['dob'])
                print p*50
                print "name     total marks     sub1    sub2    sub3    sub4    sub5    sub6"
                print p*50
            for j in std_marks :
                print "%s    %d     %d  %d  %d  %d   %d   %d"%(j["name"],j["total marks"],j["sub1"],j["sub2"],j["sub3"],j["sub4"],j["sub5"],j["sub6"])
            """


def all_student_report():

            p="="
            print p*50
            print "       Student report         "
            print p*50
            #print "Name    Reg   Address Section   Contact DOB  "
            #print p*50
            #print "%s   %s   %s     %s   %s    %s"%(each_student['name'],each_student['reg'],each_student['address'],each_student['section'],each_student['contact'],each_student['dob'])
            print p*50
            #print "name     total marks     sub1    sub2    sub3    sub4    sub5    sub6"
            print p*50
            """for student in std_marks:
                if student['name'] == name:
                    print "%s    %d     %d  %d  %d  %d   %d   %d"%(student["name"],student["total marks"],student["sub1"],student["sub2"],student["sub3"],student["sub4"],student["sub5"],student["sub6"])
            """
            """for j in std_marks :
                print "%s    %d     %d  %d  %d  %d   %d   %d"%(j["name"],j["total marks"],j["sub1"],j["sub2"],j["sub3"],j["sub4"],j["sub5"],j["sub6"])
            """
            for i in std_list:
                print "%s   %s   %s     %s   %s    %s"%(i['name'],i['reg'],i['address'],i['section'],i['contact'],i['dob'])
                print p*50
                print p*50
                for student in std_marks:
                    if student == i:
                        print "name     total marks     sub1    sub2    sub3    sub4    sub5    sub6"
                        print "%s    %d     %d  %d  %d  %d   %d   %d"%(student["name"],student["total marks"],student["sub1"],student["sub2"],student["sub3"],student["sub4"],student["sub5"],student["sub6"])
            """for j in std_marks :
                print "name     total marks     sub1    sub2    sub3    sub4    sub5    sub6"
                print "%s    %d     %d  %d  %d  %d   %d   %d"%(j["name"],j["total marks"],j["sub1"],j["sub2"],j["sub3"],j["sub4"],j["sub5"],j["sub6"])
            """


def fee_details():
    p="="
    print p*50
    print "       Student Fee Details         "
    print p*50
    name = raw_input("enter the student name:")
    t=total = input("enter the total fee")
    print "total fee is:",total
    p=pay = input("enter how much do you want to pay")
    due = t - p
    print "Due fee is :",due
    std_Fee.append({'name':name,'total Fee':total,"pay":pay,"Remaining Fee":due})

def menu():

    global std_list
    std_list=[]
    global std_marks
    std_marks=[]
    global std_Fee
    std_Fee =[]
    global db
    global cursor
    import MySQLdb
    db = MySQLdb.connect("localhost","root","aneel","world")
    cursor = db.cursor()
    sql = """create table if not exists std_details2(
         first_name char(20) not null,
         last_name char(20),
         age int,
         address char(20),
         sex char(1),
         income float)"""
    cursor.execute(sql)


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
            student_search_result()
        elif opt == 4:
            print "@@@@student report@@@@"
            student_report()
        elif opt == 5:
            print "!@#$ALL Students Report%^&*"
            all_student_report()
        elif opt == 6:
            print "$$$$Fee Details$$$$"
            fee_details()
        elif opt == 7:
            print "Have a Nice Day"
        else :
            print "enter proper output"
        ent = raw_input("if you want Main Menu press yes/y or no/n:")
        if ent in ("yes","y","YES","Y"):
            f = True
        else :
            f = False
menu ()

print " Bye Bye Thank You Use Again"

