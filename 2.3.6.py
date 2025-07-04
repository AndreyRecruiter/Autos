from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from Calculated import calc


link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element(By.ID,'input_value')
x = x_element.text
y = calc(x)
browser.find_element(By.TAG_NAME,'input').send_keys(y)
browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
time.sleep(5)
