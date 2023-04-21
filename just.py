# # """def do_revers_line(line):
# #     print "line:",line
# #     list_line = line.split()
# #     res_str = ""
# #     for each_word in list_line:
# #         st = ""
# #         l = len(each_word)
# #         while l>0:
# #             st = st + each_word[l-1]
# #             l = l-1
# #         res_str = res_str + " " +st
# #     print res_str
# #     return res_str.strip()
# # line = 'anilkumar pathapati'
# # do_revers_line(line)
# # """
# #
# # import threading
# # import subprocess
# #
# # #
# # #
# # # def do_something(eb):
# # #     subprocess.run("date", shell=True)
# # #
# # # t1 = threading.Thread(target=do_something,args=(10,))
# # # t1.start()
# #
# #
# # # max of sum of elements in the list
# #
# # list1 = [[3, 4, 5], [1, 2, 3], [0, 9, 0]]
# # max_count = sum(list1[0])
# # for index in range(1, len(list1)):
# #     out = max(sum(list1[index]), max_count)
# #     if out != max_count:
# #         max_count = out
# # print(max_count)
# # # pairing without same value
# # l1 = [100, 20, 30, 400]
# # l2 = [400, 2, 30]
# # l3 = []
# # for i in l1:
# #     for j in l2:
# #         if i != j:
# #             l3.append([i, j])
# # print(l3)
# # l4 = [[a,b] for a in l1 for b in l2 if a !=b ]
# # print(l4)
# #
# # l5 = []
# # for index in range(len(l1)-1):
# #     l5.append([l1[index], l1[index+1]])
# # print(l5)
# #
# #
# # test_list1 = [[1, 4, 5], [8, 7], [2]]
# # test_list2 = [['g', 'f', 'g'], ['f', 'r'], ['u']]
# #
# #
# # for el1, el2 in zip(test_list1, test_list2):
# #     for e1, e2 in zip(el1, el2):
# #         print((e1, e2))
# #
# # l6 = [(e1, e2)for element1, element2 in zip(test_list1, test_list2) for e1, e2 in zip(element1, element2)]
# # print(l6)
# #
# # l7 = [['Paras', 90], ['Jain', 32], ['Geeks', 120], ['for', 338], ['Labs', 532]]
# #
# # max_value = l7[0]
# # for element in l7:
# #     if element[1] > max_value[1]:
# #         max_value = element
# # print(max_value)
# #
# # test_list = [1, 4, 5, 6, 4, 5, 6, 5, 4,3]
# # out_list = []
# # temp_list = []
# # for element in test_list:
# #     temp_list.append(element)
# #     if element == 5:
# #         out_list.append(temp_list)
# #         temp_list = []
# # else:
# #     out_list.append(temp_list)
# #
# # print(out_list)
# #
# # test_list = [{'gfg' : 1, 'is' : 2, 'best' : 3}, {'gfg' : 1, 'is' : 2, 'best' : 3},{'gfg' : 9, 'is' : 8, 'best' : 6}]
# # new_out_list = []
# # for ele in test_list:
# #     if ele not in new_out_list:
# #         new_out_list.append(ele)
# # print(new_out_list)
# #
# #
# # def sample_default_args(emp, empty_list=[]):
# #     if empty_list:
# #         empty_list = []
# #     empty_list.append(emp)
# #     print(empty_list)
# #
# # sample_default_args("anil")
# # sample_default_args("kumar")
# # sample_default_args("eee")
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
# # # pdb - built module
# # print("good  morning")
# # aaa = 10
# # bbb = 20
# #
# #
# # def sample(name):
# #     print(name)
# #
# # import pdb
# # pdb.set_trace()
# # print("good  evening")
# # print("good  evening")
# # print("good  evening")
# # print("good  evening")
# # print("good  evening")
# # print("good  evening")
# #
# #
# # sample("bye")
#
#
#
# # l and ll
# # n -- > next  line(only one line)
# # c -- continue
#
# # s -- inside function
# # a -- args
# # w - stack trace
# # quit
# # b - break
#
#
# # import re
# # fd = open("aaa.txt")
# # for line in fd:
# #
# #     print(line)
#
# d = {"k1":"v1", "k2": {"nk1":"v2", "nk2":{"nk3":"v3"}}}
#
# #
# # def sample_function(new_dict, result_str="", out_list=[]):
# #     for key, value in new_dict.items():
# #         if type(value) == dict:
# #             result_str = result_str + key
# #             sample_function(value, result_str, out_list)
# #         else:
# #             if result_str:
# #                 out_list.append(("{}{}".format(result_str, key), value))
# #             else:
# #                 out_list.append((key, value))
# #     return out_list
# # res = sample_function(d)
# #
# # print(res)
#
#
# #
# # def sample_decorator(orignal_function):
# #     def wrapper_function(string1):
# #         print("this will be executed first")
# #         out = orignal_function(string1)
# #         return out.upper()
# #     return wrapper_function
# #
# # @sample_decorator
# # def display_hi(new_string):
# #     print("hi")
# #     return new_string
# #
# # print(display_hi("good morning"))
# #
# #
# # def uppercase_decorator(original_func):
# #     def wrapper_func():
# #         res = original_func()
# #         print("uppercase decorator")
# #         return res.upper()
# #     return wrapper_func
# #
# # def splitting_string(original_func):
# #     def wrapper_func():
# #         out = original_func()
# #         print("splitting string")
# #         return out.split()
# #     return wrapper_func
# #
# # @splitting_string
# # @uppercase_decorator
# # def return_string():
# #     return "hi good evening testing "
# #
# # print(return_string())
#
#
# # string1 = "godd morning"
# # result = ""
# # for element in string1:
# #     result = element + result
# # print(result)
#
# #
# # def sample_decorator(original_function):
# #     def wrapper_function(var):
# #         print("wrapper will be executed first")
# #         out =  original_function(var)
# #         return out.upper()
# #     return wrapper_function
# #
# #
# # @sample_decorator
# # def sample_display(var):
# #     return var
# #
# # # sample_display = sample_decorator(sample_display)
# # # sample_display()
# #
# # print(sample_display("good morning"))
#
# # import json
# #
# #
# # string ="""
# # {
# # "peoples" : [
# #     {"name":"some",
# #     "age":"23"
# #     },
# #     {"name":"some1",
# #     "age":"231"
# #     }
# #
# # ]
# #
# # }
# #
# # """
# # out = json.loads(string)
# # print(type(out))
# # #
# # import requests
# # res = requests.get("https://reqres.in/api/users?page=2")
# # print(res.status_code)
# #
# # import pexpect
# #
# #
# # def main():
# #
# # 	# spawn a child process.
# # 	child = pexpect.spawn('ftp ftp.us.debian.org')
# #
# # 	# search for the Name pattern.
# # 	child.expect('Name .*: ')
# #
# # 	# send the username with sendline
# # 	child.sendline('anonymous')
# #
# # 	# search for the Password pattern
# # 	child.expect('Password:')
# #
# # 	# send the password to the childprocess
# # 	# by sendline
# # 	child.sendline('anonymous@')
# #
# # 	# detect ftp accepts command from user
# # 	# by 'ftp> ' pattern
# # 	child.expect('ftp> ')
# #
# # 	# If it accepts command then download the
# # 	# welcome.msg file from the ftp server
# # 	child.sendline('get welcome.msg')
# #
# # 	# again check whether ftp client accepts
# # 	# command from user by 'ftp> ' pattern
# # 	child.expect('ftp> ')
# #
# # 	# close the ftp client.
# # 	child.sendline('bye')
# #
# # 	# print the interactions with the child
# # 	# process.
# # 	print(child.before.decode())
# # 	child.interact()
# #
# # 	# print the downloaded file by executing cat
# # 	# command with pexpect.run method
# # 	print(pexpect.run('cat ./welcome.msg').decode())
# #
# # #
# # # if __name__ == '__main__':
# # # 	main()
# # # code
# # class Person:
# #
# # 	# Constructor
# # 	def __init__(self, name, id):
# # 		self.name = name
# # 		self.id = id
# #
# # 	# To check if this person is an employee
# # 	def Display(self):
# # 		print(self.name, self.id)
# #
# #
# # class Emp(Person):
# #
# # 	def __init__(self, name, id):
# # 		self.name_ = name
# #
# # 	def Print(self):
# # 		print("Emp class called")
# #
# #
# # Emp_details = Emp("Mayank", 103)
# #
# # # calling parent class function
# # Emp_details.name_, Emp_details.name
#
#
# # Input : {[]{()}}
# # Output : Balanced
# #
# # Input : [{}{}(]
# # Output : Unbalanced
# # sample_input = "[{}{}(]"
# # new_dict = {"{": "}", "[": "]", "(": ")"}
# # out_list = []
# #
# # import pdb
# # # pdb.set_trace()
# # for element in sample_input:
# # 	if element in list(new_dict.keys()):
# # 		out_list.append(element)
# # 	else:
# # 		if len(out_list) == 0:
# # 			print("given input is invalid")
# # 			break
# # 		last_item = out_list.pop()
# # 		value = new_dict[last_item]
# # 		if element != value:
# # 			print("given input is not valid")
# # 			break
# # else:
# # 	print("given input is valid")
# # from threading import Thread
# # from time import sleep
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# # from selenium.common.exceptions import TimeoutException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # # This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
# # caps=[{
# #       'os_version': '10',
# #       'os': 'Windows',
# #       'browser': 'chrome',
# #       'browser_version': 'latest',
# #       'name': 'Parallel Test1', # test name
# #       'build': 'browserstack-build-1' # Your tests will be organized within this build
# #       },
# #       {
# #       'os_version': 'Big Sur',
# #       'os': 'OS X',
# #       'browser': 'Safari',
# #       'browser_version': '14',
# #       'name': 'Parallel Test2',
# #       'build': 'browserstack-build-1'
# #       },
# #       {
# #       'os_version': '10',
# #       'os': 'Windows',
# #       'browser': 'firefox',
# #       'browser_version': 'latest-beta',
# #       'name': 'Parallel Test3',
# #       'build': 'browserstack-build-1'
# # }]
# # #run_session function searches for 'BrowserStack' on google.com
# # def run_session(desired_cap):
# #   driver = webdriver.Remote(
# #       command_executor='https://anilpathapati_L2pmNh:UxzsDpZ9ggVcca8Ew3Ay@hub-cloud.browserstack.com/wd/hub',
# #       desired_capabilities=desired_cap)
# #   driver.get("https://www.google.com")
# #   if not "Google" in driver.title:
# #       raise Exception("Unable to load google page!")
# #   elem = driver.find_element_by_name("q")
# #   elem.send_keys("BrowserStack")
# #   elem.submit()
# #   try:
# #       WebDriverWait(driver, 5).until(EC.title_contains("BrowserStack"))
# #       driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
# #   except TimeoutException:
# #       driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
# #   print(driver.title)
# #   driver.quit()
# # #The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
# # for cap in caps:
# #   Thread(target=run_session, args=(cap,)).start()
# #   import pdb
# #   pdb.set_trace()
# #
# #
# #
# #
# #
# def isBalanced(s):
#     # Write your code here
#     new_dict = {"(": ")", "{": "}", "[": "]"}
#     flag = False
#     out = []
#     for index, value in enumerate(s):
#         if value not in list(new_dict.keys()):
#             prev = s[index -1]
#
#             if len(out) > 0 and new_dict[prev] == value:
#                 out.pop()
#                 print(out)
#             else:
#                 print("un balanced")
#         else:
#             out.append(value)
#
#
# print(isBalanced("{}{}()"))

