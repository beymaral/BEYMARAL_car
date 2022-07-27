# OOP

class Car:
    wheel = 4

    def __init__(self, model, color, owner, year):
        self.model = model
        self.miles = 0
        self.fuel_tank = 0
        self.color = color
        self.owner = owner
        self.year = year

    def get_fuel_tank(self, liter):
        self.fuel_tank += liter
        print(f'You have purchased {liter} liters of gas, you have {self.fuel_tank} in the tank')
        return self.fuel_tank

    def drive(self, km):
        liter = km * 0.1
        if self.fuel_tank >= liter:
            print('We are riding!')
            self.miles += km
            self.fuel_tank -= liter
        else:
            print('Gas insufficient')
    def change_color(self, new_color):
        self.color = new_color
        print(f'Congratulations you have new color - {self.color}')


tesla = Car('Model X', 'White', 'Nazgul', '2022')
porshe = Car('Cayenne', 'red', 'Mirlan', '2022')
tesla.get_fuel_tank(40)
tesla.get_fuel_tank(50)
porshe.get_fuel_tank(40)
tesla.drive(400)
porshe.drive(400)
tesla.change_color('black')
print(tesla.fuel_tank)
print(porshe.fuel_tank)
print(tesla.color)
tesla.wheel = 6
print(tesla.wheel)
print(porshe.wheel)
del tesla.wheel
print(tesla.__dict__)
print(porshe.__dict__)

print(tesla.wheel)
print(porshe.wheel)


porshe.exhaust = 'noise'
print(tesla.__dict__)
print(porshe.__dict__)

