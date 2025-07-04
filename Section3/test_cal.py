import math
import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    # Инициализация браузера
    browser = webdriver.Chrome()
    yield browser
    # Закрытие браузера после теста
    browser.quit()


class TestStepikLessons():
    message = ""  # Переменная для сообщений
    links = [  # Массив со списком адресов
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]

    @pytest.mark.parametrize('link', links)
    def test_stepik_lessons(self, browser, link):
        # Открываем страницу
        browser.get(link)

        # Неявное ожидание
        browser.implicitly_wait(10)

        # Находим textarea и вводим текст
        textarea = browser.find_element(By.TAG_NAME, "textarea")
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)

        # Находим и кликаем кнопку
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()

        # Получаем текст сообщения
        message_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        feedback = message_element.text

        # Проверяем и сохраняем сообщение
        if feedback != "Correct!":
            self.message += feedback
        print(f"\nСообщение на странице {link}: {feedback}")

        # Проверяем, что сообщение не равно "Correct!" (ожидаем False)
        assert (feedback == "Correct!") == False

        if __name__ == "__main__":
            unittest.main()