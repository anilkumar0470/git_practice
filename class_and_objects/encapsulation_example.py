class Employee:

    def __init__(self):
        self.name = "anil"
        self.__loc = "Bang"

    def display(self):
        print("name of the employee {} and location is {}".format(self.name, self.__loc))


emp = Employee()
emp.display()
print(emp._Employee__loc)


class Car:

    def __init__(self, name, millage):
        self.__name = name
        self.millage = millage

    def descritpion(self):
        return f'the {self.__name} car gives millage of {self.millage}km/l'


obj = Car("indica", 12)
print(obj.descritpion())

print(obj.millage)
print(obj._Car__name)
