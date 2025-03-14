# prompt: vehical class python code

class Vehicle:
    def __init__(self, brand, model, color, fuel_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Fuel Type: {self.fuel_type}")

# Example usage
my_vehicle = Vehicle("Toyota", "Camry", "Silver", "Gasoline")
my_vehicle.display_info()
