# working with frames is different than the other element
# so when you are working with frames first we need to switch to frame using name or id
# then we will do operation like click or something
# after that if you want click on another frame first we need to switch to  page using default_content()
# then we will switch to different frame
# driver.switch_to.frame(Nameof theframe)
# driver.switch_to.frame(id )
# driver.switch_to.default_content()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By



# 6281137209
driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-tree.html")

# first frame
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()

# second frame
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()

# thrid frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()
time.sleep(3)
driver.close()
