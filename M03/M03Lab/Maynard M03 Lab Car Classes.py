"""
Car Creator
Lukas Maynard
SDEV - 220
Practice using classes to store data needed from a user
"""
class Vehicle:
    def __init__(self, type='Car'):
        self.type = type
        
    def setType(self, type):
        self.type = type
    
    def __str__(self):
        return f'Vehicle type: {self.type}'

class Automobile(Vehicle):
    def __init__(self, year=None, make=None, model=None, doors=None, roof='solid'):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def setYear(self, year):
        self.year = year

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setDoors(self, doors):
        self.doors = doors

    def setRoof(self, roof):
        self.roof = roof

    def __str__(self):
        return '-----------------\n'+\
        super().__str__() +\
        f'\nYear: {UserCar.year}\
        \nMake: {UserCar.make}\
        \nModel: {UserCar.model}\
        \nNumber of doors: {UserCar.doors}\
        \nType of roof: {UserCar.roof}'

UserCar = Automobile()
UserCar.setType(input('Input type of vehicle: '))
print(f'For your {UserCar.type} enter the following: ')
UserCar.setYear(input('Input year: '))
UserCar.setMake(input('Input manufacturer: '))
UserCar.setModel(input('Input model: '))
UserCar.setDoors(input('Input door amount: '))
UserCar.setRoof(input('Input roof type (sun roof or solid): '))
print(UserCar)