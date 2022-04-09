from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"C:\Users\akumarpathap\Downloads\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

element = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")

action = ActionChains(driver)
action.context_click(element).perform()
