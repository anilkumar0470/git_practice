a = 1
b = 1
n = 200
while a < n:
    c = 2
    while c <a-1:
        if a%c ==0:
            break
        c = c+1
    else:
        print "prime:",a
    if b==10:
        print ">>",b
        break
    else:
        b+=1
        a+=1
