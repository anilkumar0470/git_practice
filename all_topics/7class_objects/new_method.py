class MyClass:
    def __new__(cls, *args, **kwargs):
        print("creating instance")
        return super(MyClass, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print("object is initializing")

import pdb
pdb.set_trace()
m = MyClass()
