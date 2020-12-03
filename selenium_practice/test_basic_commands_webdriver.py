# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\apathapa\Downloads\chromedriver.exe")
#



import pytest
import random

class Test_sample:

    @pytest.fixture(scope="class")
    def generate_random(self):
        return  random.randint(1,10)


    def test_fix_fun_level(self, generate_random):
        print(generate_random)


    def test_fix_fun_level_1(self, generate_random):
        print(generate_random)







