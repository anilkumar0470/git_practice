list1 = ["anil",123,"kumar",456]
print list1
list = list1.reverse()
print list
print "max(list1)",max(list1)
print "min(list1)",min(list1)
print list1.pop()
print "remove (kumar)",list1.remove("kumar")
print list1
print "remove(123)",list1.remove(123)
print list1
print "extend",list1.extend([1,2,3,4])
print list1
print list1.index(2)
print list1.index("anil")
list2 = ["zara",789]
print "max(list2)",max(list2)
print "min(list2)",min(list2)
print "cmp(list1,list2)",cmp(list1,list2)
print "cmp(list2,list1)",cmp(list2,list1)
list3 = list2 + [123]
print list3
print "max(list3)",max(list3)
print "min(list3)",min(list3)
print "cmp(list1,list3)",cmp(list1,list3)
print "cmp(list3,list1)",cmp(list3,list1)
print "cmp(list2,list3)",cmp(list2,list3)
print "cmp(list3,list2)",cmp(list3,list2)

l = []
l.append(1)
l.append([1,2,3])
print len(l)

print l
