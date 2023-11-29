from datetime import time
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from utilites.logger import Logger
import allure



class My_books_page(Base):


    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators








    # Getters










        # Actions










    # Methods



    def accept_books(self):
        with allure.step("Accept books"):
            Logger.add_start_step(method="accept_books")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver_g.current_url, method="accept_books")













