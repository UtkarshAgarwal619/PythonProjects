from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(12)
driver.close()