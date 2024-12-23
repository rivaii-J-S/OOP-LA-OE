print("OOP_OE#1 |", "Name: Sumaylo, Joseph L. ")
print("")

class heroTeam():
    def __init__(self, name, role, damageType):
        self.name = name
        self.role = role
        self.damageType = damageType
   
    def __str__(self):
        return f"{self.name} | {self.role} : {self.damageType}"
 
print("WELCOME TO RIVAII ESPORTS")  
print("")  
hero1 = heroTeam("Hayabusa", "Assassin", "Physical")
print(hero1)
hero2 = heroTeam("Kagura", "Mage", "Magic")
print(hero2)
hero3 = heroTeam("Clint", "Marksman", "Physical")
print(hero3)
hero4 = heroTeam("Tigreal", "Tank", "Physical")
print(hero4)
hero5 = heroTeam("Ruby", "Fighter", "Physical")
print(hero5)

