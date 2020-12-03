import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Users\Apathapa\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://site21.way2sms.com/content/index.html?")
time.sleep(5)
#assert "Python" in driver.title
elem = driver.find_element_by_css_selector("#username")
elem.clear()
elem.send_keys("8123210095")
elem2 = driver.find_element_by_css_selector("#password")
elem2.send_keys("7067")
driver.find_element_by_css_selector("#loginBTN").click()
time.sleep(5)
driver.find_element_by_css_selector("#sendSMS > a").click()
elem3 = driver.find_element_by_css_selector("#mobile")
elem3.send_keys("8884313888")
#assert "No results found." not in driver.page_source
#driver.close()