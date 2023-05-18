from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://grinfer.com/")

btn_log_in = driver.find_element(By.XPATH, "//a[@class='sc-2aalce-2 dvzzdp']").click()

input_email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("test@test.com")

input_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("1234567")

click_btn_log_in = driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Пауза на 10 секунд
time.sleep(10)

# Закриття веб-сторінки та браузера
driver.quit()
