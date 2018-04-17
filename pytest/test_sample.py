from sconfest import cmdopt, pytest_addoption
import pytest
pytest.set_trace()

def test_answer(cmdopt):
    if cmdopt == "type1":
        print ("first")
    elif cmdopt == "type2":
        print ("second")
    assert 0 # to see what was printed

