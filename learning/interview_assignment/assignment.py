# question 1

str1 = input("enter string1: ")
str2 = input("enter string2: ")
op1 = ""
op2 = ""
for ele in str1:
    if ele not in str2:
        op1 = op1 + ele
for char in str2:
    if char not in str1:
        op2 = op2 + char
print(op1)
print(op2)

# question 2

list1 = [["u1","u2"], ["u3","u4"], ["u1","u5"], ["u2","u1"], ["u3","u4"]]
list2 = []
for element in list1:
    if [element[1], element[0]] not in list2 and element not in list2:
        list2.append(element)
print(list2)
