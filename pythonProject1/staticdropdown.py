import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://www.yatra.com/")
ata=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']" )
time.sleep(3)
ata.click()
time.sleep(3)
ata.send_keys("New York")
time.sleep(3)
ata.send_keys(Keys.ENTER)
time.sleep(3)