class Parent1:

    def method1(self):
        print("I am in method1")


class Parent2:
    def method1(self):
        print("I am in method1")

class Child(Parent1, Parent2):
    pass

# c = Child()
# c.method1()

# diamond problem
# class 1
# class 2(class 1) class3(class 1)
# class 4


class Class1:
    def m1(self):
        print("i am in class1 ")


class Class2(Class1):
    def m1(self):
        print("i am in class2 ")
        Class1.m1(self)


class Class3(Class1):
    def m1(self):
        print("i am in class3 ")
        Class1.m1(self)


class Class4(Class2, Class3):
    def m1(self):
        print("i am in class4 ")
        Class2.m1(self)
        Class3.m1(self)


# obj = Class4()
# obj.m1()

# when we use super instead of calling the parent class method
# then the output will change 


class Class1:
    def m1(self):
        print("i am in class1 ")


class Class2(Class1):
    def m1(self):
        print("i am in class2 ")
        super(Class2, self).m1()


class Class3(Class1):
    def m1(self):
        print("i am in class3 ")
        super(Class3, self).m1()

class Class5(Class1):
    def m1(self):
        print("i am in class 5")
        super(Class5, self).m1()


class Class4(Class2, Class3, Class5):
    def m1(self):
        print(Class4.mro())
        print("i am in class4 ")
        super(Class4, self).m1()
        # super(Class4, self).m1()


obj = Class4()
obj.m1()
