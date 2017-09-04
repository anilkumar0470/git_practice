import re
reg = re.compile(r'\s*HWIDB\#\d\s*\d\s*\d\s*(.*\,)\s*HW')




def reg_match_int(filename):
    out_dict={}
    pid = 1
    fd = open(filename,'r')
    for line in fd.readlines():
        regmatch=reg.search(line)
        if regmatch:
            out_dict['version']=regmatch.group(1)
            pid=pid+1

    return out_dict
p = reg_match_int('showid.txt')
print '='*50
print "interface details"
print '='*50
print "int details status"
print '='*50
for k,v in p.items():
    print '%s   %s'%(k,v)

print '='*50