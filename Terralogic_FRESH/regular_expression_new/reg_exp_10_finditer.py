import re
text = 'ip 10.20.123.45 up ip 12.123.456.789 down abbbababababbaba' \
       'ip 10.20.123.45 up ip 12.123.456.789 down abbbababababbaba'
pattern = '\d+.\d+.\d+.\d+'
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    #print "found %s==%s at %d:%d" %(match.re.pattern,text[s:e],s,e)
    print match.re.pattern,text[s:e],"starting index",s,"ending index",e
