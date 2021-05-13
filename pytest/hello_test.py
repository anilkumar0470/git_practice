# import math
# #
# # def test_sqrt():
# #    num = 25
# #    assert math.sqrt(num) == 5
# #
# # def testsquare():
# #    num = 7
# #    assert 7*7 == 40
# #
# # def tesequality():
# #    assert 10 == 11
#
#
# class Testsample():
#    def test_hello(self):
#       print("sss")
#
# class Testsample_1():
#    def test_hello(self):
#       print("sss")
#       assert True

import logging
import pytest

class Test_log_level:

   @pytest.fixture
   def logger_fixture(self):
       logging.basicConfig(filename="newfile.log",
                           format='%(asctime)s %(message)s',
                           filemode='w')
       log = logging.getLogger(__name__)
       log.setLevel(logging.DEBUG)
       return log
   def test_we(self, logger_fixture):
      self.log = logger_fixture
      self.log.debug("this is first test case")

















