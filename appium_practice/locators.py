# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# import time
# desired_cap = {
#   "platformName": "Android",
#   "appium:deviceName": "8a88e220",
#   "appium:app": "/Users/anilkumar/Downloads/universal.apk"
# }
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# driver.implicitly_wait(18)
# inner_text = driver.find_element(MobileBy.ID, "in.upstox.app:id/inputLabelText").text
# assert inner_text == "Enter mobile number"
#
#
# wait = WebDriverWait(driver, 20)
# mob_field = wait.until(EC.presence_of_element_located((MobileBy.ID, "in.upstox.app:id/inputTextLineField")))
# mob_field.send_keys("9581228818")
# # driver.find_element_by_id("in.upstox.app:id/inputTextLineField").send_keys("9581228818")
# time.sleep(2)
# driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.Button").click()
# time.sleep(10)


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time
# desired_caps['platformName'] = 'Android'
# desired_caps['automationName'] = 'UiAutomator2'
# desired_caps['platformVersion'] = '10'
# desired_caps['deviceName'] = 'Pixel3XL'
# desired_caps['app'] = ('/Appium_Demo_App/Android/Android_Appium_Demo.apk')
# desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
# desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '13'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = ('/Users/anilkumar/Downloads/Android_Appium_Demo.apk')
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# using id
# element = driver.find_element(MobileBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")
# element.click()
# time.sleep(2)

# using class name
# element2 = driver.find_element(MobileBy.CLASS_NAME, "android.widget.EditText")
# element2.send_keys("23")
# time.sleep(2)

# using text -- with android uiautomator --uiselector
# element3 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter some Value")')
# element3.click()

# using text -- with android auiautomator -- without uiselector
# element4 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter some Value")')
# element4.click()
# using content-desc --with android uiautomator -- with UiSelector()
# element5 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Btn1")')
# element5.click()

# using index -- with android uiautomation -- with UiSelector()
# element6 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().index(3)')
# element6.click()

# element3 = driver.find_element(MobileBy.ID, "com.skill2lead.appiumdemo:id/Btn1")
# element3.click()

# xpath //tagname[@attribute=value] -- tagname is nothing but html tagname or android.widget.button or classname

# find_elements
elements7 = driver.find_elements(MobileBy.CLASS_NAME, "android.widget.Button")
print(elements7)
for element7 in elements7:
    print(element7.text)
    if element7.text == "ScrollView":
        element7.click()
        time.sleep(2)
        break


driver.quit()
