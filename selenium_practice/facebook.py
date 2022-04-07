from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

driver.get("https://www.facebook.com/")

# css -selector tag with ID
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("anilkumar.0444@gmial.com")
# css selector only with id tag is optional
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("anilkumar.0444@gmial.com")

# css -selector tag with class -- represents .

# css selector tag with class with attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[id=pass]").send_keys("fdfd")

# css
# driver.find_element(By.CSS_SELECTOR, )
driver.close()