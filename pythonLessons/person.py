class Person():
    """Модель человека"""

    def __init__(self, name ,age):
        """Инициализиция атрибутов человека - имя , возраст"""
        self.name= name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " Танцует")


man = Person("Valera" , 22)
woman = Person("Julia" , 30)

# print(man.name)

man.sing()
woman.dance()