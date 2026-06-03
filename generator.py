def choose_class():
classes = ["Warrior", "Mage", "Rogue"]
print("Available Classes:", ", ".join(classes))

def main():
print("--- Welcome to the Character Generator ---")
name = input("Enter character name: ")
char_class = choose_class() # Added by Person B
print(f"\nCharacter {name} the {char_class} has been created!")