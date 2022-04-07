import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
time.sleep(3)
print(driver.title)

driver.get("http://pavantestingtools.blogspot.in")
time.sleep(3)
print(driver.title)

driver.back()  # going back to previous url
time.sleep(3)
print(driver.title)

driver.forward()
time.sleep(3)
print(driver.title)

driver.close()