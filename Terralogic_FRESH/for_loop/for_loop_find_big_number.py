list = [23,10,45,85,26,74]
# big = list[0]
# for i in range(1,len(list)):
#     if big < list[i]:
#         big = list[i]
# print "Big number is :",big

# big = list[0]
# for i in range(1, len(list)):
#     if big < list[i]:
#         big = list[i]
# print(big)

small = list[0]
for i in range(1, len(list)):
    if small > list[i]:
        small = list[i]
print(small)