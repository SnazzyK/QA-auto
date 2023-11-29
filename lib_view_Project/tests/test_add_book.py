import datetime
import time
import allure
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.add_author_page import Add_author_page
from pages.add_book_page import Add_book_page
from pages.add_metabook_page import Add_metabook_page
from pages.add_text_page import Add_text_page
from pages.login_page import Login_page
from pages.my_books_page import My_books_page
from pages.personal_account_page import Personal_account_page


@allure.description("Test add books")
def test_add_books():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\snazz\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start test")

    lp=Login_page(driver_g)
    lp.authorization()

    pap=Personal_account_page(driver_g)
    pap.select_author()

    aap=Add_author_page(driver_g)
    aap.add_author()
    aap.accept_alert()

    pap = Personal_account_page(driver_g)
    pap.select_metabook()

    amp=Add_metabook_page(driver_g)
    amp.add_metabook()
    amp.accept_alert()

    pap = Personal_account_page(driver_g)
    pap.select_book()

    adp=Add_book_page(driver_g)
    adp.add_book()
    adp.accept_alert()

    pap = Personal_account_page(driver_g)
    pap.select_text()


    atp=Add_text_page(driver_g)
    atp.add_text()
    amp.accept_alert()

    mbp=My_books_page(driver_g)
    mbp.accept_books()




