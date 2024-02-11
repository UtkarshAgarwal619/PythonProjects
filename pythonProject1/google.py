from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
served=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=served)
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@title='Search']").send_keys("gmail")
driver.find_element(By.CSS_SELECTOR," div[class='FPdoLc lJ9FBc'] input[name='btnK']").click()
time.sleep(4)
driver.find_element(By.CLASS_NAME,"LC20lb MBeuO DKV0Md").click()