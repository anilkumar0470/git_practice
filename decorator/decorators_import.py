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