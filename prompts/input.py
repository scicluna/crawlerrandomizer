from randomizers.random_class import random_class
import names

def get_input(prompt: str, type=str, default=None) -> any:
    """Prompts the user for an input of specified type. Returns the default if the input is empty."""
    while True:
        input_value = input(prompt)
        
        if input_value == "":
            return default
        try: 
            return type(input_value)
        except ValueError:
            print(f"Invalid input, please enter a value of type {type.__name__}.")

def get_class_input() -> str:
    """Prompts the user for a class input. Returns a random class if the input is empty."""
    while True:
        input_value = input("What class is this crawler? (leave empty for random)")

        if input_value == "":
            return random_class()
        
        try:
            return str(input_value)
        except ValueError:
            print(f"Invalid input, please enter a string that represents your class name")

def get_name_input() -> str:
    """Prompts the user for a name input. Returns a random name if the input is empty."""
    while True:
        input_value = input("What is the name of your crawler? (leave empty for random)")

        if input_value == "":
            return names.get_full_name()
        
        try:
            return str(input_value)
        except ValueError:
            print(f"Invalid input, please enter a string that represents your crawler's name")