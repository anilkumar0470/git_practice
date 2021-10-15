# # # from threading import Thread
# # # import time
# # #
# # #
# # # li = [1,2,3,4,5,6,7]
# # # my_li = [ n for n in li]
# # # print(my_li)
# # #
# # #
# # # def timer(name, delay, repeat):
# # #     print("Timer {} is started at time {}".format(name, time.ctime(time.time())))
# # #
# # #     while repeat > 0:
# # #         time.sleep(delay)
# # #         print("Name of the thread is {} and started at {} ".format(name, time.ctime(time.time())))
# # #         repeat -= 1
# # #     print("Timer {} is Completed ".format(name))
# # #
# # #
# # # def main():
# # #     t1 = Thread(target=timer, args=("test1", 2, 5))
# # #     t2 = Thread(target=timer, args=("test2", 1, 5))
# # #     t1.start()
# # #     t2.start()
# # #     t1.join()
# # #     t2.join()
# # #
# # # if __name__ == "__main__":
# # #      pass
# # #
# # # import threading
# # # import time
# # # import logging
# # #
# # # logging.basicConfig(level=logging.DEBUG,
# # #                     format='(%(threadName)-9s) %(message)s',)
# # #
# # #
# # # def n():
# # #     logging.debug('Starting')
# # #     logging.debug('Exiting')
# # #
# # #
# # # def d():
# # #     logging.debug('Starting')
# # #     time.sleep(5)
# # #     logging.debug('Exiting')
# # #
# # # if __name__ == '__main__':
# # #
# # #     t = threading.Thread(name='non-daemon', target=n)
# # #
# # #     d = threading.Thread(name='daemon', target=d)
# # #     d.setDaemon(True)
# # #
# # # 	d.start()
# # # 	t.start()
# #
# # #
# # # fd = open("sample.txt", "r+")
# # # fd.write("spotlach")
# #
# # # with open("sample.txt","w+") as f:
# # #     out = f.read()
# # # print (out)
# #
# # # str1 = input()
# # # str2 = input()
# # # str3 = ''
# # # l = ''
# # # for i,j in zip(str1,str2):
# # #     if len(str1) == len(str2):
# # #         str3 += i+j
# # #         l = ''
# # #     elif len(str1) < len(str2):
# # #         str3 +=i+j
# # #         l = str2[len(str1):]
# # #     elif len(str1) > len(str2):
# # #         str3 += i+j
# # #         l = str1[len(str2):]
# # # str3 += l
# # # print(str3)
# #
# # #import pytest
# # import logging
# #
# #
# # # class TestSample:
# # #     logging.basicConfig(level=logging.DEBUG)
# # #     log = logging.getLogger(__name__)
# # #
# # #     @pytest.mark.order2
# # #     def test_1(self):
# # #         self.log.info("def test1")
# # #
# # #     @pytest.mark.order1
# # #     def test_2(self):
# # #         self.log.info("def test2")
# #
# # #
# # # class TestSample2:
# # #
# # #     logging.basicConfig(level=logging.DEBUG)
# # #     log = logging.getLogger(__name__)
# # #
# # #     @pytest.mark.run(order=1)
# # #     def test_run_order_1(self):
# # #         self.log.info("I am order1 but placed in last")
# # #
# # #     @pytest.mark.run(order=2)
# # #     def test_run_order_2(self):
# # #         self.log.info("I am order2 but placed in top")
# # #         assert True
# # #
# # #     @pytest.mark.run(order=3)
# # #     def test_run_order_3(self):
# # #         self.log.info("I am order1 but placed in last")
# # #
# # #     def test_fun(self):
# # #         self.log.info("I am order1 but placed in last")
# # #
# #
# #
# # #
# # # class TestDependency:
# # #     logging.basicConfig(level=logging.DEBUG)
# # #     log = logging.getLogger(__name__)
# # #
# # #     def test_dependency_1(self):
# # #         self.log.info("i am testing dependency 1")
# # #         # assert False, "we are waiting"
# # #
# # #     def test_dependency_2(self, depends=[test_dependency_1]):
# # #         self.log.info("this should execute after execution of first one")
# #
# # #
# # # def test_answer(cmdopt):
# # #     if cmdopt == "type1":
# # #         print ("first")
# # #     elif cmdopt == "type2":
# # #         print ("second")
# # #     assert 0 # to see what was printed
# #
# # a = [2,3,8,7,5]
# # c = []
# # for i,j in enumerate(a):
# #     b = j
# #     print (b)
# #     for k in range(0,len(a)-1):
# #         if b == a[k] :
# #             pass
# #         else :
# #             b = b * a[k]
# #         c.append(b)
# # print (c)
# #
# #
# # new_array = []
# # f=[]
# # #a = [5,0.5,8,7,-1]
# # a = [2,3,8,7,5]
# # temp = 1
# # for i in range(0,len(a)-1):
# #     for j in range(0,len(a)-1):
# #         if i == j:
# #             pass
# #         else:
# #             if a[j] == 0:
# #                 pass
# #             else:
# #                 temp = temp * a[j]
# #     print(temp)
# #     if a[i] == 0:
# #         new_array.append('0')
# #     else:
# #         # new_value = temp/a[i]
# #         new_array.append(abs(int(temp)))
# #         #f.append(new_value)
# # print (new_array)
# #
# #
# #
# # # class sample_hello():
# # #     def __init__(self):
# # #         print(" i am in hello")
# # # class sample_hai():
# # #     def __init__(self):
# # #         print("i am in hai")
# # # a = input("enter")
# # # c = eval("sample_{}()".format(a))
# # # print(c)
# #
# # # st = input("enter string")
# # # k = int(input("enter secret level"))
# # # a = ""
# # # for i in st :
# # #     v = ord(i) + k
# # #     a = a + chr(v)
# # # print(a)
# #
# #
# #
# # # This is code to validate expression
# # #
# # user_input = "[a+b-{(c/d}+a)*c]^2"
# # user_input = "[a(v)v}v)v]"
# # sample_dict = {"{": "}", "[": "]", "(": ")"}
# # Flag = 0
# # for letter in user_input:
# #     if letter in sample_dict:
# #         for num in range(0, len(user_input)):
# #             if user_input[len(user_input)-num-1] in sample_dict.values():
# #                 if sample_dict[letter] == user_input[len(user_input)-num-1]:
# #                     user_input = user_input.replace(sample_dict[letter], " ")
# #                     Flag += 1
# #                     break
# #                 else:
# #                     break
# # if Flag == 3:
# #     print ("valid")
# # else:
# #     print ("invalid")
# #
# # ll = "!@#$%^&*()[]{};:,./<>?\|`~-=_+"
# # pr_details = 'Hello !@#$%^&*()[]{};:,./<>?\|`~-=_+ Prasad'
# # for e in ll:
# #     if e in pr_details:
# #        pr_details = pr_details.replace(e, "")
# # print pr_details
# #
# #
# # from string import maketrans   # Required to call maketrans function.
# #
# # intab = "aeiou"
# # outtab = "12345"
# # trantab = maketrans(intab, outtab)
# # print trantab
# #
# # str = "this is string example....wow!!!";
# # print str.translate(trantab)
# # c is focus variable here and to make c value as zero how many instances it will take
#
# # dict = [{"a": 6}, {"b": 3}, {"c": 5}, {"d": 4}]
# #
# #
# # def sample_func(arg, main_count):
# #     focus_variable = "c"
# #     for index, val in enumerate(arg):
# #         for key, value in val.items():
# #             if value > 0:
# #                 main_count = main_count + 1
# #                 value = value - 1
# #                 aa = dict[index]
# #                 aa.update({key: value})
# #                 if key == focus_variable and value == 0:
# #                         print(main_count)
# #                         import sys
# #                         sys.exit()
# #
# #                 else:
# #                         print(value)
# #     else:
# #         sample_func(dict, main_count)
# #
# # sample_func(dict, 0)
#
#
# # arr = [1, 2, 3]
# # m = len(arr)
# # n = 4
# # table = [[0 for x in range(m)] for x in range(n+1)]
# # print(table)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
list1 = [1,4,5,6]

