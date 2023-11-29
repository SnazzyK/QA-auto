from datetime import time
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from utilites.logger import Logger
import allure



class Add_text_page(Base):


    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    time.sleep(5)
    area_text = "//textarea[@name='text']"
    add_text_button = "//input[@type='submit']"







    # Getters


    def get_area_text(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.area_text)))

    def get_add_text_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_text_button)))





        # Actions


    def input_area_text(self,area_text):
        self.get_area_text().send_keys(area_text)
        print("Input text")

    def click_add_text_button(self):
        self.get_add_text_button().click()
        print("Click add text button text")








    # Methods


    def add_text(self):
        with allure.step("Add text"):
            Logger.add_start_step(method="add_text")
            self.input_area_text("{Glava1\nText\n{")
            self.click_add_text_button()
            Logger.add_end_step(url=self.driver_g.current_url, method="add_text")


    def accept_alert(self):
        with allure.step("Accept alert"):
            Logger.add_start_step(method="accept_alert")
            self.alert = self.driver_g.switch_to.alert
            self.alert.accept()
            time.sleep(1)
            self.alert.accept()
            Logger.add_end_step(url=self.driver_g.current_url, method="accept_alert")











