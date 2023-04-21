# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome(r"C:\Users\akumarpathap\Downloads\chromedriver.exe")
#
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
#
# driver.maximize_window()
#
# source_element = driver.find_element(By.XPATH, "//*[@id='box6']")
# target_element = driver.find_element(By.XPATH, "//*[@id='box106']")
#
# actions = ActionChains(driver)
# actions.drag_and_drop(source_element, target_element).perform()
#
# import time
# time.sleep(2)

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
source_element = driver.find_element(By.XPATH, "//*[@id='draggable']")
destination_element = driver.find_element(By.XPATH, "//*[@id='droppable']")

actions = ActionChains(driver)
actions.drag_and_drop(source_element, destination_element).perform()
driver.close()
