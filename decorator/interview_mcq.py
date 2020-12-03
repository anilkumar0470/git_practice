class Vehicle(object):
    def __init__(self):
        print("AA")

class Car(Vehicle):
    def __init__(self):
        print("BB")

class RacingCar(Car):
    def __init__(self):
        print("CC")

# mycar = RacingCar()

class Vehicle(object):
    def __init__(self, model):
        self.engine = model

class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init_()

class RacingCar(Car):
    def __init__(self):
        super(RacingCar,self).__init__()
# mycar = RacingCar("Ferrari Enzo")
# print(mycar.engine)


class Vehicle(object):
    def __init__(self):
        self.val = 1

class Car(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init_()
        self.val += 2

class Bike(Vehicle):
    def __init__(self):
        super(Vehicle,self).__init__()
        self.val += 3

# mybike = Bike()
# mycar = Car()
# print(mycar.val,mybike.val)


class Vehicle(object):
    def __init__(self):
        self.name = "v"

class Car(Vehicle):
    def __init__(self):
        self.name = "c"

class Bike(Vehicle):
    pass

# mybike = Bike()
# mycar = Car()
# print(mycar.name, mybike.name)


class Vehicle(object):
    __val = 1
    def __init__(self):
        self.val = 1

class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init_()
        self.__val += 2

class Bike(Vehicle):
    def __init__(self):
        super(Bike,self).__init__()
        self.__val += 3

# mybike = Bike()
# mycar = Car()
# print(mybike.__val)

class Meta(object):
    def __init__(self):
        pass

class SteelCompany(Meta):
    def __init__(self):
        pass
class Automobile(SteelCompany):
    def __init__(self):
        pass

# print(issubclass(Automobile, object))
# print(issubclass(Automobile, Meta))
# print(issubclass(Meta, Automobile))
# print(issubclass(Meta, object))


def getval():
    global num
    num = 123
    print("sdff interviewmaq.pu {}".format(num))
# getval()

class Vehicle(object):
    val = 1
    def __init__(self):
        pass

class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init_()
        Vehicle.val += 2

class RacingCar(Car):
    def __init__(self):
        super(RacingCar,self).__init__()
        Vehicle.val += 3
    def display(self):
        print(Vehicle.val)
# mycar = RacingCar()
# mycar.display()

str1 = "hello world junk"
print(len(str1))
print(len(str1.split()))