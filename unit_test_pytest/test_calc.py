import unittest
import calc
import pytest


class TestCalc(unittest.TestCase):

    @pytest.mark.skip(reason="Testing")
    def add(self):
        result = calc.add(10,5)
        self.assertEqual(result,5)

if __name__ == "__main__":
    unittest.main()