print("SUMAYLO-BSIT2B-LA25")

import abc
from abc import ABC, abstractmethod
class Character(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass
class Batman(Character):
    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    @property
    def alias(self):
        return self.__alias

bat = Batman("Peter Parker", "Spiderman")
print(bat.alias)
