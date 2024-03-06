from classes.crawler import Crawler
from markdown import generate_markdown
from prompts.input import get_input, get_class_input
from randomizers.random_level import random_level

def main():
    num_crawlers = get_input("How many crawlers? ", int, 1)
    
    for _ in range(num_crawlers):
        crawler_name = get_input("What should we call this crawler?", str, "Crawler")
        
        class_choice = get_class_input()
        
        min_level = get_input("What is the minimum level for your crawler? (leave empty for 1)", int, 1)
        max_level = get_input("What is the maximum level for your crawler? (leave empty for 10)", int, 10)
        level = random_level(min_level, max_level)

        generate_markdown(Crawler(crawler_name, class_choice, level))
