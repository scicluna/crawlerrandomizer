class Items:
    def __init__(self, ai_json: dict):
        """Generates a list of good items based on the crawler's level."""
        self.good_items = ai_json['good_items']

        
        