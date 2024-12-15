import random
import time

class Gladiator:
    # Class representing a gladiator (player).
    def __init__(self, name, health, attack, defense, potions=3):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.potions = potions

    def attack_enemy(self, enemy):
        # Attack an enemy.
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        print(f"{self.name} deals {damage} damage to {enemy.name}!")

    def block(self):
        # Increase defense for one turn.
        self.defense += 3
        print(f"{self.name} blocks, increasing defense by 3!")

    def use_potion(self):
        # Use a healing potion.
        if self.potions > 0:
            heal_amount = random.randint(15, 30)
            self.health = min(self.health + heal_amount, self.max_health)
            self.potions -= 1
            print(f"{self.name} uses a potion and heals {heal_amount} health points!")
        else:
            print(f"{self.name} has no potions left!")

    def reset_block(self):
        # Reset defense after a turn.
        self.defense = max(self.defense - 3, 0)

    def is_alive(self):
        # Check if the gladiator is still alive.
        return self.health > 0


class Enemy:
    # Class representing an enemy.
    def __init__(self, name, health, attack, defense, critical_strike=False, regeneration=False):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.critical_strike = critical_strike
        self.regeneration = regeneration

    def attack_gladiator(self, gladiator):
        # Attack the gladiator.
        damage = self.attack

        if self.critical_strike and random.random() < 0.2:  # 20% chance for critical strike.
            damage *= 2
            print(f"{self.name} lands a CRITICAL STRIKE!")

        damage = max(0, damage - gladiator.defense)
        gladiator.health -= damage
        print(f"{self.name} deals {damage} damage to {gladiator.name}!")

    def regenerate(self):
        # Heal a portion of health if regeneration ability is active.
        if self.regeneration:
            heal_amount = random.randint(5, 15)
            self.health += heal_amount
            print(f"{self.name} regenerates {heal_amount} health!")

    def is_alive(self):
        # Check if the enemy is still alive.
        return self.health > 0


def create_enemy(level):
    # Create an enemy with random stats based on level.
    health = random.randint(30, 50) + level * 5
    attack = random.randint(5, 10) + level
    defense = random.randint(1, 5) + level // 2
    name = random.choice(["Wolf", "Bandit", "Knight", "Ogre", "Troll", "Demon"])

    # Introduce abilities from the 3rd enemy onwards.
    critical_strike = level >= 3 and random.random() < 0.5  # 50% chance for critical strike.
    regeneration = level >= 3 and random.random() < 0.5    # 50% chance for regeneration.

    return Enemy(name, health, attack, defense, critical_strike, regeneration)


def display_stats(gladiator, enemy):
    # Display dynamic and visually structured stats for gladiator and enemy.
    print("\n" + "="*30)
    print(f"GLADIATOR: {gladiator.name}")
    print(f"Health: {gladiator.health}/{gladiator.max_health}")
    print(f"Attack: {gladiator.attack} | Defense: {gladiator.defense}")
    print(f"Potions: {gladiator.potions}")
    print("="*30)
    print(f"ENEMY: {enemy.name}")
    print(f"Health: {enemy.health}")
    print(f"Attack: {enemy.attack} | Defense: {enemy.defense}")
    if enemy.critical_strike:
        print("Special Ability: Critical Strike")
    if enemy.regeneration:
        print("Special Ability: Regeneration")
    print("="*30)


def battle(gladiator, enemy):
    # Single battle between the gladiator and an enemy.
    while gladiator.is_alive() and enemy.is_alive():
        display_stats(gladiator, enemy)  # Use the new display function for stats.

        print("\nChoose an action:")
        print("1. Attack")
        print("2. Block")
        print("3. Use a potion")

        choice = input("Your choice: ")

        while choice not in ['1', '2', '3']:
            print("Invalid choice! Please choose again.")
            choice = input("Your choice: ")

        if choice == '1':
            gladiator.attack_enemy(enemy)
        elif choice == '2':
            gladiator.block()
        elif choice == '3':
            gladiator.use_potion()

        if enemy.is_alive():
            enemy.attack_gladiator(gladiator)

            # Enemy uses regeneration ability if applicable.
            enemy.regenerate()

        gladiator.reset_block()
        time.sleep(1)

    if gladiator.is_alive():
        print(f"You defeated {enemy.name}!")
    else:
        print(f"You were defeated by {enemy.name}!")


def level_up(gladiator):
    # Level up the gladiator's stats.
    print("\nCongratulations! You leveled up.")
    print("Choose what to increase:")
    print("1. Increase health (+10)")
    print("2. Increase attack (+2)")
    print("3. Increase defense (+2)")

    choice = input("Your choice: ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice! Please choose again.")
        choice = input("Your choice: ")

    if choice == '1':
        gladiator.max_health += 10
        gladiator.health += 10
    elif choice == '2':
        gladiator.attack += 2
    elif choice == '3':
        gladiator.defense += 2

    time.sleep(1)


def main():
    # Main game loop.
    print("Welcome to the Gladiator Arena!")
    name = input("Enter the name of your gladiator: ")

    while not name.isalpha():
        print("Invalid name! Please use only letters.")
        name = input("Enter the name of your gladiator: ")

    gladiator = Gladiator(name, 100, 10, 5)

    level = 1
    while gladiator.is_alive():
        print(f"\n--- LEVEL {level} ---")
        enemy = create_enemy(level)
        battle(gladiator, enemy)

        if not gladiator.is_alive():
            print(f"Game over! {gladiator.name} was defeated.")
            break

        if level == 12:
            print("Congratulations! You have won the game by defeating 12 enemies!")
            break

        level_up(gladiator)
        level += 1

    print("\nThank you for playing Gladiator Arena!")


if __name__ == "__main__":
    main()
