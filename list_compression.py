l = (x for x in range (1,10) if x%2==0)
print l
for i in l:
    print i


#square =[]
#for i in range(1,11):
   # if i ** 2%2 ==0:
       # square.append(i**2)
squares = [x **2  for x in range(1,11) if x %2 ==0]
print squares
