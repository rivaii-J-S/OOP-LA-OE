print("Sumaylo-BSIT2B-LA11")
class phone():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def describePhone(self):
        print(f"The phone brand is {self.brand} and {self.model}")

class android(phone):
    def __init__(self, brand, model):
        phone.__init__(self,brand, model)

p = phone("realme","5pro")
p.describePhone()
a = android("realme", "C2")
a.describePhone()
