l = []
l1= []
l3= []
l4= []
l5= []
global total
def student_report():
    name = raw_input("enter the name of student")
    if l[0]==l2[0]== name:
        print "name:",l[0]
        print "roll number:",l[1]
        print "address:",l[2]
        print "class:",l[3]
        print "mobile number:",l[4]
        print "date of birth",l[5]
        print total

def student_search_result():
    name = raw_input("enter the name of student")
    if l[0]==l2[0]== name:
        print "name:",l[0]
        print "roll number:",l[1]
        print "address:",l[2]
        print "class:",l[3]
        print "mobile number:",l[4]
        print "date of birth",l[5]
    elif l[6] == l2[0]== name:
        print "name:",l[6]
        print "roll number:",l[7]
        print "address:",l[8]
        print "class:",l[9]
        print "mobile number:",l[10]
        print "date of birth",l[11]
    else:
        print "marks are not updated please choose 2 option to update marks"


def student_register():

    f=True
    while f:
        name = raw_input ("enter the name of student")
        regNo = raw_input ("entet the roll number")
        address = raw_input ("enter the address")
        section = raw_input ("enter the class")
        mobile = raw_input ("enter the mobile number")
        dob = raw_input ("enter the date of bitrh ")
        std_list.append({'name':name,'reg':regNo,'address':address,'section':section,'contact':mobile,'dob':dob})
        ent=raw_input("etnre if you wnat student or not if yes or no?")
        if ent in ['yes','y']:
            f=True
        else:
            f=False

def student_marks():
    name = raw_input ("enter the name of the student ")
    a1 = input("enter the marks of ")
    a2 = input("enter the marks of ")
    a3 = input("enter the marks of ")
    a4 = input("enter the marks of ")
    a5 = input("enter the marks of ")
    a6 = input("enter the marks of ")
    total = a1+a2+a3+a4+a5+a6

def student_report():
    p="="
    print p*50
    print "       Student report         "
    print p*50
    print "Name    Reg   Address Section   Contact DOB  "
    print p*50
    for i in std_list:
        print "%s   %s   %s     %s   %s    %s"%(i['name'],i['reg'],i['address'],i['section'],i['contact'],i['dob'])
    print p*50

def menu():
    global  std_list
    std_list=[]
    p = """
    1.stdent register
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
        opt = input("choose option which ever you want from above menu")
        if opt == 1:
            print "calling student register"
            student_register()
        elif opt == 2:
            print "calling student marks details"
            student_marks()
        elif opt == 3:
            print "calling search for student"
            student_search_result()
        elif opt == 4:
            print "calling student report"
            student_report()
        elif opt == 5:
            print "calling all student report"
        elif opt == 6:
            print "calling fee collection"
        elif opt == 7:
            print "have a nice day"
        else :
            print "enter proper output"
        ent = raw_input("if you want continue press yes/y or no/n")
        if ent in ("yes","y","YES","Y"):
            f = True
        else :
            f = False
menu ()

print " Bye Bye"
"""def student_search_result():
    name = raw_input("enter the name of student")
    if l[0]==l2[0]== name:
        print "name:",l[0]
        print "roll number:",l[1]
        print "address:",l[2]
        print "class:",l[3]
        print "mobile number:",l[4]
        print "date of birth",l[5]
    elif l[6] == l2[0]== name:
        print "name:",l[6]
        print "roll number:",l[7]
        print "address:",l[8]
        print "class:",l[9]
        print "mobile number:",l[10]
        print "date of birth",l[11]
    else:
        print "marks are not updated please choose 2 option to update marks"

"""
