print("OOP_LA#4", "Name: Sumaylo, Joseph L. ")

class MLBB():
    def __init__(self, name, role):
        self.name = name 
        self.role = role
    
    def __str__(self):
        return f"{self.name} is a {self.role}."
    
hero1 = MLBB("Clint", "Marksman")
print(hero1)