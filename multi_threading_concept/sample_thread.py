# from threading import Thread
# import time
#
#
# def timer(name,delay,repeat):
#     print ("Timer is {} started:".format(name))
#     while repeat > 0:
#         time.sleep(delay)
#         print(str(time.ctime(time.time())))
#         print("Thread {}".format(name))
#         repeat -= 1
#     print ("Timer is {}completed".format(name))
#
# def Main():
#     t1 = Thread(target=timer,args=("Timer1",3,5))
#     t2 = Thread(target=timer,args=("Timer2",2,5))
#     t1.start()
#     t2.start()
#
# # if __name__ == "__main__":
# #     Main()
#
# import time
# import threading
#
#
# def do_something(seconds):
#     print("i am sleeping for {}".format(seconds))
#     time.sleep(seconds)
#     print("sleeping is done")


# start_time = time.time()
# t1 = threading.Thread(target=do_something,)
# t2 = threading.Thread(target=do_something,)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# threads = []
# for i in range(10):
#     t = threading.Thread(target=do_something,args=[1.5,])
#     t.start()
#     threads.append(t)
# print("no of active threads {}".format(threading.active_count()))
# for thread in threads:
#     thread.join()
# end_time = time.time() - start_time
# print(end_time)

# cpu bound we will go for multiprocessing or I/O bound tasks
# downloading the files or reading data from disk

# cpu bound -- multi processing
# Io bound -- multi threading..apis calls, reading /writing downloading images
import os
import threading
import time

def sleep_time(time_to_sleep):
    print("i am sleeping for {}".format(time_to_sleep))
    time.sleep(time_to_sleep)
    print("sleep done for {} and id is {}".format(threading.current_thread().name, os.getpid()))



# if __name__ == "__main__":
#     start_time = time.time()
#     threads = []
#     print("main thread name is {} and id is {}".format(threading.current_thread().name, os.getpid()))
#     # print("main thread name is {}".format(threading.main_thread().name))
#     for i in range(10):
#         t = threading.Thread(target=sleep_time, args=[i, ], name="thread {}".format(i))
#         t.start()
#         threads.append(t)
#
#     for thread in threads:
#         thread.join()
#     print("time taken is {}".format(time.time() - start_time))

#
# import multiprocessing
# import time
#
# def do_something():
#
#     print("i am sleeping for 1 second")
#     time.sleep(1)
#     print("sleeping is done")
#
#
# # p1 = multiprocessing.Process(target=do_something)
# # p2 = multiprocessing.Process(target=do_something)
#
# if __name__ == "__main__":
#     start_time = time.time()
#     processes = []
#     for i in range(10):
#         p = multiprocessing.Process(target=do_something)
#         processes.append(p)
#         p.start()
#     for process in processes:
#
#         process.join()
#     end_time = time.time()
#     print("time taken is {}".format(end_time - start_time))
#
#



# race condition and locking the variables
# https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
#
# x = 0
#
#
# def increment():
#     global x
#     x = x + 1
#
#
# def task():
#     for _ in range(100000):
#         increment()
#
#
# def main_thread():
#     global x
#     x = 0
#     t1 = threading.Thread(target=task)
#     t2 = threading.Thread(target=task)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#
# if __name__ == "__main__":
#     # for i in range(10):
#         main_thread()
#         time.sleep(2)
#         print(x)
#         # main_thread()
#         # print(x)
#

import threading
import concurrent.futures

def sleep_time1(time_to_sleep):
    print("i am sleeping for {}".format(time_to_sleep))
    time.sleep(time_to_sleep)
    return "sleep done for {} and id is {}".format(threading.current_thread().name, os.getpid())


with concurrent.futures.ThreadPoolExecutor() as executor:
    t1 = executor.submit(sleep_time1, 1)
    print(t1.result())