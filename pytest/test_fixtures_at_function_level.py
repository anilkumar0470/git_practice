# fixtures are simillar to functions we will use to do some operations in the initial it self.
# it is kind of setup which is used is to coneect some device orr connecting data base
# by default the scope of the fixture is function
# the scope of fixture can be function, module, session, and module

# Module: If the Module scope is defined, the fixture will be created/invoked only once per module.
# it will execute only once for file module is nothing but python file
#
# Class: With Class scope, one fixture will be created per class object.
#
# Session: With the Session scope, the fixture will be created only once for entire test session.
#  This is mainly used to manage Webdriver sessions and it will execute only once per entire execution
#
# Function: This is the default value for fixture scope and the fixture is executed/run once per test session.

# fixtures always execute from local file , if fixture is not availabe in current test file then it will look for
# conftest.py if available then it will execute the fixture else it will return error like fixture not available
# at scope as function level .. the fixture will be executed for each and every test

# if you see the output , the fixture will be executed once per each test case , so the generated numbers are not
# matching
import pytest
import random


@pytest.fixture(scope="function")
def generating_random_number():
    print("executing from current1   test  file ")
    return random.randint(0,10)


def test_fixture_at_function_level(generating_random_number):
    print(generating_random_number)


def test_fixture_at_function_level_example(generating_random_number):
    print(generating_random_number)


class Test_fixture_at_function_level:

    def test_fixture_at_function_level(self, generating_random_number):
        print(generating_random_number)

    def test_fixture_at_function_level_example(self, generating_random_number):
        print(generating_random_number)
