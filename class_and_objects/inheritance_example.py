class Parent:

    def __init__(self, name="Anil"):
        print(" i am in parent init")
        self.name = name

    def display(self):
        print("i am in parent")


class Child(Parent):
    def __init__(self):
        print("i am in child init")
        Parent.__init__(self)


# c = Child()
# c.display()
# print(c.name)

# single level inheritance above example is single level
# multiple inheritance  when child class inherits multiple parents then it is called multiple inheritance


class Base1:
    def __init__(self):
        self.str1 = "Base1 class"
        print("Parent1")


class Base2:
    def __init__(self):
        self.str2 = "Base2 class"
        print("Parent2")


class Derived(Base1, Base2):
    def __init__(self):
        self.str3 = "Child class"
        print("Child")
        Base1.__init__(self)
        Base2.__init__(self)

    def display(self):
        print(self.str1)
        print(self.str2)
        print(self.str3)


obj = Derived()
obj.display()

# multilevel inheritance when we have child and grand child


class Parent:
    def __init__(self):
        print(" i am in parent")


class Child1(Parent):
    def __init__(self):
        print("i am in child1")
        Parent.__init__(self)


class Child2(Child1):
    def __init__(self):
        print("i am in Child2")
        Child1.__init__(self)

c = Child2()