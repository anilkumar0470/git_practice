list1 = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for i in list1:
    new_list.append(i ** 2)
print(new_list)

# basic list comprehension
new_list1 = [element ** 2 for element in list1]
print(new_list1)
# list comprehension with if example
new_list2 = [j ** 2 for j in list1 if j%2 == 0]
print(new_list2)

# list comprehension with if  else example
new_list3 = [j ** 2 if j%2 == 0 else j**3 for j in list1]
print(new_list3)

print(["Even" if i%2==0 else "Odd" for i in range(8)])

# for prime numbers
print([x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))])