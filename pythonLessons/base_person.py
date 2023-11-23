class Person():
    """"Саоздаем человека"""

    def __init__(self,name,age,height, weight = None,hair = None):
        self.name=name
        self.age = age
        self.height = height
        self.weight = weight
        self.hair = hair

    def get_person(self):
        get_data=" Имя = " + str(self.name) + "\n Возраст = " + str(self.age) + "\n Рост = " + str(self.height) + "\n Вес = " + str(self.weight) + "\n Волосы = " +str(self.hair)
        print(get_data)
    def update_weight(self,kg):
        self.weight = kg

class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self,name ,age ,height,weight ,hair ):
        '''Иниациализируем атрибуты'''
        super().__init__(name,age,height,weight,hair )
        self.range = 100

    def get_range(self):
        print("Заряд ярости равен :" + str(self.range) )

    def get_person(self):
            get_data = " Имя = " + str(self.name) + "\n Возраст = " + str(self.age) + "\n Рост = " + str(
                self.height) + "\n Заряд его ярости равен :" + str(self.range)
            print(get_data)

