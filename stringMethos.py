a = raw_input("enter the string:")
"""
t = len(a)-1
print t
v = a[t]
print("string ends with:",v)
"""

f = a[0]
if a.isalpha():

        if a.islower():
                print("string is in lower case")
                b=a.upper()
                print("given string in upper case:",b)
                c=len(a.split())
                print("number of words:",c)
               #d=a.title()
                #print("In title form:",d)
                if a.istitle():
                        print("it is in title form")
                else :
                        print("it is  un title form")
                z = raw_input("enter string for checking starting position ")

                if a.startswith(z):
                        print("string start with given letter:",z)
                else:

                        print("string start with:",f)
                y = raw_input("enter a string for checking end position")

                if a.endswith(y):
                        print("string ends with given letter:",y)
                else:
                        t=len(a)-1
                        v=a[t]
                        print("string ends with:",v)

        elif a.isupper():
                print("input is in upper case")
                b=a.lower()
                print("given string in lower case",b)
                c=len(a.split())
                print("number of words:",c)
                d=a.title()
                print("In title form:",d)
                if d.istitle():
                        print("it is in title form")
elif a.isdigit():
        print("given number is :",a)
elif a.isalnum():
        print("it is combination of alpha and digits")
else:
        if a.islower():
                print("string is in lower case")
                b=a.upper()
                print("given string in upper case:",b)
                c=len(a.split())
                print("number of words:",c)
                #d=a.title()
                #print("In title form:",d)
                if a.istitle():
                        print("it is in title form")
                else :
                        print("it is  un title form")
                z = raw_input("enter string for checking starting position ")

                if a.startswith(z):
                        print("string start with given letter:",z)
                else:

                        print("string start with:",f)
                y = raw_input("enter a string for checking end position")

                if a.endswith(y):
                        print("string ends with given letter:",y)
                else:
                        t=len(a)-1
                        v=a[t]
                        print("string ends with:",v)

        elif a.isupper():

                print("input is in upper case")
                b = a.lower()
                print("given string in lower case",b)
                c=len(a.split())
                print("number of words:",c)
                #d=a.title()
                #print("In title form:",d)
                if a.istitle():
                        print("it is in title form")
                else:
                        print("it is untitle form")
                z = raw_input("enter string for checking starting position ")

                if a.startswith(z):
                        print("string start with given letter:",z)
                else:

                        print("string start with:",f)
                y = raw_input("enter a string for checking end position")

                if a.endswith(y):
                        print("string ends with given letter:",y)
                else:
                        t=len(a)-1
                        v=a[t]
                        print("string ends with:",v)
        else:
                print("hai")
                print("input is in combination of upper and lower & upper case")
                b = a.lower()
                print("input in lower case",b)
                u=a.upper()
                print("input in uppercase",u)
                c=len(a.split())
                print("number of words:",c)
                #d=a.title()
                #print("In title form:",d)
                if a.istitle():
                        print("it is in title form")
                else:
                        print("it is un title form")
                z = raw_input("enter string for checking starting position ")

                if a.startswith(z):
                        print("string start with given letter:",z)
                else:

                        print("string start with:",f)
                y = raw_input("enter a string for checking end position")

                if a.endswith(y):
                        print("string ends with given letter:",y)
                else:
                        t=len(a)-1
                        v=a[t]
                        print("string ends with:",v)
                k=raw_input("enter the word for counting the occurances")
                l=a.count(k)
                print("occurances of given word is ",k,l)
print("Bye Bye See You")