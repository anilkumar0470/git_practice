# list comprehension is a simple way to write a list
# when ever you are using append method , we can write list comprehension for the same
# syntax  is [expression iterable condition1 condition2]
# Example1
nums = [1,2,3,4,5,6]
result = []
for i in nums:
    i = i * 2
    result.append(i)
print(result)

# same with list comprehension we can write in one line
result1 = [i*2 for i in nums]
print(result1)

# Example2
list1 = ["hi", "good", "morning", "have", "a", "nice", "day"]
result2 = []
for element in list1:
    out = element.upper()
    result2.append(out)
print(result2)
# same with list comprehension can be like this
result3 = [j.upper() for j in list1]
print(result3)

# Example 3


def multiply_by_six(num):
    return num * 6


result4 = []
for k in nums:
    out1 = multiply_by_six(k)
    result4.append(out1)
print(result4)
# same with list comprehension
result5 = [multiply_by_six(l) for l in nums]
print(result5)

# Example 4
dict1 = [{"name": "anil"}, {"name": "kumar"}]
result6 = []
for m in dict1:
    result6.append(m["name"])
print(result6)

# same with list comprehension be like

result7 = [n["name"] for n in dict1]
print(result7)

# list comprehension with if
# [expression for i in iterable filter condition]
# only if condition always appear on right side
list2 = [1, 2, 3]
result8 = [i*5 for i in list2 if i == 3]
print(result8)

result9 = [i*5 for i in list2 if i > 1]
print(result9)

# list comprehension with if else
# [expression if condition else expression for i in iterable]
# if else will appear on left side only
result10 = [i*5 if i%2 ==0 else i*3 for i in list2]
print(result10)

# if else with if
# first right side if condition will be executed which is nothing but filter condition
# after the if else condition will be applicable for filtered output
list3 = [1,2,3,4,5,6,7,8,9]
result11 = [i*9 if i%6 == 0 else i*3 for i in list3 if i%3==0]
print(result11)

