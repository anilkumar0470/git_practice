from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# creating driver object for Chrome browser
# executable_path is an argument it will take location of driver file including the extension.
driver = webdriver.Chrome(executable_path=r"C:\Users\apathapa\Downloads\chromedriver.exe")

driver.get("https://www.youtube.com/") # get() is used to navigate to particular url or given url


assert driver.title == "YouTube", "Not able to navigate to youtube" # title is used to get the title of the website

print(driver.current_url)  # current_url to display the current URL

print(driver.page_source)  # to display the html code

driver.close() # close() is used to close the browser

# # launching on the Mozilla by giving the location og gecko driver including extension
# driver = webdriver.Firefox(executable_path=r"C:\Users\apathapa\Downloads\geckodriver.exe")
#
# # get() to navigate to particular URL
# driver.get("https://www.youtube.com/")
#
# # title is used to display title of the website
# print(driver.title)
#
# # close() is used to close the browser
#
# driver.close()


