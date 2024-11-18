import random
from monster import Monster  
class Location:
    def __init__(self, description):
        self.description = description
        self.monster = None
        self.item = None

    def enter(self, player, game):
        print(self.description)

        if random.choice([True, False]):
            self.monster = random.choice(game.monster_types)
            self.monster.level = random.randint(player.level, player.level + self.monster.level_diff)
            print(f"A {self.monster.name} (Level {self.monster.level}) appears!")
            
            if isinstance(self.monster, Monster):
                self.start_combat(player)
            else:
                print("No monster to fight in this encounter.")
        else:
            self.item = random.choice(game.loot_items)
            print(f"You found a {self.item.name}!")
            player.add_item(self.item)

    def start_combat(self, player):
        if not isinstance(self.monster, Monster):
            print("No monster to fight in this encounter.")
            return

        print(f"Starting Combat!")
        print(f"{player.name} - Level: {player.level} | HP: {player.health} | Mana: {player.mana}")
        print(f"{self.monster.name} - Level: {self.monster.level} | HP: {self.monster.health}")

        while player.is_alive() and self.monster.is_alive():
            print("\n--- New Turn ---")
            print(f"{player.name} - HP: {player.health} | Mana: {player.mana}")
            print(f"{self.monster.name} - HP: {self.monster.health}")

            player.update_skill_duration()
            self.monster.update_skill_duration()

            action = input("Do you want to (A)ttack, (S)kill, or (I)tem? ").lower()
            player_action_taken = False

            if action == "a":
                player.attack(self.monster)
                player_action_taken = True
            elif action == "s":
                if player.mana >= 10:
                    player_action_taken = player.choose_skill_in_combat() 
                else:
                    print("Not enough mana!")
            elif action == "i":
                if player.use_item_in_combat() is not None:
                    player_action_taken = True
            else:
                print("Invalid choice. Please choose a valid action.")

            if player_action_taken and self.monster.is_alive():
                self.monster.attack(player)
            elif not player_action_taken:
                print("You return to the main menu without taking an action.")

            if not self.monster.is_alive():
                experience_gained = 10 * self.monster.level
                print(f"{self.monster.name} is defeated! You gained {experience_gained} XP.")
                player.gain_experience(experience_gained)
