import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_obj = Options()
chrome_obj.add_experimental_option("prefs", {"download.default_directory":r"C:\Users\akumarpathap\Desktop"})

driver = webdriver.Chrome(r"C:\Users\akumarpathap\Downloads\chromedriver.exe", chrome_options=chrome_obj)
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

# download text file

driver.find_element(By.XPATH, "//textarea[@id='textbox']").send_keys("good morning")
driver.find_element(By.XPATH, "//button[@id='createTxt']").click()
driver.find_element(By.XPATH, "//a[@id='link-to-download']").click()

# download pdf file

driver.find_element(By.XPATH, "//textarea[@id='pdfbox']").send_keys("good evening")
driver.find_element(By.XPATH, "//button[@id='createPdf']").click()
driver.find_element(By.XPATH, "//a[@id='pdf-link-to-download']").click()

time.sleep(3)
driver.close()