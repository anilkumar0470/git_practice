def std_details_report(name,*marks,**details):
    fd = open('ccc.txt','w')
    total = 0
    for i in marks :
        total += i
    fd.write("________student________details" + '\n')
    fd.write("Name %s "%name)
    for k,v in details.items():
        fd.write("%s %s \n"%(k,str(v)))
    fd.write("total %s \n"%total)
    fd.close()
std_details_report("anil",99,99,98,99,98,99,age =22,location = 'btm')