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





    """Method assert price"""

    # def assert_price(self, price_1, price_2, price_3):
    #     value_price_1 = float(price_1.text)
    #     print(value_price_1)
    #
    #     value_price_2 = float(price_2.text)
    #     print(value_price_2)
    #
    #     value_price_3 = float(price_3.text)
    #     print(value_price_3)
    #
    #     total = value_price_1 + value_price_2
    #     assert total == value_price_3
    #     print("Good value price")





    """Method Screenshot"""

    def get_screenshot(self):
        now_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_time + '.png'
        self.driver_g.save_screenshot(f"..\\Final_project\\screen\\screenshot {now_time}.png" + name_screenshot)



