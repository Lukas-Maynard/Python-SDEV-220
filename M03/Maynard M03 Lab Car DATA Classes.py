"""
Car Creator with data classes
Lukas Maynard
SDEV - 220
Practice using data classes to store data needed from a user
"""
from dataclasses import dataclass

@dataclass
class Vehicle:
    type: str = 'Car'

    def setType(self, type):
        self.type = type
    
    def __str__(self):
        return f'Vehicle type: {self.type}'

@dataclass
class Automobile(Vehicle):
    year: str = None
    make: str = None
    model: str = None
    doors: str = None
    roof: str = 'solid'

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