# Switch to new window

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    browser.switch_to.window(browser.window_handles[1])

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
    time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()

finally:
    time.sleep(1)
    browser.quit()


