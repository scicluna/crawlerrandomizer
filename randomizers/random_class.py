import random
from lists.classes import core_classes, weird_classes


def random_class():
    """ Returns a random class from the core_classes and weird_classes lists """
    chosen_list = random.choices(
        population=[core_classes, weird_classes],
        weights=[0, 100],
        k=1
    )[0]
    return random.choice(chosen_list)