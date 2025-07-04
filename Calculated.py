from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID,'input_value')
x = x_element.text
y = calc(x)
browser.find_element(By.TAG_NAME,'input').send_keys(y)
browser.find_element(By.ID, 'robotCheckbox').click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element(By.ID, 'robotsRule').click()
button.click()
time.sleep(5)
