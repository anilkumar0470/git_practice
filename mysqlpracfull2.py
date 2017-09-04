def student_register():
    f = True
    while f:
        first_name = raw_input ("enter the first name of student:")
        last_name = raw_input("enter last name of the student")
        rollnumber = input ("enter the roll number:")
        standard = raw_input ("enter the section:")
        dob = raw_input ("enter the date of bitrh :")
        mobile = raw_input ("enter the mobile number:")
        address = raw_input ("enter the address:")
        sqll = "insert into std_details2(first_name,last_name,rollnumber,standard,dob,mobile,address)\
        values('%s','%s','%d','%s','%s','%s','%s')"\
        %(first_name,last_name,rollnumber,standard,dob,mobile,address)
        cursor.execute(sqll)
        ent=raw_input("Press y/yes for to enter another student details n/no for main menu:")
        if ent in ['yes','y','YES','Y']:
            f=True
        else:
            f=False
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
    sql = """create table if not exists std_details5(
         first_name char(20) not null,
         last_name char(20),
         rollnumber int,
         standard char(10),
         dob char(10),
         mobile char(10),
         address char(20))"""
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
        else :
            print "choose right option"
            opt = input("choose option which ever you want from above menu:")


menu ()