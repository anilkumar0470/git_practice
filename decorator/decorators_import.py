def test_decorator(original_function):
    def test_wrapper(*args, **kwargs):
        print("i am inside wrapper function")
        return original_function(*args, **kwargs)
    return test_wrapper

# @test_decorator
# def display():
#     print("testing")
#
# display()


list1 = [10, 30, 90, 60, 50, 65]
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            # temp = list1[i]
            # list1[i] = list1[j]
            # list1[j] = temp
            list1[i], list1[j] = list1[j], list1[i]

print(list1)