# in class level it will execute only once per class 

import pytest
import random

# @pytest.fixture(scope='class')
# def generate_random_number():
#     return 10
#
# class Test_sample:
#     def test_hello1(self, generate_random_number):
#         print(generate_random_number)
#
#
@pytest.fixture(scope='module')
def generating_random_number_eee():
    print("executing from test file ")
    return random.randint(100, 200)

class Test_fixtures_at_class_level_1:

    def test_scope_class_1(self, generating_random_number_eee):
        print(generating_random_number_eee)

    def test_scope_class_2(self, generating_random_number_eee):
        print(generating_random_number_eee)


class Test_fixtures_at_class_level_2:

    def test_scope_class_1(self, generating_random_number_eee):
        print(generating_random_number_eee)

    def test_scope_class_2(self, generating_random_number_eee):
        print(generating_random_number_eee)