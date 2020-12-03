# agenda is to cover the conditional commands
# is_displayed() if we want to know some of the elements are displayed or not , some elements may take time
# to load
# is_enabled() to check those elements are enabled or not
# is_selected() check boxes are checked or un checked or for radio button also we will use the same
# import basic stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# creating driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\apathapa\Downloads\chromedriver.exe")

# when u open any open any open page if u want to check some field is displaying or not and also the username
# field is enable or not.
# conditional methods always return true or False
# first we need to identify the element

driver.get("https://www.facebook.com/")
username = driver.find_element_by_name("email")
print(username.is_displayed())  # to check the specified element is presented or not
print(username.is_enabled())  # to check specified element is enabled or not

password = driver.find_element_by_name("pass")
print(password.is_displayed())
print(password.is_enabled())

# sending username
username.send_keys("anilkumar.0466@gmail.com")
password.send_keys("ANEELPATHAPATI")

button = driver.find_element_by_name("login")
print(button.is_displayed())
print(button.is_enabled())
button.click()

# button.is_selected() to check radio button is checked or not
# css selector = tag[individual_attribute=value] Eg : "input[value=oneway]"
# no need to mention quotations in inside the css selector

