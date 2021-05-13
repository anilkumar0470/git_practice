from decorators_import import test_decorator



@test_decorator
def display(name):
    print("user name is {}".format(name))

display("anil")