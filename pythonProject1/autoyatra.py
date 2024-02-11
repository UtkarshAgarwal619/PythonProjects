from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ser1=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser1)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(4)
departform=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
departform.click()
departform.send_keys("New Delhi")
time.sleep(4)
departform.send_keys(Keys.ENTER)
time.sleep(4)
goingto=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
goingto.click()
goingto.send_keys("New")
sera=driver.find_elements(By.XPATH,"(//div[@class='viewport']//div[1]/li)")
print(len(sera))
for results in sera:
    if "New York(JFK)" in results.text:
        results.click()
        time.sleep(4)
        break
time.sleep(4)
goingto.send_keys(Keys.ENTER)
