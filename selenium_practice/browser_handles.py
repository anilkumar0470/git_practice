# each and every browser window have unique 16 digit id , which is used to switch between
# the windows.Let say when we click on some button it will open a new tab, in this case
# the control always stays in the parent tab
# parent tab -- where the button click happened
# child tab -- newly opened tab after button click
# now i want to some operation on the newly opened tab but still the contorl on
# parent tab only .
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
#
# driver.get("http://demo.automationtesting.in/Windows.html")
#
# driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
#
# print(driver.current_window_handle) # it will print current window
#
# handles = driver.window_handles
# print("all existing handles are {}".format(handles))
#
# for handle in handles:
#     print(handle)
#     # to switch to that browser handle
#     driver.switch_to.window(handle)
#     # to close specific browser based on the title
#     if driver.title == "Frames & windows":
#
#         # print(handle)
#         # print(driver.title)
#         # print(driver.current_window_handle)
#         driver.close()
#
# # to close all the browser
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

import time
time.sleep(5)
handles = driver.window_handles
print(handles)
for handle in handles:
    import pdb
    driver.switch_to.window(handle)
    if driver.title == "Selenium":
        break

print(driver.current_window_handle)

driver.quit()