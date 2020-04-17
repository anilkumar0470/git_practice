a=10
n=200
b=1
while a< n:
	c=2
	while c<a-1:
		if a%c==0:
			break
		c=c+1
	else:
	    print "Prime number:",a

	if b==20:
		#print ">>",b
		break
	else:
	    b+=1
	a=a+1#a+=1