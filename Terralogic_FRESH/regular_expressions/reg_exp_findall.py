
"""import re
text = 'abbbabaaab'
pattern = 'ab'
print re.findall(pattern,text)
for match in re.findall(pattern,text):
    print 'found "%s"' % match
"""
import re
text = '12/07/1993  anil kumar  02/10/1971 pawan'
pattern = '\d+/\d+/\d+'
print re.findall(pattern,text)
for match in re.findall(pattern,text):
    print 'found "%s"' % match
    print "found ",match
# findall is a method to find the all the occurances of pattern in the given text
# start() is a method  and it will display  the index of pattern where pattern start in given text
# end() is a method  and it will display  the index of pattern where pattern end in given text
import re
fd = open("abcde.txt",'r')
line = fd.readlines()
for text in line :
   pattern = '^([0-9a-fA-F]{0,4}|0)(\:([0-9a-fA-F]{0,4}|0)){7}$'
   print re.findall(pattern,text)
   for match in re.findall(pattern,text):
        print 'found "%s"' % match