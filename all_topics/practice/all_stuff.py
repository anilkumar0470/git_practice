# # # decorators
# #
# # # def sample_decorator(original_function):
# # #     def wrapper_function():
# # #         print("wrapper will be executed first")
# # #         original_function()
# # #
# # #     return wrapper_function
# #
# # # typical way
# # # def say_hi():
# # #     print("hi saying")
# # #
# # # say_hi = sample_decorator(say_hi)
# # # say_hi()
# #
# # # standard way
# # # @sample_decorator
# # # def say_hi():
# # #     print("say hi")
# # #
# # # say_hi()
# #
# # # decorator taking arguments with returning
# #
# # # def sample_decorator(original_function):
# # #     def wrapper_function(name):
# # #         print("wrapper will be executed first")
# # #         out = original_function(name)
# # #         return out.upper()
# # #     return wrapper_function
# # #
# # # @sample_decorator
# # # def say_hi(name):
# # #     return name
# # #
# # # print(say_hi("Anil"))
# #
# #
# # # def my_generator():
# # #     print("good afternoon")
# # #     yield 1
# # #
# # #     print("good evening ")
# # #     yield 2
# # #
# # #     print("good ni8")
# # #     yield 3
# #
# # #
# # # gen_obj = my_generator()
# # # print(next(gen_obj))
# # # print(next(gen_obj))
# # # print(next(gen_obj))
# # # # print(next(gen_obj))
# # #
# # # def generate_even_number():
# # #
# # #     for i in range(100):
# # #         if i%2 == 0:
# # #             yield i
# # #
# # # my_gen_obj = generate_even_number()
# # # while True:
# # #     try:
# # #         print(next(my_gen_obj))
# # #     except StopIteration:
# # #         break
# #
# #
# # import logging
# # import threading
# # import time
# #
# # # def thread_function(name):
# # #     logging.info("Thread %s: starting", name)
# # #     time.sleep(2)
# # #     logging.info("Thread %s: finishing", name)
# # #
# # # if __name__ == "__main__":
# # #     format = "%(asctime)s: %(message)s"
# # #     logging.basicConfig(format=format, level=logging.INFO,
# # #                         datefmt="%H:%M:%S")
# # #
# # #     logging.info("Main    : before creating thread")
# # #     x = threading.Thread(target=thread_function, args=(1,), daemon=True)
# # #     logging.info("Main    : before running thread")
# # #     x.start()
# # #     logging.info("Main    : wait for the thread to finish")
# # #     x.join()
# # #     logging.info("Main    : all done")
# #
# # # print('\n'.join([''.join([('Engineer'[(x-y)%8 ] if((x*0.05)**2 + (y*0.1)**2-1)**3 - (x*0.05)**2*(y*0.1)**3<=0 else ' ') for x in range(-30,30)]) for y in range(15,-15,-1)]))
# # # primes = range(2, 20)
# # # for i in range(2, 8):
# # #     primess = filter(lambda x: x == i or x % i, primes)
# # #     print(dir(primess))
# # #
# # # def count_numbers(num):
# # #     x = num
# # #     count = 0
# # #     while x:
# # #         x = x // 10 # x//= 10
# # #         count = count + 1 # count += 1
# # #     return count
# # #
# # # print(count_numbers(123456784))
# # #
# # #
# # # def reverse_number(nn):
# # #     result = 0
# # #     while nn:
# # #         res = nn % 10
# # #         result = result * 10 + res
# # #         nn = nn//10
# # #     return result
# # #
# # # print(reverse_number(123))
# # #
# # #
# # # def sample_recursive(count):
# # #     if count > 0:
# # #        print("good evening")
# # #        sample_recursive(count-1)
# # #
# # # sample_recursive(5)
# #
# # config_file = ["__Switch1A|Switch1B__",
# # "portA:enabled=true",
# # "portB:vlan=10",
# #  "portC:vlan=200",
# #  "__Switch2__",
# #  "portA:poe=false",
# #  "portA:speed=100mbps",
# #  "portB:vlan=15",
# #  "__Switch4A|Switch4B|Switch4C__",
# #  "portB:speed=10mbps",
# #  "portD:enabled=false",
# #  "__Switch3__",
# #  "portA:use_lldp=false"]
# #
# # port_mappings = ["__Switch1A|Switch1B__",
# #   "portA:memberA_port3",
# #   "portB:memberB_port27",
# #    "portC:memberA_port14",
# #     "__Switch3__",
# #     "portA:port2",
# #     "__Switch2__",
# #     "portA:port4",
# #     "portB:port15",
# #     "__Switch4A|Switch4B|Switch4C__",
# #     "portD:memberA_port9",
# #     "portB:memberC_port22"]
# # #
# # print("expected:",["__Switch1A|Switch1B__", "memberA_port3:enabled=true", "memberB_port27:vlan=10", "memberA_port14:vlan=200", "__Switch2__", "port4:poe=false", "port4:speed=100mbps", "port15:vlan=15", "__Switch4A|Switch4B|Switch4C__", "memberC_port22:speed=10mbps", "memberA_port9:enabled=false", "__Switch3__", "port2:use_lldp=false"])
# #
# # def combine_arrays(config_file, port_mappings):
# #
# #     if len(config_file)-1 == len(port_mappings):
# #
# #         out_list = {}
# #         main_line= ""
# #         for line in port_mappings:
# #             if line.startswith("_"):
# #                 main_line = line
# #                 out_list.update({line: []})
# #             else:
# #                 if main_line:
# #                     out_list[main_line].append(line)
# #
# #         for line in config_file:
# #             if line.startswith("_"):
# #                 main_line = line
# #             else:
# #                 out_list[main_line].append(line)
# #         final_list = []
# #
# #         for key, value in out_list.items():
# #             # flag = False
# #             # if key == "__Switch3__":
# #             #     temp2_list.append(key)
# #             #     flag = True
# #             # if flag:
# #             #     temp_dict = {}
# #             #     for element in value:
# #             #         firstvalue, second_value = element.split(":")
# #             #
# #             #         if firstvalue not in temp_dict:
# #             #             temp_dict.update({firstvalue: second_value})
# #             #         else:
# #             #             final_out = "{}:{}".format(temp_dict[firstvalue], second_value)
# #             #             temp2_list.append(final_out)
# #             # else:
# #                 final_list.append(key)
# #                 temp_dict = {}
# #                 for element in value:
# #                     firstvalue, second_value = element.split(":")
# #
# #                     if firstvalue not in temp_dict:
# #                         temp_dict.update({firstvalue: second_value})
# #                     else:
# #                         final_out = "{}:{}".format(temp_dict[firstvalue], second_value )
# #                         final_list.append(final_out)
# #         # final_list.extend(temp2_list)
# #
# #         return final_list
# #     else:
# #         return "fdfd"
# #
# # # print(combine_arrays(config_file, port_mappings))
# #
# #
# # def common_prefix():
# #     input_list = ["flower", "fly", "flight"]
# #     res = ""
# #     for i in range(len(input_list[0])):
# #         for j in input_list:
# #             if input_list[0][i] != j[i]:
# #                 return res
# #         res = res + input_list[0][i]
# #
# # print(common_prefix())
# #
# # input_string = "/a//b//c//////d"
# # out = []
# # for element in input_string.split("/"):
# #     # print(element)
# #     if element == "..":
# #         if out:
# #             # print("2222")
# #             out.pop()
# #     elif element == ".":
# #         pass
# #     elif element:
# #         out.append(element)
# # print("/{}".format("/".join(out)))
#
#
# # def mutliply(a,b, bound):
# #     result = a * b
# #     if result <= bound:
# #         return result
# #     else:
# #         raise ValueError("multiplication of {} and {} with bound {} not possible")
#
#
# #
# # # import re
# # import re
# #
# # test = "good evening Everyone"
# # out = ""
# # for element in test.split():
# #     res = re.sub("^[a-z]", "", element)
# #     print(res)
# # for element in str1.split():
# #     p1 = "(^[a-z])"
# #     m1 = re.search(p1, element)
# #     if m1:
# #         e1 = re.sub(p1, m1.group().upper(), element)
# #         out = out + e1 + " "
# #     elif re.search("[A-Z]", element):
# #         out = out + element + " "
# # print(out)
#
# # import re
# # str2 = "cat hi cat hello cat cow"
# #
# # # res = re.sub("(cat(?=\scow))", "tiger", str2)
# # # print(res)
# # str3 = re.sub("cat(?=\scow)", "tiger", str2)
# # print(str3)
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
# str1 = "raj"
# print(str1)
#
# if str1 == "king":
#     print("matched")
# else:
#     print("not matched")
# print("bye")
#
# a = 15
# assert a >= 18, "age must be 18"
# print("2222")
#
#
#
#
#
#
#
# i = 1
# i++
#
#
#
#
#
#
#
#
#

