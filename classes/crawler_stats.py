import random
from randomizers.random_roll import random_roll 
from lists.mods import mods
from lists.luck_signs import luck_signs_table


class Stats:
    """A class to represent the stats of a crawler"""
    def __init__(self, lvl):
        self.str = random_roll(3,6) + random.randint(1,4)
        self.agi = random_roll(3,6) + random.randint(1,4)
        self.sta = random_roll(3,6) + random.randint(1,4)
        self.int = random_roll(3,6) + random.randint(1,4)
        self.per = random_roll(3,6) + random.randint(1,4)
        self.luc = random_roll(3,6) + random.randint(1,4)

        self.str_mod = mods[self.str]
        self.agi_mod = mods[self.agi]
        self.sta_mod = mods[self.sta]
        self.int_mod = mods[self.int]
        self.per_mod = mods[self.per]
        self.luc_mod = mods[self.luc]

        self.hp = (lvl * self.sta_mod) + (lvl * random.randint(5,10))
        self.ac = (10 + lvl + self.agi_mod + random.randint(1,4))
        self.ref = self.agi_mod+lvl+random.randint(1,6)-random.randint(1,6)
        self.fort = self.sta_mod+lvl+random.randint(1,6)-random.randint(1,6)
        self.will = self.per_mod+lvl+random.randint(1,6)-random.randint(1,6)

        self.luck_sign = random.choice(luck_signs_table)