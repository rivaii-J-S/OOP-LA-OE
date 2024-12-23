class Appliance:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
        
    def operate(self):
        print("Operating!")
    def info(self):
        print(f"This appliance has a brand name '{self.brand}' and the model is {self.model}.")
   
        
class WashingMachine(Appliance):

    def operate(self):
        print("Washing clothes")
        
class Refrigirator(Appliance):
    def operate(self):
        print("Keeping Food Cold!")
        
class Microwave(Appliance):
    print("Heating food!")
    
WM = WashingMachine("Samsung", "SM1")
Ref = Refrigirator("Condura", "CND2")
MC = Microwave("Hanabishi", "HNB3")

for Appliance in [WM, Ref, MC]:
    Appliance.operate()
    Appliance.info()
