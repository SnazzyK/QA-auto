import app
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):



    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    registration_button = "//button[@class='aF98pScNC iF7Uw2lEW bF98pScNC']"
    main_word_2 = "//h1[@class='a3La7AH14 b3La7AH14 cart-page__title']"


    # Getters



    def get_registration_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_button)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))










        # Actions


    def click_registration_button(self):
        self.get_registration_button().click()
        print("Click registration button")







    # Methods

    def select_registration(self):
        self.click_registration_button()
        self.assert_word(self.get_main_word_2(), "Корзина")


