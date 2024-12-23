print("SUMAYLO-BSIT2B-LA26")

from turtles import Leonardo, Michelangelo, Donatello, Rapheal

tur1 = Leonardo("Leonardo", "Leon")
tur2 = Michelangelo("Michelangelo", "Mikey")
tur3 = Donatello("Donatello", "Donna")
tur4 = Rapheal("Rapheal", "Rapha")

for i in [tur1,tur2,tur3,tur4]:
    print(i.alias)