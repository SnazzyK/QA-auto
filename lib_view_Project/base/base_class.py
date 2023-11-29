import datetime

class Base():
    def __init__(self, driver_g):
        self.driver_g = driver_g




    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("current url " + get_url)




    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print("Good value url")






    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word ")





    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver_g.save_screenshot(
            'C:\\Users\\snazz\\PycharmProjects\\QA-auto\\Final_project\\screen\\' + name_screenshot)
