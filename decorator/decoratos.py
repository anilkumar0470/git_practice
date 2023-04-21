# from functools import wraps
# # A decorator is a function that takes another function as argument and add some kind of
# # functionality and returns another function i.e without modifying the source code we can
# # still enhance the code
#
# # why we want use decorators
# # decorating our functions allows us to easily add functionality to our existing functions
# # by adding that functionality inside the wrapper.
#
# def decorator_function(original_function):
#     def wrapper():
#         print("wrapper execute before {} ".format(original_function.__name__))
#         return original_function()
#     return wrapper
#
#
# def display():
#     print("display function")
#
# d = decorator_function(display)# block2
# d()#  block2
#
# # instead of writing like block 2 we will @decorator_name both will same functionality
#
#
# def new_decorate_function(original_function):
#     def wrapper_func():
#         print("Wrapper will say hi first {}".format(original_function.__name__))
#         original_function()
#     return wrapper_func
#
# @new_decorate_function
# def sample_hi():
#     print(" I am saying hi second ")
# sample_hi()
# my_func = new_decorate_function(sample_hi)
# my_func()

# def decorate_function(original_fun):
#     def wrapper_function(*args, **kwargs):
#         print("wrapper will be executed before {}".format(original_fun.__name__))
#         original_fun(*args, **kwargs)
#     return wrapper_function
#
# @decorate_function
# def new_display():
#     print("i am in display function")
# new_display()
# # result = decorate_function(new_display)
# # result()
#
# @decorate_function
# def display_info(name, loc):
#     print("name is {} and loc is {}".format(name, loc))
#
# display_info("anil", "bang")

# def decorator_fun(original_func):
#     def test_wrapper():
#         print("test wrapper is executing before {}".format(original_func.__name__))
#         return original_func()
#     return test_wrapper
# @decorator_fun
# def display_func():
#     print("display function")
#
# display_func()

