import requests

class Test_user_joke():

    def __init__(self):
        pass


    def User_joke_test(self):
        """Вход в систему и вывод категорий"""

        all_category = 'animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel'
        conclusion_category = int(input("Нажмите 1,чтобы увидеть категории шуток.\nНажмите 2,чтобы выйти.\n"))

        """Основная логика выдачи шутки"""


        if conclusion_category == 1:
            print(str(all_category) + "\n Введите название нужной Вам категории.")
            name_category = str(input())
            category_url = "https://api.chucknorris.io/jokes/random?category=" + name_category
            result = requests.get(category_url)
            check = result.json()
            check_value = check.get('value')
            print(f"Вывод шутки из категории {"'"}{name_category}{"'"} : " + str(check_value))
        else:
            exit("Bye Bye")



User = Test_user_joke()
User.User_joke_test()

