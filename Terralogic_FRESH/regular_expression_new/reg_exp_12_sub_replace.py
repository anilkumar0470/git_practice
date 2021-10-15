
#replacing the  pattern by using sub method
import re

"""
str1 = 'purple alice.b--abc@gmail.com, blah monkey bob@gmail.com blah dishwasher'
#re.sub(pattern,replacement,str)--returns new string with all replacements
# \1 is group(1) for before @and it will replace nothing
# \2 is group(2) for after @  and it will replace nothing if we specifiy
print re.sub(r'([\w\.\-]+)@([\w\.\-]+)',r'\1@yahoo.com',str1)

#assignment for replacing the pattern
#str = " dob: 10/03/2016    loc : btm joined: 12/03/2017"
#output ="dob :2016  loc :btm joined :2017"
"""
"""
"""
import re
str2 = 'purple alice.b--abc@gmail.com, blah monkey bob@gmail.com blah dishwasher'
print ("actual string is:",str2)
#  alice.b--abc@gmail.com \w+\.\w+\-\-\w+@\w+\.\w+
#  firstname.lastname@company.com \w+\.\w+@\w+\.\w+
#  firstname90_lastname.119ssdf_asdsfd@company.com  \w+\_\w+\.\d+@\w+\.\w+
# [\w\_\.]+
# print (re.sub('([\w\-\.\_]+)@([\w\.-]+)','Terralogic@paxterra',str2))
print (re.sub(r'([\w\.\_\-]+)@([\w\.\_\-]+)','\1@terralogic.com',str2))

print(r"hello \n dsfsdfd")