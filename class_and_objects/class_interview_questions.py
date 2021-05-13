class Testing:
    location = "Chundi"

    def __new__(cls, *args, **kwargs):
        print("ssss")
        return

    def __init__(self):
        pass

    def __str__(self):
        return "pass"



    @classmethod
    def test_class_method(cls, current_location):
        Testing.location  = current_location





t = Testing()
print(t)