# out_list = []
# input_list = [1, 2, 3, 5]
#
# for i in range(100):
#     if i not in input_list:
#         out_list.append(i)
#     else:
#         out_list.append(i)
#     if i == input_list[-1]:
#         break
# print(out_list)
#
# import datetime;
#
# # ct stores current time
# ct = datetime.datetime.now()
# print("current time:-", ct)
#
# # ts store timestamp of current time
# ts = ct.timestamp()
# print("timestamp:-", ts)
#
# from datetime import datetime
# currentDateAndTime = datetime.now()
#
# print("The current year is ", currentDateAndTime.year) # Output: The current year is  2022
# print("The current month is ", currentDateAndTime.month) # Output: The current month is  3
# print("The current day is ", currentDateAndTime.day) # Output: The current day is  19
# print("The current hour is ", currentDateAndTime.hour) # Output: The current hour is  10
# print("The current minute is ", currentDateAndTime.minute) # Output: The current minute is  49
# print("The current second is ", currentDateAndTime.second) # Output: The current second is  18
#
#
# import datetime
# datetime.datetime.today()
# datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
# print(datetime.datetime.today().weekday())
# # 4
#
#
# def get_workday():
#     import datetime
#     datetime.datetime.today()
#     datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
#     value = datetime.datetime.today().weekday()
#     if value == 0:
#         day = "Monday"
#     elif value == 1:
#         day = "Tuesday"
#     elif value == 2:
#         day = "Wedensday"
#     elif value == 3:
#         day = "Thursday"
#     elif value == 4:
#         day = "Friday"
#     elif value == 5:
#         day = "Saturday"
#     elif value == 6:
#         day = "Sunday"
#
#     if value < 4:
#         return True
#     else:
#         return False
#
# print(get_workday())

# for i  in range(10):
#     print("i")
# else:
#     print("dfd")


def removeDuplicates(nums):
    if not nums:
        return 0

    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1

print(removeDuplicates([1,2,3,4,1,2,10,20,10]))

