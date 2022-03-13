from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome(executable_path="C:\\Users\\pathapaa\\Downloads\\chromedriver.exe")
# # driver = webdriver.Firefox(executable_path=r"C:\Users\apathapa\Downloads\geckodriver.exe")
# driver.get("https://www.youtube.com/")

# # assert driver.title == "You Tube", "Title is wrong "
# print(driver.title) # to display the title of the page
# print(driver.current_url)# to display the url
# # print(driver.page_source)  # to disply html code
# driver.close()


# import sys
#
# b = sys.argv[2]
# print("yyy {}".format(sys.argv[2]))
# d = b.replace("\'", "\"")
# print(d)


# for i in range(10):
#     print(i)
# else:
#     print("rrr")
# l = [x * x for x in range(10)]
# print(l)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\\Users\\pathapaa\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.python.org")

assert "Python" in driver.title

ele = driver.find_element_by_name("q")
ele.clear()
import time
time.sleep(2)
ele.send_keys("pycon")
time.sleep(5)
# ele.send_keys(Keys.RETURN)
# time.sleep(5)
driver.find_element_by_name("submit").click()
time.sleep(5)
driver.close()