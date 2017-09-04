#n=input("enter value")
#if n==1:
        #print("n is 1")
#elif n==2:
        #print ("n is 2")
#elif n==3:
        #print ("n is 3")
#else:
        #print ("a is not in the range")
#print("hi this is practice for elseis")
"""
a=input("enter a value")
if a<=10:
        print("a value is below 10")
elif a>=10 & a<=20:
        print("a value is above 10 and below 20")
else:
        print("a is out of range")
"""

#a=input("enter a value")
#b=input("enter b value")
#c=input("enter c value")
#if a<b :
        #if b<c :
                #print ("c is bigger")
        #else:
                #print ("b is bigger")
#else:
        #if a<c:
                #print ("c is bigger")
        #else :
                #print ("a is bigger")


"""for line in range(1,11):
    for table in range(1,11):
        print line * table, '\t',
    print
"""
global std_list
std_list = []


def student_register():

    f = True
    while f:
        name = raw_input ("enter the name of student:")
        regNo = raw_input ("enter the roll number:")
        address = raw_input ("enter the address:")
        section = raw_input ("enter the class:")
        mobile = raw_input ("enter the mobile number:")
        dob = raw_input ("enter the date of bitrh :")
        fd = open("std_details.txt","w")
        p = "="
        z = p *50
        fd.write(z)
        fd.write("\n")
        fd.write("        student details      ")
        fd.write("\n")
        print p
        fd.write("\n")
        fd.write(z)

        fd.write("\n")
        fd.write("\t")
        #fd.write("SNO \t")
        fd.write("Name \t \t")
        fd.write("Location \t \t")
        fd.write("Mobile \t \t")
        fd.write("DOB \t \t")
        fd.write("\n")

        fd.write(name)
        fd.write("\t\t")
        fd.write(address)
        fd.write("\t\t")
        fd.write(mobile)
        fd.write("\t\t")
        fd.write(dob)
        fd.write("\t\t")
        std_list.append({'name':name,'reg':regNo,'address':address,'section':section,'contact':mobile,'dob':dob})
        fd.writelines(std_list)
        ent=raw_input("enter if you want student or not if yes or no?")
        if ent in ['yes','y']:
            f=True
        else:
            f=False

student_register()