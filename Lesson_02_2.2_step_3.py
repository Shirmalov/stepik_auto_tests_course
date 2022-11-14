from selenium import webdriver
from selenium.webdriver.common.by import By
import select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    a = num1.text
    b = num2.text
    sum = (int(a)+int(b))
    dropdown = browser.find_element(By.ID, "dropdown")
    dropdown.click()
    browser.find_element(By.CSS_SELECTOR, f'option[value="{int(a)+int(b)}"]').click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

