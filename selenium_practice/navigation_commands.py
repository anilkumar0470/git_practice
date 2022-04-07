# Agenda navigation commands
# let say u open a company website , after that u click social accounts like twitter or facebook,
# then the page will be redirected to another page . Again if you want to go back to previous page
# we will use navigation commands

# importing basic needs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# creating driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")


# navigating to URL
driver.get("http://demo.automationtesting.in/Windows.html")
import time
time.sleep(5)

# displaying the title
print(driver.title)

# displaying current ulr
print(driver.current_url)

# clicking element

driver.find_element(By.XPATH, "//a/button[@class='btn btn-info']").click()

# closing the window it will always closes the current or focused window

driver.close()

time.sleep(5)

# if you want to close all windows use quit method
driver.quit()





# # to navigate to url
# driver.get("https://www.youtube.com/")
#
# print(driver.title) # to get title of the page
#
# # to navigate to another url
# driver.get("http://www.pavantestingtools.com/")
# time.sleep(5)
#
# print(driver.title)  # to get the title of the page
#
# driver.back()  # to go back to previous page
# time.sleep(5)
# print(driver.title)  # tours as output
#
# driver.forward()  # to go back to the next page
# time.sleep(5)
# print(driver.title)


# driver.get("https://accounts.lambdatest.com/register/")
#
# ele = driver.find_element_by_xpath("//input[@id='name']")
# ele.click()
# ele.send_keys("ddd")