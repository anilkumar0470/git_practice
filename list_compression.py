# l = (x for x in range (1,10) if x%2==0)
# print l
# for i in l:
#     print i
#
#
# #square =[]
# #for i in range(1,11):
#    # if i ** 2%2 ==0:
#        # square.append(i**2)
# squares = [x **2  for x in range(1,11) if x %2 ==0]
# print squares

squares = [i**2 if i%2 == 0 else i*i*i for i in range(10)]
print(squares)

l = [11,22,11,33,22,11]
ki = [l.count(i) for i in l if l.count(i) > 1 ]
print(ki)