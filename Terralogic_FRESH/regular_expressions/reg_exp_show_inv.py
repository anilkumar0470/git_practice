import re
reg = re.compile('^\s*PID\s*:\s*([\w\-\/]+)\s*.*SN:\s*(\w+)')


def get_pid(filename):
    out_dict={}
    pid = 1
    fd = open(filename,'r')
    for line in fd.readlines():
        regmatch = reg.search(line)
        if regmatch:
            out_dict['pid'+str(pid)]=regmatch.group(1),regmatch.group(2)
            pid = pid + 1
    return out_dict
p =get_pid('showinventory.txt')
print '='*50
print "pid details"
print '='*50
print 'pid pid disc version'
print '='*50
for k,v in p.items():
    print '%s %s %s'%(k,v[0],v[1])
print '='*50
