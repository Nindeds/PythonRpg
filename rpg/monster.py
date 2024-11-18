from entity import Entity
import random

class Monster(Entity):
    def __init__(self, name, base_health, base_attack_power, player_level, level_diff, skills=[]):
        # Monster Stat
        super().__init__(name, health=base_health)
        self.base_attack_power = base_attack_power
        self.player_level = player_level
        self.level_diff = level_diff
        self.skills = skills
        self.level = random.randint(player_level, player_level + level_diff)
        self.attack_power = base_attack_power + (self.level * 2)  
        self.defense = 5 + (self.level * 1)  
        
    def attack(self, target):
        if random.random() < 0.2:
            print(f"{self.name}'s attack missed!") #Chance of missing hit
            return

        base_damage = self.attack_power
        if random.random() < 0.1:  #Critical hit
            print("Critical hit!")
            base_damage *= 2

        total_damage = max(base_damage - target.defense, 0)
        print(f"{self.name} attacks {target.name} for {total_damage} damage!")
        target.health -= total_damage

    def update_skill_duration(self):
        """Update the duration of active skills for the monster."""
        for skill in self.skills:
            if skill.duration > 0:
                skill.duration -= 1
                if skill.duration == 0:
                    skill.remove(self)
                    print(f"{self.name}'s skill effect {skill.name} has expired.")
