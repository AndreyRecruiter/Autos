import time

from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR,'[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]').click()
    browser.find_element(By.NAME,'login').send_keys('Andrey.Peskichev@norbit.ru')
    browser.find_element(By.NAME,'password').send_keys('ihidabu228azapim')
    browser.find_element(By.CSS_SELECTOR,'[class="sign-form__btn button_with-loader "]').click()
    time.sleep(5)


