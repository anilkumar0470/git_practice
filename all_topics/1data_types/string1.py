# Python program to find the longest word in a sentence
sentence = "be confident and be yourself testinggg"

max_len = ""
d = {}
for word in sentence.split():
    if not max_len:
        max_len = len(word)
    else:
        if len(word) >= max_len:
            max_len = len(word)
            d.update({word: len(word)})
print(d)

# Capitalize repeated characters in a string
# input_str = "geeks for geeks"
input_str = "programming language"
out_str = ""
for character in input_str:
    if input_str.count(character) > 1:
        out_str = out_str + character.upper()
    else:
        out_str = out_str + character
print(out_str)

# Capitalize repeated characters in a string
out_dict = {}
for character in input_str:
    if character in out_dict:
        out_dict[character] = out_dict[character] + 1
    else:
        out_dict[character] = 1
ans = ""
for character in input_str:
    if out_dict[character]>1:
        character = character.upper()
    ans = ans + character
print(ans)

# Consecutive characters frequency
input_str1 = "geekksforgggeeks"
import re
match_obj = re.finditer(r"(\w)\1*", input_str1)
# print(match_obj)
for sub in match_obj:
    print(sub.group(), len(sub.group()))

#Convert String to matrix having K characters per row

input_str2 = "GeeksforGeeks "
k = 7
out_list = []
temp_list = []
for value in input_str2:
    if len(temp_list) == k:
        out_list.append(temp_list)
        temp_list = []
    temp_list.append(value)
else:
    # if temp_list:
        out_list.append(temp_list)
print(out_list)

# Python – All substrings Frequency in String
input_str3 = "ababa"
out_dict1 ={}
for iii in range(len(input_str3)):
    for jjj in range(1, len(input_str3)+1):
        if input_str3[iii:jjj]:
            out_dict1.update({input_str3[iii:jjj]: input_str3.count(input_str3[iii:jjj])})
print(out_dict1)

#Python – Maximum Consecutive Substring Occurrence
input_str4 = "geeksgeeks are geeks for all geeksgeeksgeeks"
out_dict2 = {}
for ij in range(len(input_str4)):
    for ijk in range(len(input_str4)):
        if input_str4[ij:ijk]:
            test_str = input_str4[ij:ijk]
            match_obj1 = re.finditer(r"({})\1+".format(test_str), input_str4)
            if match_obj1:
                for mm in match_obj1:
                    # print(mm.group())
                    out_dict2.update({mm.group(): len(mm.group())})
# print(out_dict2)
max_string = max(out_dict2.values())

for k,v in out_dict2.items():
    if v == max_string:
        print(k)