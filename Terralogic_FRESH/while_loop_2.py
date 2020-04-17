''' A neater interactive loop with an agreed upon sentinal value
to end the looping.'''

lines = []
print 'Enter lines of text.'
print 'Enter an empty line to quit.'

line = raw_input('Next line: ') # initialize before the loop
while line != '':
    lines.append(line)
    line = raw_input('Next line: ')  # !! reset value at end of loop!

print 'Your lines were:'
for line in lines:
    print line
