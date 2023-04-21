from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.makemytrip.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='fromCity']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//p[text()='Mumbai, India']").click()



