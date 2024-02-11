import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Demofindelement():
    def locate_by_id(self):
        ser=Service(executable_path="C:\selenium\chromedriver.exe")
        driver=webdriver.Chrome(service=ser)
        driver.get("https://training.openspan.com/login")
        demo=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo)
        time.sleep(4)
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("utkarsh")
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("123456uk")
        demo1=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo1)
        time.sleep(4)
findelement=Demofindelement()
findelement.locate_by_id()