from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for element in veggieWebElements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy()

browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList