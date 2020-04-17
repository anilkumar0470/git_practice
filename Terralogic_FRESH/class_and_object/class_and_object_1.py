#Basic example for class
class Student():
    # initializer
    def __init__(self):
        print "good morning to  every one"
    # methods
    def std_details(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print "Name:",self.name,self.age
#creating object
s = Student()
print s
print id(s)
#calling methods  by using .dot operator
s.std_details("anil",23)
s.display()
