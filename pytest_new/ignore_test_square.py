import pytest
import logging

class Test_Fixtures_Class:

    @pytest.fixture
    def logger(self):
        # logger = logging.getLogger("Test_Fixtures_Class")
        logging.basicConfig(level=logging.DEBUG)
        return logging
    def test_2(self,logger ):
        log = logging.getLogger('logger')
        log.debug("testing")




# import time
# import logging
#
# logging.basicConfig(level=logging.DEBUG)
#
#
# def test_1():
#     log = logging.getLogger('test_1')
#     time.sleep(1)
#     log.debug('after 1 sec')
#     time.sleep(1)
#     log.debug('after 2 sec')
#     time.sleep(1)
#     log.debug('after 3 sec')
#     assert 1, 'should pass'
#     log.info("test1 execution done")
#
#
# def test_2():
#     log = logging.getLogger('test_2')
#     time.sleep(1)
#     log.debug('after 1 sec')
#     time.sleep(1)
#     log.debug('after 2 sec')
#     time.sleep(1)
#     log.debug('after 3 sec')
#     #assert 0, 'failing for demo purposes'
#     log.info("test2 execution done")


#
# def test_print():
#     print("aaa")
#
# @pytest.mark.sample
# def test_info():
#     print("sss")
#
# @pytest.fixture
# def fixture_test():
#     """this is for testing"""
#     print("fixture testing")
#
# # def test_sample_fixture(take_input):
# #     print(take_input)
#
#
# def test_sample_fixture(fixturee_test):
#     print("wwww")