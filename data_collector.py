from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = ""
email_adress = ""
user_password = ""

driver = webdriver.Edge()
driver.get("https://my.strengthlevel.com/login")

email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
email.send_keys(email_address)

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
password.send_keys(user_password)

driver.find_element(By.XPATH, '//button[normalize-space()="Log In"]').click()

driver.get(f"https://my.strengthlevel.com/{username}/workouts")

driver.get(f"https://my.strengthlevel.com/{username}/export")
