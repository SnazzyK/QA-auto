from utils.http_method import  Http_methods


"""Методы для тестирования star wars api"""

base_url = "https://swapi.dev/"

class Star_wars_api():

    """Метод для вызова персонажа"""

    @staticmethod
    def get_people():


        get_resourse = "api/people/"
        num_people = "1"
        # for i in num_people:
        #     if i < 81 :
        #         i+1
        #     print(num_people)

        get_url = base_url + get_resourse + str(num_people) + "/"
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")











        # get_url = base_url + get_resourse + str(num_people) + "/"
        # print(get_url)
        # result_get = Http_methods.get(get_url)
        # print(result_get.json())
        # return result_get