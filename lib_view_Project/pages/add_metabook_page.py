from datetime import time
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from utilites.logger import Logger
import allure



class Add_metabook_page(Base):



    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators

    title = "//input[@name='title']"
    author_book = "//select[@name='author']"
    add_author_book = "//option[@value='10']"
    number_of_chapters = "//input[@name='size']"
    language_book = "//select[@name='language']"
    add_language_book = "//option[@value='4']"
    creation_year ="//input[@name='create_date']"
    add_metabook_button ="//input[@type='submit']"





    # Getters


    def get_title(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_author_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.author_book)))

    def get_add_author_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_author_book)))

    def get_number_of_chapters(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_of_chapters)))

    def get_language_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.language_book)))

    def get_add_language_book(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_language_book)))

    def get_creation_year(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.creation_year)))

    def get_add_metabook_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_metabook_button)))





        # Actions


    def input_title(self, title):
        self.get_title().send_keys(title)
        print("Input title")


    def click_author_book(self):
        self.get_author_book().click()
        print("Click author book")


    def click_add_author_book(self):
        self.get_add_author_book().click()
        print("click add author book")

    def input_number_of_chapters(self,number_of_chapters):
        self.get_number_of_chapters().send_keys(number_of_chapters)
        print("Input number of chapters")

    def click_language_book(self):

        self.get_language_book().click()
        print("Click language book")

    def click_add_language_book(self):

        self.get_add_language_book().click()
        print("Click add language book")


    def input_creation_year(self,creation_year):

        self.get_creation_year().send_keys(creation_year)
        print("Input creation year")


    def click_add_metabook_button(self):

        self.get_add_metabook_button().click()
        print("Click add metabook button")






    # Methods


    def add_metabook(self):
        with allure.step("Add metabook"):
            Logger.add_start_step(method="add_metabook")
            self.input_title("Оно")
            self.click_author_book()
            self.click_add_author_book()
            self.input_number_of_chapters("1")
            self.click_language_book()
            self.click_add_language_book()
            self.input_creation_year("1830")
            self.click_add_metabook_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="add_metabook")

    def accept_alert(self):
        with allure.step("Accept alert"):
            Logger.add_start_step(method="accept_alert")
            self.alert = self.driver_g.switch_to.alert
            self.alert.accept()
            time.sleep(1)
            self.alert.accept()
            Logger.add_end_step(url=self.driver_g.current_url, method="accept_alert")












