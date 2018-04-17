l = []
def student_register():
    a = raw_input ("enter the name of student")
    b = raw_input ("entet the roll number")
    c = raw_input ("enter the address")
    d = raw_input ("enter the class")
    e = raw_input ("enter the mobile number")
    f = raw_input ("enter the date of bitrh ")
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    l.append(e)
    l.append(f)
student_register()
print (l)

l2 = []


def student_marks():
    name = input ("enter the name of the student ")
    a1 = input("enter the marks of ")
    a2 = input("enter the marks of ")
    a3 = input("enter the marks of ")
    a4 = input("enter the marks of ")
    a5 = input("enter the marks of ")
    a6 = input("enter the marks of ")
    l2.append(name)
    l2.append(a1)
    l2.append(a2)
    l2.append(a3)
    l2.append(a4)
    l2.append(a5)
    l2.append(a6)
student_marks()
print (l2)
print (l2[0])


def student_search_result():
    if l[0]==l2[0]:
        print "name:",l[0]
        print "roll number:",l[1]
        print "address:",l[2]
        print "class:",l[3]
        print "mobile number:",l[4]
        print "date of birth",l[5]
    else:
        print "marks are not updated please choose 2 option to update marks"


student_search_result()