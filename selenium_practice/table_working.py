# if you are working with table, first we need to observer the table carefully
# which means observer tr -- tables rows and th-- table headers
# to fetch all the values in the table we need to find the two things row and columns count
#  to find the all rows .. find the common element for rows and use find_elements
# /html/body/table/tbody/tr
# to find the all column .. find the common element for columns and use find_elements


from selenium import webdriver
from selenium.webdriver.common.by import By

# creating driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

driver.get(r"file:///C:/Users/pathapaa/OneDrive%20-%20Mitel%20Networks%20Corporation/Desktop/sample.html")

rows = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")

columns = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[2]/td")

print(len(rows), len(columns))

for row in range(2, len(rows)+1):
    for column in range(1, len(columns)+1):
        print(driver.find_element(By.XPATH, "/html/body/table/tbody/tr[{}]/td[{}]".format(row, column)).text, end=" ")
    print()