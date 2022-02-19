# import pytest
#
#
# def test_hi():
#     print("hii")
#
# class Test_hello:
#
#     def test_hel(self):
#         print("rrr")
#
import pytest
@pytest.mark.parametrize("a,b",[(3,3),(5,5)])
def test_sample_parameter(a,b):
    assert a ==b
