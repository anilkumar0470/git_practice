import pytest
import random
# fixtures scopes are function, class, session, module

@pytest.fixture
def take_input():
    """this is for testing in confest"""
    input_a = 38
    return input_a

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


def pytest_addoption(parser):
    parser.addoption("--user_input", action="store", default="10", help="this is  for testing ")
    parser.addoption("--user_age", action="store", help="age of the student")
    parser.addoption("--user_name", action="store", help="name of the user ")


@pytest.fixture
def user_name(request):
    return request.config.getoption("--user_name")

@pytest.fixture
def user_input(request):
    return request.config.getoption("--user_input")

@pytest.fixture
def user_age(request):
    return request.config.getoption("--user_age")


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

#
# @pytest.fixture(scope="session", autouse=True)
# def my_own_session_run_at_beginning(request):
#     print('\nIn my_own_session_run_at_beginning()')
#
#     def my_own_session_run_at_end():
#         print('In my_own_session_run_at_end()')
#
#     request.addfinalizer(my_own_session_run_at_end)


# @pytest.fixture(scope="session")
# def some_resource(request):
#     print('\nIn some_resource()')
#
#     def some_resource_fin():
#         print('\nIn some_resource_fin()')
#
#     request.addfinalizer(some_resource_fin)

@pytest.fixture(scope="session")
def generating_random_number_in_module_level():
    print("executing from conftest  file ")
    return random.randint(0,10)

@pytest.fixture(scope="module")
def generating_random_number_in_session_level():
    print("executing from conftest  session file ")
    return random.randint(0,10)


@pytest.fixture(scope="class")
def generating_random_numbero():
    print("executing from conftest  file ")
    return random.randint(0,100)


@pytest.fixture(scope="session")
def scope_of_fixture_at_module_level():
    import random
    return random.randint(0,10)

@pytest.fixture(scope="class")
def scope_of_fixture_at_class_level():
    import random
    return random.randint(0,10)