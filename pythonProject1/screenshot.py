import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
demos= driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
demos.screenshot(".\\test.png")
demos.click()
time.sleep(5)
driver.get_screenshot_as_file(".\\C:\selenium\error.png")
driver.save_screenshot(".\\test1.png")