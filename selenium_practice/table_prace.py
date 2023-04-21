from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://tv.upstox.com/charts/NSE_INDEX%7CNifty%2050")

import pdb

import time
pdb.set_trace()

element = "//div[contains(@class,'active')]//tbody//tr[contains(@class,'ka-tr')]"

out = WebDriverWait(driver, 10).until(EC.presence_of_element_located((element)))


rows = driver.find_elements(By.XPATH, element)
driver.find_element(By.XPATH, "//div[contains(@class,'active')]")
# rows1 = table_element.find_elements(By.TAG_NAME, "tr")

for i in range(len(rows)):
    columns = driver.find_elements(By.XPATH, "//div[contains(@class,'active')]//tbody//tr[{}]//td".format(i))

    for j in range(len(columns)):
        print(columns[j].text, end="    ")
    print()
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_dict = {}
        for element in nums:
            if element not in new_dict:
                new_dict.update({element:element})
            else:
                return True
        return False