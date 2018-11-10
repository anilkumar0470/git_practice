import unittest

from basic_example import multiply


class TestUnitTest(unittest.TestCase):

    def setUp(self):
        print("i am setup section")

    def test_multiply(self):
        assert multiply(3, 4) == 12


if __name__ == "main":
    unittest.main()
