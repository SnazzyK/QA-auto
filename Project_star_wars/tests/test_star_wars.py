import json

from requests import Response
from utils.api import Star_wars_api

"""Показ персонажа"""

class Test_get_people():
    def test_give_new_people(self):
        print("Метод GET")
        result_get = Star_wars_api.get_people()


