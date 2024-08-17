import os

# File to store the user's name
NAME_FILE = 'user_name.txt'

def get_name_from_file():
    """Read the user's name from a file."""
    if os.path.exists(NAME_FILE):
        with open(NAME_FILE, 'r') as file:
            return file.read().strip()
    return None

def save_name_to_file(name):
    """Save the user's name to a file."""
    with open(NAME_FILE, 'w') as file:
        file.write(name)

def chat():
    """Chat function to interact with the user."""
    name = get_name_from_file()
    
    if name:
        print(f"Welcome back, {name}!")
    else:
        name = input("Hi! What’s your name? ")
        save_name_to_file(name)
        print(f"Nice to meet you, {name}!")
    
    while True:
        user_input = input(f"{name}, how can I assist you today? (type 'quit' to exit) ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            print("I'm here to help!")

# Run the chatbot
if __name__ == "__main__":
    chat()
