# Agenda navigation commands
# let say u open a company website , after that u click social accounts like twitter or facebook,
# then the page will be redirected to another page . Again if you want to go back to previous page
# we will use navigation commands

# importing basic needs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# creating driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\apathapa\Downloads\chromedriver.exe")

# to navigate to url
driver.get("https://www.youtube.com/")

print(driver.title) # to get title of the page

# to navigate to another url
driver.get("http://www.pavantestingtools.com/")
time.sleep(5)

print(driver.title)  # to get the title of the page

driver.back()  # to go back to previous page
time.sleep(5)
print(driver.title)  # tours as output

driver.forward()  # to go back to the next page
time.sleep(5)
print(driver.title)