from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link ="https://serkonsdev.dis.norbit.ru/bitrix/admin/cache.php?lang=ru"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
login_string = WebDriverWait(browser, 25).until(
EC.presence_of_element_located((By.NAME, "USER_LOGIN")))
y = calc
login_string.send_keys("admin")
password_string = browser.find_element(By.NAME, "USER_PASSWORD")
password_string.send_keys("-HW6!+U&XwJGY~hgszKA")
login_button = browser.find_element(By.NAME, "Login").click()
