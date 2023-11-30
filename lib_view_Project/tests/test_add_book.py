import datetime
import time
import allure
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.add_author_page import Add_author_page
from pages.add_book_page import Add_book_page
from pages.add_metabook_page import Add_metabook_page
from pages.add_text_page import Add_text_page
from pages.login_page import Login_page
from pages.my_books_page import My_books_page
from pages.personal_account_page import Personal_account_page

"""Тестирование всего пути добавления книги"""
@allure.description("Test add books")
def test_add_books():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # g = Service('C:\\Users\\snazz\\PycharmProjects\\resource\\chromedriver.exe')
    g = Service()
    driver_g = webdriver.Chrome(options=options, service=g)


    print("Start test")
#Авторизация
    lp=Login_page(driver_g)
    lp.authorization()

#Переходы по страницам
    pap=Personal_account_page(driver_g)
    pap.select_author()

#Добавление автора
    aap=Add_author_page(driver_g)
    aap.add_author()
    aap.accept_alert()

# Переходы по страницам
    pap = Personal_account_page(driver_g)
    pap.select_metabook()

# Добавление метакниги
    amp=Add_metabook_page(driver_g)
    amp.add_metabook()
    amp.accept_alert()

    pap = Personal_account_page(driver_g)
    pap.select_book()

# Добавление книги
    adp=Add_book_page(driver_g)
    adp.add_book()
    adp.accept_alert()

# Переходы по страницам
    pap = Personal_account_page(driver_g)
    pap.select_text()

# Добавление текста в книгу
    atp=Add_text_page(driver_g)
    atp.add_text()
    atp.accept_alert()
# Переходы по страницам
    pap = Personal_account_page(driver_g)
    pap.select_my_books()

#провека на добавление книги
    mbp=My_books_page(driver_g)
    mbp.accept_books()





