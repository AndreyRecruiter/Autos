from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link ="http://172.30.56.36:8500/Login/Login.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

login_string = WebDriverWait(browser, 25).until(
EC.presence_of_element_located((By.ID, "loginEdit-el")))
login_string.send_keys("Администратор_Пескичев")
password_string = browser.find_element(By.ID, "passwordEdit-el")
password_string.send_keys("Администратор_Пескичев")
login_button = browser.find_element(By.ID, "t-comp15-textEl").click()

chapterhomepage = WebDriverWait(browser, 25).until(
EC.presence_of_element_located((By.ID, "sidebar-item-text-0"))).text
print(chapterhomepage)
chapterhomepagename = "Домашняя страница"
assert chapterhomepage == chapterhomepagename, f"Тест не пройден, вот что получилось {chapterhomepage}"