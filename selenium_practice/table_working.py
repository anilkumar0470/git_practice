# if you are working with table, first we need to observer the table carefully
# which means observer tr -- tables rows and th-- table headers
# to fetch all the values in the table we need to find the two things row and columns count
#  to find the all rows .. find the common element for rows and use find_elements
# /html/body/table/tbody/tr
# to find the all column .. find the common element for columns and use find_elements


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # creating driver object
# driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")
#
# driver.get(r"file:///C:/Users/pathapaa/OneDrive%20-%20Mitel%20Networks%20Corporation/Desktop/sample.html")
#
# rows = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")
#
# columns = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[2]/td")
#
# print(len(rows), len(columns))
#
# for row in range(2, len(rows)+1):
#     for column in range(1, len(columns)+1):
#         print(driver.find_element(By.XPATH, "/html/body/table/tbody/tr[{}]/td[{}]".format(row, column)).text, end=" ")
#     print()
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
#
# rows = len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr"))
#
# columns = len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th"))
#
#
# print("rows are {}".format(rows))
# print("columns are {}".format(columns))
#
# for row in range(2,rows+1):
#     for column in range(1, columns+1):
#         print(driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[{}]/td[{}]".format(row, column)).text, end=" ")
#     print()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

# driver.get("https://login.upstox.com/")
# import pdb
# pdb.set_trace()
# import time
# # time.sleep(30)
#
# rows = len(driver.find_elements(By.XPATH, "//*[@id='books']/div/div/div/div[2]/div/div/table/tbody/tr"))
# columns = len(driver.find_elements(By.XPATH, "//*[@id='books']/div/div/div/div[2]/div/div/table/tbody/tr[1]/td"))
#
# for row in range(1, rows+1):
#     for column in range(1, columns+1):
#         print(driver.find_element(By.XPATH, "//*[@id='books']/div/div/div/div[2]/div/div/table/tbody/tr[{}]/td[{}]".format(row, column)).text, end="    ")
#     print()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
#
# driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
#
# table_element = driver.find_element(By.XPATH, "//*[@id='customers']")
#
# import pdb
# # pdb.set_trace()
#
# rows = driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr")
#
# # rows1 = table_element.find_elements(By.TAG_NAME, "tr")
#
# for i in range(len(rows)):
#     columns = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr[{}]/td".format(i))
#
#     for j in range(len(columns)):
#         print(columns[j].text, end="    ")
#     print()

