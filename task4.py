#Creating Multiple Objects
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Focus", 2022)
