sample_input = [1,2,[3,4,5],[[6]]]
output = [1,2,3,4,5,6]

empty_list = []

def list_extraction(new_list=[], empty_list=[]):

    for i in new_list :
        if type(i) == list:
            list_extraction(i)
        else:
            empty_list.append(i)
    return empty_list


print(list_extraction(sample_input))


def sample(a, test_list=[]):
    if test_list != []:
        test_list =[]
    test_list.append(a)
    print(test_list)

sample(10)
sample(20)
sample(30)


#
# # def sample_function(a, b):
# #     for i in range(len(a)):
# #        for j in range(1,len(a)):
# #
# #            if a[i] + a[j] == b:
# #                print(a[i], a[j])
# #
# # sample_function([1,2,3,4], 5)
#
#
# #
# # def sample_decorator(original_function):
# #     def test_wrapper(*args, **kwargs):
# #         print("i am inside wrapper")
# #         original_function(*args, **kwargs)
# #
# #     return test_wrapper
# #
# # @sample_decorator
# # def display(a):
# #     print("i am inside display function {} ".format(a))
# #
# # display(10)
#
#
# # l1 =  [1,3,4,7,8]
# # l2 =  [2,5]
# # # [1,2,3,4,5,7,8,9]
# #
# # new_list = []
# #
# # for i in range(len(l1)):
# #     for j in range(len(l2)):
# #         if l1[i] > l2[j] < l1[i+1]:
# #             new_list.append()
#
#
#
# # def list_sorted_func(a,b):
# #     final_list = []
# #     i, j = 0, 0
# #     while a[i] > :
# #
# #     return final_list
# # print(list_sorted_func([1,3,4,7,8], [2,5]))
#
# import re
#
#
# def replace_function(file_path, replaced_text):
#     fd = open(file_path, 'r+')
#     file_content = fd.readlines()
#
#     new_string = ""
#     for line in file_content:
#         print(line)
#
#         pattern = r'[d|D]og'
#
#         match = re.sub(pattern, replaced_text, line, re.I)
#         if match:
#             new_string = new_string + match +"\n"
#     fd.seek(0)
#     fd.write(new_string)
#     fd.truncate()
#     fd.close()
#
# # replace_function("/home/test/Desktop/sample.txt", 'elephant')
#
#
# def replace_function(file_path, replaced_text):
#     fd = open(file_path, 'r')
#     file_content = fd.readlines()
#     fd1 = open(file_path, 'w')
#
#     for line in file_content:
#         print(line)
#
#         pattern = r'[d|D]og'
#
#         match = re.sub(pattern, replaced_text, line, re.I)
#         if match:
#             print(match)
#             fd1.write(match)
#
#
# # replace_function("/home/test/Desktop/sample.txt", 'elephant')
#
#
# # using naive method
# # to combine two sorted lists
#
# def merge_sorted_list(list1, list2):
#     final_list = []
#     i, j = 0, 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             final_list.append(list1[i])
#             i += 1
#         else:
#             final_list.append(list2[j])
#             j += 1
#     final_list = final_list + list1[i:] + list2[j:]
#     return final_list
#
# # print(merge_sorted_list([1,3, 6,7,8], [2,5]))
#
#
# # Python | Inserting item in sorted list maintaining orderPython | Inserting item in sorted list maintaining order
#
# test_list = [1, 2, 3, 6,7]
# k = 8
# for i in range(len(test_list)):
#     print(test_list[i], k)
#     if test_list[i] > k:
#         position = i
#         break
# else:
#     position = len(test_list)
# print(position)
# test_list.insert(position, k)
# print(test_list)
#
# test_list1 = [1,3,5,6,7,10]
# test_list2 = [2,4,8,9]
#
# i, j = 0, 0
# res = []
# while i < len(test_list1) and j < len(test_list2):
#     if test_list1[i] < test_list2[j]:
#         res.append(test_list1[i])
#         i += 1
#     else:
#         res.append(test_list2[j])
#         j = j + 1
# print(res + test_list1[i:] + test_list2[j:])
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


import subprocess

p1 = subprocess.run(["cat", "sample.txt"], capture_output=True, text=True)
# print(p1.stdout)

p2 = subprocess.run(["grep", "-inr", "elephant"], stdout=subprocess.PIPE, text=True, input=p1.stdout)
print(p2.stdout)