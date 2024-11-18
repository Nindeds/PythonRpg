class Skill:
    def __init__(self, name, description, buff_type, buff_amount, mana_cost, duration=3):
        self.name = name
        self.description = description
        self.buff_type = buff_type
        self.buff_amount = buff_amount
        self.mana_cost = mana_cost  
        self.duration = duration 
    def apply(self, entity):
        if self.buff_type == "attack":
            entity.attack_power += self.buff_amount
            print(f"{entity.name}'s attack power increased by {self.buff_amount}!")
        elif self.buff_type == "health":
            entity.health = min(100, entity.health + self.buff_amount)
            print(f"{entity.name}'s health increased by {self.buff_amount}!")
        elif self.buff_type == "defense":
            entity.defense += self.buff_amount
            print(f"{entity.name}'s defense increased by {self.buff_amount}!")

    def remove(self, entity):
        if self.buff_type == "attack":
            entity.attack_power -= self.buff_amount
            print(f"{entity.name}'s attack power buff has expired.")
        elif self.buff_type == "defense":
            entity.defense -= self.buff_amount
            print(f"{entity.name}'s defense buff has expired.")
