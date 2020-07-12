# def test_alpha_1():
#     print('\nIn test_alpha_1()')
#
#
# def test_alpha_2(some_resource):
#     print('\nIn test_alpha_2()')

# def test_fixture_at_module_level_1(scope_of_fixture_at_module_level):
#     print(scope_of_fixture_at_module_level)
#
# def test_fixture_at_module_level_2(scope_of_fixture_at_module_level):
#     print(scope_of_fixture_at_module_level)

class Test_1():


    def test_fixture_at_class_level_1(self, scope_of_fixture_at_class_level):
        print(scope_of_fixture_at_class_level)
        print("class test1 class level_1")

    def test_fixture_at_class_level_2(self, scope_of_fixture_at_class_level):
        print(scope_of_fixture_at_class_level)
        print("class test1 class level_2")


class Test_2():

    def test_fixture_at_class_level_3(self, scope_of_fixture_at_class_level):
        print(scope_of_fixture_at_class_level)
        print("class Test2 class level3 ")