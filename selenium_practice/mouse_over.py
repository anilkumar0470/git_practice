# some times we need to place the mouse on the element so that those options will appear which is
# nothing but mouse over, we can achieve the same by using ActionChains with move_to_element
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

