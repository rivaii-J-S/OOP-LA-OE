class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        damage = self.power
        target.health -= damage
        target.health = max(0, target.health)  # Ensure health doesn't go below zero
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        print(f"{target.name}'s remaining health: {target.health}")

    def special_move(self):
        print(f"{self.name} uses a generic special move!")

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        self.health -= reduced_damage
        self.health = max(0, self.health)
        print(f"{self.name} defends! Takes {reduced_damage} damage. Remaining health: {self.health}")


class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power *= 2  # Doubles power for the next attack


class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball!")
        print(f"{self.name} deals 100 damage directly!")
        self.power = 100  # Deals a fixed large amount of damage


class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow!")
        print(f"{self.name}'s next attack ignores defenses!")


class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50
        print(f"{self.name}'s health increases to {self.health}")


# Create objects for each class
warrior = Warrior("Warrior", 150, 20)
mage = Mage("Mage", 100, 15)
archer = Archer("Archer", 120, 18)
monster = Monster("Monster", 200, 25)

# Simulate a battle
print("\n--- Battle Start ---")
characters = [warrior, mage, archer]

# Each character attacks and uses their special move on the Monster
for character in characters:
    character.attack(monster)
    character.special_move()

# Monster retaliates by attacking and using its special move on each character
for character in characters:
    monster.attack(character)
    monster.special_move()

# Demonstrate polymorphism by calling special_move() for each character
print("\n--- Demonstrating Polymorphism ---")
all_characters = [warrior, mage, archer, monster]
for character in all_characters:
    character.special_move()

# Display final health states
print("\n--- Final Health States ---")
for character in all_characters:
    print(f"{character.name}: {character.health} HP")