def std_details(name,*marks,**details):
    print "="*20
    print  "student details"
    print "="*20
    print "Name :",name
    total=0
    for i in marks:
        total+=i
    print "type",type(details)
    for k,v in details.items():
        print k,":",v
    print "Marks:",total
    print "="*20

std_details("Sita",45,56,78,age=23,loc="BTM")