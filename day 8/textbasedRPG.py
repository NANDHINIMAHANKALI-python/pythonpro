import random

# Character class
class Character:
    def __init__(self, name, character_class, health, attack):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        enemy.take_damage(damage)
        return damage

# Enemy class
class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, "Enemy", health, attack)

# Function to create a character
def create_character():
    print("Create your character:")
    name = input("Enter name: ")
    character_class = input("Enter class (Warrior/Mage/Rogue): ")
    health = random.randint(50, 100)
    attack = random.randint(10, 20)
    return Character(name, character_class, health, attack)

# Function to explore and engage in battles
def explore():
    player = create_character()
    print(f"Welcome to the RPG World, {player.name}!")

    while player.is_alive():
        choice = input("Do you want to explore (1) or quit (2)? ")
        if choice == "1":
            enemy = Enemy("Monster", random.randint(30, 60), random.randint(5, 15))
            print(f"A wild {enemy.name} appears!")
            while enemy.is_alive() and player.is_alive():
                print(f"{player.name} (Health: {player.health}) vs. {enemy.name} (Health: {enemy.health})")
                action = input("Do you want to attack (1) or run (2)? ")
                if action == "1":
                    damage = player.attack_enemy(enemy)
                    print(f"{player.name} attacks {enemy.name} for {damage} damage!")
                    if enemy.is_alive():
                        enemy_damage = enemy.attack_enemy(player)
                        print(f"{enemy.name} counterattacks for {enemy_damage} damage!")
                elif action == "2":
                    print(f"{player.name} runs away from {enemy.name}!")
                    break
                else:
                    print("Invalid choice. Try again.")
        elif choice == "2":
            print(f"{player.name} decides to quit the game.")
            break
        else:
            print("Invalid choice. Try again.")

    if not player.is_alive():
        print(f"{player.name} has been defeated! Game over.")

# Main game loop
if __name__ == "__main__":
    print("Welcome to the RPG World!")
    while True:
        start = input("Do you want to start a new game (1) or quit (2)? ")
        if start == "1":
            explore()
        elif start == "2":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")
