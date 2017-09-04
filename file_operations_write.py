fd=open("abc.txt","w")
c=True
while c == True:
    str1 = raw_input("enter the string to write")
    fd.write(str1)
    fd.write("\n")
    c=raw_input("enter do you want con press yes")
    if c.lower() in ["yes","y"]:
        c = True
    else:
        break
