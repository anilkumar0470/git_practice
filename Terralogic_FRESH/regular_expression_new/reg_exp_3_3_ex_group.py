import re

str = "anil btm terralogic 12/12/1996"


match = re.search('(\w+) (\w+) (\w+) (\d+\/\d+\/\d+)',str)
if match :
    print (match.group(1),match.group(4))
    print(match.groups())

    # print("groups" ,match.groups())
