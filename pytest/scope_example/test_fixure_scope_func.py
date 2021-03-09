import pytest
import random
@pytest.fixture(scope='function')
def generate_random_number():
    return random.randint(10,20)

def test_random_number_1(generate_random_number):
    print(generate_random_number)

def test_random_number_2(generate_random_number):
    print(generate_random_number)


class Test_random_number_at_function_level():

    def test_random_number1(self, generate_random_number):
        print(generate_random_number)

    def test_random_number2(self, generate_random_number):
        print(generate_random_number)