from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from utilites.logger import Logger
import allure



class Personal_account_page(Base):




    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators

    add_author = "/html/body/div[2]/div/div/table/tbody/tr[6]/td/a"
    add_metabook = "/html/body/div[2]/div/div/table/tbody/tr[8]/td/a"
    add_book = "/html/body/div[2]/div/div/table/tbody/tr[7]/td/a"
    add_text = "/html/body/div[2]/div/div/table/tbody/tr[9]/td/a"
    my_books = "/html/body/div[2]/div/div/table/tbody/tr[5]/td/a"




    # Getters


    def get_add_author(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_author)))

    def get_add_metabook(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_metabook)))
    def get_add_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_book)))

    def get_add_text(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_text)))

    def get_my_books(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_books)))





        # Actions


    def click_add_author(self):
        self.get_add_author().click()
        print("Click add author")

    def click_add_metabook(self):
        self.get_add_metabook().click()
        print("Click add metabook")

    def click_add_book(self):
        self.get_add_book().click()
        print("Click add book")

    def click_add_text(self):
        self.get_add_text().click()
        print("Click add text")

    def click_my_books(self):
        self.get_my_books().click()
        print("Click my books")







    # Methods


    def select_author(self):
        with allure.step("Select author"):
            Logger.add_start_step(method="select_author")
            self.click_add_author()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_author")


    def select_metabook(self):
        with allure.step("Select metabook"):
            Logger.add_start_step(method="select_metabook")
            self.click_add_metabook()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_metabook")

    def select_book(self):
        with allure.step("Select book"):
            Logger.add_start_step(method="select_book")
            self.click_add_book()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_book")

    def select_text(self):
        with allure.step("Select text"):
            Logger.add_start_step(method="select_text")
            self.click_add_text()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_text")

    def select_my_books(self):
        with allure.step("Select text"):
            Logger.add_start_step(method="select_text")
            self.click_my_books()
            Logger.add_end_step(url=self.driver_g.current_url, method="select_text")