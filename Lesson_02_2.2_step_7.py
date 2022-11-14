import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get(link)
    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys("Alex")
    second = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    second.send_keys("Polo")
    mail = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    mail.send_keys("mail@mail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

