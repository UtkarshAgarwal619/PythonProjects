import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select

ser = Service(executable_path="C:\selenium\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)
con = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(con))
for co in con:
    if co.text == "India":
        co.click()
        break
    time.sleep(4)
