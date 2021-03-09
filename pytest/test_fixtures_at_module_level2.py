# in class level it will execute only once per class

class Test_fixtures_at_class_level_1:

    def test_scope_class_1(self, generating_random_number_in_module_level):
        print(generating_random_number_in_module_level)

    def test_scope_class_2(self, generating_random_number_in_module_level):
        print(generating_random_number_in_module_level)


class Test_fixtures_at_class_level_2:

    def test_scope_class_1(self, generating_random_number_in_module_level):
        print(generating_random_number_in_module_level)

    def test_scope_class_2(self, generating_random_number_in_module_level):
        print(generating_random_number_in_module_level)