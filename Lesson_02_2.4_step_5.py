# Implicitly Wait

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
browser.implicitly_wait(5)
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")
assert "successful" in message.text

browser.quit()
