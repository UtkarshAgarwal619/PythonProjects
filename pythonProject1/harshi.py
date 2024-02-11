import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
serv=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.find_element(By.NAME,"username").send_keys("Utkarsh Agarwal")
driver.find_element(By.ID,"password").send_keys("hola123")
#driver.find_element(By.XPATH,"//select[@class='form-control']").click()
drop=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
drop.select_by_index(2)
driver.find_element(By.NAME,"signin").click()
time.sleep(5)
driver.close()