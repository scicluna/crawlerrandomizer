import random
from ai.get_items import get_items
from lists.item_slots import item_slots_table


class Items:
    def __init__(self, lvl):
        """Generates a list of good items based on the crawler's level."""
        item_types = []
        for _ in range(lvl):
            item_types.append(random.choice(item_slots_table))
        
        #use langchain to generate random items using gpt 3.5
        good_item_names = get_items(item_types)

        self.good_items = []
        for item in good_item_names:
            self.good_items.append(item)

        
        