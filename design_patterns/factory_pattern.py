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
