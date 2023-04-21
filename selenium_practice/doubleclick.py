# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
#
#
# driver = webdriver.Chrome(r"C:\Users\akumarpathap\Downloads\chromedriver.exe")

# driver.get("https://testautomationpractice.blogspot.com/")

# driver.maximize_window()
#
# click_element = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
#
# action = ActionChains(driver)
# action.double_click(click_element).perform()
#
# time.sleep(5)
# print(driver.title)
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")

element = driver.find_element(By.XPATH, "//button[contains(text(), 'Copy Text')]")


actions = ActionChains(driver)
actions.double_click(element).perform()

driver.close()