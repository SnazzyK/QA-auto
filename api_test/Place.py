import requests


class Test_new_loctaion():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации POST"""

        base_url = "https://rahulshettyacademy.com"  # Базовая url
        key = "?key=qaclick123"  # Параметр для всех запросов
        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {

                "lat": -38.383494,

                "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

                "shoe park",

                "shop"

            ],

            "website": "http://google.com",

            "language": "French-IN"

        }

        result_post = requests.post(post_url,json=json_for_create_new_location)
        print(result_post.json())

        assert 200 == result_post.status_code
        print("Успешно!!Создана новая локанция")
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Статус код ответа : " + check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верен")
        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)



        """Проверка создание новой локации  GET """


        get_resource = "/maps/api/place/get/json"
        get_url = base_url  + get_resource  + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.json())

        assert 200 == result_get.status_code
        print("Успешно!!Создана новая локанция")


        """Изменение новой локации Put"""

        put_resourse = "/maps/api/place/update/json"
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,

            "address": "100 Lenina street, RU",

            "key": "qaclick123"
        }

        result_put = requests.put(put_url,json=json_for_update_new_location)
        print(result_put.json())

        assert 200 == result_put.status_code
        print("Успешно!!Изменена новая локанция")
        check_put = result_put.json()
        check_info_put = check_put.get("msg")
        print("Сообщение " + check_info_put)
        assert check_info_put == 'Address successfully updated'
        print("Сообщение верно: " + check_info_put)




        """Проверка изменение новой локации GET"""

        result_get = requests.get(get_url)
        print(result_get.json())

        assert 200 == result_get.status_code
        print("Проверка изменения локации ,прошло успешно")
        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print("Сообщение " + check_address_info)
        assert check_address_info == '100 Lenina street, RU'
        print("Сообщение верно: " )

        """Удаление новой локации DELETE"""

        delete_resourse = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url,json = json_for_delete_new_location)
        print(result_delete.json())

        assert 200 == result_delete.status_code
        print("Проверка удаления локации ,прошло успешно")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Сообщение " + check_status_info)
        assert check_status_info == 'OK'

        







new_place = Test_new_loctaion()
new_place.test_create_new_location()
