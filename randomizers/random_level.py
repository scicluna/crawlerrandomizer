import random


def random_level(min: int, max: int) -> int:
    """Generates a random level between the min and max provided. If min is greater than max, the values are swapped."""
    if min > max:
        min, max = max, min

    return random.randint(min, max)