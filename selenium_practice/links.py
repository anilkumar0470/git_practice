# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
#
#
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#
# driver.get("https://google.com")
#
# driver.find_element(By.XPATH, "//input[@class='gLFyf']").send_keys("top news")
#
# driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
#
#
#
#
#
# import time
# time.sleep(3)
#
# elements = driver.find_elements(By.TAG_NAME, "a")
#
# print(len(elements))
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
#
#
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#
#
# driver.get("https://demo.guru99.com/test/newtours/")
#
# all_links = driver.find_elements(By.TAG_NAME, "a")
#
# print("number of links in the page {}".format(len(all_links)))
#
#
# for link in all_links:
#     if link.text:
#         print(link.text)
# # driver.find_element(By.LINK_TEXT, "REGISTER").click()
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()
# import time
# time.sleep(2)
#
# driver.quit()
#
#
#
#
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get("https://demo.guru99.com/test/newtours/")

# to find all the links in the given page

all_links = driver.find_elements(By.TAG_NAME, "a")
print(len(all_links))
for link in all_links:
    print(link.get_attribute("href"))
    print(link.text)

driver.close()





