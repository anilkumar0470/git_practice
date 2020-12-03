class Testing:
    location = "Chundi"

    def __init__(self):
        pass

    def __str__(self):
        return "{}".format(self.__class__)

    @classmethod
    def test_class_method(cls, current_location):
        Testing.location  = current_location





t = Testing()
