a = input("enter a value:")
b = input("enter b value:")
for num in range(a,b):#10,11,12,13,14....19
    for i in range(2,num):#2,3,4,5,6,7,8,9
        if num % i == 0:
            break
    else:
        print "prime number is:",num