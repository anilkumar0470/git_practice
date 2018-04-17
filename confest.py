# import pytest
#
#
# def pytest_addoption(parser):
#     parser.addoption("--testing", action="true",help="testing pytest")
#
# @pytest.fixture(autouse=True)
# def base_instance_setup(request):
#
#     config = request.config
#
#     if getattr(config.option, "testing", None):
#         junk= config.getoption("--testing")


import pytest

def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1",
        help="my option: type1 or type2")

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")