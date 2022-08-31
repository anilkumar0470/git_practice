# select one option
# to get  all the options
# how many options count

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Downloads\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drp_btn = driver.find_element(By.ID, "RESULT_RadioButton-9")
drp = Select(drp_btn)
# select by visible text
drp.select_by_visible_text("Morning")
# select by index number index start from 0
# drp.select_by_index(2)
# select by value attribute in html
drp.select_by_value("Radio-2")
#
# # drop down count

print(len(drp.options))
# capture all the options in drop down
all_options = drp.options
for option in all_options:
    print(option.text)