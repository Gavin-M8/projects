import pandas as pd

# WEAPONS

kin = 'Kinetic'
fir = 'Fire'
ele = 'Electric'
ice = 'Ice'

high = 1.0
med = 0.75
low = 0.5
vlow = 0.25

weapon_data = {
        'name':['Rusty Sword', 'Broken Bow', 'Cracked Staff', 'Death Stick', 'The Icicle', 'Razorbeam'], 
        
        'damage':[3, 5, 4, 25, 12, 18], 

        'type':[kin, kin, fir, ele, ice, kin],

        'precision':[high, low, med, vlow, high, high]
}

weapons = pd.DataFrame(weapon_data)


# ACCESSORIES

lvl1 = 1
lvl2 = 3
lvl3 = 5
lvl4 = 7
lvl5 = 10

none = None
loot = "Looting"
heal = "Healing"
rage = "Damage"
accu = "Accuracy"

accessory_data = {
        'name': ['Busted Shield', 'Shiny Amulet', 'Emerald Pendant', 'Keen Monocle', 'Crimson Cloak', 'Polished Boots', 'Hands of Providence'],

        'defense':[lvl2, lvl2, lvl3, lvl1, lvl3, lvl4, lvl5],

        'ability':[none, loot, heal, accu, rage, none, none]
}

accessories = pd.DataFrame(accessory_data)


# CONSUMABLES

long = "Long"
brief = "Brief"
short = "Short"
instant = "Instant"

consumable_data = {
        'name':['Apple Pie', 'Glowing Potion', 'Golden Chicken Nugget', "Hot Coal"],

        'buff':[heal, rage, loot, rage], 

        'duration':[instant, brief, long, short]
}

consumables = pd.DataFrame(consumable_data)