# def f(a, b=1, c=2):
#     print("a is ", a, "b is :",b, "c is :",c)
# f(2, c=2)
# f(c=100, a=110)
#
# s = "sting"
# out = ""
#
# for i in s:
#     out = i + out
# print(out)


# target = "1234"
# print(type(int(target))  == int)
# print(target.isdigit())

def validate(target):

    if target.startswith("0") or target.startswith("."):
        return False
    else:
        return True

print(validate("33.1234"))
strs = ["eat","tea","tan","ate","nat","bat"]
Output = [["bat"],["nat","tan"],["ate","eat","tea"]]

# out = []
# for element in strs:
#     temp_list = []
#     for i in range(1, len(strs)-1):
#         if sorted(element) == sorted(strs[i]):
#             if element not in temp_list:
#                 temp_list.append(element)
#             if strs[i] not in temp_list:
#                 temp_list.append(strs[i])
#     if temp_list not in out:
#         out.append(temp_list)
# print(out)

# res = {}
# for s in strs:
#     count = [0] * 26
#
#     for c in s:
#         count[ord(c) - ord("a")] += 1
#     res[tuple(count)].append(s)
# print(res.values())

l1 = [1,1,1,2,2,3]
k = 2
out = {}
for element in l1:
    out.update({element: l1.count(element)})
print(out)
print(sorted(out.values()))
for key, value in out.items():
    if value <= k:
        print(key, value)




print("h")





