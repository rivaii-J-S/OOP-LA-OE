print("SUMAYLO-BSIT2B-LA18")

class Favorite_food():
    def __init__(self,name,main_ingredient,onion,carrot):
        self.__name = name
        self.__main_ingredient = main_ingredient
        self.__onion = onion
        self.__carrot = carrot

    def __str__(self):
        return f"My favorite food is {self.__name} and the mian ingredients are {self.__main_ingredient}, {self.__onion}, {self.__carrot}"

food1 = Favorite_food("lumpia_shanghai", "baboy" , "sibuyas" , "karot")
food2 = Favorite_food("adobo" , "chicken" , "soy sauce" ,"vinegar")
food3 = Favorite_food("bread", "flour" , "egg" , "baking powder")

for i in [food1,food2,food3]:
    print(i)