class Vehicle():
    def __init__(self, brand, model, fuelType):
        self.brand = brand
        self.model = model
        self.fuelType = fuelType
        
    def describeVehicle(self):
        return f"Brand: {self.brand} | Model: {self.model} | Fuel: {self.fuelType}"
    
class Car(Vehicle):
        pass

class Motorcycle(Vehicle):
        pass
    
car1 = Car("Toyota", "Hilux", "diesel")
print(car1.describeVehicle())
car2 = Motorcycle("Honda", "Click", "kerosene")   
print(car2.describeVehicle())
           