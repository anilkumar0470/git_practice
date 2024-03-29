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

print(merge_sorted_list([1,3, 6,7,8,], [2,5]))
