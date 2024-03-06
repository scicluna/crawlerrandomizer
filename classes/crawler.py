from classes.crawler_bio import Bio
from classes.crawler_items import Items
from classes.crawler_status import Status


class Crawler:
    def __init__(self, crawler_name: str, crawler_class: str, crawler_level: int):
        self.crawler_name = crawler_name
        self.crawler_class = crawler_class
        self.crawler_level = crawler_level

        self.status = Status(crawler_level)
        self.bio = Bio(crawler_level)