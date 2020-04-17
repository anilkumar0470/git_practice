import re
# Valid email ID
# Description
# Consider that email IDs are supposed to be for the following format:
# username@website.extension.
# Here, there are three conditions to keep in mind:
# 1. The username can only contain characters 0-9, a-z and A-Z.
# 2. The website name can contain only characters a-z
# 3. The extension can have 2 or 3 alphabets(a-z).
#
# Given an email ID, you have to determine if it is valid or not.
#
# Sample Input:
# prerna@upgrad.com
#
# Sample Output:
# valid

str = "prerna@upgrad.com"
pattern = r"[A-Za-z0-9]+\@[a-z]\.([a-z]){2,3}"
pattern = "^[A-Za-z0-9]+\@[a-z]+\.([a-z]){2,3}"
match =  re.search(pattern, str)
if match:
    print( "Valid")
else:
    print("invalid")

# Flatten a list
# Description
# Given a nested list, write python code to flatten the list.
# Note: The input list will strictly have 2 levels, i.e. the list will be of the form [[1,2],[3,4]]. Inputs like
# [1,[2,3]] and [[1,[2,3],4],5] are not applicable.
#
# For example: If the input list is :
# [[1,2,3],[4,5],[6,7,8,9]]
# Then the output should be:
# [1,2,3,4,5,6,7,8,9]

l = [[1,2,3],[4,5],[6,7,8,9]]
new_list =  []
def is_list(element):
    for ele in element:
        new_list.append(ele)
for i in l :
    if type(i) == list:
        is_list(i)
    else:
        new_list.append(i)
print(new_list)


# Squares
# Description
# Given a list of positive integers, you have to find numbers divisible by 3 and replace them with their squares.
# For example, consider the list below:
# Input: [1,2,3,4,5,6]
# The output for the above list would be: [1,2,9,4,5,36]. Because 3 and 6 were divisible by 3, these numbers were
# replaced with their squares.
# Execution Time Limit
# Default.
input_list =  [1,2,3,4,5,6]
new_list = []
for i in input_list:
    if i%3 == 0 :
        new_list.append(i * i)
    else:
        new_list.append(i)
print(new_list)


n = 9
sum  = 0
l = []
for i in range(4):
    l.append(n)
    print(l)



# ['a', 'c', 'd']
# def is_ascii_value(char1, char2):
#     ascii_char1 = ord(char1)
#     ascii_char2 = ord(char2)
#     if ascii_char1 > ascii_char2:
#         return char2
#     else:
#         return char1
#n = 2
n = 2
sample_input = "aabbccc"
d = {}
mi = None

for element in sample_input:
    d.update({element:sample_input.count(element)})
print(d)
sorted_values = sorted(d.values())
sorted_values_one = sorted_values[len(sorted_values)-n : ]
print("sorted list {}".format(sorted_values_one))
non_s_li = sorted_values[:len(sorted_values)-n]
print("non sorted list {}".format(non_s_li))
for i in non_s_li:
    if i in sorted_values_one:
        chars = []
        for k,v in d.items():
            if v == i:
                chars.append(k)
                sorted_values.remove(v)
        char_values = []
        for i in chars:
            char_values.append(ord(i))
        mi = min(char_values)
print("mi ", mi)
new_dict =  []
for k, v in d.items():
    for value  in sorted_values_one:
        if value ==  v :
            new_dict.append(k)
        break
if mi:
    print("kk")
    character = chr(mi)
    new_dict.append(character)
print(sorted(new_dict))


if mi :
    pass
elif(mi=="junk"):
    pass
