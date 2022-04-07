from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# creating driver object
driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")


# navigating to URL
driver.get("https://www.google.com/")

driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("IBM")

driver.find_element(By.XPATH, "//div[@class='o3j99 LLD4me yr19Zb LS8OJ']").click()

# driver.find_element(By.XPATH, "//form/div/div/div/center/input[@class='gNO89b']").click()

driver.find_element(By.XPATH, "(//input[@class='gNO89b'])[2]").click()

urls = driver.find_elements(By.TAG_NAME, "a")
print(urls)

for ulr in urls:
    print(ulr.get_attribute("href"))
