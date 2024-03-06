import random


def random_roll(n, d):
    """Rolls n dice with d sides and returns the sum of the rolls."""
    return sum([random.randint(1, d) for _ in range(n)])