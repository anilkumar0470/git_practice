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

    return False if new_list else True

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


strs = ["eat","tea","tan","ate","nat","bat"]
output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


def group_of_anagrams(strs):
    res = {}
    for element in strs:
        count = [0] * 26
        for c in element:
            count[ord(c)-ord("a")] = count[ord(c)-ord("a")] + 1
        if tuple(count) not in res:
            res.update({tuple(count): []})
        res[tuple(count)].append(element)
    return list(res.values())


# print(group_of_anagrams(strs))

def check_k_frequent_element():
    list12 = [1,1,1,2,2,2,4,4,4,4,3]
    freq = [[] for i in range(len(list12))]
    print("freq is",freq)
    count = {}
    for i in list12:
        count[i] = 1 + count.get(i, 0)
    print("count is ", count)
    for n, c in count.items():
        freq[c].append(n)
    print("freq after update",freq)
    res = []

    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == 2:
                return res


print(check_k_frequent_element())

list1 = [100, 4, 200, 3, 2, 1]


def longest_consecutive_sequence(list1):
    nums = set(list1)
    longest = 0
    for n in nums:
        if n-1 not in nums:
            length = 0
            while (n+length) in nums:
                length += 1
            longest = longest if longest > length else length
    return longest

# print("www", longest_consecutive_sequence(list1))


nums = [1, 2, 3, 4]
res = 1
out = []
for i in range(len(nums)):
    res = 1
    for j in range(len(nums)):
        if i != j:
            res = res * nums[j]
    out.append(res)

print(out)



