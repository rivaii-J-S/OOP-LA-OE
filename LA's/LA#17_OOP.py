class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} cannot attack because they are defeated.")
            return
        damage = self.attack_power
        target.health -= damage
        print(
            f"{self.name} attacks {target.name} for {damage} damage! "
            f"{target.name} has {max(0, target.health)} health remaining."
        )

    def heal(self, amount):
        if self.health > 0:
            self.health += amount
            print(f"{self.name} heals for {amount} points! Current health: {self.health}")
        else:
            print(f"{self.name} cannot heal because they are defeated.")


player1 = Player("Hayabusa", 100, 20)
player2 = Player("Kagura", 80, 25)

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} cannot attack because they are defeated.")
            return
        damage = self.attack_power
        target.health -= damage
        print(
            f"{self.name} attacks {target.name} for {damage} damage! "
            f"{target.name} has {max(0, target.health)} health remaining."
        )

    def heal(self, amount):
        if self.health > 0:
            self.health += amount
            print(f"{self.name} heals for {amount} points! Current health: {self.health}")
        else:
            print(f"{self.name} cannot heal because they are defeated.")


player1 = Player("Hayabusa", 100, 20)
player2 = Player("Kagura", 80, 25)


while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    if player2.health <= 0:
        print(f"{player2.name} has been defeated! {player1.name} wins!")
        break
    player2.attack(player1)
    if player1.health <= 0:
        print(f"{player1.name} has been defeated! {player2.name} wins!")
        break


print("\n--- Bonus Healing Example ---")
player1.heal(15)
player2.heal(10)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    if player2.health <= 0:
        print(f"{player2.name} has been defeated! {player1.name} wins!")
        break
    player2.attack(player1)
    if player1.health <= 0:
        print(f"{player1.name} has been defeated! {player2.name} wins!")
        break


print("\n--- Bonus Healing Example ---")
player1.heal(15)
player2.heal(10)
