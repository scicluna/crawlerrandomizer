import json
import os
import httpx

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), http_client=httpx.Client(verify=False))

def get_ai_json(crawler_class: str, crawler_level: int, item_types: list, ai_detailed: str):
    """
    Returns a json object containing the AI for a crawler
    use openai to generate random items, alignment, personality traits, story, strengths, weaknesses, and twist
    """

    prompt = generate_ai_prompt(crawler_class, crawler_level, item_types)
    model = "gpt-4-1106-preview" if ai_detailed == "y" else "gpt-3.5-turbo-0125"

    print(f"Generating AI response using {model}")
    response = client.chat.completions.create(
    model= model,
    response_format={ "type": "json_object" },
    temperature=0.7,
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



def generate_ai_prompt(crawler_class: str, crawler_level: int, item_types: list):
    """Returns a string containing a prompt for the AI to generate a crawler"""
    prompt = f"""
        In 2020, the Earth was "flattened," reducing its population by 99.99999%. The survivors find themselves in two categories: those who remained on the surface, and those who ventured into "The Crawl." "The Crawl" is not just a dungeon; it's an interstellar pay-per-view television event watched by countless alien civilizations. This dungeon is bizarre, merciless, and sadistic, designed for entertainment. Participants who reach the end win, reclaiming some of what humanity lost. 

        This crawler has braved the following floors:
        Floor One: The first floor of "The Crawl" is a classic fantasy labyrinth filled with odd low-leveled creatures and themed areas. The odd creatures are all based around combining a fantasy race with an earthen stereotype, making for a unique and challenging starting point for crawlers.

        Within this context, create a detailed profile for a Dungeon Crawl Classics character. The character, used to be a normal human, but was assigned the class: "{crawler_class}" and at level {crawler_level} out of 10 in their daunting journey, is one of the daring crawlers. 
        
        For each item type listed below, generate ONE unique, powerful, and strangely named item:
        Item Types: {', '.join(item_types)}

        The character's profile should include a randomly chosen alignment (CH for Chaotic, LA for Lawful, N for Neutral), three distinctive personality traits, a brief background of their modern (the year is 2020) life before entering "The Crawl," and a concise narrative highlighting their key adventures and challenges faced so far in the game. Also, include three strengths and three weaknesses that define them. Finally, incorporate a twist that makes this character uniquely intriguing. Structure the generated information in JSON format as shown below:

        {{
            "good_items": ["Example Item 1: brief description", "Example Item 2: brief description", "Example Item 3: brief description", "etc..."],
            "alignment": "CH",
            "personality_traits": ["trait1", "trait2", "trait3"],
            "origin": "A brief sentence about their life before 'The Crawl'.",
            "story": "A paragraph detailing their journey, key adventures, and challenges in 'The Crawl'.",
            "strengths": ["strength1", "strength2", "strength3"],
            "weaknesses": ["weakness1", "weakness2", "weakness3"],
            "twist": "A unique and intriguing twist about the character. Maybe something they regret doing in the crawl, or a strange quest hook they've come across, or even strange goals."
        }}
    """
    return prompt
