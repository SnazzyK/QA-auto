import time

import allure
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilites.logger import Logger


class Main_page(Base):




    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    burger_menu = "//button[@class='cmAEiN9sK']"
    category_1 = "//a[@href='/catalog/novogodnie-podarki-20']"
    category_2 = "//a[@href='/catalog/bestseller-729']"




    # Getters



    def get_burger_menu(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_category_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_1)))

    def get_category_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_2)))






        # Actions


    def click_burger_menu(self):

        self.get_burger_menu().click()
        print("Click burger menu")

    def click_category_1(self):
        self.get_category_1().click()
        print("Click category 1 ")


    def click_category_2(self):
        self.get_category_2().click()
        print("Click category 2 ")







    # Methods

    def choice_category_1(self):
        with allure.step("Choice category 1"):
            Logger.add_start_step(method="choice_category_1")
            self.assert_url("https://kdvonline.ru/")
            self.click_burger_menu()
            self.click_category_1()
            self.driver_g.execute_script("window.scrollTo(0,300)")
            Logger.add_end_step(url=self.driver_g.current_url, method="choice_category_1")




    def choice_category_2(self):
        with allure.step("Choice category 2"):
            Logger.add_start_step(method="choice_category_2")
            self.click_burger_menu()
            self.click_category_2()
            self.driver_g.execute_script("window.scrollTo(0,300)")
            Logger.add_end_step(url=self.driver_g.current_url, method="choice_category_2")

