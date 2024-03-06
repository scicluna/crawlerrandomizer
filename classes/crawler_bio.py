class Bio:
    def __init__(self, ai_json: dict):
        """Generates a Bio which contains a random alignment, personality traits, story, strengths, weaknesses, and twist."""
        #use langchain to generate random alignment, personality traits, story, strengths, weaknesses, and twist
        #{'good_items': ['Soulcrusher Mace'], 'alignment': 'CH', 'personality_traits': ['reckless', 'ferocious', 'stubborn'], 'origin': "Before 'The Crawl,' they were a competitive athlete known for their aggressive playing style and never backing down from a challenge.", 'story': "As a Warrior in 'The Crawl,' they have faced numerous challenges on the first floor, including navigating the labyrinth filled with strange creatures and overcoming traps that test their physical strength and combat skills. Their key adventure involved a fierce battle with a Minotaur-like creature that tested their courage and determination. Despite facing setbacks, they emerged victorious, earning the respect of other crawlers.", 'strengths': ['exceptional combat skills', 'high endurance', 'quick reflexes'], 'weaknesses': ['lack of strategic thinking', 'recklessness in decision-making', 'difficulty trusting others'], 'twist': "Despite their fierce demeanor in combat, this character harbors a deep-seated fear of failure and constantly doubts their own abilities, leading to moments of vulnerability and self-doubt during their journey in 'The Crawl.' This inner conflict drives them to push themselves harder to prove their worth to themselves and others."}       
        self.alignment = ai_json['alignment']
        self.personality_traits = ai_json['personality_traits']
        self.origin = ai_json['origin']
        self.story = ai_json['story']
        self.strengths = ai_json['strengths']
        self.weaknesses = ai_json['weaknesses']
        self.twist = ai_json['twist']
