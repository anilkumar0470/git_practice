# class Testing:
#     location = "Chundi"
#
#     def __new__(cls, *args, **kwargs):
#         print("ssss")
#         return cls
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return "pass"
#
#     @classmethod
#     def test_class_method(cls, current_location):
#         Testing.location  = current_location
#
#     @staticmethod
#     def sample_method():
#         print("sdfdsfd")
#
#
#
#
#
#
# t = Testing()
# print(t)


class Sample:

    count = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Sample.count += 1

    def display_details(self,):
        print(self.name, self.location)

    @classmethod
    def display_count(cls):
        print(cls.count)

    @staticmethod
    def sample_method():
        print(Sample.count)


s1 = Sample("anil", "chu")
s1.display_details()
s1.display_count()
s1.sample_method()