# def dec_func(org_fun):
#     def wrapper_function():
#         print("i am inside wrapper")
#         return org_fun()
#     return wrapper_function
#
# def display_func():
#
#
#
#
#
# #
# #
# # # when we are passing arguments along with original function
# # @decorator_fun
# # def display_details(name, age):
# #     print("name {} and age {}".format(name, age))
# # #display_details("anil", 23)
# #
# # # when we run above code it will throw error (TypeError: test_wrapper() takes
# # # no arguments (2 given)) because the flow will go like this
# # # at the end it will return test_wrapper object for that object u r trying to pass
# # # two values but test wrapper is not at all accepting arguments
# #
# # # to overcome this error we need to add *args, **kwargs for test wrapper and original
# # # function so that we can handle any number of arguments.
# #
# #
# # def dec_func(org_fun):
# #     def wrapper_fun(*args, **kwargs):
# #         print("wrapper fun is executing before {}".format(org_fun.__name__))
# #         return org_fun(*args, **kwargs)
# #     return wrapper_fun
# #
# # def display_info(name, age):
# #     print("name {}: age {}:".format(name, age))
# #
# # display_info("anil", 25)
# #
# # # class as decorator
# # # In class decorator we will declare the original function inside the init and
# # # simillar to wrapper function we will have __call_ method.
# #
# #
# # class decorator_class(object):
# #
# #     def __init__(self, original_function):
# #         self.original_function = original_function
# #
# #
# #     def __call__(self, *args, **kwargs):
# #         print("__call__ is executing before {}".format(self.original_function.__name__))
# #         return self.original_function(*args, **kwargs)
# #
# # @decorator_class
# # def display():
# #     print("I am in caaalass")
# # display()
# #
# #
# # # practical examples of decorator
# # # to calculate how many times u used function
# #
# # def logger_function(original_function):
# #     import logging
# #     logging.basicConfig(filename="sample.log", level=logging.INFO)
# #     @wraps(original_function)
# #
# #     def wrapper_function(*args, **kwargs):
# #         logging.info("Executing wrapper function before {} with args {} and kwargs {} ".
# #               format(original_function.__name__, *args, **kwargs))
# #         original_function(*args, **kwargs)
# #     return wrapper_function
# #
# # @logger_function
# # def display_howmany_times(name, age):
# #     print("display how many times executed successfully with name {} age {}".format(name, age))
# #
# # display_howmany_times("Anil", 24)
# #
# # # another one how much time to taken to execute function
# #
# #
# # def timer(org_func):
# #     import time
# #     @wraps(org_func)
# #
# #     def wrapper(*args, **kwargs):
# #         start_time = time.time()
# #         result =org_func(*args, **kwargs)
# #         time_taken = time.time()-start_time
# #         print("time taken for the function {} execution is {}".format(org_func.__name__,time_taken))
# #         return result
# #     return wrapper
# #
# # @timer
# # def display_info_with_time(name, age,sleep_time):
# #     import time
# #     time.sleep(sleep_time)
# #     print("success")
# #
# # display_info_with_time("anil",25, 1)
# #
# # #lets try to apply two decorators on one function
# #
# # @logger_function
# # @timer
# # def display_info_with_time(name, age,sleep_time):
# #     import time
# #     time.sleep(sleep_time)
# #     print("success")
# #
# # display_info_with_time("anil",25, 1)
# # # when we are executing two decorators in a row we called as stack .In stack the order
# # # will always from top to bottom and this is how it will execute
# # #d = logger_function(timer(display_info_with_time))
# # # the python will try to execute in the above order when we complete first decorator
# # # always it returns the wrapper object and we are passing this wrapper object to new
# # # decorator as argument instead of original function so we are not getting expected output
# # # to over come this we need to add @wrap to the all the wrapper functions with original functions
# #
# #
# #
# # def sample_function(arg_function):
# #     def wrapper_function():
# #         print("i am in wrapperrrrr function")
# #         return arg_function()
# #     return wrapper_function
# #
# # @sample_function
# # def display():
# #     print("Welcome to india")
# #
# # display()
# #
# #
# # def sam(a):
# #     if a  == 0:
# #         return 0
# #     elif a == 1:
# #         return 1
# #     else:
# #         print("dfdsfd")
# #         return sam(a-2) #  + sam(a-1)
# # print(sam(4))
#
# # import psutil
# # for proc in psutil.process_iter():
# #     print(proc.name())
# #     print(proc._pid)
# import subprocess
# import re
# import os
# import signal
#
#
#
# # result = subprocess.run(['netstat', '-aon'], stdout=subprocess.PIPE)
# # print(result.stdout)
# # pattern = '\d.\d.\d.\d:("port_number")\s*\d\.\d\.\d\.\d:\d+\s*LISTENING\s*(\d+)'
# # match = re.search(pattern, result.stdout.decode("utf-8"))
# # if match:
# #     print(match.group(1), match.group(2))
# #     os.kill(match.group(2), signal.SIGTERM)
#
#
# # def decorate_function100(original_function):
# #     def wrapper():
# #         print("wrapper first")
# #         return original_function()
# #     return wrapper
# #
# # @decorate_function100
# # def disp(a,b):
# #     print("second")
# # disp(10,20)
#
#
#
# # def my_decorator(func):
# #
# #
# #     def wrapper():
# #         print("i am inside wrapper function")
# #         func()
# #
# #     return wrapper
# #
# # def say_hello():
# #
# #     print("hello")
# #
# #
# # say_hello  = my_decorator(say_hello)
# # say_hello()
#
#
# # def my_decorator(func):
# #     def wrapper():
# #         print("I am in wrapper")
# #         func()
# #     return wrapper
# #
# # @my_decorator
# # def say_hi():
# #     print("hii")
# # say_hi()
#
#
# # def my_decorator(original_func):
# #
# #     def test_wrapper():
# #         print("test wrapper")
# #         original_func()
# #     return test_wrapper
# #
# # @my_decorator
# # def display():
# #     print("display")
# # display()
#
# # def new_decorator(actual_function):
# #
# #     def wrapper_do_twice(*args, **kwargs):
# #         print("i am in wrapper")
# #         actual_function(*args, **kwargs)
# #         actual_function(*args, **kwargs)
# #     return wrapper_do_twice
#
#
#
#
# # assigning to some variable
# def addition(num):
#     return num + 1
#
# add_one = addition
# print(add_one(1))
#
# # defining the functions inside functions
# def outer_function(num):
#     def inner_function(num):
#         result = num + 1
#         return result
#     return inner_function(num)
# print(outer_function(3))
#
# # passing functions as arguments to other function
#
# def addition_new(num):
#     return num + 1
#
# def function_call(function):
#     num = 5
#     return function(num)
#
# print(function_call(addition_new))
#
# # functions returning other functions
#
# def hello():
#     def say_hi():
#         return "hi"
#     return say_hi
#
# result = hello()
# print(result())
#
#
# def outer_function(message):
#
#     def inner_function():
#         print(message)
#     return inner_function()
#
# outer_function("some random message")
#
#
# # sample decorator
#
# def sample_decorator(original_function):
#     def wrapper_function():
#         output = original_function()
#         upper_case = output.upper()
#         return upper_case
#
#     return wrapper_function
#
#
# # def display():
# #     return "hi good evening"
# # dec = sample_decorator(display)
# # print(dec())
#
# @sample_decorator
# def display():
#     return "hello"
# print(display())
#
# # another decorator with returning upper case of given string
# print("="*50)
# def test_decorator(original_function):
#     def wrapper_funct():
#         output = original_function()
#         upper_case = output.upper()
#         return upper_case
#     return wrapper_funct
#
#
# def splitted_string(new_func):
#     def wrapper_fun():
#         res = new_func()
#         return res.split()
#     return wrapper_fun
#
#
# @splitted_string
# @test_decorator
# def string_func():
#     return "hi hello good evening"
# print(string_func())
#
# # another example for retuning upper case
#
#
# def uppercase_decorator(original_func):
#     def wrapper_func():
#         res = original_func()
#         print("rererere")
#         return res.upper()
#     return wrapper_func
#
# def splitting_string(original_func):
#     def wrapper_func():
#         out = original_func()
#         print("666666")
#         return out.split()
#     return wrapper_func
#
# @splitting_string
# @uppercase_decorator
# def return_string():
#     return "hi good evening testing "
#
# print(return_string())
#
# # passing variables for the decorator
#
#
# # def sample_decorator(ori_fun):
# #     def wrapper_func(arg1, arg2):
# #         print("my arguments are {} {} ".format(arg1, arg2))
# #         ori_fun(arg1, arg2)
# #     return wrapper_func
# #
# # @sample_decorator
# # def my_cites(city1, city2):
# #     print("cities are {} {}".format(city1, city2))
# #
# # my_cites("Bangalore", "hyderabad")
#
# decorator as class
# class decorator_class:
#
#     def __init__(self, original_function):
#         print("i am init")
#         self.original_function = original_function
#
#
#     def __call__(self, *args, **kwargs):
#         print("call method will be executed first")
#         return self.original_function(*args, **kwargs)
# @decorator_class
# def display_something():
#     print("i am something")
#
# display_something()
#
# # realtime example
# from functools import wraps
# def my_timer(org_func):
#     @wraps(org_func)
#     def wrapp_fun(*args, **kwargs):
#         import time
#         start_time = time.time()
#         org_func(*args, **kwargs)
#         time_taken =time.time() -start_time
#         print("time taken for {} to complet is {}".format(org_func.__name__,time_taken))
#     return wrapp_fun
#
#
# def my_logger(original_function):
#     print("something")
#     import logging
#     logging.basicConfig(filename="{}.log".format(original_function.__name__), level=logging.INFO)
#     @wraps(original_function)
#     def wrapper_function(*args, **kwargs):
#         logging.info("{} Ran with with args : {} and kwargs {}".format(original_function.__name__,args, kwargs))
#         original_function(*args, **kwargs)
#     return wrapper_function
# @my_logger
# @my_timer
#
# def display_info_new(name, loc):
#     import time
#     time.sleep(1)
#     print("args are name {} loc {}".format(name, loc))
# display_info_new("anil", "chennai")
#
#
#
#
# def sample_decorator_new(original_func):
#     def wrapper_func():
#         result = original_func()
#         return result.title()
#     return wrapper_func
#
# @sample_decorator_new
# def display_first():
#     return "good morning"
#
# print(display_first())
#
# def decorator_function(original_function):
#     def wrapper_function():
#         print("wrapper will be executed first")
#         return original_function()
#     return wrapper_function
# @decorator_function
# def display():
#     print("good morning")
#
# display()
#
# # decorator with arguments
#
# def decorate_new_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("wrapper will be executed first")
#         return original_function(*args, **kwargs)
#     return wrapper_function
#
#
# @decorate_new_function
# def display_info(name, age):
#     print("name {} and age is {}  ".format(name, age))
#
# display_info("anil", 2899)
#
# def decorate_function(original_function):
#     def wrapper_function(name):
#         res = original_function(name)
#         return res.upper()
#     return wrapper_function
#
# @decorate_function
# def display(name):
#     return name
#
# res = display("anil")
# print(res)
#
# def sample_decorator(original_function):
#     def wrapper_function(a, b):
#         print("inside wrapper")
#         if b == 0:
#             print("divisible by zero is not possible")
#             return
#         return original_function(a,b)
#     return wrapper_function
# @sample_decorator
# def dividing(a,b):
#     print( a/b)
#
# dividing(5,2)
# print("=========")
# dividing(4,0)
#
#
# def star_decorator(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("*"*15)
#         original_function()
#         print("*" * 15)
#     return wrapper_function
#
# def divide_decorator(original_function2):
#     def wrapper_function(*args, **kwargs):
#         print("%"*15)
#         original_function2()
#         print("%" * 15)
#     return wrapper_function
# @star_decorator
# @divide_decorator
# def display():
#     print("hello")
#
#
# display()
# # display = star_decorator(divide_decorator(display))

