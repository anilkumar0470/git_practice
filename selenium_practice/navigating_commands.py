# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome(executable_path=r"/Users/anilkumar/Downloads/chromedriver")
# driver.maximize_window()
#
# driver.get("http://www.google.com")
#
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'/Users/anilkumar/Downloads/chromedriver')
driver.get("http://www.upstox.com")

# maximize the window
driver.maximize_window()

print(driver.title)

driver.quit() # to close all windows
driver.close() # to quit only current window
