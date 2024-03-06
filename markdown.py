from classes.crawler import Crawler


def save_crawler_profile(crawler, filename="crawler_profile.md"):
    """Saves a Crawler object to a Markdown file."""
    with open(f"markdown_files/{filename}", "w") as file:
        file.write(generate_markdown(crawler))
        print(f"Crawler profile saved to {filename}")

def generate_markdown(crawler: Crawler) -> None:
    """Converts a Crawler object to a Markdown-formatted string."""
    newline = '\n'

    markdown_content = (
        f"**Class:** {crawler.crawler_class}\n"
        f"**Level:** {crawler.crawler_level}\n\n"

        f"## Stats:\n"
        f"**HP:** {crawler.crawler_stats.hp}/{crawler.crawler_stats.hp}\n"
        f"**AC:** {crawler.crawler_stats.ac}\n\n"

        f"**Reflex:** {crawler.crawler_stats.ref}\n"
        f"**Fortitude:** {crawler.crawler_stats.fort}\n"
        f"**Will:** {crawler.crawler_stats.will}\n\n"

        f"**Strength:** {crawler.crawler_stats.str} ({crawler.crawler_stats.str_mod})\n"
        f"**Agility:** {crawler.crawler_stats.agi} ({crawler.crawler_stats.agi_mod})\n"
        f"**Stamina:** {crawler.crawler_stats.sta} ({crawler.crawler_stats.sta_mod})\n"
        f"**Intelligence:** {crawler.crawler_stats.int} ({crawler.crawler_stats.int_mod})\n"
        f"**Personality:** {crawler.crawler_stats.per} ({crawler.crawler_stats.per_mod})\n"
        f"**Luck:** {crawler.crawler_stats.luc} ({crawler.crawler_stats.luc_mod})\n"
        f"**Luck Sign:** {crawler.crawler_stats.luck_sign}\n\n"

        f"## Notable Items:\n"
        f"{newline.join(f'- {item}' for item in crawler.crawler_items)}\n\n"
        
        
        f"## Bio:\n"
        f"**Alignment:** {crawler.crawler_bio.alignment}\n" 
        f"**Personality Traits:** {' - '.join(f'{trait}' for trait in crawler.crawler_bio.personality_traits)}\n"
        f"**Strengths:** {' - '.join(f'{strength}' for strength in crawler.crawler_bio.strengths)}\n"
        f"**Weaknesses:** {' - '.join(f'{weakness}' for weakness in crawler.crawler_bio.weaknesses)}\n"
        f"**Origin Story:**\n"
        f"{crawler.crawler_bio.origin}\n"
        f"**Journey So Far:**\n"
        f"{crawler.crawler_bio.story}\n"
        f"**Twist:**\n"
        f"{crawler.crawler_bio.twist}\n\n"


        f"## Special Abilities:\n"
        f"{newline.join(f'- {ability}' for ability in crawler.crawler_bio.abilities)}\n"
    )
    return markdown_content