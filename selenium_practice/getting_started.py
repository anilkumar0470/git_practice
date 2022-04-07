from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
driver.maximize_window()

driver.get("http://www.python.org")
assert "Python" in driver.title

element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)
import time
time.sleep(4)

driver.close()

