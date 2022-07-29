

class Car:
    CompanyName = 'BEYMARAL'

    def __init__(self):
        pass

    def input(self):
        self.name_of_car = str(input('Input a car name:'))
        self.color_of_car = str(input('Input the car color:'))
        self.price_of_car = str(input('Input the car price:'))

    def print(self):
        print(f' Your car is {self.name_of_car}, with color - {self.color_of_car} and price - {self.price_of_car} $')
    @property
    def get_color(self):
        return self.color

    @get_color.setter
    def get_color(self, val):
        self.color = val
        return self.color


car1 = Car()
car1.input()
car1.print()
