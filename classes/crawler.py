from classes.crawler_bio import Bio
from classes.crawler_status import Status


class Crawler:
    def __init__(self, crawler_name: str, crawler_status: Status, crawler_bio: Bio):
        self.crawler_name = crawler_name
        self.crawler_status = crawler_status
        self.crawler_bio = crawler_bio
        # Add more attributes as needed (e.g., equipment, skills, stats)
        # Class/Stats/Good Items/Personality Traits/Alignment/Story Thus Far/Strengths/Weaknesses/Twist
