import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
ser=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.find_element(By.XPATH,"//input[@value='radio2']").is_selected())
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='radio2']").click()
print(driver.find_element(By.XPATH,"//input[@value='radio2']").is_selected())
time.sleep(4)
driver.find_element(By.ID,"autocomplete").send_keys("India")
drop=Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
drop.select_by_index(2)
driver.find_element(By.NAME,"checkBoxOption3").click()
time.sleep(4)
driver.find_element(By.ID,"openwindow").click()
driver.maximize_window()
time.sleep(4)