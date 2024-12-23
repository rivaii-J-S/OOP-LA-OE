class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def toysInfo(self):
        return f" Toy name: {self.name} | Toy price: Php{self.price}"
    
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
        
carToy = Car("Scooter", 1200)
print(carToy.toysInfo())
    