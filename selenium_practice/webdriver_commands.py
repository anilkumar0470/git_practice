import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()

driver = webdriver.Chrome(executable_path=r"C:\Users\pathapaa\Videos\git_practice\selenium_practice\chromedriver_win\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")  # to navigate to given URL

print(driver.title)  # displays the title of the page

print(driver.current_url)  # returns url of the current page

# to perform action/click or some thing , once u find the button we need to click on the same
# so we are using click method
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)

# close the browser and it will open only one window at a time . Let say we are clicking on one button
# where it is opening new tab , if u use close it will close the parent tab only not the child tab which
# opened by your click
# driver.close()  # currently focused tab

driver.quit()  # to close the all the tabs
