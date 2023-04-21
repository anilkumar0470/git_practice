# import time
#
# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.touch_action import TouchAction
#
#
#
#
# desired_caps = {}
# desired_caps['automationName'] = 'UiAutomator2'
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '13'
# desired_caps['deviceName'] = 'emulator-5554'
# desired_caps['app'] = ('/Users/anilkumar/Downloads/Android_Appium_Demo.apk')
# desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
# desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'
#
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#
# # scroll  -- android uiautomator with UiSelector with UiScrollable
# # element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
# #                               'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))')
# # element.click()
#
# # actions = TouchAction(driver)
# # print(dir(actions))
# # actions.long_press(element, 3)
# # actions.perform()
#
# element = driver.find_element(MobileBy.ID, "com.skill2lead.appiumdemo:id/ScrollView")
# element.click()
# time.sleep(1)
#
# for i in range(10):
#     touch = TouchAction(driver)
#     import random
#     random_num = random.randint(1500, 1743)
#     print(random_num)
#     touch.press(x=481, y=random_num).move_to(x=481, y=796).release().perform()
#     time.sleep(2)
#
# # time.sleep(2)
#
# driver.quit()
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
# desired_caps = {}
# desired_caps['automationName'] = 'UiAutomator2'
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '13'
# desired_caps['deviceName'] = 'emulator-5554'
# desired_caps['app'] = ('/Users/anilkumar/Downloads/Android_Appium_Demo.apk')
# desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
# desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

# mCurrentFocus=Window{1ce4509 u0 com.android.contacts/com.android.contacts.activities.PeopleActivity}

desired_caps = {}
desired_caps["deviceName"] = "emulator-5554"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = '13'
desired_caps["appPackage"] = "com.android.contacts"
desired_caps["appActivity"] = "com.android.contacts.activities.PeopleActivity"


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(3)
# for i in range(4):
element = driver.find_element(MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
element.click()
time.sleep(2)
touch = TouchAction(driver)
touch.tap(x=963, y=2160).perform()
time.sleep(2)
element2 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First name")')
element2.send_keys("test2")

element3 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Last name")')
element3.send_keys("test2")

element4 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone")')
element4.send_keys("9879879871")

touch.tap(x=126, y=2264).perform()
time.sleep(2)

element4 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("More fields")')
element4.click()
time.sleep(2)

touch.press(x=413, y=2070).move_to(x=411, y=1250).release().perform()
time.sleep(2)

element5 = driver.find_element(MobileBy.ID, "com.android.contacts:id/editor_menu_save_button")
element5.click()
time.sleep(2)

driver.quit()


