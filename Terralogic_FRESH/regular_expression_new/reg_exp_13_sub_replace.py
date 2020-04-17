import re

str = "dob=12/7/1993 loc@btm joined:12/03/2016"
str = re.sub(r'([\w.]+):([\d/\d/\d-]+)',r'\1:2016',str)
print re.sub(r'([\w.]+)=([\d/\d/\d-]+)',r'\1=1993',str)
