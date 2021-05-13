# destructor will automatically call once the execution is done
class Sample:

    def __init__(self):
        print("object initialized")

    def __del__(self):
        print("object destructed")


    def display(self):
        print("sample method")

s = Sample()
s.display()
