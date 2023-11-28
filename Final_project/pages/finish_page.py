import app
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Finish_page(Base):



    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    text_area = "//textarea[@id='comment']"
    first_name = "//input[@id='firstname']"
    last_name = "//input[@id='lastname']"
    phone = "//input[@id='phone']"




    # Getters



    def get_text_area(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_area)))

    def get_first_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))





        # Actions


    def input_text_area(self,text_area):
        self.get_text_area().send_keys(text_area)
        print("Input text area")

    def delete_my_first_name(self):
        self.get_first_name().send_keys(Keys.CONTROL + "a")
        self.get_first_name().send_keys(Keys.DELETE)

    def input_first_name(self,first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def delete_my_last_name(self):
        self.get_last_name().send_keys(Keys.CONTROL + "a")
        self.get_last_name().send_keys(Keys.DELETE)

    def input_last_name(self,last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def delete_my_phone(self):
        self.get_phone().send_keys(Keys.CONTROL + "a")
        self.get_phone().send_keys(Keys.DELETE)
    def input_phone(self,phone):
        self.get_phone().send_keys(phone)
        print("Input phone")








    # Methods

    def input_data(self):
        self.input_text_area("Передаю привет Алексу!!!)")
        self.delete_my_first_name()
        self.input_first_name("Valeriy")
        self.delete_my_last_name()
        self.input_last_name("Kaurov")
        self.delete_my_phone()
        self.input_phone("00000000000")
        self.get_screenshot()