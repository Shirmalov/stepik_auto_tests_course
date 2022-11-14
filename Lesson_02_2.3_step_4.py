# Modal windows - [Cancel, OK]

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.dismiss()  # For push "Cancel" button
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()  # For push "OK" button

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    x_element2 = browser.find_element(By.ID, "answer")
    x_element2.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
