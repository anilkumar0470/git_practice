def outer_function():
    message = "hi"

    def inner_function():
        print("message is {}".format(message))
    inner_function()


outer_function()

# free variable even though the outer function execution completed successfully still
# we are able to access the  message variable in the inner_function.Those variables are
# called as free variables.

# A closure is inner function that remembers and has accesss to variables in the local
# scope in which it was created even though outer function is executed

def outer_function():
    message = "message"

    def inner_function():
        print("messagea", message)
    return inner_function

my_func = outer_function()
# print(my_func)
# print(my_func)
# print(my_func)

# In the above example we are returning the only function object only .
# when we add () to the function object it will execute.
# the above code will print only inner function objects
my_func()
# lets take a look on closure which is taking argument


def outer_function(msg):
    message = msg

    def inner_function():
        print("message with argument {}".format(message))
    return inner_function


my_func = outer_function("Hi")

# when we execute the above code .it will not print anything because we are returning
# only inner function object
# Now even though the outer function execution completed successfully still we are
# able to access those variables(called free variables) in inner function
my_func()

def outer_function(msg):
    message = msg

    def inner_function():
        print("closures with free variables {}".format(message))
    return inner_function

hi = outer_function("HI")
hello = outer_function("Hello")
hi()
hello()

#inner function taking multiple arguments

import logging
logging.basicConfig(filename="sample.txt", level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info("name of the function {} and args are {}".format(func.__name__,args))
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3,5)
sub_logger(10,5 )