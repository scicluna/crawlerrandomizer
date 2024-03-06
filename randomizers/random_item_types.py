import random
from lists.item_slots import item_slots_table


def random_item_types(lvl: int) -> list[str]:
    """Randomizes the item types for the crawler"""
    random_item_types = []
    for _ in range(lvl):
        rng = random.randint(1,2)

        if rng == 1:
            continue

        random_item_types.append(random.choice(item_slots_table))
        
    return random_item_types