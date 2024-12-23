print("SUMAYLO-BSIT2B-LA22")

class Party():
    def __init__(self,food,special,theme):
        self.food = food
        self.special = special
        self.theme = theme
    def __special_food(self):
        print(f"The special is {self.special}")
    def list_food(self):
        self.__special_food()
    def dish_food(self):
        print(f"The food is {self.food}")
   
food1 = Party("ice cream" , "cake" ,"birthday")
food2 = Party("pancit" , "adobo" ,"valentines day")
food3 = Party("fried chicken" , "halo-holo" ,"Christmas")

for i in [food1,food2,food3]:
    i.dish_food()
    i.list_food()