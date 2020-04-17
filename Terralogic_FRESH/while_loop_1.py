"""
Example for while loop
Taking input dynamically from user with interactive session
"""
lines = []
print type(lines)
testAnswer = raw_input('Press y if you want to enter more lines: ')
while testAnswer == 'y':
    line = raw_input('Next line: ')
    lines.append(line)
    testAnswer = raw_input('Press y if you want to enter more lines: ')
#print lines
print 'Your lines were:'
for line in lines:
    print line


