import time
import math
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(options=chrome_options)
    browser.delete_all_cookies()
    yield browser
    print("\nquit browser..")
    browser.quit()
    time.sleep(5)

TEST_LINKS = [
    ("lesson_236895", "https://stepik.org/lesson/236895/step/1"),
    ("lesson_236896", "https://stepik.org/lesson/236896/step/1"),
    ("lesson_236897", "https://stepik.org/lesson/236897/step/1"),
    ("lesson_236898", "https://stepik.org/lesson/236898/step/1"),
    ("lesson_236899", "https://stepik.org/lesson/236899/step/1"),
    ("lesson_236903", "https://stepik.org/lesson/236903/step/1"),
    ("lesson_236904", "https://stepik.org/lesson/236904/step/1"),
    ("lesson_236905", "https://stepik.org/lesson/236905/step/1")
]

@pytest.mark.parametrize("name,url", TEST_LINKS, ids=[name for name, url in TEST_LINKS])
def test_open_stepik_links(browser, name, url):
    #Тест открывает каждую ссылку из списка и проверяет основные элементы страницы
    browser.get(url)
    browser.implicitly_wait(10)
    #WebDriverWait(browser,25).until(EC.presence_of_element_located(By.ID,'ember479')).click()
    browser.find_element(By.CSS_SELECTOR,'[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]').click()
    browser.find_element(By.NAME,'login').send_keys('Andrey.Peskichev@norbit.ru')
    browser.find_element(By.NAME,'password').send_keys('ihidabu228azapim')
    browser.find_element(By.CSS_SELECTOR,'[class="sign-form__btn button_with-loader "]').click()
    time.sleep(5)
    AgainButton = browser.find_elements(By.CSS_SELECTOR,'[class="again-btn white"]')
    if AgainButton:
        AgainButton[0].click()
        OKButton = browser.find_element(By.CSS_SELECTOR,'div[data-theme="confirm"] .modal-popup__footer button[type="button"]:nth-child(1)')
        OKButton.click()
        return True
    return False
    TextAnswer = browser.find_element(By.TAG_NAME,'textarea')
    TextAnswer.send_keys(str(math.log(int(time.time() + 0.2))))
    button = browser.find_element(By.CSS_SELECTOR,'[class="submit-submission"]')
    button.click()
    message_element = browser.find_element(By.CSS_SELECTOR,'[class="smart-hints__hint"]')
        #ebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[class="smart-hints__hint"]')))
    feedback = message_element.text
    print(feedback)
    assert feedback == "Correct!"
