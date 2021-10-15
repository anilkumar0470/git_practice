s = "Please refer to the madam to know the level"
# s = "refer to dad"
# Input: S = “refer to dad”
# Output: dad to refer

# steps :
# write a function to know the palindrome or not
# append all the palindrome elements into one list
# replace the palindrome element with the palindrome element list after sorting based on index


def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


new_list = []
actual_list = s.split()

for word in actual_list:
    if is_palindrome(word):
        new_list.append(word)
j = 0
new_list.sort()
for i in range(len(actual_list)):
    if is_palindrome(actual_list[i]):
        actual_list[i] = new_list[j]
        j = j + 1
print(" ".join(actual_list))



# Given a list, write a Python program to swap first and last element of the list.
#
# Examples:
#
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
#
# Input : [1, 2, 3]
# Output : [3, 2, 1]

def swap_elements(list):

    temp = list[0]
    list[0] = list[len(list)-1]
    list[len(list)-1] = temp
    return list

# print(swap_elements([12,35,9,56,24]))
# print(swap_elements([1,2,3]))

# to find the minimum number in the list
# we can use sort then display the first index number or we can use min also

def minimum_number(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    print("smallest number is {}".format(min))


minimum_number(list = [11, 22, -333, 444, 5, 11, 32, 22])

def maximum_number(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    print("largest number is {}".format(max))


maximum_number(list = [11, 22, -333, 444, 5, 11, 32, 22])

def second_largest_number(list):
    max_number = max(list[0], list[1])
    sec_max_number = max(list[0], list[1])
    for i in range(2, len(list)):
        if list[i] > max_number:
            sec_max_number = max_number
            max_number = list[i]
        elif list[i] > sec_max_number and list[i] != max_number:
            sec_max_number = list[i]
    print("second largest number is {}".format(sec_max_number))


second_largest_number(list = [70, 11, 20, 4, 100, 7,87, 100])




