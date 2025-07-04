from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
alert = browser.switch_to.alert
alert.accept()
#time.sleep(5)
x_element = browser.find_element(By.ID,'input_value')
x = x_element.text
y = calc(x)
browser.find_element(By.TAG_NAME,'input').send_keys(y)
browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
time.sleep(5)



