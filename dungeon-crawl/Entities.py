import pandas as pd
import numpy as np

class Hero:

    def __init__(self, health, power, defense, intellect, weapons, accessories, consumables, x, y):
        self.health = health
        self.power = power
        self.defense = defense
        self.intellect = intellect
        self.inventory = pd.DataFrame(data = {'weapons':[weapons], 'accessories':[accessories], 'consumables':[consumables]})
        self.active_weapon = self.inventory['weapons'][0]
        self.x = x
        self.y = y

    def attack(self, other):
        other.health -= self.power

    def solve(self):
        return self.intellect > 10

    def heal(self):
        self.health += self.intellect

    def add_weapon(self, item):
        self.inventory['weapons'].append(item)
    
    def add_accessory(self, item):
        self.inventory['accessories'].append(item)

    def add_consumable(self, item):
        self.inventory['consumables'].append(item)

class Monster:

    def __init__(self, name, health, power, defense, intellect, element, drops, drop_chances, position):
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        self.intellect = intellect
        self.element = element
        self.drops = drops
        self.drop_chances = drop_chances
        self.x = position[0]
        self.y = position[1]

    def __str__(self):
        return (f"{self.name}")

    def attack(self, other):
        other.health -= self.power

    def heal(self):
        self.health += self.intellect

    def drop_loot(self, drops, drop_chances):
        return np.random.choice(drops, size = 1, replace = True, p = drop_chances)
    



