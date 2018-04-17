# from threading import Thread
# import time
#
#
# li = [1,2,3,4,5,6,7]
# my_li = [ n for n in li]
# print(my_li)
#
#
# def timer(name, delay, repeat):
#     print("Timer {} is started at time {}".format(name, time.ctime(time.time())))
#
#     while repeat > 0:
#         time.sleep(delay)
#         print("Name of the thread is {} and started at {} ".format(name, time.ctime(time.time())))
#         repeat -= 1
#     print("Timer {} is Completed ".format(name))
#
#
# def main():
#     t1 = Thread(target=timer, args=("test1", 2, 5))
#     t2 = Thread(target=timer, args=("test2", 1, 5))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
# if __name__ == "__main__":
#      pass
#
# import threading
# import time
# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-9s) %(message)s',)
#
#
# def n():
#     logging.debug('Starting')
#     logging.debug('Exiting')
#
#
# def d():
#     logging.debug('Starting')
#     time.sleep(5)
#     logging.debug('Exiting')
#
# if __name__ == '__main__':
#
#     t = threading.Thread(name='non-daemon', target=n)
#
#     d = threading.Thread(name='daemon', target=d)
#     d.setDaemon(True)
#
# 	d.start()
# 	t.start()

#
# fd = open("sample.txt", "r+")
# fd.write("spotlach")

# with open("sample.txt","w+") as f:
#     out = f.read()
# print (out)

# str1 = input()
# str2 = input()
# str3 = ''
# l = ''
# for i,j in zip(str1,str2):
#     if len(str1) == len(str2):
#         str3 += i+j
#         l = ''
#     elif len(str1) < len(str2):
#         str3 +=i+j
#         l = str2[len(str1):]
#     elif len(str1) > len(str2):
#         str3 += i+j
#         l = str1[len(str2):]
# str3 += l
# print(str3)

import pytest
import logging


# class TestSample:
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger(__name__)
#
#     @pytest.mark.order2
#     def test_1(self):
#         self.log.info("def test1")
#
#     @pytest.mark.order1
#     def test_2(self):
#         self.log.info("def test2")

#
# class TestSample2:
#
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger(__name__)
#
#     @pytest.mark.run(order=1)
#     def test_run_order_1(self):
#         self.log.info("I am order1 but placed in last")
#
#     @pytest.mark.run(order=2)
#     def test_run_order_2(self):
#         self.log.info("I am order2 but placed in top")
#         assert True
#
#     @pytest.mark.run(order=3)
#     def test_run_order_3(self):
#         self.log.info("I am order1 but placed in last")
#
#     def test_fun(self):
#         self.log.info("I am order1 but placed in last")
#


#
# class TestDependency:
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger(__name__)
#
#     def test_dependency_1(self):
#         self.log.info("i am testing dependency 1")
#         # assert False, "we are waiting"
#
#     def test_dependency_2(self, depends=[test_dependency_1]):
#         self.log.info("this should execute after execution of first one")

#
# def test_answer(cmdopt):
#     if cmdopt == "type1":
#         print ("first")
#     elif cmdopt == "type2":
#         print ("second")
#     assert 0 # to see what was printed


# c = []
# for i,j in enumerate(a):
#     b = j
#     print (b)
#     for k in range(0,len(a)-1):
#         if b == a[k] :
#             pass
#         else :
#             b = b * a[k]
#         c.append(b)
# print (c)


new_array = []
f=[]
#a = [5,0.5,8,7,-1]
a = [2,3,8,7,5]
temp = 1
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1):
        if i == j:
            pass
        else:
            if a[j] == 0:
                pass
            else:
                temp = temp * a[j]
    print(temp)
    if a[i] == 0:
        new_array.append('0')
    else:
        # new_value = temp/a[i]
        new_array.append(abs(int(temp)))
        #f.append(new_value)
print (new_array)
