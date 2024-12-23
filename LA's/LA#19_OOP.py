print("SUMAYLO-BSIT2B-LA19")

class Favorite_food():
    def __init__(self,name,main_ingredient,onion,carrot):
        self.__name = name
        self._main_ingredient = main_ingredient
        self.__onion = onion
        self._carrot = carrot

    def __str__(self):
        return f"My favorite food is {self.__name} and the main ingredients are {self._main_ingredient}, {self.__onion}, {self._carrot}"

food1 = Favorite_food("lumpia_shanghai", "rabbit" , "sibuyas" , "karot")
print(food1)
print(food1._main_ingredient)
print(food1.__carrot)
