from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    x_element2 = browser.find_element(By.ID, "answer")
    x_element2.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:

    time.sleep(5)
    browser.quit()