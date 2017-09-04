
def fun(a,b):
    if a>b :
        return a
    else :
        return b
l =[1,4,10,45,98]
r = reduce (fun,l)
print r

f = lambda x,y:x*y
p = reduce(f,[x for x in range (1,6)])
print p


def fun(x,y):
        return  x*y

r = reduce(fun ,[x for x in range(1,6)])
print r

f = lambda a,b:a + b
