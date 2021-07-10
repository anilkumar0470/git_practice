import multiprocessing
import time

start_time = time.time()


def do_something():
    print("waiting for 1 sec")
    time.sleep(1)
    print("waiting done ")
#do_something()
#do_something()
# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
# end_time = time.time()
# print(end_time - start_time)
#
#
#
#
# if __name__ == '__main__':
#     p1.start()
#     p2.start()
#     #p1.join()
#     #p2.join()
#
#     end_time = time.perf_counter()
#     print("fininshed in {} seconds ".format(round(end_time - start_time, 2)))