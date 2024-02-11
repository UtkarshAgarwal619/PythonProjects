import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.NAME,"enter-name").send_keys("Utkarsh")
time.sleep(5)