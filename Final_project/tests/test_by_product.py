import datetime
import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.products_page import Products_page

@allure.description("Test select product")
def test_select_product(set_up):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\snazz\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start test")


    lp = Login_page(driver_g)
    lp.authorization()

    mp = Main_page(driver_g)
    mp.choice_category_1()

    time.sleep(2)

    pp = Products_page(driver_g)
    pp.selection_product_1()

    mp = Main_page(driver_g)
    mp.choice_category_2()

    time.sleep(2)

    pp = Products_page(driver_g)
    pp.selection_product_2()

    cp = Cart_page(driver_g)
    cp.select_registration()

    fp = Finish_page(driver_g)
    fp.input_data()











