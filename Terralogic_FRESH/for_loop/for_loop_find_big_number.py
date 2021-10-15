

list = [100,23,10,450,85,26,74,1000, 3000,22,334343]
# print(max(list))
# print(min(list))
# list.sort()
# print(list)
#
big = list[0] # 1000
for i in range(1,len(list)):  # range(1,11), [1,2,3,...10] , 1, 2, 3
    if big < list[i]: # 100 < 1000
        big = list[i] #
print ("Big number is :",big)

# range function
# for loop
# prime number
# big number in the gievn list
# small number in the given list
# prime numbers in the given range
# fibanocci series
# while loops




# big = list[0]
# for i in range(1, len(list)):
#     if big < list[i]:
#         big = list[i]
# print(big)

# small = list[0]
# for i in range(1, len(list)):
#     if small > list[i]:
#         small = list[i]
# print(small)


# l = [1,2,3,4,5,6,7]
#
# # three positons
#
# n = 3
# for i in range(n+1):
#    l.append(i)
#    l.remove(i)
# print(l)