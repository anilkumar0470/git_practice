
########## basic commands
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path=r'/Users/anilkumar/Downloads/chromedriver')
#
# driver.get("http://demo.automationtesting.in/Windows.html")
#
# print("title is {}".format(driver.title))
#
# print("url is {}".format(driver.current_url))
#
# driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
#
# time.sleep(5)
#
# # driver.close() # close only parent window or currently focused browser
#
# driver.quit()

########### navigational commands
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# # driver = webdriver.Chrome(executable_path=r'/Users/anilkumar/Downloads/chromedriver')
# #
# # driver.get("https://upstox.com/")
# #
# # print("driver title is {}".format(driver.title))
# # print("driver url is {}".format(driver.current_url))
# #
# # driver.get("https://www.pavanonlinetrainings.com/")
# #
# # print("driver title is {}".format(driver.title))
# # print("driver url is {}".format(driver.current_url))
# #
# # driver.back() # to go back to previous page
# #
# # print("driver title is {}".format(driver.title))
# # print("driver url is {}".format(driver.current_url))
# #
# # driver.forward()
# #
# # print("driver title is {}".format(driver.title))
# # print("driver url is {}".format(driver.current_url))
# #
# # driver.close()
#
#
# ############## conditional commands
# # is_displayed()
# # is_enabled()
# # is_selected()
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome(executable_path=r'/Users/anilkumar/Downloads/chromedriver')
#
#
#
# driver.get("https://www.phptravels.net/login")
#
# element = driver.find_element(By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input')
#
# print("element displayed", element.is_displayed())
# print("element is enabled or not", element.is_enabled())
#
# rem_ele = driver.find_element(By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[1]/label')
# print("element is selected", rem_ele.is_selected())
# rem_ele.click()
# print("element is selected ", rem_ele.is_selected())
# driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'/Users/anilkumar/Downloads/chromedriver')

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element(By.XPATH, '//*[@id="wizardMainRegionV2"]/div/div/div/div/ul/li[2]/a/span').click()


driver.close()
