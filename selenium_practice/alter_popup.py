# working alert/popup
# alret is kindof popup , once  it is avilable we cannot select any element in the webpage.
# first we have to accept the alret or cancel the popup then u will be able to select the
# element in webpage
# we cannot identifiy any element in popup and there are two buttons in alret window
# okay button and cancel button
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

print(dir(driver))
# switch to is a method a switch to alert and if you want to click on okay use accept method
#
# driver.switch_to.alert.accept()
# driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
#
# time.sleep(5)
# # if you want click on cancel use dismiss
driver.switch_to.alert.dismiss()