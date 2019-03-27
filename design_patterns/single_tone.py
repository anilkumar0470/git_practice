# This is example for Single tone design pattern
# https://howto.lintel.in/python-__new__-magic-method-explained/
# Please refer the above link for the full context of __new__
# Single tone design patterns are used to create only one object for the class
# We can create multiple objects but still we will have only one object at a time


class SingleTOne:

    def __new__(cls, *args, **kwargs):
        print("I am in __new__ method")
        if not hasattr(cls, "instance"):
            cls.instance = super(SingleTOne, cls).__new__(cls)
        return cls.instance

    def __init__(self, name, age):
        print("I am in __init__ method")
        self.name = name
        self.age = age

    def display(self):
        print("name :{} age :{}".format(self.name, self.age))


s1 = SingleTOne("anil", 26)
print(s1)
s1.display()

s2 = SingleTOne("valli", 23)
print(s2)
s2.display()

