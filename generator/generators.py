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
