from ai.get_ai_json import get_ai_json
from classes.crawler_bio import Bio
from classes.crawler_items import Items
from classes.crawler_stats import Stats
from randomizers.random_item_types import random_item_types


class Crawler:
    """A class to represent a crawler"""
    def __init__(self, crawler_name: str, crawler_class: str, ai_detailed:str, crawler_level: int):
        self.crawler_name = crawler_name
        self.crawler_class = crawler_class
        self.crawler_level = crawler_level

        ai_json = get_ai_json(crawler_class, crawler_level, random_item_types(crawler_level), ai_detailed)

        self.crawler_stats = Stats(crawler_level)
        self.crawler_bio = Bio(ai_json)
        self.crawler_items = Items(ai_json)
    
    def __str__(self):
        return f"{self.crawler_name} the {self.crawler_class} is a level {self.crawler_level} crawler with the following stats: \n" \
                f"Strength: {self.crawler_stats.str} ({self.crawler_stats.str_mod})\n" \
                f"Agility: {self.crawler_stats.agi} ({self.crawler_stats.agi_mod})\n" \
                f"Stamina: {self.crawler_stats.sta} ({self.crawler_stats.sta_mod})\n" \
                f"Intelligence: {self.crawler_stats.int} ({self.crawler_stats.int_mod})\n" \
                f"Psersonality: {self.crawler_stats.per} ({self.crawler_stats.per_mod})\n" \
                f"Luck: {self.crawler_stats.luc} ({self.crawler_stats.luc_mod})\n" \
                f"HP: {self.crawler_stats.hp}\n" \
                f"AC: {self.crawler_stats.ac}\n" \
                f"Reflex: {self.crawler_stats.ref}\n" \
                f"Fortitude: {self.crawler_stats.fort}\n" \
                f"Will: {self.crawler_stats.will}\n" \
                f"Crawlers Bio:\n" \
                f"Alignment: {self.crawler_bio.alignment}\n" \
                f"Personality Traits: {', '.join(self.crawler_bio.personality_traits)}\n" \
                f"Origin: {self.crawler_bio.origin}\n" \
                f"Story: {self.crawler_bio.story}\n" \
                f"Strengths: {', '.join(self.crawler_bio.strengths)}\n" \
                f"Weaknesses: {', '.join(self.crawler_bio.weaknesses)}\n" \
                f"Twist: {self.crawler_bio.twist}\n"
                