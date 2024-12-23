print("SUMAYLO-BSIT2B-OE7")

class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def decorator(*args, **kwargs):
            print("..... executing a function")
            result = func(*args, **kwargs) 
            print("This character is strong!")
            return result  
        return decorator

char = TekkenCharacter("Jade", "Fatal Judgement")

@char.introduce
def character_intro():
    print(f"I am {char.name}, and I can use {char.ability}")
character_intro()
