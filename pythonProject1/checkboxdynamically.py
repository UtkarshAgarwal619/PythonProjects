import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select

ser = Service(executable_path="C:\selenium\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for check in checkboxes:
    if check.get_attribute("value")=="option2":
        check.click()
        break