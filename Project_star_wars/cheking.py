import json

from requests import Response
from utils.api import Star_wars_api



staticmethod
def check_json_search_word_in_value(response: Response, field_name, search_name):
    check = response.json()
    check_info = check.get(field_name)
    if search_name in check_info:
        print("Слово " + search_name + " присутствует !")
    else:
        print("Слово " + search_name + " отсутствует !")