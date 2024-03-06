class Status:
    def __init__(self, crawler_class: str, level: int, crawler_stats: Stats, crawler_items: Items):
        self.crawler_class = crawler_class
        self.level = level
        self.crawler_stats = crawler_stats
        self.crawler_items = crawler_items
        # Add more attributes as needed (e.g., equipment, skills, stats)
        # Class/Stats/Good Items/Personality Traits/Alignment/Story Thus Far/Strengths/Weaknesses/Twist