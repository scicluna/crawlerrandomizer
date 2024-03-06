import random
from randomizers.random_roll import random_roll 
from lists.mods import mods
from lists.luck_signs import luck_signs_table


class Stats:
    """A class to represent the stats of a crawler"""
    def __init__(self, lvl: int):
        self.str = random_roll(3,6) + random.randint(1,lvl)
        self.agi = random_roll(3,6) + random.randint(1,lvl)
        self.sta = random_roll(3,6) + random.randint(1,lvl)
        self.int = random_roll(3,6) + random.randint(1,lvl)
        self.per = random_roll(3,6) + random.randint(1,lvl)
        self.luc = random_roll(3,6) + random.randint(1,lvl)

        self.str_mod = mods[self.str]
        self.agi_mod = mods[self.agi]
        self.sta_mod = mods[self.sta]
        self.int_mod = mods[self.int]
        self.per_mod = mods[self.per]
        self.luc_mod = mods[self.luc]

        self.hp = (random_roll(1,4)) + ((lvl+1) * self.sta_mod) + (lvl * random.randint(1,10))
        self.ac = (10 + lvl + self.agi_mod + random.randint(1,4) + random.randint(1,lvl))

        self.ref = self.agi_mod+lvl+max((random.randint(1,lvl)-random.randint(1,(lvl))), 0)
        self.fort = self.sta_mod+lvl+max((random.randint(1,lvl)-random.randint(1,(lvl))), 0)
        self.will = self.per_mod+lvl+max((random.randint(1,lvl)-random.randint(1,(lvl))), 0)

        self.luck_sign = random.choice(luck_signs_table)