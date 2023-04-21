#https://www.programiz.com/python-programming/generator
def my_generator():
    print("first item")
    yield 10

    print("second item")
    yield 20

    print("third item")
    yield 30


my_func = my_generator()
print(next(my_func))
print(next(my_func))
print(next(my_func))
# print(next(my_func))

def generator_with_for_loop_even_number():
    for i in range(100):
        if i%2 == 0 :
            yield i


new_fun = generator_with_for_loop_even_number()

# always use while loop to retrieve the same
# for j in range(100):
#     try:
#         print (next(new_fun))
#     except StopIteration:
#         break

while True:
    try:
        print(next(new_fun))
    except StopIteration:
        break


# def remove_dup(a):
#    i = 0
#    while i < len(a):
#       j = i + 1
#       while j < len(a):
#          if a[i] == a[j]:
#             del a[j]
#          else:
#             j += 1
#       i += 1
# s = [11,34,45,1,2,3,4,5,2,3,2,23,4,1,2,3,23,1,2]
# remove_dup(s)
# print(s)