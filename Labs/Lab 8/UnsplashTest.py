from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://unsplash.com/")

btn_input = driver.find_element(By.XPATH, "//button[@type='button']")
btn_input.click()

# Пауза на 3 секунд
time.sleep(3)

img_input = driver.find_element(By.XPATH, "//input[@type='file']")
img_input.send_keys("C:/Users/Win7/PycharmProjects/pythonProject/images/zolkin.jpg")

# Пауза на 10 секунд
time.sleep(10)

# Закриття веб-сторінки та браузера
driver.quit()
