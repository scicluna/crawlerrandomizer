import random
from classes.crawler import Crawler
from markdown import save_crawler_profile
from prompts.input import get_input, get_class_input, get_name_input
from randomizers.random_level import random_level


def main():
    num_crawlers = get_input("How many crawlers? (leave empty for 1)", int, 1)
    
    for _ in range(num_crawlers):
        crawler_name = get_name_input()
        class_choice = get_class_input()
        min_level = get_input("What is the minimum level for your crawler? (leave empty for 1)", int, 1)
        max_level = get_input("What is the maximum level for your crawler? (leave empty for 1)", int, 1)
        crawler_skill = get_input("How skilled is your crawler on a rank from 1-10?", int, 5)
        ai_detailed = get_input("Do you want more detailed AI? y/n (leave empty for n)", str, "n")
        level = random_level(min_level, max_level)

        crawler = Crawler(crawler_name, class_choice, ai_detailed, crawler_skill, level )
        save_crawler_profile(crawler, f"{crawler.crawler_name}_{max(random.randint(1,20) - random.randint(1,10), 1)}.md")

if __name__ == "__main__":
    main()