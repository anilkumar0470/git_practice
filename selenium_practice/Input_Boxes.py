# how to find how many input boxes presented in webpage
# how to provide value to text box
# how to get the status
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# to get all input box in the page
input_boxes = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(input_boxes))

status  = driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()
print(status)

status2  = driver.find_element(By.ID,"RESULT_TextField-1").is_enabled()
print(status2)

# how to provide the value into text box
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("ANIL KUMAR")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("PATHAPATI")

driver.find_element(By.ID, "RESULT_TextField-3").send_keys("999999999")

# how to get the status of the text box whether it is enabled or not