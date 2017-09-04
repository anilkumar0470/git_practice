d = {'name':"anilkumar",'age':21,"class":"B.Tech 3 rd year","address":"chundi","mobile number":8123210095}
for i in d.keys():
    print "key:",i
for i in d.values():
    print "values:",i
for i in d.items():
    print "items",i
print d.has_key('name')
d.update({"hobby":"chess","88":88})

for k,v in d.iteritems():
    print k,v
