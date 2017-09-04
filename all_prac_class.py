"""
t = (1,2,3,4,2,5,2)
print type(t)
print t.count(2)
print "hai",t.index(2)
l = ['anil','kumar','sita','shanti',1,2,3,4]
print "length:",len(l)
print l[6]
l.append([1,2,3,4])
print l
print l[8][2]
l.extend((85,96,85))
print l
l.insert(0,4)
print l
l[0]='pathapati'
print l
l[10]=78
print l
print l.pop()
print l
print l.remove(78)
print l
print l.count(2)
print "this is output is belonging to strings only"
str = 'anilkumar pathapati naidu'
print str.count('a')
print str.count('p')
print str.find('p')
print str.index('n')
print str.find('w')
print str.index('u')
a = str.lower()
print a
b = str.upper()
print b
c = str.title()
print c
d = c.istitle()
print d
e = 'anilkumar'

print e.islower()
print e.isalpha()
print e.isalnum()
f = 'PATHAPATI'
print f.isupper()
print f.isalpha()
print f.isalnum()
print str
print str[1:7]
print range(10)
print str.startswith('anil')
print str.startswith('anilkumar p')
print str.startswith('nil')
print str.endswith('idu')
print str.endswith('naidu')
print str
#a = input("enter the string ")
#if 'a' in str :
   # print "searching word is found"
print str.capitalize()
print str.replace('anilkumar','aneelkumar')
print str
q = 'anilkumar is pathapati '
print q.lstrip()
print q.rstrip()
print q.strip()
print q.split('is')
print l
for i in l:
    for j in range(len(l)):
        print j,"==",i
print l[2]
print l.index('sita')
print "="*50
print "DICTIONARY"
d ={1:2,2:3,3:4,4:5,5:6,2:9}
print d
print d.items()
print d.keys()
print d.values()
print len(d)
for k,v in d.items():
    print k,"==",v
print d.has_key(2)
print d
d.update({2:20})
print d
d1 =d.copy()
print d1
d.pop(2)
print d
d.popitem()
print d
st = 'hello'
for i in st :

    if i == 'l':
        continue
        print "hai welcome to bvsrec"
    else:
        print i

print "generating prime numbers"
for num in range(2,20):
    for i in range (2,num):
        if num%i ==0:
            break
    else:
        print "num",num
print "welcome to india"
a=1
b=1
n=200
z = input('enter input upto where you want end:')

while a<n:
    c=2
    while c<a-1:
        if a%c==0:
            break
        c=c+1
    else:
        print "prime number:",a
    if b==z:
        print "b value is :",b
        break;
    else:
        a+=1
        b+=1
"""
print "now we are in  functions "
print "do practice well"

"""
def total(a,b):
    c = a+b
    return c
a = input('enter a value:')
b = input('enter b value:')
p=total(a,b)
print "total:",p
"""
def sum(a,b):
    c =a+b
    print c
sum(12,15)

def details(name,age):
    print "name:",name
    print "age:",age
details(age=30,name='pavan')
def detail(name,age):
    print "name",name
    print "age",age
detail('anil','23')