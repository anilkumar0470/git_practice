# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # # # creating driver object
# # driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# # # driver = webdriver.Firefox()
# # # # navigating to URL
# # driver.maximize_window()
# # driver.get("https://login.upstox.com/")
# # time.sleep(3)
# # driver.find_element(By.ID, "mobileNum").send_keys("9581228818")
# #
# #
#
#
#
#
#
#
#
# # import pdb
# # pdb.set_trace()
# #
# # #
# # #
# # import random
# # #
# # mobiles_nums = []
# # while True:
# #     number = random.randrange(9000000000, 9999999999)
# #     if number not in mobiles_nums:
# #         mobiles_nums.append(number)
# #
# #     if len(mobiles_nums) == 100:
# #         break
# # for mobiles_num in range(30):
# #     import time
# #     time.sleep(1)
# #     driver.find_element(By.XPATH, "//*[@id='mobilenumber']").clear()
# #     driver.find_element(By.XPATH, "//*[@id='mobilenumber']").send_keys("9581228818")
# #     driver.find_element(By.XPATH, "//*[@id='sendotp']").click()
# #     time.sleep(5)
# #     driver.switch_to.alert.accept()
# # # print(mobiles_nums)
#
#
# # driver.quit()
# # #
# # driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("IBM")
# #
# # driver.find_element(By.XPATH, "//div[@class='o3j99 LLD4me yr19Zb LS8OJ']").click()
# # driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/canvas[2]").click()
# #
# # # driver.find_element(By.XPATH, "//form/div/div/div/center/input[@class='gNO89b']").click()
# #
# # driver.find_element(By.XPATH, "(//input[@class='gNO89b'])[2]").click()
# #
# # urls = driver.find_elements(By.TAG_NAME, "a")
# # print(urls)
# #
# # for ulr in urls:
# #     print(ulr.get_attribute("href"))
#
# # aaa = "giri hari suri"
# # #
# # # for i in range(len(aaa.split())):
# # #     for character in aaa.split()[i]:
# # #         for new_word in aaa.split():
# # #             if new_word != aaa.split()[i]:
# # #                 pass
# #
# # out = aaa.split()
# # result = ""
# # for word in out:
# #     for character in word:
# #         for new_word in out:
# #             if character not in new_word:
# #                 break
# #         else:
# #            if character not in result:
# #                result = result + character
# # print(result)
#
#
# from appium import webdriver
# # from appium.options.android import UiAutomator2Options
# # from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# desired_cap = {
#     # Set your access credentials
#     "browserstack.user" : "anilkumar_4VqU0N",
#     "browserstack.key" : "X2qpPW3caKEKhLxLzLVx",
#
#     # Set URL of the application under test
#     "app" : "bs://e8b7928cf4ce2db96ef0cd4ae4a1ff039996a090",
#
#     # Specify device and os_version for testing
#     "device" : "Google Pixel 3",
#     "os_version" : "9.0",
#
#     # Set other BrowserStack capabilities
#     "project" : "First Python project",
#     "build" : "browserstack-build-1",
#     "name" : "first_test"
# }
#
# # Initialize the remote Webdriver using BrowserStack remote URL
# # and desired capabilities defined above
# driver = webdriver.Remote(
#     command_executor="http://hub-cloud.browserstack.com/wd/hub",
#     desired_capabilities=desired_cap)
#
# ID_BASE = "in.upstox.app"
# MOB_NUM_INPUT = ID_BASE + ":id/inputTextLineField"
# element = driver.find_element("id", MOB_NUM_INPUT)
# element.click()
# element.clear()
# element.send_keys("9581228818")
#
# # self.enter_text_action(value, LL.MOB_NUM_INPUT)
#
#
# driver.quit()
# #
# # # Options are only available since client version 2.3.0
# # options = {"capabilities":
# #                {"firstMatch":
# #                     [{"appium:build": "Python Android",
# #                       "appium:device": "Google Pixel 5",
# #                       "appium:browserstack.networkLogs": True,
# #                       "appium:browserstack.idleTimeout": "300",
# #                       "appium:deviceName": "emulator-5554",
# #                       "platformName": "Android",
# #                       "appium:automationName": "UiAutomator2",
# #                       "appium:autoGrantPermissions": True,
# #                       "appium:skipDeviceInitialization": True,
# #                       "appium:skipServerInstallation": True,
# #                       "appium:chromedriverExecutable": "/Users/pushphaskanugo/UPSTOX_REPO/mobile-automation-global-upstox/drivers/chromedriver",
# #                       "appium:autoDismissAlerts": True,
# #                       "appium:appPackage": "in.upstox.app",
# #                       "appium:appActivity": "in.upstox.pro.beta.app.UpstoxMainActivity",
# #                       "appium:newCommandTimeout": "60",
# #                       "appium:app": "bs://e8b7928cf4ce2db96ef0cd4ae4a1ff039996a090",
# #                       "appium:userName": "anilkumar_4VqU0N",
# #                       "appium:accessKey": "X2qpPW3caKEKhLxLzLVx",
# #                       "appium:networkProfile": "4g-lte-good"}]},
# #                       "desiredCapabilities": {
# #                           "build": "Python Android",
# #                           "device": "Google Pixel 5",
# #                           "browserstack.networkLogs": True,
# #                           "browserstack.idleTimeout": "300",
# #                           "deviceName": "emulator-5554",
# #                           "platformName": "Android",
# #                           "automationName": "UiAutomator2",
# #                           "autoGrantPermissions": True,
# #                           "skipDeviceInitialization": True,
# #                           "skipServerInstallation": True,
# #                           "chromedriverExecutable": "/Users/pushphaskanugo/UPSTOX_REPO/mobile-automation-global-upstox/drivers/chromedriver",
# #                           "autoDismissAlerts": True,
# #                           "appPackage": "in.upstox.app",
# #                           "appActivity": "in.upstox.pro.beta.app.UpstoxMainActivity",
# #                           "newCommandTimeout": "60",
# #
# #                           "networkProfile": "4g-lte-good"}}
# # # Initialize the remote Webdriver using BrowserStack remote URL
# # # and options defined above
# # driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options)
# # # If you have uploaded your app, update the test case here.

