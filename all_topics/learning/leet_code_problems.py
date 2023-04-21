# valid paranthese
valid_input1 = "{([])}"
invalid_input1 = "{[([)]]}"
def valid(s):
    new_list = []
    new_dict = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i in new_dict:
            if new_list and new_list[-1] == new_dict[i]:
                new_list.pop()
        else:
            new_list.append(i)

    if new_list:
        return False
    else:
        return True

# print(valid(valid_input1))

# sum of two numbers


input_list1 = [1, 3, 4, 5, 7, 10, 11]
target = 9


def sum_of_two_numbers(l1, expected_target):
    new_dict = {}
    for index, value in enumerate(l1):
        result = expected_target - value
        if result in new_dict:
            return new_dict[result], index
        else:
            new_dict.update({value: index})


# print(sum_of_two_numbers(input_list1, target))


def sum_of_sorted_numbers(l1, expected_target):
    r, l = 0, len(l1)-1
    while True:
        res = l1[r] + l1[l]
        if res > expected_target:
            l = l -1
        elif res < expected_target:
            r = r +1
        else:
            return [r+1, l+1]
# print(sum_of_sorted_numbers(input_list1, target))


def sum_of_three_numbers(input_list9):
    result = []
    input_list9.sort()
    for index, value in enumerate(input_list9):
        if index > 0 and value == input_list9[index-1]:
            continue
        l, r = index+1, len(input_list9)-1
        while l < r:
            three_sum = value + input_list9[l] + input_list9[r]
            if three_sum > 0:
                r = r - 1
            elif three_sum < 0:
                l = l + 1
            else:
                out = [value,  input_list9[l], input_list9[r]]
                result.append(out)
                if len(result) == 1:
                    break
    return result

input_list2 = [-66,1,2,4,5]
print(sum_of_three_numbers(input_list2))

# convert roman number to integer
def convert_roman_to_integer():
    valid_input2 = "CXIV"
    roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    res1 = 0
    for i in range(len(valid_input2)):
        if i+1 < len(valid_input2) and roman_dict[valid_input2[i]] < roman_dict[valid_input2[i+1]]:
                res1 = res1 - roman_dict[valid_input2[i]]
        else:
                res1 = res1 + roman_dict[valid_input2[i]]
    return res1
print(convert_roman_to_integer())

class Solution(object):
   def containsDuplicate(self, nums):
       """
       :type nums: List[int]
       :rtype: bool
       """
       for i in nums:
           if nums.count(i)> 1:
               return True
       else:
           return False