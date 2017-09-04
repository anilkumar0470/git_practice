n = input ("enter a value")
l = []
l2 = []
k = l
for i in range (1,n+1):
    for j in range (1,11):
        k = i *j
        l.append(k)
while len(l)>10:
        p = l[:10]
        l2.append(p)
        l = l[10:]
l2.append(l)
for m in range (len(l2)):
    print l2[m]