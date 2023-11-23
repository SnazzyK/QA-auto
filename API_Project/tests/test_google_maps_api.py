import json
import allure
from requests import Response
from utils.checking import Checking
from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локациии """

@allure.epic("Test create place")
class Test_create_place():


    @allure.description("Test create,update,delete new place")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))
        Checking.check_json_value(result_post,'status','OK')




        print("Метод GET")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")
        # token = json.loads(result_get.text)
        # print(list(token))



        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, "msg", "Address successfully updated")


        print("Метод GET - PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get,'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete,['status'])
        Checking.check_json_value(result_delete,'status','OK')

        print("Метод GET - DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get,['msg'])
        Checking.check_json_search_word_in_value(result_get,'msg','failed')

        print("Тестирование создание, изменение и удаление новой локации прошло успешно!!")



