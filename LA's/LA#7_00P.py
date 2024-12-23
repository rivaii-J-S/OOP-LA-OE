class Car():
    def __init__(self, brand, color):
        self.brand = brand 
        self.color = color
        
vehicle = Car("Ford", "Black")
print(f"Car brand is {vehicle.brand}, the color is {vehicle.color}.")

vehicle2 = Car("Ford", "Gray")
print(f"Car brand is {vehicle2.brand}, updated color is {vehicle2.color}.")
    