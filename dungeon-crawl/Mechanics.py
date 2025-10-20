import numpy as np

# Generates randomized stats based on a level, power multiplier, health mulitplier
def characteristics(level, power_multiplier, health_multiplier):
        power = round((np.random.uniform(level-1, level) * level + 1) * power_multiplier)
        health = round((np.random.uniform(level-1, level) * level + 2) * health_multiplier)
        return (power, health)

lvl1 = characteristics(1, 3, 15)
lvl2 = characteristics(2, 3, 15)
lvl3 = characteristics(3, 3, 15)
lvl4 = characteristics(4, 3, 15)
lvl5 = characteristics(5, 3, 15)

def monster_movement(battle_mode, x, y, dt):
        while battle_mode:
                x += np.random.randint(-100, 100)
                return (x, y)
        else:
                return (x, y)