import requests

class Test_place():
    """Работа с новой локацией"""
    def create_place(self):
        """Создание новой локации POST"""
        base_url = "https://rahulshettyacademy.com"  # Базовая url
        resource_url = "/maps/api/place/add/json"    # Ресурс метода Post
        key="?key=qaclick123"                        # Параметр для всех запросов

        post_url = base_url + resource_url + key
        print(post_url)
        json_for_create_new_location={
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
        for i in range(5):
            result_post = requests.post(post_url, json=json_for_create_new_location)
            print(result_post.json())
            check_post = result_post.json()
            place_id = check_post.get("place_id")
            print("Place_id : " + place_id)
            fw = open('doc/place_id_file.txt', 'a')
            fw.write(place_id + "\n")
            fw.close()





        """Проверка создание новой локации  GET """



        for i in range(1):
            fr = open('doc/place_id_file.txt', 'r')
            text = fr.readline()
            fr.close()


            get_resource = "/maps/api/place/get/json"
            get_url = base_url + get_resource + key + "&place_id=" + text.strip()
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.json())

            """Удаление локаций DELETE"""


            delete_resourse = "/maps/api/place/delete/json"
            delete_url  = base_url + delete_resourse + key
            print(delete_url)
            json_for_create_delete_location={
                "place_id" : 'fc9904bff7abcfa1991322729e7ad17f'
            }

            result_delete = requests.delete(delete_url ,json=json_for_create_delete_location )
            print(result_delete.json())


    def test_delete_new_location(self):

        """Delete new location"""

        base_url = "https://rahulshettyacademy.com"  # Base URL
        key = "?key=qaclick123"  # Parameter
        delete_resource = "/maps/api/place/delete/json" # delete resource
        delete_url = base_url + delete_resource + key
        print(delete_url)

        fr = open("place_id.txt")
        n = 0
        for i in fr.read().splitlines():
            n += 1
            if n in (2, 4):
                json_for_delete_new_location = {
                "place_id": i
                }
                result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
                print(result_delete.text)
                assert 200 == result_delete.status_code
                print("Status code: " + str(result_delete.status_code))
                check_status = result_delete.json()
                check_status_info = check_status.get("status")
                assert check_status_info == "OK"
                print("Status: " + check_status_info)
















local=Test_place()
local.create_place()