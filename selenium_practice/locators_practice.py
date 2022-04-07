from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# creating driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")


driver.get("http://automationpractice.com/index.php")

# driver.maximize_window()
# # id
# driver.find_element(By.ID, "search_query_top").send_keys("T-shirts")
# #  name
# driver.find_element(By.NAME, "submit_search").click()
# # link text
# driver.find_element(By.LINK_TEXT, "Printed Chiffon Dress").click()

# to find how many images
slide_element = driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(slide_element))

# how many links available in the web page

html_links = driver.find_elements(By.TAG_NAME, "a")
print(len(html_links))

for html_link in html_links:
    print(html_link.get_attribute("href"))

