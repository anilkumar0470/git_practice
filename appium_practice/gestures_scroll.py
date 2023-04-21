from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {}
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '13'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = ('/Users/anilkumar/Downloads/Android_Appium_Demo.apk')
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# WebDriverWait takes total four arguments
# webdriver object: driver
# max wait in seconds : 10
# polling frequency time in seconds
# Exceptions which should ignored

# example for explicit wait

# wait = WebDriverWait(driver=driver, timeout=10)
# element = wait.until(EC.presence_of_element_located((MobileBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")))
# element.click()

# scroll -- android uiautomator with UiScrollable with UiSelector

element1 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("ScrollView")')
element1.click()
time.sleep(2)

element2 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                               'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON15"))')
element2.click()
time.sleep(2)
driver.quit()
