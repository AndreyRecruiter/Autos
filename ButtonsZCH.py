from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

firstName = browser.find_element(By.CSS_SELECTOR, '[class="form-control first"]')
firstName.send_keys('FirstName')
LastName = browser.find_element(By.CSS_SELECTOR,'[placeholder="Input your last name"]')
LastName.send_keys('LastName')
Email = browser.find_element(By.CSS_SELECTOR, '[class="form-control third"]')
Email.send_keys('Email')
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
time.sleep(2)
submit_button = browser.find_element(By.CSS_SELECTOR,'[class="btn btn-default"]')
submit_button.click()
    # находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(3)
    # закрываем браузер после всех манипуляций
browser.quit()