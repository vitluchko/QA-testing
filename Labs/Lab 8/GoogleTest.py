from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

input_google = driver.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')

input_google.send_keys("Iphone")

input_google.send_keys(Keys.RETURN)

assert "Iphone - Пошук Google" in driver.title

# Пауза на 10 секунд
time.sleep(10)

driver.close()
