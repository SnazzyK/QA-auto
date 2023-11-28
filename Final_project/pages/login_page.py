from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Login_page(Base):

    url = "https://kdvonline.ru/signinemail"


    def __init__(self,driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    # entry_button = "//a[@data-toggle='modal']"
    # entry_pass_button = "//a[@class='js-login-way']"
    user_login = "//input[@type='email']"
    user_password = "//input[@type='password']"
    login_button = "//button[@class='iegjPvHGb aHIc+wd-z dHIc+wd-z qHIc+wd-z']"
    main_word = "//h2[@class='a3La7AH14 c3La7AH14 C3La7AH14 fHid9UWLQ']"


    # Getters

    # def get_entry_button(self):
    #     return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.entry_button)))

    def get_user_login(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def get_user_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

        # Actions



    # def click_entry_button(self):
    #     self.get_entry_button().click()
    #     print("Click entry button")

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
        self.get_current_url()
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.input_user_login("toster28auto@gmail.com")
        self.input_user_password("Qwerty12345")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Рекомендуем вам")








