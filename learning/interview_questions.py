import re


def replace_function(file_path, replaced_text):
    fd = open(file_path, 'r+')
    file_content = fd.readlines()
    new_string = ""
    for line in file_content:
        pattern = r'[d|D]og'
        match = re.sub(pattern, replaced_text, line, re.I)
        if match:
            new_string = new_string + match
    fd.seek(0)
    fd.write(new_string)
    fd.truncate()
    fd.close()
# replace_function("/home/test/Desktop/sample.txt", 'elephant')


def merge_sorted_list(list1, list2):
    final_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        else:
            final_list.append(list2[j])
            j += 1
    final_list = final_list + list1[i:] + list2[j:]
    return final_list

# print(merge_sorted_list([1,3, 6,7,8,], [2,5]))


# denos = sorted([100, 20, 5, 1, 2, 50, 10])
# n = len(denos)
# total = 888
# ans = []
#
# i = n-1
# while i >= 0:
#     while (total >= denos[i]):
#         total = total - denos[i]
#         ans.append(denos[i])
#     i = i - 1
#
# for i in range(len(ans)):
#         print(ans[i], end=' ')


def minimum_change(denos , total):
    n = len(denos)
    i = n - 1
    ans1 = []
    for ki in range(10):
        ans = []
        while i >=0:
            while total >= denos[i]:
                total = total - denos[i]
                ans.append(str(denos[i]))

            i = i -1
            ans1.append(ans)
    print(ans1)
print(minimum_change([1,2,3,4,5], 6))
print(minimum_change([1,2,3,4,5], 6))

str1 = 'mindtree is software company'

def get_max_char_occ(in_str):
   try:
      if len(in_str) == 0 or len(in_str) == 1:
         raise Exception("Length should be min. 2 chars")
      if type(in_str) != str:
         raise Exception("Data should be in string format")
      char_count = {}
      for char in in_str:
         if char == ' ':
            continue
         if char not in char_count.keys():
            char_count[char] = 1
         else:
            char_count[char] += 1
      print(char_count)
      max_char = max(char_count,key = lambda x :char_count[x])
      print("Char and its max occ : ", max_char, "---", char_count[max_char])
   except Exception as exec:
      print("Exception details : ",exec)

get_max_char_occ(str1)


