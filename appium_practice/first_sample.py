from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import time
desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "8a88e220",
  "appium:app": "/Users/anilkumar/Downloads/universal.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(18)
inner_text = driver.find_element(MobileBy.ID, "in.upstox.app:id/inputLabelText").text
assert inner_text == "Enter mobile number"


wait = WebDriverWait(driver, 20)
mob_field = wait.until(EC.presence_of_element_located((MobileBy.ID, "in.upstox.app:id/inputTextLineField")))
mob_field.send_keys("9581228818")
# driver.find_element_by_id("in.upstox.app:id/inputTextLineField").send_keys("9581228818")
time.sleep(2)
driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.Button").click()
time.sleep(10)