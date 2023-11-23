class Car():
    def __init__(self,model = None,year = None,engine_capacity = None,price = None,number_of_wheels = None ):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.price = price
        self.number_of_wheels = number_of_wheels

    def get_car(self):
        get_info = " Модель  : " + str(self.model) + "\n Год выпуска : " + str(self.year) + "\n Объем двигателя : " +  str(self.engine_capacity) + "\n Цена : " + str(self.price) + "$\n Количество колес : " + str(self.number_of_wheels)
        # print(get_info)

        return get_info





class Truck(Car):
    def __init__(self,model,year,engine_capacity,price,number_of_wheels  ):
        super().__init__(model,year,engine_capacity,price,number_of_wheels )





FirstCar = Car('Supra',1989,3.2,12000, 4)
# FirstCar.get_car()
print("У представленной машашины :\n" + FirstCar.get_car() )

FirstTruck = Car('Gazel`' ,'2005' ,2.2,1500,8)
# # FirstTruck.get_car()
print('----------------')
print("У представленной машашины :\n" + FirstTruck.get_car() )
