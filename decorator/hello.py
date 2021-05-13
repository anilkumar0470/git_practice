from decoratos import new_decorator

@new_decorator
def display():
    print("displaying ..")
#display()

@new_decorator
def display_name(name):
    print("name is {}".format(name))
display_name(name="anil")