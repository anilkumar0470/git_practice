# agenda is to cover the conditional commands
# is_displayed() if we want to know some of the elements are displayed or not , some elements may take time
# to load
# is_enabled() to check those elements are enabled or not
# is_selected() check boxes are checked or un checked or for radio button also we will use the same
# import basic stuff
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# # creating driver object
# driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

# when u open any open any open page if u want to check some field is displaying or not and also the username
# field is enable or not.
# conditional methods always return true or False
# first we need to identify the element

# driver.get("https://www.facebook.com/")
# username = driver.find_element(By.NAME, "email")
# # username = driver.find_element_by_name("email")
# print(username.is_displayed())  # to check the specified element is presented or not
# print(username.is_enabled())  # to check specified element is enabled or not
#
#
#
# password = driver.find_element(By.NAME, "pass")
# print(password.is_displayed())  # to check whether the element is presented or not
# print(password.is_enabled())  # to check specified element is enabled or not
#
# username.send_keys("anilkumar.0466@gmail.com")
# password.send_keys("ANEELPATHAPATI")
#
# #
# driver.find_element(By.NAME, "login").click()
#
# assert "Facebook" in driver.title

# driver.get("https://www.makemytrip.com/")
#
# #
# one_way_element = driver.find_element(By.XPATH, "//li[@data-cy='roundTrip']")
#
# # is_selected() is used to check given element is selected or not
# print(one_way_element.is_selected())



#
# password = driver.find_element_by_name("pass")
# print(password.is_displayed())
# print(password.is_enabled())
#
# # sending username
# username.send_keys("anilkumar.0466@gmail.com")
# password.send_keys("ANEELPATHAPATI")
#
# button = driver.find_element_by_name("login")
# print(button.is_displayed())
# print(button.is_enabled())
# button.click()
#
# # button.is_selected() to check radio button is checked or not
# # css selector = tag[individual_attribute=value] Eg : "input[value=oneway]"
# # no need to mention quotations in inside the css selector


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://demo.guru99.com/test/newtours/")
#
# username_element = driver.find_element(By.NAME, "userName")
#
# print(username_element.is_displayed()) # true/False
# print(username_element.is_enabled()) # true/False
# username_element.send_keys("mercury")
#
# password_element = driver.find_element(By.NAME, "password")
#
# print(password_element.is_displayed())
# print(password_element.is_enabled())
# password_element.send_keys("mercury")
#
# driver.find_element(By.NAME, "submit").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[contains(text(), 'Flight')]").click()
# time.sleep(6)
# radio_btn_ele = driver.find_element(By.XPATH, "//input[@value='roundtrip']")
# print(radio_btn_ele.is_selected())
# driver.quit()


from selenium import webdriver


driver = webdriver.Chrome(executable_path="")

driver.get("https://login.upstox.com")


driver.find_element_by_id("mobilenumber")


driver.find_element_by_id("mobilenum")
driver.find_element_by_id("mobilenum")
driver.find_element_by_id("mobilenum")
driver.find_element_by_id("mobilenum")
driver.find_element_by_id("mobilenum")
# click


driver.quit()




















