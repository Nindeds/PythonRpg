# player.py
from entity import Entity
from skill import Skill
from item import Item
import random

class Player(Entity):
    def __init__(self):
        super().__init__("Bob", health=100)
        self.level = 15
        self.experience = 0
        self.next_level_xp = 100
        self.mana = 50
        self.max_mana = 50
        self.inventory = []
        self.attack_power = 500
        self.defense = 0
        self.spell_damage = 0
        self.skills = self.initialize_skills()
        self.active_skill = None
        self.skill_duration = 0

    def initialize_skills(self):
        return {
            "Power Strike": Skill("Power Strike", "Increases attack power by 5.", "attack", 5, mana_cost=10),
            "Iron Skin": Skill("Iron Skin", "Increases defense by 3.", "defense", 3, mana_cost=10),
            "Healing Light": Skill("Healing Light", "Heals 20 health points.", "health", 20, mana_cost=15),
            "Fireball": Skill("Fireball", "Deals 10 extra damage for 3 turns.", "attack", 10, mana_cost=15),
            "Lightning Strike": Skill("Lightning Strike", "Deals 15 extra damage for 3 turns.", "attack", 15, mana_cost=20)
        }

    def add_item(self, item):
        print(f"{self.name} found a {item.name}!")
        self.inventory.append(item)

    def choose_skill_in_combat(self):
        available_skills = {k: v for k, v in self.skills.items() if v.mana_cost <= self.mana}
        print("Choose a skill for this combat:")
        for idx, (skill_name, skill) in enumerate(available_skills.items(), 1):
            print(f"{idx}. {skill.name} ({skill.mana_cost} mana): {skill.description}")
        print("0. Go Back")

        while True:
            choice = input("Enter the number of the skill you want to use or 0 to go back: ")
            if choice == "0":
                print("Returning to main combat menu.")
                return False
            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(available_skills):
                    skill_name = list(available_skills.keys())[choice]
                    self.active_skill = available_skills[skill_name]
                    self.skill_duration = self.active_skill.duration
                    self.mana -= self.active_skill.mana_cost
                    print(f"You have selected the skill: {self.active_skill.name}")
                    self.active_skill.apply(self)
                    return True
                else:
                    print("Invalid choice.")
            else:
                print("Invalid input.")

    def use_item_in_combat(self):
        if not self.inventory:
            print("No items in inventory.")
            return None

        print("Choose an item to use:")
        for idx, item in enumerate(self.inventory, 1):
            print(f"{idx}. {item.name} - {item.effect} ({item.effect_amount})")
        print("0. Go Back")

        while True:
            choice = input("Enter the number of the item you want to use or 0 to go back: ")
            if choice == "0":
                print("Returning to main combat menu.")
                return None
            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(self.inventory):
                    selected_item = self.inventory.pop(choice)
                    selected_item.use(self)
                    print(f"You used {selected_item.name}!")
                    return selected_item
                else:
                    print("Invalid choice.")
            else:
                print("Invalid input.")

    def update_skill_duration(self):
        if self.skill_duration > 0:
            self.skill_duration -= 1
            if self.skill_duration == 0 and self.active_skill:
                self.active_skill.remove(self)
                self.active_skill = None
                print(f"{self.name}'s skill effect has expired.")

    def attack(self, target):
        """Attack the target with a chance of critical hit and miss."""
        if random.random() < 0.2:
            print(f"{self.name}'s attack missed!")
            return

        base_damage = self.attack_power + self.spell_damage

        if random.random() < 0.1:
            print("Critical hit!")
            base_damage *= 2


        total_damage = max(base_damage - target.defense, 0)
        print(f"{self.name} attacks {target.name} for {total_damage} damage!")
        target.health -= total_damage

    def gain_experience(self, amount):
        """Gain experience and level up if threshold is reached."""
        self.experience += amount
        print(f"{self.name} gained {amount} experience points! Total XP: {self.experience}/{self.next_level_xp}")

    
        while self.experience >= self.next_level_xp:
            self.level_up()

    def level_up(self):
        """Increase the player's level and improve stats."""
        self.level += 1
        self.experience -= self.next_level_xp
        self.next_level_xp += 100  #
        self.health += 10  
        self.mana = self.max_mana  
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"Health: {self.health}, Attack Power: {self.attack_power}, Mana: {self.mana}")
