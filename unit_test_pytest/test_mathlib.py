import mathlib
import pytest
import sys
import unittest


def test_add():
    total = mathlib.add(5, 4)
    assert total == 9


def test_mul_dummy():
    total = mathlib.mul(5, 4)
    assert total == 20

def test_dummy():
    print ("apathapa")

if __name__ == '__main__':
    print ("papap")
    log_file = 'log_file.txt'
    f = open("sample.txt", "w")
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()