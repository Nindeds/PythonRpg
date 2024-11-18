class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0
