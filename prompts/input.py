from randomizers.random_class import random_class

def get_input(prompt, type=str, default=None):
    """Prompts the user for an input of specified type. Returns the default if the input is empty."""
    
    while True:
        input_value = input(prompt)
        
        if input_value == "":
            return default
        try: 
            return type(input_value)
        except ValueError:
            print(f"Invalid input, please enter a value of type {type.__name__}.")

def get_class_input():
    """Prompts the user for a class input. Returns a random class if the input is empty."""

    while True:
        input_value = input("What class is this crawler? (leave empty for random)")

        if input_value == "":
            return random_class()
        
        try:
            return str(input_value)
        except ValueError:
            print(f"Invalid input, please enter a string that represents your class name")