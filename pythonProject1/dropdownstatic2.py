import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser = Service(executable_path="C:\selenium\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
driver.find_element(By.NAME, "UserFirstName").send_keys("Utkarsh")
driver.find_element(By.NAME, "UserLastName").send_keys("Agarwal")
driver.find_element(By.NAME, "UserEmail").send_keys("utkarshagarwal123@gmail.com")
dope = Select(driver.find_element(By.NAME, "UserTitle"))
dope.select_by_index(1)
time.sleep(2)
dope.select_by_visible_text("IT Manager")
time.sleep(2)