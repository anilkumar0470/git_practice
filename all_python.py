# https://www.toptal.com/python/python-design-patterns
# https://restfulapi.net/http-status-codes/
# https://www.programiz.com/python-programming/methods/string/format
# https://docs.pylint.org/en/1.6.0/tutorial.html
# https://media.readthedocs.org/pdf/pytest/latest/pytest.pdf
# https://www.programiz.com/python-programming/set
# https://www.geeksforgeeks.org/multithreading-python-set-1/
# bubble_sort

def bubble_sort(list):
    for num in range(len(list) - 1, 0, -1):
        for index in range(num):
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp


list = [-2, 45, 0, 11, -9]
bubble_sort(list)
print(list)


# Singletone
class Pizza(object):
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price


class HamAndMushroomPizza(Pizza):
    def __init__(self):
        self._price = 10


class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 20


class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 30


class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "HamAndMushroomPizza":
            return HamAndMushroomPizza()
        elif pizza_type == "DeluxePizza":
            return DeluxePizza()
        elif pizza_type == "HawaiianPizza":
            return HawaiianPizza()


if __name__ == "__main__":
    print(PizzaFactory.create_pizza("DeluxePizza").get_price())


# single tone
class SingleTone:
    def __new__(cls):
        print("I am in __new__ magic method")
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleTone, cls).__new__(cls)
        return cls.instance

    def __init__(cls):
        print("I am in __init__ magic method")
        # if not hasattr(cls, 'instance'):
        #     cls.instance = super(SingleTone, cls).__new__(cls)
        # return cls.instance

    def samp(self):
        print("sampe")


# class SingleTone:
#
#     pass


s1 = SingleTone()
s1.samp()
s2 = SingleTone()


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
