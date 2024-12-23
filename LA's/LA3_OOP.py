print("OOP_LA#3", "Name: Sumaylo, Joseph L. ")

class MLBB: 
    def __init__(self, name, role):
        self.name = name
        self.role = role
   
    def heroDiscription(self): 
        return f"{self.name} is a {self.role}."
    
hero1 = MLBB("Kagura", "Mage")
print(hero1.heroDiscription())