
class Vehicle:
  def __init__(self, brand):
      self.brand = brand
  def show(self):
    return f"Brand: {self.brand}"
class Car(Vehicle):
  def __init__(self, brand, model):
   super().__init__(brand)
   self.model = model
  def show(self):
   return f"{super().show()}, Model: {self.model}"
car = Car("Tesla", "Model S")
print(car.show())
