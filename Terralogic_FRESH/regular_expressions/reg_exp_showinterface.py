import re
reg = re.compile(r'([\w\.\-\:\/]+\s*(up|down))\s*(up|down).*')


def reg_match_int(filename):
    out_dict={}
    fd = open(filename,'r')
    for line in fd.readlines():
        regmatch = reg.search(line)
        if regmatch:
            out_dict[regmatch.group(1)]=regmatch.group(2)

    return out_dict
p = reg_match_int('showinterface.txt')
print '='*50
print "interface details"
print '='*50
print "int details status"
print '='*50
for k,v in p.items():
    print '%s   %s'%(k,v)

print '='*50



