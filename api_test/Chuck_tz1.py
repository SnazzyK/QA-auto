import requests

class Test_joke_category():

    def __init__(self):
        pass


    def joke_cetegory(Test_all_category):
        """Метод для вывода всех категорий"""

        url = "https://api.chucknorris.io/jokes/categories"
        print(url)
        result = requests.get(url)
        print("Вывод всех категорий : " + str(result.json()))

        """Функция для вывода 1 шутки по каждой категории"""
        for i in result.json():
            categorys_url = "https://api.chucknorris.io/jokes/random?category=" + (i)
            try:
                result = requests.get(categorys_url)
                if result.status_code ==200:

                    check = result.json()
                    check_value = check.get('value')
                    print(f"Вывод шутки из категории {"'"}{i}{"'"} : "  + str(check_value))
                else:
                    print("Что то не так.")
            except:
                print("Хммм.ошибка.")



test_category = Test_joke_category()
test_category.joke_cetegory()