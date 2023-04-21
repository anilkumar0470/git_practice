# # working with frames is different from the other element
# # so when you are working with frames first we need to switch to frame using name or id
# # then we will do operation like click or something
# # after that if you want click on another frame first we need to switch to  page using default_content()
# # then we will switch to different frame
# # driver.switch_to.frame(name of the frame)
# # driver.switch_to.frame(id )
# # driver.switch_to.default_content()
#
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#
#
#
# # 6281137209
# driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-tree.html")
#
# # first frame
# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
# time.sleep(2)
# driver.switch_to.default_content()
#
# # second frame
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.LINK_TEXT, "WebDriver").click()
# driver.switch_to.default_content()
#
# # thrid frame
# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()
# time.sleep(3)
# driver.close()
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://tv.upstox.com/charts/NSE_INDEX%7CNifty%2050")
# driver.maximize_window()
# import pdb
# pdb.set_trace()
# driver.switch_to.frame(0)
# # canvas = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div")
# canvas = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/canvas[1]")
# # drawing = ActionChains(driver).move_by_offset(1008, 2560).click(canvas).release()
# drawing = ActionChains(driver).move_by_offset(696,259).context_click(canvas)
# drawing.perform()
# import time
# time.sleep(2)
# element = driver.find_element(By.XPATH, "//*[@id='overlap-manager-root']/div/div[1]/div/div/table")
# rows = element.find_elements(By.TAG_NAME, "tr")
# rows[0].click()
# import pdb
# pdb.set_trace()
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.maximize_window()
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-tree.html")
#
#
# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
#
# driver.switch_to.default_content()
# driver.switch_to.frame("packageFrame")
#
# driver.find_element(By.LINK_TEXT,"WebDriver").click()
#
# driver.switch_to.default_content()
# driver.switch_to.frame("classFrame")
# import time
# time.sleep(5)
# import pdb
# pdb.set_trace()
# driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[1]/a").click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-tree.html")

driver.switch_to.frame("packageListFrame")
# element = driver.find_element(By.LINK_TEXT, "org.openqa.selenium")

new_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "org.openqa.selenium")))
new_element.click()
driver.switch_to.default_content()

import time

driver.switch_to.frame("packageFrame")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()


driver.switch_to.frame("classFrame")
dep_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]/a")))
dep_element.click()







