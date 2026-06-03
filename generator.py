# RPG Character Generator
def main():
print("--- Welcome to the Character Generator ---")
# Components will be combined here
name = "Hero"
print(f"\nCharacter {name} has been successfully created!")
if __name__ == "__main__":
main()





def get_starting_gear(char_class):
    gear = {
        "Warrior": ["Iron Sword", "Shield"],
        "Mage": ["Staff", "Mana Potion"],
        "Rogue": ["Daggers", "Smoke Bomb"]
    }
    return gear.get(char_class, ["Ragged Clothes"])