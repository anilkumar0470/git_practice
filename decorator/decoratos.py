# from functools import wraps
# # A decorator is a function that takes another function as argument and add some kind of
# # functionality and returns another function i.e without modifying the source code we can
# # still enhance the code
#
# # why we want use decoratos
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
def decorator_fun(original_func):
    def test_wrapper():
        print("test wrapper is executing before {}".format(original_func.__name__))
        return original_func()
    return test_wrapper
@decorator_fun
def display_func():
    print("display function")

display_func()

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
