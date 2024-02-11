from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
served=Service(executable_path="C:\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=served)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
time.sleep(6)
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productname=product.find_element(By.XPATH,"div/h4/a").text
    if productname=="Blackberry":
        product.find_element(By.XPATH,"div/button").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
time.sleep(7)
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
dp=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in dp
time.sleep(7)
driver.close()