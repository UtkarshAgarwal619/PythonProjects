from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowopen=driver.window_handles

driver._switch_to.window(windowopen[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(4)
driver.close()
driver.switch_to.window(windowopen[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
time.sleep(5)