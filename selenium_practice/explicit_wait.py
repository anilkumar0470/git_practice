# implicit wait will be applied for all elements of the script or entire page
# Before interacting with DOM or to find the element wait for given time .
# some times element may load or not , so still we have chance of
# failing the script . So we will use one wait method which is explicit wait where we will define the
# wait for all the required elements as individually.

# import basic statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# creating the driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
# driver.implicitly_wait(5)

driver.maximize_window()


driver.get("https://www.expedia.com/")
time.sleep(5)

# clicking on flights
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='uitk-tab-text'])[2]")))
print(element)
element.click()
# driver.find_element(By.XPATH, "(//span[@class='uitk-tab-text'])[2]").click()

                            #" (//input[@class='gNO89b'])[2]"

# # entering source
# driver.find_element(By.XPATH, "//input[@id='location-field-leg1-origin']").send_keys("Bangalore")

# entering destination
# driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']").send_keys("Bangalore")

# driver.find_element(By.XPATH, "(//button[@class='uitk-fake-input uitk-form-field-trigger'])[2]").send_keys("Bangalore")

#
# # clicking flights button
# flights_ele = driver.find_element(By.CSS_SELECTOR, "span[class='uitk-tab-text']")
# print(flights_ele.is_displayed())
# print(flights_ele.is_enabled())
# # flights_ele.click()
# time.sleep(5)
#
# # clicking on source
# #
# import pdb
# # pdb.set_trace()
# driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[1]/button").send_keys("Hello")


