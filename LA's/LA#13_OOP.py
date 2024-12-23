class Animal():
        def __init__(self, name, type):
            pass
        
class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.name = name
        self.type = type
        self.can_swim = True
        
    def fishInfo(self):
        print(f"Name: {self.name} | Type: {self.type}")
    

fiish = Fish("Tilapia", "Fish",)
fiish.fishInfo()
print(f"Can swim? {fiish.can_swim}")
            

            