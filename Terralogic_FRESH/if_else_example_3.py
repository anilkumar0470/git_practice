#To find bigger number
#This is an example for nested if
a = input("enter a value:")
b = input("enter b value:")
c = input("enter c value:")

if a < b:
    if b < c:
        print "c is bigger"
    else:
        print "b is bigger"
else:
    if a < c:
        print "c is bigger"
    else:
        print "a is bigger"
print "Thank you bye bye...|"
