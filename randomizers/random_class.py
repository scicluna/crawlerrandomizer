import random
from lists.classes import core_classes, weird_classes

def random_class():
    chosen_list = random.choices(
        population=[core_classes, weird_classes],
        weights=[75, 25],
        k=1
    )[0]
    return random.choice(chosen_list)