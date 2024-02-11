import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)
print(driver.title)
lista=driver.find_elements(By.TAG_NAME,'a')
print(len(lista))
for i in lista:
    print(i.text)
driver.close()