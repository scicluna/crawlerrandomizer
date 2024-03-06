def get_ai_json(crawler_class: str, crawler_level: int, item_types: list):
    """
    Returns a json object containing the AI for a crawler
    use langchain to generate random items, alignment, personality traits, story, strengths, weaknesses, and twist
    """
    return {
        "items": item_types,
        "alignment": "Neutral",
        "personality_traits": "Loyal, Brave, and Kind",
        "story": "A wandering warrior who seeks to bring peace to the world",
        "strengths": "High health and damage",
        "weaknesses": "Low speed and accuracy",
        "twist": "Is actually a robot"
    }