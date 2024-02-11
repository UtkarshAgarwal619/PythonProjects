import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(executable_path="C:\selenium\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://www.yatra.com/")
driver.find_element(By.XPATH, "(//td[@id='16/02/2023'])[1]").click()
time.sleep(4)

