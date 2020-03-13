# normal function to return the square for each number
def square_numbers(list):
    result = []
    for i in list:
        result.append(i * i)
    print(result)
square_numbers([1,2,3,4,5])

# lets use generator
def square_generator(list):
    for i in list:
        yield i * i
generator_object  = square_generator([1,2,3,4,5])
# next is used to fetch the next number once elements are over it will return stop iteration error
# print(generator_object)
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))
# print(next(generator_object))
for num in generator_object:
    print(num)

def square_generator(list):
    for i in list:
        yield i * i
generator_object  = square_generator([1,2,3,4,5])

# list comprehenssion
f = [i*i for i in [1,2,3,4,5]]
print(f)

#genertor by using list comprehenssion

k = (i*i for i in [1,3, 5, 7])
print(list(k))
for l in k :
    print(l)