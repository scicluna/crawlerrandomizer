from classes.crawler_bio import Bio
from classes.crawler_stats import Stats
from randomizers.random_item_types import random_item_types


class Crawler:
    """A class to represent a crawler"""
    def __init__(self, crawler_name: str, crawler_class: str, crawler_level: int):
        self.crawler_name = crawler_name
        self.crawler_class = crawler_class
        self.crawler_level = crawler_level

        ai_json = get_ai_json(crawler_class, crawler_level, random_item_types(crawler_level))

        self.crawler_stats = Stats(crawler_level, ai_json)
        self.crawler_bio = Bio(crawler_level, ai_json)
    