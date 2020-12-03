# implicit will be applied for all elements of the script
# and we are keeping static time , some times element may load or not , so still we have chance of
# failing the script . So we will use one wait method which is explicit wait where we will define the
# wait for all the required elements as individually.

# import basic statements
import time
from selenium import webdriver

# creating the driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\apathapa\Downloads\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window() # to maximize the window

driver.get("https://www.expedia.co.in/?pwaLob=wizard-flight-pwa")
time.sleep(5)

driver.find_element_by_id("location-field-leg1-origin").send_keys("SFO")
import sys

driver.close()