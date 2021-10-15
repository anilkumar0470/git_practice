# Basic example for class
# class Student():
#     # initializer
#     def __init__(self):
#         print ("good morning to  every one")
#     # methods
#     def std_details(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print ("Name:",self.name,self.age)
# #creating object
# s = Student()
# print (s)
# print (id(s))
# #calling methods  by using .dot operator
# s.std_details("anil",23)
# s.display()

# self is an instance of that class which is used to carry the data between the methods i.e we can
# use the varibales of one method in another method ..

class Sample:

    def __init__(self,anemme,nnns):
        print("dfd")

    def sample_function1(self):
        print(" i am in sample method 1")

    def sample_function2(self):
        print(" i am in sample method 2")

# test object = new test();
# var_name/reference_name = classname

# s = Sample()
# s.sample_function1()
# s.sample_function2()



class TestClass:

    def __init__(self, name, loc, mob):
        self.name = name
        self.loc = loc
        self.mob = mob

    def display_details(self):
        print(self.name, self.loc, self.mob)


t = TestClass("sub", "kad", "34343")
# print(t)
t.display_details()






