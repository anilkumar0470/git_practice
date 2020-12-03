# agenda is wait commands in selenium
# when you are trying to click on some element which not loaded yet , that time it will lead to
# no such element or element not visible and script will continue further which is called
# syncronization . To avoid the same we will use waits until that element loads.
# synchronization is the balancing between the code and response of the application
# one way we can make the application faster .. this is not in our hands
# second way we can pause our code  .. this we can do
# when ever we are looking for some element we will introduce some wait here.
# in webdriver we have two types of waits
# 1)implicit wait
# 2)explicit wait
# import basic statements
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\apathapa\Downloads\chromedriver.exe")

# launching the URL

driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
# lets say opening this page is taking some time
# so we want to wait for some time we will use implicit wait command
# implicit wait is applicable for all the elements of the script 
driver.implicitly_wait(5)

# assert driver.title == "YouTube", "youtube is not loaded"

driver.find_element_by_name("email").send_keys("anilkumar.0466@gmail.com")

driver.find_element_by_name("password").send_keys("8374851518@As")

driver.find_element_by_name("submit").click()