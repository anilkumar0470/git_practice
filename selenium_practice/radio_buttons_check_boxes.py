# we can do two things on selenium
# first we can check checkbox or radiobutton is selected or not using is_selected()
# second select the checkbox or radio button using click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# working with radio buttons

# status = driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']").is_selected()
# print(" male radio button is {}".format(status))
# driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']").click()
# new_status = driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']").is_selected()
# print(" male radio button is {}".format(status))
# print(male_radio_button.is_selected())
# male_radio_button.click()
#

# working with checkboxes

driver.find_element(By.XPATH,"//input[@id='RESULT_CheckBox-8_0']").click() # sunday

driver.find_element(By.XPATH,"//input[@id='RESULT_CheckBox-8_3']").click() # wed

# import time
# time.sleep(4)
# # driver.find_element(By.ID, "RESULT_CheckBox-8_0").click()
# wait = WebDriverWait(driver, 1500)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='RESULT_RadioButton-7_0']")))
# driver.find_element(By.XPATH, "//input[@id='RESULT_RadioButton-7_0']").click()