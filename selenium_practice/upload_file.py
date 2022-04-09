from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\akumarpathap\Downloads\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()


driver.switch_to.frame(0)
driver.find_element(By.ID, "RESULT_FileUpload-10").send_keys(r"C:\Users\akumarpathap\Desktop\Rahima.PNG")