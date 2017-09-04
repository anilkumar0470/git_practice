global l
l = [0,1]


def fib(x):
    return l.append(l[x-1]+l[x-2])
f = filter(fib,(x for x in range (2,20)))
print l