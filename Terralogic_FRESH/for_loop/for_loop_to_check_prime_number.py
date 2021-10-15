num = 5


for i in range(2,num): # 2,3,4,5,6
    if num%i == 0: # 7%2 = 1
        print("given number is not prime number")
        break
else:
    print ("given number is prime number ")



