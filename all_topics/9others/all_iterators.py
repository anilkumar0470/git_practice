# https://www.programiz.com/python-programming/iterator

# https://www.youtube.com/watch?v=jTYiNjvnHZY
# An iterator is nothing but it will remember the state where it is paused and it must implement two methods called
# __iter__ and __next__
# In python most of the data types like string, list, tuple, dictionary and set are iterables but not iterators
# All iterators are iterables but all iterables not iterators

new_list = [1, 4, 7, 9]
print(dir(new_list))

# when we see output of dir(list) it will contains __iter__ only which means that we can do only iteration on it.
# And it will not remember the state where it is paused , to get the same we will apply iter method that list
# so that it will become iterator
iter_new_list = iter(new_list)
print(dir(iter_new_list))
# if we see the output of dir() it will have __iter__ and __next__ both thunder methods.
# now this variable will remember the state where it is paused and when you call next time it will continue from there.
print(next(iter_new_list))
# for loop will implement iterator concept while fetching the elements like this
# while True:
#     try:
#         element = next(iter_new_list)
#         print(element)
#     except StopIteration:
#         break

# # define a list
# my_list = [4, 7, 0, 3]
#
# # get an iterator using iter()
# my_iter = iter(my_list)
#
# # iterate through it using next()
#
# # Output: 4
# print(next(my_iter))
#
# # Output: 7
# print(next(my_iter))
#
# # next(obj) is same as obj.__next__()
#
# # Output: 0
# print(my_iter.__next__())
#
# # Output: 3
# print(my_iter.__next__())
#
# # This will raise error, no items left
# # next(my_iter)


class MyRange:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

nums = MyRange(1, 10)
for num in nums:
    print(num)


def my_range(start, end):
    current = start
    while current < end :
        yield current
        current += 1

new_nums = my_range(10,20)
print(next(new_nums))
print(next(new_nums))
print(next(new_nums))
print(next(new_nums))


# when you are writing iterator you must implement two methods __iter__ and __next__
class NewRange:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


new_range = NewRange(100, 110)
for new_ele in new_range:
    print(new_ele)



class OldRange:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


old_iter = OldRange(23, 45)
for iterm in old_iter:
    print(iterm)
