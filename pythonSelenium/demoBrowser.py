import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

#service_obj = Service("path-to-chrome-driver") #if you need manually install chrome driver, you can use Service class
#driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)



time.sleep(2)