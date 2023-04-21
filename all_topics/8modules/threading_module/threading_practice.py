# cpu bound we will go for multiprocessing or I/O bound tasks
# downloading the files or reading data from disk

# cpu bound -- multi processing -- crunching cpu -- processing image
# Io bound -- multi threading--apis calls, reading /writing downloading images, network operations

import time
import threading

start_time = time.time()


def do_something(seconds):
    print("sleeping  {} sec ".format(seconds))
    time.sleep(seconds)
    print("sleeping done")

# creating thread objects

#
# t1 = threading.Thread(target=do_something,)
# t2 = threading.Thread(target=do_something,)
#
# # starting the threads
# t1.start()
# t2.start()
#
# # join method wait until the thread completes
# t1.join()
# t2.join()
#
# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=(1.5,))
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
# end_time = time.time() - start_time
#
# print("time taken for this is {}".format(end_time))

# in python3.2 we threadpool executor
import concurrent.futures

start_time_new = time.time()


def do_something_new(seconds):
    print("sleeping for {} sec(s)".format(seconds))
    time.sleep(seconds)
    return "sleep done {}".format(seconds)


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 13, 2, 1]

    # results = [executor.submit(do_something_new, sec) for sec in secs]
    # # f1 = executor.submit(do_something_new, 1)  # submit method will always return the value
    # # f2 = executor.submit(do_something_new, 1)
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    # # print(f1.result())  # when we use result method it will wait until it completes.
    # # print(f2.result())

    results = executor.map(do_something_new, secs)

    # for result in results:
    #     print(result)

end_time_new = time.time() - start_time_new

print("time taken for concurrent  {}".format(end_time_new))