# import datetime
# start_time = datetime.datetime.now()
# import time
# time.sleep(1)
# end_time = datetime.datetime.now()
# delta = end_time - start_time
# print("#########", delta.total_seconds()*1000)


def process_dict(new_dict1, new_list = []):

    for k,v in new_dict1.items():
        if type(v) == dict:
            process_dict(v, new_list=new_list)
            # print(k, v)
        else:
            # print(k, v)
            if type(v) == int:
                new_list.append(v)
    return sum(new_list)

new_dict = {"a": 2, "b": {"x":2, "y": {"foo" : 3, "z": {"bar": 2}}}, "c": {"p": {"h" : 2, "r":5}, "d":1, "e": {"nn": { "lil": 2}, "mm": "car"}}}

# print(process_dict(new_dict))


out = []
for num in range(2, 100):
    count = 0
    for i in range(2, num):
        if num%i ==0:
            break
    else:
        out.append(num)

count = 0
skip = 0
for val in out:
    if count == skip:
        print(val)
        skip = skip + 1
        count = 0
    else:
        count = count + 1



str1 = "hello go$d mo[ning% h@ve a great day"
str2 = "yad taer$g a [evh %gn@inom dog olleh"
res = []
new_dict = {}
for index, item in enumerate(str1):
    if item.isalpha() or item.isspace():
        res.insert(0, item)
    else:
        new_dict.update({index: item})
# print("#####", new_dict)
# print("$$$$", res)
for k, v in new_dict.items():
    res.insert(k,v)
# print("final", res)
print("".join(res))


out_dict = {}
str3 = "good morning have a nice day"
for character in str3:
    if character not in out_dict and not character.isspace():
        out_dict.update({character: str3.count(character)})
print(out_dict)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(executable_path="/Users/anilkumar/Documents/msedgedriver")
driver.maximize_window()
driver.get("https://www.google.com")
import time
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("facebook")

time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cricbuzz")
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]").click()
driver.back()
time.sleep(2)
# import time
# time.sleep(2)
# ele1 = driver.find_element(By.XPATH, "//*[@aria-label='Google apps' and  @class='gb_e']")
# ele1.click()
# time.sleep(2)
# import pdb
# # pdb.set_trace()
# # wait = WebDriverWait(driver, 10)
#
# driver.switch_to.frame("app")
#
# ctnbtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'YouTube') and contains(@data-text,'YouTube')]")))
# ctnbtn.click()
#
# # ele2 = wait.until(EC.presence_of_element_located(((By.XPATH, "//*[contains(text(), 'YouTube') and contains(@data-text,'YouTube')]"))))
# # ele2 = driver.find_element(By.XPATH, "//*[contains(text(), 'YouTube') and contains(@data-text,'YouTube')]")
# # ele2.click()
