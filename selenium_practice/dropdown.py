# select one option
# to get  all the options
# how many options count
# in dropdown we can do many things
# select one option
    # select based on text
    # select based on index
    # select based on value tag in the DOM
# get all available options
# get the no of available options
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
#
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#
# drp_btn = driver.find_element(By.ID, "RESULT_RadioButton-9")
# drp = Select(drp_btn)
# # select by visible text
# drp.select_by_visible_text("Morning")
# # select by index number index start from 0
# # drp.select_by_index(2)
# # select by value attribute in html
# drp.select_by_value("Radio-2")
# #
# # # drop down count
#
# print(len(drp.options))
# # capture all the options in drop down
# all_options = drp.options
# for option in all_options:
#     print(option.text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
#
#
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#
#
#
# drp_button = Select(driver.find_element(By.ID, "RESULT_RadioButton-9"))

# select based on visibility of the text
#drp_button.select_by_visible_text("Morning")

# select based on the index

#drp_button.select_by_index(2)

# select based on the value

# drp_button.select_by_value("Radio-2")

# wait = WebDriverWait(driver, 10)
#
# element = wait.until(EC.presence_of_element_located((By.NAME, "Submit")))
#
# element.click()

# get all available options

# print(len(drp_button.options))
# for option in drp_button.options:
#     print(option.text)
#
# import time
# time.sleep(3)
# driver.quit()
# #//tag[contains(text(), "")]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drp_button = driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-9']")

drop_down = Select(drp_button)

drop_down.select_by_visible_text("Evening")

# drop_down.deselect_all()

import time
time.sleep(3)
drop_down.select_by_index(1)
time.sleep(3)
drop_down.select_by_value("Radio-1")
time.sleep(3)

print(len(drop_down.options))
for option in drop_down.options:
    print(option.text)

driver.close()