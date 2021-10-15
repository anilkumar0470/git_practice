# t = ((1,2),(2,3),(3,4))
#
# print(sum(n for n,i in t ))

#
# def sum(a, b):
#     c = a + b
#     return c
#
#
# print(sum(10,200))

# inheritance




# single level

# multi level # parent -- child1 -- child2

# multiple inheritance

class Parent1:
    def __init__(self):
        print("i am in parent class")

    # def display_parent(self):
    #     print("i am in parent1 display method")

class Parent2:

    def display(self):
        print("i am in child display method")

    def display_parent(self):
        print("i am in parent2 display method")

class Child(Parent1, Parent2):
    def display(self):
        print("i am in child display method")
# c = Child()
# c.display_parent()






class Sample:

    def __init__(self):
        print("i am init")

    # instance methods
    def display(self):
        print("i am in display method")


# s = Sample() # object creation
# s.display() # calling the methods

# method overriding


class Parent:
    def __init__(self):
        print("i am init")

    def display(self):
        print("i am in display parent method")


class Child(Parent):

    def __init__(self):
        print("i am in child init")

    def display(self):
        print("i am in child display method")
        # super().display()

# c = Child()
# c.display()



# instance variables
# class variables



class Employee:
    employee_count = 0

    def __init__(self, name, loc):
        self.name = name
        self.loc = loc
        Employee.employee_count += 1

    def display_details(self):
        print(self.name, self.loc)

    @classmethod
    def display_count(cls):
        print(Employee.employee_count)

Employee.display_count()

e1 = Employee("anil", "loc")
e1.display_details()

e2 = Employee("Sub", "kad")
e2.display_details()

e2 = Employee("Anu", "kad")
e2.display_details()

Employee.display_count()







str  = "Hai good Morning @Subhasini "

# 12
# at least oen upper case
# at least oen lower case
# @ # $














