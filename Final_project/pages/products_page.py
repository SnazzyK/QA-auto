import allure
import app
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilites.logger import Logger


class Products_page(Base):



    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    product_1 = "//*[@id='app']/div/div/div[5]/div/div/div/div[2]/div[3]/div/div[1]/div/div[4]/div[2]/div[2]/div/button"
    product_2 = "//*[@id='app']/div/div/div[5]/div/div/div/div[2]/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div/button"
    select_cart = "//a[@href='/cart']"


    # Getters



    def get_product_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_select_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart)))




        # Actions


    def click_product_1(self):

        self.get_product_1().click()
        print("Click product 1")

    def click_product_2(self):
        self.get_product_2().click()
        print("Click product 2")

    def click_select_cart(self):
        self.get_select_cart().click()
        print("Click select cart ")






    # Methods

    def selection_product_1(self):
        with allure.step("Selection product 1"):
            Logger.add_start_step(method="selection_product_1")
            self.get_current_url()
            self.click_product_1()
            Logger.add_end_step(url=self.driver_g.current_url, method="selection_product_1")


    def selection_product_2(self):
        with allure.step("Selection product 2"):
            Logger.add_start_step(method="selection_product_2")
            self.get_current_url()
            self.click_product_2()
            self.click_select_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method="selection_product_2")


