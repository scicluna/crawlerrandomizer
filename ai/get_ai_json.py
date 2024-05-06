import json
import os
import httpx

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), http_client=httpx.Client(verify=False))

def get_ai_json(crawler_name:str, crawler_class: str, crawler_level: int, crawler_skill: int, crawler_stats, item_types: list, ai_detailed: str) -> dict[str, any]:
    """
    Returns a json object containing the AI for a crawler
    use openai to generate random items, alignment, personality traits, story, strengths, weaknesses, and twist
    """

    prompt = generate_ai_prompt(crawler_name, crawler_class, crawler_level, crawler_skill, crawler_stats, item_types)
    model = "gpt-4-1106-preview" if ai_detailed == "y" else "gpt-3.5-turbo-0125"

    print(f"Generating AI response using {model}... Please Wait.")
    response = client.chat.completions.create(
    model= model,
    response_format={ "type": "json_object" },
    temperature=.8,
    messages=[
        {"role": "user", "content": prompt}
        ]
    )
    text_response = response.choices[0].message.content

    try:
        json_response = json.loads(text_response)
        return json_response
    except json.JSONDecodeError:
        print("Failed to decode JSON from model response.")
        return None



def generate_ai_prompt(crawler_name: str, crawler_class: str, crawler_level: int, crawler_skill: int, crawler_stats, item_types: list):
    """Returns a string containing a prompt for the AI to generate a crawler"""
    prompt = f"""
        In 2020, the Earth was "flattened," reducing its population by 99.99999%. The survivors find themselves in two categories: those who remained on the surface, and those who ventured into "The Crawl." "The Crawl" is not just a dungeon; it's an interstellar pay-per-view television event watched by countless alien civilizations. This dungeon is bizarre, merciless, and sadistic, designed for entertainment. Participants who reach the end win, reclaiming some of what humanity lost. 

        This crawler, who is called {crawler_name}, has only braved the following floors:
        Floor One: The first floor of "The Crawl" is like a classic fantasy dungeon crawl filled with odd low-leveled creatures that are grouped by "neighborhoods". Each neighborhood is named after its primary mob and something that mob is known for (format: [verb]ing [fantasy monster] neighborhood). "Neigborhoods" are guarded by powerful neighborhood bosses. The floor is straight forward, with each neighborhood haivng its own theme.
        Floor Two: The second floor is much the same as the first, only more dangerous and punishing. It was here where the stakes were raised and peril amplified.
        
        Within this context, create a detailed profile for a Dungeon Crawl Classics character. The character, used to be a normal human, but was assigned the class: "{crawler_class}" and at level {crawler_level} out of 10 in their daunting journey, is one of the crawlers. On a skill rank from 1-10, they are considered to be a {crawler_skill}.
        
        The character's stats are as follows:
        HP: {crawler_stats.hp}/{crawler_stats.hp}
        AC: {crawler_stats.ac}
        Reflex: {crawler_stats.ref}
        Fortitude: {crawler_stats.fort}
        Will: {crawler_stats.will}
        Strength: {crawler_stats.str} ({crawler_stats.str_mod})
        Agility: {crawler_stats.agi} ({crawler_stats.agi_mod})
        Stamina: {crawler_stats.sta} ({crawler_stats.sta_mod})
        Intelligence: {crawler_stats.int} ({crawler_stats.int_mod})
        Personality: {crawler_stats.per} ({crawler_stats.per_mod})
        Luck: {crawler_stats.luc} ({crawler_stats.luc_mod})

        The character's profile should include a randomly chosen alignment (C for Chaotic, L for Lawful, N for Neutral), three distinctive personality traits, a brief background of their modern (the year is 2020) life before entering "The Crawl" along with a random profession, and a concise narrative highlighting their key adventures and challenges faced so far in the game using specific examples. Also, include three strengths and three weaknesses that define them. Also, incorporate a twist that makes this character uniquely intriguing. Finally, she should have 3 distinct special abilities that can be derived from her background, class, and items. Structure the generated information in JSON format as shown below:
        For each item type listed below, generate ONE unique, powerful, and strangely named item:
        Item Types: {', '.join(item_types)}
        There are: {len(item_types)} item types in total.
        In addition to these item types, they should have 3-5 signature consumables that they are known to use (they can be generic).
        {{
            "good_items": ["item: brief description"  - repeat for each item type provided],
            "consumables": ["item: brief description"  - repeat for each consumable]
            "alignment": "C or L or N",
            "personality_traits": ["trait1", "trait2", "trait3"],
            "origin": "A brief sentence about their life before 'The Crawl'. Including a plausible country+city of origin and a profession.",
            "story": "A paragraph detailing their journey, key adventures, and challenges in 'The Crawl'.",
            "strengths": ["strength1", "strength2", "strength3"],
            "weaknesses": ["weakness1", "weakness2", "weakness3"],
            "twist": "A unique and intriguing twist about the character. Maybe something they regret doing in the crawl, or a strange quest hook they've come across, or even strange goals.",
            "abilities": ["ability name: brief description and DCC mechanics if possible", "ability name: brief description and DCC mechanics if possible", "ability name: brief description and DCC mechanics if possible"]
        }}
    """
    return prompt
