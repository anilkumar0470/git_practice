# https://www.programiz.com/python-programming/global-keyword
# Rules of global Keyword
# The basic rules for global keyword in Python are:
#
# When we create a variable inside a function, it is local by default.
# When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
# We use global keyword to read and write a global variable inside a function.
# Use of global keyword outside a function has no effect.

c = 1 # global variable

def add():
    print(c)
# add()

def add_two():
    c = c+2 # we can access global variable inside but we cannot modify the same
    print (c)

# add_two()
# print (c)


z = 100

def add_three():
    global z
    print("z value is {}".format(z))
    z = 50
    print ("z vlaue is {}".format(z))
add_three()
print ("z value is {}".format(z))