print(list((map(lambda x : x * x * x, list1))))
#
#
#
#
#
# class Sample()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#










class Sample:



    def __init__(self, name, age):
        print("i am in it")


    def sample_funct(self):
        print("sample function ")

    @classmethod
    def hello_class_function(cls):
        print("class function")

    @staticmethod
    def hi_static_function():
        print("static function")

# sam1 = Sample("anil", 24)
# sam2 = Sample("kumar", 29)




def my_decorator(original_function):

    def wrapper():
        print("inside wrapper function")
        original_function()
    return wrapper


@my_decorator
def display():
    print("i am in display")

# display = my_decorator(display)
# display()

# 1 50 num % 2 --terra num %3 --logic num % 5 -- terralogic
# increment


# l1 = ["logic" for i in range(2,50,2)]
# print(l1)
# l2 = ["terra" for i in range(3,50,3)]
# print(l2)
# l3 = ["terralogic" for i in range(5,50,5)]
# print(l3)


# for i in range(1,50):
#     if i in range(2,50,2):
#         print("terra")
#     elif i in range(3,50,3):
#         print("logic")
#     elif i in range(5,50,5):
#         print("terralogic")



# 50, 20,10, 5, 1

# 55 -- 50, 5
# minimum no of coins
# #
# list = [50, 20, 10, 5, 1]
# num = 55
# min_num = None
# j  = 0
# count = 0
# for i in list:
#     j = i + j
#     print(j)
#     if j > num:
#         count = count +1
#         pass
#         j = j-i
#     elif j == num :
#         count = count + 1
#         break
# print(count)


# 1
# 11
# 12
# 1211
# 112112
# 12211221



# "Mapping Lists in 2D/dict
list_1 = ['a','b','c','d','e','f','g','h','i','j']
list_2 =['1','2','3']
#
# Output
# [['a','1'], ['b','2'], ['c','3'], ['d','1'],['e','2'],['f','3'],['g','1'],['h','2'],['i','3'],['j','1']]"


list3 = []
# count = 1
# for i in range(len(list_1)):
#     list4 = []
#     print(list_1[i])
#     print(count)
#     if count < len(list_2):
#         list4.append(list_1[i])
#         list4.append(list_2[count])
#         list3.append(list4)
#         count = count + 1
#     elif count == len(list_2):
#         count = 0
#         continue
#
# print(list3)



count = 0
list_3 = []
list_4 = []
for i in range(len(list_1)):
    list_3.append(list_1[i])
    list_3.append(list_2[count])
    list_4.append(list_3)
    list_3 = []

    if count == len(list_2) -1 :
        count = 0
    else:
        count = count + 1
    print(count)
print(list_4)




list1 = [x  if x%2 == 0  else x*x for x in range(10)]
print(list1)


