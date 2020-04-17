#This is an example for fetching name and date of birth in a file
import re
fd = open("abc.txt","r")
line = fd.readlines()
for eachline in line :
#str = 'purple alice-12/12/2012 money dishwasher'
    match = re.search('^\s*(\w+)\s*(\w+)\s*(\w+)\s*(\d{1,2}/\d{1,2}/\d{4})$',eachline)
    if match :
        print match.group(1),match.group(4)
fd.close()
