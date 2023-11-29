from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base
from utilites.logger import Logger
import allure



class Login_page(Base):

    url = "http://localhost:8080/auth/authentication"


    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators

    user_login = "//input[@name='login']"
    user_password = "//input[@name='password']"
    login_button = "//*[@id='authForm']/div[3]/input"
    main_word = "/html/body/div[2]/div/div/table/tbody/tr[10]/td/a"


    # Getters


    def get_user_login(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def get_user_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))



        # Actions


    def input_user_login(self, user_login):
        self.get_user_login().send_keys(user_login)
        print("Input user login")


    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("Input user password")


    def click_login_button(self):

        self.get_login_button().click()
        print("Click login button")




    # Methods


    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.get_current_url()
            self.driver_g.get(self.url)
            self.driver_g.maximize_window()
            self.input_user_login("Брайан")
            self.input_user_password("12345")
            self.click_login_button()
            self.assert_word(self.get_main_word(), "Log out")
            Logger.add_end_step(url=self.driver_g.current_url,method="authorization")









