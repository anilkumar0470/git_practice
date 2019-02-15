# import fileutil
#
#
# def get_file_info(full_fname):
#     file_path = fileutil.get_path(full_fname)
#     return file_path
#
#
# filename = __file__
# filename_path = get_file_info(filename)
# print('path = {}'.format(filename_path))
#
# class sample_hello():
#     def __init__(self,name):
#         print(" i am in hello",name)
# class sample_hai():
#     def __init__(self):
#         print("i am in hai")
# a = "hello"
# b = "hela"
# c = eval("sample_{}(b)".format(a))
#
#
#
# class s :
#     def __init__(self,name):
#         pass
# ss = s('apathapa')
#
# import re
# pattern = r'(\d+)-(\d+)-(\d+)'
# start_date = "1-1-2018"
# end_date = "11-11-2019"
# file_names = ["sample_hello-10-10-2018", "sample1_hello-12-12-2019"]
# for file in file_names:
#     match = re.search(pattern, file)
#     date = match.group(1)
#     month = match.group(2)
#     year = match.group(3)
#
#     #if int(start_date.split("-")[2]) <= int(year) <= int(end_date.split("-")[2]):
#     #if month > start_date.split("-")[1] and month < end_date.split("-")[1]:
#     import pdb
#     pdb.set_trace()
#     if start_date.split("-")[1] <= int(month) <= end_date.split("-")[1]:
#         import pdb
#         pdb.set_trace()
#         if start_date.split("-")[0] < int(date) < end_date.split("-")[0]:
#             print "aa"
#         else:
#             print("date")
#     else:
#         print("month")

# print("apathapa")
# sequence = ["d","c","b","a","h","g","f","e","l","k","j","i","p","o","n","m","t","s","r","q","x","w","v","u","z","y"]
# words = ["apple","cat","cba","dog","ball","eat","girl","fish","hand","hen","gun","anil","junk"]
# actual_list = []
#
# for letter in sequence:
#     tem_list = []
#     for word in words:
#         if word.startswith(letter):
#             tem_list.append(word)
#     actual_list.append(tem_list)
# print(actual_list)
# for index in range(len(actual_list)):
#     if len(actual_list[index]) > 1:
#         print("kk")
#         import pdb
#         pdb.set_trace()
#         current_list = actual_list[index]
#         #actual_list[index].sort()
#         repl_list = []
#         for letter in sequence:
#             for cl in current_list:
#                 if cl[0].startswith(letter):
#                     repl_list.append(cl)
#         actual_list.remove(current_list)
#         actual_list.insert(index,repl_list)
#
# print(actual_list)
# # sorted(words, key=sequence.index(sequence[0]))
# # print(words)
# # list = [word for letter in sequence for word in words if word.startswith(letter)]
# # print(words.sort(reverse=True))
# # print(list)


# import requests
# from requests.exceptions import HTTPError
# urls = ["https://api.github.com","https://api.twitter.com/","https://twitter.com/pawankalyan"]
# for url in urls:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as htp_err:
#         print("http error occured {}".format(htp_err))
#     except Exception as e:
#         print("any other error occured {}".format(e))
#     else:
#         print("success")
#         #print response.json()
# requests.post('https://httpbin.org/post', data={'key':'value'})

# import requests
# response = requests.post("https://httpbin.org/post", json={"name": "anil"})
# print(response)
# json_response = response.json()
# import pdb
# pdb.set_trace()
# print(json_response["data"])

import requests
response = requests.post("https://httpbin.org/post", json={"name": "anil"})
print(response.request.url)
print(response.request.body)

from getpass import getpass
response = requests.get("https://api.github.com/user", auth=("apathapa-warrior", getpass()))
print(response)