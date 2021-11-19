# list comprehenssion





list1 = [10,1,12,3,87,5,6,7,8,9,10]


# for i in range(len(list1)):
#     print(i, list1[i])

# for index,value in enumerate(list1):
#     # print(index)
#     # index_vale = index[0]
#     # actual_value = index[1]
#     # print(index_vale, actual_value)
#     print(index,value)


def sample():
    for i in range(10):
        if i%2==0:
            yield i
    print("sdfdfd")

s = sample()
# print(s)
# print(dir(s))
print(s)
print(s.__next__())




# new_list = []
# for i in range(len(list1)):
#     if i%2 == 0 and list1[i]%2==0:
#         new_list.append(list1[i] ** 2)
# print(new_list)
#
# var1 = [list1[j]**2 for j in range(len(list1)) if j%2==0 if list1[j]%2==0]
# print(var1)





















# # basic list comprehension
# new_list1 = [element ** 2 for element in list1]
# print(new_list1)
# # list comprehension with if example
# new_list2 = [j ** 2 for j in list1 if j%2 == 0]
# print(new_list2)
#
# # list comprehension with if  else example
new_list3 = [j ** 2 if j%2 == 0 else j**3 for j in list1]
print(new_list3)
#
# print(["Even" if i%2==0 else "Odd" for i in range(8)])
#
# # for prime numbers
# print([x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))])

l = [{"name":"name1", "age":"age1", "loc":"loc1"},{"name":"name1", "age":"age1", "loc":"loc1"}]
for ele in l:
    print(ele["age"])