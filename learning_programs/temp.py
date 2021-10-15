import time
from decorators import do_twice
# list = [1,2,3,4,5,6,7,8,9]
# my_list = [n*n for n in list if n%2 == 0]
# print (my_list)

#why we need use decorator instead of this function
# one use of decorator is without effecting the original function  we can change/add the
# behaviour to the internal function



def main_function(arg_function):
    def wrapper_function():
        print("name of the function {}".format(arg_function.__name__))
        start_time = time.time()
        arg_function()
        print("time taken is {}".format(time.time()-start_time))
        print("happening after")
    return wrapper_function

@main_function
def display():
    time.sleep(4)
    print("i am outside of function")
#display()


@do_twice
def say_hi(name):
    print("say hai to {}".format(name))
    return "name of the candidate is {}".format(name)


p = say_hi("Apathapa")
print(say_hi)
print(say_hi.__name__)
print(p)
