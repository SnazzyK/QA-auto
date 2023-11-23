import requests

class Test_new_joke():

    """Создание новой шутку """


    def __init__(self):
        pass

    def test_create_new_joke(self):

        """Создание случайной шутки"""

        #
        # url = "https://api.chucknorris.io/jokes/random"
        # print(url)
        # result = requests.get(url)
        # print("Статус код : " + str(result.status_code))
        # assert 200 == result.status_code
        # print("Успешно!!Мы получили новую шутку")
        # result.encoding = 'utf-8'
        # print(result.json())
        # check = result.json()
        # # check_info = check.get('categories')
        # # print(check_info)
        # # assert check_info == []
        # # print("Категория верна")
        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = 'Chuck'
        # if name in check_info_value:
        #     print("Chuck тут ")
        # else:
        #     print("Chuck`а нету ")
        #

    def test_create_new_random_categories_joke(self):

        """Создание случайной  шутки в категории"""

        category = "sport"

        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print(" " + str(result.status_code))
        assert 200 == result.status_code
        print("Успешно!!Мы получили новую шутку")
        result.encoding = 'utf-8'
        print(result.json())
        check = result.json()
        check_info = check.get('categories')
        # print(check_info)
        # assert check_info == ["sport"]
        # print("Категория верна")
        check_info_value = check.get('value')
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print("Chuck тут ")
        else:
            print("Chuck`а нету ")



sport_joke = Test_new_joke()
sport_joke.test_create_new_random_categories_joke()
