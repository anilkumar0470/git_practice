# import threading
# import time
#
#
# def func_sleep(seconds):
#     print("sleeping {} second(s)!!!".format(seconds))
#     time.sleep(seconds)
#     print("sleep done !!")
#
#
# start_time = time.time()
# # func_sleep()
# # func_sleep()
#
# # let's implement threading here
# # multi threading will used when u dont have sufficient memory or if your task is not related to memory or if your task
# # is not doing anything in device memory level let say connecting  to remote device and executing some commands or
# # downloading files from internet or reading/writing files
# #
# # t1 = threading.Thread(target=func_sleep)
# # t1.start()
# #
# # t2 = threading.Thread(target=func_sleep) # creating threading object
# # t2.start() # execution of thread will start
# # t1.join() # waiting for thread to complete
# # t2.join()
#
#
# # lets say you have to call same function 10 times
# # then we cannot write 30 lines we will use for loop for the same
#
# # creating thread and starting the same we cannot use join here because it will wait for completing the thread
# # we will use another for loop for the same
# threads = []
# for _ in range(10):
#     t = threading.Thread(target=func_sleep, args=[2])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
# end_time = time.time()
# print("time taken is {}".format(end_time - start_time))
#


def funct(emp, emp_list=""):
    print(emp_list)
    emp_list = emp_list + emp
    print(emp_list)

funct("anil", "junk")
funct("kumar")



def decorator_function(original_fucntion):
    def wrapper_fucntion():
        print("i am inside wrapper")
        original_fucntion()
    return wrapper_fucntion
@decorator_function
def display():
    print(" i am in display")
display()









def deco_function(original_fucntion):
    def wrapper_function(*args, **kwargs):
        print("i am inside wrapper function")
        original_fucntion(*args, **kwargs)
    return wrapper_function

@deco_function
def display(name, age):
    print("name {} and age are {}".format(name, age))
display("anil", 20)

