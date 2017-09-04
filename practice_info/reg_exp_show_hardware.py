import re
reg = re.compile(r'\s*ROM\s*:\s*[\w\s]+\s*,\s*Version\s*([\d\.\(\)\w]+).*')
reg_up = re.compile(r'\s*Router\s*uptime\s*is\s*(\d{1,2}\s*day)\s*,\s*(\d+\s*hours)\s*,\s*(\d+\s*minutes)')


def get_hardware(filename):
    out_dict = {}
    pid = 1
    fd = open(filename,'r')
    for line in fd.readlines():
        regmatch=reg.search(line)
        regmatch2 = reg_up.search(line)
        if regmatch:
            out_dict['version']=regmatch.group(1)
        if regmatch2:
            uptime = regmatch2.group(1)+regmatch2.group(2)+regmatch2.group(3)
            out_dict['up time'] =uptime
    return out_dict
p = get_hardware('showhardware.txt')
print '='*50
print "interface details"
print '='*50
print "int details status"
print '='*50
for k,v in p.items():
    print '%s   %s'%(k,v)

print '='*50
#re.split() is like split but caan use patters
#re.split("\w+"'this is a test,short and sweet, of split().')
['this','is','a','test','short','and','sweet','of','split','']


