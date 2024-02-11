import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("utkarsh agarwal")
driver.find_element(By.NAME,"email").send_keys("utkarshagarwal619@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[id='exampleInputPassword1']").click()
#static drop down
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1" ))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
time.sleep(8)