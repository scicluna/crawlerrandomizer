class Bio:
    def __init__(self, ai_json: dict):
        """Generates a Bio which contains a random alignment, personality traits, story, strengths, weaknesses, and twist."""
        self.alignment = ai_json['alignment']
        self.personality_traits = ai_json['personality_traits']
        self.origin = ai_json['origin']
        self.story = ai_json['story']
        self.strengths = ai_json['strengths']
        self.weaknesses = ai_json['weaknesses']
        self.twist = ai_json['twist']
