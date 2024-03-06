from classes.crawler_items import Items
from classes.crawler_stats import Stats


class Status:
    """A class to represent the status of a crawler"""
    def __init__(self, crawler_class: str, level: int):
        self.crawler_class = crawler_class
        self.level = level
        self.items = Items(level)
        self.stats = Stats(level)