def decorator_function1(original_function):
    def wrapper_function1():
        print("i am inside wrapper1")
        original_function()
        # print("i am inside after wrapper1")
    return wrapper_function1
def decorator_function2(orig_function):
    def wrapper_func():
        print("i am inside wrapper2")
        orig_function()
        # print("i am inside after wrapper2")
    return wrapper_func
@decorator_function2
@decorator_function1
def display():
    print("good evening")

# display = decorator_function2(decorator_function1(display))
# display()
# decorator_function2(wrapper_function1)
# wrapper_func
# i am inside wrapper2
# i am inside wrapper1
# good evening
# i am inside after wrapper1
# i am inside after wrapper2
# display()




def decor1(func1):
    def inner1():
        x = func1()
        return x * x
    return inner1

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
@decor1
@decor
def num():
    return 10
# decor1(decor(num))
# decor1(inner)
# inner1()
# 2*10
# 20 * 20
# 100

# print(num())


# def do_twice(original_func):
#     def wrapper_do_twice():
#         original_func()
#         original_func()
#     return wrapper_do_twice

# @do_twice
# def greet():
#     print("greetings have a nice  day")
# greet()

# with arguments
# def do_twice(original_func):
#     def wrapper_do_twice(*args, **kwargs):
#         original_func(*args, **kwargs)
#         original_func(*args, **kwargs)
#     return wrapper_do_twice
#
# @do_twice
# def greet(name):
#     print("greetings have a nice  day {}".format(name))
# greet("Anil")

