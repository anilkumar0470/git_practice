"""
#replacing the  pattern by using sub method
import re
str1 = 'purple alice.b--abc@gmail.com, blah monkey bob@gmail.com blah dishwasher'
#re.sub(pattern,replacement,str)--returns new string with all replacements
# \1 is group(1) for before @and it will replace nothing
# \2 is group(2) for after @  and it will replace nothing if we specifiy
print re.sub(r'([\w\.-]+)@([\w\.-]+)',r'\1@yahoo.com',str1)
"""
#assignment for replacing the pattern
#str = " dob: 10/03/2016    loc : btm joined: 12/03/2017"
#output ="dob :2016  loc :btm joined :2017"

"""
import re

str = "dob=12/7/1993 loc@btm joined:12/03/2016"
str = re.sub(r'([\w.]+):([\d/\d/\d-]+)',r'\1:2016',str)
print re.sub(r'([\w.]+)=([\d/\d/\d-]+)',r'\1=1993',str)
"""
import re
str2 = 'purple alice.b--abc@gmail.com, blah monkey bob@gmail.com blah dishwasher'
#print re.sub(r'([\w\-.]+)@([\w\.-]+)',r'\1@anil.com',str2)
print re.sub(r'([\w\.\_\-]+)@([\w\.\_\-]+)',r'\1@teralogic.com',str2)
print str2