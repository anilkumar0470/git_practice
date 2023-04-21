# https://realpython.com/primer-on-python-decorators/
# sample decorator

def sample_decorator(original_func):
    def wrapper_function():
        print("something is happening before the function is called")
        original_func()
        print("something is happening after the function is called")
    return wrapper_function


def say_hi():
    print("say hai")


say_hi = sample_decorator(say_hi)
say_hi()

# typical way of defining decorator


def my_decorator(original_function):
    def wrap_func():
        print("something happening before executing original function")
        original_function()
        print("something is happening after execution of original function")
    return wrap_func


@my_decorator
def say_hello():
    print("wish you a happy night!")


say_hello()


# Decorating Functions With Arguments

def do_twice(orig_func):
    def wrap_inner_func(name):
        print("before original function")
        orig_func(name)
        print("after original func")
    return wrap_inner_func


@do_twice
def say_good(name):
    print("good morning {}".format(name))


say_good("anil")

# returning values from decorated function


def convert_to_upper_case(original_function):
    def wrap_func(string):
        print("this line will be executed first")
        result = original_function(string)
        return result.upper()
    return wrap_func


@convert_to_upper_case
def display(string):
    return string


print(display("good morning"))


# who are you really


def do_twice_new(original_fun):
    def wrapper_inner_func():
        print("before")
        original_fun()
        print("after")
    return wrapper_inner_func

@do_twice_new
def say_bye():
    print("bye bye")

print(say_bye)
print(say_bye.__name__)
