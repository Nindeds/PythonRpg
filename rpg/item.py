class Item:
    def __init__(self, name, effect, effect_amount):
        self.name = name
        self.effect = effect
        self.effect_amount = effect_amount

    def use(self, player):
        if self.effect == "heal":
            player.health = min(100, player.health + self.effect_amount)
            print(f"{player.name} heals {self.effect_amount} health points!")
        elif self.effect == "attack_boost":
            player.attack_power += self.effect_amount
            print(f"{player.name}'s attack power increases by {self.effect_amount}!")
        elif self.effect == "defense_boost":
            player.defense += self.effect_amount
            print(f"{player.name}'s defense increases by {self.effect_amount}!")

    def remove(self, player):
        if self.effect == "attack_boost":
            player.attack_power -= self.effect_amount
            print(f"{player.name}'s attack power boost has expired.")
        elif self.effect == "defense_boost":
            player.defense -= self.effect_amount
            print(f"{player.name}'s defense boost has expired.")
