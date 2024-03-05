from prompts.input import get_input, get_class_input

def main():
    num_crawlers = int(input("How many crawlers? "))
    
    #Escape check for non-integers

    for i in range(num_crawlers):
        class_choice = get_class_input()
        min_level = get_input("What is the minimum level for your crawler? (leave empty for 1)", int, 1)
        max_level = get_input("What is the maximum level for your crawler? (leave empty for 10)", int, 10)
        
        
