from ai.get_bio import get_bio


class Bio:
    def __init__(self, lvl: int):
        """Generates a Bio which contains a random alignment, personality traits, story, strengths, weaknesses, and twist."""
        #use langchain to generate random alignment, personality traits, story, strengths, weaknesses, and twist
        bio_json = get_bio(lvl)