"""
Example for while loop
Taking input dynamically from user with interactive session
"""
lines = []
print (type(lines))
testAnswer = input('Press y/yes if you want to enter more lines: ')
while testAnswer == 'y' or testAnswer.lower() == 'yes' :
    line = input('Next line: ')
    lines.append(line)
    testAnswer = input('Press y if you want to enter more lines: ')

print(lines)


range(100)