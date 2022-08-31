# decorators

# def sample_decorator(original_function):
#     def wrapper_function():
#         print("wrapper will be executed first")
#         original_function()
#
#     return wrapper_function

# typical way
# def say_hi():
#     print("hi saying")
#
# say_hi = sample_decorator(say_hi)
# say_hi()

# standard way
# @sample_decorator
# def say_hi():
#     print("say hi")
#
# say_hi()

# decorator taking arguments with returning

# def sample_decorator(original_function):
#     def wrapper_function(name):
#         print("wrapper will be executed first")
#         out = original_function(name)
#         return out.upper()
#     return wrapper_function
#
# @sample_decorator
# def say_hi(name):
#     return name
#
# print(say_hi("Anil"))


def my_generator():
    print("good afternoon")
    yield 1

    print("good evening ")
    yield 2

    print("good ni8")
    yield 3


gen_obj = my_generator()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
# print(next(gen_obj))

def generate_even_number():

    for i in range(100):
        if i%2 == 0:
            yield i

my_gen_obj = generate_even_number()
while True:
    try:
        print(next(my_gen_obj))
    except StopIteration:
        break


