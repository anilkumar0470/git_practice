# # l = (x for x in range (1,10) if x%2==0)
# # print l
# # for i in l:
# #     print i
# #
# #
# # #square =[]
# # #for i in range(1,11):
# #    # if i ** 2%2 ==0:
# #        # square.append(i**2)
# # squares = [x **2  for x in range(1,11) if x %2 ==0]
# # print squares
#
# squares = [i**2 if i%2 == 0 else i*i*i for i in range(10)]
# print(squares)
#
# l = [11,22,11,33,22,11,0]
# ki = [l.count(i) for i in l if l.count(i) > 1 ]
# print(ki)
#
# squares_n = [i*i for i in range(10) if i%2 == 0]
# print(squares_n)
#
# out = [i**2 if i%2== 0 else i**3 for i in range(10)]
# print(out)
#
#
# # Implement a method to flatten a nested dictionary.  We can assume dictionary has strings as keys and a string or a nested dictionary as a value
# #  e.g d = {'k1' : 'v1', 'k2' : {'nk1' : 'v2', 'nk2' : {'nk3' : 'v3'}}}
# #  when given the above dictionary as an input it should return an output like this
# #  [('k1', 'v1'), ('k2nk1', 'v2'), ('k2nk2nk3', 'v3')]
# #  assume you are writing this method as a utility method that can be used by importing
#
#
# def process_nested_dict(new_dict, res_string=""):
#     out_list = []
#     for key, value in new_dict.items():
#         if type(value) == dict:
#             res_string = res_string + key
#             out_list.extend(process_nested_dict(value, res_string))
#         else:
#             if res_string:
#                 out_list.append(("{}{}".format(res_string, key), value))
#             else:
#                 out_list.append((key, value))
#     return out_list
#
#
# d = {'k1': 'v1', 'k2': {'nk1': 'v2', 'nk2': {'nk3': 'v3'}}}
# print(process_nested_dict(d))