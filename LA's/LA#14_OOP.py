class Spiderman:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    def describeSpiderman(self):
        print(f"Hero: {self.name} | Age: {self.age} ")
        
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)  
        self.movieTitle = movieTitle 
    
class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
           
class Tom(Spiderman):
    def __init__(self, name, age, movieTtile):
        super().__init__(name, age)
        self.movieTitle = movieTtile
        
Spidey1 = Tobey("Tob", "20", "Spiderman")
Spidey2 = Andrew("Andrew", "30", "The Amazing Spiderman")
Spidey3 = Tom("Tom", "19", "Spiderman: Far from Home")

Spidey1.describeSpiderman()
Spidey2.describeSpiderman()
Spidey3.describeSpiderman()

print(Spidey1.name.upper(), Spidey1.movieTitle.upper())
print(Spidey2.name.upper(), Spidey2.movieTitle.upper())
print(Spidey3.name.upper(), Spidey3.movieTitle.upper())