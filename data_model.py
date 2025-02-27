class Weapon:
    def __init__(self, data):
        self.name = data['name']
        self.damage = data['damage']

class Enemy:
    def __init__(self, data):
        self.name = data['name']
        self.health = data['health']
        self.armor = data['armor']
        self.attack = data['attack']

class Player:
    def __init__(self, data):
        self.name = data['name']
        self.health = data['health']
        self.armor = data['armor']

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.armor)  # Armor snižuje damage
        self.health -= actual_damage
        print(f"{self.name} took {actual_damage} damage! Remaining health: {self.health}")
