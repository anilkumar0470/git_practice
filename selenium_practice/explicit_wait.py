# implicit wait will be applied for all elements of the script or entire page
# Before interacting with DOM or to find the element wait for given time .
# sometimes element may load or not , so still we have chance of
# failing the script . So we will use one wait method which is explicit wait where we will define the
# wait for all the required elements as individually.
# explicit wait work with particular element with help of condition so that we will wait for only that
# particular element by specifying any one of the condition.

# import basic statements
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # creating the driver object
# driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
# # driver.implicitly_wait(5)
#
# driver.maximize_window()
#
#
# driver.get("https://www.expedia.com/")
# time.sleep(5)
#
# # clicking on flights
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='uitk-tab-text'])[2]")))
# print(element)
# element.click()
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


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
#
#
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#
# driver.implicitly_wait(10)
#
# driver.get("https://www.expedia.com/")
#
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//a/span[contains(text(), 'Flights')]").click()
#
# import time
# time.sleep(15)
#
# element = "//div/div/div/label/span[@class='uitk-checkbox-label-content' and contains(text(), 'Non')]"
#
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# wait = WebDriverWait(driver, 10)
#
# some = wait.until(EC.element_to_be_clickable(element))
# some.click()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# driver = webdriver.get("https://login.upstox.com/")
#
# driver.find_element
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://login.upstox.com/")
# driver.find_element(By.ID, "mobileNum").send_keys("9581228818")

# wait = WebDriverWait(driver, 20)
# getotp_btn = driver.find_element(By.ID, "getOtp")
# element = wait.until(EC.element_to_be_clickable((By.ID, "getOtp")))
# element.click()
# import time
# time.sleep(1)
#
# ctnbtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "continueBtn")))
# ctnbtn.click()
# driver.quit()
# # driver.find_element()

import time

start_time = time.time()

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "getOtp")))
except:
    print(time.time()-start_time)

finally:
    driver.quit()




