import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://www.yatra.com/")
driver.find_element(By.XPATH,"//a[normalize-space()='Student Fare']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Armed Forces']").click()
time.sleep(4)
driver.maximize_window()