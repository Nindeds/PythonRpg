from player import Player
from location import Location
from monster import Monster
from item import Item
from skill import Skill
import random

class Game:
    def __init__(self):
        self.player = Player()
        self.locations = {}
        self.visited_zones = set() 
        self.boss_zone_unlocked = False  
        self.create_world()

    def create_world(self):
        self.locations["start"] = Location("You are in a forest, surrounded by trees.")
        self.locations["east"] = Location("You venture deeper into the forest.")
        self.locations["north"] = Location("The trees are dense, and the air is thick.")
        self.locations["west"] = Location("A small clearing with a shimmering light.")
        self.locations["south"] = Location("A quiet area with a clear path back to the start.")
        self.locations["boss"] = Location("You face the terrifying forest boss!")
        
        self.loot_items = [
            Item("Healing Potion", "heal", 20),
            Item("Mana Potion", "mana", 20),
            Item("Attack Boost", "attack_boost", 5),
            Item("Defense Boost", "defense_boost", 5),
        ]

        self.monster_skills = [
            Skill("Poison Strike", "Inflicts poison for 3 turns.", "attack", 5, mana_cost=10),
            Skill("Fury", "Increases attack power by 5.", "attack", 5, mana_cost=10),
            Skill("Howl", "Increases defense by 3.", "defense", 3, mana_cost=10),
            Skill("Inferno", "Deals 20 extra damage.", "attack", 20, mana_cost=15),
            Skill("Stone Skin", "Increases defense by 10.", "defense", 10, mana_cost=15)
        ]

        self.monster_types = [
            Monster("Goblin", base_health=30, base_attack_power=8, player_level=0, level_diff=3, skills=[self.monster_skills[0]]),
            Monster("Wolf", base_health=40, base_attack_power=10, player_level=0, level_diff=3, skills=[self.monster_skills[1]]),
            Monster("Orc", base_health=50, base_attack_power=12, player_level=0, level_diff=4, skills=[self.monster_skills[2]]),
            Monster("Troll", base_health=60, base_attack_power=14, player_level=0, level_diff=4, skills=[self.monster_skills[3]]),
            Monster("Spider", base_health=20, base_attack_power=5, player_level=0, level_diff=2, skills=[self.monster_skills[0]]),
            Monster("Skeleton", base_health=35, base_attack_power=9, player_level=0, level_diff=3, skills=[self.monster_skills[1]]),
            Monster("Zombie", base_health=45, base_attack_power=10, player_level=0, level_diff=3, skills=[self.monster_skills[2]]),
            Monster("Wraith", base_health=50, base_attack_power=12, player_level=0, level_diff=3, skills=[self.monster_skills[3]]),
            Monster("Minotaur", base_health=70, base_attack_power=16, player_level=0, level_diff=5, skills=[self.monster_skills[4]]),
            Monster("Vampire", base_health=55, base_attack_power=13, player_level=0, level_diff=4, skills=[self.monster_skills[4]])
        ]

    def start_game(self):
        print("Welcome to the RPG game!")
        print(f"Your character's name is {self.player.name}.")
        self.game_loop()

    def game_loop(self):
        current_location = "start" 
        while self.player.is_alive():
            if current_location not in self.locations:
                print("Error: Location not found!")
                break

            self.locations[current_location].enter(self.player, self)

            if current_location in ["east", "north", "west", "south"]:
                self.visited_zones.add(current_location)


            if len(self.visited_zones) >= 4 and self.player.level >= 10:
                self.boss_zone_unlocked = True

            if not self.player.is_alive():
                print("You have been defeated. Game Over.")
                break

            if current_location == "boss" and not self.locations["boss"].monster.is_alive():
                print("Congratulations! You have defeated the boss and won the game!")
                break

            print("\nWhere would you like to go?")
            print("1. Go East\n2. Go North\n3. Go West\n4. Go South (Back to Start)")
            if self.boss_zone_unlocked:
                print("5. Go to the Boss Zone")

            choice = input("Choose a direction: ")

            if choice == "1":
                current_location = "east"
            elif choice == "2":
                current_location = "north"
            elif choice == "3":
                current_location = "west"
            elif choice == "4":
                current_location = "south"
            elif choice == "5" and self.boss_zone_unlocked:
                current_location = "boss"
            else:
                print("Invalid choice. Please enter a valid option.")

    def save_game(self):
        print("Game saved (placeholder).")

    def load_game(self):
        print("Game loaded (placeholder).")
