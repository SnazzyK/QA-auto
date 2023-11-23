class Cat():

    def __init__(self,name , color ,isHungry ):

        self.set_data(name ,color,isHungry)
        self.come_cat()

    def set_data(self,name ,color,isHungry=None):
        self.name = name
        self.color = color
        self.isHungry = isHungry
    def come_cat(self):
        print("У меня есть кошка,её зовут - " + str(self.name),", цвет у неё - " + str(self.color), "Голод - " + str(self.isHungry))


Cat1 = Cat('Busya','Grey',False)



