
import re
text = 'abbbabaaab'
pattern = 'ab'
print (re.findall(pattern,text))
for match in re.findall(pattern,text):
    print (match)










# start() is a method  and it will display  the index of pattern where pattern start in given text
# end() is a method  and it will display  the index of pattern where pattern end in given text