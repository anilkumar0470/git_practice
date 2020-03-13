#first class functions
#it treat functions as first class citizenship
# is an entity wich supports all the general operations available for other entities.
# passed as argument
# return as argument
# assigning to variable

# assigning to variable

def square(x):
    print (x * x)

f = square
f(10)

# passed as argument we will implement similar to map

def check_given_number_is_even(num):
    if num%2 == 0 :
        return num
    else:
        return None

def my_map(func, args):
    even_list = []
    for i in args:
        return_value = func(i)
        if return_value:
            if i not  in even_list:
                even_list.append(i)
    print(even_list)

my_map(check_given_number_is_even, [2,4,6,5,7])

# return as argument



# free variable even though the outer function execution completed successfully still
# we are able to access the  message variable in the inner_function.Those variables are
# called as free variables.

# A closure is inner function that remembers and has accesss to variables in the local
# scope in which it was created even though outer function is executed

def outer_function() :

    message = "i am in outer function "
    def inner_function():
        print(message)
    return inner_function
return_function =  outer_function()
print(return_function)
return_function()

# example 2 for closure

def outer_func(msg):
    message = msg
    def inner_func():
        print(" {} to everyone ".format(message))
    return inner_func
hi_return =  outer_func("hi")
hi_return()
hello_return =  outer_func("hell0")
hello_return()


# decorator
# A decorator is a function that takes another function as argument and add some kind of
# functionality and returns another function i.e without modifying the source code we can
# still enhance the code

# why we want use decorators
# decorating our functions allows us to easily add functionality to our existing functions
# by adding that functionality inside the wrapper.

def decorator_function(original_function):
    print("decorator will be executed first ")
    def test_wrapper():
        print("test wrapper will be excuted second")
        return original_function()
    return test_wrapper

def actual_function():
    print("it will execute last ")

result = decorator_function(actual_function)
result()


def connect(original_function):
    print("decorator function here")
    print(original_function.__name__)

    def wrapper(*args , **kwargs):
        print("wrapper will be executed first ")
        return original_function(*args, **kwargs)
    return wrapper

@connect
def execute_command(command):
    print("command executed successfully!! {}".format(command))
execute_command("ls")
