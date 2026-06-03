def get_starting_gear(char_class):
    gear = {
        "Warrior": ["Iron Sword", "Shield"],
        "Mage": ["Staff", "Mana Potion"],
        "Rogue": ["Daggers", "Smoke Bomb"]
    }
    return gear.get(char_class, ["Ragged Clothes"])