# returning values from decorator
# def do_twice(original_func):
#     def wrapper_do_twice(*args, **kwargs):
#         res = original_func(*args, **kwargs)
#         return res
#     return wrapper_do_twice
#
# @do_twice
# def return_greeting(name):
#     print("creating greeting ")
#     return "Hi {}".format(name)
#
# hi_anil = return_greeting("anil")
# print(hi_anil)

# import functools
# def do_twice(original_function):
#     @functools.wraps(original_function)
#     def wrapper_do_twice():
#         original_function()
#     return wrapper_do_twice
#
# @do_twice
# def say_whee():
#     print("eee")
#
# say_whee()
# print(say_whee)
# print(say_whee.__name__)


import functools

def decorator_function(original_function):
    @functools.wraps(original_function)
    def wrapper_function():
        print("do something before calling func")
        value = original_function()
        print("do something after calling the func")
        return value
    return wrapper_function

# timing decorator
import time
import functools
def timer_decorator(original_function):
    @functools.wraps(original_function)
    def wrapper_function(*args, **kwargs):
        startime = time.time()
        res = original_function(*args, **kwargs)
        endtime = time.time()
        print("function {} finished  {}".format(original_function.__name__, endtime-startime))
        return res
    return wrapper_function

@timer_decorator
def waste_some_time():
    import time
    time.sleep(2)

# waste_some_time()
# print(waste_some_time.__name__)


import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting("ANil",29)


def sample_dec(*args, **kwargs):
    print(sample_dec.__name__, *args)
sample_dec(10,20)