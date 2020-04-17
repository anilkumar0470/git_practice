num = input("enter a number to check prime number or not:")
for i in range(2,num):
    if num%i ==0:
        print "given number is not prime number"
        break
else:
    print "given number is prime number "
