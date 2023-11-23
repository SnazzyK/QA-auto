

import requests



for i in range(1, 81):

        url = f'https://swapi.dev/api/people/{i}/'
        response = requests.get(url)


        if response.status_code == 200:
            data = response.json()
            # Проверяем, что поле "name" присутствует в данных
            if 'name' in data:
                name = data['name']
                print(f"Name для числа {i}: {name}")
                fw = open('names_people.txt', 'a',encoding='utf-8')
                fw.write(str(name + "\n"))
            else:
                print(f"Поле 'name' отсутствует в данных для числа {i}")
        else:
            print(f"Ошибка при выполнении запроса для числа {i}: {response.status_code}")



