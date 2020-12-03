fd = open("nweee.txt","w")
c = True
while c == True :
    str1 = input("enter the string to write into file:")
    fd.write(str1)
    fd.write("\n")
    c = input("Do you want continue press yes otherwise no")
    if c in ("yes","y","YES","Y"):
        c = True
    else :
        break
fd.close()
print ("Write Done")