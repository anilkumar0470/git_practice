"""
import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
print ">>",re.finditer(pattern,text)
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print "found %s==%s at %d:%d" %(match.re.pattern,text[s:e],s,e)
#finditer() is a method available in re and it is used to find pattern till it matches
# and it will create iterative object by using for loop we can get the pattern
#and it will display the all the occurance of patterns
"""

import re
text = 'ip 10.20.123.45 up ip 12.123.456.789 down abbbababababbaba' \
       'ip 10.20.123.45 up ip 12.123.456.789 down abbbababababbaba'
pattern = '\d+.\d+.\d+.\d+'
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    #print "found %s==%s at %d:%d" %(match.re.pattern,text[s:e],s,e)
    print match.re.pattern,text[s:e],s,e
"""
import re
import sys
exit = raw_input ('enter input from the user do u want continue:')
if exit in ('yes' or 'no' or 'YES' or 'NO'):
    sys.exit()
"""


