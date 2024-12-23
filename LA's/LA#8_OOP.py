class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
info = Book("NARUTO", "Masashi Kishimoto")

print(f"Book: ", info.title)
print(f"Author: ", info.author)
del info.author
print("Deleted author: ", info.author)

info2 = Book ("ONE PIECE", "Eiichiro Oda")
print(f"Book: ", info2.title)
print(f"Author: ", info2.author)