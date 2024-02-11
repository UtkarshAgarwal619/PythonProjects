from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
ser=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(4)
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(4)
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(4)