import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from utilites.logger import Logger
import allure



class Add_author_page(Base):



    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators

    name_eng = "//input[@name='english_name']"
    name_ru = "//input[@name='russian_name']"
    name_ge = "//input[@name='german_name']"
    name_fr = "//input[@name='french_name']"
    year_of_birth ="//input[@name='birth_date']"
    year_of_death ="//input[@name='death_date']"
    lang_author = "//select[@name='language']"
    select_lang_author = "//option[@value='4']"
    add_button = "//input[@type='submit']"
    enter_button = "/html/body/div[2]"





    # Getters


    def get_name_eng(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_eng)))

    def get_name_ru(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_ru)))

    def get_name_ge(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_ge)))

    def get_name_fr(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_fr)))

    def get_year_of_birth(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_of_birth)))

    def get_year_of_death(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_of_death)))

    def get_lang_author(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.lang_author)))

    def get_select_lang_author(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_lang_author)))

    def get_add_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_button)))

    # def get_enter_button(self):
    #     return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))



        # Actions


    def input_name_eng(self, name_eng):
        self.get_name_eng().send_keys(name_eng)
        print("Input name english")


    def input_name_ru(self, name_ru):
        self.get_name_ru().send_keys(name_ru)
        print("Input name russian")


    def input_name_ge(self,name_ge):

        self.get_name_ge().send_keys(name_ge)
        print("Input name german")

    def input_name_fr(self,name_fr):
        self.get_name_fr().send_keys(name_fr)
        print("Input name french")

    def input_year_of_birth(self,year_of_birth):
        self.get_year_of_birth().send_keys(year_of_birth)
        print("Input year of birth")

    def input_year_of_death(self,year_of_death):
        self.get_year_of_death().send_keys(year_of_death)
        print("Input year of death")


    def click_lang_author(self):
        self.get_lang_author().click()
        print("Click lang author")


    def click_select_lang_author(self):
        self.get_select_lang_author().click()
        print("Click select lang author")

    def click_add_button(self):
        self.get_add_button().click()
        print("Click add button")



    # def click_enter_button(self):
    #     self.get_enter_button().send_keys(Keys.ENTER)



    # Methods

    def add_author(self):
        with allure.step("Add author"):
            Logger.add_start_step(method="add_author")
            self.input_name_eng("King")
            self.input_name_ru("Кинг")
            self.input_name_ge("King")
            self.input_name_fr("King")
            self.input_year_of_birth("1810")
            self.input_year_of_death("1830")
            self.click_lang_author()
            self.click_select_lang_author()
            self.click_add_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="add_author")

    def accept_alert(self):
        with allure.step("Accept alert"):
            Logger.add_start_step(method="accept_alert")
            self.alert = self.driver_g.switch_to.alert
            self.alert.accept()
            time.sleep(1)
            self.alert.accept()
            Logger.add_end_step(url=self.driver_g.current_url, method="accept_alert")











