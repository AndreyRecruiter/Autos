from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.NAME,'firstname').send_keys('Petr')
browser.find_element(By.NAME,'lastname').send_keys('Petrov')
browser.find_element(By.NAME,'email').send_keys('PetrovPetr@yandex.ru')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
time.sleep(5)



