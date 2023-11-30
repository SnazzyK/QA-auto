from datetime import time
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from utilites.logger import Logger
import allure



class Add_book_page(Base):



    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators

    title = "//input[@name='title']"
    author_book = "//input[@name='author']"
    select_metabook = "//select[@name='metabook']"
    add_metabook = "//option[@value='23']"
    year_of_translation = "//input[@name='translation_date']"
    lang_book = "//select[@name='language']"
    select_lang_book ="//option[@value='2']"
    add_book_button ="//input[@type='submit']"





    # Getters


    def get_title(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_author_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.author_book)))

    def get_select_metabook(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_metabook)))

    def get_add_metabook(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_metabook)))

    def get_year_of_translation(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_of_translation)))

    def get_lang_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.lang_book)))

    def get_select_lang_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_lang_book)))

    def get_add_book_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_book_button)))





        # Actions


    def input_title(self, title):
        self.get_title().send_keys(title)
        print("Input title")


    def input_author_book(self,author_book):
        self.get_author_book().send_keys(author_book)
        print("Input author book")


    def click_select_metabook(self):
        self.get_select_metabook().click()
        print("click select metabook")

    def click_add_metabook(self):
        self.get_add_metabook().click()
        print("Click add metabook")

    def input_year_of_translation(self,year_of_translation):
        self.get_year_of_translation().send_keys(year_of_translation)
        print("Input year of translation")

    def click_lang_book(self):
        self.get_lang_book().click()
        print("Click lang_book")


    def click_select_lang_book(self):
        self.get_select_lang_book().click()
        print("Click select lang book")


    def click_add_book_button(self):

        self.get_add_book_button().click()
        print("Click add book button")






    # Methods


    def add_book(self):
        with allure.step("Add book"):
            Logger.add_start_step(method="add_book")
            self.input_title("It")
            self.input_author_book("King")
            # self.click_select_metabook()
            # self.click_add_metabook()
            self.input_year_of_translation("1840")
            self.click_lang_book()
            self.click_select_lang_book()
            self.click_add_book_button()


    def accept_alert(self):
        with allure.step("Accept alert"):

            self.alert = self.driver_g.switch_to.alert
            self.alert.accept()
            time.sleep(1)
            self.alert.accept()
            Logger.add_end_step(url=self.driver_g.current_url, method="accept_alert")















