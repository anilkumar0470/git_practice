import pytest

@pytest.mark.adds
def test_add_two_numbers():
    assert 7+2 == 9

@pytest.mark.subs
def test_sub_two_numbers():
    assert 7-2 == 5